"""
친구들로부터 천재 프로그래머로 불리는 프로도는 음악을 하는 친구로부터 자신이 좋아하는 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 궁금하니 프로그램으로 개발해 달라는 제안을 받았습니다. 그 제안 사항 중, 키워드는 와일드카드 문자중 하나인 '?'가 포함된 패턴 형태의 문자열을 뜻합니다. 와일드카드 문자인 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정합니다. 예를 들어 "fro??"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는 매치되지 않습니다.

가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때, 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해 주세요.

가사 단어 제한사항

words의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
전체 가사 단어 길이의 합은 2 이상 1,000,000 이하입니다.
가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공됩니다.
각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
검색 키워드 제한사항

queries의 길이(검색 키워드 개수)는 2 이상 100,000 이하입니다.
각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하입니다.
검색 키워드는 중복될 수도 있습니다.
각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 '?' 로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며, '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.
예를 들어 "??odo", "fro??", "?????"는 가능한 키워드입니다.
반면에 "frodo"('?'가 없음), "fr?do"('?'가 중간에 있음), "?ro??"('?'가 양쪽에 있음)는 불가능한 키워드입니다.
입출력 예

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = [3, 2, 4, 1, 0]
입출력 예에 대한 설명

"fro??"는 "frodo", "front", "frost"에 매치되므로 3입니다.
"????o"는 "frodo", "kakao"에 매치되므로 2입니다.
"fr???"는 "frodo", "front", "frost", "frame"에 매치되므로 4입니다.
"fro???"는 "frozen"에 매치되므로 1입니다.
"pro?"는 매치되는 가사 단어가 없으므로 0 입니다.
"""

# def solution(words, queries):
#     answer = []
#
#     for q in queries:
#         same_idx = [idx for idx in range(len(q)) if q[idx] != '?']
#
#         ck = []
#         for w in words:
#             if len(w) == len(q):
#                 if w[min(same_idx):max(same_idx)+1] == q[min(same_idx):max(same_idx)+1]:
#                     ck.append(w)
#         answer.append(len(ck))
#
#     return answer
#
#
# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# print(solution(words, queries))
class Node:
    def __init__(self, key):
        self.key = key
        self.child = dict()
        self.count_leaf = 0


class Trie:
    def __init__(self):
        self.head = Node(None)
        self.word_count = 0

    def insert(self, word):
        curr = self.head

        for c in word:
            if c not in curr.child:
                curr.child[c] = Node(c)
            curr = curr.child[c]
            curr.count_leaf += 1

        curr.child['*'] = True
        self.word_count += 1

    def count_match(self, word):
        curr = self.head
        match_fail = False

        for c in word:
            if c != '?':
                if c not in curr.child:
                    match_fail = True
                    break
                curr = curr.child[c]
            else:
                return curr.count_leaf  # Case1: 와일드카드 매치

            if match_fail is True:
                return 0  # Case2: 단어 매치가 없음

        return 1  # Case3: 단어 매치


def solution(words, queries):
    tries = dict()
    inv_tries = dict()

    for word in words:
        word_len = len(word)

        if word_len not in tries:
            tries[word_len] = Trie()
            inv_tries[word_len] = Trie()

        tries[word_len].insert(word)
        inv_tries[word_len].insert(word[::-1])

    answer = list()
    for query in queries:
        query_len = len(query)
        if query_len not in tries:
            answer.append(0)  # Case1: 해당 길이의 단어가 없음
        elif query.count('?') == query_len:
            answer.append(tries[query_len].word_count)  # Case2: 전체 와일드카드
        elif query[0] == '?':
            answer.append(inv_tries[query_len].count_match(query[::-1]))  # Case3: 전위 와일드카드
        else:
            answer.append(tries[query_len].count_match(query))  # Case4: 후위 와일드카드 or 단어 매칭

    return answer
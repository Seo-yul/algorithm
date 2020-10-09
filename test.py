import pymongo


class USER_INFO(object):

    _instance = None
    # 몽고디비연결
    client = pymongo.MongoClient('mongodb+srv://reso:1q2w3e4r@reso.ympo0.mongodb.net/school_meal?retryWrites=true&w=majority')
    # collection 생성
    database = client['school_meal']['user_info']

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def get_user_info_from_collection(cls, *_query):
        assert cls.database
        return cls.database.find(_query[0], _query[1])

    @classmethod
    def add_user_info_to_collection(cls, _data):
        if type(_data) is list:
            return cls.database.insert_many(_data)
        else:
            return cls.database.insert_one(_data)

    @classmethod
    def update_user_info_to_collection(cls, *_query):
        assert cls.database
        return cls.database.update_one(_query[0], _query[1])


sql_query_0 = {'user_id': '154387'}
sql_query_1 = {'_id':0}
result_dict = USER_INFO.get_user_info_from_collection(sql_query_0, sql_query_1)
print(list(result_dict))
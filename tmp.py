import tempfile


def print_tmp():
    """
    Support

        $ cd `tmp`

    """
    print(tmp())


def tmp():
    """
    Create temp dir
    """
    return tempfile.mkdtemp()


if __name__ == '__main__':
    print_tmp()


'''
from requests import get

ip = get('https://api.ipify.org').text
print('My public IP address is:', ip)
'''
import requests
from operator import itemgetter


def main():
    url = 'http://137.116.169.76:5000/find_similar'
    files = {'file': open('/home/jack/Downloads/rest_mat.png', 'rb')}

    response = requests.post(url, files=files)

    data = response.json()

    print('raw:', data)

    data = sorted(data, key=itemgetter(1), reverse=True)

    print('sorted:', data)

    for item in data:
        print(item[0])


if __name__ == "__main__":
    main()
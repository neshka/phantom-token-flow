import requests

RESOURCE_SERVER = 'http://localhost:5002/resource'


def access_resource():
    phantom_token = 'valid_phantom_token'
    headers = {'Authorization': phantom_token}
    response = requests.get(RESOURCE_SERVER, headers=headers)
    print(response.text)


if __name__ == '__main__':
    access_resource()

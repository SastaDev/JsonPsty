try:
    import requests
    import json
except Exception as e:
    if e == 'No module named \'requests\'':
        print('The following module requests is not installed.\nInstall it and try again later.')
    elif e == 'No module named \'json\'':
        print('The following module json is not installed.\nInstall it and try again later.')
    else:
        print(f'ERROR: {e}')

class JsonPstyClient:
    def __init__(self, api_key):
        headers = {'Api-Key': str(api_key), 'Content-Type': 'application/json'}
        r = requests.get('https://json.psty.io/api_v1/all_stores', headers=headers)
        if r.status_code == 200:
            self.headers = {'Api-Key': str(api_key), 'Content-Type': 'application/json'}
        elif r.status_code == 403:
            print('Invalid api key.')
            return
        else:
            print(f'ERROR: {r.content.decode()}')
            return

    def getStore(self, store_name):
        r = requests.get(f'https://json.psty.io/api_v1/stores/{store_name}', headers=self.headers)
        if r.status_code == 200:
            return r.json()['data']
        elif r.status_code == 403:
            print('Invalid api key.')
            return
        else:
            print(f'ERROR: {r.content.decode()}')
            return

    def createStore(self, store_name, *data):
        data = {'store_name': str(store_name), 'data': data}
        r = requests.post('https://json.psty.io/api_v1/create', headers=self.headers, data=json.dumps(data))
        if r.status_code == 200:
            return f'Created store: {store_name}'
        elif r.status_code == 403:
            print('Invalid api key.')
            return
        else:
            print(f'ERROR: {r.content.decode()}')
            return

    def updateStore(self, store_name, data):
        r = requests.put(f'https://json.psty.io/api_v1/stores/{store_name}', headers=self.headers, data=json.dumps(data))
        if r.status_code == 200:
            return f'Updated store: {store_name}'
        elif r.status_code == 403:
            print('Invalid api key.')
            return
        else:
            print(f'ERROR: {r.content.decode()}')
            return

    def deleteStore(self, store_name):
        r = requests.delete(f'https://json.psty.io/api_v1/stores/{store_name}', headers=self.headers)
        if r.status_code == 200:
            return f'Deleted store: {store_name}'
        elif r.status_code == 403:
            print('Invalid api key.')
            return
        else:
            print(f'ERROR: {r.content.decode()}')
            return

    def getAllStores(self):
        headers = {'Api-Key': str(self.headers['Api-Key'])}
        r = requests.get('https://json.psty.io/api_v1/all_stores', headers=headers)
        if r.status_code == 200:
            return r.json()
        elif r.status_code == 403:
            print('Invalid api key.')
            return
        else:
            print(f'ERROR: {r.content.decode()}')
            return

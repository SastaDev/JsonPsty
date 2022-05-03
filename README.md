# JsonPsty

A wrapper for <a href='https://json.psty.io'>json.psty.io</a>
Use it as storing things, or as database.

<p><b>Orginal site:</b> https://json.psty.io</p>
<p><b>Original documention:</b> https://json.psty.io/api_documentation</p>

<h5>Current/Latest Version: 1.0 (03 May, 2022 || 03:54 PM)</h5>

# Generating Api-Key
Go to https://json.psty.io and login or sign up, and then go to bottom part of https://json.psty.io/account and take your api-key from there.

# Examples
Check this [`examples.py`](https://github.com/SastaDev/JsonPsty/blob/main/examples.py) for all available methods and their examples.

# Initializing Client
```py
from jsonpsty import JsonPstyClient

api_key = '' # Take your Api-Key from https://json.psty.io/signup

client = JsonPstyClient(api_key=api_key)
```

# Available Methods
<h4>Getting A Single Store</h4>
```py
get_store = client.getStore('lang')
print(get_store)
```

<h4>Creating A Single Store</h4>
```py
create_store = client.createStore('store_name')
print(create_store)
```

<h4>Updating A Single Store<\h4>
```py
update_store = client.updateStore('lang', data={"key": "value"})
print(update_store)
```

<h4>Deleting A Store</h4>
```py
delete_store = client.deleteStore('store_name')
print(delete_store)
```

<h4>Getting All Stores</h4>
```py
get_all_stores = client.getAllStores()
print(get_all_stores)
```


# Last Words
For more help, queries, contact us on our Telegram Group.
<b>Link:</b> https://telegram.dog/HelpSupportChat

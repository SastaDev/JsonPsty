from jsonpsty import JsonPstyClient

api_key = '' # Take your Api-Key from https://json.psty.io/signup

client = JsonPstyClient(api_key=api_key)

# Getting a single store.
get_store = client.getStore('lang')
print(get_store)

# Creating a single store
create_store = client.createStore('store_name')
print(create_store)

# Updating a single store
update_store = client.updateStore('lang', data={"key": "value"})
print(update_store)

# Deleting a single store
delete_store = client.deleteStore('store_name')
print(delete_store)

# Getting all stores
get_all_stores = client.getAllStores()
print(get_all_stores)
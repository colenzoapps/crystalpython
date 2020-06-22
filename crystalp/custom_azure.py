from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'payplusfileshare'
    account_key = 'JtzCknKz4pvL88EfzvoqWivPq+gFNC/Ttn0jC3qmDbea8WsplpE0kRWWP6CYpRijdC9EVaE8vz6tbP25u14beA=='
    azure_container = 'dctpython'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'payplusfileshare'
    account_key = 'JtzCknKz4pvL88EfzvoqWivPq+gFNC/Ttn0jC3qmDbea8WsplpE0kRWWP6CYpRijdC9EVaE8vz6tbP25u14beA==' 
    azure_container = 'static'
    expiration_secs = None
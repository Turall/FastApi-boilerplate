import os


envsettings = os.getenv("settings")

if envsettings is None:
    raise Exception("settings for app not exported. example:  ```export settings=dev```")

if envsettings == "dev" or envsettings == "default":
    from core.settings.devsettings import DevSettings
    settings = DevSettings()

elif envsettings == "prod":
    from core.settings.prodsettings import ProdSettings
    settings= ProdSettings()
    
else:
    from core.settings.settings import BaseConfig
    settings = BaseConfig()




import os

from app import create_app

print("\n\n")
print("################################")
print("########## APP SETUP ###########")
print("################################")
print("\n\n")

config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = create_app(config_name)

print("\n\n")
print("################################")
print("########## APP READY ###########")
print("################################")
print("\n\n")

if __name__ == '__main__':
    app.run()

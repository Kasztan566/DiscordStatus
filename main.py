from pypresence import Presence
import time
import Config

config = Config.Config('config.json')
ico = config.read()['image']
i2 = config.read()['name']
i = config.read()['description']
client_id = config.read()['id']
RPC = Presence(client_id)
RPC.connect()

RPC.update(state=i, details=i2, large_image=ico)
while True:
    time.sleep(15)
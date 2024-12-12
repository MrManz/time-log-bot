import factorio_rcon
from dotenv import load_dotenv
import os

load_dotenv()
ip = os.getenv('IP')
rcon_password = os.getenv('RCON_PASSWORD')

while True:
    client = factorio_rcon.RCONClient(ip, 27015, rcon_password)
    response = client.send_command("/players online")
    print(response)



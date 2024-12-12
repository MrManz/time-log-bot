import factorio_rcon
from dotenv import load_dotenv
import os
from flask import Flask, render_template

load_dotenv()
ip = os.getenv('IP')
rcon_password = os.getenv('RCON_PASSWORD')
client = factorio_rcon.RCONClient(ip, 27015, rcon_password)

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = client.send_command("/players online")
    response = response.replace("(online)"," ")
    response = response.split("\n")
    return render_template('player_template', text=response)

    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)



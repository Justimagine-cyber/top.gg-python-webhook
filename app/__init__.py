import json
from quart import Quart, request
import aiohttp


app = Quart(__name__)

@app.route('/')
async def index():
  return {'webhook': 'rocks'}

@app.route('/topgg/', methods=["POST"])
async def topgg():
  authorization = request.headers['Authorization']
  
  if (authorization != 'imaginedisveryepicmydude'):
    print('Unauthorized')
    return {'error': '401 Unauthorized'}
  webhook = 'https://discord.com/api/webhooks/863266244164714506/PQa3YaT7CDsbRycIt0dmNXkY5OotWs-dVPMXPac4z_0LYJxOReP1U5YW9EmGcyW7Pi_d'
  data = json.loads(await request.data)
  webhook_data = {
                "username": "Top.gg Imagined",
                "avatar_url": "https://i2.paste.pics/D8YTI.png",
                "content": f"**__User: {data['user']}, voted on top.gg!__**"
   }
  
  async with aiohttp.ClientSession() as session:
    async with session.post(webhook, data=webhook_data) as rsponse:
      pass
     
  return data
import telethon
import re

app_api_id = ''
app_api_hash = ''
tg_btc_bot_username = ''

client = telethon.TelegramClient('Pizder', app_api_id, app_api_hash)
client.start()


@client.on(telethon.events.NewMessage())
async def handler(event):
  message = event.to_dict()['message'].text
  if re.search(r'BTC_CHANGE_BOT\?start=', message):
    m = re.search(r'c_\S+', message)
    await client.send_message(tg_btc_bot_username, '/start ' + m.group(0).replace('`', ''))

client.run_until_disconnected()

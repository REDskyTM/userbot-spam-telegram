from pyrogram import Client, filters
import random
import json
from colorama import init, Fore
init()

print(Fore.YELLOW + """
╔══╗╔══╗╔══╗╔╗──╔╗╔═══╗╔═══╗
║╔═╝║╔╗║║╔╗║║║──║║║╔══╝║╔═╗║
║║──║║║║║╚╝║║╚╗╔╝║║╚══╗║╚═╝║
║║──║║║║║╔╗║║╔╗╔╗║║╔══╝║╔══╝
║╚═╗║║║║║║║║║║╚╝║║║╚══╗║║
╚══╝╚╝╚╝╚╝╚╝╚╝──╚╝╚═══╝╚╝
╔════╗╔══╗
╚═╗╔═╝║╔═╝
──║║──║║
──║║──║║
──║║──║║
──╚╝──╚╝
╔══╗╔════╗──╔═══╗╔╗╔╗╔═══╗╔╗╔╗╔══╗╔╗╩╔╗
║╔╗║╚═╗╔═╝──╚══╗║║║║║║╔══╝║║║║║╔╗║║║─║║
║║║║──║║─────╔═╝║║╚╝║║╚══╗║╚╝║║║║║║║─║║
║║║║──║║─────╚═╗║╚═╗║║╔═╗║║╔╗║║║║║║║─╔║
║╚╝║──║║────╔══╝║─╔╝║║╚═╝║║║║║║╚╝║║╚═╝║
╚══╝──╚╝────╚═══╝─╚═╝╚═══╝╚╝╚╝╚══╝╚═══╝
╔══╗╔╗╔╗╔═══╗╔════╗╔╗╔══╗╔╗╔╗
║╔═╝║║║║║╔══╝╚═╗╔═╝║║║╔═╝║║║║
║║──║╚╝║║╚══╗──║║──║╚╝║──║║║║
║║──╚═╗║║╔══╝──║║──║╔╗║──║║╔║
║╚═╗──║║║╚══╗──║║──║║║╚═╗║╚╝║
╚══╝──╚╝╚═══╝──╚╝──╚╝╚══╝╚══╝
	""")

print("Вам нужно получить api_id, api_hash. Перейдите на страницу my.telegram.org и авторизируйтесь, дальше кликните на API development tools")

text_file = open("apiid.txt", "w")
apiid = input('Вставьте ваш api_id:')
text_file.write(apiid)
text_file.close()

text_file = open("apihash.txt", "w")
apihash = input('Вставьте ваш api_hash:')
text_file.write(apihash)
text_file.close()

with open('apiid.txt') as f:
    contents = f.read()

with open('apihash.txt') as f:
    contentss = f.read()

app = Client(
	"my_account",
	api_id = contents,
	api_hash = contentss
	)

@app.on_message(filters.me & filters.command("spam", "."))
async def lol_cmd(app, msg):
	for i in range(350):
		text = msg.text.split(maxsplit=1)[1]
		await msg.reply(text)

app.run()
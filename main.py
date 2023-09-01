# This example requires the 'voice_states' intent.
import discord
from discord.ext import tasks
from asyncio import sleep
from random import randint

with open("bing","r") as bing:
	token = bing.readline()

heypikmin = open("sounds/pikmin.raw","rb")
pikminwoo = open("sounds/pikminwoo.raw","rb")

#opus :]
discord.opus.load_opus("libopus.so.0")
if discord.opus.is_loaded():
	print("WE BALL!!!")
#opus :[

bingung = False

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')

	pikmin = client.get_guild(903236631958548501).get_member(client.user.id)
	olimar = client.get_guild(903236631958548501).get_member(616228691155877898)
	server = client.get_guild(903236631958548501)

	if olimar.voice != None:
		await sleep(randint(128,1024))
		await olimar.voice.channel.connect(reconnect=False)
		#server.voice_client.play(discord.PCMAudio(heypikmin))

	resurrection.start(bingung, heypikmin)

@client.event
async def on_voice_state_update(member, before, after):

	pikmin = client.get_guild(903236631958548501).get_member(client.user.id)
	olimar = client.get_guild(903236631958548501).get_member(616228691155877898)
	server = client.get_guild(903236631958548501)

	if member == olimar:
		if after.channel == None:
			await server.voice_client.disconnect(force=True)
		if before.channel == None:
			await after.connect(reconnect=False)

	if member == pikmin:


		if after.channel == None:
			await server.voice_client.disconnect(force=True)
		else:
			if after.deaf == True:
				await sleep(0.25)
				await sleep(2)
				server.voice_client.play(discord.FFmpegOpusAudio("http://localhost:1984", options="-filter:a \"volume=0.12\""))
			else:
				if after.channel != before.channel:
					heypikmin = open("sounds/pikmin.raw","rb")
					await sleep(2)
					server.voice_client.play(discord.PCMAudio(heypikmin))

				if pikmin.voice.mute == True:
					pikminwoo = open("sounds/pikminwoo.raw","rb")
					await pikmin.edit(mute=False)
					server.voice_client.play(discord.PCMAudio(pikminwoo))
		
		#if before.deaf == False:
		#	if after.deaf == True:
		#		server.voice_client.play(discord.FFmpegPCMAudio("http://localhost:1984", options="-filter:a \"volume=0.12\""))
				#server.voice_client.play(discord.FFmpegPCMAudio("http://localhost:1984"))

		if before.deaf == True:
			if after.deaf == False:
				server.voice_client.stop()
	"""
	print(member.id)
	print(member)
	print(after)
	if member == pikmin:
		if after == None:
			if olimar.voice != None:
				await server.voice_client.disconnect(force=True)
				await sleep(5)
				await olimar.voice.channel.connect(reconnect=True)
				#await sleep(1)
				#await server.change_voice_state(channel=olimar.voice.channel)
				#print("bing")
				#print(pikmin.voice)
				#await olimar.voice.channel.connect(reconnect=True,timeout=1)
				#await sleep(2)
	""""""
	print("member")
	print(member)
	print("before")
	print(before)
	print("after")
	print(after)
	print("pikminvoice:")
	print(pikmin.voice.channel)
	print("olimarvoice:")
	print(olimar.voice.channel)
	print("----")
	"""
	if olimar.voice == None:
		if pikmin.voice != None:
			await server.voice_client.disconnect()

	if olimar.voice != None:
		if pikmin.voice != None:
			if pikmin.voice.channel != olimar.voice.channel:
				await server.voice_client.move_to(channel=olimar.voice.channel)
		#else:
			#await olimar.voice.channel.connect(reconnect=True)

@client.event
async def on_member_update(before, after):
	if client.get_guild(903236631958548501).get_member(client.user.id).nick != "pikmin :]":
		if client.get_guild(903236631958548501).get_member(client.user.id).nick != "yellow pikmin :]":
			await client.get_guild(903236631958548501).get_member(client.user.id).edit(nick="pikmin :]")
	else:
		pass

@tasks.loop(seconds = 2)
async def resurrection(bingung, heypikmin):
	try:
		if client.get_guild(903236631958548501).get_member(client.user.id).voice == None:
			if bingung == False:
				bingung = True
			if bingung == True:
				if client.get_guild(903236631958548501).get_member(616228691155877898).voice != None:
					await client.get_guild(903236631958548501).get_member(616228691155877898).voice.channel.connect(reconnect=False,timeout=3)
	except Exception as e:
		pass

# PAST ME: genuinely cant implement this part
#	FUTURE ME:  I WAS A FOOL
#		else:
#			await server.voice_client.disconnect()

"""
@client.event
async def on_voice_state_update(member, before, after):
	#if not before.channel and after.channel and member.id == 616228691155877898:
	if after.channel != before.channel and member.id == 616228691155877898:
		#print("yeah!!")
		  # print(client.get_guild(952442339509551124).get_member(client.user.id))
		   # print(client.get_guild(952442339509551124).get_member(client.user.id).voice.channel)

		if client.get_guild(903236631958548501).get_member(client.user.id).voice != None:
			if client.get_guild(903236631958548501).get_member(client.user.id).voice.channel != after.channel:
				await client.get_guild(903236631958548501).voice_client.move_to(channel=client.get_channel(after.channel.id))
				client.get_guild(903236631958548501).voice_client.play(discord.PCMAudio(heypikmin))
		else:
			await after.channel.connect(reconnect=True)
			client.get_guild(903236631958548501).voice_client.play(discord.PCMAudio(heypikmin))

	if member.id == client.user.id:
		if client.get_guild(903236631958548501).get_member(client.user.id).voice == None:
			if client.get_guild(903236631958548501).get_member(616228691155877898).voice != None:
				await client.get_guild(903236631958548501).get_member(616228691155877898).voice.channel.connect(reconnect=True)
				client.get_guild(903236631958548501).voice_client.play(discord.PCMAudio(heypikmin))

			else:
				pass
		else:
			if client.get_guild(903236631958548501).get_member(616228691155877898).voice != None:
				if client.get_guild(903236631958548501).get_member(client.user.id).voice.channel != client.get_guild(903236631958548501).get_member(616228691155877898).voice.channel:
					await client.get_guild(903236631958548501).voice_client.move_to(channel=client.get_guild(903236631958548501).get_member(616228691155877898).voice.channel)
					#await client.get_guild(903236631958548501).get_member(616228691155877898).voice.channel.connect(reconnect=True)
					client.get_guild(903236631958548501).voice_client.play(discord.PCMAudio(heypikmin))

	#print(before.channel)
	#print(after.channel)
	#print("-")

@client.event
async def on_message(message):
	if "pikmin" in message.content:
		if client.get_guild(903236631958548501).get_member(616228691155877898).voice != None:
			await client.get_guild(903236631958548501).get_member(616228691155877898).voice.channel.connect(reconnect=True)
			client.get_guild(903236631958548501).voice_client.play(discord.PCMAudio(heypikmin))
"""

@client.event
async def on_message(message):
	if "pikmin" in message.content:
		if message.author.id == client.user.id:
			if message.channel.type = "private":
				await message.reply("pikmin :]")
			else:
				pass
		else:

		#if message.author.id == 616228691155877898:
		#client.get_guild(903236631958548501).voice_client.stop()
		#heypikmin = open("sounds/pikmin.raw","rb")
		#client.get_guild(903236631958548501).voice_client.play(discord.PCMAudio(heypikmin))
			await message.reply("pikmin :]")

	if message.author.id == 431809762024488960:
		if randint(1,5) == 1:
			await message.channel.send("pikmin :]")

	if message.author.id == 769632057575342081:
		if randint(1,50) == 1:
			await message.channel.send("pikmin :]")
	
	if "https://www.youtube.com/watch?v=bbmSBLaZ6Ps" in message.content:
		await message.delete()

	#if "bingungppp" in message.content:
	#	msg = await client.get_channel(928950243041615892).fetch_message(1145350761253961769)
	#	print(msg)
	#	print(msg.content)
	#	await msg.delete()


@client.event
async def on_member_update(before, after):
	benjamin = await client.get_guild(903236631958548501).fetch_roles()
	for p in benjamin:
		if p.name == "benjamin":
		#	await p.delete(reason="no benjamin :[ -pikmin")
			for pp in p.members:
				if pp.id != 270983683723362304:
					await p.delete(reason="no benjamin :[ -pikmin")
					await sleep(1)
					ppp = await client.get_guild(903236631958548501).create_role(name="benjamin", hoist=True, reason="benjamin :] -pikmin")
					await client.get_guild(903236631958548501).get_member(270983683723362304).add_roles(ppp)
					await sleep(1)
					break
			break
"""
@client.event
async def on_message(message):
	if "bing" in message.content:
		guild = client.get_guild(903236631958548501)
		print(guild.get_member(616228691155877898).voice)
	if "bong" in message.content:
		print(message.content)
		print(message.content[5:])
		boong = client.get_channel(int(message.content[5:]))
		await boong.connect(reconnect=True)
"""
client.run(token)

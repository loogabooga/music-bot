# This example requires the 'voice_states' intent.
import discord
from asyncio import sleep

with open("bing","r") as bing:
	token = bing.readline()

heypikmin = open("sounds/pikmin.raw","rb")


intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

def status(p, pp):
	return client.get_guild(p).get_member(pp).voice

@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')
	if client.get_guild(903236631958548501).get_member(616228691155877898).voice != None:
		await client.get_guild(903236631958548501).get_member(616228691155877898).voice.channel.connect(reconnect=True)
		client.get_guild(903236631958548501).voice_client.play(discord.PCMAudio(heypikmin))

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

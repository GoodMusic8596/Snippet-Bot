import json
import discord
from discord.ext import commands
import os
openf=open("snippets.json","r+")
f=json.load(openf)
client = commands.Bot(command_prefix="s!")


@client.command()
async def snippet(ctx,snippet:str):
	try:
		var=str(f[snippet]["css"][0])
		await ctx.send("```css\n"+var+"```")
	except:
		await ctx.send(snippet+" doesn't exist!")

@client.command()
async def invite(ctx):
	await ctx.send("https://discord.com/oauth2/authorize?client_id=916189103832317972&scope=bot&permissions=68608")
openg=open("config.json","r+")
g=json.load(openg)
client.run(openg["token"])
from nextcord.ext import commands
bot = commands.Bot(command_prefix='$')
# Order food
# very basic currently
@bot.command()
async def order(ctx, *args):
	order = " ".join(args)
	await ctx.send(f'You ordered {order}!')

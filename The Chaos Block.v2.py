from bedrock.server import Server
import asyncio
import random

app = Server()

@app.server_event
async def ready(ctx):
    print("Python Bridge is Active! Move in game to trigger the build!")

@app.game_event
async def block_broken(ctx):
    roll = random.randint(1,4)
    if roll == 1:
        await ctx.server.run("fill ~ ~2 ~ ~ ~7 ~ diamond_block")
    elif roll == 2:
        await ctx.server.run("summon zombie ~ ~ ~")
        await ctx.server.run("summon zombie ~ ~ ~")
        await ctx.server.run("summon zombie ~ ~ ~")
        await ctx.server.run("summon zombie ~ ~ ~")
        await ctx.server.run("summon zombie ~ ~ ~")
        await ctx.server.run("summon zombie ~ ~ ~")
        await ctx.server.run("summon zombie ~ ~ ~")
        await ctx.server.run("summon zombie ~ ~ ~")
        await ctx.server.run("summon zombie ~ ~ ~")
        await ctx.server.run("summon zombie ~ ~ ~")
    elif roll == 3:
        await ctx.server.run("effect @s levitation 10 1 true")
    elif roll == 4:
        await ctx.server.run("effect @s slow_falling 10 255 true")

if __name__ == "__main__":
     app.start("localhost", 3847)
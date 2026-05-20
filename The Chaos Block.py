from bedrock.server import Server
import asyncio
import random

app = Server()

@app.server_event
async def ready(ctx):
    print("Python Bridge is Active! Move in game to trigger the build!")

@app.game_event
async def block_broken(ctx):
    roll = random.randint(1,6)
    if roll == 1:
        await ctx.server.run("fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 emerald_block")
    elif roll == 2:
        await ctx.server.run("fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 diamond_block")
    elif roll == 3:
        await ctx.server.run("fill ~ ~2 ~ ~ ~2 ~ gold_block")
    elif roll == 4:
        await ctx.server.run("fill ~ ~-1 ~ ~ ~-1 ~ iron_block")
    elif roll == 5:
        await ctx.server.run("fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 glass")
    elif roll == 6:
        await ctx.server.run("fill ~-2 ~-2 ~-2 ~2 ~2 ~2 obsidian hollow")
if __name__ == "__main__":
     app.start("localhost", 6666)
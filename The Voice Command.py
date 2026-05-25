from bedrock.server import Server
import asyncio
import random

app = Server()

@app.server_event
async def ready(ctx):
    print("Python Bridge is Active! Move in game to trigger the build!")

@app.game_event
async def player_message(ctx):
    message = ctx.message
    if message =="house":
        await ctx.server.run("fill ~-2 ~-2 ~-2 ~2 ~2 ~2 obsidian hollow")
    if message == "tower":
        # Build the tower walls
        await ctx.server.run("fill ~-2 ~ ~-2 ~2 ~10 ~2 stone hollow")
        await ctx.server.run("fill ~-3 10 ~-3 ~3 10 ~3 stone")
        # Clear interior at top
        await ctx.server.run("fill ~ ~10 ~ ~ ~10 ~ air")
        # Add ladder on one side
        await ctx.server.run("fill ~-2 ~1 ~3 ~-2 ~9 ~3 ladder[facing=south]")
        # Add door at base
        await ctx.server.run("setblock ~1 ~ ~-2 dark_oak_door[facing=south,half=lower]")
        await ctx.server.run("setblock ~1 ~1 ~-2 dark_oak_door[facing=south,half=upper]")
        # Add bed on the ground floor
        await ctx.server.run("setblock ~ ~1 ~-1 red_bed[facing=north,part=head]")
        await ctx.server.run("setblock ~ ~1 ~ red_bed[facing=north,part=foot]")
        # Add lanterns for lighting
        await ctx.server.run("setblock ~2 ~2 ~-1 lantern[hanging=false]")
        await ctx.server.run("setblock ~-2 ~5 ~-1 lantern[hanging=false]")
        await ctx.server.run("setblock ~ ~8 ~2 lantern[hanging=false]")
        # Add armor stand with netherite gear at top
        await ctx.server.run("summon armor_stand ~ ~11 ~ {ArmorItems:[{id:netherite_boots,Count:1},{id:netherite_leggings,Count:1},{id:netherite_chestplate,Count:1},{id:netherite_helmet,Count:1}],NoBasePlate:1}")
    elif message == "day":
        await ctx.server.run("time set day")
    elif message == "night":
        await ctx.server.run("time set night")
    elif message == "clear":
        await ctx.server.run("weather clear")



if __name__ == "__main__":
     app.start("localhost", 3847)
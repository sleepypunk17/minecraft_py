from bedrock.server import Server
import asyncio

app = Server()

@app.server_event
async def ready(ctx):
    print("Python Bridge is Active! Move in game to trigger the build!")

@app.game_event
async def player_travelled(ctx):
    # #This Fires every time you take a step in the game!
    # # print("player_travelled event fired!")
    # await ctx.server.run("fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 gold_block")
    # print(f"Placed gold at postion:X = {ctx.player_position[0].coord},Y = {ctx.player_position[1].coord}, Z = {ctx.player_position[2].coord}")
    for height in range(1,11):
        await ctx.server.run(f"setblock ~10 ~{height} ~10 diamond_block")

        await asyncio.sleep(0.1)
    

if __name__ == "__main__":
    app.start("localhost", 6666)
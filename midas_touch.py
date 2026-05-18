from bedrock.server import Server
import asyncio

app = Server()

@app.server_event
async def ready(ctx):
    print("Python Bridge is Active! Move in game to trigger the build!")

@app.game_event
async def player_travelled(ctx):
    #This Fires every time you take a step in the game!
    # print("player_travelled event fired!")
    await ctx.server.run("fill ~ ~-1 ~ ~ ~-1 ~ gold_block")
    print(f"Placed gold at postion:X = {ctx.player_postion[0].coord},1 Y = {ctx.player_postion[1].coord}, Z = {ctx.player_postion[2].coord}")
    

if __name__ == "__main__":
    app.start("localhost", 6666)
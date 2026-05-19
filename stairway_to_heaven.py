from bedrock.server import Server
import asyncio

app = Server()

@app.server_event
async def ready(ctx):
    print("Python Bridge is Active! Move in game to trigger the build!")

@app.game_event
async def player_travelled(ctx):
    for height in range(1,11):
        await ctx.server.run(f"setblock ~{height} ~{height} ~10 diamond_block")

        await asyncio.sleep(0.1)
    

if __name__ == "__main__":
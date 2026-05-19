from bedrock.server import Server
import asyncio

app = Server()

@app.server_event
async def ready(ctx):
    print("Python Bridge is Active! Move in game to trigger the build!")

@app.game_event
async def block_broken(ctx):
    await ctx.server.run("fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 glass")

if __name__ == "__main__":
     app.start("localhost", 6666)
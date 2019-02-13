import asyncio
import websockets

async def hatnote():
    async with websockets.connect("ws://wikimon.hatnote.com:9000") as ws:
        while True:
            event = await ws.recv()
            print(event)

asyncio.get_event_loop().run_until_complete(hatnote())

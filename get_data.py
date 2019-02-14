import asyncio
import json
import time
import websockets

async def hatnote(duration=1):

    data = []
    t_end = time.time() + duration

    async with websockets.connect("ws://wikimon.hatnote.com:9000") as ws:
        while time.time() < t_end:
            event = await ws.recv()
            event = json.loads(event)
            event["timestamp"] = time.time()

            data.append(event)
        
        return data

if __name__ == "__main__":

    print("Start timestamp: ", time.time())

    duration = 60 * 60 # 60 minutes in seconds

    data = asyncio.get_event_loop().run_until_complete(hatnote(duration))

    print("End timestamp: ", time.time())

    with open("output.json", "w") as outfile:  
        json.dump(data, outfile)
import time
import asyncio
from spade import quit_spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class DummyAgent(Agent):
    class MyBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour...")
            self.counter = 0
            
        async def run(self):
            print(f"Counter: {self.counter}")
            self.counter+=1
            await asyncio.sleep(1)
    async def setup(self):
        print("Agent starting...")
        b = self.MyBehav()
        self.add_behaviour(b)

if __name__ == "__main__":
    dummy = DummyAgent("taduma@jabber.cz", "@octo808")
    future = dummy.start()
    future.result()
    
    print("Wait until user interrupts with Ctrl+C")
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        print("Stopping")
    dummy.stop()
        
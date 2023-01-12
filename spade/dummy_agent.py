from spade import agent, quit_spade

class DummyAgent(agent.Agent):
    async def setup(self):
        print(f"Hello world, I am agent {str(self.jid)}")
    
dummy = DummyAgent("taduma@jabber.cz", "@octo808")
future = dummy.start()
future.result()

dummy.stop()
quit_spade()
    
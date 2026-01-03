class MessageBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event, agent):
        self.listeners.setdefault(event, []).append(agent)

    def publish(self, event, payload):
        for agent in self.listeners.get(event, []):
            agent.handle(event, payload)

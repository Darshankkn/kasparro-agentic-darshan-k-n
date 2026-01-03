class Agent:
    def __init__(self, name, bus):
        self.name = name
        self.bus = bus

    def subscribe(self, event):
        self.bus.subscribe(event, self)

    def handle(self, event, payload):
        raise NotImplementedError

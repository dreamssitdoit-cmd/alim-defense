from alim_defense.event_bus.event_bus import EventBus
from alim_defense.agents.registry import AgentRegistry
from alim_defense.pipeline.processor import PipelineProcessor


class CoreEngine:
    def __init__(self) -> None:
        self.bus = EventBus()
        self.registry = AgentRegistry()
        self.pipeline = PipelineProcessor(self.registry)

        print("alim-defense engine started")

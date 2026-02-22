from alim_defense.event_bus.event import Event
from alim_defense.agents.registry import AgentRegistry


class PipelineProcessor:
    def __init__(self, registry: AgentRegistry) -> None:
        self.registry = registry

    def process(self, event: Event) -> None:
        for agent in self.registry.all():
            agent.handle(event)


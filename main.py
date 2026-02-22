from alim_defense.engine.core_engine import CoreEngine
from alim_defense.event_bus.event import Event
from alim_defense.agents.base_agent import BaseAgent


class PrintAgent(BaseAgent):
    name = "print-agent"

    def handle(self, event: Event) -> None:
        print(f"[agent] received → {event.type} {event.data}")


def main():
    engine = CoreEngine()

    agent = PrintAgent()
    engine.registry.register(agent)

    event = Event(type="boot", data={"ok": True})
    engine.pipeline.process(event)


if __name__ == "__main__":
    main()

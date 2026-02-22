from abc import ABC, abstractmethod
from alim_defense.event_bus.event import Event


class BaseAgent(ABC):
    name: str

    @abstractmethod
    def handle(self, event: Event) -> None:
        ...

from typing import Callable, Dict, List
from .event import Event


Listener = Callable[[Event], None]


class EventBus:
    def __init__(self) -> None:
        self._listeners: Dict[str, List[Listener]] = {}

    def subscribe(self, event_type: str, listener: Listener) -> None:
        self._listeners.setdefault(event_type, []).append(listener)

    def emit(self, event: Event) -> None:
        for listener in self._listeners.get(event.type, []):
            listener(event)

from dataclasses import dataclass
from typing import Any, Dict

@dataclass(slots=True)
class Event:
    type: str
    data: Dict[str, Any]

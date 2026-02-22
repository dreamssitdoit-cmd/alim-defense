from typing import Dict, List
from .base_agent import BaseAgent


class AgentRegistry:
    def __init__(self) -> None:
        self._agents: Dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        self._agents[agent.name] = agent

    def all(self) -> List[BaseAgent]:
        return list(self._agents.values())

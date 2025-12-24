from abc import ABC, abstractmethod
from typing import List

class Agent(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass
    
    @abstractmethod
    def get_keywords(self) -> List[str]:
        pass
    
    @abstractmethod
    def handle(self, query: str) -> str:
        pass


class GitHubAgent(Agent):
    def get_name(self) -> str:
        return "GitHubAgent"
    
    def get_keywords(self) -> List[str]:
        return [
            "pull request", "pr", "github", "repository", "repo",
            "commit", "branch", "merge", "code review", "fork"
        ]
    
    def handle(self, query: str) -> str:
        return f"GitHubAgent: Processed query '{query}'."


class LinearAgent(Agent):
    def get_name(self) -> str:
        return "LinearAgent"
    
    def get_keywords(self) -> List[str]:
        return [
            "issue", "issues", "linear", "ticket", "task",
            "assigned", "bug", "feature", "project", "sprint"
        ]
    
    def handle(self, query: str) -> str:
        return f"LinearAgent: Processed query '{query}'."
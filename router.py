import logging
from typing import List, Optional
from agents import Agent

class QueryRouter:
    
    def __init__(self, agents: List[Agent]):
        self.agents = agents
        # Set up a logger to track what's happening
        self.logger = logging.getLogger(__name__)
    
    def route(self, query: str) -> str:
        if not query or not query.strip():
            return "Please provide a valid query."
        
        # Figure out which agent is best suited for this question
        agent = self._detect_intent(query)
        
        if agent:
            #Routing result to the selected agent
            self.logger.info(f"Routing query to {agent.get_name()}: '{query}'")
            response = agent.handle(query)
            return response
        else:
            # for invalid queries
            self.logger.warning(f"No agent found for query: '{query}'")
            return "I cannot answer this question"
    
    def _detect_intent(self, query: str) -> Optional[Agent]:
        query_lower = query.lower()
        
        # keep track of the best scoring agent
        best_agent = None
        best_score = 0
        
        # Loop through every agent to see who has the most matching keywords
        for agent in self.agents:
            score = 0
            for keyword in agent.get_keywords():
                # If the keyword appears anywhere in the query, give a point
                if keyword in query_lower:
                    score += 1
            
            # agent with higher match score is preferred
            if score > best_score:
                best_score = score
                best_agent = agent
        
        # Return the best agent found, or None if no matches
        return best_agent if best_score > 0 else None
    
    def list_agents(self) -> List[str]:
        # accurate list of all available agent names, for now just 2
        return [agent.get_name() for agent in self.agents]
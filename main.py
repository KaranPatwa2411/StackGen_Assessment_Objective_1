# main.py
import logging
from router import QueryRouter
from agents import GitHubAgent, LinearAgent

def create_router():
    # initializing agents
    agents = [
        LinearAgent(),
        GitHubAgent()
    ]
    return QueryRouter(agents)

def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    router = create_router()
    
    while True:
        try:
            query = input("Query: ")
            if query.lower() in ['quit', 'exit']: # to exit or quit the cli
                break
            
            # fetching response from the router
            response = router.route(query)
            print(f"Response: {response}\n")
            
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()
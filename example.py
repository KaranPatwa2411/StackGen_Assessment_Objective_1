from main import create_router

def main():
    router = create_router()
    
    queries = [
        "Show my open pull requests",
        "What issues are assigned to me?",
        "How many repositories do I have?",
        "Show current sprint progress",
        "What's the weather today?",
    ]
    
    print("Query Router - Programmatic Usage Example")
    print("=" * 60)
    
    for query in queries:
        print(f"Query: {query}")
        response = router.route(query)
        print(f"Response: {response}")
        print("-" * 60)

if __name__ == "__main__":
    main()
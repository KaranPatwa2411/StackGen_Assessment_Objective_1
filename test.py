import unittest
from router import QueryRouter
from agents import GitHubAgent, LinearAgent

class TestQueryRouter(unittest.TestCase):
    
    def setUp(self):
        self.agents = [GitHubAgent(), LinearAgent()]
        self.router = QueryRouter(self.agents)
    
    def test_routing_success(self):
        # Test GitHub routing
        github_response = self.router.route("Show my open pull requests")
        self.assertIn("pull request", github_response.lower())
        
        # Test Linear routing
        linear_response = self.router.route("What issues are assigned to me?")
        self.assertIn("issue", linear_response.lower())
    
    def test_routing_fallback(self):
        # Test unknown query
        unknown_response = self.router.route("What's the weather today?")
        self.assertEqual(unknown_response, "I cannot answer this question")
        
        # Test empty query
        empty_response = self.router.route("")
        self.assertEqual(empty_response, "Please provide a valid query.")

if __name__ == "__main__":
    unittest.main()
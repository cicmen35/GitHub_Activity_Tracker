import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from interaction_snippet import fetch_github_events


class TestFetchGithubEvents(unittest.TestCase):
    @patch('your_module.requests.get')
    def test_fetch_github_events_success(self, mock_get):
        # Mock response data
        mock_response = {
            "status_code": 200,
            "json.return_value": [
                {"type": "PushEvent", "repo": {"name": "owner/repo1"}, "created_at": "2024-04-07T10:00:00Z"},
                {"type": "PullRequestEvent", "repo": {"name": "owner/repo1"}, "created_at": "2024-04-07T10:30:00Z"}
            ]
        }
        mock_get.return_value = mock_response

        # Expected result
        expected_events = [
            {"type": "PushEvent", "repo": {"name": "owner/repo1"}, "created_at": "2024-04-07T10:00:00Z"},
            {"type": "PullRequestEvent", "repo": {"name": "owner/repo1"}, "created_at": "2024-04-07T10:30:00Z"}
        ]

        # Test fetch_github_events function
        repo_name = "owner/repository"
        since_date = (datetime.now() - timedelta(days=7)).isoformat()  # Fetch events from the last 7 days
        actual_events = fetch_github_events(repo_name, since_date)

        # Assert
        self.assertEqual(actual_events, expected_events)
        mock_get.assert_called_once_with(
            f"https://api.github.com/repos/{repo_name}/events",
            headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN', 'Accept': 'application/vnd.github.v3+json'},
            params={'since': since_date}
        )

    @patch('your_module.requests.get')
    def test_fetch_github_events_failure(self, mock_get):
        # Mock response data
        mock_response = {"status_code": 404}
        mock_get.return_value = mock_response

        # Test fetch_github_events function
        repo_name = "owner/repository"
        since_date = (datetime.now() - timedelta(days=7)).isoformat()  # Fetch events from the last 7 days
        actual_events = fetch_github_events(repo_name, since_date)

        # Assert
        self.assertIsNone(actual_events)
        mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()

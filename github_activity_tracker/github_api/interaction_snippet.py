import requests


class GitHubEventTracker:
    def __init__(self, access_token):
        self.access_token = access_token

    def fetch_github_events(self, repo_name, since_date):
        """
        Fetches GitHub events for a given repository since a specified date.

        Args:
            repo_name (str): The name of the GitHub repository.
            since_date (str): The start date in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ).

        Returns:
            list: List of GitHub events.
        """
        api_url = f"https://api.github.com/repos/{repo_name}/events"

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/vnd.github.v3+json"
        }

        params = {
            "since": since_date
        }

        try:
            response = requests.get(api_url, headers=headers, params=params)

            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to fetch GitHub events for {repo_name}. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred while fetching events for {repo_name}: {str(e)}")
            return None

    def monitor_repositories(self, repositories, since_date):
        """
        Monitor configured repositories and retrieve events periodically.

        Args:
            repositories (list): List of repository names to monitor.
            since_date (str): The start date in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ).
        """
        for repo_name in repositories:
            events = self.fetch_github_events(repo_name, since_date)
            if events:
                print(f"Fetched {len(events)} events from {repo_name}")
            else:
                print(f"Failed to fetch events from {repo_name}")


'''
# Example usage:
access_token = "YOUR_ACCESS_TOKEN"
event_tracker = GitHubEventTracker(access_token)
repositories = ["owner/repository1", "owner/repository2"]
since_date = "2024-04-01T00:00:00Z"
event_tracker.monitor_repositories(repositories, since_date)
'''
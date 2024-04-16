

class GithubAPi:
    """"""

    def __init__(self):
        """"""
        # mby : super.init
        self.events = [
            {"type": "PushEvent", "repo": {"name": "owner/repo1"}, "created_at": "2024-04-07T10:00:00Z"},
            {"type": "PushEvent", "repo": {"name": "owner/repo2"}, "created_at": "2024-04-07T10:10:00Z"},
            {"type": "PullRequestEvent", "repo": {"name": "owner/repo1"}, "created_at": "2024-04-07T10:20:00Z"},
            {"type": "PullRequestEvent", "repo": {"name": "owner/repo1"}, "created_at": "2024-04-07T10:30:00Z"}
        ]

    def calculate_average_time_between_events(self):
        """
        Calculate the average time between consecutive events for each combination of event type and repository name.

        Args:
            events (list): List of GitHub events.

        Returns:
            dict: Dictionary containing average time between events for each combination of event type and repository name.
        """

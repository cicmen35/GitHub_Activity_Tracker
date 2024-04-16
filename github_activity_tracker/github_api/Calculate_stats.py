from flask import Flask, jsonify
from datetime import datetime
from collections import defaultdict

app = Flask(__name__)

class CalcStat:
    def __init__(self, events):
        self.events = events

    def calculate_average_time_between_events(self):
        """
        Calculate the average time between consecutive events for each combination of event type and repository name.

        Returns:
            dict: Dictionary containing average time between events for each combination of event type and repository name.
        """
        event_timestamps = defaultdict(list)

        for event in self.events:
            event_type = event["type"]
            repo_name = event["repo"]["name"]
            created_at = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ")

            event_timestamps[(event_type, repo_name)].append(created_at)

        average_times = {}
        for key, timestamps in event_timestamps.items():
            timestamps.sort()
            time_diffs = [(timestamps[i + 1] - timestamps[i]).total_seconds() for i in range(len(timestamps) - 1)]
            if time_diffs:
                average_time = sum(time_diffs) / len(time_diffs)
                average_times[key] = average_time

        return average_times


#Sample events
events = [
    {"type": "PushEvent", "repo": {"name": "owner/repo1"}, "created_at": "2024-04-07T10:00:00Z"},
    {"type": "PushEvent", "repo": {"name": "owner/repo2"}, "created_at": "2024-04-07T10:10:00Z"},
    {"type": "PullRequestEvent", "repo": {"name": "owner/repo1"}, "created_at": "2024-04-07T10:20:00Z"},
    {"type": "PullRequestEvent", "repo": {"name": "owner/repo1"}, "created_at": "2024-04-07T10:30:00Z"}
]


@app.route('/statistics', methods=['GET'])
def get_statistics():
    """
    Endpoint to retrieve the calculated statistics.
    """
    calc_stat = CalcStat(events)
    statistics = calc_stat.calculate_average_time_between_events()
    return jsonify(statistics)


if __name__ == '__main__':
    app.run(debug=True)

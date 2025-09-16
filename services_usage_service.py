import datetime

class UsageService:
    def __init__(self):
        self.consent_given = False

    def request_consent(self):
        # Request permission, show dialog
        pass

    def get_usage_summary(self):
        if not self.consent_given:
            raise PermissionError("Consent not given for usage stats.")
        # Call Android usage stats API via PyJNIus
        # Return daily/weekly summaries
        return {"screen_time": 0, "top_apps": []}
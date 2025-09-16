import json
import os

class AuditService:
    def __init__(self, log_file="audit_log.json"):
        self.log_file = log_file
        self.log_data = []

    def log_action(self, action, details):
        entry = {"action": action, "details": details}
        self.log_data.append(entry)
        self.save_log()

    def save_log(self):
        with open(self.log_file, "w") as f:
            json.dump(self.log_data, f)

    def export_log(self):
        # Export for audit/compliance
        return self.log_data

    def delete_log(self):
        self.log_data = []
        self.save_log()
class SafeBrowsingService:
    def __init__(self):
        self.active = False
        self.consent_given = False

    def request_consent(self):
        pass

    def start_filtering(self):
        if self.consent_given:
            self.active = True
            # Start local VPN or browser component for filtering
            # Show persistent notification
        else:
            raise PermissionError("Consent not given for safe browsing.")

    def stop_filtering(self):
        self.active = False
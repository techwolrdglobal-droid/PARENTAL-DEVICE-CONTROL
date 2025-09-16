from plyer import gps

class LocationService:
    def __init__(self):
        self.active = False
        self.consent_given = False

    def request_consent(self):
        # Show dialog to child, record explicit opt-in
        pass

    def start_location(self):
        if self.consent_given:
            self.active = True
            gps.configure(on_location=self.on_location)
            gps.start()
            # Show persistent notification (handled in UI)
        else:
            raise PermissionError("Consent not given for location sharing.")

    def stop_location(self):
        self.active = False
        gps.stop()

    def on_location(self, **kwargs):
        # Save/encrypt location data, log action
        pass
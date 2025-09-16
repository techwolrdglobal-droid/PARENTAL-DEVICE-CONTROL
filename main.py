from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from services.location_service import LocationService
from services.usage_service import UsageService
from services.lock_service import LockService
from services.safe_browsing_service import SafeBrowsingService
from services.audit_service import AuditService

class ConsentScreen(Screen):
    pass

class DashboardScreen(Screen):
    pass

class AppScreenManager(ScreenManager):
    pass

class ParentControlApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.location_service = LocationService()
        self.usage_service = UsageService()
        self.lock_service = LockService()
        self.safe_browsing_service = SafeBrowsingService()
        self.audit_service = AuditService()
        sm = AppScreenManager()
        sm.add_widget(ConsentScreen(name="consent"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        return sm

if __name__ == '__main__':
    ParentControlApp().run()
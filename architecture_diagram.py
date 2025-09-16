"""
Modular Architecture Diagram (ASCII)
+-------------------+
|  main.py (Kivy UI)|
+--------+----------+
         |
         v
+--------+----------+
| AppScreenManager  |
+--------+----------+
         |
         v
+---------------------------+
| Modular Services          |
| - location_service.py     |
| - usage_service.py        |
| - lock_service.py         |
| - safe_browsing_service.py|
| - audit_service.py        |
+---------------------------+
         |
         v
+-------------------+    +------------------+
| Local Storage     |    | Cloud Backend    |
| (Encrypted, opt)  |    | (Optional, opt)  |
+-------------------+    +------------------+

All monitoring actions logged, consent required for each module, persistent notification always shown.
"""
# PARENTAL-DEVICE-CONTROL

## Overview
This app helps parents **responsibly** support children’s device use. It is **transparent, consent-based, privacy-first**, and compliant with local and platform laws.

**Tech:** Python, Kivy (UI), PyJNIus/Plyer (Android APIs), Buildozer (APK).

## Features
- **Explicit consent required for all monitoring**
- **Location sharing:** Opt-in, visible notification
- **Screen time & app usage:** Daily/weekly summaries, permission-based
- **Remote lock/scheduling:** Consent, override option
- **Safe browsing:** Configurable, visible filter
- **Gallery/contacts:** Only user-initiated sharing
- **Parental notifications/messages:** Consent-based only
- **Audit log:** Export/delete options
- **Data encryption:** At rest & in transit
- **What we collect:** Always visible
- **Stop monitoring:** One-tap consent revoke

## Architecture
See `architecture_diagram.png`.

## Build Steps
1. Install [Python](https://python.org), [Kivy](https://kivy.org), [Buildozer](https://buildozer.readthedocs.io), Android SDK, and dependencies.
2. Run `buildozer init`
3. Edit `buildozer.spec` for permissions (see below)
4. Build APK: `buildozer -v android debug`
5. Test on device (consent screens, notification visibility, stop button).

## Permissions & APIs
- **Location:** Only with explicit opt-in
- **Usage stats:** Requires user permission
- **Device lock:** Consent + override
- **VPN/browsing:** Transparent, visible filter
- **Contacts/gallery:** Only user-initiated
- **Biometric/PIN:** For parent access

See `developer_guide.md` for details and ethical/legal notes.

## Compliance
See `legal_privacy_checklist.md`.

## Tests
Run `pytest tests/` for unit/integration tests.

## Hard Constraints
- **NO message interception/keylogging**
- **NO hidden monitoring**
- **NO silent data extraction**
- **NO background access to WhatsApp/other apps**

See `legal_privacy_checklist.md`.

## Demo Mode
Run with `--demo` for safe, non-monitoring preview (no data stored).

## Contact & Audit
Export/delete all collected data via the app dashboard.

## License
MIT# PARENTAL-DEVICE-CONTROL

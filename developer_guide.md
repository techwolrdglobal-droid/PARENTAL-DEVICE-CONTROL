# Developer Guide: Permissions, APIs, and Ethics

## Android Permissions

- **Location:** Used for periodic sharing with explicit opt-in. Do NOT request background location unless child explicitly allows and sees notification.
- **Usage Stats:** Requires `PACKAGE_USAGE_STATS` permission; must show dialog and purpose.
- **Device Lock:** Use Device Owner APIs only with consent; always allow child to override/see schedule.
- **VPN/Filtering:** Use local VPN or browser filter; always show notification.
- **Contacts/Gallery:** Only user-initiated sharing (no background extraction).

## Why We Avoid Certain APIs

- **Message interception:** Disallowed by Play policy and laws; violates privacy.
- **Keylogging:** Disallowed; unethical and illegal.
- **Hidden monitoring:** Disallowed by Play policy and laws; always show notification.
- **Third-party app data:** Do NOT access WhatsApp or similar apps’ data.

## Ethical & Legal Basis

- **GDPR/CCPA/Play Store:** Require explicit, age-appropriate consent, transparency, and data minimization.
- **Age restriction:** Do NOT target children under local legal minimum age.
- **Audit & export:** Let users export/delete data.

See `legal_privacy_checklist.md`.
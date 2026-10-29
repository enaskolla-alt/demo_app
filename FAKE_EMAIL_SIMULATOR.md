# Offline fake-email simulator

Generate clearly marked, fictional email messages as local `.eml` files for training and interface testing. **No emails are sent.** This tool uses only Python's standard library and has no SMTP, HTTP, or network functions.

## Run

Requires Python 3.9+.

```bash
python fake_email_simulator.py
python fake_email_simulator.py --from-address demo@example.test --to-address learner@example.test --subject "Practice notification" --body "This is only a simulation."
```

Output is written to `simulated_emails/`. Open an `.eml` file with an email client to inspect it. The recipient field is only simulated metadata; nothing is delivered.

All generated messages include a simulation label in the subject, body, and header. Do not use this to impersonate others or deceive recipients.

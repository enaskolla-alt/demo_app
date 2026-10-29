"""Offline fake-email simulator. Does not connect to any network or send mail."""
import argparse
from email.message import EmailMessage
from pathlib import Path
from datetime import datetime, timezone
from uuid import uuid4

def simulate(sender: str, recipient: str, subject: str, body: str, output: Path) -> Path:
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = "[SIMULATION - NOT SENT] " + subject
    msg["X-Training-Simulation"] = "true"
    msg["Date"] = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
    msg.set_content("TRAINING SIMULATION — THIS EMAIL WAS NOT SENT.\n\n" + body)
    output.mkdir(parents=True, exist_ok=True)
    filename = output / ("simulated_" + uuid4().hex + ".eml")
    filename.write_bytes(msg.as_bytes())
    return filename

def main():
    parser = argparse.ArgumentParser(description="Generate offline simulated .eml files; never sends mail.")
    parser.add_argument("--from-address", default="training@example.test")
    parser.add_argument("--to-address", default="recipient@example.test")
    parser.add_argument("--subject", default="Example training message")
    parser.add_argument("--body", default="This is a harmless offline email example.")
    parser.add_argument("--output", type=Path, default=Path("simulated_emails"))
    args = parser.parse_args()
    path = simulate(args.from_address, args.to_address, args.subject, args.body, args.output)
    print(f"Saved locally: {path} (NOT SENT)")

if __name__ == "__main__":
    main()

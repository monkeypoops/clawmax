import asyncio
import os
from dotenv import load_dotenv

from cognee_memory import store_contact_memory, recall_contact_context
from email_sender import get_gmail_service, send_followup
from luma_contacts import load_contacts

load_dotenv()

SENDER = os.getenv("GMAIL_SENDER")
MAX_EMAILS = 3
DELAY_SECONDS = 300  # 5 minutes between sends


async def main():
    print("Authenticating Gmail...")
    service = get_gmail_service()

    contacts = load_contacts()
    if not contacts:
        print("No contacts found. Add contacts.csv first.")
        return

    print(f"Storing {len(contacts)} contacts in Cognee memory...")
    for c in contacts:
        await store_contact_memory(
            email=c["email"],
            name=c["name"],
            fun_fact=c["fun_fact"],
            context="Met at Luma event (hackathon)"
        )

    sent = 0
    for contact in contacts[:MAX_EMAILS]:
        email, name = contact["email"], contact["name"]
        if not email:
            continue

        context_list = await recall_contact_context(email, name)
        context_snippet = context_list[0] if context_list else ""

        subject = f"Great meeting you, {name}!"
        body = f"""Hi {name},

It was great meeting you at the event! {contact.get('fun_fact', '')}

{context_snippet or 'I enjoyed our conversation and would love to stay connected.'}

Best,
Your Name
"""

        try:
            msg_id = send_followup(service, SENDER, email, subject, body)
            print(f"[{sent + 1}/{MAX_EMAILS}] Sent to {email} (id: {msg_id})")
            sent += 1
        except Exception as e:
            print(f"Failed to send to {email}: {e}")
            continue

        if sent < MAX_EMAILS and sent < len(contacts):
            print(f"Waiting {DELAY_SECONDS}s before next send...")
            await asyncio.sleep(DELAY_SECONDS)

    print(f"\nDone. Sent {sent} follow-up(s).")


if __name__ == "__main__":
    asyncio.run(main())
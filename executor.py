import time
import pandas as pd

from gmail_service import get_gmail_service
from logger import log

# Execution control flags
pause_flag = False
abort_flag = False


def _extract_recipients(headers):
    """
    Extract email addresses from To and Cc headers.
    """
    recipients = set()

    for header in headers:
        if header["name"] in ("To", "Cc"):
            values = header.get("value", "")
            for part in values.split(","):
                recipients.add(part.strip())

    return recipients


def run_pipeline(sender_email, output_excel_path):
    """
    Main execution pipeline.
    """
    global pause_flag, abort_flag

    try:
        # Step 1: Authenticate
        log("Authenticate Gmail", "Gmail API", "STARTED")
        service = get_gmail_service()
        log("Authenticate Gmail", "Gmail API", "SUCCESS")

        # Step 2: Fetch message list
        log(f"Fetch emails from {sender_email}", "Gmail API", "STARTED")
        response = service.users().messages().list(
            userId="me",
            q=f"from:{sender_email}"
        ).execute()

        messages = response.get("messages", [])
        log(f"Fetched {len(messages)} emails", "Gmail API", "SUCCESS")

        recipients = set()

        # Step 3: Process each email
        for msg in messages:
            if abort_flag:
                log("Execution aborted by user", "System", "FAILED")
                return

            while pause_flag:
                time.sleep(1)

            message = service.users().messages().get(
                userId="me",
                id=msg["id"],
                format="metadata",
                metadataHeaders=["To", "Cc"]
            ).execute()

            headers = message["payload"].get("headers", [])
            recipients.update(_extract_recipients(headers))

        log("Extract recipients", "Parser", "SUCCESS")

        # Step 4: Save to Excel
        df = pd.DataFrame(sorted(recipients), columns=["Recipient Email"])
        df.to_excel(output_excel_path, index=False)

        log("Save Excel", output_excel_path, "SUCCESS")

    except Exception as exc:
        log(str(exc), "System", "FAILED")

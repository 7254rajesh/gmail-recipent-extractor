\# Gmail Recipient Extractor with Live Execution Logs



This project is a local Python application that authenticates with Gmail using OAuth 2.0, fetches emails from a given sender email address, extracts distinct recipient email IDs, and saves them to an Excel file while displaying live execution logs in a UI.



The application is built to satisfy the WorkCortex Intelligence evaluation assignment requirements, with special focus on real-time execution logging and clean system design.



---



\## Features



\- Fetch emails from Gmail by sender email address

\- Extract distinct recipient email IDs (To / Cc)

\- Export extracted recipients to an Excel file

\- Live execution logs displayed during runtime (not post-execution)

\- Execution status tracking: STARTED / SUCCESS / FAILED

\- Start / Pause / Resume / Abort controls

\- Secure OAuth-based Gmail authentication (no hard-coded credentials)

\- Runs completely locally



---



\## Tech Stack



\- Python 3

\- Gmail API (OAuth 2.0)

\- Streamlit (UI)

\- Pandas (Excel export)



---



\## Project Structure



pip install -r requirements.txt



---



Gmail API Setup (One-time)



\- Create a Google Cloud project

\- Enable Gmail API

\- Create OAuth Client ID (Desktop App)

\- Download `credentials.json`

\- Place `credentials.json` in the project root



> Note: The application uses OAuth 2.0. No Gmail credentials are hard-coded.



---



Run the application



streamlit run app.py



The browser-based UI will open automatically.



---



\## Usage



1\. Enter sender email address

2\. Enter Excel output file path

3\. Click \*\*Start\*\*

4\. Observe live execution logs

5\. Excel file is generated at the specified location



---



\## Sample Output



A sample Excel output file is included in the repository for reference.



---



\## Design Decisions



\- Gmail API used instead of browser automation for reliability and security

\- OAuth 2.0 used to avoid storing credentials

\- Background execution thread used to keep UI responsive

\- Thread-safe logging queue used for real-time UI log updates

\- Modular separation between UI, execution, Gmail service, and logging



---



\## Assumptions



\- The Gmail account belongs to the user running the application

\- Sender email exists in the mailbox

\- Recipient information is available in email headers (To / Cc)

\- Application is run in a local environment

\- OAuth consent screen is configured in testing mode



---






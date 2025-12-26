import threading
import time

import pandas as pd
import streamlit as st

import executor
from logger import log_queue

# ---------------- UI SETUP ----------------

st.set_page_config(layout="wide")
st.title("📧 Gmail Recipient Extractor")

sender_email = st.text_input(
    "Sender Email Address",
    placeholder="example@domain.com"
)

output_path = st.text_input(
    "Excel Output Path",
    value="recipients.xlsx"
)

# ---------------- CONTROL BUTTONS ----------------

c1, c2, c3, c4 = st.columns(4)

if c1.button("▶ Start"):
    executor.abort_flag = False
    executor.pause_flag = False

    threading.Thread(
        target=executor.run_pipeline,
        args=(sender_email, output_path),
        daemon=True
    ).start()

if c2.button("⏸ Pause"):
    executor.pause_flag = True

if c3.button("▶ Resume"):
    executor.pause_flag = False

if c4.button("⛔ Abort"):
    executor.abort_flag = True

# ---------------- LIVE LOG VIEW ----------------

st.subheader("📜 Live Execution Logs")

log_rows = []

while not log_queue.empty():
    log_rows.append(log_queue.get())

if log_rows:
    df_logs = pd.DataFrame(log_rows)
    st.dataframe(df_logs, use_container_width=True)
else:
    st.info("No logs yet. Click Start to begin execution.")

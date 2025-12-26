from queue import Queue
from datetime import datetime

# Thread-safe queue for live logs
log_queue = Queue()

# Global step counter
_order_counter = 1

def log(step_description, tool, status):
    """
    Push a log entry into the live log queue.
    """
    global _order_counter

    log_queue.put({
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Order": _order_counter,
        "Step Description": step_description,
        "Tool/App/URL/EXE": tool,
        "Status": status
    })

    _order_counter += 1

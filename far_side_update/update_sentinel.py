from update_checker import checker
from sentinel_memory import memory_recall
from hermes_call import send_message

new_url = checker()
if memory_recall(new_url) is False:
    send_message(new_url)
elif memory_recall(new_url) is True:
    send_message(new_url)

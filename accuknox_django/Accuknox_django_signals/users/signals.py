

import threading
import time
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

    # Simulate a delay to show synchronous behavior
    print("Signal execution started.")
    time.sleep(2)  # Simulate heavy work
    print(f"Signal executed at: {time.time()}")

    # Raise an exception to test transaction rollback
    raise ValueError("Simulating an error in the signal.")

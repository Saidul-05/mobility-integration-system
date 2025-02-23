from celery import shared_task

@shared_task
def example_task():
    print("Celery task running every 5 minutes")
    # Do something, e.g. send emails, cleanup, etc.

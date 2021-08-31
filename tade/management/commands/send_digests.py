from django.core.management.base import BaseCommand
from django.apps import apps

config = apps.get_app_config("tade")
from tade.mail import Digest


class Command(BaseCommand):
    help = "Send digest mails"

    def handle(self, *args, **kwargs):
        Digest.send_digests()

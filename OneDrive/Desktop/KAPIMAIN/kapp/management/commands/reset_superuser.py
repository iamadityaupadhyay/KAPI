from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Deletes the current superuser and creates a new one'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Delete the current superuser
        superuser = User.objects.filter(is_superuser=True).first()
        if superuser:
            superuser.delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted the superuser.'))
        else:
            self.stdout.write(self.style.WARNING('No superuser found.'))

        # Create a new superuser
        from django.core.management import call_command
        call_command('createsuperuser')

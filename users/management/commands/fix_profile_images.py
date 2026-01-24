"""
Management command to fix profile image paths and ensure default.png is set correctly.
"""
from django.core.management.base import BaseCommand
from users.models import ProfileModel
from pathlib import Path
from django.conf import settings


class Command(BaseCommand):
    help = 'Fix profile image paths (remove old media/media/ prefix) and reset broken images'

    def add_arguments(self, parser):
        parser.add_argument(
            '--reset-all',
            action='store_true',
            help='Reset ALL profiles to default.png',
        )

    def handle(self, *args, **options):
        self.stdout.write("=" * 60)
        self.stdout.write("Fixing Profile Images")
        self.stdout.write("=" * 60)

        profiles = ProfileModel.objects.all()
        fixed_count = 0
        reset_count = 0

        for profile in profiles:
            image_name = profile.image.name
            
            # Case 1: Reset all if requested
            if options['reset_all']:
                profile.image = 'default.png'
                profile.save()
                reset_count += 1
                self.stdout.write(f"  Reset {profile.user.username} → default.png")
                continue
            
            # Case 2: Fix old double media/ prefix
            if image_name.startswith('media/media/'):
                new_path = image_name.replace('media/media/profile/', 'profile/', 1)
                profile.image.name = new_path
                profile.save(update_fields=['image'])
                fixed_count += 1
                self.stdout.write(self.style.SUCCESS(
                    f"  Fixed {profile.user.username}: {image_name} → {new_path}"
                ))
            
            # Case 3: Check if file exists
            elif image_name != 'default.png':
                full_path = Path(settings.MEDIA_ROOT) / image_name
                if not full_path.exists():
                    self.stdout.write(self.style.WARNING(
                        f"  File missing for {profile.user.username}: {image_name}"
                    ))
                    self.stdout.write(f"    Resetting to default.png")
                    profile.image = 'default.png'
                    profile.save()
                    reset_count += 1

        self.stdout.write("\n" + "=" * 60)
        self.stdout.write(self.style.SUCCESS(
            f"Done! Fixed: {fixed_count}, Reset: {reset_count}"
        ))
        self.stdout.write("=" * 60)

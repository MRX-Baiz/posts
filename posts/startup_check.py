# startup_check.py
"""
Startup check middleware ou fichier d'aide pour BasicBlogger.
Affiche le status DEBUG et MEDIA serving au démarrage.
"""
import os
from django.conf import settings

def check_media_serving():
    """Check if MEDIA files will be served in current configuration."""
    debug_status = settings.DEBUG
    media_url = settings.MEDIA_URL
    media_root = settings.MEDIA_ROOT
    
    print("\n" + "=" * 60)
    print("🔧 BasicBlogger - Startup Configuration Check")
    print("=" * 60)
    print(f"DEBUG mode: {debug_status}")
    print(f"MEDIA_URL: {media_url}")
    print(f"MEDIA_ROOT: {media_root}")
    
    if debug_status:
        print("✅ MEDIA serving: ENABLED (urls.py serves /media/)")
        print("   → Profile images will work correctly")
    else:
        print("⚠️  MEDIA serving: DISABLED (DEBUG=False)")
        print("   → Profile images will return 404!")
        print("   → To fix: $env:DEBUG=\"True\"; python manage.py runserver")
    
    print("=" * 60 + "\n")

if __name__ == "__main__":
    # Can be run standalone for testing
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'posts.settings')
    import django
    django.setup()
    check_media_serving()

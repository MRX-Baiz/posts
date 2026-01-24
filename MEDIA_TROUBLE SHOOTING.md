# 🔧 BasicBlogger - Media Troubleshooting

## Problem: Profile images return 404 or show default.png

### Quick Fix (DEV)
```powershell
# In PowerShell, ALWAYS run with:
$env:DEBUG="True"; python manage.py runserver

# Verify it worked:
# - Check terminal output shows "✅ MEDIA serving: ENABLED"
# - Test: http://127.0.0.1:8000/media/default.png (should show image, not 404)
```

### Why?
- Django only serves `/media/` when `DEBUG=True`
- Without `$env:DEBUG="True"`, DEBUG defaults to `False`
- When DEBUG=False → `/media/` NOT served → 404 on uploaded images

### Test Upload
1. Set DEBUG: `$env:DEBUG="True"`
2. Run server: `python manage.py runserver`
3. Go to `/profile/`, upload image
4. Refresh with Ctrl+Shift+R (clear cache)
5. Check image appears on `/profile/` AND `/blog/`

### Still Not Working?
- Check terminal shows "✅ MEDIA serving: ENABLED" on startup
- Check file exists: `dir media\profile\`  
- Hard reload browser: Ctrl+Shift+R

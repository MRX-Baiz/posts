"""
Management command to seed the database with demo data.

Usage:
    python manage.py seed_demo
    python manage.py seed_demo --clear
    python manage.py seed_demo --verbose

This command is idempotent - running it multiple times won't create duplicates.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post, Comment
from users.models import ProfileModel
from django.utils import timezone
from datetime import timedelta
import random


class Command(BaseCommand):
    help = 'Seed the database with demo data (idempotent)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing demo data before seeding',
        )
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Show detailed output of operations',
        )

    def handle(self, *args, **options):
        clear = options.get('clear')
        verbose = options.get('verbose')

        if clear:
            self.stdout.write(self.style.WARNING('Clearing existing demo data...'))
            self._clear_demo_data(verbose)

        self.stdout.write(self.style.SUCCESS('Starting demo data seeding...'))
        
        # Check if demo data already exists
        if User.objects.filter(username__startswith='demo_').exists() and not clear:
            self.stdout.write(
                self.style.WARNING(
                    'Demo data already exists. Use --clear to reset.'
                )
            )
            return

        # Seed users
        users = self._create_demo_users(verbose)
        
        # Seed posts
        posts = self._create_demo_posts(users, verbose)
        
        # Seed comments
        comments_count = self._create_demo_comments(users, posts, verbose)
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('Demo data seeded successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Created: {len(users)} users, {len(posts)} posts, {comments_count} comments'))
        self.stdout.write(self.style.SUCCESS('='*50 + '\n'))

    def _clear_demo_data(self, verbose):
        """Remove all demo data from the database."""
        demo_users = User.objects.filter(username__startswith='demo_')
        
        if verbose:
            self.stdout.write(f'Found {demo_users.count()} demo users to delete')
        
        # Delete posts and comments (cascade)
        Post.objects.filter(author__in=demo_users).delete()
        
        # Delete users (profiles will cascade)
        demo_users.delete()
        
        self.stdout.write(self.style.SUCCESS('Demo data cleared.\n'))

    def _create_demo_users(self, verbose):
        """Create demo users with profiles."""
        demo_users_data = [
            {
                'username': 'demo_alice',
                'email': 'alice@demo.blog',
                'first_name': 'Alice',
                'last_name': 'Johnson',
                'password': 'demo123456'
            },
            {
                'username': 'demo_bob',
                'email': 'bob@demo.blog',
                'first_name': 'Bob',
                'last_name': 'Smith',
                'password': 'demo123456'
            },
            {
                'username': 'demo_charlie',
                'email': 'charlie@demo.blog',
                'first_name': 'Charlie',
                'last_name': 'Brown',
                'password': 'demo123456'
            },
        ]

        users = []
        for user_data in demo_users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                }
            )
            
            if created:
                user.set_password(user_data['password'])
                user.save()
                
                # Create profile (signal should handle this, but ensure it exists)
                ProfileModel.objects.get_or_create(user=user)
                
                if verbose:
                    self.stdout.write(
                        self.style.SUCCESS(f'[OK] Created user: {user.username}')
                    )
            else:
                if verbose:
                    self.stdout.write(f'- User already exists: {user.username}')
            
            users.append(user)

        return users

    def _create_demo_posts(self, users, verbose):
        """Create demo blog posts."""
        demo_posts_data = [
            {
                'title': 'Getting Started with Django',
                'content': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. In this post, we\'ll explore the basics of setting up a Django project and creating your first app. Django follows the Model-View-Template (MVT) pattern and comes with many built-in features like an ORM, admin interface, and authentication system.'
            },
            {
                'title': 'Understanding Python Decorators',
                'content': 'Decorators are a powerful feature in Python that allow you to modify the behavior of functions or classes. They are widely used in frameworks like Django and Flask. A decorator is essentially a function that takes another function as an argument and returns a new function. This pattern is perfect for adding functionality like logging, authentication, or caching.'
            },
            {
                'title': 'Best Practices for Web Development',
                'content': 'When building web applications, following best practices is crucial for maintainability and scalability. Some key principles include: writing clean, readable code; implementing proper error handling; using version control; writing tests; and documenting your code. Security should also be a top priority - always validate user input and protect against common vulnerabilities.'
            },
            {
                'title': 'Introduction to RESTful APIs',
                'content': 'REST (Representational State Transfer) is an architectural style for designing networked applications. RESTful APIs use HTTP methods like GET, POST, PUT, and DELETE to perform operations on resources. They are stateless, cacheable, and provide a uniform interface. Django REST Framework makes it easy to build robust, browsable APIs in Django.'
            },
            {
                'title': 'Database Design Fundamentals',
                'content': 'Good database design is essential for application performance and data integrity. Key concepts include normalization, indexing, and relationships. Understanding foreign keys, one-to-many, and many-to-many relationships is crucial. Django\'s ORM abstracts much of this complexity, but understanding the underlying principles helps you make better design decisions.'
            },
            {
                'title': 'Frontend vs Backend Development',
                'content': 'The distinction between frontend and backend development is important to understand. Frontend deals with what users see and interact with - HTML, CSS, and JavaScript. Backend handles data, logic, and server-side operations. Modern full-stack developers need skills in both areas. Django excels at backend development while integrating well with frontend frameworks.'
            },
            {
                'title': 'Version Control with Git',
                'content': 'Git is an essential tool for modern software development. It allows you to track changes, collaborate with others, and manage different versions of your code. Key concepts include commits, branches, merging, and rebasing. GitHub, GitLab, and Bitbucket provide hosting for Git repositories along with collaboration features like pull requests and code reviews.'
            },
            {
                'title': 'Testing Your Django Applications',
                'content': 'Testing is crucial for maintaining code quality and catching bugs early. Django provides a robust testing framework built on Python\'s unittest module. You can write unit tests for models, integration tests for views, and functional tests for complete user workflows. Tools like pytest and coverage.py enhance the testing experience.'
            },
            {
                'title': 'Deploying Django to Production',
                'content': 'Deploying a Django application requires careful consideration of several factors. You\'ll need a WSGI server like Gunicorn or uWSGI, a reverse proxy like Nginx, and a database like PostgreSQL. Static files should be served efficiently with WhiteNoise or a CDN. Don\'t forget to set DEBUG=False and use environment variables for sensitive settings.'
            },
            {
                'title': 'Understanding CSS Flexbox and Grid',
                'content': 'Modern CSS layout techniques have revolutionized web design. Flexbox is perfect for one-dimensional layouts and component alignment, while Grid excels at two-dimensional layouts. Both are supported across modern browsers and eliminate the need for float-based layouts. Learning these tools will significantly improve your frontend development skills.'
            },
            {
                'title': 'Authentication and Authorization',
                'content': 'Security is paramount in web applications. Authentication verifies who a user is, while authorization determines what they can do. Django provides a comprehensive auth system with user models, permissions, and groups. For more advanced needs, you might implement token-based auth with JWT or integrate social authentication providers.'
            },
            {
                'title': 'Responsive Web Design Principles',
                'content': 'With users accessing websites from various devices, responsive design is essential. Use flexible layouts, media queries, and relative units. Mobile-first design approach often yields better results. CSS frameworks like Bootstrap provide responsive grids and components, but understanding the underlying principles helps you create custom solutions.'
            },
        ]

        posts = []
        for i, post_data in enumerate(demo_posts_data):
            # Assign posts to users randomly
            author = users[i % len(users)]
            
            # Create posts with varying timestamps
            days_ago = random.randint(1, 30)
            created_time = timezone.now() - timedelta(days=days_ago)
            
            post, created = Post.objects.get_or_create(
                title=post_data['title'],
                author=author,
                defaults={
                    'content': post_data['content'],
                }
            )
            
            if created:
                # Update the created timestamp
                post.date_created = created_time
                post.save()
                
                if verbose:
                    self.stdout.write(
                        self.style.SUCCESS(f'[OK] Created post: {post.title}')
                    )
            else:
                if verbose:
                    self.stdout.write(f'- Post already exists: {post.title}')
            
            posts.append(post)

        return posts

    def _create_demo_comments(self, users, posts, verbose):
        """Create demo comments on posts."""
        comment_templates = [
            "Great article! Thanks for sharing.",
            "This was really helpful, learned a lot!",
            "Interesting perspective on this topic.",
            "Could you elaborate on this point?",
            "I've been looking for this information, thank you!",
            "Well explained and easy to understand.",
            "This helped me solve my problem, thanks!",
            "Looking forward to more content like this.",
            "Excellent breakdown of the concepts.",
            "Very informative post!",
            "This is exactly what I needed to know.",
            "Thanks for the detailed explanation!",
            "Great insights, really appreciate it.",
            "This cleared up a lot of confusion for me.",
            "Bookmarking this for future reference.",
            "Simple and straightforward, love it!",
            "I had the same question, this helps a lot.",
            "Perfect timing, just what I was researching!",
            "Nice work on this article!",
            "This is a must-read for beginners.",
        ]

        comments_count = 0
        
        for post in posts:
            # Each post gets 1-3 comments
            num_comments = random.randint(1, 3)
            
            for _ in range(num_comments):
                commenter = random.choice(users)
                content = random.choice(comment_templates)
                
                comment, created = Comment.objects.get_or_create(
                    user=commenter,
                    post=post,
                    content=content,
                    defaults={}
                )
                
                if created:
                    comments_count += 1
                    if verbose:
                        self.stdout.write(
                            self.style.SUCCESS(
                                f'[OK] Created comment by {commenter.username} on "{post.title}"'
                            )
                        )

        return comments_count

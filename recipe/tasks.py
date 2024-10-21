# recipe/tasks.py

import logging
from celery import shared_task
from django.core.mail import send_mail
from .models import Recipe
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__) 

@shared_task
def send_daily_like_notifications():
    try:
        logger.info("Start")
        recipes = Recipe.objects.all()
        logger.info(f"Recipes: {recipes}")
        
        for recipe in recipes:
            likes_count = recipe.get_total_number_of_likes()
            logger.info(f'Recipe: {recipe.title}, Likes: {likes_count}, Author; {recipe.author.email}')
            if likes_count > 0:
                send_mail(
                    subject='Daily Like Notification',
                    message=f'Your recipe "{recipe.title}" has received {likes_count} likes today!',
                    from_email='bryanlewis.freelance@outlook.com',
                    recipient_list=[recipe.author.email],
                    fail_silently=False,
                )
    except Exception as e:
        logger.error(f"Error occurred: {e}")

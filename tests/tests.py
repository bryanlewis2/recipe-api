import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Recipe, RecipeLike
from config.celery import app as celery_app


User = get_user_model()

@pytest.mark.django_db
class TestRecipeViews:

    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up a test client and a user for authentication."""
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_recipe_list(self):
        """Test retrieving a list of recipes."""
        recipe = Recipe.objects.create(title="Test Recipe", author=self.user)

        response = self.client.get(reverse('recipe-list'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['title'] == recipe.title

    def test_recipe_create(self):
        """Test creating a new recipe."""
        response = self.client.post(reverse('recipe-create'), {
            'title': 'New Recipe',
            'content': 'Recipe content goes here.',
        })
        assert response.status_code == status.HTTP_201_CREATED
        assert Recipe.objects.count() == 1
        assert Recipe.objects.get().title == 'New Recipe'

    def test_recipe_retrieve_update_delete(self):
        """Test retrieving, updating, and deleting a recipe."""
        recipe = Recipe.objects.create(title="Update Recipe", author=self.user)
        url = reverse('recipe-detail', kwargs={'pk': recipe.id})

        # Retrieve the recipe
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == recipe.title

        # Update the recipe
        response = self.client.put(url, {'title': 'Updated Recipe'})
        assert response.status_code == status.HTTP_200_OK
        recipe.refresh_from_db()
        assert recipe.title == 'Updated Recipe'

        # Delete the recipe
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Recipe.objects.count() == 0

    def test_recipe_like(self):
        """Test liking and unliking a recipe."""
        recipe = Recipe.objects.create(title="Like Recipe", author=self.user)

        # Like the recipe
        response = self.client.post(reverse('recipe-like', kwargs={'pk': recipe.id}))
        assert response.status_code == status.HTTP_201_CREATED
        assert RecipeLike.objects.count() == 1

        # Attempt to like again
        response = self.client.post(reverse('recipe-like', kwargs={'pk': recipe.id}))
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        # Unlike the recipe
        response = self.client.delete(reverse('recipe-like', kwargs={'pk': recipe.id}))
        assert response.status_code == status.HTTP_200_OK
        assert RecipeLike.objects.count() == 0

    def test_recipe_like_list(self):
        """Test listing likes for a recipe."""
        recipe = Recipe.objects.create(title="Like List Recipe", author=self.user)
        RecipeLike.objects.create(user=self.user, recipe=recipe)

        response = self.client.get(reverse('recipe-like-list', kwargs={'pk': recipe.id}))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['user'] == self.user.id  # Ensure the correct user is listed


from django.test import TestCase
from .models import Post, Categories
from django.core.exceptions import ValidationError


class PostModelTests(TestCase):
    ''' Test the post model class for features. '''
    def test_post_model_save_without_category(self):
        ''' Tests that object is saving properly with out specifiying post category. '''

        post_obj = Post.objects.create(
            post_title='Test post title',
            post_content='This is post content for test post',
            post_url='test-post-url',
        )
        self.assertIsInstance(post_obj, Post, 'Post object complete created without category')

    def test_post_model_without_url(self):
        ''' Tests the post object to prevent from saving post object with empty url. '''

        with self.assertRaises(ValidationError, msg='Post can be saved without post url.'):
            post_obj = Post.objects.create(
                post_title='Test post title',
                post_content='This is post content for test post',
            )

    def test_post_model_save_complete(self):
        ''' Tests that object is not saving properly when specifiying post category (many-to-many). '''
        category_object = Categories.objects.create(
            id=12,
            category_name='Test Category',
            category_desc='This is test category description',
            category_url='test-category',
        )
        post_obj = Post.objects.create(
            id=124,
            post_title='Test post title',
            post_content='This is post content for test post',
            post_url='test-post-url'
        )
        post_obj.post_category.add(category_object)
        self.assertIsInstance(post_obj, Post, 'Post object cannot be saved with category object.')

    def test_post_model_save_without_title(self):
        with self.assertRaises(ValidationError, msg='The post model is being saved without title.'):
            post_obj = Post.objects.create(
                id=124,
                post_content='This is post content for test post',
                post_url='test-post-url'
            )


class CategoriesModelTests(TestCase):
    ''' Tests the attributes and behaviours of Categories Model class. '''

    def test_complete_category_model_save(self):
        ''' Tests that complete category object can be saved. '''
        category_object = Categories.objects.create(
            id=12,
            category_name='Test Category',
            category_desc='This is test category description',
            category_url='test-category',
        )
        self.assertIsInstance(category_object, Categories, 'Complete category objects is not being saved')

    def test_category_model_save_without_name(self):
        ''' Tests that category object model cannot be saved without title. '''
        with self.assertRaises(ValidationError, msg='Category objects is being saved completely without name.'):
            category_object = Categories.objects.create(
                id=12,
                category_desc='This is test category description',
                category_url='test-category',
            )

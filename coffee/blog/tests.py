from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user and a post for testing
        user = User.objects.create(username="testuser", password="testpass")
        Post.objects.create(
            title="Test post",
            slug="test-post",
            author=user,
            body="This is a test post",
            status=Post.Status.PUBLISHED,
        )

    def test_title_label(self):
        # Test that the title field has the correct verbose name
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_title_max_length(self):
        # Test that the title field has the correct max_length
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field("title").max_length
        self.assertEqual(max_length, 250)

    def test_slug_label(self):
        # Test that the slug field has the correct verbose name
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("slug").verbose_name
        self.assertEqual(field_label, "slug")

    def test_slug_max_length(self):
        # Test that the slug field has the correct max_length
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field("slug").max_length
        self.assertEqual(max_length, 250)

    def test_author_label(self):
        # Test that the author field has the correct verbose name
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_body_label(self):
        # Test that the body field has the correct verbose name
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("body").verbose_name
        self.assertEqual(field_label, "body")

    def test_publish_default(self):
        # Test that the publish field has the correct default value
        post = Post.objects.get(id=1)
        default_value = post._meta.get_field("publish").default()
        self.assertEqual(default_value, timezone.now())

    def test_created_auto_now_add(self):
        # Test that the created field has the correct auto_now_add value
        post = Post.objects.get(id=1)
        auto_now_add = post._meta.get_field("created").auto_now_add
        self.assertTrue(auto_now_add)

    def test_updated_auto_now(self):
        # Test that the updated field has the correct auto_now value
        post = Post.objects.get(id=1)
        auto_now = post._meta.get_field("updated").auto_now
        self.assertTrue(auto_now)

    def test_status_label(self):
        # Test that the status field has the correct verbose name
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("status").verbose_name
        self.assertEqual(field_label, "status")

    def test_status_max_length(self):
        # Test that the status field has the correct max_length
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field("status").max_length
        self.assertEqual(max_length, 2)

    def test_status_choices(self):
        # Test that the status field has the correct choices
        post = Post.objects.get(id=1)
        choices = post._meta.get_field("status").choices
        self.assertEqual(choices, Post.Status.choices)

    def test_status_default(self):
        # Test that the status field has the correct default value
        post = Post.objects.get(id=1)
        default_value = post._meta.get_field("status").default
        self.assertEqual(default_value, Post.Status.DRAFT)

    def test_meta_ordering(self):
        # Test that the meta class has the correct ordering attribute
        ordering = Post._meta.ordering
        self.assertEqual(ordering, ["-publish"])

    def test_meta_indexes(self):
        # Test that the meta class has the correct indexes attribute
        indexes = Post._meta.indexes[0].fields
        self.assertEqual(indexes, ["-publish"])

    # def test_author_related_name(self):
    #     # Test that the author field has the correct related_name
    #     post = Post.objects.get(id=1)
    #     related_name = post._meta.get_field("author").related_name
    #     self.assertEqual(related_name, "blog_posts")

    def test_object_name(self):
        # Test that the object name is correct
        post = Post.objects.get(id=1)
        expected_object_name = post.title
        self.assertEqual(expected_object_name, str(post))

    def test_get_absolute_url(self):
        # Test that the get_absolute_url method returns the correct url
        post = Post.objects.get(id=1)
        expected_url = f"/blog/{post.publish.year}/{post.publish.month}/{post.publish.day}/{post.slug}/"
        self.assertEqual(expected_url, post.get_absolute_url())

    def test_published_manager(self):
        # Test that the published manager returns only published posts
        posts = Post.published.all()
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].title, "Test post")

    def test_post_list_view(self):
        # Test that the post_list view returns the correct status code and template
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/list.html")

    def test_post_detail_view(self):
        # Test that the post_detail view returns the correct status code and template
        post = Post.objects.get(id=1)
        response = self.client.get(post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/detail.html")

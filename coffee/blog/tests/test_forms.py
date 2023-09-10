from django.test import TestCase

from blog.forms import EmailPostForm


class EmailPostFormTest(TestCase):
    # Test that the form has the correct fields
    def test_name_field_label(self):
        form = EmailPostForm()
        self.assertTrue(form.fields["name"].label == None or form.fields["name"].label == "name")

    def test_name_field_max_length(self):
        # Test that the name field has the correct max_length
        form = EmailPostForm()
        self.assertEqual(form.fields["name"].max_length, 25)

    def test_email_field_label(self):
        # Test that the email field has the correct label
        form = EmailPostForm()
        self.assertTrue(form.fields["email"].label == None or form.fields["email"].label == "email")

    def test_to_field_label(self):
        # Test that the to field has the correct label
        form = EmailPostForm()
        self.assertTrue(form.fields["to"].label == None or form.fields["to"].label == "to")

    def test_comments_field_label(self):
        # Test that the comments field has the correct label
        form = EmailPostForm()
        self.assertTrue(form.fields["comments"].label == None or form.fields["comments"].label == "comments")

    def test_comments_field_required_false(self):
        # Test that the comments field has required=False
        form = EmailPostForm()
        self.assertEqual(form.fields["comments"].required, False)

    def test_comments_field_widget(self):
        # Test that the comments field has the correct widget
        form = EmailPostForm()
        self.assertEqual(form.fields["comments"].widget.__class__.__name__, "Textarea")


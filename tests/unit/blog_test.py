from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('test', 'Test Author')

        self.assertEqual('test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)


    def test_repr(self):
        b = Blog('test', 'Test Author')
        b2 = Blog('Working', 'Keith')

        self.assertEqual(b.__repr__(), 'test by Test Author (0 post)')
        self.assertEqual(b.__repr__(), 'test by Test Author (0 post)')

    def test_repr_multiple_posts(self):
        b = Blog('test', 'Test Author')
        b.posts = ['test']
        b2 = Blog('test', 'Test Author')
        b2.posts = ['test', 'another test']

        self.assertEqual(b.__repr__(), 'test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'test by Test Author (2 posts)')



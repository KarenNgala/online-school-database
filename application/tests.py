from django.test import TestCase
from .models import *
from datetime import datetime


class TestUser(TestCase):
    ''' test user model class '''
    def setUp(self):
        ''' method called before each testcase '''
        self.user = User.objects.create_user(email='address@email.com', password='Password123')

    def tearDown(self):
        ''' method to clear all setup instances after each test is run '''
        self.user.delete()

    def test_user_creation(self):
        ''' method to test creation of user instances '''
        self.assertIsInstance(self.user, User)
        self.assertEqual(len(User.objects.all()), 1)


class TestUniversity(TestCase):
    ''' test university model class '''
    def setUp(self):
        ''' method called before each testcase '''
        self.uni = University(name='Masinde Muliro')
        self.uni.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test is run '''
        self.uni.delete()

    def test_uni_creation(self):
        ''' method to test creation of university instances '''
        self.assertIsInstance(self.uni, University)
        self.assertEqual(len(University.objects.all()), 1)


class TestCourse(TestCase):
    ''' test course model class '''
    def setUp(self):
        ''' method called before each testcase '''
        self.course = Course(name='Computer Science')
        self.course.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test is run '''
        self.course.delete()

    def test_course_creation(self):
        ''' method to test creation of course instances '''
        self.assertIsInstance(self.course, Course)
        self.assertEqual(len(Course.objects.all()), 1)


class TestYear(TestCase):
    ''' test year model class '''
    def setUp(self):
        ''' method called before each testcase '''
        self.year = Year_Of_Study(name=1.1)
        self.year.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test is run '''
        self.year.delete()

    def test_year_creation(self):
        ''' method to test creation of year instances '''
        self.assertIsInstance(self.year, Year_Of_Study)
        self.assertEqual(len(Year_Of_Study.objects.all()), 1)


class TestUnit(TestCase):
    ''' test unit model class '''
    def setUp(self):
        ''' method called before each testcase '''
        self.uni = University(name='Masinde Muliro')
        self.uni.save()

        self.year = Year_Of_Study(name='3.1')
        self.year.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test is run '''
        self.uni.delete()
        self.course.delete()
        self.year.delete()

    def test_unit_creation(self):
        ''' method to test creation of unit instances '''
        self.unit = Unit(name='314: Electronics III', uni=self.uni, year=self.year)
        self.unit.save()
        self.course = self.unit.course.create(name='Computer Science')

        self.assertIsInstance(self.unit, Unit)
        self.assertEqual(len(Unit.objects.all()), 1)
        self.assertEqual(self.unit.name, '314: Electronics III')


class TestFile(TestCase):
    ''' test file model class '''
    def setUp(self):
        ''' method called before each testcase '''
        self.user = User.objects.create_user(email='address@email.com', password='Password123')

        self.uni = University(name='Masinde Muliro')
        self.uni.save()

        self.unit = Unit(name='314: Electronics II')
        self.unit.save()
        
        # year

    def tearDown(self):
        ''' method to clear all setup instances after each test is run '''
        self.user.delete()
        self.uni.delete()
        self.unit.delete()

    def test_file_creation(self):
        ''' method to test creation of file instances '''
        self.file = File(name='2016 Course Outline', uploaded_by=self.user, date=datetime.now, 
                url='https://res.cloudinary.com/oceanic/image/upload/v1609160582/default_ynolea.png',
                unit=self.unit)
        self.file.save()

        self.assertIsInstance(self.file, File)
        self.assertEqual(len(File.objects.all()), 1)
        self.assertEqual(self.file.name, '2016 Course Outline')
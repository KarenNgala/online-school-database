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


class TestUnit(TestCase):
    ''' test unit model class '''
    def setUp(self):
        ''' method called before each testcase '''
        self.unit = Unit(name='Electronics II')
        self.unit.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test is run '''
        self.unit.delete()

    def test_unit_creation(self):
        ''' method to test creation of unit instances '''
        self.assertIsInstance(self.unit, Unit)
        self.assertEqual(len(Unit.objects.all()), 1)


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
        self.year = Year(name='Third')
        self.year.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test is run '''
        self.year.delete()

    def test_year_creation(self):
        ''' method to test creation of year instances '''
        self.assertIsInstance(self.year, Year)
        self.assertEqual(len(Year.objects.all()), 1)


class TestSemester(TestCase):
    ''' test semester model class '''
    def setUp(self):
        ''' method called before each testcase '''
        self.sem = Semester(name='3')
        self.sem.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test is run '''
        self.sem.delete()

    def test_semester_creation(self):
        ''' method to test creation of semester instances '''
        self.assertIsInstance(self.sem, Semester)
        self.assertEqual(len(Semester.objects.all()), 1)



class TestType(TestCase):
    ''' test type model class '''
    def setUp(self):
        ''' method called before each testcase '''
        self.type = Type(name='Course Outline')
        self.type.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test is run '''
        self.type.delete()

    def test_type_creation(self):
        ''' method to test creation of type instances '''
        self.assertIsInstance(self.type, Type)
        self.assertEqual(len(Type.objects.all()), 1)


class TestMaterial(TestCase):
    ''' test material model class '''
    def setUp(self):
        ''' method called before each testcase '''
        self.user = User.objects.create_user(email='address@email.com', password='Password123')

        self.uni = University(name='Masinde Muliro')
        self.uni.save()

        self.unit = Unit(name='Electronics II')
        self.unit.save()
        
        self.year = Year(name='Third')
        self.year.save()
  
        self.sem = Semester(name='3')
        self.sem.save()

        self.type = Type(name='Course Outline')
        self.type.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test is run '''
        self.user.delete()
        self.uni.delete()
        self.course.delete()
        self.unit.delete()
        self.year.delete()
        self.sem.delete()
        self.type.delete()
        self.material.delete()

    def test_material_creation(self):
        ''' method to test creation of material instances '''
        self.material = Material(name='326: Software Development Course Outline', uploaded_by=self.user, date=datetime.now, 
                url='https://res.cloudinary.com/oceanic/image/upload/v1609160582/default_ynolea.png', image='https://res.cloudinary.com/tradity-capital/image/upload/v1609160582/default_ynolea.png',
                uni=self.uni, unit=self.unit, year=self.year, semester=self.sem, type_of_material=self.type)
        self.material.save()
        self.course = self.material.course.create(name='Computer Science')

        self.assertIsInstance(self.material, Material)
        self.assertEqual(len(Material.objects.all()), 1)
        self.assertEqual(self.material.name, '326: Software Development Course Outline')


class TestBook(TestCase):
    ''' test book model class '''
    def setUp(self):
        ''' method called before each testcase '''
        self.user = User.objects.create_user(email='address@email.com', password='Password123')

        self.unit = Unit(name='Electronics II')
        self.unit.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test is run '''
        self.user.delete()
        self.course.delete()
        self.unit.delete()
        self.book.delete()

    def test_book_creation(self):
        ''' method to test creation of book instances '''
        self.book = Book(name='Principles of Electronics', author='V.K. Mehta', uploaded_by=self.user, date=datetime.now, 
                url='https://res.cloudinary.com/oceanic/image/upload/v1609160582/default_ynolea.png', image='https://res.cloudinary.com/tradity-capital/image/upload/v1609160582/default_ynolea.png',
                unit=self.unit)
        self.book.save()
        self.course = self.book.course.create(name='Electronics and Electronics Engineering')

        self.assertIsInstance(self.book, Book)
        self.assertEqual(len(Book.objects.all()), 1)
        self.assertEqual(self.book.name, 'Principles of Electronics')
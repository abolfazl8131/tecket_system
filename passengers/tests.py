from django.test import TestCase
from.models import Passenger,SimpleUser
# Create your tests here.

class PassengerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        if not Passenger.objects.get(ID = 6090077194):

            Passenger.objects.create(ID = 6090077194 , 
                firstname='abolfazl' ,
                lastname='andalib',
                age = 21,
                gender='M',)


    def test_object_exists(self):

        obj = Passenger.objects.get(ID = 6090077194)
        self.assertEqual(obj.ID , 6090077194)

    def test_save_frequent_passenger(self):
        try:
            Passenger.objects.create(ID = 6090077194)
        except:
            pass
    
    def test_save_not_frequent_passenger(self):
        try:

            Passenger.objects.get(ID = 6090077195)
            
        except:
            Passenger.objects.create(ID = 6090077195 , firstname='ali' , lastname='amiri',gender='M',age=49)
        
        

    def test_update_object(self):
        obj = Passenger.objects.get(ID = 6090077194)

        obj.name = 'gholam'

        obj.save()

        self.assertNotEqual(obj.name , 'abolfazl')

    def test_soft_delete_object(self):
        obj = Passenger.objects.get(ID = 6090077194)
        obj.delete()
        self.assertEqual(obj.is_deleted , True)


class SimpleUserModelTest(TestCase):
    if not SimpleUser.objects.get(ID = 6090077194):
        SimpleUser.objects.create(ID = 6090077194 , 
                firstname='abolfazl' ,
                lastname='andalib',
                age = 21,
                gender='M',
                phone_number= 9170417381)


    def test_object_exists(self):

        obj = SimpleUser.objects.get(ID = 6090077194)
        self.assertEqual(obj.ID , 6090077194)

    def test_save_frequent_object(self):
        try:
            SimpleUser.objects.create(ID = 6090077194)
        except:
            pass
    
    def test_save_not_frequent_object(self):
        try:

            SimpleUser.objects.get(ID = 6090077195)
            
        except:
            SimpleUser.objects.create(ID = 6090077195 , firstname='ali' , lastname='amiri',gender='M',age=49,phone_number=90135634543)

    def test_update_object(self):
        obj = SimpleUser.objects.get(ID = 6090077194)

        obj.name = 'gholam'

        obj.save()

        self.assertNotEqual(obj.name , 'abolfazl')

    def test_soft_delete_object(self):
        obj = SimpleUser.objects.get(ID = 6090077194)
        obj.delete()
        self.assertEqual(obj.is_deleted , True)
    


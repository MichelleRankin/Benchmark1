from app.views import alarm_clock
from django.test import SimpleTestCase

# Create your tests here.
class TestSumDouble(SimpleTestCase):
    def test_double(self):
        response = self.client.get("/sum-double/4/4/")
        self.assertContains(response, "16")

    def test_add(self):
        response = self.client.get("/sum-double/3/4/")
        self.assertContains(response, "7")

    def test_multiple(self):
        response = self.client.get("/sum-double/6/5/")
        self.assertContains(response, "11")

class TestDaysOff(SimpleTestCase):
    def test_mon_true(self):
        response = self.client.get("/alarm-clock/True/1/")
        self.assertContains(response, "10:00")

    def test_sun_true(self):
        response = self.client.get("/alarm-clock/True/0/")
        self.assertContains(response, "off")

    def test_wed_true(self):
        response = self.client.get("/alarm-clock/False/3/")
        self.assertContains(response, "7:00")


class TestLuckySum(SimpleTestCase):
    def test_lucky_sum(self):
        response = self.client.get("/lucky-sum/13/4/5/")
        self.assertContains(response, "0")


    def test_all_add(self):
        response = self.client.get("/lucky-sum/2/2/2/")
        self.assertContains(response, "6")

    def test_add_b_c(self):
        response = self.client.get("/lucky-sum/2/4/13/")
        self.assertContains(response, "6")

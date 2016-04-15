from django.test import TestCase
from django.db import models
from django.test import SimpleTestCase
from django.test.utils import isolate_apps

class TestModelDefinition(SimpleTestCase):
    @isolate_apps('copysc')
    def test_model_definition(self):
	print('Hello Ryan')
	assert True

# Create your tests here.


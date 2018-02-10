import camelCase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelCase.camel_case('Hello World'))
        self.assertEqual('helloWorld', camelCase.camel_case('HELLO WORLD'))
        self.assertEqual('helloWorld', camelCase.camel_case('hello world'))

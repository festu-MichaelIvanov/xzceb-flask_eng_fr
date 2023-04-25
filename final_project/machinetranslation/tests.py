import unittest

from ibm_cloud_sdk_core.api_exception import ApiException

from translator import english_to_french, french_to_english


class TestEnglishToFrenchTranslation(unittest.TestCase): 

    def test_hello_translation(self): 
        self.assertEqual(english_to_french(english_text='Hello'), 'Bonjour')
        self.assertEqual(english_to_french(english_text='Bonjour'), 'Bonjour')

    def test_empty_translation(self):
        with self.assertRaises(ApiException):
            english_to_french(english_text='')


class TestFrenchToEnglishTranslation(unittest.TestCase): 

    def test_hello_translation(self): 
        self.assertEqual(french_to_english(french_text='Bonjour'), 'Hello')
        self.assertEqual(french_to_english(french_text='Hello'), 'Hello')

    def test_empty_translation(self):
        with self.assertRaises(ApiException):
            french_to_english(french_text='')


unittest.main()

from unittest import TestCase, main
from unittest.mock import MagicMock
from crawler_controller import CrawlerController

class TestCrwalerController(TestCase):

	def test_instance_object(self):
		crawler = CrawlerController()

	def test_return_false_if_page_status_different_200(self):
		url_qualquer = 'https://wwww.qualquer.com'
		crawler = CrawlerController()
		crawler.handle = MagicMock(return_value = False)
		assert crawler.handle(url_qualquer) == False




main()
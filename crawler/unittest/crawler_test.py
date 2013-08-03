import unittest
import crawler

class TestCrawler(unittest.TestCase):

  def setUp(self):
    print("setup")

  def test_format(self):
    url = crawler.formaturl("http://www.kuaidi100.com/network/net_%d_all_all_%d.htm",1,1)
    expected = "http://www.kuaidi100.com/network/net_1_all_all_1.htm"
    assert url == expected, 'error formating url'
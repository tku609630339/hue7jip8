from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式
from django.core.management import call_command


class 教典詞條試驗(TestCase):

    def test句數正確(self):
        call_command('教典詞條')
        self.assertGreater(訓練過渡格式.資料數量(), 25000)

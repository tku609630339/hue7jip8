from django.test.testcases import TestCase
from 臺灣言語資料庫.資料模型 import 外語表
from 臺灣言語資料庫.資料模型 import 文本表

# 測試：
# 台華下載
# 台華匯入

class 台華試驗(TestCase):
    def setUp(self):
        self.下載資料阿母 = {
            'ID':'12',
            '台語羅馬字': 'a-bo2',
            '台語羅馬字2': 'a-bu2',
            '台語漢字': '阿母',
            '華語對譯': ';母親;媽媽;',
            '英文': 'mother',
            'freq': '1884',
            'pos_h': 'Na'
        }
        self.下載資料鬱熱 = {
            'ID':'62024',
            '台語羅馬字': 'ut-joah8',
            '台語羅馬字2': '',
            '台語漢字': '鬱熱',
            '華語對譯': ';悶熱;',
            '英文': '',
            'freq': '536',
            'pos_h': 'VH'
        }
         
    def test下載詞目數正確(self):
        台華辭典陣列 = 某函式()
        self.assertCountEqual(台華辭典陣列, 62046)

    def test下載資料正確(self):
        台華辭典陣列 = 某函式()
        self.assertEqual(台華辭典陣列[12], self.下載資料阿母)
    
    def test匯入外語數量正確(self):
        # '華語對譯': ';母親;媽媽;',
        # '英文': 'mother',
        一筆query = 匯入一筆func(self.下載資料阿母)
        self.assertEqual(外語表.objects.count(), 3)
        
    def test匯入外語英文正確(self):
        一筆query = 匯入一筆func(self.下載資料阿母)
        外語表.objects.get(外語資料='mother')
        
    def test匯入外語華語正確(self):
        一筆query = 匯入一筆func(self.下載資料阿母)
        外語表.objects.get(外語資料='母親')
        外語表.objects.get(外語資料='媽媽')
        
    def test匯入文本數量正確(self):
        一筆query = 匯入一筆func(self.下載資料阿母)
        self.assertEqual(文本表.objects.count(), 6)
        
    def test匯入文本翻譯文本正確(self):
        一筆query = 匯入一筆func(self.下載資料阿母)
        一外語 = 外語表.objects.get(外語資料='母親')
        self.assertEqual(一外語.翻譯文本.count(), 2)
            
    def test匯入教羅轉臺羅(self):
        #62024, ut-joah8 -> ut-juah8
        一筆query = 匯入一筆func(self.下載資料鬱熱)
        一文本 = 文本表.objects.get(文本資料='鬱熱')
        self.assertEqual(一文本.音標資料, 'ut-juah8')
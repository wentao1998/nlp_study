Fasttext
===

数据集
---
使用的的数据集：清华大学的新闻分类文本数据集下载：https://thunlp.oss-cn-qingdao.aliyuncs.com/THUCNews.zip<br>
下载后进行解压，把相应的中文目录替换成以下英文名，方便程序读取数据<br>
['affairs','constellation','economic','edu','ent','fashion','game','home','house','lottery','science','sports','society','stock']<br>

安装fasttext
---
fasttext链接：https://www.lfd.uci.edu/~gohlke/pythonlibs/#fasttext<br>
打开链接安装对应的python版本<br>
安装时打开Anacona Prompt，cd到.whl文件所在位置<br>
pip install 文件名.whl即可

环境
---
python3.7<br>
cpu:i7-8750H<br>
Gpu:GTX-1050i<br>
在这个环境下分词阶段用了较长的时间，训练阶段很快

运行结果
---
`---------train done----------`<br>
`precision:    0.8601910575201334`<br>
`---------输出各类的统计情况----------`<br>
`['__label__edu', '__label__stock', '__label__lottery', '__label__economic', '__label__game', '__label__science', '__label__sports', '__label__house', '__label__ent', '__label__constellation', '__label__society', '__label__home', '__label__affairs', '__label__fashion']`<br>
`['house', 'sports', 'science', 'game', 'edu', 'ent', 'home', 'affairs', 'fashion', 'stock', 'society', 'economic']`<br>

`预测正确的各个类的数目: {'house': 9691, 'sports': 8054, 'science': 9600, 'game': 9427, 'edu': 9026, 'ent': 7592, 'home': 8751, 'affairs': 6743, 'fashion': 3249, 'stock': 7370, 'society': 9409, 'economic': 8607}`<br>

`测试数据集中各个类的数目: {'house': 10000, 'sports': 10000, 'science': 10000, 'game': 10000, 'edu': 10000, 'ent': 10000, 'home': 10000, 'affairs': 10000, 'fashion': 3369, 'stock': 10000, 'society': 10000, 'economic': 10000}`<br>

`预测结果中各个类的数目: {'__label__edu': 9723, '__label__stock': 9428, '__label__lottery': 1427, '__label__economic': 8856, '__label__game': 9693, '__label__science': 11558, '__label__sports': 8186, '__label__house': 11469, '__label__ent': 7924, '__label__constellation': 927, '__label__society': 12206, '__label__home': 9805, '__label__affairs': 7333, '__label__fashion': 4834}`<br>

`house:	 p:0.844973	 r:0.969100	 f:0.902790`<br>
`sports:	 p:0.983875	 r:0.805400	 f:0.885736`<br>
`science:	 p:0.830594	 r:0.960000	 f:0.890621`<br>
`game:	 p:0.972558	 r:0.942700	 f:0.957396`<br>
`edu:	 p:0.928314	 r:0.902600	 f:0.915277`<br>
`ent:	 p:0.958102	 r:0.759200	 f:0.847132`<br>
`home:	 p:0.892504	 r:0.875100	 f:0.883716`<br>
`affairs:	 p:0.919542	 r:0.674300	 f:0.778053`<br>
`fashion:	 p:0.672114	 r:0.964381	 f:0.792149`<br>
`stock:	 p:0.781714	 r:0.737000	 f:0.758699`<br>
`society:	 p:0.770850	 r:0.940900	 f:0.847429`<br>
`economic:	 p:0.971883	 r:0.860700	 f:0.912919`<br>

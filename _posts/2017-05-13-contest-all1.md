---
layout: post
title:  "第一轮 训练赛情况汇总"
---
- [第一次]({{site.url}}/2017/04/09/contest-1.html)
- [第二次]({{site.url}}/2017/04/23/contest-2.html)
- [第三次]({{site.url}}/2017/04/30/contest-3.html)
- [第四次]({{site.url}}/2017/05/06/contest4-2.html)
- [第五次]({{site.url}}/2017/05/10/contest5.html)

- [汇总excel]({{site.url}}/assets/1-all.xlsx)
- 汇总辅助程序
```python
import sys
import pprint
d = dict()
for name in sys.stdin:
    name = name.strip()
    if name not in d:
            d[name] = 1
    else:
            d[name] += 1
pprint.pprint(d)
print(len(d))
```

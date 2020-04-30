# 递归学习

## 学习计划与记录
2020-04-29 10:04:10
昨晚看完了视频，本周课程的核心主题是递归。以递归模板的实践应用结合超哥提供的心法：拒绝人肉递归、寻找最小重复、应用数学归纳法，一举搞定递归比较合适。

这两天的规划是：把超哥提到的题目都先给做了，就先来死磕递归。

```
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
	   process_result
	   return
    # process logic in current level
    process(level, data...)
    # drill down
    self.recursion(level + 1, p1, ...)
    # reverse the current level status if needed
```

lt70 要滚瓜烂熟，因为题目简单，先尝试傻递归，然后各种其他方式的实现。
lt22
lt226
lt98
lt104
lt111
lt297

https://time.geekbang.org/dailylesson/detail/100028406
看一下重学算法的递归的专栏

lt236
lt105
lt77
lt46
lt47

之后再升级，做分治和回溯的题目
lt50
lt78
lt169
lt17
lt51 八皇后


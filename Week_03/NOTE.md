# 递归学习

## 刷题笔记

2020-05-10 18:07:46
笔记都在每周提交的题目的py文件中了，我会把整个思考过程都记录下来。
从下周开始会在这里也再做一些总结，本周没时间了。

## 学习过程总结
2020-05-10 18:07:41

由于五一集中刷了两天的题，非常疲劳，后面休息了两天。周中又特别忙，所以本周效果不好。学习了[BruceLuo33](https://github.com/BruceLuo33/algorithm008-class01/blob/master/Week_03/README.md)的笔记之后有了新的认识。
因为根据我的时间记录，我在一道题上要花2小时，如果按照BruceLuo33的刷题节奏，14天刷了52题，其中还有几天休息或者产出不大，即使平均起来104小时在14天里，每天要大概7个多小时的时间，显然这是不现实的。所以问题在哪呢，问题在自己的学习方法上。
经过认真的思考，我的刷题方法有问题，还是不够效率，在于自己还是潜意识里想自己做出来。这一次的反思让自己彻底放弃了这个想法，要提高一道题的刷题效率。

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




## 使用场景

让我们来考虑如下问题（来自[wikipedia](https://en.wikipedia.org/wiki/Logistic_regression)）：

有20个学生花费不等的时间在复习考试上，其中一些最后通过了考试而另一些没有。根据统计出来的数据，如何找到复习时间与考试通过与否之间的关系？

| 复习时长（小时） | 0.50 | 0.75 | 1.00 | 1.25 | 1.50 | 1.75 | 1.75 | 2.00 | 2.25 | 2.50 | 2.75 | 3.00 | 3.25 | 3.50 | 4.00 | 4.25 | 4.50 | 4.75 | 5.00 | 5.50 |
| :--------------: | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|       通过       | 0    | 0    | 0    | 0    | 0    | 0    | 1    | 0    | 1    | 0    | 1    | 0    | 1    | 0    | 1    | 1    | 1    | 1    | 1    | 1    |

对于寻找变量之间相关性的问题，我们很容易想到使用线性回归 $Y = \omega^T X + b$。 如果说这里统计的因变量是考试分数，那当然没问题，但这里考试是否通过明显是一个二分类问题，其取值只能为0或1，这样线性回归这种预测连续变量的模型就不适用了。

怎么办呢？一个最直接的办法是设置一个阈值，比如复习时间 > 3 就通过，否则不通过，也即一个简单的感知机模型：$Y = sign(\omega^T X + b)$。但很多时候我们不光想得到一个分类结果，还想量化得到这个结果的可能性，也就是概率。但是我们还不能直接预测概率，因为概率是属于 $[0, 1]$ 区间，但 $\omega^T X + b$ 的值域是 $(-\infty,+\infty)$，所以我们**要么用一个映射函数把模型的输出限定在 $[0, 1]$ 区间之内**，**要么去预测一个值域在 $(-\infty,+\infty)$ 内且能转换成概率的函数**。

## logit函数

https://www.theanalysisfactor.com/link-functions-and-errors-in-logistic-regression/

https://en.wikipedia.org/wiki/Logistic_distribution

https://data.princeton.edu/wws509/notes/c3.pdf

https://stats.idre.ucla.edu/other/mult-pkg/faq/general/faq-how-do-i-interpret-odds-ratios-in-logistic-regression/

https://en.wikipedia.org/wiki/Logistic_regression

https://juejin.cn/post/6844904008293810183

https://datascience.stackexchange.com/questions/53226/what-is-the-purpose-of-logit-function-at-what-stage-of-model-building-process-t

https://towardsdatascience.com/logit-of-logistic-regression-understanding-the-fundamentals-f384152a33d1

https://zhuanlan.zhihu.com/p/44591359

https://zhuanlan.zhihu.com/p/100763009

https://zhuanlan.zhihu.com/p/34670728

https://zhuanlan.zhihu.com/p/34670728

https://github.com/arulrajnet/attila-demo


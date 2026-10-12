# Assignment1 实验报告

## Part 1

### 指标定义

| 指标      | 含义                                           | 使用场景                                                   |
| --------- | ---------------------------------------------- | ---------------------------------------------------------- |
| Accuracy  | 预测正确的样本数占总样本数的比例               | 类别分布较均衡分类任务                                     |
| MSE       | 预测值与真实值之差的平方的平均值               | 回归任务                                                   |
| Precision | 预测为正例的样本中，实际为正例的比例           | 假正例代价较高的分类任务                                   |
| Recall    | 所有实际为正例的样本中，被正确预测为正例的比例 | 假反例代价较高的分类任务                                   |
| F1        | Precision 和 Recall 的调和平均数               | 类别分布不均衡，而且需要平衡 Precision 和 Recall的分类任务 |

### 分类指标计算

$$
\text{Accuracy} = \frac{4}{9}\\
\\
\text{TP}=2, \text{FP}=1,\text{FN}=4,\text{TN}=2\\
\\
\text{Precision}=\frac{\text{TP}}{\text{TP}+\text{FP}}=\frac{2}{3}\\
\\
\text{Recall}=\frac{\text{TP}}{\text{TP}+\text{FN}}=\frac{1}{3}\\
\\
\text{F1}=\frac{2\times\text{Precision}*\text{Recall}}{\text{Precision}+\text{Recall}}=\frac{4}{9}
$$

### 运行日志

```
(base)  swift@Yimings-MacBook-Pro  ~/Desktop/FDU-PRML-2026Fall/Assignment1/classification   main ±  python3 test.py
============================================================
实验：Part 1 - 分类评测指标
姓名：张一鸣    学号：25803050045
时间：2026-10-12 18:30:00
============================================================
[BASIC] accuracy / MSE
 - accuracy expected 0.75 -> got 0.75 : PASS
 - mse      expected 0.6667 -> got 0.6667 : PASS
[PRF] precision / recall / f1 (binary)
 - precision expected 0.50 -> got 0.50 : PASS
 - recall    expected 0.50 -> got 0.50 : PASS
 - f1        expected 0.50 -> got 0.50 : PASS
```

## Part 2

### 运行日志

```
(base)  swift@Yimings-MacBook-Pro  ~/Desktop/FDU-PRML-2026Fall/Assignment1/decision_tree   main ±  python test_decision_tree.py

=== Criterion: info_gain ===
Accuracy: 0.9167
Tree depth: 5; leaves: 8

=== Criterion: info_gain_ratio ===
Accuracy: 0.9444
Tree depth: 7; leaves: 9

=== Criterion: gini ===
Accuracy: 0.8611
Tree depth: 6; leaves: 11

=== Criterion: error_rate ===
Accuracy: 0.8889
Tree depth: 5; leaves: 9
```

`Information Gain` 准则生成的树结构比较对称紧凑，叶节点最少，测试准确率比较高。

`Information Gain Ratio` 准则生成的树呈偏向一侧的链式结构，深度最大，测试准确率最高。

`Gini Index` 生成的树节点数最多，有 `gain` 只有 0.01 的分裂，有过拟合的倾向，测试准确率最低。

`Classification Error`生成的树结构和`Gini Index` 类似，但有 `gain` 为 0 的分裂。

## Part 3

### 运行日志

```
======================================================================
实验：Part 3 - kNN 分类
姓名：张一鸣    学号：25803050045    时间：2026-10-12 20:03:30
======================================================================
[DATA] Summary
 - train = 250, val = 125, test = 125, D = 2, classes = 4
   · train per-class: class 0: 62, class 1: 63, class 2: 62, class 3: 63
   · val per-class: class 0: 31, class 1: 31, class 2: 32, class 3: 31
   · test per-class: class 0: 32, class 1: 31, class 2: 31, class 3: 31
----------------------------------------------------------------------
[DIST] L2 two_loops vs no_loops
 - shape: (2, 4), max|diff| = 0.000e+00  -> PASS
[DIST] Cosine basic case
 - expected = [0.292893, 0.292893], got = [0.292893, 0.292893]  -> PASS
----------------------------------------------------------------------
[PRED] sanity checks (k=1 / k=3 / tie rule)
 - k=1 pred = [0, 1, 0]  (expect [0,1,0])  -> PASS
 - k=3 pred = [0, 1, 0]  (expect [0,1,0])  -> PASS
 - tie case (k=4) -> pred = 0 (expect 0) -> PASS
----------------------------------------------------------------------
[MODEL SELECTION] validation curve
 - ks & val_accs: k=1:0.7840, k=3:0.7840, k=5:0.8080, k=7:0.7920, k=9:0.8080, k=11:0.8240, k=13:0.8240
 - best_k = 11 (val_acc = 0.8240)
----------------------------------------------------------------------
[E2E] train+val -> test (metric=l2, mode=no_loops)
 - test_acc(best_k=11) = 0.8080
======================================================================
All kNN tests passed.
```

把`select_k_by_validation`和`knn_predict`的 `metric` 改为 `cosine` 后：

```
======================================================================
实验：Part 3 - kNN 分类
姓名：张一鸣    学号：25803050045    时间：2026-10-12 20:46:35
======================================================================
[DATA] Summary
 - train = 250, val = 125, test = 125, D = 2, classes = 4
   · train per-class: class 0: 62, class 1: 63, class 2: 62, class 3: 63
   · val per-class: class 0: 31, class 1: 31, class 2: 32, class 3: 31
   · test per-class: class 0: 32, class 1: 31, class 2: 31, class 3: 31
----------------------------------------------------------------------
[DIST] L2 two_loops vs no_loops
 - shape: (2, 4), max|diff| = 0.000e+00  -> PASS
[DIST] Cosine basic case
 - expected = [0.292893, 0.292893], got = [0.292893, 0.292893]  -> PASS
----------------------------------------------------------------------
[PRED] sanity checks (k=1 / k=3 / tie rule)
 - k=1 pred = [0, 1, 0]  (expect [0,1,0])  -> PASS
 - k=3 pred = [0, 1, 0]  (expect [0,1,0])  -> PASS
 - tie case (k=4) -> pred = 0 (expect 0) -> PASS
----------------------------------------------------------------------
[MODEL SELECTION] validation curve
 - ks & val_accs: k=1:0.7120, k=3:0.8000, k=5:0.7680, k=7:0.7920, k=9:0.8000, k=11:0.8160, k=13:0.8240
 - best_k = 13 (val_acc = 0.8240)
----------------------------------------------------------------------
[E2E] train+val -> test (metric=cosine)
 - test_acc(best_k=13) = 0.7680
======================================================================
All kNN tests passed.
```



![knn_k_curve_cosine](/Users/swift/Documents/Typora/images/knn_k_curve_cosine.png)

![knn_boundary_grid_l2](/Users/swift/Documents/Typora/images/knn_boundary_grid_l2.png)



![knn_k_curve_l2](/Users/swift/Documents/Typora/images/knn_k_curve_l2.png)

![knn_boundary_grid_cosine](/Users/swift/Documents/Typora/images/knn_boundary_grid_cosine.png)

L2 在验证集上的最优 k 是 11，测试准确率 0.8080，边界随 k 增大而变平滑。k=1、k=3 时边界有很多锯齿和零散色块，有过拟合情况，k=5 到 k=9 色块逐渐连成四块，k=13 边界最平滑，有一点欠拟合。

Cosine 在验证集上的最优 k 也是 11，验证准确率是 0.7680，边界是从原点射出的扇形，k=1 时细扇形很多，决策区被切得很碎，有过拟合情况，k 增大后细扇形并成更宽的扇形，k=13 时基本为 4 个扇形，扇形交界处的黑色叉变多，出现欠拟合的情况。

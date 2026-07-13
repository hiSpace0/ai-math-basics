import itertools, math

x = [11, 20, 22, 35]
n = len(x)
xbar = sum(x) / n

# 1) 用偏差(从均值)定义：传统写法，分母 n-1 还是 n ?
s2_nminus1 = sum((xi - xbar)**2 for xi in x) / (n - 1)
s2_n       = sum((xi - xbar)**2 for xi in x) / n
print(f"样本均值 xbar = {xbar}")
print(f"离均差平方和 Sum(xi-xbar)^2 = {sum((xi-xbar)**2 for xi in x)}")
print(f"样本方差(分母 n-1) s^2 = {s2_nminus1}")
print(f"平均平方偏差(分母 n)   s~^2 = {s2_n}")

# 2) 论文的核心：两两之间(半)偏差的均方 MS-PHD
pairs = list(itertools.combinations(range(n), 2))   # C(n,2) 对
C = len(pairs)
print(f"\n两两配对数量 C(n,2) = {C}")
PHD_sq_sum = sum(((x[i]-x[j])/2)**2 for i, j in pairs)
MS_PHD = PHD_sq_sum / C
print(f"所有 半偏差^2 之和 = {PHD_sq_sum}")
print(f"MS-PHD = (1/{C}) * 上述和 = {MS_PHD}")
print(f"样本方差 s^2 应等于 2 * MS-PHD = {2*MS_PHD}")

# 3) 展示代数消元：分子里那个 n 与组合数里的 n 抵消
sum_pairs_sq = sum((x[i]-x[j])**2 for i, j in pairs)
print(f"\nSum_{{i<j}} (xi-xj)^2 = {sum_pairs_sq}")
print(f"它恰好 = n * Sum(xi-xbar)^2 = {n*sum((xi-xbar)**2 for xi in x)}")
print("MS-PHD = [1/C(n,2)] * (1/4) * n * Sum(xi-xbar)^2")
print("       = [2/(n(n-1))] * (1/4) * n * Sum(...)  <- 分子n 与 分母n 抵消")
print("       = [1/(2(n-1))] * Sum(xi-xbar)^2 = s^2 / 2")
print(f"\n=> 抵消后分母剩下 (n-1) = {n-1}")

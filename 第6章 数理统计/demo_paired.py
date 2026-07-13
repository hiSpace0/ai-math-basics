import itertools

x = [11, 20, 22, 35]
n = len(x)
xbar = sum(x) / n

print("数据:", x, "  样本均值 xbar =", xbar, "  n =", n)
print("两两配对共有 C(n,2) =", n*(n-1)//2, "对\n")

print(f"{'点对(i,j)':<12}{'两两偏差|xi-xj|':<16}{'半偏差 /2':<12}{'半偏差^2':<10}")
pairs = list(itertools.combinations(range(n), 2))
half_sq_sum = 0
for i, j in pairs:
    pd  = abs(x[i] - x[j])          # 两两偏差
    phd = pd / 2                     # 半偏差
    sq  = phd**2
    half_sq_sum += sq
    print(f"({x[i]},{x[j]})".ljust(12), str(pd).ljust(16), f"{phd}".ljust(12), f"{sq}")

C = len(pairs)
MS_PHD = half_sq_sum / C
s2 = sum((xi - xbar)**2 for xi in x) / (n - 1)

print(f"\n半偏差^2 之和           = {half_sq_sum}")
print(f"MS-PHD = 和 / 配对数({C}) = {half_sq_sum} / {C} = {MS_PHD}")
print(f"样本方差 s^2            = {s2}")
print(f"2 * MS-PHD             = {2*MS_PHD}")
print(f"\n结论: s^2 = 2 * MS-PHD  ?  -> {abs(2*MS_PHD - s2) < 1e-9}")

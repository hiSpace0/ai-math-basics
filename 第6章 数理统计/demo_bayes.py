# 硬币: 10次抛掷 -> 7正3反
heads, tails, n = 7, 3, 10

# 各种先验 Beta(a,b)，看后验均值如何被拉向先验
priors = {"无信息/弱先验 Beta(2,2)": (2,2),
          "强先验(偏向公平) Beta(20,20)": (20,20),
          "强先验(偏向正面) Beta(20,5)": (20,5)}

print(f"MLE (只看数据) = {heads/n:.3f}\n")
print(f"{'先验':<28}{'先验均值':>8}{'后验均值':>10}")
for name,(a,b) in priors.items():
    prior_mean = a/(a+b)
    post_mean  = (a+heads)/(a+b+n)      # Beta后验均值
    print(f"{name:<28}{prior_mean:>8.3f}{post_mean:>10.3f}")

print("\n结论: 后验均值 = (先验 successes + 观测 heads) / (先验总数 + 观测总数)")
print("     数据越多, 后验越靠近 MLE; 先验越强, 后验越被拉向先验均值。")

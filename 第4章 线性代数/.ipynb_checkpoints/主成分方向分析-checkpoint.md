The user wants a detailed explanation of this specific plotting code block (figure ①). Let me explain each line thoroughly, connecting to the math.

This is the matplotlib code that draws the original data scatter with principal component directions. Let me break it down line by line.

Let me explain:
- ax = axs[0,0] — gets the subplot at row 0, col 0
- ax.scatter(X[:,0], X[:,1], ...) — scatter plot of original points, X[:,0] is all x-coordinates (column 0), X[:,1] is all y-coordinates (column 1)
- ax.scatter(mean[0], mean[1], ...) — plot the mean point as red X
- for loop over i in range(2): for each principal component
  - vec = eigvecs[:, i] * np.sqrt(eigvals[i]) — the eigenvector (column i) scaled by sqrt(eigenvalue). This gives the direction AND length of the PC axis.
  - ax.arrow(mean[0], mean[1], vec[0], vec[1], ...) — draw arrow starting at mean, with dx=vec[0], dy=vec[1]
  - color, width, head_width, length_includes_head, label
- ax.axvline, ax.axhline — dashed lines through the mean (reference axes at mean)
- set_title, set_xlabel, set_ylabel
- ax.legend() — show legend
- ax.grid(alpha=0.2) — grid
- ax.set_aspect('equal') — equal aspect ratio so the geometry isn't distorted

Let me also explain the math connection:
- eigvecs[:, i] is the unit eigenvector (direction of PC i)
- np.sqrt(eigvals[i]) scales it so the arrow length represents the standard deviation (spread) along that direction
- This visually shows that PC1 is longer (more variance) than PC2

Let me explain the arrow function signature: ax.arrow(x, y, dx, dy) draws arrow from (x,y) to (x+dx, y+dy).

length_includes_head=True means the head is counted within the length.

Let me write a clear, detailed explanation. I'll connect to the data values we computed earlier (eigvals = [10, 2], eigvecs columns = [1/√2, 1/√2] and [1/√2, -1/√2]).

So:
- PC1: vec = [1/√2, 1/√2] * √10 = [√5, √5] ≈ [2.236, 2.236]. Arrow from (4,6) to (4+2.236, 6+2.236) = (6.236, 8.236). Length = √10 ≈ 3.16.
- PC2: vec = [1/√2, -1/√2] * √2 = [1, -1]. Arrow from (4,6) to (5,5). Length = √2 ≈ 1.41.

So PC1 arrow is about 2.24× longer than PC2 in each component, visually showing more variance.

Let me write this all out. I'll structure it well with the math per line.

I should keep it focused on explaining this code block in detail. Let me be thorough since the user clearly wants deep
下面把**图①这段代码逐行拆开**讲，并说明每一行对应的几何/数学含义。

---

## 整体目标

这个子图要在**原始坐标系**里画出：
- 5 个原始数据点（蓝点）
- 数据均值点（红 X）
- 两条**主成分方向箭头**（红=PC1，绿=PC2），箭头长度代表该方向的方差大小

---

## 逐行详解

```python
ax = axs[0,0]
```
从 2×2 的子图网格里取出**第 0 行第 0 列**那个坐标系，后续所有 `ax.` 操作都画在这里。

```python
ax.scatter(X[:,0], X[:,1], s=90, c='steelblue', zorder=3)
```
画原始数据散点。
- `X[:,0]`：取所有行的第 0 列 → 全部 **x 坐标** `[2,2,4,8,4]`
- `X[:,1]`：取所有行的第 1 列 → 全部 **y 坐标** `[2,6,6,8,8]`
- `s=90`：点大小；`c='steelblue'`：蓝色；`zorder=3`：层级高，保证点在箭头**上层**不被盖住

```python
ax.scatter(mean[0], mean[1], s=160, c='red', marker='x', label='均值')
```
把均值点 \((\bar x,\bar y)=(4,6)\) 用**红色 X** 标出来，作为后面箭头的起点。

```python
for i in range(2):
```
对每个主成分（共 2 个）循环一次，分别画 PC1、PC2。

```python
    vec = eigvecs[:, i] * np.sqrt(eigvals[i])      # 轴长 = √特征值(方差)
```
这是**最关键的一行**，算箭头的"方向 + 长度"：
- `eigvecs[:, i]`：第 \(i\) 个**单位特征向量**（纯方向，长度=1），例如 PC1 是 \([1/\sqrt2,\ 1/\sqrt2]^T\)
- `np.sqrt(eigvals[i])`：特征值开方 = 该方向的**标准差**（散布半径）

两者相乘 → 一个既有方向、长度又等于 \(\sqrt{\lambda_i}\) 的向量。

代入我们之前算的值：
- PC1：\([1/\sqrt2,1/\sqrt2]\times\sqrt{10}=[\sqrt5,\sqrt5]\approx[2.24,2.24]\)，长度 \(\sqrt{10}\approx3.16\)
- PC2：\([1/\sqrt2,-1/\sqrt2]\times\sqrt2=[1,-1]\)，长度 \(\sqrt2\approx1.41\)

→ **PC1 箭头明显比 PC2 长，直观体现 PC1 方差（10）远大于 PC2（2）**。

```python
    ax.arrow(mean[0], mean[1], vec[0], vec[1],
```
画箭头。`ax.arrow(x, y, dx, dy)` 的语义是：**从点 \((x,y)\) 出发，画到 \((x+dx,\ y+dy)\)**。
- 起点 = 均值 \((4,6)\)
- 位移 = `vec`，即刚才算的方向向量
→ 箭头落在均值 + 主成分方向 × 标准差 的位置。

```python
             color=['red','green'][i], width=0.06, head_width=0.4,
             length_includes_head=True,
```
- `color=['red','green'][i]`：PC1 红、PC2 绿
- `width` / `head_width`：箭杆粗细 / 箭头大小（纯美观）
- `length_includes_head=True`：箭头总长度**包含**箭头头部，保证视觉长度和 \(\sqrt{\lambda}\) 一致

```python
             label=f'PC{i+1} (λ={eigvals[i]:.1f})')
```
给图例用的标签，例如 `PC1 (λ=10.0)`、`PC2 (λ=2.0)`。

```python
ax.axvline(mean[0], ls='--', c='gray', alpha=0.3)
ax.axhline(mean[1], ls='--', c='gray', alpha=0.3)
```
过均值点画一条**竖直虚线**和一条**水平虚线**（灰色、半透明），作为参考坐标轴，帮助眼睛判断均值位置和箭头方向。

```python
ax.set_title("① 原空间：数据点 + 主成分方向\n(轴越长=该方向方差越大)")
ax.set_xlabel("x1"); ax.set_ylabel("x2")
```
设置标题和横/纵坐标名称。`\n` 是换行。

```python
ax.legend(); ax.grid(alpha=0.2); ax.set_aspect('equal')
```
- `ax.legend()`：把 `label` 显示成图例
- `ax.grid(alpha=0.2)`：浅色网格，方便读数
- **`ax.set_aspect('equal')` 很重要**：强制 x、y 轴**等比例**，否则椭圆/箭头会被纵向或横向拉伸，几何关系失真（比如斜 45° 看起来不像 45°）

---

## 一句话总结这段代码

> 它把"均值点 + 沿特征向量方向、长度等于 \(\sqrt{\text{特征值}}\) 的箭头"画在原始数据散点图上——**箭头指向 = 主成分方向，箭头长短 = 该方向方差大小**，一眼就能看出哪个主成分更重要。

需要我把图②（协方差椭圆）和图④（新空间）也按这种"逐行 + 数学"的粒度拆讲一遍吗？
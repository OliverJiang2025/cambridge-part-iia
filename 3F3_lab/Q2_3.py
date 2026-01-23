import numpy as np
import matplotlib.pyplot as plt

# 1. 生成样本：10^6个服从U(0, 2π)的x样本
np.random.seed(42)  # 固定随机种子，结果可复现
x = np.random.uniform(0, 2 * np.pi, size=10**6)

# 2. 计算输出：y = min(sin(x), 0.7)
y = np.minimum(np.sin(x), 0.7)

# 计算y=0.7处的样本比例（验证理论概率）
ratio_07 = np.sum(y == 0.7) / len(y)
print(f"y=0.7处的样本比例: {ratio_07:.4f}（理论值≈0.184）")


# 3. 估计密度 + 4. 对比理论：绘制直方图+理论曲线
plt.figure(figsize=(10, 6))

# 绘制样本直方图（归一化为概率密度）
bins = np.linspace(-1, 0.8, 50)  # 覆盖y的取值范围（-1到0.7+）
plt.hist(y, bins=bins, density=True, alpha=0.5, color='skyblue', label='样本直方图')

# 绘制y < 0.7的理论概率密度曲线
y_theory = np.linspace(-1, 0.7, 200)
pdf_theory = 1 / (np.pi * np.sqrt(1 - y_theory**2))  # 理论密度公式
plt.plot(y_theory, pdf_theory, 'r-', linewidth=2, label=r'理论密度 $1/(\pi\sqrt{1-y^2})$')

# 标记y=0.7的位置（样本集中区）
plt.axvline(x=0.7, color='green', linestyle='--', linewidth=2, label=r'$y=0.7$（理论比例≈18.4%）')

# 图表美化
plt.legend(fontsize=12)
plt.title(r'$y = \min(\sin(x), 0.7)$ 的概率密度（$x \sim \mathcal{U}(0, 2\pi)$）', fontsize=14)
plt.xlabel('y', fontsize=12)
plt.ylabel('概率密度', fontsize=12)
plt.grid(alpha=0.3)

plt.show()
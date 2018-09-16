# 1

import statistics

nums = [3, 42, 322, 4, 3, 43, 5, 66, 889, 24]

print(statistics.median(nums))  # 33.0
print(statistics.mean((nums)))  # 140.1

# 平均値に比べ、中央値は外れ値（889）に対して堅牢(robust)である。

print(statistics.median_low(nums))   # 24  偶数個のデータの場合、中心の二つの値の小さな方。
print(statistics.median_high(nums))  # 42  偶数個のデータの場合、中心の二つの値の大きな方。

print(statistics.harmonic_mean(nums)) # 8.164...  逆数の算術平均の逆数。

print(statistics.stdev(nums))  # 280.1445....  不偏分散による標準偏差

# 2

import cubed

print(cubed.cube_it(3))

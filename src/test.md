```python
# 读入数据
n, a, b = map(int, input().split())

# 初始化二维矩阵
mp = [[0]*1011 for i in range(1011)]
# 将敌人放入矩阵
for i in range(n):
    x, y = map(int, input().split())
    mp[x][y] += 1       
# 对矩阵求前缀和
for i in range(1, 1011):
    for j in range(1, 1011):
        # 转移方程解释见Oi-Wiki
        mp[i][j] += mp[i-1][j] + mp[i][j-1] - mp[i-1][j-1]
# 枚举技能矩阵(的右下角)
ans = 0
for i in range(a+1, 1011):  #枚举右上端点
    for j in range(b+1, 1011):      #此时枚举的矩形为 (i-a, j-b) 到 (i,j)之间的矩形
        t = mp[i][j] - mp[i-a-1][j] - mp[i][j-b-1] + mp[i-a-1][j-b-1]
        ans = max(ans, t)
print(ans)
```


import numpy as np

def riemann_integration():
    # 分割點數目
    n = 100  # 將區間 [0,1] 分為 n 個小區間
    dx = 1 / n  # x 軸方向每個小區間的寬度
    dy = 1 / n  # y 軸方向每個小區間的寬度
    dz = 1 / n  # z 軸方向每個小區間的寬度

    integral = 0  # 初始化積分值
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # x, y, z 分別取區間的左端點
                x = i * dx
                y = j * dy
                z = k * dz
                # 計算函數值 f(x, y, z)
                f_xyz = 3 * x**2 + y**2 + 2 * z**2
                # 累加小立方體的貢獻值
                integral += f_xyz * dx * dy * dz

    return integral

def monte_carlo_integration():
    # 隨機點數目
    num_points = 100000  # 在 [0,1]^3 區域內生成的隨機點數

    # 在區間 [0,1]^3 中隨機取點
    x = np.random.uniform(0, 1, num_points)  # 隨機生成 x 坐標
    y = np.random.uniform(0, 1, num_points)  # 隨機生成 y 坐標
    z = np.random.uniform(0, 1, num_points)  # 隨機生成 z 坐標

    # 計算函數值 f(x, y, z) = 3x^2 + y^2 + 2z^2
    f_xyz = 3 * x**2 + y**2 + 2 * z**2

    # 估算積分值
    volume = 1 * 1 * 1  # 區間 [0,1]^3 的體積為 1
    integral = volume * np.mean(f_xyz)  # 平均函數值乘以區域體積即為積分值

    return integral

# 計算積分
riemann_result = riemann_integration()  # 使用黎曼積分計算結果
monte_carlo_result = monte_carlo_integration()  # 使用蒙地卡羅法計算結果

# 輸出結果
print("黎曼積分結果:", riemann_result)
print("蒙地卡羅法結果:", monte_carlo_result)

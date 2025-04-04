from model import main_program
import numpy as np

# Test Case 1: Bộ dữ liệu với một hàm bậc 2 (Parabola)
def testcase1():
    X = np.arange(0, 1000, 0.1).reshape(-1, 1)
    X_flatten = X.flatten()
    Y = X_flatten**2 + 3*X_flatten - 4 + np.random.rand(X.shape[0])

    # Dự đoán Y0 cho X0 = 0
    X0 = 0
    return main_program(X, Y, X0)



# Test Case 2: Bộ dữ liệu tuyến tính (Linear)
def testcase2():
    X = np.arange(0, 1000, 0.1).reshape(-1, 1)
    X_flatten = X.flatten()
    Y = 2*X_flatten + 5 + np.random.rand(X.shape[0])

    # Dự đoán Y0 cho X0 = 50
    X0 = 50
    return main_program(X, Y, X0)



# Test Case 3: Dữ liệu phân tán ngẫu nhiên (Random Scatter)
def testcase3():
    X = np.arange(0, 100, 0.5).reshape(-1, 1)
    X_flatten = X.flatten()
    Y = np.random.rand(X.shape[0])

    # Dự đoán Y0 cho X0 = 30
    X0 = 30
    return main_program(X, Y, X0)



# Test Case 4: Dữ liệu với mối quan hệ bậc 3 (Cubic Relationship)
def testcase4():
    X = np.arange(0, 100, 0.1).reshape(-1, 1)
    X_flatten = X.flatten()
    Y = 0.1*X_flatten**3 - 2*X_flatten**2 + 3*X_flatten + 10 + np.random.rand(X.shape[0])

    # Dự đoán Y0 cho X0 = 50
    X0 = 50
    return main_program(X, Y, X0)



# Test Case 5: Dữ liệu có xu hướng giảm (Decreasing Trend)
def testcase5():
    X = np.arange(0, 100, 0.5).reshape(-1, 1)
    X_flatten = X.flatten()
    Y = -2*X_flatten + 100 + np.random.rand(X.shape[0])

    # Dự đoán Y0 cho X0 = 30
    X0 = 30
    return main_program(X, Y, X0)



# Test Case 6: Dữ liệu không có sự tương quan rõ ràng (No Clear Relationship)
def testcase6():
    X = np.random.rand(100).reshape(-1, 1) * 100
    Y = np.random.rand(100)

    # Dự đoán Y0 cho X0 = 50
    X0 = 50
    return main_program(X, Y, X0)



# Test Case 7: Dữ liệu chỉ có một điểm (Single Data Point)
def testcase7():
    X = np.array([1]).reshape(-1, 1)
    Y = np.array([3])

    # Dự đoán Y0 cho X0 = 1
    X0 = 1
    return main_program(X, Y, X0)



# Test Case 8: Dữ liệu có mối quan hệ mạnh với nhiễu (Strong Relationship with Noise)
def testcase8():
    X = np.arange(0, 1000, 0.1).reshape(-1, 1)
    X_flatten = X.flatten()
    Y = 2*X_flatten + 10 + np.random.randn(X.shape[0]) * 100  # Thêm nhiễu ngẫu nhiên

    # Dự đoán Y0 cho X0 = 200
    X0 = 200
    return main_program(X, Y, X0)



# Test Case 9: Bộ dữ liệu nhỏ (Small Dataset)
def testcase9():
    X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
    Y = np.array([2, 4, 6, 8, 10])

    # Dự đoán Y0 cho X0 = 3
    X0 = 3
    return main_program(X, Y, X0)



# Test Case 10: Dữ liệu với xu hướng theo hàm số mũ (Exponential Trend)
def testcase10():
    X = np.arange(1, 20, 0.5).reshape(-1, 1)
    X_flatten = X.flatten()
    Y = np.exp(X_flatten) + np.random.rand(X.shape[0])

    # Dự đoán Y0 cho X0 = 10
    X0 = 10
    return main_program(X, Y, X0)



testcases = [testcase1(), testcase2(), testcase3(), testcase4(), testcase5(), testcase6(), testcase7(), testcase8(), testcase9(), testcase10()]
for testcase_index, result_json in enumerate(testcases):
    print(f"Kết quả ở testcase {testcase_index + 1} : {result_json}")

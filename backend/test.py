import unittest
import numpy as np
from model import main_program


class TestMainProgram(unittest.TestCase):
    
    # Test Case 1: Bộ dữ liệu với một hàm bậc 2 (Parabola)
    def test_case1(self):
        X = np.arange(0, 1000, 0.1).reshape(-1, 1)
        X_flatten = X.flatten()
        Y = X_flatten**2 + 3*X_flatten - 4 + np.random.rand(X.shape[0])
        X0 = 0
        result = main_program(X, Y, X0)
        self.assertIsNotNone(result, "Kết quả không hợp lệ")


    # Test Case 2: Bộ dữ liệu tuyến tính (Linear)
    def test_case2(self):
        X = np.arange(0, 1000, 0.1).reshape(-1, 1)
        X_flatten = X.flatten()
        Y = 2*X_flatten + 5 + np.random.rand(X.shape[0])
        X0 = 50
        result = main_program(X, Y, X0)
        self.assertIsNotNone(result, "Kết quả không hợp lệ")


    # Test Case 3: Dữ liệu phân tán ngẫu nhiên (Random Scatter)
    def test_case3(self):
        X = np.arange(0, 100, 0.5).reshape(-1, 1)
        X_flatten = X.flatten()
        Y = np.random.rand(X.shape[0])
        X0 = 30
        result = main_program(X, Y, X0)
        self.assertIsNotNone(result, "Kết quả không hợp lệ")


    # Test Case 4: Dữ liệu với mối quan hệ bậc 3 (Cubic Relationship)
    def test_case4(self):
        X = np.arange(0, 100, 0.1).reshape(-1, 1)
        X_flatten = X.flatten()
        Y = 0.1*X_flatten**3 - 2*X_flatten**2 + 3*X_flatten + 10 + np.random.rand(X.shape[0])
        X0 = 50
        result = main_program(X, Y, X0)
        self.assertIsNotNone(result, "Kết quả không hợp lệ")


    # Test Case 5: Dữ liệu có xu hướng giảm (Decreasing Trend)
    def test_case5(self):
        X = np.arange(0, 100, 0.5).reshape(-1, 1)
        X_flatten = X.flatten()
        Y = -2*X_flatten + 100 + np.random.rand(X.shape[0])
        X0 = 30
        result = main_program(X, Y, X0)
        self.assertIsNotNone(result, "Kết quả không hợp lệ")


    # Test Case 6: Dữ liệu không có sự tương quan rõ ràng (No Clear Relationship)
    def test_case6(self):
        X = np.random.rand(100).reshape(-1, 1) * 100
        Y = np.random.rand(100)
        X0 = 50
        result = main_program(X, Y, X0)
        self.assertIsNotNone(result, "Kết quả không hợp lệ")


    # Test Case 7: Dữ liệu chỉ có một điểm (Single Data Point)
    def test_case7(self):
        X = np.array([1]).reshape(-1, 1)
        Y = np.array([3])
        X0 = 1
        result = main_program(X, Y, X0)
        self.assertIsNotNone(result, "Kết quả không hợp lệ")


    # Test Case 8: Dữ liệu có mối quan hệ mạnh với nhiễu (Strong Relationship with Noise)
    def test_case8(self):
        X = np.arange(0, 1000, 0.1).reshape(-1, 1)
        X_flatten = X.flatten()
        Y = 2*X_flatten + 10 + np.random.randn(X.shape[0]) * 100  # Thêm nhiễu ngẫu nhiên
        X0 = 200
        result = main_program(X, Y, X0)
        self.assertIsNotNone(result, "Kết quả không hợp lệ")


    # Test Case 9: Bộ dữ liệu nhỏ (Small Dataset)
    def test_case9(self):
        X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
        Y = np.array([2, 4, 6, 8, 10])
        X0 = 3
        result = main_program(X, Y, X0)
        self.assertIsNotNone(result, "Kết quả không hợp lệ")


    # Test Case 10: Dữ liệu với xu hướng theo hàm số mũ (Exponential Trend)
    def test_case10(self):
        X = np.arange(1, 20, 0.5).reshape(-1, 1)
        X_flatten = X.flatten()
        Y = np.exp(X_flatten) + np.random.rand(X.shape[0])
        X0 = 10
        result = main_program(X, Y, X0)
        self.assertIsNotNone(result, "Kết quả không hợp lệ")



if __name__ == '__main__':
    unittest.main()

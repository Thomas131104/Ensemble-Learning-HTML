import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from json import dumps



# Định nghĩa các mô hình trong biến toàn cục
MODELS = {
    "LinearRegression": LinearRegression(),
    "Lasso": Lasso(max_iter=10000),
    "Ridge": Ridge(),
    "ElasticNet": ElasticNet(max_iter=10000),
    "DecisionTreeRegressor": DecisionTreeRegressor(),
    "RandomForestRegressor": RandomForestRegressor(),
    "SVR": SVR()
}



# Hàm build mô hình, tính RMSE và dự đoán Y0
def build_model(X, Y, X0, model):
    """
    X: Dữ liệu đầu vào
    Y: Dữ liệu mục tiêu
    X0: Dữ liệu đầu vào cho việc dự đoán Y0 (có thể là một giá trị duy nhất)
    model: Một trong các mô hình trong MODELS
    
    Trả về:
    - RMSE (Root Mean Squared Error)
    - Dự đoán Y0 (dự đoán giá trị cho X0)
    """
    # Chia dữ liệu thành train và test
    n = X.shape[0]
    if n <= 10:
        X_train, X_test, Y_train, Y_test = X, X, Y, Y
    elif 10 < n <= 100:
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    else:
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

    # Huấn luyện mô hình
    model.fit(X_train, Y_train)

    # Dự đoán trên tập test
    Y_pred = model.predict(X_test)
    
    # Tính toán RMSE
    rmse = np.sqrt(mean_squared_error(Y_test, Y_pred))

    # Dự đoán Y0 (dự đoán giá trị cho X0)
    Y0 = model.predict([[X0]])

    return rmse, Y0[0]



# Hàm chính để chọn mô hình tốt nhất và tìm Y0 cho mô hình đó
def main_program(X: list, Y: list, X0: list):
    """
    Hàm chính để xác định mô hình hồi quy có RMSE thấp nhất và dự đoán Y0 cho X0.

    Các tham số:
    - X (list): Danh sách các giá trị đầu vào (biến độc lập), được chuyển đổi thành numpy array.
    - Y (list): Danh sách các giá trị mục tiêu (biến phụ thuộc), được chuyển đổi thành numpy array.
    - X0 (list): Danh sách các giá trị đầu vào cho việc dự đoán, sẽ được sử dụng với mô hình tốt nhất.

    Trả về:
    - str: Chuỗi JSON chứa thông tin về mô hình tốt nhất, RMSE của nó và các dự đoán Y0.
    """
    X = np.array(X).reshape(-1, 1)
    Y = np.array(Y)
    X0 = np.array(X0)

    best_model = None
    min_rmse = float('inf')  # Giá trị RMSE tối thiểu
    best_Y0 = None

    # Duyệt qua các mô hình
    for model_name, model in MODELS.items():
        rmse, Y0 = build_model(X, Y, X0, model)

        # Cập nhật nếu tìm được mô hình có RMSE nhỏ hơn
        if rmse < min_rmse:
            min_rmse = rmse
            best_model = model_name
            best_Y0 = Y0

    # In kết quả
    return dumps({
        "best_model": best_model,
        "min_rmse" : min_rmse,
        "best_Y0" : best_Y0
    })
import eel
import sys
import numpy as np
import json
from backend.model import main_program  # Import hàm từ model.py

# Đảm bảo đường dẫn đúng
eel.init('web')  # Thư mục web chứa các file frontend như index.html

@eel.expose
def predict(X, Y, x_predict):
    try:
        print(f"Received from frontend - X: {X}, Y: {Y}, X_predict: {x_predict}")

        if not X or not Y or x_predict == '':
            return json.dumps({"error": "Dữ liệu không hợp lệ!"})

        X = np.array(X, dtype=float).reshape(-1, 1)
        Y = np.array(Y, dtype=float)
        x_predict = float(x_predict)

        result = main_program(X, Y, x_predict)
        print("Kết quả từ app.py", result)
        return result
    except Exception as e:
        print(f"Error occurred: {e}")
        return json.dumps({"error": str(e)})


# Chạy ứng dụng Eel
if __name__ == "__main__":
    try:
        eel.start('index.html', size=(800, 600))
    except KeyboardInterrupt:
        print("Chương trình đang ngắt")
        sys.exit(0)
    except Exception as e:
        print(e)
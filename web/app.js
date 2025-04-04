// Khởi tạo ứng dụng AngularJS
var app = angular.module('myApp', []);



app.service('scatterDataService', function() {
    var xValues = [];
    var yValues = [];

    return {
        setData: function(x, y) {
            xValues = x;
            yValues = y;
        },
        getData: function() {
            return { xValues: xValues, yValues: yValues };
        }
    };
});



app.factory('eel', function() {
    return eel;  // Assuming eel is a Python-Eel bridge object
});



// Controller để xử lý nhập liệu và vẽ biểu đồ scatter
app.controller('scatterPlotController', function($scope, scatterDataService, eel) {
    // Khởi tạo các biến
    $scope.xPlot = "";
    $scope.yPlot = "";
    $scope.message = "";
    $scope.status = false;
    $scope.noiseSelection = "noNoise";
    $scope.noiseLevel = 0;
    $scope.xPredict = "";  // Thêm biến cho giá trị X dự đoán
    $scope.predictedY = "";  // Thêm biến cho giá trị Y dự đoán

    // Hàm xử lý khi người dùng nhấn nút OK
    $scope.processData = function() {
        $scope.status = false;
        $scope.message = validateInputs();
    
        if ($scope.message) {
            alert($scope.message);
        } else {
            $scope.xValues = parseValues($scope.xPlot);
            $scope.yValues = parseValues($scope.yPlot);
            if ($scope.xValues.length === $scope.yValues.length) {
                $scope.status = true;
                addNoiseIfRequired();
                $scope.drawChart();
    
                // Lưu dữ liệu vào service sau khi xử lý
                scatterDataService.setData($scope.xValues, $scope.yValues);
            } else {
                $scope.message = "Số lượng giá trị X và Y không khớp.";
                alert($scope.message);
            }
        }
    };
    

    // Hàm kiểm tra các giá trị nhập
    function validateInputs() {
        if (!$scope.xPlot || !$scope.yPlot) {
            return "Vui lòng nhập đầy đủ các giá trị X và Y.";
        }
        return "";
    }

    // Hàm phân tích giá trị đầu vào thành mảng số
    function parseValues(input) {
        return input.split(',').map(function(val) {
            return parseFloat(val.trim());
        });
    }

    // Hàm xử lý thêm nhiễu vào dữ liệu y
    function addNoiseIfRequired() {
        if ($scope.noiseSelection === "withNoise" && $scope.noiseLevel > 0) {
            $scope.yValues = $scope.yValues.map(function(y) {
                var noise = (Math.random() * 2 - 1) * $scope.noiseLevel;
                return y + noise;
            });
        }
    }

    // Hàm vẽ biểu đồ
    $scope.drawChart = function() {
        var ctx = document.getElementById("myScatterChart").getContext("2d");

        var scatterData = {
            datasets: [{
                label: "Dữ liệu Scatter",
                data: $scope.xValues.map((x, i) => ({ x: x, y: $scope.yValues[i] })),
                backgroundColor: "rgba(0, 0, 0, 1)",
                borderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 1
            }]
        };

        // Hủy biểu đồ cũ nếu có (tránh vẽ đè)
        if ($scope.myChart) {
            $scope.myChart.destroy();
        }

        // Vẽ lại biểu đồ
        setTimeout(function() {
            $scope.myChart = new Chart(ctx, {
                type: "scatter",
                data: scatterData,
                options: getChartOptions()
            });
        }, 1000);
    };

    // Hàm trả về các tùy chọn cho biểu đồ
    function getChartOptions() {
        return {
            scales: {
                x: {
                    type: "linear",
                    position: "bottom",
                    grid: { color: "rgba(0, 0, 0, 1)" },
                    ticks: { color: "rgba(0, 0, 0, 1)" },
                    title: { display: true, text: 'Trục X (Giá trị X)', color: "rgba(0, 0, 0, 1)", font: { size: 14 } }
                },
                y: {
                    beginAtZero: true,
                    grid: { color: "rgba(0, 0, 0, 1)" },
                    ticks: { color: "rgba(0, 0, 0, 1)" },
                    title: { display: true, text: 'Trục Y (Giá trị Y)', color: "rgba(0, 0, 0, 1)", font: { size: 14 } }
                }
            },
            plugins: {
                legend: { labels: { color: "rgba(0, 0, 0, 1)" } },
                title: {
                    display: true,
                    text: 'Biểu đồ Scatter',
                    color: "rgba(0, 0, 0, 1)",
                    font: { size: 14 }
                }
            }
        };
    }
});



app.controller("predictionController", function ($scope, scatterDataService, eel) {
    $scope.xPredict = "";  
    $scope.best_Y0 = null;  
    $scope.best_model = null;  
    $scope.min_rmse = null;  

    // Hàm dự đoán giá trị Y từ X
    $scope.predictValues = function() {
        var plotData = scatterDataService.getData();
    
        if (!plotData.xValues || plotData.xValues.length === 0) {
            alert("Không có dữ liệu để dự đoán!");
            return;
        }
    
        eel.predict(plotData.xValues, plotData.yValues, $scope.xPredict)(function(predictedY) {
            console.log("Dữ liệu từ Python:", predictedY);
    
            try {
                // Parse JSON và lưu vào $scope.result
                $scope.result = JSON.parse(predictedY);
                console.log("Kết quả sau khi parse JSON:", $scope.result);
    
                // Kiểm tra và cập nhật giá trị vào scope
                $scope.$apply(function() {
                    $scope.best_Y0 = $scope.result.best_Y0;
                    $scope.best_model = $scope.result.best_model;
                    $scope.min_rmse = $scope.result.min_rmse;
                });
    
                // Kiểm tra giá trị đã được cập nhật
                console.log("Sau khi cập nhật: ", $scope.best_Y0, $scope.best_model, $scope.min_rmse);
            } catch (error) {
                console.error("Lỗi khi parse JSON:", error);
                alert("Lỗi xử lý dữ liệu!");
            }
        });
    };
});
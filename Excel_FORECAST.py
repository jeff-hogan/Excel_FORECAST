import math


def forecast(x, x_values, y_values):
    # excel forecast.linear function
    # https://support.microsoft.com/en-us/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99
    if len(x_values) != len(y_values):
        return None

    x_mean = sum(x_values) / len(x_values)
    y_mean = sum(y_values) / len(y_values)

    Numerator = 0
    Denominator = 0
    for i in range(len(y_values)):
        Numerator += (x_values[i] - x_mean) * (y_values[i] - y_mean)
        Denominator += (x_values[i] - x_mean) ** 2.0

    b = Numerator / Denominator
    a = y_mean - b * x_mean

    forecast = a + b * x
    return forecast


xv = [20, 28, 31, 38, 40]
yv = [6, 7, 9, 15, 21]
print(forecast(30, xv, yv))  # should be 10.607253

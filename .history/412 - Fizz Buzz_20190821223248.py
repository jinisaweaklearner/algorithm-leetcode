# add trend
for i in range(0, len(ts)):
    ts[i] = ts[i] + ((a * i) + b)

for i in range(0, fh):
    y_hat_test_MLP[i] = y_hat_test_MLP[i] + ((a * (len(ts) + i + 1)) + b)
    y_hat_test_RNN[i] = y_hat_test_RNN[i] + ((a * (len(ts) + i + 1)) + b)

# add seasonality
for i in range(0, len(ts)):
    ts[i] = ts[i] * seasonality_in[i % freq] / 100

for i in range(len(ts), len(ts) + fh):
    y_hat_test_MLP[i - len(ts)] = y_hat_test_MLP[i - len(ts)] * seasonality_in[i % freq] / 100
    y_hat_test_RNN[i - len(ts)] = y_hat_test_RNN[i - len(ts)] * seasonality_in[i % freq] / 100

# check if negative or extreme
for i in range(len(y_hat_test_MLP)):
    if y_hat_test_MLP[i] < 0:
        y_hat_test_MLP[i] = 0
    if y_hat_test_RNN[i] < 0:
        y_hat_test_RNN[i] = 0
        
    if y_hat_test_MLP[i] > (1000 * max(ts)):
        y_hat_test_MLP[i] = max(ts)         
    if y_hat_test_RNN[i] > (1000 * max(ts)):
        y_hat_test_RNN[i] = max(ts)
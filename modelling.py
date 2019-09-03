import numpy as np
import pandas as pd
import csv
import math
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from statistics import mean, stdev

chi_data = pd.read_csv('transformed_data.csv', index_col=0)
features = list(chi_data.columns)

scaler = StandardScaler()
scaled_chi_data = pd.DataFrame(data=scaler.fit_transform(chi_data), columns=chi_data.columns, index=chi_data.index)

y = scaled_chi_data['total_rides']
X = scaled_chi_data[['is_sat','is_holi','avg_precip','temp_mid','temp_rng',
                  'temp_bs','hum_mid','hum_rng','wind_mid','wind_rng','pres_mid','pres_rng']]

num_folds = 5

kfold = KFold(num_folds, True, 34)
# kfold_split = kfold.split(new_chi_data)

alpha_exps = np.linspace(-2,6,17)
L1L2_ratios = np.linspace(0,1,21)
L1L2_ratios[0] = 0.01
# model_grid = {round(alpha_exp,3):
#               {round(L1L2_ratio,3): [] for L1L2_ratio in L1L2_ratios}
#                   for alpha_exp in alpha_exps}

grid = {round(alpha_exp,3):
            {round(L1L2_ratio,3): 
                {'models': [],
                 'MSEs': [],
                 'RMSEs': [],
                 'training_scores': [],
                 'test_scores': []}
                    for L1L2_ratio in L1L2_ratios}
                        for alpha_exp in alpha_exps}


for alpha_exp in grid:
    alpha = pow(10,alpha_exp)
    for L1L2_ratio in grid[alpha_exp]:
        # experiment = grid[alpha_exp][L1L2_ratio]
        # print(f'running experiment with alpha_exp={alpha_exp} and L1L2_ratio={L1L2_ratio}')
        for train, test in kfold.split(y):
            # print(len(train), len(test))
            X_train = X.iloc[train]
            X_test = X.iloc[test]
            y_train = y.iloc[train]
            y_test = y.iloc[test]

            model = ElasticNet(alpha=alpha, l1_ratio=L1L2_ratio, random_state=34)
            model.fit(X_train, y_train)
            
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            rmse = math.sqrt(mse)

            training_score = model.score(X_train, y_train)
            test_score = model.score(X_test, y_test)

            grid[alpha_exp][L1L2_ratio]['models'].append(model)
            grid[alpha_exp][L1L2_ratio]['MSEs'].append(mse)
            grid[alpha_exp][L1L2_ratio]['RMSEs'].append(rmse)
            grid[alpha_exp][L1L2_ratio]['training_scores'].append(training_score)
            grid[alpha_exp][L1L2_ratio]['test_scores'].append(test_score)
    

        
for alpha_exp in grid:
    alpha = pow(10,alpha_exp)
    for L1L2_ratio in grid[alpha_exp]:
# scaler.inverse_transform(X and y...)

# Print x,y and z values
print(x_values)
print(y_values)
print(z_values)

# Provide a title for the contour plot
plot.title('Contour plot')

# Set x axis label for the contour plot
plot.xlabel('X')

# Set y axis label for the contour plot
plot.ylabel('Y')

# Create contour lines or level curves using matplotlib.pyplot module
contours = plot.contour(x_values, y_values, z_values)

# Display z values on contour lines
plot.clabel(contours, inline=1, fontsize=10)

# Display the contour plot
plot.show()
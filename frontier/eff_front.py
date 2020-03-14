import os
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import scipy.optimize as sco


def efficient_frontier(allocations):
    header = []
    header.append(allocations.aa_1)
    header.append(allocations.aa_2)
    header.append(allocations.aa_3)
    header.append(allocations.aa_4)
    header.remove('none')
    count = len(header)
    
    cov_matrix = pd.read_csv("/Users/hlevin/turing/aa_application/frontier/data/cov_matrix.csv", index_col=0)
    cov_matrix = cov_matrix.loc[header, header]
    returns_table = pd.read_csv("/Users/hlevin/turing/aa_application/frontier/data/returns.csv", index_col=0)
    mean_returns = returns_table.loc[header, ['Expected Return (Nominal)']]
    mean_returns = mean_returns['Expected Return (Nominal)']

    np.random.seed(42)
    num_ports = 6000
    all_weights = np.zeros((num_ports, count))
    ret_arr = np.zeros(num_ports)
    vol_arr = np.zeros(num_ports)
    sharpe_arr = np.zeros(num_ports)

    for x in range(num_ports):
        # Weights
        weights = np.array(np.random.random(count))
        weights = weights/np.sum(weights)
        
        # Save weights
        all_weights[x,:] = weights
        
        # Expected return
        ret_arr[x] = np.sum(mean_returns * weights)
        
        # Expected volatility
        vol_arr[x] = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        
        # Sharpe Ratio
        sharpe_arr[x] = ret_arr[x]/vol_arr[x]


    max_sharp_location = sharpe_arr.argmax()

    #all_weights = (all_weights[sharpe_arr.argmax(),:])
    max_sr_ret = ret_arr[sharpe_arr.argmax()]
    max_sr_vol = vol_arr[sharpe_arr.argmax()]

    # plt.figure(figsize=(12,8))
    # plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='viridis')
    # plt.colorbar(label='Sharpe Ratio')
    # plt.xlabel('Volatility')
    # plt.ylabel('Return')
    # plt.scatter(max_sr_vol, max_sr_ret,c='red', s=50) # red dot
    return {'returns': ret_arr, 'volatility': vol_arr, 'sharp': sharpe_arr, 'max_sharp_ret': max_sr_ret, 'max_sharp_vol': max_sr_vol}
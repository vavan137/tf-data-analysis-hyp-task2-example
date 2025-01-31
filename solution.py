import pandas as pd
import numpy as np
from scipy.stats import ks_2samp
#from hyppo.ksample import MMD
#from scipy.stats import anderson_ksamp

chat_id = 5463739632 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.03
    statistic, pvalue = ks_2samp(x, y) #3/4
    #pvalue = MMD(compute_kernel="poly").test(x, y)[1] #1/4
    #pvalue = anderson_ksamp([x, y]).pvalue #2/4
    return pvalue < alpha

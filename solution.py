import pandas as pd
import numpy as np

from scipy.stats import uniform


chat_id = 263819966 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = 0.065
    scale = 2 * x.mean() - 0.065
    return 2*x.mean() - 2*0.065 + 2 * np.sqrt(np.var(x)) * uniform.ppf(1 - alpha/2) / np.sqrt(len(x)), \
           2*x.mean() - 2*0.065 + 2 * np.sqrt(np.var(x)) * uniform.ppf(alpha/2) / np.sqrt(len(x))

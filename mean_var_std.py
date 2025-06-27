import numpy as np

def mean(list):
  return (list.mean(axis=0).tolist(), list.mean(axis=1).tolist(), list.mean().tolist())

def variance(list):
  return (list.var(axis=0).tolist(), list.var(axis=1).tolist(), list.var().tolist())

def standard_deviation(list):
  return (list.std(axis=0).tolist(), list.std(axis=1).tolist(), list.std().tolist())

def maximo(list):
  return (list.max(axis=0).tolist(), list.max(axis=1).tolist(), list.max().tolist())

def minimo(list):
  return (list.min(axis=0).tolist(), list.min(axis=1).tolist(), list.min().tolist())

def sumatoria(list):
  return  (list.sum(axis=0).tolist(), list.sum(axis=1).tolist(), list.sum().tolist())

def calculate(list):

    np_list = np.array(list)
    reshaped_array = np_list.reshape(3, 3)

    if reshaped_array.size != 9:
      calculations = "The series is NOK, it most have 9 values"
    else:
      calculations = {
        'mean': mean(reshaped_array),
        'variance': variance(reshaped_array),
        'standard deviation': standard_deviation(reshaped_array),
        'max': maximo(reshaped_array),
        'min': minimo(reshaped_array),
        'sum': sumatoria(reshaped_array)
      }
      return calculations
        
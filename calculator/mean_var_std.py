import numpy as np

def calculate(list):
	if (len(list) != 9):
		raise ValueError("List must contain nine numbers.")
	a = np.array(list)
	b = np.reshape(a, [3,3])
	res = dict()
	f_mean = np.mean(a)
	f_max = np.max(a)
	f_var = np.var(a)
	f_std = np.std(a)
	f_min = np.min(a)
	f_sum = np.sum(a)
	b_mean1 = np.mean(b, axis=0)
	b_var1 = np.var(b,axis=0)
	b_max1 = np.max(b, axis=0)
	b_std1 = np.std(b, axis=0)
	b_min1 = np.min(b, axis=0)
	b_sum1 = np.sum(b, axis=0)
	b_mean2 = np.mean(b, axis=1)
	b_var2 = np.var(b, axis=1)
	b_max2 = np.max(b, axis=1)
	b_std2 = np.std(b, axis=1)
	b_min2 = np.min(b, axis=1)
	b_sum2 = np.sum(b, axis=1)
	mean_list = [b_mean1.tolist(), b_mean2.tolist(), f_mean.tolist()]
	sd_list = [b_std1.tolist(), b_std2.tolist(), f_std.tolist()]
	var_list = [b_var1.tolist(), b_var2.tolist(), f_var.tolist()]
	max_list = [b_max1.tolist(), b_max2.tolist(), f_max.tolist()]
	min_list = [b_min1.tolist(), b_min2.tolist(), f_min.tolist()]
	sum_list = [b_sum1.tolist(), b_sum2.tolist(), f_sum.tolist()]
	res['mean'] = mean_list
	res['variance'] = var_list
	res['standard deviation'] = sd_list
	res['max'] = max_list
	res['min'] = min_list
	res['sum'] = sum_list
	return res
print(calculate([2,6,2,8,4,0,1,5,7]))

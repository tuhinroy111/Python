import statistics

example_list= [1,2,7,4,9,8,9]

x= statistics.mean(example_list)
print('Mean',x)
x= statistics.median(example_list)
print('Median',x)
y= statistics.mode(example_list)
print('Mode',y)
x= statistics.stdev(example_list)
print('Standard Deviation',x)
x= statistics.variance(example_list)
print('Variance',x)

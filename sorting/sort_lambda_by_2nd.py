ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort=sorted(ex_lst, key=lambda x: str(x)[1])
#key will return 2nd element and accoding to 2nd letter ex_let would be sorted
print(lambda_sort)

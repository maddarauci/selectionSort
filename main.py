# author: Dom 
'''
class: Sorting algorithmn.
selection sort is an in-place comparison sorting algorithmn. it has O(n2) time complexity.

which makes it inefficient on large lists.
'''
def selection_sort(input_list):
  for idx in range(len(input_list)):
    min_idx = idx
    for j in range( idx + 1, len(input_list)):
      if input_list[min_idx]> input_list[j]:
        min_idx = j
    # swap the min value with the comare value 
    input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

sort = [12, 3, 4, 30, 55, 1, 8, 90]
selection_sort(sort)
print(f"finished selection sort is: {sort}")
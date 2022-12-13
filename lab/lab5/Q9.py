def run_length_encode(nums):
    frequency = {}
# iterating over the list
    for item in nums:
   # checking the element in dictionary
        if item in frequency:
      # incrementing the counr
            frequency[item] += 1
        else:
      # initializing the count
            frequency[item] = 1
    return list(frequency.items())
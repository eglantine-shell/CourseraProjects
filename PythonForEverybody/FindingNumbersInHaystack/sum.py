import re

handle = open('/Users/yetingzhi/Documents/GIT/PythonForEverybody/FindingNumbersInHaystack/regex_sum_1696443.txt')
sum = 0
for line in handle:
    nums = re.findall('[0-9]+', line)
    if len(nums) < 1:
        continue
    for num in nums:
        sum = sum + int(num)
print(sum)

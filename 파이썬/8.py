num = int(input())
result = str(num)
    
if num >= 1000000:
    result = str(num // 1000000) + 'G'
elif num >= 0:
    pass
    
print(result)
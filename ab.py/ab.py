# ab = [0]*127
# abc = input()
# for i in range(len(abc)):
#     ab[ord(abc[i])]+=1
# # a = ab.index(max(ab))
# max_number = ab[0]
# index_number_max = 0
# for i in range(len(ab)):
#     if ab[i] > max_number:
#         max_number = ab[i]
#         index_number_max = i


# print(chr(index_number_max))
# count=1
# result=""
# abc = input()
# for i in range (1,len(abc)):
#     if abc[i] == abc[i-1]:
#         count+=1
#     else:
#         result += abc[i-1] + str(count)
#         count = 1
# result += abc[i-1] + str(count)
# print(result)
a,b = map(int,input().split())
yr = 0
while not a>b:
    yr+=1
    a*=3
    b*=2
print(yr)
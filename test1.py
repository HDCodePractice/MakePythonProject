users = "abc"       # users "abc" string
users = ""          # ""  空的 string
users = 12          # int 的 12
users = "12"        # string 内容是  "12"
users = str(12)     # string 内容是  "12"   str()  把 int 12 变为了 string的  "12"
users = int("12")   # int 的 12 ，把 "12" 用int()变为了 int
users = []          # 一个空的 []  List/Array/数组
users = [1]         # 一个List，包含有一个元素，是 int 1

users = ["1","a"]   # 一个List，包含有两个元素， 位置0-> "1"   位置 1-> "a"

print( users[1] )   # "a"
print( users[1] + users[0] ) # a1

print("==========================")
for user in users:
    print( f"user:{user}" )
# user:1
# user:a


print("==========================")
for i in range(2):
    print( f"user{i}:{users[i]}" )
# user0:1
# user1:a

print("==========================")
for i in range( len(users) ):
    print( f"user{i}:{users[i]}" )
# user0:1
# user1:a

print("==========================")
for u in ['parker','noah','sicheng']:
    users.append(u)
print(users)
#  ['1', 'a', 'parker', 'noah', 'sicheng']

print("==========================")
for u in [1,3]:
    users.remove( users[u] )
print(users)
#  ['1', 'a', 'parker', 'noah', 'sicheng']
# remove 1 -> ['1', 'parker', 'noah', 'sicheng']
# remove 3 -> ['1', 'parker', 'noah']

print("==========================")
#  split list的练习
users = "parker:noah:sicheng:cola:claire"
# 得到 ["cola","sicheng","noah","parker"]
#  u = users.split(":")
#  n = len(u)   :4
#  for i in range(n)    : 0/1/2/3
#     n - i - 1   : 3/2/1/0
u = users.split(":")
s = len(u)
r = []
for i in range(s):
    e = (s - i - 1)
    r.append(u[e])
print(r)
# m = [u[4],u[3],u[2],u[1],u[0]]
# print(m)

print("==========================")
users = ['claire', 'cola', 'sicheng', 'noah', 'parker']
# "1:claire,2:cola,3:sicheng,4:noah,5:parker"
a = len(users)
c = ""
for i in range(a):
    c += f"{i+1}:{users[i]}"
print(c)
# d = f"1:{users[0]},2:{users[1]},3:{users[2]},4:{users[3]},5:{users[4]}"
# print(d)

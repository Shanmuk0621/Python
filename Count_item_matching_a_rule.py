# 1773. Count Items Matching a Rule

# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

 

# Example 1:

# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
# Example 2:

# Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
# Output: 2
# Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.


n=int(input("enter a no of elements"))
lis=[]

for i in range(n):
    a=[]
    for j in range(3):
        ele=(input("enter a element"))
        a+=[ele,]
    lis+=[a,]

rulekey=int(input("enter a key"))
rulevalue=input("enter a value")

print(lis)

count=0
for i in range(n):
    for j in range(3):
        if (j==rulekey and lis[i][j]==rulevalue):
            count+=1

print(count)



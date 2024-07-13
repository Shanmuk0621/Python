#  Minimum Number of Moves to Seat Everyone

# There are n availabe seats and n students standing in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.

# You may perform the following move any number of times:

# Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
# Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

# Note that there may be multiple seats or students in the same position at the beginning.

 

# Example 1:

# Input: seats = [3,1,5], students = [2,7,4]
# Output: 4
# Explanation: The students are moved as follows:
# - The first student is moved from from position 2 to position 1 using 1 move.
# - The second student is moved from from position 7 to position 5 using 2 moves.
# - The third student is moved from from position 4 to position 3 using 1 move.
# In total, 1 + 2 + 1 = 4 moves were used.
# Example 2:

# Input: seats = [4,1,5,9], students = [1,3,2,6]
# Output: 7
# Explanation: The students are moved as follows:
# - The first student is not moved.
# - The second student is moved from from position 3 to position 4 using 1 move.
# - The third student is moved from from position 2 to position 5 using 3 moves.
# - The fourth student is moved from from position 6 to position 9 using 3 moves.
# In total, 0 + 1 + 3 + 3 = 7 moves were used.
# Example 3:

# Input: seats = [2,2,6,6], students = [1,3,2,6]
# Output: 4
# Explanation: Note that there are two seats at position 2 and two seats at position 6.
# The students are moved as follows:
# - The first student is moved from from position 1 to position 2 using 1 move.
# - The second student is moved from from position 3 to position 6 using 3 moves.
# - The third student is not moved.
# - The fourth student is not moved.
# In total, 1 + 3 + 0 + 0 = 4 moves were used. 



def mysort(lis):
    for i in range(n):
        temp=lis[i]
        j = i-1
        while (j>=0 and lis[j] > temp):
            lis[j+1]=lis[j]
            j-=1
        lis[j+1]=temp


n=m=int(input("enter no of elements in an array"))

seats=[]
students=[]

for i in range(n):
    ele=int(input("enter a seat vacany position"))
    seats+=[ele]
mysort(seats)
print(seats)

for j in range(m):
    ele=int(input("enter a student position"))
    students+=[ele]
mysort(students)
print(students)

moves=0

for i in range(n):
    diff = students[i]-seats[i]

    if (diff < 0):
        diff=diff*-1
        moves+=diff
    else:
        moves+=diff

print("the minimum no of moves is",moves)
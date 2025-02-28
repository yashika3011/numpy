'''1.Find Common Elements:
     Given two lists:
     list1 = [1, 2, 3, 4]
     list2 = [3, 4, 5, 6]
     Find the common elements using a set.'''

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = list(set(list1) & set(list2))
print(common_elements)

''' 2. Unique Characters in a String:
       Write a program to find all unique characters in the string "programming" using a set.'''

string = "programming"
unique_chars = set(string)
print(unique_chars) 

'''   3. Union of Sets:
        Find the union of the sets:
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)


'''4. Intersection of Sets:
      Find the intersection of the sets:
      A = {'a', 'b', 'c'}
      B = {'b', 'c', 'd'}'''

A = {'a', 'b', 'c'}
B = {'b', 'c', 'd'}
intersection_set = A & B
print(intersection_set) 

''' 5. Difference of Sets:
       Find the difference of the sets:
       X = {1, 2, 3, 4}
       Y = {3, 4, 5, 6}'''


X = {1, 2, 3, 4}
Y = {3, 4, 5, 6}
difference_set = X - Y
print(difference_set)
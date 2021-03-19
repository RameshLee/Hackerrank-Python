#!/usr/bin/python
import sys
import time
import math
import abc
#import numpy
#import pandas

def helloworld():
    print("Hello World")

    a, b, c = 1, 1, 1

    total = a + \
            b + \
            c
    print("Total=%0.02f" % total)  # This is a comment

    if (type(total) is not int): print("True\n");
    A = 2.333;
    print("%0.02f\n" % A) # print with format specifier
    '''
    Multi-line comment
    '''

def set_function():
    #unordered collection of items without duplicates
    #when printed or iterated, the items may appear in a random order.
    str = "Hackerrank"
    print(set(str))
    list = [1, 2, 2, 3, 4]
    print(set(list))
    #print(set(enumerate(['H','a','c','k','e','r','r','a','n','k'])))

    ## add element
    setarr = set("Hackerrank")
    setarr.add('Q')
    print(setarr)

    ## delete element
    # way-1: raises keyError if element doesn't exist
    try:
        setarr.remove('z')
    except:
        print("raises KerError if element doesn't exist!")
    # way-2: does not raise keyError if element doesn't exist
    setarr.discard('z')

    # way-3: pop up a random element (bullshit!)
    setarr.pop()

    ## finding union and intersections
    print("Finding union and intersections:")
    a = set("12345")
    b = set("1234567")
    print(a.union(b)) # print(a | b)
    print(a.intersection(b))  # print(a & b)
    print(a.difference(b)) # print(a - b)
    print(a.symmetric_difference(b)) # print(a ^ b)
    print(a.update(b)) # print(a |= b)
    print(a.intersection_update(b))  # print(a &= b)
    print(a.difference_update(b)) # print(a -= b)
    print(a.symmetric_difference_update(b)) # print(a ^= b)

def string():
    # A = input("Enter here: " + "\n")
    # print("Printing= \n", A)

    # A = int(input());
    str = 'rameshtaker@gmail.com'
    print(str + " is my email-ID")  # Prints concatenated string

    #### find elements in string
    if ('@gmail.com' not in str): print("True\n");
    index = str.find('k', 0, 7)
    print("Index of element in str: %d" % index) # if not found, it returns -1

    #### String split() and join()
    str = "This is an ecstacy!";  print(str)
    str = str.split(' ');  print(str)
    str = '-'.join(str);   print(str)

    ### inserting a letter in the string
    str = "rameshcuriosity@gmail.com"
    position, character = 6, '.'
    print(str[0:position] + character + str[position:len(str)])

    ### find occurences of substring in a string
    str = "ABCDCDC"
    substr = "CDC"
    count = 0
    i = str.find(substr)
    while i != -1:
        count += 1
        i = str.find(substr, i+1) ## starts search from position i+1
    print("Occurences: ", count)

    ### any() returns true if any of the condition is true
    str = "aQ4"
    print(any(c.isalnum() for c in str))
    print(any(c.isalpha() for c in str))
    print(any(c.isdigit() for c in str))
    print(any(c.islower() for c in str))
    print(any(c.isupper() for c in str))


    ### alignments
    str = "Hackerrank"
    width = 20
    print(str.ljust(width,"-"))
    print(str.rjust(width, "-"))
    print(str.center(width, "-"))

    ### capitalize
    s = "ramesh ramasamy pandi"
    str = s.split(" ")
    #print(str)
    newstr = []
    for i in range(len(str)):
        str[i] = str[i].capitalize()
    #print(str)
    str = " ".join(str)
    print(str)

def ExtractNumbers_from_String():
    S = input().strip()
    S = S.replace(' ','') # replace white spaces
    print(S)
    try:
        S = int(S)
        print(S)
    except:
        print("Bad String")

def listandtuples():
    list = [1, 2.0, 'RoboCop']  # Can be updated on-the-fly
    tuple = (1, 2.0, 'RoboCop')  # READ-only: cannot be updated
    list.append(5);
    tuple = tuple * 2;
    print("MyTuple: " , tuple)

    MulList = list + list

    if (type(MulList[0]) is int): print("True\n")
    else: print("Something else\n")

    if (1 in list): print("True\n")

    del MulList[6:7]
    MulList.insert(0, 'GVP') # insert(index, element)
    MulList.remove(2.0)
    print(MulList)

    list2 = [ 4, 2, 3, 3]
    list2.count(3) # returns number of times an element occurs in the list
    list2.sort()
    list2.reverse()
    print(list2)

    ##### list comprehension: one-line-for-loop
    list = [input() for i in range(5)]
    #above is equal to
    list = []
    for i in range(5):
        list.append(input())

    #### find index of an element in python
    element = 5
    start = 0
    end = 8
    list.index(element, start, end)

def MathFunctions():
    divmod(177, 10) # finds tuple of quotient and remainder
    pow(2,3) # find a ^ b
    pow(2,3,4) # finds a^b mod m

from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import product
def IterationTools():
    #a = [i+1 for i in range(3)]
    a = list("1233")
    comboLength = int(2)

    b = list(permutations(sorted(a), comboLength)) # permutations
    print(a, "Permutations =>", b)

    b = list(combinations(sorted(a), comboLength)) # combinations
    print(a, "Combinations =>", b)

    b = list(combinations_with_replacement(sorted(a), comboLength))  # combinations with permission to repeat the individual elements
    print(a, "Combinations_with_replacement =>", b)

    #b = list(product(a), repeat=2))  # cartesian products (Matrix multiplication)
    b = list(product([1, 2, 3], [4, 5, 6]))
    print(a, "Cartesian products =>", b)


def dictionary():
    dict = {}
    dict[1] = 'John'
    dict['two'] = 'Wick'
    print("Dict keys: ", dict.keys())
    print("Dict values", dict.values())

    dict2 = {1:'Rossi', 2:'Bautista'}
    print(dict2)
    del dict2[1]
    print("Dict2: After deleting one element: ", dict2)
    dict2.clear()
    print("Dict2: After clearing: ", dict2)
    dict2.update(dict);
    print("Updated Dict2: ", dict2)


def operators(a, b):
    print(a // b)  # Floor division
    c = 60 #00111100
    d = 13 #00001101
    print(c&d) #Bitwise operation

    #variety-1
    list = [ 1, 2, 3 ]
    item = 1;
    if (item in list): print("true \n")
    else: print("false \n")

    # variety-2
    if (type(item) is int): print("true that\n")
    else: print("false ofcourse\n")


def CheckNumberinRange(N):
    if N % 2 != 0:
        print("Weird")
    else:
        if N in range(2,6): # this checks 2 <= N < 6 -> similar to for (int N=2; N<6; N++).
            print("Not Weird")
        elif N in range(6,21): # this checks 6 <= N < 21 -> similar to for (int N=6; N<21; N++)
            print("Weird")
        else:
            print("Not Weird")

def TimeGlock(ElapsedTime):
    now = time.time_ns()
    n = 99999
    for i in range(n):
        A = n * n
    ElapsedTime = (time.time_ns() - now)
    print("ElapsedTime: %0.02f ns" % ElapsedTime)
    return


class Person:
    age = 0

    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        self.age = initialAge
        if (self.age < 0):
            self.age = 0
            print("Age is not valid, setting age to 0.")

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if (self.age < 13):
            print("You are young.")
        elif self.age in range(13, 18):
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
### end of class ###

def PassbyValueVsReferenceInnerFunc(A):
    A = A + [3, 4]   # Special case: Assignment operator always creates a new variable.
   # A += [3, 4]  # Special case: Assignment operator makes this 'A' as a new variable.
    print("From inside the func: ", A)
    b = 2
    c = 3
    return b, c # return multiple values

def PassbyValueVsReferenceOuterFunc(A):
    print("From outside the func: ", A)
    [b, c] = PassbyValueVsReferenceInnerFunc(A)  # Primitive (int, float, bool, etc) are always PassbyValue, others are always Passbyref.
    print("After: from outside the func: ", A)
    print(b, c)


def stringSeparation():
    n = int(input()) # Sample I/P: 2 Hacker Rank, O/P: Hce akr Rn ak
    list = []
    for i in range(n):
        list.append(input())

    NewList = []
    for i in range(n):
        str1 = ''
        str2 = ''
        for j in range(len(list[i])):
            if (j % 2 == 0):
                str1 = str1 + list[i][j]
            else:
                str2 = str2 + list[i][j]
        NewList.append(str1)
        NewList.append(str2)

    for i in range(0, 2 * n - 1, 2):
        print(NewList[i], NewList[i + 1])


def DictnMaps_Hackerrank():
    n = int(input())
    map = {}
    for i in range(n):
        A = input().split()
        map[A[0]] = A[1]

    # print(map)

    while True:
        try:
            queryKey = input()
            if (queryKey == ''):
                break
            else:
                if queryKey in map.keys():
                    print(queryKey + "=" + map[queryKey])
                else:
                    print("Not found")
        except EOFError:
            break;


def convertDecimalToBinary(n):
    ### 1) Convert Decimal to Binary

    remainder = []
    while (n > 1):
        remainder.insert(0, (n % 2))
        n = math.floor(n / 2)
    # print(remainder, "quotient", n, "remainder", remainder[0])
    remainder.insert(0, n)

    ### 2) Count the Number of Consecutive 1's

    index = 0
    count = []
    count.append(0)
    if (remainder[0] == 1):
        count[0] = 1
    for i in range(len(remainder) - 1):
        if (remainder[i] == 1 and remainder[i + 1] == 1):
            count[index] += 1
        else:
            index += 1
            count.append(0)
            if (remainder[i + 1] == 1):
                count[index] = 1

    ### 3) Find and Print the MaxCount of consecutive 1's

    MaxCount = 0
    for i in range(len(count)):
        if (count[i] > MaxCount):
            MaxCount = count[i]

    if (MaxCount == 0):
        count = 1
    else:
        count = MaxCount

    print(count)


def my_gcd_computation(a, b):
    real_a = a
    real_b = b

    if a < b:
        Temp = a
        a = b
        b = Temp

    #print(a,b)
    while b > 0:
        Temp = a%b
        a = b
        b = Temp
        #print(a,b)

    gcd = a
    lcm = (int(real_a/ gcd * real_b))
    print(gcd, lcm)


def sumExceptTwo(list):
    sum = 0
    for i in range(len(list)):
        if (i == 3 or i == 5):
            sum += 0  # print("Illegal entry i vaule: ", i)
        else:
            sum += list[i]

    return sum


def maxHourGlass_Hackerrank(arr):
    # print(len(arr))

    hourGlassValues = []
    for x in range(0, len(arr) - 2):
        for y in range(0, len(arr) - 2):
            # print("Value of x and y is: ", x,y)
            list = []
            for i in range(x + 0, x + 3):
                for j in range(y + 0, y + 3):
                    list.append(arr[i][j])
            #      print(arr[i][j], " ", end='')
            #   print("\n")
            # print("---\n")
            hourGlassValues.append(list)

    summation = []
    for i in range(len(hourGlassValues)):
        summation.append(sumExceptTwo(hourGlassValues[i]))
    # print("here", sumExceptTwo(hourGlassValues[i]))
    # print(summation)
    print(max(summation))

def my_fibonacci_number_Rule(n, m):

    previous = 0
    current = 1
    Fibonacci = [0, 1]
    Fibonacci_Modulo = [0, 1]
    for i in range(2, 1000000):
        temp = current
        current = current + previous
        previous = temp
        Fibonacci.append(current)
        Fibonacci_Modulo.append(current % m)
        if Fibonacci_Modulo[i-1] == 0 and Fibonacci_Modulo[i] == 1:
            break

    Period = len(Fibonacci_Modulo) - 2
    TargetNumber = Fibonacci[n % Period]
    Ans = TargetNumber % m
    print(Ans)
    return Ans
    #print(Ans)
    #print(Fibonacci)
    #print(Fibonacci_Modulo)
    #print(Period)

def myFibonacci_lastNumber(n):
    previous = 0
    current = 1
    #Fibonacci = [0, 1]
    for i in range(n-1):
        temp = current
        current = current + previous
        previous = temp
        #Fibonacci.append(current)
        current = current % 10
        previous = previous % 10

    #print(Fibonacci)
    #print(current)
    return current

def myFibonacci_lastdigitOfPartialSum(first, second):
    # To find last digit, just get modulo 10. All modulo of fibonacci starts with '0 1' piasono period.
    # 1) find the period for mod 10
    '''
    previous = 0
    current = 1
    Fibonacci = [0, 1]
    Fibonacci_Modulo = [0, 1]
    for i in range(2, 1000000):
        temp = current
        current = current + previous
        previous = temp
        Fibonacci.append(current)
        Fibonacci_Modulo.append(current % 10)
        if Fibonacci_Modulo[i-1] == 0 and Fibonacci_Modulo[i] == 1:
            break
    Period = len(Fibonacci_Modulo) - 2
    '''
    previous = 0
    current = 1
    Period = 60
    Fibonacci = [0, 1]
    for i in range(Period-2):
        temp = current
        current = current + previous
        previous = temp
        current = current % 10
        previous = previous % 10
        Fibonacci.append(current)
    print(len(Fibonacci))
    SummationUnderOnePeriod = sum(Fibonacci)

    # 2) find the lastDigit between numbers first and second
    PeriodNumberOfTheFirst = floor(first/Period)
    PeriodNumberOfTheSecond = floor(second/Period)
    NumberOfInBetweenPeriods = 2
    LengthOne = first % Period
    LengthTwo = second % Period
    ElementsFromSecondToStartOfNewPeriod = 2

    LastDigits = []
    for i in range(first, second+1):
        LastDigits.append(Fibonacci[i % Period])

    TheLastDigit = sum(LastDigits)%10
    print(TheLastDigit)
    return TheLastDigit


from abc import ABCMeta, abstractmethod
class BaseClass_Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self): pass

class DerivedClass_MyBook(BaseClass_Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = int(price)

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data):
    #Complete this method
        NewNode = Node(data)
        if head is None:
            head = NewNode
        else:
            currNode = head
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = NewNode
        return head

    def removeDuplicates_on_SortedLinkedList(self, head):
        currNode = head
        while currNode is not None:
            nextNode = currNode.next
            if nextNode is not None:
                if currNode.data == nextNode.data:
                    #delete next node
                    currNode.next = nextNode.next
                else:
                    currNode = currNode.next
            else:
                break
        return head

def get_Coins_change(m):
    # write your code here #for example, 28 as input gives 6 coins (two 10 rs, one 5 rs, and three 1 rs).
    Tens = math.floor(m/10)
    NewNum1 = m % 10

    Fives = math.floor(NewNum1/5)
    NewNum2 = m % 5
    Ones = NewNum2
    Coins = Tens+Fives+Ones
    #print(Tens, Fives, Ones, NewNum1, NewNum2)
    return Coins

class Calculator:
    def power(self, n,p):
        if n < 0 or p < 0:
            raise ValueError('n and p should be non-negative')
        else:
            return n**p

class StackAndQueue:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, dataVal):
        self.stack.append(dataVal)  # insert at the top
        print("Stack: ", self.stack)

    def enqueueCharacter(self, dataVal):
        self.queue.insert(0, dataVal)  # insert at the front
        print("Queue: ", self.queue)

    def popCharacter(self):
        print("Stack: ", self.stack)
        return self.stack.pop()  # delete last element

    def dequeueCharacter(self):
        print("Queue: ", self.queue)
        return self.queue.pop()  # delete last element


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class BinarySearchTree:
    def insert(self, root, node):
        if root is None:
            root = node
        else:
            if node.data < root.data:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)


    def getHeight(self, root):
        # Base case:
        if root is None:
            return -1
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


    def levelOrderTraversal(self,root):
        #Write your code here
        queue = []
        if root is not None:
            queue.insert(0, root)
        while queue:
            node = queue.pop()
            print(node.data, end=" ")
            if node.left:
                queue.insert(0,node.left)
            if node.right:
                queue.insert(0,node.right)


def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def printNamesinAscending_for_GmailIDs():
    N = int(input())
    list = []
    for N_itr in range(N):
        firstName, emailID = input().split()
        if ("@gmail.com" in emailID):
            list.append(firstName)

    list.sort()
    for i in range(len(list)):
        print(list[i])

if __name__ == '__main__':
    # helloworld()
    #print(math.floor((50) % 60))
    #printNamesinAscending_for_GmailIDs()

# BST
    #myTree = BinarySearchTree()
    #Arr = [3, 5, 4, 7, 2, 1]
    #root = Node(Arr[0])
    #for i in range(1, len(Arr)):
    #    myTree.insert(root, Node(Arr[i]))
    #myTree.levelOrderTraversal(root)

# Other functions
    # get_Coins_change(28)
    # mylist = LinkedList(); head=None; head=mylist.insert(head,2); head=mylist.insert(head,2); head=mylist.insert(head,4); mylist.display(head)
    # A = DerivedClass_MyBook('Alchemist', 'Coelho', 70); A.display()
    # myFibonacci_lastdigitOfPartialSum(1, 100000000)
    # myFibonacci_lastNumber(327305)
    # my_fibonacci_number_Rule(2816213588, 239)
    # maxHourGlass_Hackerrank(give a 3D square array here...)
    # my_gcd_computation(int(761457), int(614573))
    # convertDecimalToBinary
    # DictnMaps_Hackerrank()
    # stringSeparation()
    # PassbyValueVsReferenceOuterFunc([1, 2])
    # Obj = Person(15); Obj.amIOld()
    # TimeGlock(ElapsedTime)
    # CheckNumberinRange(20)
    # operators(5.9, 2)
    # dictionary();
    # listandtuples()
    # ExtractNumbers_from_String()
    # string()
    # set_function()
    IterationTools()



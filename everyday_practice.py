## 2.to convert to farenheit and celcius
#
# def convertToCelsius(Fahrenheit):
#     Celsius = (Fahrenheit - 32) * (5 / 9)
#     return Celsius
#
# def convertToFahrenheit(Celsius):
#     Fahrenheit = Celsius * (9 / 5) + 32
#     return Fahrenheit
#
#
# print(convertToCelsius(0))
# print(convertToCelsius(180))
#
# print(convertToFahrenheit(0))
# print(convertToFahrenheit(100))
#
# print(convertToCelsius(convertToFahrenheit(15)))

## 3.odd or even
#
# def isOdd(odd):
#     if odd%2 == 1:
#         return True
#     else:
#         return False

# def isEven(even):
#     if even%2 ==0:
#         return True
#     else:
#         return False
#
# assert isOdd(42) == False
# assert isOdd(9999) == True
# assert isOdd(-10) == False
# assert isOdd(-11) == True
# assert isOdd(3.1415) == False
#
# assert isEven(42) == True
# assert isEven(9999) == False
# assert isEven(-10) == True
# assert isEven(-11) == False
# assert isEven(3.1415) == False


# 4. Area and volume

# def box(l,w,h):
# #     area = l*h
# #     perimeter = l+l+h+h
# #     volume = l*w*h
# #     surfarea = (l*w*2)+(l*h*2)+(w*h*2)
# #     print("Area:",area, "\nPerimeter:",perimeter, "\nVolume:",volume, "\nSurface area:",surfarea)
# #
# # box(10,10,10)
#
# def area(l,h):
#     return l*h
#
# def perimeter(l,h):
#     return l+l+h+h
#
# def volume(l,w,h):
#     return l*w*h
#
# def surfaceArea(l, w, h):
#     return (l*w*2)+(l*h*2)+(w*h*2)
#
#
# # print(area(10, 10))
# # print(area(0, 9999))
# # print(area(5, 8))
#
# # print(perimeter(10, 10))
# # print(perimeter(0, 9999))
# # print(perimeter(5, 8))
#
# # print(volume(10, 10, 10))
# # print(volume(9999, 0, 9999))
# # print(volume(5, 8, 10))
#
# print(surfaceArea(10, 10, 10))
# print(surfaceArea(9999, 0, 9999))
# print(surfaceArea(5, 8, 10))

# # 5.fizzbuzz
#
# # def fizzBuzz(num):
# #     if num%3==0 and num%5==0:
# #         print('FizzBuzz')
# #     elif num%3==0:
# #         print('Fizz')
# #     elif num%5==0:
# #         print('Buzz')
# #     else:
# #         print(num)
# #
# #
# # fizzBuzz(17)
#
# def fizzBuzz(upTo):
#     for number in range(1, upTo+1):
#
#         if number % 3 == 0 and number % 5 == 0:
#             print('FizzBuzz', end= '\n')
#
#         elif number % 3 == 0:
#             print('Fizz', end= '\n')
#
#         elif number%5 == 0:
#             print('Buzz', end= '\n')
#
#         else:
#             print(number, end= '\n')
#
# ##fizzBuzz(20)
# fizzBuzz(35)

#6.Ordinal Suffix, 17feb2023 Fri

# # def ordinalSuffix(number):
# #     numstr = str(number)
# #
# #     if numstr[-2:] in ('11', '12', '13'):
# #         return numstr+'th'
# #
# #     elif numstr[-1:] == ('1'):
# #         return numstr + 'st'
# #
# #     elif numstr[-1:] == ('2'):
# #         return numstr + 'nd'
# #
# #     elif numstr[-1:] == ('3'):
# #         return numstr + 'rd'
# #
# #     else:
# #         return numstr + 'th'
#
#
# def ordinalSuffix(number):
#     numstr = str(number)
#
#     if numstr[-2:] == '11' or numstr[-2:] == '12' or numstr[-2:] == '13':
#         return numstr+'th'
#
#     elif numstr[-1:] == '1':
#         return numstr + 'st'
#
#     elif numstr[-1:] == '2':
#         return numstr + 'nd'
#
#     elif numstr[-1:] == '3':
#         return numstr + 'rd'
#
#     else:
#         return numstr + 'th'
#
#
#
# print(ordinalSuffix(0))
#
# print(ordinalSuffix(11))
#
# print(ordinalSuffix(12))
#
# print(ordinalSuffix(3))
#
# print(ordinalSuffix(44))
#
# print(ordinalSuffix(105))
#
# print(ordinalSuffix(116))

# #7.ASCII
# orc() , chr()

# def printASCIITable(a,b):
#     for i in range(a,b+1):
#         print(i, 'is equal to', chr(i))
#
# printASCIITable(32,126)

# #8.read write file
# #with open(filename, mode)
#
# def writeToFile():
#     # with open('greet.txt', 'w') as fileObj:
#     #     fileObj.write('hello \n')
#     f= open('greet.txt', 'a')
#     print(f.write('saranghae'))
#
# def appendToFile():
#     # with open('greet.txt','a') as fileObj:
#     #     fileObj.write('Goodbye \n')
#     f = open('greet.txt', 'w')
#     print(f.write('Hello! Welcome to demofile.txt.This file is for testing purposes. Good Luck!'))
#
# def readFromFile():
#     # with open('greet.txt', 'r') as fileObj:
#     #     return fileObj.read()
#     f = open('greet.txt', 'r')
#     print(f.read())
#
#
# # readFromFile()
# # appendToFile()
# # print(readFromFile())
# # print(appendToFile())
# # print(readFromFile())
# writeToFile()
# readFromFile()

# #9.chess square color
#
# def getChessSquareColor(column, row):
#     # If the column and row is out of bounds, return a blank string:
#     if column < 0 or column > 8 or row < 0 or row > 8:
#         return ''
#
#     # If the even/oddness of the column and row match, return 'white':
#     if (column % 2 == 0 and row % 2 == 0) or (column %2 != 0 and row % 2 != 0):
#         return 'white'
#     # If they don't match, then return 'black':
#     else:
#         return 'black'
#
# print(getChessSquareColor(1, 1))
# print(getChessSquareColor(2, 2))
# print(getChessSquareColor(1, 2))
# print(getChessSquareColor(2, 1))
# print(getChessSquareColor(-1, 7))
# print(getChessSquareColor(1, 8))
# print(getChessSquareColor(0, 7))

#10. Find and replace

# 1. def findAndReplace(text, oldtext, newtext):
#     splittext = text.split(' ')
#     result= ''
#     for splits in splittext:
#         if splits == oldtext:
#             splits = newtext
#             result = result + ' ' + splits
#         else:
#             result = result + ' ' + splits
#     print(result)
#
#
# findAndReplace('the owner of the ring', 'owner', 'lord')

# 2. def findAndReplace(text, oldtext, newtext):
#     result= text.replace(oldtext, newtext)
#     print(result)
#
# findAndReplace('the owner of the ring', 'ow', 'lord')

# 3. def findAndReplace(text, oldText, newText):
#
#     replacedText = ''
#     i = 0
#     while i < len(text):
#         # If index i in text is the start of the oldText pattern, add
#         # the replacement text:
#         if text[i:i + len(oldText)] == oldText:
#             # Add the replacement text:
#             replacedText += newText
#             # Increment i by the length of oldText:
#             i += len(oldText)
#         # Otherwise, add the characters at text[i] and increment i by 1:
#
#         else:
#             replacedText += text[i]
#             i += 1
#
#     return replacedText
#
# print(findAndReplace('the owner of the ring', 'owner', 'lord'))

#11. hours, minutes and seconds

# 1. def getHoursMinutesSecond(totalSec):
#     m = 0
#     hour = 0
#
#     if totalSec< 60:
#         return str(totalSec) + 'sec'
#
#     elif totalSec >= 60:
#         sec = totalSec % 60
#         m += totalSec//60
#
#         if m >= 60:
#             minute = m % 60
#             hour += m//60
#             return str(hour) + 'h' + ' ' + str(minute) + 'min' + ' ' + str(sec) + 'sec'
#
#         return str(m) + 'min' + ' ' + str(sec) + 'sec'
#
#     else:
#        None
#
# # print(getHoursMinutesSecond(500))
# assert getHoursMinutesSecond(30) == '30sec'
# assert getHoursMinutesSecond(60) == '1min 0sec'
# assert getHoursMinutesSecond(90) == '1min 30sec'
# assert getHoursMinutesSecond(3600) == '1h 0min 0sec'
# assert getHoursMinutesSecond(3601) == '1h 0min 1sec'
# assert getHoursMinutesSecond(3661) == '1h 1min 1sec'
# assert getHoursMinutesSecond(90042) == '25h 0min 42sec'
# assert getHoursMinutesSecond(0) == '0sec'

#2. def getHoursMinutesSeconds(totalSeconds):
#
#     #calculation
#
#     if totalSeconds == 0:
#         return totalSeconds+'s'
#
#     hours = 0
#     while totalSeconds > 3600:
#         hours += 1
#         totalSeconds -= 3600
#
#     minutes = 0
#     while totalSeconds >= 60:
#         minutes +=1
#         totalSeconds -= 60
#
#     seconds = totalSeconds
#
#     #string to present h,m,s
#
#     hms = []
#
#     if hours > 0:
#         hms.append(str(hours)+ 'h')
#
#     if minutes > 0:
#         hms.append(str(minutes)+ 'm')
#
#     if seconds > 0:
#         hms.append(str(seconds) + 's')
#
#     return ' '.join(hms)
#
#
# print(getHoursMinutesSeconds(3601))

# #13. Smallest and biggest
#
# # def getSmallest(*args):
# #
# #     x = min(args)
# #     return x
# #
# # print(getSmallest(1,20,9,0))
#
# def getSmallest(numbers):
#     # If the numbers list is empty, return None:
#     if len(numbers) < 1:
#         return None
#
#     # Create a variable that tracks the smallest value so far, and start
#     # it off a the first value in the list:
#     smallest = numbers[0]
#
#     # Loop over each number in the numbers list:
#     for number in numbers:
#         # If the number is smaller than the current smallest value, make
#         # it the new smallest value:
#         if number < smallest:
#             smallest = number
#     # Return the smallest value found:
#     return smallest
#
# print(getSmallest([1, 2, 3]))
# print(getSmallest([3, 2, 1]))
# print(getSmallest([28, 25, 42, 2, 28]))
# print(getSmallest([1]))
# print(assert getSmallest([]))

# #13. sum and product
#
# def calculateSum(numbers):
#     sum = 0
#     for num in numbers:
#         sum +=num
#     return sum
#
#
# def calculateProduct(numbers):
#     product = 1
#     for num in numbers:
#         product *= num
#     return product
#
# print(calculateSum([2, 4, 6, 8, 10]))
# print(calculateProduct([2, 4, 6, 8, 10]))

#14.average

#def average(numbers):
#     result = sum(numbers)/len(numbers)
#     return result
#
# print(average([1, 2, 3]))
# print(average(([1, 2, 3, 1, 2, 3, 1, 2, 3])))
# print(average([12, 20, 37]))

# def average(number):
#     if len(number) == 0:
#         return None
#
#     total = 0
#     for num in number:
#         total+=num
#
#     result = total/len(number)
#     return result
#
# print(average([1, 2, 3]))
# print(average(([1, 2, 3, 1, 2, 3, 1, 2, 3])))
# print(average([12, 20, 37]))

# 15. median
# cara : susun no ->ambil nilai di tengah , kalau even makan perlu amik average 2 no.

# def median(numbers):
#
#     if len(numbers) == 0:
#         return None
#
#     sortnum = sorted(numbers)
#
#     #even num
#     if len(numbers)%2 != 0:
#         x = len(numbers)//2
#         middle = sortnum[x]
#         return middle
#
#     #odd num
#     if len(numbers)%2 == 0:
#         x = len(numbers) // 2
#         y = (len(numbers) // 2) + 1
#         middle1 = sortnum[x]
#         middle2 = sortnum[y]
#         return (middle1 + middle2)/2
#
#
# print(median([]))
# print(median([1, 2, 3]))
# print(median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]))
# print(median([3, 7, 10, 4, 1, 9, 6, 2, 8]))

# def median(numbers):
#     # Special case: If the numbers list is empty, return None:
#     if len(numbers) == 0:
#         return None
#
#     # Sort the numbers list:
#     numbers.sort()
#
#     # Get the index of the middle number:
#     middleIndex = len(numbers) // 2
#
#     # If the numbers list has an even length, return the average of the
#     # middle two numbers:
#     if len(numbers) % 2 == 0:
#         return (numbers[middleIndex] + numbers[middleIndex - 1]) / 2
#
#   # If the numbers list has an odd length, return the middlemost number:
#     else:
#         return numbers[middleIndex]
#
# print(median([]))
# print(median([1, 2, 3]))
# print(median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]))
# print(median([3, 7, 10, 4, 1, 9, 6, 2, 8]))

#16.mod , most frequent number

# def mode(numbers):
#     # Special case: If the numbers list is empty, return None:
#     if len(numbers) == 0:
#         return None
#
#     # Dictionary with keys of numbers and values of how often they appear:
#     numberCount = {}
#
#     # Track the most frequent number and how often it appears:
#     mostFreqNumber = None
#     mostFreqNumberCount = 0
#
#     # Loop through all the numbers, counting how often they appear:
#     for number in numbers:
#         #must know the basic of dict
#         # If the number hasn't appeared before, set it's count to 0.
#         if number not in numberCount:
#             numberCount[number] = 0
#         # Increment the number's count:
#         numberCount[number] += 1
#         # If this is more frequent than the most frequent number, it
#         # becomes the new most frequent number:
#         if numberCount[number] > mostFreqNumberCount:
#             mostFreqNumber = number
#             mostFreqNumberCount = numberCount[number]
#     # The function returns the most frequent number:
#     return numberCount
#
# print(mode([]))
# print(mode([1, 2, 3, 4, 4]))
# print(mode([1, 1, 2, 3, 4]))

#18.dice roll

# import random
#
# def rollDice(dice):
#
#     result = 0
#     for num in range(dice):
#         rand = random.randint(1,6)
#         print('rand', num+1, ':', rand)
#         result += rand
#     return result
#
# print(rollDice(2))

#19.buy 8 get 1 free

# def getCostOfCoffee(numberofCoffee, pricePerCoffee):
#
#     #dalam satu pembelian
#     price = 0
#     for num in range(1, numberofCoffee+1):
#         if num % 9 == 0:
#             price *= 1
#         else:
#             price += pricePerCoffee
#     return price
#
# print(getCostOfCoffee(7, 2.50))
#
# print(getCostOfCoffee(8, 2.50))
#
# print(getCostOfCoffee(9, 2.50))
#
# print(getCostOfCoffee(10, 2.50))
#
# print(getCostOfCoffee(18, 2.50))

#19. password generator

# import random, string
#
# def generatorPassword(length):
#
#     #create string
#     LOWER_LETTERS = string.ascii_lowercase
#     UPPER_LETTERS = string.ascii_uppercase
#     NUMBERS = string.digits
#     SPECIAL = string.punctuation
#
#     # combine string
#     ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
#
#     # For security reasons, if length is less than 12, the function forcibly sets it to 12 characters anyway.
#     if length < 12:
#         length = 12
#
#     # create pass list
#     password = []
#
#     # Add a random character from the lowercase, uppercase, digits, and
#     # punctuation character strings:
#     password.append(LOWER_LETTERS[random.randint(0, 25)])
#     password.append(UPPER_LETTERS[random.randint(0, 25)])
#     password.append(NUMBERS[random.randint(0, 9)])
#     password.append(SPECIAL[random.randint(0, 12)])
#
#     # Keep adding random characters from the combined string until the
#     # password meets the length:
#     while len(password) < length:
#         password.append(ALL_CHARS[random.randint(0, 74)])
#
#     # Randomly shuffle the password list:
#     random.shuffle(password)
#
#     # Join all the strings in the password list into one string to return:
#     return ''.join(password)
#
# print('pass:', generatorPassword(6))
# print(len(generatorPassword(6)))

# import secrets
# from string import digits, ascii_letters
# def generate_pwd(length=8):
#     chars = digits + ascii_letters
#     return ''.join(secrets.choice(chars) for c in range(length))
#
# def generate_secure_pwd(length=16, upper=3, digits=3):
#     if length < upper + digits + 1:
#         raise ValueError('Nice try!')
#     while True:
#         pwd = generate_pwd(length)
#         if (any(c.islower() for c in pwd)
#         and sum(c.isupper() for c in pwd) >= upper
#         and sum(c.isdigit() for c in pwd) >= digits):
#             return pwd
#
# print(generate_secure_pwd())
# print(generate_secure_pwd(length=3, upper=1, digits=1))
#
# #20.leap year
# def isLeapYear(year):
#     if year%4 == 0:
#         if year%100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
#
# print(isLeapYear(1999))
#
# print(isLeapYear(2000))
#
# print(isLeapYear(2001))
#
# print(isLeapYear(2004))
#
# print(isLeapYear(2100))
#
# print(isLeapYear(2400))

# #21.validate date
#
# def isValidDate(year, month, day):
#
#     #12months in a year
#     if month > 12:
#         return False
#
#     #sept,april,jun,nov has 30days
#     thirtyday = [4,6,9,11]
#     #others has 31days
#     thirtyoneday = [1,3,5,7,8,10,12]
#     #feb has 28days
#     febday = [2]
#
#     if day <1:
#         return False
#
#     if month <1:
#         return False
#
#     if year <1:
#         return False
#
#     if month in thirtyday:
#         if day > 30:
#             return False
#
#     if month in thirtyoneday:
#         if day > 31:
#             return False
#
#     if month in febday:
#         if year%4 != 0:
#             if year%100 != 0:
#                 if year % 400 != 0:
#                     return False
#                 else:
#                     return True
#             else:
#                 return False
#         else:
#             return True
#
#     else:
#          return True
#
# print(isValidDate(2000, 2, 29))
#
# print(isValidDate(2001, 2, 29))
#
# print(isValidDate(2029, 13, 1))
#
# print(isValidDate(1000000, 1, 1))
#
# print(isValidDate(2015, 4, 31))
#
# print(isValidDate(1970, 5, 99))
#
# print(isValidDate(1981, 0, 3))
#
# print(isValidDate(1666, 4, 0))

#22.rock, paper, scissor

# def rpsWinner(move1, move2):
#     if move1 == 'rock' and move2 == 'paper':
#         return 'player two'
#     elif move1 == 'rock' and move2 == 'scissors':
#         return 'player one'
#     elif move1 == 'scissors' and move2 == 'paper':
#         return 'player one'
#     elif move1 == 'scissors' and move2 == 'rock':
#         return 'player two'
#     elif move1 == 'paper' and move2 == 'rock':
#         return 'player one'
#     elif move1 == 'paper' and move2 == 'scissors':
#         return 'player two'
#
#     else:
#         return 'tie'
# print(rpsWinner('rock', 'paper'))
# print(rpsWinner('rock', 'scissors'))
# print(rpsWinner('paper', 'scissors'))
# print(rpsWinner('paper', 'rock'))
# print(rpsWinner('scissors', 'rock'))
# print(rpsWinner('scissors', 'paper'))
# print(rpsWinner('rock', 'rock'))
# print(rpsWinner('paper', 'paper'))
# print(rpsWinner('scissors', 'scissors'))

# #try to solve to play with computer
# import random
#
# def rpsWinner(ourmove):
#
#     move = ['rock', 'scissors', 'paper']
#     compmove = random.choice(move)
#
#     if ourmove == 'rock' and compmove == 'paper':
#         return 'our move: ' + ourmove + ' || computer move: ' + compmove +' || computer win'
#
#     if ourmove == 'rock' and compmove == 'scissors':
#         return 'our move: ' + ourmove + ' || computer move:' + compmove + ' || we win'
#
#     if ourmove == 'scissors' and compmove == 'paper':
#         return 'our move: ' + ourmove + ' || computer move:' + compmove + ' || we win'
#
#     if ourmove == 'scissors' and compmove == 'rock':
#         return 'our move: ' + ourmove + ' || computer move:' + compmove + ' || computer win'
#
#     if ourmove == 'paper' and compmove == 'rock':
#         return 'our move: ' + ourmove + ' || computer move:' + compmove + ' || we win'
#
#     if ourmove == 'paper' and compmove == 'scissors':
#         return 'our move: ' + ourmove + ' || computer move:' + compmove + ' || computer win'
#
#     else:
#         return 'our move: ' + ourmove + ' || computer move: ' + compmove + ' || tie'
#
#
# print(rpsWinner('rock'))
# print(rpsWinner('rock'))
# print(rpsWinner('paper'))
# print(rpsWinner('paper'))
# print(rpsWinner('scissors'))
# print(rpsWinner('scissors'))
# print(rpsWinner('rock'))
# print(rpsWinner('paper'))
# print(rpsWinner('scissors'))

#23.bottles of beer

# def repeatSong(numofbottle):
#     for i in range(numofbottle, 0, -1):
#         if i == 1:
#             print(f"""
#    {i} bottle of beer on the wall,
#
#    {i} bottle of beer,
#
#    Take one down,
#
#    Pass it around,
#
#    No more bottles of beer on the wall!
#
#                """)
#         else:
#             print(f"""
#    {i} bottles of beer on the wall,
#
#    {i} bottles of beer,
#
#    Take one down,
#
#    Pass it around,
#
#    {i - 1} bottles of beer on the wall,
#
#                     """)
#
#
# repeatSong(99)

#24. Every 15 minutes

# for meridiem in ['am', 'pm']:
#     # Loop over every hour:
#     for hour in ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
#         # Loop over every 15 minutes:
#         for minutes in ['00', '15', '30', '45']:
#             # Print the time:
#             print(hour + ':' + minutes + ' ' + meridiem)


# #25. Multiplication table
# """ | 1  2  3  4  5  6  7  8  9 10
#
# --+------------------------------
#
#  1| 1  2  3  4  5  6  7  8  9 10
#
#  2| 2  4  6  8 10 12 14 16 18 20
#
#  3| 3  6  9 12 15 18 21 24 27 30
#
#  4| 4  8 12 16 20 24 28 32 36 40
#
#  5| 5 10 15 20 25 30 35 40 45 50
#
#  6| 6 12 18 24 30 36 42 48 54 60
#
#  7| 7 14 21 28 35 42 49 56 63 70
#
#  8| 8 16 24 32 40 48 56 64 72 80
#
#  9| 9 18 27 36 45 54 63 72 81 90
#
# 10|10 20 30 40 50 60 70 80 90 100"""
#
# # #row di atas
# # print('  |  1    2    3    4    5    6    7    8    9   10   11   12')
# # print('--+----------------------------------------------------------')
# #
# # #column di sebelah kiri
# # # Loop over all numbers from 1 to 10:
# # for column in range(1, 13):
# #     # Print the number label on the right side:
# #     print(str(column).rjust(2) + '|', end='')
# #
# #     for row in range(1, 13):
# #         print(str(row * column).rjust(3) + ' ', end=' ')
# #     print()
# #
# # # for row in range(1, 11):
# # #     for column in range(1, 11):
# # #         print(str(row * column) + ' ', end='')
# # #     print()

# #26. handshakes
# #using The pattern of i and j’s movement. Bila kita tak nak ulang loops dekat tempat yang sama.
#
# def printHandShake(people):
#     numofhandshake = 0
#
#     for i in range(0, len(people)):
#         for j in range(i+1, len(people)):
#             print(people[i], 'shakes hands with', people[j])
#             numofhandshake +=1
#
#     return numofhandshake
#
# printHandShake(['ali', 'abu', 'senah','timoh'])

# #27. rectangle drawing
#
# def drawRectangle(height,width):
#
#     if width<1 or height<1:
#         return 'cannot draw rectangle. not valid.'
#     for row in range(width):
#         for col in range(height):
#             print("#", end = '')
#         print()
#
# print(drawRectangle(5, -1))

# #28.drawing border
#
# def drawBorder(height,width):
#
#     if width<2 or height<2:
#         return 'cannot draw rectangle. not valid.'
#
#     print('+' + '-'*(int(width)-2) + '+')
#
#     for col in range(int(height)-2):
#             print('|' + ' ' * (int(width) - 2) + '|')
#
#     print('+' + '-' * (int(width) - 2) + '+')
#
# drawBorder(6,16)

# #29.pyramid drawing
#
# def drawPyramid(height):
#
#     if height<1:
#         return 'cannot draw pyramid. not valid.'
#
#     if height == 1:
#         print('#')
#
#     center = 1
#
#     for col in range(height):
#
#         right = int(height) - center/ 2
#         left = int(height) - center / 2
#
#         print(' '*int(right) + '#'*int(center) + ' '*int(left))
#
#         center+=2
#
#     print(""" See my pyramid... cool -_-""")
#
# drawPyramid(7)

# #30. 3d box drawing
#
# def drawBox(size):
#
#     # Special case: Draw nothing if size is less than 1:
#     if size < 1:
#         print('Error occur!')
#
#     else:
#
#         #at top
#         print(" "*(int(size)+1) + '+' + "-"*(int(size)*2) + '+')
#
#         right = 0
#         titik = size
#
#         for top in range(size):
#             print(' '*(int(titik)) + '/' + " "*(int(size)*2) + '/' + ' '*(int(right)) + '|')
#
#             titik -= 1
#             right += 1
#
#         print('+' + "-" * (int(size) * 2) + '+' + ' '*int(size) + '+')
#
#         #at front
#
#         titik_t = int(size)-1
#
#         for front in range(size):
#             print('|' + ' '*(int(size)*2) + '|' + ' '*(titik_t) + '/')
#
#             titik_t -=1
#
#         #at bottom
#         print('+' + "-" * (int(size) * 2) + '+')
#
#         print(f'Now you already got 3d of size {size}!')
#
#
# drawBox(0)
# drawBox(1)
# drawBox(2)
# drawBox(3)
# drawBox(4)
# drawBox(5)

# #31.convert int to str
# #menggunakan konsep pecah dan gabung
## right to left
#
# def convertIntToStr(integerNum):
#
#     if integerNum == 0:
#         return 'Erorr!!!'
#
#         # This dictionary maps single integer digits to string digits:
#
#     DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
#                         5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
#
#     # Make a note whether the number is negative or not, and make
#     # integerNum positive for the rest of the function's code:
#     if integerNum < 0:
#         isNegative = True
#         integerNum = -integerNum
#
#     else:
#         isNegative = False
#
#     # stringNum holds the converted string, and starts off blank:
#     stringNum = ''
#
#     # Keeping looping while integerNum is greater than zero:
#     while integerNum > 0:
#
#         # Mod the integerNum by 10 to get the digit in the ones place:
#         onesPlaceDigit = integerNum % 10
#
#         # Put the corresponding string digit at the front of stringNum:
#         stringNum = DIGITS_INT_TO_STR[onesPlaceDigit] + stringNum
#
#         # Divide integerNum by ten to remove one entire digit place:
#         integerNum //= 10
#
#     # If the number was originally negative, add a minus sign:
#     if isNegative:
#         return '-' + stringNum
#
#     else:
#         return stringNum
#
# #
# # for i in range(-10000, 10000):
# #     print(convertIntToStr(i) == str(i))
#
# print(convertIntToStr(100))

# #32.convert int to str
# #menggunakan konsep pecah dan gabung
# # left to right
#
# def convertStrToInt(stringNum):
#
#     # This dictionary maps string digits to single integer digits:
#     DIGITS_STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#                          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#     # Make a note whether the number is negative or not, and make
#     # integerNum positive for the rest of the function's code:
#
#     if stringNum[0] == '-':
#         isNegative = True
#         stringNum = stringNum[1:]  # Remove the negative sign.
#
#     else:
#         isNegative = False
#
#     # integerNum holds the converted integer, and starts off at 0:
#     integerNum = 0
#
#     # Loop over the digits in the string from left to right:
#     for i in range(len(stringNum)):
#
#         # Get the integer digit from the string digit:
#         digit = DIGITS_STR_TO_INT[stringNum[i]]
#
#         # Add this to the integer number:
#         integerNum = (integerNum * 10) + digit
#
#     # If the number was originally negative, make the integer
#     # negative before returning it:
#     if isNegative:
#         return -integerNum
#
#     else:
#         return integerNum
#
# print(convertStrToInt('-100'))

#33. comma format

# def commaFormat(nums):
#
#     #variable
#     nums = str(nums)
#     lst = []
#     lst.extend(nums)
#     print(lst)
#     bfinal = ''
#     lst_bfinal = []
#
#     #if error
#     if nums == '0':
#         print('Error!!!')
#
#     #if float num
#
#
#
#     #if normal int num
#     for fourth in range(len(lst), 0, -1):
#         # print(str(fourth)[-1])
#
#         bfinal = str(fourth) + bfinal
#
#         if len(bfinal)%3 == 0:
#             bfinal = ',' + bfinal
#             lst_bfinal.append(bfinal)
#             # print(lst_bfinal)
#             bfinal = ''
#
#     lst_bfinal.append(bfinal)
#     # print(lst_bfinal)
#     lst_bfinal.reverse()
#     # print(lst_bfinal)
#
#     answer = ''.join(map(str, lst_bfinal))
#     print(answer)
#
#
#
#
#
# commaFormat(123456789)
# # commaFormat(0)


# #34. uppercase letters
#
# # def getUpperCase(input):
# #
# #     x = input.upper()
# #     return x
# #
# # print(getUpperCase('selamat'))
#
# # LOWER_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
# LOWER_TO_UPPER = dict(zip(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] , ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']))
# def getUpperCase(input):
#
#     #to hold final answer
#     upperCase = ''
#
#     #loop and check character one by one
#     for character in input:
#
#         if character in LOWER_TO_UPPER:
#             upperCase += LOWER_TO_UPPER[character]
#
#         else:
#             upperCase += character
#
#     return upperCase
#
# print(getUpperCase('selamat'))
# print(getUpperCase('hello'))
# print(getUpperCase('HELLO'))
# print(getUpperCase('Hello, world!'))
# print(getUpperCase('goodbye 123!'))
# print(getUpperCase('12345'))
# print(getUpperCase(''))

# #35. Title case
#
# # def getTitleCase(text):
# #
# #     x = text.title()
# #     return x
# #
# # print(getTitleCase('selamat hari@raya'))
#
# def getTitleCase(text):
#
#     # Create a titledText variable to store the titlecase text:
#     titledText = ''
#
#     # Loop over every index in text:
#     for i in range(len(text)):
#
#         # The character at the start of text should be uppercase:
#         if i == 0:
#
#             titledText += text[i].upper()
#
#         # If the character is a letter and the previous character is
#         # not a letter, make it uppercase:
#         elif text[i].isalpha() and not text[i - 1].isalpha():
#
#             titledText += text[i].upper()
#
#         # Otherwise, make it lowercase:
#         else:
#
#             titledText += text[i].lower()
#
#     # Return the titled cased string:
#     return titledText

#36. Reverse string

# def reverseString(text):
#
#     final= ''
#     text = list(text)
#
#     for txt in range(len(text)-1, -1, -1):
#         final = final + text[txt]
#
#     return final
#
#
# print(reverseString('selamat hari raya'))

# #using mirror concept
# def reverseString(text):
#
#     # Convert the text string into a list of character strings:
#     text = list(text)
#
#     # Loop over the first half of indexes in the list:
#     for i in range(len(text) // 2):
#
#         # Swap the values of i and it's mirror index in the second
#         # half of the list:
#         print(i)
#         mirrorIndex = len(text) - 1 - i
#         text[i], text[mirrorIndex] = text[mirrorIndex], text[i]
#
#     # Join the list of strings into a single string and return it:
#     print(''.join(text))
#
# reverseString('hello')

# #37. change maker
# #American currency has coins in the denominations of 1 (pennies),
# # 5 (nickels), 10 (dimes), and 25 cents (quarters)
#
#
#
# def makeChange(amount):
#     #letak dalam function sbb hanya nak tambah ketika mainkan fx ni sahaja.
#     money = {
#         'quarters': 0,
#         'dimes': 0,
#         'nickles': 0,
#         'pennies': 0
#     }
#
#     # for quarters
#     if amount >= 25:
#         money['quarters'] = amount // 25
#         amount = amount % 25
#
#
#     #for dimes
#     if amount >= 10:
#         money['dimes'] = amount//10
#         amount = amount%10
#
#     #for nickel
#     if amount >= 5:
#         money['nickels'] = amount//5
#         amount = amount%5
#
#     #for pennies
#     money['pennies'] = amount
#
#     return money
#
# print(makeChange(30))
# print(makeChange(10))
# print(makeChange(57))
# print(makeChange(100))
# print(makeChange(125))

# #38. random shuffle
#
# import random
# def shuffle(values):
#     random.shuffle(values)
#     return values
#
# print(shuffle([1,2,3,4,5]))
#
# #akan shuffle kedudukan nombor yang telah diubah melalui randint.
# import random
# def shuffle(values):
#
#     for i in range(len(values)):
#
#         #index to swap
#         swapIndex = random.randint(0, len(values)-1
#         #sapping
#         values[i], values[swapIndex] = values[swapIndex], values[i]
#
#     return values
#
# print(shuffle([1,2,3,4,5]))w

# #39.collatz sequence
#
# def collatz(startingNumber):
#
#
#     if startingNumber < 1:
#         return []
#
#     # sequence.append(startingNumber)
#     sequence = [startingNumber]
#     temp = startingNumber
#
#     while temp!= 1:
#         #if odd
#         if temp%2 == 0:
#             # temp = 3 * temp + 1
#             temp = temp // 2
#
#
#         #if even
#         else:
#             # temp = temp // 2
#             temp = 3 * temp + 1
#
#         sequence.append(temp)
#
#     return sequence
#
# print(collatz(1))
# print(collatz(10))
# print(collatz(11))

#40.Merging two sorted lists

# def mergeTwoLists(list1, list2):
#
#     list3 = list1 + list2
#     list3.sort()
#     return list3
#
# def mergeTwoLists(list1, list2):
#
#     result = []
#
#     #start daripada index 0 untuk kedua2 list
#     i1= 0
#     i2= 0
#
#     #sementara belum habis list nombor
#     while i1 < len(list1) and i2 <len(list2):
#
#         #compare dan append nilai yang lebih kecil
#         if list1[i1] < list2[i2]:
#             result.append(list1[i1])
#             #untuk ke index seterusnya
#             i1 += 1
#
#         else:
#             result.append(list2[i2])
#             i2 += 1
#
#     #bila salah satu list dah di penghujungnya
#     #bila ada remainining, yang selebihnya akan ditambah dlm result
#     if i1 < len(list1):
#         for j in range(i1, len(list1)):
#             result.append(list1[j])
#     #bila ada remainining, yang selebihnya akan ditambah dlm result
#     if i2 < len(list2):
#         for j in range(i2, len(list2)):
#             result.append(list2[j])
#
#     return result
#
# ##saya baru faham tugasan ni, maknanya macam kita zip. Dia hanya compare
# #antara nombor yang bertemu. Maka yang selebihnya kita letak sahaja.
#
#
# print(mergeTwoLists([57,7,9], [5,1,90, 78, 1,9]))
#
# assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
# assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
# assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
# assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
# assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
# assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]

# #41. ROT Encryption
#
# def rot13(text):
#     # Create an encryptedText variable to store the encrypted string:
#     encryptedText = ''
#
#     # Loop over each character in the text:
#     for character in text:
#
#         # If the character is not a letter, add it as-is to encryptedText:
#         if not character.isalpha():
#             encryptedText += character
#
#         # Otherwise calculate the letter's "rotated 13" letter:
#         else:
#             rotatedLetterOrdinal = ord(character) + 13
#
#             # If adding 13 pushes the letter past Z, subtract 26:
#             if character.islower() and rotatedLetterOrdinal > 122:
#                 rotatedLetterOrdinal -= 26
#             if character.isupper() and rotatedLetterOrdinal > 90:
#                 rotatedLetterOrdinal -= 26
#
#             # Add the encrypted letter to encryptedText:
#             #convert ord to chr
#             encryptedText += chr(rotatedLetterOrdinal)
#
#     # Return the encrypted text:
#     return encryptedText
#
# print(rot13('Hello, world!'))
# print(rot13('Uryyb, jbeyq!'))
# print(rot13('abcdefghijklmnopqrstuvwxyz'))
# print(rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))





















































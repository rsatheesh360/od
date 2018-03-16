def find_odds(numbers, odds):
    if len(numbers) == 0:
        return
    v = numbers.pop()
    if v % 2 == 1:
        odds.append(v)
    find_odds(numbers, odds)

odds = []
numbers = [int(odds) for odds in input("enter the array element").split()]
find_odds(numbers,odds)
print (odds)
print(n)

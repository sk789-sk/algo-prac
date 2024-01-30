#Write a function called solution(data, n) that takes in a list of less than 100 integers and a number n, and returns that same list but with all of the numbers that occur more than n times removed entirely. The returned list should retain the same ordering as the original list - you don't want to mix up those carefully-planned shift rotations! For instance, if data was [5, 10, 15, 10, 7] and n was 1, solution(data, n) would return the list [5, 15, 7] because 10 occurs twice, and thus was removed from the list entirely.

#Simplest way i think would just be for each number check if its in the list less than n times. If it is we keep it in the list, if not we never add it. Would be slow since we go over the array twice per val N^2.


def solution(data, n):
    new_arr = []
    for val in data:
        if data.count(val) <= n:
            new_arr.append(val)
    return new_arr

def solution2(data,n):
    return [val for val in data if data.count(val) <= n]

data = [5,10,15,10,7,10]


print(solution(data,1))
print(solution2(data,1))

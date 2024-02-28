# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


#If i have a list of values, indicating when the ping occured i should just delete pings that are older than t-3000 and then return the length of the list

#while leftmost value is less than t-3000 we pop it once we hit this number we can terminate the loop

from collections import deque

def ping(self, t):
    min = t-3000

    

class RecentCounter: 
    def __init__(self):
        self.que = deque() 

    def ping(self, t):
        min_val = t-3000
        self.que.append(t)
        while self.que[0] < min_val:
            self.que.popleft()
        
        return len(self.que)
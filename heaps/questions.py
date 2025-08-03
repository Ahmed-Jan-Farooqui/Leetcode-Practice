def lastStoneWeight(self, stones: List[int]) -> int:
    import heapq
    stones = [-stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        stone1 = -heapq.heappop(stones)
        stone2 = -heapq.heappop(stones)
        if stone1 == stone2:
            continue
        if stone1 > stone2:
            heapq.heappush(stones, -(stone1 - stone2))
            continue
        if stone1 < stone2:
            heapq.heappush(stones, -(stone2 - stone1))
    return -stones[0] if len(stones) > 0 else 0


def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    '''
        To solve this question, we will maintain a max-heap of size k
        For every point, we will calculate the distance from the
        origin (sqrt(x ** 2 + y ** 2)).
        Next, if the heap is less than size k, we will put into the
        heap.
        Else, we will check the top of the heap, and if the distance
        is greater than the value at the top, we won't add it.
        If the distance is less than the value at the top, we will 
        pop the value at the top and add this element.
        At the end, we will return the three points in the heap.
        Importantly, we will use a tuple of (distance, index) in the heap,
        and return the points corresponding to the indices at the end.
    '''
    import heapq
    import math
    my_heap = []
    final = []
    for point in points:
        dist = math.sqrt((point[0] ** 2) + (point[1] ** 2))
        if len(my_heap) < k:
            heapq.heappush(my_heap, (-dist, point))
        elif -my_heap[0][0] > dist:
            heapq.heapreplace(my_heap, (-dist, point))
    
    for value in my_heap:
        final.append(value[1])
    
    return final
            
'''
    The trick here is to maintain a min heap of size k. Since the top
    will always be the smallest of the k elements, all we have to do
    is make sure we get the largest elements in here. The way we 
    do this is by evicting the top element each time we encounter
    an element greater than it. 
'''
def findKthLargest(self, nums: List[int], k: int) -> int:
    import heapq
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)
    return min_heap[0]


def leastInterval(self, tasks: List[str], n: int) -> int:
    '''
        hashmap that maps task : (time_before_allowed, count)
        simulate cpu cycles, for every cycle:
            1. Pick a task that time_before_allowed == 0 and count > 0
            2. For task x, hashmap[x] = (n, hashmap[x][1] - 1)
            3. If no tasks can be scheduled, idle.
            4. If all tasks count == 0, break.
        Here, we iterate through the hashmap every cycle, but 
        due to how the problem is structured (namely, it takes us the 
        most amount of cycles if all tasks are the same, but then the
        hashmap is of size one), the time complexity comes out to:
        O(m*m) => O(m^2)

        We realize we must schedule the most frequent task first. To do this, 
        we can maintain a max-heap. Now, we must also ensure that we don't let the
        task be scheduled again until the cooldown has passed. To do this, we
        store the cooling down tasks in a queue. And there we have it. 

        An important distinction that brings this algorithm from pseudopolynomial to
        truly polynomial: we don't need to siumlate cpu cycles. We can just
        skip to the next allowed time. 
    '''
    import heapq
    from collections import defaultdict, deque
    current = 0
    tasks_count = defaultdict(int)
    tasks_queue = deque()
    for task in tasks:
        tasks_count[task] += 1
    heap = [-tasks_count[key] for key in tasks_count]
    heapq.heapify(heap)
    while len(heap) > 0 or len(tasks_queue) > 0:
        
        # If heap is empty, skip to the task at the front of the queue.
        if len(heap) == 0:
            new_task = tasks_queue.pop()
            current = new_task[1]
            heapq.heappush(heap, new_task[0])
            continue

        # If we can put a task back to being scheduled.
        if len(tasks_queue) > 0 and current >= tasks_queue[-1][1]:
            new_task = tasks_queue.pop()
            heapq.heappush(heap, new_task[0])

        # If we have values in the heap, process them.
        task = heapq.heappop(heap) + 1
        # If we still have more of this task left, add it to the queue
        if task < 0: 
            tasks_queue.appendleft((task, current + n + 1))
        
        # Finally, increment current
        current += 1

    return current

class Twitter:
    import heapq
    from collections import defaultdict
    '''
        REALIZE:
            The timestamp is monotonically increasing. No concurrent
            tweets means no two timestamps are equal and all of a user's
            tweets are sorted in ascending order.
            As such, we can just run the merge algorithm on the user's 
            following to get the feed. 
            Importantly, since we only show the 10 most recent tweets, the
            time complexity becomes:
            10 * O(m) where m is the number of accounts the user follows.
            Therefore -> O(m) time complexity for the getNewsFeed function, and
            O(1) for everything else.
    '''
        

    def __init__(self):
        self.timestamp = 1
        self.users = {}
        self.tweets = defaultdict(list)
        self.following = defaultdict(dict)
        self.feed = defaultdict(list)

    def mergeKLists(self, userId: int) -> List[int]:
        tweets = []
        for key in self.users:
            if self.following[userId].get(key) is not None:
                tweets.append(self.tweets[key])
        counters = [len(user_tweets) - 1 for user_tweets in tweets]
        final = []
        
        for _ in range(10):
            maximum_time_stamp = float("-inf")
            maximum_val = -1
            maximum_val_idx = -1

            # Find the maximum value.
            for idx, user_tweets in enumerate(tweets):
                if counters[idx] < 0:
                    continue
                if user_tweets[counters[idx]][1] > maximum_time_stamp:
                    maximum_val = user_tweets[counters[idx]][0]
                    maximum_time_stamp = user_tweets[counters[idx]][1]
                    maximum_val_idx = idx
            
            # Change the maximum idx value.
            if maximum_val_idx != -1:
                counters[maximum_val_idx] -= 1
            # Add the maximum value in. 
            if maximum_val != -1:
                final.append(maximum_val)
        
        return final

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Also keep track of the users.
        self.users[userId] = True
        self.following[userId][userId] = True # Follow myself as well.
        # If I post a tweet, update the tweets object for my userId
        self.tweets[userId].append((tweetId, self.timestamp))
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        return self.mergeKLists(userId)


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.following[followerId]:
            del self.following[followerId][followeeId]





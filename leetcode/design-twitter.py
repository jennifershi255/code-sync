class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # stores {userId : [time, tweetId]}
        self.following = defaultdict(list) # stores {userId : [followingIds]}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following[userId]
        feed = []
        res = []
        num = 10

        for k,v in self.tweets.items():
            if k in following or k == userId:
                for i in v:
                    feed.append(i)

        heapq.heapify(feed)
        
        while feed and num > 0:
            time, val = heapq.heappop(feed)
            res.append(val)
            num -= 1
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
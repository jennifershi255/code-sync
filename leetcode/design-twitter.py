class Twitter:

    def __init__(self):
        self.time = 0
        self.twitter = defaultdict(lambda : [[],set()]) # stores {userID : [[newsFeed], [followers]]}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitter[userId][0].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        tweets_to_consider = []
        users = self.twitter[userId][1].copy()
        users.add(userId)

        for u in users:
            tweets_to_consider.extend(self.twitter[u][0][-10:])  # last 10 per user
        # sort descending by timestamp
        tweets_to_consider.sort(reverse=True)
    
        # sort for most to least recent
        for t in tweets_to_consider[:10]:
            res.append(t[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.twitter[followerId][1].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.twitter[followerId][1].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
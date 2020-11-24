class User:
    def __init__(self, nickname, rating, friends=0, posts=0, comments=0):
        self.nickname = nickname
        self.rating = rating
        self.friends = friends
        self.posts = posts
        self.comments = comments
        if self.reglament_rating():
            self.rating = 0
        if self.reglament_friends():
            self.friends = 0
        if self.reglament_posts():
            self.posts = 0
        if self.reglament_comments():
            self.comments = 0


    def __str__(self):
        return f'{self.nickname:^8} ({self.friends:^3}friends, {self.posts:^3} posts, {self.comments:^3}comments,\
    rating {self.rating:<4})'

    def like(self):
        if self.like_ratingOK():
            self.rating += 0.5

    def dislike(self):
        if self.dislike_ratingOK():
            self.rating -= 0.5

    def like_ratingOK(self):
        return self.rating <= 4.5

    def dislike_ratingOK(self):
        return self.rating >= 0.5

    def reglament_rating(self):
        return self.rating < 0

    def reglament_friends(self):
        return self.friends < 0

    def reglament_posts(self):
        return self.posts < 0

    def reglament_comments(self):
        return self.comments < 0




users = []
users.append(User("Marry", 4.0, 10, 3, 50))
users.append(User("John", 3.5, 50, 10, 60))
users.append(User("Kate", 5.0, 76, 5, 15))
users.append(User("Jane", 2.0, 8, 5,-1 ))

users[2].like()

for u in users:
    print(u)


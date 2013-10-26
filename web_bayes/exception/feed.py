class FeedReadError(Exception):

    def __init__(self, url):
        super(FeedReadError, self).__init__(url)

    def __str__(self):
        return "FeedReadError({})".format(self.url)

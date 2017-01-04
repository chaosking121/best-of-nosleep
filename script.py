def get_data():
    import pickle

    with open('data.p', 'rb') as f:
        return pickle.load(f)

if __name__ == '__main__':
    import praw
    from datetime import date

    reddit = praw.Reddit(**get_data())
    bons = reddit.subreddit('best_of_nosleep')
    ns = reddit.subreddit('nosleep')

    posts = []

    for submission in ns.top(time_filter = 'day', limit = 10):

        if (submission.link_flair_text != 'Series') and (len(posts) < 3):
            posts.insert(0,
                dict(
                    title = '[{}, +{}] "{}" by /u/{}'.format(
                        date.today(),
                        submission.score,
                        submission.title,
                        submission.author)[0:300],
                    url = submission.url.replace('www', 'np', 1),
                    send_replies = False))

    for post in posts:
        bons.submit(**post)
def get_data():
    import pickle

    with open('data.p', 'rb') as f:
        return pickle.load(f)

if __name__ == '__main__':
    import praw
    from datetime import datetime, timedelta

    reddit = praw.Reddit(**get_data())
    bons = reddit.subreddit('best_of_nosleep')
    ns = reddit.subreddit('nosleep')

    posts = []

    # Three days was arbitrarily chosen so that the first batch of posts
    # would be from 17/01/01.
    three_days_ago = (datetime.utcnow() - timedelta(days = 3)).date()

    for submission in ns.top(time_filter = 'week', limit = 50):

        post_date = datetime.utcfromtimestamp(submission.created_utc).date()

        if ((post_date == three_days_ago)
                and (submission.link_flair_text != 'Series')
                and (len(posts) < 3)):

            posts.insert(0,
                dict(
                    title = '[{}, +{}] "{}" by /u/{}'.format(
                        post_date,
                        submission.score,
                        submission.title,
                        submission.author)[0:300],
                    url = submission.url.replace('www', 'np', 1),
                    send_replies = False))

    for post in posts:
        bons.submit(**post)
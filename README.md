# Best of /r/nosleep bot.
Bot that x-posts from /r/nosleep to /r/best_of_nosleep

# About

There's a lot of not-so-great stories on /r/nosleep. This script arbitrarily selects the best ones and post them to /r/best_of_nosleep.

Right now, the bot runs as follows: every night at midnight Eastern Time, the bot will pull the top 10 posts from /r/nosleep and then, if the post does not have the 'Series' flair, it will add it to a stack. This continued until the bot goes through all 10 posts or adds the third post to the stack. Once that ends, it will begin popping posts off the stack and posting them to /r/best_of_nosleep using non-participation links with titles of the format '[$iso-format-date, +$score] "$original-title" by /u/$original-poster'.


# Usage

If you're using this, I assume it's to automatically post to a similar subreddit. In which case, you'll want to replace the hard-coded strings 'nosleep' and 'best_of_nosleep' in script.py with your source and output subs respectively. Next, you'll want to use the [pickle python module](https://docs.python.org/2/library/pickle.html) to dump a dict to the file data.p in the same directory as the script.py file. The dict should have the following fields, as described by the [PRAW documentation](https://praw.readthedocs.io/en/stable/getting_started/authentication.html#oauth) for script-type bots:
* client_id
* client_secret
* password
* user_agent
* username

Then, you'll want to use pip to install the necessary requirements from the requirements.txt file. You can do that with:  

`pip install -r requirements.txt`.   

You'll want to have [pip installed](https://pip.pypa.io/en/stable/installing/) and, naturally, this should be done in a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Also, for reference, I'm using Python 2.7.6, which I'm sure is less than ideal.

From there, running this from the terminal with `python script.py` will be enough. Ideally, you'd want to make this a cronjob or your OS's equivalent to ensure it runs automatically at midnight. But, you could always leave it running all the time and use a time.sleep() of the appropriate length instead.

import praw
import time

user_agent = ("tm_finder comment searcher by /u/pinebender")
r = praw.Reddit(user_agent=user_agent)
thing_limit = 10

# get posts with "trademark" in comments
search_terms = ["trademark", "Trademark", "trade mark", "Trade Mark", "Trade mark", "copyright", "patent"]
comment_added = set()
submission_added = set()
iteration = 0
while True:
	
	# check submission titles for keyword
	#submissions = r.get_subreddit("all").get_new()
	submissions = r.get_subreddit("law+legal+legaladvice+cyberlaws+startups+entrepreneur+smallbusiness").get_new()
	for submission in submissions:
		for search_term in search_terms:
			if search_term in submission.title and submission.id not in submission_added:
				with open("comments.html", "a") as f:
					f.write(submission.title.encode("utf-8", "replace"))
					f.write("<br>")
					f.write(submission.permalink)
					f.write("<br><br>")
					print(submission.title + "\n")
					print(submission.permalink + "\n\n")
					submission_added.add(submission.id)

	# check comments for keyword
	comments = r.get_comments("law+legal+legaladvice+cyberlaws+startups+entrepreneur+smallbusiness")
	for comment in comments:
		for search_term in search_terms:
			if search_term in comment.body and comment.id not in comment_added:
				with open("comments.html", 'a') as f:
					f.write(comment.submission.title.encode("utf-8", "replace"))
					f.write("<br>")
					f.write(comment.permalink)
					f.write("<br>")
					f.write(comment.body)
					f.write("<br><br>")
					print(comment.submission.title + "\n")
					print(comment.permalink + "\n")
					print(comment.body +"\n\n")
					comment_added.add(comment.id)
	# wait
	iteration += 1
	print(iteration)
	time.sleep(180)


'''
convert to flask app:

save results to a database
send results to html
use jinja to display comments
'''
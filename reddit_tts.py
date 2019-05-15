import json
import os
import praw
import inquirer
from voice import speak

def make_title_index_dict(submissions):
	look_up = {}
	choices = []
	submissions_store = {}
	for _, submission in enumerate(submissions):
		look_up[submission.title] = submission.id
		choices.append(submission.title)
		submissions_store[submission.id] = submission
	return look_up, choices, submissions_store

def make_menu(look_up, choices, submissions_store):
	menu = [
		inquirer.List('posts',
		message="Select a post",
		choices=choices,
		),
		]
	title = inquirer.prompt(menu).get('posts')
	os.system('clear') 
	index = look_up[title]
	submission = submissions_store[index]
	return submission

def main():
	with open('credentials.json', 'r') as file:
		CREDENTIALS = json.load(file)
	
	with open('config.json', 'r') as file:
		CONFIG = json.load(file)
		subreddit_name = CONFIG['subreddit']
		limit = CONFIG['limit']

	reddit = praw.Reddit(**CREDENTIALS)
	chosen_subreddit = reddit.subreddit(subreddit_name)
	submissions = chosen_subreddit.hot(limit=limit)
	look_up, choices, submissions_store = make_title_index_dict(submissions)
	while True:
		submission = make_menu(look_up, choices, submissions_store)
		print('Playing: {}'.format(submission.title))
		msg = submission.selftext
		speak(msg)

if __name__ == "__main__":
	main()

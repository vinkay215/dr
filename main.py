# This is an example to prove that people shouldn't overrated a person by 
# his/her github graph

from datetime import datetime
from datetime import timedelta
import subprocess, argparse

parser = argparse.ArgumentParser("graph-drawer")
parser.add_argument('-i', '--input-file', help='path to the input file.', default='example.txt')
parser.add_argument('-d', '--start-date', help='date to start drawing in iso 8601 format e.g., 2014-01-07T02:00:00+70:00', default='2013-01-07T00:00:00+00:00')

args, unknownargs = parser.parse_known_args()

start_date = datetime.fromisoformat(args.start_date)

def gen_cmd(date):
	cmd = []
	cmd.append('git')
	for u in unknownargs:
		cmd.append(u)
	cmd.append('commit')
	cmd.append('--date="' + str(date.isoformat()) +'"')
	cmd.append('-m ""')
	cmd.append('--allow-empty')
	cmd.append('--allow-empty-message')

	env = {}
	env["GIT_COMMITTER_DATE"] = str(date.isoformat())

	return cmd, env

def git_commit(date):
	cmd, env = gen_cmd(date)
	# print(cmd)
	subprocess.call(cmd, env=env)

with open(args.input_file, 'r') as f:
	for line in f:
		for c in line[::-1]:
			if c >= '0' and c <= '9':
				print(int(c))
				for i in range(int(c)):
					# print(start_date, c)
					git_commit(start_date)
				start_date += timedelta(1)
		print()

# print(unknownargs)
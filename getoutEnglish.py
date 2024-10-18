#! /usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
	import random
	import json
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("--dict", default="dict.json")
	parse_result = parser.parse_args()

	words = dict()
	for filename in parse_result.dict.split(","):
		with open(filename, "rt", encoding="utf-8") as f:
			words.update(json.loads(f.read()))
	
	keys = [ i for i in words.keys() ]
	random.shuffle(keys)
	wrong = {}
	for i in keys:
		print(i, ": ", end='')
		inputValue = input()
		if inputValue != words[i]:
			wrong [i] = inputValue
	
	print("\033[1mFinish, here the result:\033[0m")
	for i in wrong:
		print(i, ": ", words[i], " (Your answer: ", wrong[i], ")")
	print("\033[1mAll for all\033[0m")


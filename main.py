
from stats import *
import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		get_book_text(sys.argv[1])

def get_book_text(input):
	with open(input) as f:
		contents = f.read()

	word_count_return = get_num_words(contents)

	output = f"Found {word_count_return} total words"


	lower_characters = contents.lower()
	result = character_count(lower_characters)


	sorted_result = {k: v for k, v in sorted(result.items(), key = lambda v: v[1], reverse = True)}


	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("---------- Word Count ----------")
	print(output)
	print("--------- Character Count ---------")
	for key, value in sorted_result.items():
		print(f"{key}: {value}")


main()

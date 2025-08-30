def get_num_words(input):
	words = input.split()
	word_count = len(words)
	return word_count

def character_count(input):
	char_counts = {}

	for char in input:
		char_counts[char] = char_counts.get(char, 0) + 1
	alphabet_filtered = {k: v for k, v in char_counts.items() if k.isalpha()}
	return alphabet_filtered

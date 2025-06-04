def sentenceToSet(sentence):
	return set(sentence.strip().split())

def displaySet(heading, theSet):
	print(heading)
	for word in theSet:
		    print(word)
	print('The number of common words is %d' % (len(theSet)))

def main():
	print('Each sentence must consist of words in lowercase')
	print(' only, no punctuation!')
	sentence1 = input("Enter the first sentence:\n")
	wordSet1 = sentenceToSet(sentence1)
	sentence2 = input("Enter the second sentence:\n")
	wordSet2 = sentenceToSet(sentence2)
	commonWords = wordSet1.intersection(wordSet2)
	displaySet('\nThe set of words common to the sentences is:',
               commonWords)

main()
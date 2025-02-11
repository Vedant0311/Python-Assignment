import string

def word_count(input_text):

    input_text = input_text.lower()
    input_text = input_text.translate(str.maketrans('', '', string.punctuation))
    
    words = input_text.split()
    
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    return word_freq

input_text = input("Enter a sentence or text: ")

output = word_count(input_text)

print("Word count:", output)

input("Press Enter to exit...")

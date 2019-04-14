# Reverse a sentence, but don't reverse the words
# Alice likes Bob => Bob likes Alice
# String is only separated by whitespace

# Make the string sentence into a list of chars since strings are immutable
def reverse_words(sentence):
    s = list(sentence)[::-1]

    beginning_of_word = 0
    for i, c in enumerate(s):
        if c == ' ':
            s[beginning_of_word:i] = s[beginning_of_word:i][::-1]
            beginning_of_word = i+1

    s[beginning_of_word:len(s)] = s[beginning_of_word:len(s)][::-1]
    return ''.join(s)

if __name__ == "__main__":
    s = 'ram is costly'
    print(reverse_words(s))
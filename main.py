def count_words(file_content):
    words = file_content.split()
    return len(words)

def count_chars(file_content):
    words = file_content.split()
    output = {}
    for word in words:
        for char in word.lower():
            if char not in output:
                output[char]=1
            else:
                output[char]+=1
    return output

def format_output(num_words, character_dict):
    print(f"There are {num_words} words in the text.")
    print("Lets break down how many characters there are!")
    for i in character_dict:
        print(f"The character {i} appears {character_dict[i]} times.")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    number_of_words = count_words(file_contents)
    characters_analysis = count_chars(file_contents)
    format_output(number_of_words, characters_analysis)
    
main()

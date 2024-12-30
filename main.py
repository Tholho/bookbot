from collections import defaultdict

def count_each_letter(text):
    formatted_text = text.lower()
    letters_dict = defaultdict(int)
    
    for letter in formatted_text:
        if 'a' <= letter <= 'z':
            letters_dict[letter] += 1
    
    return (letters_dict)

def report_letters(book):
    report = ""
    letters_dict = count_each_letter(book)
    for letter in letters_dict:
        report += "The '" + letter + "' character was found " + str(letters_dict[letter]) + " time"
        if letters_dict[letter] > 1:
            report += "s\n"
        else:
            report += "\n"
    return report

def report_book(book):
    report = "--- Begin report of books/frankenstein.txt ---"
    word_count = str(count_words(book))
    report += word_count + " words found in the document" + "\n" + "\n"
    report += report_letters(book)
    report += "--- End report ---"
    return report


def count_words(text):
    words_array = text.split()
    return len(words_array)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(report_book(file_contents))
main()
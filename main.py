def count_words(content):
    return len(content.split())

def letter_frequency(contents):
    ret = {}
    for ch in contents.lower():
        if not ch.isalpha():
            continue
        if not ch in ret:
            ret[ch] = 0
        ret[ch]+=1
    return ret

def book_report(contents, file_name):
    print(f"------book report for {file_name}------")
    print(f"{count_words(contents)} words found in the document")
    print("")
    freq = letter_frequency(contents)
    for entry in freq:
        print(f"The '{entry}' character was found {freq[entry]} times")
    


def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    book_report(file_contents, book_path)
main()
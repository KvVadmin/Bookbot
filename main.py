def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    words_lowered = text.lower() 
    num_character = get_num_character(words_lowered)
    char_list = []
    for char, count in num_character.items():
        char_dict = {'char': char, 'count': count}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key= sort_on)
   # sorted_num_character = dict(sorted(num_character.items()))
    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{num_words} words found in the document")
    for i in char_list:
        print(f"The '{i['char']}' character was found {i['count']} times")  
    print ("--- End report ---")



def get_num_words(text):
    num_words = text.split()
    return len(num_words)

    

def get_book_text(book_path):
    with open (book_path) as f:
        return f.read()
    

def get_num_character(words_lowered):
    characters_count = {}
    for i in words_lowered:
        if i.isalpha():
            if i in characters_count:
                characters_count[i] += 1  
            else: characters_count [i] = 1

    return characters_count


def sort_on (dict):
    return dict ["count"]




    
main()


     



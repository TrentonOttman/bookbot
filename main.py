def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        lower_file_contents = file_contents.lower()
        char_dictionary = charcount(lower_file_contents)

        listOfDicts = convertToListOfDicts(char_dictionary)
        listOfDicts.sort(reverse=True, key=sort_on)

        num_words = wordcount(file_contents)

        printReport(num_words, listOfDicts)

        return 0

def wordcount(stringList):
    words = stringList.split()
    return len(words)

def charcount(stringList):
    char_dict = {}
    for char in stringList:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def convertToListOfDicts(dictionary):
    listOfDicts = []
    for key in dictionary:
        currDict = {}
        currDict["key"] = key
        currDict["value"] = dictionary[key]
        listOfDicts.append(currDict)
    return listOfDicts


def sort_on(dict):
    return dict["value"]

def printReport(num_words, listOfDicts):
    print("Report of frankenstein.txt:\n")
    print(f"There were {num_words} words found in the text\n")
    print("Here is a list of characters and their frequencies:\n")
    for dict in listOfDicts:
        if dict["key"].isalpha():
            print(f"{dict["key"]} : {dict["value"]}")
    print("\nEnd of the report\n")


main()
    
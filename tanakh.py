import re
import os
import sys


def is_heb_letter(letter):
    """Returns False if a letter is teamim or nikkud and True otherwise

    Should only be used with single character strings
    """
    teamimpattern = re.compile("[\u0591-\u05BD\u05C1\u05C2\u05C7]")
    if re.match(teamimpattern, letter):
        return False
    else:
        return True


def searchterm_pattern(input):
    """Constructs a re pattern which searches for a string of words starting with the letters of the input"""
    string = ""
    for x in input:
        string += "[\u05BE  ]"+x + \
            "[\u05D0-\u05EA\u0591-\u05BD\u05C1\u05C2\u05C7]*"
        # pattern indicates: hebrew letter or hebrew teamim/nikud or shin/sin signs or katamz qatan.
    return re.compile(string)


input = sys.argv[1]

# Goes through each text file for each book of the tanakh
for filename in os.listdir("Tanach.txt\TextFiles\\"):
    with open("Tanach.txt\TextFiles\\" + filename, encoding="utf8") as file:
        terms = re.findall(searchterm_pattern(input), file.read())
        if terms != []:
            print(filename)
            # The map and filter just clean up the output by filtering out nikkud and teamim
            print(list(map(lambda pasuk: "".join(
                list(filter(is_heb_letter, pasuk))), terms)))

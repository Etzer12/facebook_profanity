"""
FileName: Facebook Filter.py
Version: 1.0
Author: Andrew Racine
Python version: 2.7
Date of Creation: 1/14/2016
Date of Last modification 1/15/2016
Synopsis: This program checks articles against a the conditions set by facebook instant to determine whether or not it
is suitable to be uploaded to facebook.
"""

import WebpageParser

PAUSE_ON_ERROR = False
"""
If you would like to stop the program when it finds a article that does not pass all the tests to review the article,
set the PAUSE_ON_ERROR variable to True. if you would like to skip them, set it to False.
"""

def parse_single(webpage):
    """
    This function parses a single webpage and calls the filtering functions.
    :param webpage: A article URL
    :return: None
    """
    text = WebpageParser.get_webpage(webpage)
    if text is False:
        print "Error processing the webpage. It may no longer exist or has text that doesn't support parsing"
        if PAUSE_ON_ERROR:
            raw_input()
    else:
        text = text.lower()
        print "Testing article: {}".format(webpage)
        passed = filtering_checks(text)
        print "This article passed {} tests and failed {}".format(passed, abs(passed - 5))
        if passed < 5 and PAUSE_ON_ERROR:
            raw_input()


def parse_multiple():
    """
    This function recursively goes through a specified file and checks all the URL's inside against the guidelines.
    :return: None
    """
    print "Please ensure the text file contains only one URL per line, and that the file is in the project folder."
    file_name = raw_input("Enter the list of websites: ")
    lst_of_articles = []
    f = open(file_name, "r")
    for line in f:
        lst_of_articles.append(line.strip())
    articles_checked = 0
    for article in lst_of_articles:
        parse_single(article)
        articles_checked += 1
    raw_input("Finished checking all websites.")
    print "{} articles were checked in this search.".format(articles_checked)



def filtering_checks(text):
    """
    This helper function manges the tests.
    :param text: The text of a article
    :return: How many tests were passed
    """
    passed = 0
    passed += filter_attack_on_public_figures(text)
    passed += filter_dangerous_organizations(text)
    passed += filter_hate_speech(text)
    passed += filter_self_injury(text)
    passed += filter_sexual_violence_and_exploitation(text)
    return passed


def filter_attack_on_public_figures(text):
    """
    Tests the articles to ensure they do not defame and public figures
    :param text: the articles information.
    :return: Pass/fail Value
    """
    f = open("Attack on Public Figures.txt", "r")
    lst_of_criteria = []
    used_words = []
    for word in f:
        lst_of_criteria.append(word.strip())
    f.close()
    passed = True
    for slander in lst_of_criteria:
        slander = slander.lower()
        if slander in text:
            passed = False
            if slander not in used_words:
                used_words.append(slander)
    if passed is False:
        print "Attack on public figures test failed."
        print "Reason: this articles calls a person a bad influence or role model"
        print "Facebook does not allow the slander of public figures."
        print "---------------------------------------------------------------------------"
        return 0
    else:
        return 1


def filter_dangerous_organizations(text):
    """
    Tests the articles to ensure they don't talk about terrorist groups
    :param text: the articles information.
    :return: Pass/fail Value
    """
    f = open("Dangerous Organizations.txt", "r")
    lst_of_organizations = []
    used_words = []
    for word in f:
        lst_of_organizations.append(word.strip())
    f.close()
    passed = True
    for organization in lst_of_organizations:
        organization = organization.lower()
        if organization in text:
            passed = False
            if organization not in used_words:
                used_words.append(organization)
    if passed is False:
        print "Dangerous Organizations test failed."
        print "Reason: The following Terrorist group(s) were mentioned: {}".format(used_words)
        print "Supporting leaders, or condoning their actions are against the guidelines set."
        print "This article may not violate the terms, but ensure that it shows sensitivity towards victims."
        print "---------------------------------------------------------------------------"
        return 0
    else:
        return 1


def filter_hate_speech(text):
    """
    Tests articles to ensure they don't contain words that discriminates against any races or groups of people
    :param text: the articles information.
    :return: Pass/fail Value
    """
    f = open("Hate Speech.txt", "r")
    lst_of_hate = []
    used_words = []
    for word in f:
        lst_of_hate.append(word.strip())
    f.close()
    passed = True
    for word in lst_of_hate:
        word = word.lower()
        if word in text:
            passed = False
            if word not in used_words:
                used_words.append(word)
    if passed is False:
        print "Hate Speech test failed."
        print "Reason: the following words were found in webpage: {}".format(used_words)
        print "These words are against the terms of service on facebook and can lead to a deleted post."
        print "---------------------------------------------------------------------------"
        return 0
    else:
        return 1


def filter_self_injury(text):
    """
    Tests the article to ensure there isn't any talk of suicide.
    :param text: the articles information.
    :return: Pass/fail Value
    """
    f = open("Self Injury.txt", "r")
    lst_of_criteria = []
    used_words = []
    for word in f:
        lst_of_criteria.append(word.strip())
    f.close()
    passed = True
    for word in lst_of_criteria:
        word = word.lower()
        if word in text:
            passed = False
            if word not in used_words:
                used_words.append(word)
    if passed is False:
        print "Self Injury test failed."
        print "Reason: this articles contains talk of suicide or self injury"
        print "If the context is of oneself, this goes against the guidelines provided by facebook."
        print "---------------------------------------------------------------------------"
        return 0
    else:
        return 1


def filter_sexual_violence_and_exploitation(text):
    """
    Tests the article to ensure there isn't any sexual violence/rape mentioned.
    :param text: the articles information.
    :return: Pass/fail Value
    """
    f = open("Sexual Violence and Exploitation.txt", "r")
    lst_of_criteria = []
    used_words = []
    for word in f:
        lst_of_criteria.append(word.strip())
    f.close()
    passed = True
    for slander in lst_of_criteria:
        slander = slander.lower()
        if slander in text:
            passed = False
            if slander not in used_words:
                used_words.append(slander)
    if passed is False:
        print "Sexual Violence and Exploitation test failed."
        print "Reason: this articles contains talk of rape or sexual abuse"
        print "This material goes against the guidelines provided by facebook under any circumstances."
        print "---------------------------------------------------------------------------"
        return 0
    else:
        return 1



def main():
    response = raw_input("Are you checking a single webpage or multiple? Enter 'S' or 'M'.").upper()
    if response == "S":
        webpage = raw_input("Enter URL: ")
        parse_single(webpage)
    elif response == "M":
        parse_multiple()
    else:
        print "Invalid input"
        main()


#  User info
raw_input("Welcome to facebook filter version 1.0 (Enter to continue)")
print "Please note that just because an article fails a test, it does not mean it does not follow the guidelines."
raw_input("It just means that it contains material that may be unsuitable. (Enter to continue)")
main()
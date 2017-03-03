__author__ = 'Andrew'

import urllib2
import time
from bs4 import BeautifulSoup


def get_webpage(webpage):
    """
    This function takes in a URL and returns the body text contained in the processed URL
    :param webpage: A URL
    :return: Body of Text
    """
    try:
        response = urllib2.urlopen(webpage)
    except:
        return False
    html = response.read()
    try:
        soup = BeautifulSoup(html, 'html.parser')
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text
    except:
        time.sleep(1)
        return False


def get_webpage_output(webpage,output):
    """
    This function takes in a URL and returns the body text contained in the processed URL
    :param webpage: A URL
    :return: Body of Text
    """
    response = urllib2.urlopen(webpage)
    html = response.read()
    try:
        soup = BeautifulSoup(html, 'html.parser')
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text
    except:
        time.sleep(1)
        output.write("The following line could not be parsed: {}".format(webpage))
        output.write('\n')
        output.write("---------------------------------------------------------------------------")
        output.write('\n')
        print("The following line could not be parsed: {}".format(webpage))
        print("---------------------------------------------------------------------------")
        return False
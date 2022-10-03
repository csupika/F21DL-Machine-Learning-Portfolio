"""
Downloads data of "vital" Wikipedia articles for the MSc project.
Can also process the data in various ways.

------

Hi group members! Here's what I think you'll need to do:
- unzip the articles folder in the same location as this file.
- run this python file.
It will take a few seconds, but then there will be a massive dictionary
containing the data for each article.

(I think having a dictionary of dictionaries might be bad practice?
Or is that what JSON files do? Oh, well, it's what I've done.)

Some of the other functions here are to download the data from scratch,
but they won't work unless you have the wikipedia module installed.

------

The early functions here are to actually download the data
from scratch, but that won't work unless you install the wikipedia module.

The following files have been renamed:
HIV/AIDS --> HIV_Aids
Acid–base reaction --> Acid-base reaction (uses a different dash)
If you have any problems, it might be because of these files!


"""

# ALWAYS put auto_suggest=False when calling the wikipedia page method!
# Beware articles with a comma in their title!

import os
import wikipedia #un-comment this if you want to use it!
import string
import ast

# I have a horrible feeling that ast has too much power...
# but it serves its job for now.

NUMERICAL_COLUMNS = ("Links", "Categories", "Images", "References", "Length")
QUALITY_MAP = {"FA": 5, "GA": 4, "A": 4, "B": 3, "C": 2, "Start": 1}
LIST_OF_ARTICLES = [x.removesuffix(".txt") for x in os.listdir("articles")]


# To do:
# Download all the pages in the list.
# Save them all in an easy-to-process format.
# Check if their titles match what I'm looking for.
# If not, I can inspect the oddities.
# Maybe extract other categories?

def download_and_store(page_title, overwrite_existing_files=False):
    """Downloads and saves data for the named wikipedia article."""
    # WILL NOT WORK without the "wikipedia" module installed.
    if '|' in page_title:
        page_title = page_title.split('|')[0]
    page = wikipedia.page(page_title, auto_suggest=False)
    if page.title != page_title:
        print("This page's title is different from the input!")
        print("Input:", page_title)
        print("Title:", page.title, '\n')
    if not overwrite_existing_files and os.path.exists(f"articles\\{page_title}.txt"):
        print(f"{page.title} has already been downloaded. I'm leaving it alone.\n")
        return
    with open(f"articles\\{page_title}.txt", 'w', encoding='utf-8') as page_file:
        entries = [
            # data I haven't used has been commented out.
            (page.title, 'TITLE'),
            (page.links, 'LINKS'),  # All the other wikipedia pages this one links to.
            (page.categories, 'CATEGORIES'),  # All of the categories that this page has been put in.
            # Within the categories, we could extract simpler categories, and ignore admin categories.
            #            (page.coordinates, 'COORDINATES'), # Only if this page has associated coordinates.
            (page.images, 'IMAGES'),  # Names of image files in this page.
            #            (page.original_title, 'ORIGINAL_TITLE'), # If the title has been changed, I assume this is the oldest one.
            #            (page.pageid, 'PAGEID'), # A reference number
            #            (page.parent_id, 'PARENT_ID'),
            (page.references, 'REFERENCES'),  # All the
            #            (page.revision_id, 'REVISION_ID'),
            #            (page.sections, 'SECTIONS'), #Section headings, but I'm not sure this works.
            #            (page.url, 'URL') # Where to find this page
            (page.summary, 'SUMMARY'),  # The first chunk of text.
            (page.content, 'CONTENT')  # The entire text of the article.
        ]
        for entry in entries:
            page_file.write(f"####### {entry[-1]} #######\n\n")
            page_file.write(str(entry[0]) + '\n\n')  # Yay, it handles \n correctly!
    # other things I could fetch:
    # page quality
    # interested wikiprojects and their rankings
    #


def collate_articles(list_of_article_names):
    """Puts all the already-downloaded articles named in the list into in a single file."""
    # Untested since I first used it, despite editing...
    with open("collated_articles.txt", 'w', encoding="utf-8") as collated_articles:
        for article_name in list_of_article_names:
            collated_articles.write('#' * 27 + "\n####### NEW ARTICLE #######\n" + '#' * 27 + "\n\n")
            with open(f"articles\\{article_name}.txt", encoding="utf-8") as article_file:
                for line in article_file:
                    collated_articles.write(line)


def get_article_data_from_file(article_name):
    with open(f"articles\\{article_name}.txt", encoding="utf-8") as article_file:
        data = {}
        current_key = None
        for line in article_file:
            if "#######" in line:
                current_key = line.strip("# \r\n").capitalize()
                data[current_key] = ''
                # Will be added to if it's meant to be a string,
                # and overwritten if it's meant to be a list.
            else:
                text = line.strip()
                if len(text) > 0:
                    if text[:2] in ('["', "['") and text[-2:] in ('"]', "']"):  # looks like a list
                        data[current_key] = ast.literal_eval(text)
                    else:
                        data[current_key] += text
    return data


def get_article_numbers(article_name):
    """Summary statistics of the article."""
    data = get_article_data_from_file(article_name)
    data["Length"] = data["Content"]
    return {x: len(data[x]) for x in NUMERICAL_COLUMNS}


def generate_numerical_csv_file():
    with open("Numerical_article_summary.csv", 'w', encoding="utf-8") as summary_file:
        summary_file.write("Title, " + ', '.join(NUMERICAL_COLUMNS) + '\n')
        with open("List of level 3 vital articles.txt", encoding="utf-8") as article_list:
            for line in article_list:
                article_name = line.strip().replace('/', '_')
                summary_file.write(article_name + ',')
                with open(f"articles\\{article_name}.txt", encoding="utf-8") as article_file:
                    data = get_article_numbers(article_name)
                    for column in NUMERICAL_COLUMNS:
                        summary_file.write(str(data[column]))
                        if column != NUMERICAL_COLUMNS[-1]:
                            summary_file.write(",")
                summary_file.write('\n')


def word_counts(article_name):
    """Gives the word count for all words in the article."""
    article_data = get_article_data_from_file(article_name)
    # letters_to_strip = ''.join([letter for letter in string.printable if letter not in string.ascii_lowercase]) #remove everything that's not a letter
    text = article_data["Content"].lower().split()  # Consider using "categories" or "links" as well.
    text = [word.strip(string.punctuation) for word in text]
    words = set(text)
    return {word: text.count(word) for word in words}


def generate_word_count_columns():
    with open("List of level 3 vital articles.txt", encoding="utf-8") as article_list:
        article_names = [line.strip().replace('/', '_') for line in article_list]
    all_counts = {article_name: word_counts(article_name) for article_name in article_names}
    all_words = []
    for article_name in all_counts:  # This may be bad for memory...
        print(article_name + "...", flush=True)
        for word in all_counts[article_name]:
            if word not in all_words:
                all_words.append(word)
    #        all_words += list(all_counts[article_name].keys())
    #        all_words = set(all_words)
    return all_words  # article_names


all_article_data = {name: get_article_data_from_file(name)
                    for name in LIST_OF_ARTICLES}
asd = 0
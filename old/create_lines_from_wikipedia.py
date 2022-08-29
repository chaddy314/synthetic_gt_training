import sys
import re
import requests
from bs4 import BeautifulSoup
import random
import wikipedia
from wikipedia import DisambiguationError, PageError


def main():
    max_count = int(sys.argv[1])
    language = sys.argv[2]
    # lines = create_strings_from_wikipedia(4, 20, max_count, language)
    # max_words = 0
    # for line in lines:
    #     max_words = max_words + len(line.split(" "))
    #
    # print("mean word length: " + str(max_words/max_count))
    lines = create_lines_from_wiki_but_better(['en'], 4, 11, max_count)
    with open("text/text_from_wiki_" + language + '_' + str(max_count) + ".txt", 'w') as f_out:
        f_out.writelines(s + '\n' for s in lines)


# https://github.com/Belval/TextRecognitionDataGenerator/blob/f096b6f623d2d7fd1844c809e8298950d4431b85/trdg/string_generator.py#L45
#
def create_strings_from_wikipedia(minimum_length, maximum_length, count, lang):
    """
        Create all string by randomly picking Wikipedia articles and taking sentences from them.
    """
    sentences = []

    while len(sentences) < count:
        # We fetch a random page

        page_url = "https://{}.wikipedia.org/wiki/Special:Random".format(lang)

        try:
            page = requests.get(page_url, timeout=3.0)  # take into account timeouts
        except requests.exceptions.Timeout:
            continue

        print(page.url)
        soup = BeautifulSoup(page.text, "html.parser")

        for script in soup(["script", "style"]):
            script.extract()

        # Only take a certain length
        lines = list(
            filter(
                lambda s: maximum_length >= len(s.split(" ")) > minimum_length
                          and not "Wikipedia" in s
                          and not "wikipedia" in s,
                [
                    " ".join(re.findall(r"[\w']+", s.strip()))[0:200]
                    for s in soup.get_text().splitlines()
                ],
            )
        )

        # Remove the last lines that talks about contributing
        sentences.extend(lines[0: max([1, len(lines) - 5])])
    return sentences[0:count]


def create_lines_from_wiki_but_better(lang_list, min_word, max_word, line_count):
    lines = []
    length_range = list(range(min_word, max_word))

    while len(lines) < line_count:
        wikipedia.set_lang(random.choice(lang_list))
        try:
            text = wikipedia.page(wikipedia.random(1)).content
        except (DisambiguationError, PageError):
            continue
        text = text.replace('\n', ' ')
        words = text.split(' ')
        new_lines = []
        while len(words) > max_word:
            line_words, words = split_list(words, random.choice(length_range))
            line = " ".join(line_words).rstrip().lstrip()
            if len(line) > 5 and line.count('=') < 3 and not "http" in line:
                new_lines.append(line)
        print(new_lines)
        lines.extend(new_lines)
    return lines[0:line_count]


def split_list(a_list, count):
    return a_list[:count], a_list[count:]


if __name__ == "__main__":
    main()

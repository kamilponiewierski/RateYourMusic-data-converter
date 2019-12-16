import re
import datetime


class AlbumRating:
    rating = 0
    name = ""
    rate_date = ""

    def __init__(self, rate_date, name, rating):
        self.rate_date = rate_date
        self.name = name
        self.rating = int(float(rating) * 2)

    def __str__(self):
        return str(self.rate_date) + "\t" + str(self.rating) + "\t" + self.name


def month_to_int(month):
    months = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }
    return months[month]


def convert_text_to_album_rating_list(rows):
    album_ratings_list = []
    rating_regex = re.compile(
        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s'  # month
        r'(\d{2})\s'              # day
        r'(\d{4})[\s]*'            # year
        r'(\d.\d{2}) stars\s'     # rating
        r'\[Rating[0-9]*\]\s'     # skipping rym rating number
        r'(.*)\n'
    )                # full artist name + album name + year

    m = rating_regex.finditer(rows)
    for match in m:
        assert(month_to_int("Aug") == 8)
        month = month_to_int(match.group(1))
        ratedate = datetime.date(int(match.group(3)), month, int(match.group(2)))
        album_ratings_list.append(AlbumRating(ratedate, match.group(5), match.group(4)))

    return album_ratings_list


file = open("in.txt", encoding='utf-8')
text = file.read()
album_rating_list = convert_text_to_album_rating_list(text)
file.close()

with open("result.txt", "w+", encoding="utf-8") as out:
    for album_rating in album_rating_list:
        out.write(str(album_rating) + '\n')

from collections import namedtuple
import arrow

Sign = namedtuple(
    'Sign',
    ['name', 'description', 'start', "end", "element", "quality"]
)

aries =         Sign('Aries', 'The Ram', 'March 21', 'April 19', 'Fire', 'Cardinal')
taurus =        Sign('Taurus', 'The Bull', 'April 20', 'May 20', 'Earth', 'Fixed')
gemini =        Sign('Gemini', 'The Twins', 'May 21', 'June 21', 'Air', 'Mutable')
cancer =        Sign('Cancer', 'The Crab', 'June 22', 'July 22',  'Water', 'Cardinal')
leo =           Sign('Leo', 'The Lion', 'July 23', 'August 22', 'Fire', 'Fixed')
virgo =         Sign('Virgo', 'The Virgin', 'August 23', 'September 22', 'Earth', 'Mutable')
libra =         Sign('Libra', 'The Scales', 'September 23', 'October 23', 'Air', 'Cardinal')
scorpio =       Sign('Scorpio', 'The Scorpion', 'October 24', 'November 20', 'Water', 'Fixed')
sagittarius =   Sign('Sagittarius', 'The Archer', 'November 21', 'December 22',  'Fire', 'Mutable')
capricorn =     Sign('Capricorn', 'The Sea Goat', 'December 23', 'January 20', 'Earth', 'Cardinal')
aquarius =      Sign('Aquarius', 'The Water Bearer', 'January 21', 'February 21', 'Air', 'Fixed')
pisces =        Sign('Pisces', 'The Fish', 'February 22', 'March 20', 'Water', 'Mutable')

sign_list = [aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces]
all_signs = set(sign_list)

sign_map = {}

for sign in sign_list:
    sign_map[sign.name.lower()] = sign


def get_sign(month, day):

    fake_day = arrow.get(0001, month, day)

    for sign in all_signs:
        start = arrow.get(sign.start, "MMMM DD")
        end = arrow.get(sign.end, "MMMM DD")

        if start.month == 12 and \
               (fake_day >= start and fake_day <= arrow.get(0001, 12, 31) or
                fake_day >= arrow.get(0001, 1, 1) and fake_day <= end):
            return sign
        elif fake_day >= start and fake_day <= end:
            return sign

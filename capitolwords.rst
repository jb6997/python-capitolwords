===================
python-capitolwords
===================

All that is required to start using the API is for it to be imported, no API key is
required for Capitol Words.

Import ``capitolwords``:
    
    >>> import capitolwords
    
All Capitol Words API methods return a WordResult object with three attributes:
    * word          - a word in question
    * word_date     - a particular date
    * word_count    - the number of times ``word`` was said on ``word_date``

dailysum
========

``dailysum(word, year, month=None, day=None, endyear=None, endmonth=None, endday=None)``

dailysum returns a list of records given a word and a series of days.

Using ``dailysum`` to find out how many times 'transparency' was said on
May 22nd 2008:

    >>> wr = capitolwords.dailysum('transparency', 2008, 5, 22)[0]
    >>> print wr.word_count
    24

Using ``dailysum`` to find out how many times 'transparency' was said
in May 2008:

    >>> for wr in capitolwords.dailysum('transparency', 2008, 5):
    ...     print wr.word_date, wr.word_count
    2008-05-23 3
    2008-05-22 24
    2008-05-21 3
    2008-05-19 25
    2008-05-15 15
    2008-05-14 17
    2008-05-13 13
    2008-05-12 10
    2008-05-08 8
    2008-05-07 9
    2008-05-06 5
    2008-05-02 1
    2008-05-01 3

Using ``dailysum`` to find out how many times 'transparency' was said
for all days in a given range of days:

    >>> for wr in capitolwords.dailysum('transparency', 2008, 4, 3, 2008, 4, 10):
    ...     print wr.word_date, wr.word_count
    2008-04-10 2
    2008-04-09 8
    2008-04-08 5
    2008-04-07 4
    2008-04-03 5

wordofday
=========

``dailysum(year=None, month=None, day=None, endyear=None, endmonth=None, endday=None, maxrows=1)``

wordofday returns a list of records representing the most commonly used words
on a given day.

Using ``wordofday`` to get the top 5 words for April 3rd, 2008:

    >>> for w in capitolwords.wordofday(2008, 4, 3, maxrows=5):
    ...     print w.word, w.word_count
    housing 1285
    director 973
    enterprise 843
    mortgage 773
    loan 665

Using ``wordofday`` to get the top words for every day in May 2008:

    >>> for w in capitolwords.wordofday(2008, 5):
    ...     print w.word, w.word_count, w.word_date
    conrad 3 2008-05-29
    webb 3 2008-05-27
    name 146 2008-05-23
    defense 2122 2008-05-22
    tax 510 2008-05-21
    johnson 37 2008-05-20
    assistance 625 2008-05-19
    food 40 2008-05-16
    iraq 521 2008-05-15
    farm 386 2008-05-14
    food 1338 2008-05-13
    oil 546 2008-05-12
    housing 1207 2008-05-08
    research 271 2008-05-07
    insurance 495 2008-05-06
    school 83 2008-05-05
    housing 81 2008-05-02
    health 346 2008-05-01
    
Using ``wordofday`` to get the word of day across a given range:

    >>> for w in capitolwords.wordofday(2008, 4, 3, 2008, 4, 10):
    ...     print w.word, w.word_count, w.word_date
    judge 214 2008-04-10
    health 366 2008-04-09
    health 237 2008-04-08
    housing 540 2008-04-07
    energy 152 2008-04-04
    housing 1285 2008-04-03

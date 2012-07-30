Fictionary
==========

Generate made-up words following the patterns used by real English words.

Using Fictionary
----------------

Fictionary doesn't have any sort of installer at the moment. If you have
python installed, just clone this repository, and run
``fictionary.py --help``. This should print out something like the
following::

    usage: fictionary.py [-h] [-v] [-c COUNT] [-m MIN]

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         Be verbose.
      -c COUNT, --count COUNT
                            The number of words to generate.
      -m MIN, --min-length MIN
                            Only generate words of MIN length or longer.

Why???
------

Why not? It is particularly good for generating memorable yet reasonable
length passwords, although I'm not sure how secure those passwords would be
given that they follow well-defined patterns. One day I might sit down and
work it out.

What Should I Expect To See
---------------------------

The results are random, but you should see something like the following::

    $ fictionary.py -c 20 -m 5
    prodybating
    awbalemisfrewhic
    billars
    rotous
    fratorgater
    incens
    cradpantle
    gatinspon
    intneshemblary
    clumake
    pladrachoppedally
    sours
    fuledi
    pheable
    frilita
    sederels
    hippostaligarupyrrelised
    haridisuppechooge
    turefurnic
    butermel
    
You'll notice that 'sours' is an actual word -- this is likely when using the
rules of English to generate words! One day, fictionary will check results
against its word list and reject any that match, but I haven't done this yet.
                            
How it Works
------------

The first time it runs, fictionary loads a word database into a data structure
called a Markov chain, which represents the patterns of letters found in the
words (e.g. The most common first-letter is 's'. The most common letter
following 's' at the start of a word is 't' etc.)

Once fictionary understands the patterns of letters used in words in the
English language, it can use these rules to generate new, nonsense words that
look like English words, but (probably) aren't.

To Do
-----

The following is my to-do list for this project:

Max Length
    Reject words over a certain threshold.
Existing Words
    Reject words that are real.
Language Choice
    Currently, fictionary conforms to the rules of British English. I'm going
    to add American English.
Word Generation Rollback
    Rejecting words that are too long or short is reasonably expensive. I may
    refactor this to rollback and remake choices until a valid 'word' is
    reached. Or I may find something better to do with my time.
Better Code
    The code was written in my lunch hour. It's not awful, but it could be
    better, and better commented.
Packaging
    I need to write a setup.py and possibly a standalone installer. Mainly
    for my own benefit -- I don't really expect anyone to be interested
    in this.
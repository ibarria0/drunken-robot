Drunken-robot (Reddit Comment Analyzer)
=======================================

For now it only counts recurring words and urls.

Possible expansion is to do lex/mood analysis.


Features
-------------------------------------
* Stopword filtering with nltk.corpora




Example
-------------------------------------


    python drunken-robot.py ubuntu 50
    ############################################
    Bot status
    Total Words: 1714
    Total Comments: 50
    Total Urls: 2
    ############################################
    like 22
    linux 21
    people 18
    use 16
    ...
    ...
    ...
    years 2
    http://www.gnu.org/philosophy/nonfree-games.html 1
    https://en.wikipedia.org/wiki/fluxbox). 1

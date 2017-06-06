# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 22:55:34 2017

@author: Guiyang
"""

import media,fresh_tomatoes

## Construction of a list of movies.

# placeholder for the list of movies.
movies =[]
# append movies one-by-one
movies.append(media.Movie('The Transporter', \
                                 'https://upload.wikimedia.org/wikipedia/en/6/68/Transporterposter.jpg',\
                                 'https://www.youtube.com/watch?v=0poXFSvX0_4'))

movies.append(media.Movie('War',\
                                 'https://upload.wikimedia.org/wikipedia/en/f/ff/Warposter.jpg',\
                                 'ttps://www.youtube.com/watch?v=eKqbjcR_YD8'))

movies.append(media.Movie('The Bank Job', \
                                 'https://upload.wikimedia.org/wikipedia/en/6/66/Bank_job_ver2.jpg',\
                                 'https://www.youtube.com/watch?v=twnd6onh5ec'))

movies.append(media.Movie('Death Race',\
                                     'https://upload.wikimedia.org/wikipedia/en/d/d2/Death_race_poster.jpg',\
                                     'https://www.youtube.com/watch?v=C8bxcJZrus0'))

movies.append(media.Movie('High Voltage', \
                          'https://upload.wikimedia.org/wikipedia/en/9/93/Crank_two_ver2.jpg',\
                          'https://www.youtube.com/watch?v=t2koYVqwzT4'))

movies.append(media.Movie('Parker',\
                                  'https://upload.wikimedia.org/wikipedia/en/f/fd/Killer_Elite_Poster.jpg',\
                                  'https://www.youtube.com/watch?v=_-Z6gp1_1aI'))


## Call the function to construct a html page with the list of movies.
fresh_tomatoes.open_movies_page(movies)

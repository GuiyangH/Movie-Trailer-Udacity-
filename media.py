# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 22:55:34 2017

@author: Guiyang
"""
class Movie(object):
    def __init__(self, title, pics, trailer):
        self.title = title
        self.poster_image_url = pics
        self.trailer_youtube_url = trailer
    def show_detail(self):
        print self.title
        print self.poster_image_url
        
        
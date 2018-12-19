"""
module for redflags in models
"""

from flask import Flask, jsonify

class Redflags:
    """ class handling the redflags model """

    redflag_list = []

    def __init__(self, *args):
        self.createdOn = args[0]
        self.createdBy = args[1]
        self.type = args[2]
        self.location = args[3]
        self.status = args[4]
        self.Images = args[5]
        self.Videos = args[6]
        self.comment = args[7]

    @classmethod
    def len_of_redflag_dict(cls):
        """ class method that returns the length of redflag_list with increment """
        return len(cls.redflag_list) + 1

    @classmethod
    def create_redflag(cls, redflag):
        """ class method to create a new redflag """
        cls.redflag_list.append(redflag)
        return cls.redflag_list
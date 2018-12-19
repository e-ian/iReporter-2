"""
module for redflags in models
"""

from flask import Flask, jsonify

class Redflags:
    """ class handling the redflags model """

    redflag_list = []

    def __init__(self, createdOn, createdBy, incidenttype, location, status, Images, Videos, comment):
        self.createdOn = createdOn
        self.createdBy = createdBy
        self.incidenttype = incidenttype
        self.location = location
        self.status = status
        self.Images = Images
        self.Videos = Videos
        self.comment = comment

    @classmethod
    def len_of_redflag_dict(cls):
        """ class method that returns the length of redflag_list with increment """
        return len(cls.redflag_list) + 1

    @classmethod
    def create_redflag(cls, redflag):
        """ class method to create a new redflag """
        cls.redflag_list.append(redflag)
        return cls.redflag_list

    @classmethod
    def get_all_redflags(cls):
        """ class method that returns all redflag records """
        return cls.redflag_list

    @classmethod
    def get_specific_redflag(cls, flagid):
        """ class method that returns a specific redflag """
        redflag = [redflag for redflag in cls.redflag_list if redflag['flagid']==flagid]
        if redflag:
            return redflag[0]
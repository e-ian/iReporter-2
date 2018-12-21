"""
module for redflags in models
"""

from flask import Flask, jsonify

class Redflags:
    """ class handling the redflags model """

    redflag_list = []

    def __init__(self, **kwargs):
        self.createdOn = kwargs['createdOn']
        self.createdBy = kwargs['createdBy']
        self.incidenttype = kwargs['incidenttype']
        self.location = kwargs['location']
        self.status = kwargs['status']
        self.Images = kwargs['Images']
        self.comment = kwargs['comment']

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
    def get_single_redflag(cls, flagid):
        """ class method that returns a specific redflag """
        redflag = [redflag for redflag in cls.redflag_list if redflag['flagid']==flagid]
        if redflag:
            return redflag[0]

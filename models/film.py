# -*- coding: utf-8 -*-
from pkg_resources import PathMetadata
from setuptools import Require
from odoo import models, fields


class film(models.Model):
    
    _name = 'film.film'
    _description = 'Films'

    name = fields.Char('Title', required=True)
    category_ids = fields.Many2many('films.category', string='Category')
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Post Creator')
    director = fields.Char(string="Director")
    protagonista=fields.Char(string='Main Character')
  
    renter_name = fields.Char(string='Renter Name', required=True,  track_visibility="always")
   
    renter_age = fields.Integer(String=" Renter Age")
    fav=fields.Char("Fav")
    image_id=fields.Char("Movie Cover")
    image_id = fields.Binary()

    state = fields.Selection(
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('Not rented', 'Not Rented'),
         ('rented','Rented')],
        'State', default="draft")
# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class cultfilms(models.Model):
    _name = 'cult.films'
    _description = 'Cult Films'


    name=fields.Char(string='Name',required=True)
    category = fields.Many2many('films.category', string='Category')
    plot=fields.Char(string='Plot')
    ideology=fields.Char(string='Ideology')

    
  
   

   
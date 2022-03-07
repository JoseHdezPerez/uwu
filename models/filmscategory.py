# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class filmscategory(models.Model):
    _name = 'films.category'
    _description = 'Films Category'


    _parent_store = True
    _parent_name = "parent_id" 


    name = fields.Char(string='Category')
    genre=fields.Char(string='Genre')
    rating_system=fields.Char(string='Rating_System')
    parent_id = fields.Many2one(
        'films.category',
        string='Parent Category',
        ondelete='restrict',
        index=True
    )
    child_ids = fields.One2many(
        'films.category', 'parent_id',
        string='Child Categories')
    parent_path = fields.Char(index=True)

    films_ids = fields.Many2many(
        'film.film',
        string='Category_ids',
        
        )

        
    cult_films_ids = fields.Many2many(
        'cult.films',
        string='category',
        
        )

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error! You cannot create recursive categories.')
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class persona(models.Model):
    _name = 'reciclaje.persona'
    _description = 'reciclaje.persona'

    nombre = fields.Char()
    apellidos = fields.Char()
    correo = fields.Char()
    materiales = fields.One2many("reciclaje.material", "persona")

class material(models.Model):
    _name = 'reciclaje.material'
    _description = 'reciclaje.material'

    tipo = fields.Char()
    cantidad = fields.Integer()
    descripcion = fields.Text()
    imagen = fields.Image (
        string='Imagen',
        help='Tamaño máximo: 512x512',
        max_width=512,
        max_height=512,
    )
    persona = fields.Many2one("reciclaje.persona")
    empresa = fields.Many2one("reciclaje.empresa")

class empresa(models.Model):
    _name = 'reciclaje.empresa'
    _description = 'reciclaje.empresa'

    nombre = fields.Char()
    direccion = fields.Char()
    telefono = fields.Char()
    materiales = fields.One2many("reciclaje.material", "empresa")

#class reciclaje(models.Model):
#    _name = 'reciclaje.reciclaje'
#    _description = 'reciclaje.reciclaje'
#
#    name = fields.Char()
#    value = fields.Integer()
#    value2 = fields.Float(compute="_value_pc", store=True)
#    description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

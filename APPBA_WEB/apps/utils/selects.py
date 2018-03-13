#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Selects(object):

    # Selector de nacionalidad.
    def nationality(self):
        return (
            ('', 'Nacionalidad'),
            ('v', 'V'),
            ('e', 'E'),
        )
    # selector de generos
    def gender(self):
        return (
            ('', 'Genero'),
            ('hombre', 'Masculino'),
            ('mujer', 'Femenino'),
        )

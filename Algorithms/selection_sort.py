"""
 * Copyright 2020, Departamento de sistemas y Computación,
 *  Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribución de:
 *
 * Dario Correal
 *
 """

from Algorithms import config as cf

from Algorithms import default_sort_criteria as dsc
assert cf
from DataStructures.List import array_list as arlt
from DataStructures.List import single_linked_list as slt


"""
  Los algoritmos de este libro están basados en la implementación
  propuesta por R.Sedgewick y Kevin Wayne en su libro
  Algorithms, 4th Edition
"""


def sort(lt, sort_criteria: callable)->dict:
    if lt["type"] == "ARRAY_LIST":
        lst = arlt
    elif lt["type"] == "LINKED_LIST":
        lst = slt
    size = lt.size(lst)
    pos1 = 0
    while pos1 < size:
        minimum = pos1    # minimun tiene el menor elemento
        pos2 = pos1 + 1
        sort_criteria = dsc.default_sort_criteria
        while (pos2 <= size):
            if (sort_criteria(lt.get_element(lst, pos2),
               (lt.get_element(lst, minimum)))):
                minimum = pos2  # minimum = posición elemento más pequeño
            pos2 += 1
        lt.exchange(lst, pos1, minimum)  # elemento más pequeño -> elem pos1
        pos1 += 1
    return lst

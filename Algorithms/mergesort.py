"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
from DataStructures.List import array_list as lst
#from DataStructures.List import single_linked_list
from typing import Callable


def sort(lt: dict, sort_crit: Callable) -> dict:
    size = lst.size(lt)
    if size > 1:
        mid = (size // 2)
        _left_lt = lst.sub_list(lt, 0, mid)
        _right_lt = lst.sub_list(lt, mid + 1, size - 1)
        sort(_left_lt, sort_crit)
        sort(_right_lt, sort_crit)
        i = j = k = 0

        _n_left = lst.size(_left_lt)
        _n_right = lst.size(_right_lt)

        while (i < _n_left) and (j < _n_right):
            elemi = lst.get_element(_left_lt, i)
            elemj = lst.get_element(_right_lt, j)
            if sort_crit(elemj, elemi):
                lst.update(lt, k, elemj)
                j += 1
            else:
                lst.update(lt, k, elemi)
                i += 1
            k += 1

        while i < _n_left:
            lst.update(lt, k, lst.get_element(_left_lt, i))
            i += 1
            k += 1

        while j < _n_right:
            lst.update(lt, k, lst.get_element(_right_lt, j))
            j += 1
            k += 1
    return lt





#===============================================================================
# Copyright (C) 2014 Anton Vorobyov
#
# This file is part of Phobos.
#
# Phobos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Phobos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Phobos. If not, see <http://www.gnu.org/licenses/>.
#===============================================================================


from abc import ABCMeta, abstractmethod


class AbstractMiner(object):
    """
    Abstract class, which defines interface to all data miners
    used in Phobos.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def tablename_iter(self):
        """
        Provide an iterator over tables provided by miner.
        """
        pass

    @abstractmethod
    def get_table(self, table_name):
        """
        Fetch data from specified table as list of objects.
        """
        pass

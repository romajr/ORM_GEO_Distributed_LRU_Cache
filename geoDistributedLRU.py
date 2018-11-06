#!/usr/bin/env python
# -*- coding: utf-8
"""
##################### Q3 Question C - ORMUCO ####################
#-------------------------- Luiz Roma --------------------------#
#
# This code implements a network handling using a cache manager
#
# QUESTION ENUMERATION
# The goal is to write a new library that can be integrated to
# the Ormuco stack. Dealing with network issues everyday, latency
# is our biggest problem. Thus, the challenge is to write a new
# Geo Distributed LRU (Least Recently Used) cache with time
# expiration. This library will be used extensively by many of our
# services so it needs to meet the following criteria:
# 1 - Simplicity. Integration needs to be dead simple.
# 2 - Resilient to network failures or crashes.
# 3 - Near real time replication of data across Geolocation.
# Writes need to be in real time.
# 4 - Data consistency across regions
# 5 - Locality of reference, data should almost always be available
# from the closest region
# 6 - Flexible Schema
# 7 - Cache can expire
#
#---------------------------------------------------------------#
#################################################################
"""

import sys
from collections import OrderedDict
from collections import Mapping

class _cachenode(object):
    def __init__(self):
        self.empty = True
    """
    CACHE NODE INSTANCE creation
    this creates an empty node
    :param empy: flag identifying node is empy or not
    """

class GeoDistributedLRUCacheRecorder(object):
    """
    CLASS FOR RECORDING CACHE
    this stablishes the pattern to save, consume and update
    cache accordingly, individually as an object, receiving
    information from outside
    """

    def __init__(self, max_size, callback = None):
        self.table = {} # OrderedDict or Mapping
        self.cache_train = _cachenode()
        self.cache_current_size = 1
        self.cache_size = max_size
        self.timer = 5
        """
        INITIALIZING THE CACHE INSTANCE
        this is builds the main structure of the class
        :param table: ordered list referencing the cache nodes
        :param cache_train: cache 'train' is the variable where we will manage all the 'cars'
        available, ordering them by usage (recently used)
        :param cache_current_size: saves the current size of the cache, will be compared to
        'cache_size' (which is the max size allowed)
        :param cache_size: local maximum size allowed for the cache
        :param timer: cache expiration set time, for expiration reference
        """

    def _new_node(self):
        self.cache_train = _cachenode()
        self.cache_train.next = self.cache_train
        self.cache_train.prev = self.cache_train
        """
        CREATE NEW NODE, EMPTY CAR IN THE TRAIN
        this is builds an empty node and links it to the train of nodes
        :param cache_train: cache 'train' is the variable where we will manage all the 'cars'
        available, ordering them by usage (recently used)
        """

    def _len_cache(self):
        return len(self.table)
        """
        MESURES THE SIZE OF THE CACHE (NUMBER OF NODES)
        this method returns the current size of the cache table
        :param table: ordered list referencing the cache nodes
        :return: the size of the table
        """

    def _get_value(self, key):
        node = self.table[key]
        self._update_LRU(node)

        return node.value
        """
        GET THE VALUE FROM THE NODE
        :param table: ordered list referencing the cache nodes
        :param node: node to be checked
        :return: the value of the node in the position 'key'
        """

    def _update_LRU(self, node):
        """
        updates the order of the 'cars' in the train so the Least Recently Used
        goes to the 1st car place in the train
        """

        # TODO
        # update cars position within the train

        self.cache_train = node

    def _new_car_node(self, node):
        """
        add new value to the cache list
        """

        # TODO
        # add new value to the cache node

        self.cache_current_size += 1
        self._update_LRU(node)

    def _set_value(self, key, value):
        if key in self.table:
            node = self.table[key]
            node.value = value
            self.(_update_LRU(node))
        elif self.cache_current_size < self.cache_size:
            self._new_car_node(node)
        elif self.cache_current_size = self.cache_size:
            self._watchdog_TTL_update(self.timer)
            self._new_car_node(node)

    def _unlink_value(self, node):
        """
        add new value to the cache list
        """

        # TODO
        # delete value from the cache node


        self.cache_current_size -= 1
        self._update_LRU(node)

    def _clear_based_on_time(self):
        # TODO
        # see all cache nodes and values and delete the oldest ones
        # count how many nodes were delete

    def _watchdog_TTL_update(self):
        """
        expire old items accordingly
        """

        self._clear_based_on_time():

        self.cache_current_size = self.cache_current_size - nodes_expired
        if(self.cache_current_size < = ):
            self.cache_current_size = 0
        self._unlink_value(node)

        return 1

class NetworkWatchDog(object):
    """
    this will verify network availability according to GEOCachesInstances availability
    the main purpose of this block will be check the network around the local point,
    verify stability, verify connectivity, availability, verify latency,
    stablishing communication with backup plan, disaster recovery and redundance
    so when the object GEOCachesInstances consumes it, it will know what is the
    healthy of the network for the nearest nodes and work to save/consume/update/delete
    cache accordingly to the needs
    """

class GEOCachesInstances(object):
    """
    this block will get the current local consuming point and it will calculate
    the instances nearest to my location, showing a list of prior network points
    most recommended to connect and receive their 'healthy' status from NetworkWatchDog
    object, creating a priorization list for saving/consuming/updating/deleting cache
    """

class ManageWriteThroughCache(object):
    """
    this will receive from GEOCachesInstances a priorization list of what are the
    most recommended networks/places to save/consume/update/delete cache,
    sync the top priorities in a 1st moment and send the other locations to a queue
    that queue is based on 2 main filter ideas:
    - most recommended networks for getting the information by distance (are they
    near to my current position or not?)
    - most probable networks will request that kind of information in cache
    """

class SyncAllNetworkPoints(object):
    """
    this will guarantee that all caches are well sync according to a priorization list 1st
    this priorization list will take in consideration:
    - nearest locations for spreading/sharing cache information
    - most probable needed database content requests for cache update, it means, if that
    cache has a high probability in being consumed by X database in Y location, we will
    sync it in 1st place than the others
    """

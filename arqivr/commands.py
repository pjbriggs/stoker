#!/usr/bin/env python
#
#     index.py: indexing classes and functions
#     Copyright (C) University of Manchester 2018 Peter Briggs
#

import index

def _print_list(l):
    """
    """
    for i in l:
        print "\t%s" % i

def compare(source,target):
    """
    """
    source = index.ObjectIndex(source).build()
    target = index.ObjectIndex(target).build()
    diff = index.compare(source,target)
    print "%d missing objects" % len(diff.missing)
    _print_list(diff.missing)
    print "%d additional objects" % len(diff.extra)
    _print_list(diff.extra)
    print "%d uncheckable objects" % len(diff.uncheckable)
    _print_list(diff.uncheckable)
    print "%d objects changed type" % len(diff.changed_type)
    _print_list(diff.changed_type)
    print "%d objects changed size" % len(diff.changed_size)
    _print_list(diff.changed_size)
    print "%d objects changed link" % len(diff.changed_link)
    _print_list(diff.changed_link)
    print "%d objects changed time" % len(diff.changed_time)
    _print_list(diff.changed_time)

def check_accessibility(dirn):
    """
    """
    indx = index.ObjectIndex(dirn).build()
    objs = index.check_accessibility(indx)
    print "%d inaccessible objects" % len(objs)
    for obj in objs:
        print "\t%s" % obj


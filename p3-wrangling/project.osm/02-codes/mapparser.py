#!/usr/bin/env python

import xml.etree.ElementTree as ET
import pprint

def count_tags(filename):
    """count tags in filename.
    
    Init 1 in dict if the key not exist, increment otherwise."""
    tags = {}
    for ev,elem in ET.iterparse(filename):
        tag = elem.tag
        if tag not in tags.keys():
            tags[tag] = 1
        else:
            tags[tag]+=1
    return tags

def test():

    tags = count_tags(OSM_FILE)
    pprint.pprint(tags)
#     assert tags == {'bounds': 1,
#                      'member': 3,
#                      'nd': 4,
#                      'node': 20,
#                      'osm': 1,
#                      'relation': 1,
#                      'tag': 7,
#                      'way': 1}

    

if __name__ == "__main__":
    test()
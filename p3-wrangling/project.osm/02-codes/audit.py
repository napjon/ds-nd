
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
from optparse import OptionParser

# OSMFILE = "sample.osm"
# OSMFILE = "example_audit.osm"
#In Indonesia, type first, then name. So the regex has to be changed.
#street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
street_type_re = re.compile(r'^\b\S+\.?', re.IGNORECASE)


# expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
#             "Trail", "Parkway", "Commons"]
expected = ['Jalan', 'Gang','Street', 'Road']
# UPDATE THIS VARIABLE
#Mapping has to sort in length descending.
#languange English-Indonesian{Street: Jalan}. 
#{Sudirman Stret:Jalan Sudirman}
mapping = {

            'jl.':'Jalan',
            'JL.':'Jalan',
            'Jl.':'Jalan',
            'GG':'Gang',
            'gg': 'Gang',
            'jl' :'Jalan',
            'JL':'Jalan',
            'Jl':'Jalan',
        
        }
# mapping = { 
#             "Ave":"Avenue",
#             "St.": "Street",
#             "Rd." : "Road",
#             "N.":"North",
#             "St" : "Street",
#             }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
            #return True if need to be updated
            return True
    return False


def is_street_name(elem):
    """
    Perhaps the addr:full should also included to be fixed  
    """
    return (elem.attrib['k'] == "addr:street") or (elem.attrib['k'] == "addr:full")

def is_name_is_street(elem):
    """Some people fill the name of the street in k=name.
    
    Should change this"""
    s = street_type_re.search(elem.attrib['v'])
    #print s
    return (elem.attrib['k'] == "name") and s and s.group() in mapping.keys()

def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
#     tree = ET.parse(osm_file, events=("start",))
    tree = ET.parse(osm_file)
    
    listtree = list(tree.iter())
    for elem in listtree:
        if elem.tag == "node" or elem.tag == "way":
            n_add = None
            
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    if audit_street_type(street_types, tag.attrib['v']):
                        #Update the tag attribtue
                        tag.attrib['v'] = update_name(tag.attrib['v'],mapping)
                elif is_name_is_street(tag):
                    tag.attrib['v'] = update_name(tag.attrib['v'],mapping)
                    n_add = tag.attrib['v']
                   
            if n_add:
                elem.append(ET.Element('tag',{'k':'addr:street', 'v':n_add}))

            
                
    #write the to the file we've been audit
    tree.write(osmfile[:osmfile.find('.osm')]+'_audit.osm')
    return street_types


def update_name(name, mapping):
    """
    Fixed abreviate name so the name can be uniform.
    
    The reason why mapping in such particular order, is to prevent the shorter keys get first.
    """
    dict_map = sorted(mapping.keys(), key=len, reverse=True)
    for key in dict_map:
        
        if name.find(key) != -1:          
            name = name.replace(key,mapping[key])
            return name

#essentially, in Indonesia, you specify the all type of street as Street. 
#So if it doesnt have any prefix, add 'Jalan'
    return 'Jalan ' + name


def test():
    st_types = audit(OSMFILE)
    pprint.pprint(dict(st_types))
    #assert len(st_types) == 3
    

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name


if __name__ == '__main__':
#     test()
    parser  = OptionParser()
    parser.add_option('-d', '--data', dest='audited_data', help='osm data that want to be audited')
    (opts,args) = parser.parse_args()
    audit(opts.audited_data)
    
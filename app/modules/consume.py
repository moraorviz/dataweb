# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import json
from collections import namedtuple

from SPARQLWrapper import SPARQLWrapper, JSON


endpoint_url = "https://query.wikidata.org/sparql"

query_k2191 = '''
SELECT ?cuerpo ?cuerpoLabel ?tipoLabel ?simbadID WHERE {
  ?cuerpo ?label "K2-191"@en .
  ?cuerpo wdt:P31 wd:Q523 .
  ?cuerpo wdt:P31 ?tipo .
  ?cuerpo wdt:P3083 ?simbadID
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}'''

query_k2191b = '''
SELECT ?cuerpo ?cuerpoLabel ?tipoLabel ?timeodLabel ?discoveryLabel WHERE {
  ?cuerpo ?label "K2-191 b"@en .
  ?cuerpo wdt:P31 wd:Q44559 .
  ?cuerpo wdt:P31 ?tipo .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
  ?cuerpo wdt:P575 ?timeod .
  ?cuerpo wdt:P1046 ?discovery
}'''

query_hd202696 = '''
SELECT ?cuerpo ?cuerpoLabel ?tipoLabel ?simbadID WHERE {
  ?cuerpo ?label "HD 202696"@en .
  ?cuerpo wdt:P31 wd:Q523 .
  ?cuerpo wdt:P31 ?tipo .
  ?cuerpo wdt:P3083 ?simbadID
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}'''

query_hd202696b = '''
SELECT ?cuerpo ?cuerpoLabel ?tipoLabel ?timeodLabel ?discoveryLabel WHERE {
  ?cuerpo ?label "HD 202696 b"@en .
  ?cuerpo wdt:P31 wd:Q44559 .
  ?cuerpo wdt:P31 ?tipo .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
  ?cuerpo wdt:P575 ?timeod .
  ?cuerpo wdt:P1046 ?discovery
}'''

query_hd202696c = '''
SELECT ?cuerpo ?cuerpoLabel ?tipoLabel ?timeodLabel ?discoveryLabel WHERE {
  ?cuerpo ?label "HD 202696 c"@en .
  ?cuerpo wdt:P31 wd:Q44559 .
  ?cuerpo wdt:P31 ?tipo .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
  ?cuerpo wdt:P575 ?timeod .
  ?cuerpo wdt:P1046 ?discovery
}'''

query_gj4276b = '''
SELECT ?cuerpo ?cuerpoLabel ?tipoLabel ?timeodLabel ?discoveryLabel WHERE {
  ?cuerpo ?label "GJ 4276 b"@en .
  ?cuerpo wdt:P31 wd:Q44559 .
  ?cuerpo wdt:P31 ?tipo .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
  ?cuerpo wdt:P575 ?timeod .
  ?cuerpo wdt:P1046 ?discovery
}'''


queries_lst = [query_k2191, query_k2191b,
               query_hd202696, query_hd202696b, query_hd202696c, query_gj4276b]


def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    return sparql.query().convert()


def query_all(queries_lst):
    outlist = []
    for query in queries_lst:
        results = get_results(endpoint_url, query)
        outlist.append(results)

    return outlist


def parseobjects(olist):
    outputlist = []
    for o in olist:
        o = o['results']['bindings'][0]
        p = Payload(json.dumps(o))
        outputlist.append(p)

    return outputlist


class Payload(object):
    '''Class to deseiarlize the response into an object.'''

    def __init__(self, j):
        self.__dict__ = json.loads(j)

    def get_attributes(self):
        outlist = []
        for key in self.__dict__.keys():
            outlist.append(key)

        return outlist


def getobjects():
    olist = query_all(queries_lst)
    plist = parseobjects(olist)

    return plist

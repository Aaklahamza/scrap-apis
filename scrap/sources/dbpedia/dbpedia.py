
from SPARQLWrapper import SPARQLWrapper, JSON

class Dbpedia:
    
    def __init__(self):
        self.sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        self.sparql.setReturnFormat(JSON)
    
    def format_row(self, row):
        d = {}
        
        for k in row:
            for kk in row[k] :
                d[k+'_'+kk] = row[k][kk]

        dd = {}
        dd['child_uri'] = d['o_value']
        dd['lang'] = d['label_xml:lang']
        dd['child'] = d['label_value']
        return dd

    
    def build_query(self, term, limit, lang):
        query = """
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        SELECT DISTINCT *
        WHERE {
            {
              ?o dbo:wikiPageRedirects|dct:Subject|rdfs:seeAlso dbr:%s .
              ?o rdfs:label ?label .
            }
            UNION
            {
              ?o ^dbo:wikiPageRedirects|dct:Subject|rdfs:seeAlso dbr:%s .
              ?o rdfs:label ?label .
            }
            FILTER ( langMatches(lang(?label),"%s") )
        }
        LIMIT %s
        """ % ( term, term, lang, str(limit) )
        return query
    
    def get_related(self, 
                  term,
                  limit=100, 
                  lang="en"):

        
        query = self.build_query( term, limit, lang)
        
        self.sparql.setQuery(query)
        results = self.sparql.query().convert()
        resp = results['results']['bindings']
        
        res = list(map( self.format_row, resp ))
        
        return list(map( lambda x: {**x, **{'query': term}}, res))


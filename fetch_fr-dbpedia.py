from SPARQLWrapper import SPARQLWrapper, CSV

sparql = SPARQLWrapper("http://fr.dbpedia.org/sparql")
sparql.setQuery(
    """
select *
where 
{
	?location rdfs:label ?name ;
		dbpedia-owl:peopleName ?peopleName ;
		prop-fr:gentilé ?gentile ;
		dbpedia-owl:country dbpedia-fr:France ; 
		dbpedia-owl:inseeCode ?inseeCode.

FILTER ( LANG ( ?name ) = 'fr' )
FILTER ( LANG ( ?peopleName ) = 'fr' )
FILTER ( LANG ( ?gentile ) = 'fr' )
}

"""
)
sparql.setReturnFormat(CSV)
results = sparql.query().convert()

f = open("demonyms-fr.csv", "w")
f.write(results.decode("utf-8", "ignore"))

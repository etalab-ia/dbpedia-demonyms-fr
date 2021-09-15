from SPARQLWrapper import SPARQLWrapper, CSV

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery(
    """
select *
where {
?location rdfs:label ?name ;
		dbo:country dbr:France ;
		dbp:demonym ?demonym.

OPTIONAL {
		?location dbp:insee ?inseeCode
}

FILTER ( LANG ( ?name ) = 'fr' )
}

"""
)
sparql.setReturnFormat(CSV)
results = sparql.query().convert()

f = open("demonyms-alt-fr.csv", "w")
f.write(results.decode("utf-8", "ignore"))

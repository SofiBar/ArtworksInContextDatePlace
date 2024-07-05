import sys
import os



from functions import sparql_query_setting 

db_endpoint = "https://dbpedia.org/sparql" 



qmdb1 = '''
prefix dbo: <http://dbpedia.org/ontology/>
prefix dcterms: <http://purl.org/dc/terms/>
prefix dbp: <http://dbpedia.org/property/>
SELECT distinct ?artwork ?subject WHERE {
?artwork a dbo:Artwork;
dbp:subject ?subject .
}ORDER BY RAND()
LIMIT 50'''




def q_db_tot(): 
    "Count of artworks in Dbpedia"
    q = """ 

    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>


    SELECT (count (distinct ?artwork) as ?tot) WHERE {

    ?artwork a dbo:Artwork .
    }

    """
    res = sparql_query_setting(q, db_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_db_date(): 

    q = """ 

    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
    select distinct ?art ?date where {
    
    ?art a dbo:Artwork; 
        dbp:completionDate ?date.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, db_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        date = result["date"]["value"]
        result_list.append([art, date])
    return result_list

def q_db_date_tot():
    q= """ 
    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
    select distinct  (count (distinct ?art) as ?tot) where {
    
    
    ?art a dbo:Artwork; 
        dbp:completionDate ?date.
} 

"""
    res = sparql_query_setting(q, db_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_db_place():
    q = """ 
    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
    select distinct  ?art ?site where {
    
    ?art a dbo:Artwork; 
        dbp:releaseLocation ?date.

    } LIMIT 100
    
    """
    res = sparql_query_setting(q, db_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        loc = result["site"]["value"]
        result_list.append([art, loc])
    return result_list


def q_db_place_tot():
    q= """ 
    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
    select distinct  (count (distinct ?art) as ?tot) where {
    
    
    ?art a dbo:Artwork; 
        dbp:releaseLocation ?date.


} 

"""
    res = sparql_query_setting(q, db_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)
    

def q_db_date_place():
    q = """ 

    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
    select distinct  ?art ?date ?site where {
    
    
    ?art a dbo:Artwork; 
        dbp:releaseLocation ?date;
        dbp:completionDate ?date.


} LIMIT 100


"""
    res = sparql_query_setting(q, db_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        loc = result["site"]["value"]
        date = result["date"]["value"]
        result_list.append([art, loc, date])
    return result_list

def q_db_date_place_tot():
    q = """ 

    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
    select (count (distinct ?art) as ?tot) where {
    
    

    ?art a dbo:Artwork; 
        dbp:releaseLocation ?date;
        dbp:completionDate ?date.


} 


"""

    res = sparql_query_setting(q, db_endpoint)
    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



#----------- Contextual information: AUTHOR ----------------#

def q_db_author(): 

    q = """ 

    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
    select distinct ?art ?author where {
    
    ?art a dbo:Artwork; 
    dbp:author | dbp:artist ?author.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, db_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        result_list.append([art, author])
    return result_list


def q_db_author_tot(): 
    "Count of artworks having an author specified"
    q = """ 

    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
    select (count(distinct ?art) as ?tot) where {
    
    ?art a dbo:Artwork; 
    dbp:author | dbp:artist ?author.
    } 

    """
    res = sparql_query_setting(q, db_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_db_author_date(): 

    q = """ 

   prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
    select distinct ?art ?author ?date where {
    
    ?art a dbo:Artwork; 
        dbp:author | dbp:artist ?author.
    ?author dbp:birthYear | dbp:deathYear ?date.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, db_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        date = result["date"]["value"]
        result_list.append([art, author, date])
    return result_list


def q_db_author_date_tot(): 
    "Count of artworks having an author specified"
    q = """ 

    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>


    select (count(distinct ?art) as ?tot) where {
    
    ?art a dbo:Artwork; 
        dbp:author | dbp:artist ?author.
    ?author dbp:birthYear | dbp:deathYear ?date.
    } 

    """
    res = sparql_query_setting(q, db_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)




def q_db_author_place(): 

    q = """ 

    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
    select distinct ?art ?author ?place where {
    
    ?art a dbo:Artwork; 
    dbp:author | dbp:artist ?author.
    ?author  dbp:livingPlace | dbp:placeOfBurial | dbp:residence | dbp:restingPlace  ?date.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, db_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        place = result["place"]["value"]
        result_list.append([art, author, place])
    return result_list


def q_db_author_place_tot(): 
    "Count of artworks having an author specified"
    q = """ 

    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
    select (count(distinct ?art) as ?tot) where {
    
    ?art a dbo:Artwork; 
    dbp:author | dbp:artist ?author.
    ?author  dbp:livingPlace | dbp:placeOfBurial | dbp:residence | dbp:restingPlace  ?date.
    } 

    """
    res = sparql_query_setting(q, db_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_db_author_wikidata(): 

    q = """ 

    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
    select distinct ?author ?wikidata where {
    
    ?art a dbo:Artwork; 
        dbp:author | dbp:artist ?author.
    ?author owl:sameAs ?aligned. 

    FILTER(regex(str(?aligned), "wikidata", "i"))
  
} LIMIT 100

    """
    res = sparql_query_setting(q, db_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        author = result["author"]["value"]
        wd = result["wikidata"]["value"]
        result_list.append([author, wd])
    return result_list


def q_db_author_wikidata_tot(): 
    "Count of artworks having an author aligned with Wikidata"
    q = """ 

    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>


     select (count(distinct ?art) as ?tot) where {
    
    ?art a dbo:Artwork; 
        dbp:author | dbp:artist ?author.
       
    ?author owl:sameAs ?aligned. 

    FILTER(regex(str(?aligned), "wikidata", "i"))
    } 

    """
    res = sparql_query_setting(q, db_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_db_author_ulan_tot(): 
    "Count of artworks having an author aligned with ULAN"
    q = """ 

    prefix dbo: <http://dbpedia.org/ontology/>
    prefix dcterms: <http://purl.org/dc/terms/>
    prefix dbp: <http://dbpedia.org/property/>
    
     select (count(distinct ?art) as ?tot) where {
    
    ?art a dbo:Artwork; 
        dbp:author | dbp:artist ?author.
       
    ?author owl:sameAs ?aligned.

    FILTER(regex(str(?aligned), "ulan", "i"))
    } 

    """
    res = sparql_query_setting(q, db_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)
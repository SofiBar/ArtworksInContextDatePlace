
from functions import sparql_query_setting 



eu_endpoint = "http://sparql.europeana.eu/"

def q_eu_tot(): 
    "Count of visual works in Europeana"
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    select (count (distinct ?art) as ?tot) where {
        ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s .
    #OPTIONAL {?s skos:prefLabel ?label
    #FILTER(lang(?label)='en')}
    } 
    
    """

    res = sparql_query_setting(q, eu_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_eu_date(): 

    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
        
    select distinct ?art ?date where {
    
     ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dcterms:created ?date.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, eu_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        date = result["date"]["value"]
        result_list.append([art, date])
    return result_list


def q_eu_date_tot():
    q= """ 
    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
        
    select (count (distinct ?art) as ?tot) where {
    
     ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dcterms:created ?date.
     
} 

"""
    res = sparql_query_setting(q, eu_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)




def q_eu_place():
    q = """ 

    
    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
        
    select distinct ?art ?site where {
    
     ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dcterms:spatial ?site.

    } LIMIT 100
    
    """
    res = sparql_query_setting(q, eu_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        loc = result["site"]["value"]
        result_list.append([art, loc])
    return result_list


def q_eu_place_tot():
    q= """ 
    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
        
    
    select (count (distinct ?art) as ?tot) where {
    
     ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dcterms:spatial ?site.

} 

"""
    res = sparql_query_setting(q, eu_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)
    

def q_eu_date_place():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
        
    
    select distinct ?art ?date ?site where {
    
     ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dcterms:spatial ?site; 
      dcterms:created ?date.


} LIMIT 100


"""
    res = sparql_query_setting(q, eu_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        loc = result["site"]["value"]
        date = result["date"]["value"]
        result_list.append([art, loc, date])
    return result_list

def q_eu_date_place_tot():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
        
    
    select (count (distinct ?art) as ?tot) where {
    
     ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dcterms:spatial ?site; 
      dcterms:created ?date.
} 


"""

    res = sparql_query_setting(q, eu_endpoint)
    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



# -------------------------- AUTHOR -------------------------- #



def q_eu_author():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
        
    
    select distinct ?art ?author where {
    
     ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dc:creator ?author. 


} LIMIT 100


"""
    res = sparql_query_setting(q, eu_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        auth = result["auth"]["value"]

        result_list.append([art, auth])
    return result_list



def q_eu_author_tot():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
        
    
    select (count (distinct ?art) as ?tot) where{
    
      ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dc:creator ?author. 
    } 


    """

    res = sparql_query_setting(q, eu_endpoint)
    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)




def q_eu_author_date():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaGr2: <http://rdvocab.info/ElementsGr2/>
        
    
    select distinct ?art ?author ?date where {
    
     ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dc:creator ?author. 
    ?author rdaGr2:dateOfDeath | rdaGr2:dateOfBirth ?date.



} LIMIT 100


"""
    res = sparql_query_setting(q, eu_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        date = result["date"]["value"]
        result_list.append([art, author, date])

    return result_list



def q_eu_author_date_tot():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaGr2: <http://rdvocab.info/ElementsGr2/>
        
    
    select (count (distinct ?art) as ?tot) where{
    
      ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dc:creator ?author. 
    ?author rdaGr2:dateOfDeath | rdaGr2:dateOfBirth ?date.
    } 


    """

    res = sparql_query_setting(q, eu_endpoint)
    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_eu_author_place():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaGr2: <http://rdvocab.info/ElementsGr2/>
        
    
    select distinct ?art ?author ?place where {
    
     ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dc:creator ?author. 
    ?author rdaGr2:placeOfBirth | rdaGr2:placeOfDeath ?place.



} LIMIT 100


"""
    res = sparql_query_setting(q, eu_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        date = result["place"]["value"]
        result_list.append([art, author, date])

    return result_list



def q_eu_author_place_tot():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaGr2: <http://rdvocab.info/ElementsGr2/>
        
    
    select (count (distinct ?art) as ?tot) where{
    
      ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dc:creator ?author. 
    ?author rdaGr2:placeOfBirth | rdaGr2:placeOfDeath ?place.
    } 


    """

    res = sparql_query_setting(q, eu_endpoint)
    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_eu_art_aligned_tot():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaGr2: <http://rdvocab.info/ElementsGr2/>
        
    
    select (count (distinct ?art) as ?tot) where{
    
      ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
       owl:sameAs ?a.
    
    FILTER(regex(str(?a), "wikidata", "i"))
    } 


    """

    res = sparql_query_setting(q, eu_endpoint)
    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_eu_author_wikidata():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaGr2: <http://rdvocab.info/ElementsGr2/>
        
    
    select distinct ?art ?author ?a where {
    
     ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dc:creator ?author. 
    ?author owl:sameAs ?a.
    
    FILTER(regex(str(?a), "wikidata", "i"))
    



    } LIMIT 100


    """
    res = sparql_query_setting(q, eu_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        aligned = result["a"]["value"]
        result_list.append([art, author, aligned])

    return result_list



def q_eu_author_wikidata_tot():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaGr2: <http://rdvocab.info/ElementsGr2/>
        
    
    select (count (distinct ?art) as ?tot) where{
    
      ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dc:creator ?author. 
    ?author owl:sameAs ?a.
    
    FILTER(regex(str(?a), "wikidata", "i"))
    } 


    """

    res = sparql_query_setting(q, eu_endpoint)
    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_eu_author_ulan():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaGr2: <http://rdvocab.info/ElementsGr2/>
        
    
    select distinct ?art ?author ?a where {
    
     ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dc:creator ?author. 
    ?author owl:sameAs ?a.
    
    FILTER(regex(str(?a), "ulan", "i"))
    



} LIMIT 100


"""
    res = sparql_query_setting(q, eu_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        aligned = result["a"]["value"]
        result_list.append([art, author, aligned])

    return result_list



def q_eu_author_ulan_tot():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaGr2: <http://rdvocab.info/ElementsGr2/>
        
    
    select (count (distinct ?art) as ?tot) where{
    
      ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dc:creator ?author. 
    ?author owl:sameAs ?a.
    
    FILTER(regex(str(?a), "ulan", "i"))
    } 


    """

    res = sparql_query_setting(q, eu_endpoint)
    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_eu_author_aligned_tot():
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaGr2: <http://rdvocab.info/ElementsGr2/>
        
    
    select (count (distinct ?art) as ?tot) where{
    
      ?s a skos:Concept ;
            skos:broader*  <http://vocab.getty.edu/aat/300191086>. # aat term for visual work
    ?art dc:type ?s ;
      dc:creator ?author. 
    ?author owl:sameAs ?a.
    
    FILTER((regex(str(?aligned), "ulan", "i") || regex(str(?aligned), "wikidata", "i")))
    } 


    """

    res = sparql_query_setting(q, eu_endpoint)
    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



## NOTES 
"""
http://purl.org/dc/elements/1.1/creator
http://purl.org/dc/terms/spatial # spatial characteristics of the resource - indicates other places than the current location. Not further specified. 
http://purl.org/dc/terms/provenance 
http://purl.org/dc/terms/temporal # Temporal characteristics of the resource
http://purl.org/dc/elements/1.1/date 
"""

"""definition of dcterms:spatial: Information about the spatial characteristics of the original analog or born
digital object, i.e. what the resource represents or depicts in terms of space.
This may be a named place, a location, a spatial coordinate or a named
administrative entity."""


"""
# agent info
http://rdvocab.info/ElementsGr2/dateOfDeath
http://rdvocab.info/ElementsGr2/dateOfBirth 
http://rdvocab.info/ElementsGr2/placeOfBirth


"""
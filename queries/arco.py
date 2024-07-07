import sys
import os

# Get the absolute path of the parent directory
#parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Add the parent directory to the Python path
#sys.path.append(parent_dir)

from functions import sparql_query_setting 



arco_endpoint = "https://dati.beniculturali.it/sparql"


def q_arco_tot(): 
    "Count of artworks (a-arco:HistoricOrArtisticProperty) in ArCO"
    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>

    
    select (count(distinct ?art) as ?tot) where {
    
    ?art a a-arco:HistoricOrArtisticProperty.
    } 

    """
    res = sparql_query_setting(q, arco_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_arco_date(): 

    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    
    select distinct ?art ?date where {
    
    ?art a a-arco:HistoricOrArtisticProperty;
      dc:date ?date.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, arco_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        date = result["date"]["value"]
        result_list.append([art, date])
    return result_list

def q_arco_date_tot():
    q= """ 
    PREFIX a-loc: <https://w3id.org/arco/ontology/location/>
    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX c-arco: <https://w3id.org/arco/ontology/context-description/>
    PREFIX lite: <https://w3id.org/arco/ontology/arco-lite/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cis: <http://dati.beniculturali.it/cis/>
    
    select distinct  (count (distinct ?art) as ?tot) where {
    
    
    ?art a a-arco:HistoricOrArtisticProperty;
      dc:date ?date.
} 

"""
    res = sparql_query_setting(q, arco_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_arco_place():
    q = """ 
    PREFIX a-loc: <https://w3id.org/arco/ontology/location/>
    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX c-arco: <https://w3id.org/arco/ontology/context-description/>
    PREFIX lite: <https://w3id.org/arco/ontology/arco-lite/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cis: <http://dati.beniculturali.it/cis/>
    
    select distinct  ?art ?site where {
    
    
    ?art a a-arco:HistoricOrArtisticProperty;
      a-loc:hasTimeIndexedTypedLocation ?loc. 
    ?loc a-loc:hasLocationType a-loc:ProductionRealizationLocation; 
        a-loc:atSite / cis:siteAddress ?site. 


    } LIMIT 100
    
    """
    res = sparql_query_setting(q, arco_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        loc = result["site"]["value"]
        result_list.append([art, loc])
    return result_list


def q_arco_place_tot():
    q= """ 
    PREFIX a-loc: <https://w3id.org/arco/ontology/location/>
    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX c-arco: <https://w3id.org/arco/ontology/context-description/>
    PREFIX lite: <https://w3id.org/arco/ontology/arco-lite/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cis: <http://dati.beniculturali.it/cis/>
    
    select distinct  (count (distinct ?art) as ?tot) where {
    
    
    ?art a a-arco:HistoricOrArtisticProperty;
      a-loc:hasTimeIndexedTypedLocation ?loc. 
    ?loc a-loc:hasLocationType a-loc:ProductionRealizationLocation; 
        a-loc:atSite / cis:siteAddress ?site. 


} 

"""
    res = sparql_query_setting(q, arco_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)
    

def q_arco_date_place():
    q = """ 

    PREFIX a-loc: <https://w3id.org/arco/ontology/location/>
    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX c-arco: <https://w3id.org/arco/ontology/context-description/>
    PREFIX lite: <https://w3id.org/arco/ontology/arco-lite/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cis: <http://dati.beniculturali.it/cis/>
    
    select distinct  ?art ?date ?site where {
    
    
    ?art a a-arco:HistoricOrArtisticProperty;
      dc:date ?date; 
      a-loc:hasTimeIndexedTypedLocation ?loc. 
    ?loc a-loc:hasLocationType a-loc:ProductionRealizationLocation; 
        a-loc:atSite / cis:siteAddress ?site. 


} LIMIT 100


"""
    res = sparql_query_setting(q, arco_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        loc = result["site"]["value"]
        date = result["date"]["value"]
        result_list.append([art, loc, date])
    return result_list

def q_arco_date_place_tot():
    q = """ 

    PREFIX a-loc: <https://w3id.org/arco/ontology/location/>
    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX c-arco: <https://w3id.org/arco/ontology/context-description/>
    PREFIX lite: <https://w3id.org/arco/ontology/arco-lite/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cis: <http://dati.beniculturali.it/cis/>
    
    select (count (distinct ?art) as ?tot) where {
    
    

    ?art a a-arco:HistoricOrArtisticProperty;
        dc:date ?date; 
        a-loc:hasTimeIndexedTypedLocation ?loc. 
    ?loc a-loc:hasLocationType a-loc:ProductionRealizationLocation; 
        a-loc:atSite / cis:siteAddress ?site. 


} 


"""

    res = sparql_query_setting(q, arco_endpoint)
    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



#----------- Contextual information: AUTHOR ----------------#

def q_arco_author(): 

    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    
    select distinct ?art ?author where {
    
    ?art a a-arco:HistoricOrArtisticProperty;
      dc:creator ?author.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, arco_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        result_list.append([art, author])
    return result_list


def q_arco_author_tot(): 
    "Count of artworks having an author specified"
    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    
    select (count(distinct ?art) as ?tot) where {
    
    ?art a a-arco:HistoricOrArtisticProperty;
      dc:creator ?author.
    } 

    """
    res = sparql_query_setting(q, arco_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_arco_author_date(): 

    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cpv: <https://w3id.org/italia/onto/CPV/>
    
    select distinct ?art ?author ?date where {
    
    ?art a a-arco:HistoricOrArtisticProperty;
      dc:creator ?author.
    ?author cpv:dateOfBirth | cpv:dateOfDeath ?dated.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, arco_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        date = result["date"]["value"]
        result_list.append([art, author, date])
    return result_list


def q_arco_author_date_tot(): 
    "Count of artworks having an author specified"
    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cpv: <https://w3id.org/italia/onto/CPV/>
    
    select (count(distinct ?art) as ?tot) where {
    
    ?art a a-arco:HistoricOrArtisticProperty;
      dc:creator ?author.
    ?author cpv:dateOfBirth | cpv:dateOfDeath ?dated.
    } 

    """
    res = sparql_query_setting(q, arco_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)




def q_arco_author_place(): 

    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cpv: <https://w3id.org/italia/onto/CPV/>
    
    select distinct ?art ?author ?place where {
    
    ?art a a-arco:HistoricOrArtisticProperty;
      dc:creator ?author.
    ?author cpv:hasBirthPlace | cpv:hasDeathPlace ?place.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, arco_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        place = result["place"]["value"]
        result_list.append([art, author, place])
    return result_list


def q_arco_author_place_tot(): 
    "Count of artworks having an author specified"
    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cpv: <https://w3id.org/italia/onto/CPV/>
    
    select (count(distinct ?art) as ?tot) where {
    
    ?art a a-arco:HistoricOrArtisticProperty;
      dc:creator ?author.
    ?author cpv:hasBirthPlace | cpv:hasDeathPlace ?place.
    } 

    """
    res = sparql_query_setting(q, arco_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)

#------------- ALIGNMENTS -------------------#

def q_arco_art_aligned_tot(): 
    "Count of artworks being aligned to wikidata"
    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cpv: <https://w3id.org/italia/onto/CPV/>
    
    
    select (count(distinct ?art) as ?tot) where {
    
    ?art a a-arco:HistoricOrArtisticProperty;
           owl:sameAs ?aligned. 

    FILTER(regex(str(?aligned), "wikidata", "i"))
    } 

    """


    res = sparql_query_setting(q, arco_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)

def q_arco_author_wikidata(): 

    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cpv: <https://w3id.org/italia/onto/CPV/>
    
    select distinct ?author ?wikidata where {
    
    ?art a a-arco:HistoricOrArtisticProperty;
                   rdfs:label ?label;
                 dc:creator ?author.
       
    ?author owl:sameAs ?aligned. 

    FILTER(regex(str(?aligned), "wikidata", "i"))
  
} LIMIT 100

    """
    res = sparql_query_setting(q, arco_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        author = result["author"]["value"]
        wd = result["wikidata"]["value"]
        result_list.append([author, wd])
    return result_list


def q_arco_author_wikidata_tot(): 
    "Count of artworks having an author aligned with Wikidata"
    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cpv: <https://w3id.org/italia/onto/CPV/>
    
     select (count(distinct ?art) as ?tot) where {
    
    ?art a a-arco:HistoricOrArtisticProperty;
                   rdfs:label ?label;
                 dc:creator ?author.
       
    ?author owl:sameAs ?aligned. 

    FILTER(regex(str(?aligned), "wikidata", "i"))
    } 

    """
    res = sparql_query_setting(q, arco_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_arco_author_ulan_tot(): 
    "Count of artworks having an author aligned with ULAN"
    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cpv: <https://w3id.org/italia/onto/CPV/>
    
     select (count(distinct ?art) as ?tot) where {
    
    ?art a a-arco:HistoricOrArtisticProperty;
                   rdfs:label ?label;
                 dc:creator ?author.
       
    ?author owl:sameAs ?aligned. 

    FILTER(regex(str(?aligned), "ulan", "i"))
    } 

    """
    res = sparql_query_setting(q, arco_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_arco_author_aligned_tot(): 
    "Count of artworks having an author aligned with ULAN"
    q = """ 

    PREFIX a-arco: <https://w3id.org/arco/ontology/arco/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX cpv: <https://w3id.org/italia/onto/CPV/>
    
     select (count(distinct ?art) as ?tot) where {
    
    ?art a a-arco:HistoricOrArtisticProperty;
                   rdfs:label ?label;
                 dc:creator ?author.
       
    ?author owl:sameAs ?aligned. 

    # either ulan or wikidata
    FILTER((regex(str(?aligned), "ulan", "i") || regex(str(?aligned), "wikidata", "i")))
    } 

    """
    res = sparql_query_setting(q, arco_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)
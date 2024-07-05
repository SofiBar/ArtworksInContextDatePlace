import sys
import os



from functions import sparql_query_setting 

wikidata_endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"


def q_wd_tot(): 
    "Count of visual works in Wikidata"
    q = """ 

  select (count(distinct ?art) as ?tot) where {
  
  wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art. # visual work
 
}

    """
    res = sparql_query_setting(q, wikidata_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_wd_date(): 

    q = """ 


    
    select distinct ?art ?date where {
    
    wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art.
    ?art wdt:P571 ?date.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, wikidata_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        date = result["date"]["value"]
        result_list.append([art, date])
    return result_list

def q_wd_date_tot():
    q= """ 

    
    select distinct  (count (distinct ?art) as ?tot) where {
    
    
    wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art.
    ?art wdt:P571 ?date.
} 

"""
    res = sparql_query_setting(q, wikidata_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_wd_place():
    q = """ 

    
    select distinct  ?art ?site where {
    
    wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art.
    ?art wdt:P1071 ?site. 


    } LIMIT 100
    
    """
    res = sparql_query_setting(q, wikidata_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        loc = result["site"]["value"]
        result_list.append([art, loc])
    return result_list


def q_wd_place_tot():
    q= """ 

    
    select distinct  (count (distinct ?art) as ?tot) where {
    
    wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art.
    ?art wdt:P1071 ?site. 

} 

"""
    res = sparql_query_setting(q, wikidata_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)
    

def q_wd_date_place():
    q = """ 


    
    select distinct  ?art ?date ?site where {
    
    
    wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art.
    ?art wdt:P1071 ?site;
        wdt:P571 ?date.
    


} LIMIT 100


"""
    res = sparql_query_setting(q, wikidata_endpoint)
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        loc = result["site"]["value"]
        date = result["date"]["value"]
        result_list.append([art, loc, date])
    return result_list

def q_wd_date_place_tot():
    q = """ 


    
    select (count (distinct ?art) as ?tot) where {
    

    wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art.
    ?art wdt:P1071 ?site;
        wdt:P571 ?date.

} 


"""

    res = sparql_query_setting(q, wikidata_endpoint)
    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



#----------- Contextual information: AUTHOR ----------------#

def q_wd_author(): 

    q = """ 

    
    select distinct ?art ?author where {
    
    wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art.
    ?art wdt:P170 ?author.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, wikidata_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        result_list.append([art, author])
    return result_list


def q_wd_author_tot(): 
    "Count of artworks having an author specified"
    q = """ 

    
    
    select (count(distinct ?art) as ?tot) where {
    
    wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art.
    ?art wdt:P170 ?author.
    } 

    """
    res = sparql_query_setting(q, wikidata_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_wd_author_date(): 

    q = """ 


    
    select distinct ?art ?author ?date where {
    
    wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art.
    ?art wdt:P170 / (wdt:P569 | wdt:P570) ?dated.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, wikidata_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        date = result["date"]["value"]
        result_list.append([art, author, date])
    return result_list


def q_wd_author_date_tot(): 
    "Count of artworks having an author specified"
    q = """ 
    
    select (count(distinct ?art) as ?tot) where {
    
    wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art.
    ?art wdt:P170 / (wdt:P569 | wdt:P570) ?dated.
    } 

    """
    res = sparql_query_setting(q, wikidata_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)




def q_wd_author_place(): 

    q = """ 

    select distinct ?art ?author ?place where {
    
    wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art.
    ?art wdt:P170 / (wdt:P19 | wdt:P20) ?dated.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, wikidata_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        author = result["author"]["value"]
        place = result["place"]["value"]
        result_list.append([art, author, place])
    return result_list


def q_wd_author_place_tot(): 
    "Count of artworks having an author specified"
    q = """ 
    
    select (count(distinct ?art) as ?tot) where {
    
        wd:Q110910970 ^(wdt:P31/wdt:P279*)  ?art.
    ?art wdt:P170 / (wdt:P19 | wdt:P20) ?dated.

    } 

    """
    res = sparql_query_setting(q, wikidata_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_wd_author_wikidata(): 


    return 0


def q_wd_author_wikidata_tot(): 

    return 0


def q_wd_author_ulan_tot(): 
    "Count of artworks having an author aligned with ULAN"
    q = """ 
     select (count(distinct ?art) as ?tot) where {
    
        wd:Q110910970 ^(wdt:P31/wdt:P279*) ?art. 
        ?ulan ^wdt:P245 / ^wdt:P170 ?art.
    } 

    """
    res = sparql_query_setting(q, wikidata_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)
import sys
import os

# Get the absolute path of the parent directory
#parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Add the parent directory to the Python path
#sys.path.append(parent_dir)

from functions import sparql_query_setting 



zeri_endpoint = "http://data.fondazionezeri.unibo.it/sparql"

def q_zeri_tot(): 
    "Count of artworks (fabio:ArtisticWork) in Zeri"
    q = """ 

    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

    
    select (count(distinct ?art) as ?tot) where {
    
    ?art a fabio:ArtisticWork.
    } 

    """
    res = sparql_query_setting(q, zeri_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_zeri_date(): 
    "Artworks with date of creation in Zeri"
    q = """ 

    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

    
    select distinct ?art ?date where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P4_has_time_span ?time. 
    ?art a fabio:ArtisticWork.
    } LIMIT 100

    """
    res = sparql_query_setting(q, zeri_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        date = result["date"]["value"]
        result_list.append([art, date])
    return result_list



def q_zeri_date_tot(): 
    "Count of artworks with date of creation in Zeri"
    q = """ 

    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

    
    select (count(distinct ?art) as ?tot) where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P4_has_time_span ?time. 
    ?art a fabio:ArtisticWork.
    } 

    """
    res = sparql_query_setting(q, zeri_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)



def q_zeri_place(): 
    "Artworks with place of creation in Zeri"
    q = """ 

    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

    
    select distinct ?art ?place where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P7_took_place_at ?place. 
    ?art a fabio:ArtisticWork.
    }  LIMIT 100

    """
    res = sparql_query_setting(q, zeri_endpoint)

    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        place = result["place"]["value"]
        result_list.append([art, place])
    return result_list



def q_zeri_place_tot(): 
    "Count of artworks with place of creation in Zeri"
    q = """ 

    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    
    select (count(distinct ?art) as ?tot) where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P7_took_place_at ?place.  
    ?art a fabio:ArtisticWork.
    } 

    """
    res = sparql_query_setting(q, zeri_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_zeri_date_place_tot(): 
    "Count of artworks with place of creation in Zeri"
    q = """ 

    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    
    select (count(distinct ?art) as ?tot) where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P7_took_place_at ?place;
        crm:P4_has_time_span ?time.  
    ?art a fabio:ArtisticWork.
    } 

    """
    res = sparql_query_setting(q, zeri_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)

#----------- Contextual information: AUTHOR ----------------#

def q_zeri_author(): 

    q = """ 

    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    
    select distinct ?art ?author where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P14_carried_out_by ?author.  
    ?art a fabio:ArtisticWork.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, zeri_endpoint)
    result_list = []

    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        auth = result["author"]["value"]
        result_list.append([art, auth])
    return result_list



def q_zeri_author_tot(): 
    "Count of artworks with author in Zeri"
    q = """ 

    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

    
    select (count(distinct ?art) as ?tot) where {
    
     ?cre ^crm:P94i_was_created_by ?art; 
        crm:P14_carried_out_by ?author.  
    ?art a fabio:ArtisticWork.
    } 

    """
    res = sparql_query_setting(q, zeri_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_zeri_author_date(): 

    q = """ 
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    PREFIX prov: <http://www.w3.org/ns/prov#>
    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX oaentry: <http://purl.org/emmedi/oaentry/>
    
    select distinct ?art ?author ?date where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P14_carried_out_by ?author.  
    ?art a fabio:ArtisticWork.
    ?author (crm:P92i_was_brought_into_existence_by | crm:P93i_was_taken_out_of_existence_by) / crm:P4_has_time_span ?date.
  
} LIMIT 100

    """
    res = sparql_query_setting(q, zeri_endpoint)
    result_list = []

    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        auth = result["author"]["value"]
        date = result["date"]["value"]
        result_list.append([art, date])
    return result_list



def q_zeri_author_date_tot(): 
    "Count of artworks with authors' date of place or death in Zeri"
    q = """ 

    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    
    select (count(distinct ?art) as ?tot) where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P14_carried_out_by ?author.  
    ?art a fabio:ArtisticWork.
    ?author (crm:P92i_was_brought_into_existence_by | crm:P93i_was_taken_out_of_existence_by) / crm:P4_has_time_span ?date.
    } 

    """
    res = sparql_query_setting(q, zeri_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_zeri_author_place(): 

    q = """ 
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    PREFIX prov: <http://www.w3.org/ns/prov#>
    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX oaentry: <http://purl.org/emmedi/oaentry/>
    
    select distinct ?art ?author ?place where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P14_carried_out_by ?author.  
    ?art a fabio:ArtisticWork.
    ?author (crm:P92i_was_brought_into_existence_by | crm:P93i_was_taken_out_of_existence_by) / crm:P8_took_place_at ?date.
    # NB: the right property should be P7. The error is in the data. 
  
} LIMIT 100

    """
    res = sparql_query_setting(q, zeri_endpoint)
    result_list = []

    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        auth = result["author"]["value"]
        result_list.append([art, auth])
    return result_list



def q_zeri_author_place_tot(): 
    "Count of artworks with author in Zeri"
    q = """ 

    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    
    select (count(distinct ?art) as ?tot) where {
    
     ?cre ^crm:P94i_was_created_by ?art; 
        crm:P14_carried_out_by ?author.  
    ?art a fabio:ArtisticWork.
    ?author (crm:P92i_was_brought_into_existence_by | crm:P93i_was_taken_out_of_existence_by) / crm:P8_took_place_at ?date.
    # NB: the right property should be P7. The error is in the data. 
    } 

    """
    res = sparql_query_setting(q, zeri_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)




def q_zeri_art_aligned_tot(): 
    "Count of artworks aligned with Wikidata"
    q = """ 

    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    PREFIX prov: <http://www.w3.org/ns/prov#>
    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX oaentry: <http://purl.org/emmedi/oaentry/>
    
    select (count(distinct ?art) as ?tot) where {
    
    ?cre ^crm:P94i_was_created_by ?art. 
    ?art a fabio:ArtisticWork;
        owl:sameAs ?aligned. 
  

    FILTER(regex(str(?aligned), "wikidata", "i"))
    } 

    """
    res = sparql_query_setting(q, zeri_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_zeri_author_aligned(): 

    q = """ 
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    PREFIX prov: <http://www.w3.org/ns/prov#>
    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX oaentry: <http://purl.org/emmedi/oaentry/>
    
    select distinct ?art ?aligned where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P14_carried_out_by ?author.  
    ?art a fabio:ArtisticWork.
    ?author owl:sameAs ?aligned. 
  
} LIMIT 100

    """
    res = sparql_query_setting(q, zeri_endpoint)
    result_list = []

    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        aligned = result["aligned"]["value"]
        result_list.append([art, aligned])
    return result_list


def q_zeri_author_wikidata_tot(): 
    "Count of artworks having an author aligned with Wikidata"
    q = """ 

    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    PREFIX prov: <http://www.w3.org/ns/prov#>
    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX oaentry: <http://purl.org/emmedi/oaentry/>
    
    select (count(distinct ?art) as ?tot) where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P14_carried_out_by ?author.  
    ?art a fabio:ArtisticWork.
    ?author owl:sameAs ?aligned. 
  

    FILTER(regex(str(?aligned), "wikidata", "i"))
    } 

    """
    res = sparql_query_setting(q, zeri_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_zeri_author_ulan_tot(): 
    "Count of artworks having an author aligned with ULAN"
    q = """ 

       PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    PREFIX prov: <http://www.w3.org/ns/prov#>
    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX oaentry: <http://purl.org/emmedi/oaentry/>
    
    select (count(distinct ?art) as ?tot) where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P14_carried_out_by ?author.  
    ?art a fabio:ArtisticWork.
    ?author owl:sameAs ?aligned. 
  

    FILTER(regex(str(?aligned), "ulan", "i"))
    } 

    """
    res = sparql_query_setting(q, zeri_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def q_zeri_author_aligned_tot(): 
    "Count of artworks having an author aligned with ULAN or Wikidata"
    q = """ 

       PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    PREFIX prov: <http://www.w3.org/ns/prov#>
    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX oaentry: <http://purl.org/emmedi/oaentry/>
    
    select (count(distinct ?art) as ?tot) where {
    
    ?cre ^crm:P94i_was_created_by ?art; 
        crm:P14_carried_out_by ?author.  
    ?art a fabio:ArtisticWork.
    ?author owl:sameAs ?aligned. 
  

    FILTER((regex(str(?aligned), "ulan", "i") || regex(str(?aligned), "wikidata", "i")))
    } 

    """
    res = sparql_query_setting(q, zeri_endpoint)

    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)
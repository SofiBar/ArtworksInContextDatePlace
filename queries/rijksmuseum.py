import sys
import os



from functions import sparql_query_setting, query_wrapper_tot

# Rk dataset was downloaded and uploaded on a local Blazegraph server
local_endpoint = 'http://localhost:9999/blazegraph/namespace/kb/sparql'




def q_rk_tot(): 
    "Count of artworks (a-arco:HistoricOrArtisticProperty) in ArCO"
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    select (count (distinct ?art) as ?tot) where {
    
    ?art a edm:ProvidedCHO; dcterms:created ?date.

    }

    """

    tot =  query_wrapper_tot(q, local_endpoint) 
    return tot


def q_rk_date_tot(): 
    "Count of artworks (a-arco:HistoricOrArtisticProperty) in ArCO"
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    select (count (distinct ?art) as ?tot) where {
    
    ?art a edm:ProvidedCHO; dcterms:created ?date.

    }

    """

    tot =  query_wrapper_tot(q, local_endpoint) 
    return tot


def q_rk_place_tot(): 
    "Count of artworks (a-arco:HistoricOrArtisticProperty) in ArCO"
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    select (count (distinct ?art) as ?tot) where {
    
    ?art a edm:ProvidedCHO; 
        dcterms:spatial ?place.

    }

    """

    tot =  query_wrapper_tot(q, local_endpoint) 
    return tot


def q_rk_date_place_tot(): 
    "Count of artworks (a-arco:HistoricOrArtisticProperty) in ArCO"
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    select (count (distinct ?art) as ?tot) where {
    
    ?art a edm:ProvidedCHO; 
        dcterms:created ?date; 
        dcterms:spatial ?place.
    }

    """

    tot =  query_wrapper_tot(q, local_endpoint) 
    return tot


#----------- Contextual information: AUTHOR ----------------#

def q_rk_author_tot(): 
    "Count of artworks (a-arco:HistoricOrArtisticProperty) in ArCO"
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    select (count (distinct ?art) as ?tot) where {
    
    ?art a edm:ProvidedCHO; 
        dc:creator ?author.
    FILTER (?author != <http://hdl.handle.net/10934/RM0001.PEOPLE.0>)
    }

    """

    tot =  query_wrapper_tot(q, local_endpoint) 
    return tot


def q_rk_author_date_tot(): 
    "Count of artworks (a-arco:HistoricOrArtisticProperty) in ArCO"
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaGr2: <http://rdvocab.info/ElementsGr2/>

    select (count (distinct ?art) as ?tot) where {

    VALUES ?rel {rdaGr2:dateOfDeath rdaGr2:dateOfBirth}
     ?art a edm:ProvidedCHO; 
        dc:creator ?author.
    ?author ?rel ?date.
    FILTER (?author != <http://hdl.handle.net/10934/RM0001.PEOPLE.0>)

    }

    """

    tot =  query_wrapper_tot(q, local_endpoint) 
    return tot


def q_rk_author_place_tot(): 
    "Count of artworks (a-arco:HistoricOrArtisticProperty) in ArCO"
    q = """ 

     PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaGr2: <http://rdvocab.info/ElementsGr2/>
        
    
    select (count (distinct ?art) as ?tot) where {
    # VALUES ?rel {rdaGr2:placeOfDeath rdaGr2:placeOfBirth}
     ?art a edm:ProvidedCHO; 
        dc:creator ?author.
    ?author rdaGr2:placeOfDeath | rdaGr2:placeOfBirth ?place.

    FILTER (?author != <http://hdl.handle.net/10934/RM0001.PEOPLE.0>)
    }

    """

    tot =  query_wrapper_tot(q, local_endpoint) 
    return tot



def q_rk_art_aligned_tot(): 
    "Count of artworks (a-arco:HistoricOrArtisticProperty) in ArCO"
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    select (count (distinct ?art) as ?tot) where {
    
    ?art a edm:ProvidedCHO; owl:sameAs ?aligned.

    FILTER(regex(str(?aligned), "wikidata", "i"))
    }

    """

    tot =  query_wrapper_tot(q, local_endpoint) 
    return tot


def q_rk_author_aligned_tot(): 
    "Count of artworks (a-arco:HistoricOrArtisticProperty) in ArCO"
    q = """ 

    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    select (count (distinct ?art) as ?tot) where {
    
    ?art a edm:ProvidedCHO; 
        dc:creator ?author. 
    ?author owl:sameAs ?aligned.

    FILTER (?author != <http://hdl.handle.net/10934/RM0001.PEOPLE.0>)
    FILTER((regex(str(?aligned), "ulan", "i") || regex(str(?aligned), "wikidata", "i")))
    }

    """

    tot =  query_wrapper_tot(q, local_endpoint) 
    return tot
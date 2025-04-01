import sys
import os



from functions import sparql_query_setting, query_wrapper_tot

# Rk dataset was downloaded and uploaded on a local Blazegraph server
local_endpoint = 'http://localhost:9999/blazegraph/namespace/kb/sparql'
rkd_endpoint = "https://api.rkd.triply.cc/datasets/rkd/RKD-Knowledge-Graph/services/SPARQL/sparql"



def q_rkd_tot(): 
    "Count of artworks in RKD"
    q = """ 

    prefix aat: <http://vocab.getty.edu/aat/>
    prefix crm: <http://www.cidoc-crm.org/cidoc-crm/>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>

    select (count (distinct ?art) as ?tot) where {
    
    ?art a crm:E22_Human-Made_Object;
    crm:P2_has_type aat:300133025. # work of art

    }

    """

    tot =  query_wrapper_tot(q, rkd_endpoint) 
    return tot


def q_rkd_date_tot(): 
    
    q = """ 

    prefix aat: <http://vocab.getty.edu/aat/>
    prefix crm: <http://www.cidoc-crm.org/cidoc-crm/>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>

    select (count (distinct ?art) as ?tot) where {
    
    ?art a crm:E22_Human-Made_Object;
    crm:P2_has_type aat:300133025;
    crm:P108i_was_produced_by /crm:P4_has_time-span ?timespan. 

    }

    """

    tot =  query_wrapper_tot(q, rkd_endpoint) 
    return tot


def q_rkd_place_tot(): 
    
    q = """ 

    prefix aat: <http://vocab.getty.edu/aat/>
    prefix crm: <http://www.cidoc-crm.org/cidoc-crm/>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>

    select (count (distinct ?art) as ?tot) where {
    
    ?art a crm:E22_Human-Made_Object;
    crm:P2_has_type aat:300133025;
    crm:P108i_was_produced_by /crm:P7_took_place_at ?place. 

    }

    """

    tot =  query_wrapper_tot(q, rkd_endpoint) 
    return tot


def q_rkd_date_place_tot(): 
    
    q = """ 

    prefix aat: <http://vocab.getty.edu/aat/>
    prefix crm: <http://www.cidoc-crm.org/cidoc-crm/>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>

    select (count (distinct ?art) as ?tot) where {
    
    ?art a crm:E22_Human-Made_Object;
        crm:P2_has_type aat:300133025;
        crm:P108i_was_produced_by ?prod. 
    ?prod crm:P7_took_place_at ?place; 
        crm:P4_has_time-span ?time. 
    }

    """

    tot =  query_wrapper_tot(q, rkd_endpoint) 
    return tot


#----------- Contextual information: AUTHOR ----------------#

def q_rkd_author_tot(): 
    
    q = """ 

    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix aat: <http://vocab.getty.edu/aat/>
    prefix crm: <http://www.cidoc-crm.org/cidoc-crm/>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix owl: <http://www.w3.org/2002/07/owl#>

    select (count (distinct ?art) as ?tot) where {

    ?art a crm:E22_Human-Made_Object;
    crm:P2_has_type aat:300133025;
    crm:P108i_was_produced_by /crm:P14_carried_out_by ?auth. 
    
    }

    """

    tot =  query_wrapper_tot(q, rkd_endpoint) 
    return tot


def q_rkd_author_attr_tot(): 
    
    q = """ 

    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix aat: <http://vocab.getty.edu/aat/>
    prefix crm: <http://www.cidoc-crm.org/cidoc-crm/>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix owl: <http://www.w3.org/2002/07/owl#>

    select (count (distinct ?art) as ?tot) where {

    ?art a crm:E22_Human-Made_Object;
    crm:P2_has_type aat:300133025;
      # the majority of authors attributions are made through an attribution act. The property rdf:first indicates the first of the list. 
    crm:P140i_was_attributed_by / rdf:first /crm:P141_assigned ?assigned.
    ?assigned a crm:E21_Person.
    
    }

    """

    tot =  query_wrapper_tot(q, rkd_endpoint) 
    return tot


def q_rkd_author_date_tot(): 
    
    q = """ 

    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix aat: <http://vocab.getty.edu/aat/>
    prefix crm: <http://www.cidoc-crm.org/cidoc-crm/>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix owl: <http://www.w3.org/2002/07/owl#>

    select (count (distinct ?art) as ?tot) where {

    ?art a crm:E22_Human-Made_Object;
    crm:P2_has_type aat:300133025;
      # the majority of authors attributions are made through an attribution act. The property rdf:first indicates the first of the list. 
    crm:P140i_was_attributed_by / rdf:first / crm:P141_assigned ?person. 
  ?person a crm:E21_Person; (crm:P100i_died_in | crm:P98i_was_born) ?event.  #(crm:P100i_died_in | crm:P98i_was_born) ?place.
 # ?first crm:P141_assigned [ a crm:E21_Person; (crm:P100i_died_in | crm:P98i_was_born) ?event ]. 
    ?event crm:P4_has_time-span ?time. 
#  ?time crm:P82a_begin_of_the_begin ?date. 
  # ?event crm:P7_took_place_at ?place. 

    }

    """

    tot =  query_wrapper_tot(q, rkd_endpoint) 
    return tot


def q_rkd_author_place_tot(): 
    
    q = """ 

    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix aat: <http://vocab.getty.edu/aat/>
    prefix crm: <http://www.cidoc-crm.org/cidoc-crm/>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix owl: <http://www.w3.org/2002/07/owl#>
        
    select (count (distinct ?art) as ?tot) where {
    ?art a crm:E22_Human-Made_Object;
    crm:P2_has_type aat:300133025;
      # the majority of authors attributions are made through an attribution act. The property rdf:first indicates the first of the list. 
    crm:P140i_was_attributed_by / rdf:first / crm:P141_assigned ?person. 
  ?person a crm:E21_Person; (crm:P100i_died_in | crm:P98i_was_born) ?event.  #(crm:P100i_died_in | crm:P98i_was_born) ?place.
 # ?first crm:P141_assigned [ a crm:E21_Person; (crm:P100i_died_in | crm:P98i_was_born) ?event ]. 
   ?event crm:P7_took_place_at ?place. 
    }

    """

    tot =  query_wrapper_tot(q, rkd_endpoint) 
    return tot



def q_rkd_art_aligned_tot(): 
    
    q = """ 

    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix aat: <http://vocab.getty.edu/aat/>
    prefix crm: <http://www.cidoc-crm.org/cidoc-crm/>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix owl: <http://www.w3.org/2002/07/owl#>
    prefix la: <https://linked.art/ns/terms/>

    select (count (distinct ?art) as ?tot) where {
    
      ?art a crm:E22_Human-Made_Object;
        crm:P2_has_type aat:300133025;
        la:equivalent ?aligned. 


    FILTER(regex(str(?aligned), "wikidata", "i"))
    }

    """

    tot =  query_wrapper_tot(q, rkd_endpoint) 
    return tot


def q_rkd_author_aligned_tot(): 
    
    q = """ 

    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix aat: <http://vocab.getty.edu/aat/>
    prefix crm: <http://www.cidoc-crm.org/cidoc-crm/>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix owl: <http://www.w3.org/2002/07/owl#>
    prefix la: <https://linked.art/ns/terms/>

    select (count(distinct ?art) as ?tot) where {

        ?art a crm:E22_Human-Made_Object;
        crm:P2_has_type aat:300133025;
        # the majority of authors attributions are made through an attribution act. The property rdf:first indicates the first of the list. 
        crm:P140i_was_attributed_by / rdf:first / crm:P141_assigned ?person. 
    ?person la:equivalent ?aligned. 
    # filter for authors having at least an alignment to ULAN or Wikidata
    FILTER((regex(str(?aligned), "ulan", "i") || regex(str(?aligned), "wikidata", "i")))

    }

    """

    tot =  query_wrapper_tot(q, rkd_endpoint) 
    return tot
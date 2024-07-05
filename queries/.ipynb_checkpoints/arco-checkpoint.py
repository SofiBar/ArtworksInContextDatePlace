import sys
import os

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

from functions import sparql_query_setting 



arco_endpoint = "https://dati.beniculturali.it/sparql"


def q_arco_date(): 

    q = """ 


    """
    res = sparql_query_setting(q_arco, arco_endpoint)

# manipulate the result
    result_list = []
    for result in res["results"]["bindings"]:
        art = result["art"]["value"]
        loc = result["place"]["value"]
        date = result["date"]["value"]
        result_list.append([art, loc, date])
    return result_list

q_arco_place = """ 


"""

q_arco_date_place = """ 


"""
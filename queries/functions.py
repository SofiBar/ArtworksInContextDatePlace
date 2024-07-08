from SPARQLWrapper import SPARQLWrapper, JSON
import json

def sparql_query_setting(query, endpoint):# set the endpoint
  sparql = SPARQLWrapper(endpoint)
                         #, agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
  # set the query
  sparql.setQuery(query)
  # set the returned format
  sparql.setReturnFormat(JSON)
  # get the results
  results = sparql.query().convert()
  return results



def query_wrapper_tot(q, endpoint): 
    "function to launch queries retrieving only a sum of results"
    res = sparql_query_setting(q, endpoint)
    tot =  res["results"]["bindings"][0]["tot"]["value"]
    return int(tot)


def pprint_prop(num1, tot, l, l_prop): 
    "prints the number and the proportion over the total of artworks. It adds the absolute number to the dataset list and the percentage to the dataset proportion list" 
    p = round((int(num1)/int(tot))*100, 2)
    print("total: ", num1)
    print("percentage of the total of artworks: ", p)
    l.append(num1)
    l_prop.append(p)
    print(l)
    print(l_prop)
    return p


def make_prop_list(res_list): 
    "returns the dataset proportion list. Total of artwork at index one, name of dataset at index 0 of the list" 
    # append the name of the dataset to the prop_list
    l_prop = [res_list[0]]
    tot = res_list[1]
    for num in res_list[2:]:
        p = round((int(num)/int(tot))*100, 2)
        l_prop.append(p)
  
    return l_prop


def q_rdflib_tot(q, g): 
    "Input: every SPARQL query having 'tot' as unique result. Query against a given graph with rdflib"

    tot = g.query(q)
    for row in tot:
        res = int(row.tot)
    return res


# open dictionaries stored in json
def open_json(json_file): 
  with open(json_file, mode='r', encoding="utf-8") as jsonfile:
    dictName = json.load(jsonfile)
    return dictName

# save a dictionary in json
def store_in_json(file_name, dictName): 
  with open(file_name, mode='w', encoding="utf-8") as jsonfile:
    json.dump(dictName, jsonfile)
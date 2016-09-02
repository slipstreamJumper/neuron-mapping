import math
import random
import sys

nodes_to_generate = int(sys.argv[1])
required_strength = float(sys.argv[2])
existing_relationships = []

def generate_synapse(req_strength):
    nodes = []
    relationship_probabilities = []
    relationships = []
    
    for i in range(nodes_to_generate):
        nodes.append({"node_id":i})

    for n in nodes:
        for no in nodes:
            relationship_probabilities.append({"from_node":n["node_id"], "to_node":no["node_id"], "probability":random.random()})


    for rp in relationship_probabilities:
      print("relationships: ", len(relationships))
      if (rp["probability"] >= req_strength and rp["to_node"] != rp["from_node"]):
    
        if([rp["to_node"], rp["from_node"]] not in existing_relationships and [rp["from_node"],rp["to_node"]] not in existing_relationships):
          rp["relationship_id"] = (random.random()*random.random())*1000
          relationships.append(rp)
          existing_relationships.append([rp["to_node"],rp["from_node"]])

         
    f = open("gephi_neurons.csv", "w+")
    for r in relationships:
        f.write(str(r["from_node"])+";"+str(r["to_node"])+"\n")
            
    return len(relationships)  

print("Number of Nodes: ", str(nodes_to_generate))
print("Required Strength: " , str(required_strength))
print("Number of Synapse: " , str(generate_synapse(required_strength)))
    

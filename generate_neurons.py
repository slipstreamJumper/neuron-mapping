import math
import random
import sys

nodes_to_generate = int(sys.argv[1])
trial_to_run = int(sys.argv[2])
required_strength = float(sys.argv[3])


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
        if (rp["probability"] >= req_strength and rp["to_node"] != rp["from_node"]):
            rp["relationship_id"] = (random.random()*random.random())*1000
            relationships.append(rp)

    return len(relationships)    

print("Number of Nodes: ", str(nodes_to_generate))
print("Required Strength: " , str(required_strength))

for i in range(trial_to_run):
    print ("Number of Synapse: " , str(generate_synapse(required_strength)))
    

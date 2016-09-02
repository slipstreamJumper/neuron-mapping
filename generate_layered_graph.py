import math
import random
import sys
import uuid

layers = int(sys.argv[1])
nodes_to_generate = int(sys.argv[2])
required_strength = float(sys.argv[3])
existing_relationships = []


def generate_synapse(req_strength):
    nodes = []
    relationship_probabilities = []
    relationships = []
    temp = 0
    for l in range(layers):
        temp = 0
        for i in range(random.randrange(nodes_to_generate)):
            nodes.append({"layer": l,"node_num":temp, "node_id": str(l)+ "::" + str(temp) + "::" + str(uuid.uuid4())})
            temp += 1

    for n in nodes:
      for no in nodes:
            n_temp = [int(n["node_num"])-1, int(n["node_num"]), int(n["node_num"])+1]
            no_temp = [int(no["node_num"])-1, int(no["node_num"]), int(no["node_num"])+1]
            if(no["layer"] != n["layer"] and (int(n["node_num"]) in no_temp)
               and ((int(no["layer"]) ==(int(n["layer"]) + 1))
               or (int(no["layer"]) == int(n["layer"]))
               or (int(no["layer"]) ==(int(n["layer"]) - 1)))
               ):
              relationship_probabilities.append({"from_node":n["node_id"], "to_node":no["node_id"], "probability":random.random()})

  
           
    for rp in relationship_probabilities:

      if (rp["probability"] >= req_strength and rp["to_node"] != rp["from_node"]):
    
        if([rp["to_node"], rp["from_node"]] not in existing_relationships and [rp["from_node"],rp["to_node"]] not in existing_relationships):
          rp["relationship_id"] = (random.random()*random.random())*1000
          relationships.append(rp)
          existing_relationships.append([rp["to_node"],rp["from_node"]])

         
    f = open("gephi_layered_neurons.csv", "w+")
    for r in relationships:
        f.write(str(r["from_node"])+";"+str(r["to_node"])+"\n")
            
    return len(relationships)  

print("Number of Nodes: ", str(nodes_to_generate))
print("Required Strength: " , str(required_strength))
print("Number of Synapse: " , str(generate_synapse(required_strength)))
    

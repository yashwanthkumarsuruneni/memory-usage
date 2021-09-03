import pandas as pd
from dict2xml import dict2xml
import yaml
import json

data = pd.read_csv("input.csv")

# Calculate AVG
def Average(lst):
    return round(sum(lst) / len(lst),2)


def dict_to_xml(agg_dict):
    # convert to xml
    xml = dict2xml(agg_dict)
    return xml

def write_to_xml(file_name,data):
    # open file to write
    with open(file_name,'w') as f:
        f.write(data)

def write_to_yaml(file_name,data):
    # open file to write
    with open(file_name,'w') as f:
        yaml.dump(data, f)


def write_to_json(file_name,data):
    # open file to write
    with open(file_name, "w") as f:  
        json.dump(data, f)

# calculate the stats 
def stats():
    agg_values = []
    total_sum=total_count=0
    agg_min=float('inf')
    agg_max=-float('inf')
    agg_average=0
    summary = {
        "hosts":[],
        "agg_min":0,
        "agg_max":0,
        "agg_avg":0
    }
    print("HOST_NAME, MAX, MIN, AVG")
    for column in data:
        column_obj = data[column]
        if "#" in column:
            host_name,host_max,host_min,host_avg=column.split("#")[1],column_obj.values.max(), column_obj.values.min() , Average(column_obj.values)
            print(column.split("#")[1], column_obj.values.max(), column_obj.values.min() , Average(column_obj.values))
            values=[x for x in column_obj.values if str(x) != 'nan']
            total_sum+=sum(values)
            total_count+=len(values)
            agg_max=max(agg_max,host_max)
            agg_min=min(agg_min,host_min)
            host_map={"max": str(host_max) if str(host_max) == 'nan' else int(host_max),"min": str(host_min) if str(host_min) == 'nan' else int(host_min),"average":str(host_avg) if str(host_avg) == 'nan' else int(host_avg),"name":host_name}
            summary["hosts"].append(host_map)
            
    summary["agg_max"]=float(agg_max)
    summary["agg_min"]=float(agg_min)
    summary["agg_avg"]=float(round(total_sum/total_count,2))
    return summary


# main 
def main():
    print("This program calculates the memory usage\n")
    output = stats()
    #convert to xml
    xml=dict_to_xml(output)
    #write to xml
    write_to_xml('output.xml',xml)
    #write to json
    write_to_json('output.json',output)
    #write to yaml
    write_to_yaml('output.yaml',output)

main()







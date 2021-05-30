from graphviz import Graph
import xmltodict

with open("HACK.xml") as fd:
    doc = xmltodict.parse(fd.read())

company_to_processes = dict()
process_id = dict()
id_process = dict()
for i in doc['Batch']['LogicalUnit']:
    tmp = []
    try:
        for j in i['ProcessNodeDataDO']:
            tmp.append(j['NodeName'])
            process_id[j['NodeName']] = j['NodeId']
            id_process[j['NodeId']] = j['NodeName']
    except:
        tmp = []
    company_to_processes[i['CampaignDO']['Name']] = tmp

diag_to_process = dict()
for comp in doc['Batch']['LogicalUnit']:
    diag_to_process[comp['CampaignDO']['Name']] = comp['FlowDO']['ZOrderIdList']['#text'].split(',')

new_diag_process = dict()
for diag in diag_to_process:
    new_diag_process[diag] = []
    for process in diag_to_process[diag]:
        try:
            new_diag_process[diag].append(id_process[process])
        except:
            continue

process_data = dict()
for prc in process_id:
    process_data[prc] = []

for comp in doc['Batch']['LogicalUnit']:
    try:
        for process in comp['ProcessNodeDataDO']:
            process_data[process['NodeName']].append(process['Process']['TableName'])
    except:
        print(end='')

for i in process_data:
    process_data[i] = list(set(process_data[i]))


graph = Graph('G', filename='er.gv', engine='dot')
graph.attr(overlap='false')
for prc in process_data:
    graph.node('PROC_' + str(prc), shape='circle')
    for data in process_data[prc]:
        graph.node('TABLE_' + data, shape='square')
        graph.edge('PROC_' + str(prc), 'TABLE_' + data, ranksep='0.75')

for diag in new_diag_process:
    graph.node('DIAG_' + diag, shape='octagon')
    for prc in new_diag_process[diag]:
        graph.edge('DIAG_' + diag, 'PROC_' + str(prc), ranksep='0.75')
graph.view()
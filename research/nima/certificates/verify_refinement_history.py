"""Independent finite-DAG coherence checker for the two admitted scalar edge types."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import sys

HERE=Path(__file__).resolve().parent


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,HERE/file)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


d=load('diagonal_edges','verify_diagonal_transition.py')
t=load('tail_edges','verify_tail_refinement.py')
v=d.v


def multiply(a,b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def maps(old,new,cert):
    if cert['kind']=='positive-diagonal-refinement-v1':
        d.verify_transition(old,new,cert)
        n=len(old['rows'])
        def diagonal(field):
            values=list(map(v.q,cert[field]))
            return tuple(tuple(F(1)/values[i] if i==j else F(0) for j in range(n)) for i in range(n))
        return diagonal('source_scale'),diagonal('observation_scale'),v.q(cert['target_scale'])
    if cert['kind']=='unit-tail-partition-v1':
        t.verify_edge(old,new,cert)
        matrix=tuple(tuple(F(int(j in group)) for j in range(len(new['rows']))) for group in cert['groups'])
        return matrix,matrix,F(1)
    raise ValueError('Unadmitted history transition')


def verify_history(bundle):
    v.fields(bundle,('version','kind','calibration_contract','structural_transport','nodes','edges'))
    v.require(type(bundle['version']) is int and bundle['version']==1,'Wrong history version')
    v.require(bundle['kind']=='finite-scalar-refinement-history-v1','Wrong history kind')
    v.require(bundle['calibration_contract']=='one-fixed-ideal-detector-up-to-declared-coordinate-gains','Detector redesign is not certified')
    v.require(bundle['structural_transport']=='not-certified','Unsupported structural claim')
    v.array(bundle['nodes']);v.array(bundle['edges'])
    v.require(1<=len(bundle['nodes'])<=32 and len(bundle['edges'])<=128,'History exceeds supported bounds')
    nodes={};order={};incoming={};ledger=[]
    for index,node in enumerate(bundle['nodes']):
        v.fields(node,('id','problem','certificate'))
        key=node['id'];v.require(type(key) is str and 0<len(key)<=128 and key not in nodes,'Invalid node id')
        v.verify(node['problem'],node['certificate'])
        nodes[key]=node;order[key]=index;incoming[key]=[]
    pairs=set()
    for edge in bundle['edges']:
        v.fields(edge,('from','to','certificate'))
        start,end=edge['from'],edge['to']
        v.require(type(start) is str and type(end) is str and start in nodes and end in nodes,'Unknown endpoint')
        v.require(order[start]<order[end] and (start,end) not in pairs,'Cycle, bad order or duplicate edge')
        pairs.add((start,end))
        cert=edge['certificate'];v.require(type(cert) is dict and 'kind' in cert,'Missing edge kind')
        triple=maps(nodes[start]['problem'],nodes[end]['problem'],cert)
        incoming[end].append((start,triple))
        old_status=nodes[start]['certificate']['status'];new_status=nodes[end]['certificate']['status']
        ledger.append({'from':start,'to':end,'kind':cert['kind'],
            'old_status':old_status,'new_status':new_status,
            'claim_boundary':'Universal implications pull back; new nonempty feasibility uses the destination certificate.',
            'source_budget':{'old':nodes[start]['problem']['budget'],'new':nodes[end]['problem']['budget']},
            'old_dimension':len(nodes[start]['problem']['rows']),
            'new_dimension':len(nodes[end]['problem']['rows'])})
    ancestors={};comparisons=0
    for index,node in enumerate(bundle['nodes']):
        key=node['id'];v.require(index==0 or bool(incoming[key]),'Disconnected nonroot node')
        known={}
        def admit(ancestor,triple):
            nonlocal comparisons
            if ancestor in known:
                comparisons+=1
                v.require(known[ancestor]==triple,'Incoherent routes from '+ancestor+' to '+key)
            else:known[ancestor]=triple
        for parent,edge_map in incoming[key]:
            admit(parent,edge_map)
            for ancestor,earlier in ancestors[parent].items():
                composed=(multiply(earlier[0],edge_map[0]),multiply(earlier[1],edge_map[1]),earlier[2]*edge_map[2])
                admit(ancestor,composed)
        ancestors[key]=known
    return {'verified':True,'nodes':len(nodes),'edges':len(bundle['edges']),
            'alternative_route_comparisons':comparisons,'transition_ledger':ledger,
            'scope':'Finite declared scalar changes only. Calibration identity, source embeddings and acquisitions remain external assumptions; structural transport is not certified.'}


if __name__=='__main__':
    import json
    print(json.dumps(verify_history(v.strict_load(sys.argv[1])),indent=2))

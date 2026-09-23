"""Independent paths, triangle completeness and modular statement checks."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
if not __debug__:raise RuntimeError('Assertions required')
OUT=Path(__file__).resolve().parents[1]/'results'
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def original_edges(b):
    edges=[]
    for v in b['nodes']:
        if v:edges.extend([[0,v,str(98+2*v)],[v,0,'0']])
    return edges+b['evidence']
def path_check(path,edges,start,end,weight):
    current=start;total=Q(0)
    for index in path:
        assert type(index) is int and 0<=index<len(edges)
        u,v,w=edges[index];assert u==current;current=v;total+=Q(w)
    assert current==end and total==weight

def closure_check(nodes,edges,p):
    if p['status']=='INCONSISTENT':
        cycle=p['cycle'];assert cycle
        assert all(type(k) is int and 0<=k<len(edges) for k in cycle)
        start=edges[cycle[0]][0];weight=sum(Q(edges[k][2]) for k in cycle);assert weight<0
        path_check(cycle,edges,start,start,weight);return None
    assert p['status']=='CONSISTENT';D=[list(map(Q,row)) for row in p['distance']];paths=p['paths'];n=len(nodes)
    assert len(D)==len(paths)==n and all(len(r)==n for r in D+paths)
    for i,u in enumerate(nodes):
        assert D[i][i]==0
        for j,v in enumerate(nodes):
            path_check(paths[i][j],edges,u,v,D[i][j])
            assert all(D[i][j]<=D[i][k]+D[k][j] for k in range(n))
    for u,v,w in edges:assert D[nodes.index(u)][nodes.index(v)]<=Q(w)
    return D

def check(expected,packet,*,_local_check=closure_check,_interface_check=closure_check):
    # Internal hooks for verifier-owned memoization; default is full replay.
    assert packet['state']==expected and packet['state_digest']==digest(expected)
    blocks=expected['blocks'];m=expected['m'];assert len(packet['blocks'])==len(blocks)
    owners={};boundary=set()
    for b in blocks:
        assert b['nodes']==sorted(set(b['nodes'])) and b['boundary']==sorted(set(b['boundary']))
        assert 0 in b['boundary'] and set(b['boundary'])<=set(b['nodes'])
        assert all(type(v) is int and 0<=v<=m for v in b['nodes'])
        for v in b['nodes']:owners.setdefault(v,[]).append(b)
        boundary.update(b['boundary'])
    assert set(owners)==set(range(m+1))
    assert all(len(bs)==1 or all(v in b['boundary'] for b in bs) for v,bs in owners.items())
    assert set(expected['public'])<=boundary and 0 in expected['public']
    assert expected['retention'] in ('public-only','archive-backed')
    assert all(u in boundary and v in boundary for u,v,w in expected['exterior'])
    local=[_local_check(b['nodes'],original_edges(b),p) for b,p in zip(blocks,packet['blocks'])]
    if 'inconsistent_block' in packet:
        assert packet['status']=='INCONSISTENT' and local[packet['inconsistent_block']] is None;return None
    assert all(D is not None for D in local)
    nodes=sorted(boundary);assert packet['interface_nodes']==nodes
    edges=[];expanded=[]
    for bi,(b,D,p) in enumerate(zip(blocks,local,packet['blocks'])):
        for u in b['boundary']:
            for v in b['boundary']:
                if u==v:continue
                i,j=b['nodes'].index(u),b['nodes'].index(v)
                edges.append([u,v,str(D[i][j])]);expanded.append([['block',bi,k] for k in p['paths'][i][j]])
    for k,e in enumerate(expected['exterior']):edges.append(e);expanded.append([['exterior',k]])
    D=_interface_check(nodes,edges,packet['composed']);assert packet['status']==packet['composed']['status']
    if D is None:
        assert packet['expanded_cycle']==[e for k in packet['composed']['cycle'] for e in expanded[k]]
        fine=[]
        for e in packet['expanded_cycle']:
            fine.append(original_edges(blocks[e[1]])[e[2]] if e[0]=='block' else expected['exterior'][e[1]])
        assert fine and sum(Q(w) for u,v,w in fine)<0
        assert all(fine[k][1]==fine[(k+1)%len(fine)][0] for k in range(len(fine)))
        return None
    summary=[[u,v,str(D[nodes.index(u)][nodes.index(v)])] for u in expected['public'] for v in expected['public'] if u!=v]
    assert packet['summary']==summary;return summary

def live_check(s,summary,live):
    assert live=={'m':s['m'],'binding':s['binding'],'public':s['public'],'summary':summary,
                 'retention':s['retention'],'origin_digest':digest(s)}

def main():
    cp=OUT/'modular-difference-contract.json';rp=OUT/'modular-difference.json';raw=(OUT/'modular-difference-packet.json.gz').read_bytes()
    c=json.loads(cp.read_text());report=json.loads(rp.read_text())
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==report['contract_sha256'] and hashlib.sha256(raw).hexdigest()==report['packet_sha256']
    assert hashlib.sha256(Path(__file__).with_name('modular_difference_interfaces.py').read_bytes()).hexdigest()==c['implementation_sha256']
    packets=json.loads(gzip.decompress(raw));assert set(packets)==set(c['states'])
    for name,s in c['states'].items():
        e=packets[name];summary=check(s,e['certificate'])
        edges=[edge for b in s['blocks'] for edge in original_edges(b)]+s['exterior']
        D=closure_check(list(range(s['m']+1)),edges,e['monolithic'])
        assert (summary is None)==(D is None)
        if summary is None:continue
        assert summary==[[u,v,str(D[u][v])] for u in s['public'] for v in s['public'] if u!=v]
        live_check(s,summary,e['live'])
        assert len(e['membership'])==2
        for query in e['membership']:
            y=dict(zip(s['public'],map(Q,query['point'])))
            admitted=y[0]==0 and all(y[v]-y[u]<=Q(w) for u,v,w in summary)
            assert query['admitted']==admitted
        if s['retention']=='archive-backed':
            x=list(map(Q,e['lift']));assert len(x)==s['m']+1 and x[0]==0
            assert [str(x[v]) for v in s['public']]==e['point']
            assert all(x[v]-x[u]<=Q(w) for u,v,w in edges)
            extended=copy.deepcopy(s);node=s['m']-1;extended['public']=sorted(set(s['public'])|{node})
            for b in extended['blocks']:b['boundary']=sorted(set(b['boundary'])|({node}&set(b['nodes'])))
            extended_summary=check(extended,e['reexposure']);live_check(extended,extended_summary,e['exposed_live'])
        else:assert e['refused_continuations']==['expose','fill'] and 'lift' not in e and 'reexposure' not in e
    # Both block states are separately feasible; only composition closes a
    # negative cycle in the designated cross-block control.
    assert all(p['status']=='CONSISTENT' for p in packets['cross-block-cycle']['certificate']['blocks'])
    rejected=[];name='chain-8-archive-backed';s=c['states'][name];base=packets[name]['certificate']
    for defect in ('boundary','history','policy','path','distance','summary'):
        bad=copy.deepcopy(base)
        if defect=='boundary':bad['state']['blocks'][0]['boundary'].remove(4)
        if defect=='history':bad['state']['blocks'][0]['evidence'].pop()
        if defect=='policy':bad['state']['retention']='public-only'
        if defect=='path':bad['blocks'][0]['paths'][0][1]=[]
        if defect=='distance':bad['blocks'][0]['distance'][0][1]='0'
        if defect=='summary':bad['summary'].pop()
        bad['state_digest']=digest(bad['state'])
        try:check(s,bad)
        except (AssertionError,ValueError,KeyError,IndexError):rejected.append(defect)
        else:raise AssertionError('bad modular certificate accepted')
    bad=copy.deepcopy(packets['cross-block-cycle']['certificate']);bad['expanded_cycle']=[]
    try:check(c['states']['cross-block-cycle'],bad)
    except AssertionError:rejected.append('negative-cycle-expansion')
    else:raise AssertionError('bad cycle accepted')
    result={'passed':True,'states':len(packets),'modular_monolithic_comparisons':len(packets),
      'public_membership_controls':16,'archive_reexposures':4,'fine_witnesses':4,'cross_block_negative_cycles':1,'local_negative_cycles':1,
      'attacks_rejected':rejected,'scope':'Raw-atom difference constraints only; live, archive and migration-proof costs remain separate.'}
    (OUT/'modular-difference-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()

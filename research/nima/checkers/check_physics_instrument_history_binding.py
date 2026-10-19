"""Full sharp-input detector histories in Fock/memory, with composition guards."""
import argparse
import copy
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
import check_physics_geometric_candidate as G
import check_physics_observation_resource_interface as O

ROOT=G.ROOT
CONTRACT='research/nima/contracts/physics-instrument-history-binding.v1.json'


def preparation(inputs,ready):
    occupancy=[0]*G.DIM
    for k,n in enumerate(inputs):occupancy[2+3*k]=n
    state={tuple(occupancy):F(1)}
    return [(w,m,state.copy()) for w,m in ((ready,'R'),(1-ready,'D')) if w]


def segment(branches,word,start=0):
    G.require(type(start) is int and 0<=start<=3 and start+len(word)<=3,'segment bin domain')
    for k,y in enumerate(word,start):
        output=[]
        for weight,memory,state in branches:
            for m,s in G.instrument(2+3*k,y,[(memory,state)]):output.append((weight,m,s))
        branches=output
    return branches


def populations(branches):
    return tuple(sum(w*G.inner(s,s) for w,m,s in branches if m==memory) for memory in ('R','D'))


def history(start,word):
    return {'source_id':'passive-port-fock-memory.v1','start':start,'end':start+len(word),
            'records':[{'bin':start+j,'port':2+3*(start+j),'outcome':y,
                        'occurrence_id':str(start+j),'memory_policy':'retain'} for j,y in enumerate(word)]}


def validate_history(h):
    G.require(h['source_id']=='passive-port-fock-memory.v1' and type(h['start']) is int
              and 0<=h['start']<=h['end']<=3,'history source/bin domain')
    G.require(h['end']-h['start']==len(h['records']),'history record coverage')
    ids=[]
    for j,r in enumerate(h['records'],h['start']):
        G.require(r['bin']==j and r['port']==2+3*j and r['outcome'] in ('C','N')
                  and r['memory_policy']=='retain' and r['occurrence_id'],'history event/identity')
        ids.append(r['occurrence_id'])
    G.require(len(ids)==len(set(ids)),'duplicate occurrences')


def join(a,b):
    validate_history(a);validate_history(b)
    G.require(a['end']==b['start'],'history attachment')
    result={'source_id':a['source_id'],'start':a['start'],'end':b['end'],'records':a['records']+b['records']}
    validate_history(result)
    return result


def main():
    p=argparse.ArgumentParser();p.add_argument('--pin',action='store_true');args=p.parse_args()
    c=G.load(CONTRACT);paths={CONTRACT}|set(c['source_evidence']);pin=ROOT/c['source_pins']
    if args.pin:
        G.require(not pin.exists(),'refusing implicit re-pin')
        pin.write_text(json.dumps({'source_sha256':{p:G.sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=G.load(c['source_pins']);G.require(set(pins['source_sha256'])==paths,'pin coverage')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source drift: '+path)
    G.require(c['decision']=='constructed_conditional_instrument_history_packet'
              and not c['physical_instrument_binding_admitted'] and not c['native_source_law_selected'],'scope promotion')
    G.require(c['source_witness_id']==G.load('research/nima/contracts/physics-geometric-candidate.v1.json')['source_id'],'source witness')
    cases=splits=prefixes=resources=0
    for ready in (F(0),F(1,2),F(1)):
        for length in range(1,4):
            for inputs in itertools.product((0,1),repeat=length):
                initial=preparation(inputs,ready);total=F(0)
                for word in itertools.product('CN',repeat=length):
                    source=(ready,1-ready);branches=initial
                    for k,(n,y) in enumerate(zip(inputs,word)):
                        source=O.step(n,y,source)
                        branches=segment(branches,(y,),k)
                        G.require(populations(branches)==source,'full memory/posterior square')
                        for _,_,s in branches:
                            for occ,a in s.items():
                                G.require(all(occ[2+3*j]==(0 if j<=k else inputs[j]) for j in range(length)),'future input changed or consumed input retained')
                        likelihood=sum(source);remaining=sum(inputs[k+1:])
                        number=sum(w*sum(sum(o)*a*a*G.weight(o) for o,a in s.items()) for w,_,s in branches)
                        G.require(number==likelihood*remaining,'spectator photon budget')
                        G.require(number+likelihood*sum(inputs[:k+1])==likelihood*sum(inputs),'absorbed photon ledger')
                        prefixes+=1;resources+=1
                    total+=sum(source);cases+=1
                    for cut in range(length+1):
                        staged=segment(segment(initial,word[:cut]),word[cut:],cut)
                        G.require(staged==branches,'segment composition')
                        G.require(join(history(0,word[:cut]),history(cut,word[cut:]))==history(0,word),'retained history composition')
                        splits+=1
                    # All three segment parenthesizations agree, including empty segments.
                    for a in range(length+1):
                        for b in range(a,length+1):
                            x,y,z=history(0,word[:a]),history(a,word[a:b]),history(b,word[b:])
                            G.require(join(join(x,y),z)==join(x,join(y,z)),'retained associativity')
                G.require(total==1,'complete word normalization')
    # This enlarges detector-only histories, NOT the cavity/detector overlap domain.
    two={G.occupation([0,1]):F(1)};mixed=G.lift_state(G.round_map(0),two)
    invalid_mass=sum(a*a*G.weight(o) for o,a in mixed.items() if o[2]>1)
    G.require(invalid_mass>0,'multiphoton cavity-interface counterexample missing')
    try:G.instrument(2,'N',[('R',mixed)])
    except ValueError:guard=True
    else:raise AssertionError('silently admitted passive-mixed multiphoton detector input')
    hostile=[]
    valid=history(0,('N','C'))
    for name in ('drop-no-click','reset-memory','duplicate-occurrence','foreign-source'):
        bad=copy.deepcopy(valid)
        if name=='drop-no-click':bad['records'].pop(0)
        elif name=='reset-memory':bad['records'][1]['memory_policy']='reset-ready'
        elif name=='duplicate-occurrence':bad['records'][1]['occurrence_id']=bad['records'][0]['occurrence_id']
        else:bad['source_id']='native-bool-square-pilot'
        try:validate_history(bad)
        except ValueError:hostile.append(name)
        else:raise AssertionError('accepted '+name)
    try:join(history(0,('N',)),history(0,('C',)))
    except ValueError:hostile.append('nonmatching-bin-attachment')
    else:raise AssertionError('bad segment attachment accepted')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source changed during check')
    out={'schema':c['schema'],'status':'pass','full_detector_histories':cases,
         'prefix_memory_squares':prefixes,'segment_composition_splits':splits,'resource_prefix_balances':resources,
         'history_associativity':True,'maximum_initial_total_photons':3,
         'passive_mixed_invalid_detector_mass':str(invalid_mass),'assembly_domain_guard':guard,
         'rejected_history_hostiles':hostile,'physical_instrument_binding_admitted':False,
         'source_sha256':pins['source_sha256'],'checker_sha256':G.sha(Path(__file__))}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()

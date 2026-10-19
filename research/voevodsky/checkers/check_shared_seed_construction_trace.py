"""Replayable record-instruction trace, NOT a physical mass-arrow identification.
No owner sources or results are rewritten. Every trace event appends one result.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from hashlib import sha256
import json,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_twelve_triangle_positive_geometry import (POINTS,LABELS,ONE,ZERO,OMEGA,mean,transpose,mm,mv,det,sub,compose,rotation,zmv,zmul,zconj,zscale,znorm,boundary)
from check_twenty_four_triangle_shared_seed import cell_boundary,surface_check
from check_collective_four_state_identity import rank

BASE='research/voevodsky/'
SPEC=BASE+'contracts/shared-seed-construction-trace.v1.json'
TRACE=BASE+'results/shared_seed_construction_trace.v1.json'
RESULT=BASE+'results/shared_seed_construction_count.v1.json'

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    return x

def digest_value(x):return sha256(json.dumps(encode(x),sort_keys=True,separators=(',',':')).encode()).hexdigest()
def file_digest(p):return sha256((ROOT/p).read_bytes()).hexdigest()

def evaluate(spec,op,args,inputs,values):
    v=[values[i] for i in inputs]
    if op=='cycle':
        cycle=args['cycle'];assert cycle in spec['cycles']
        assert all(a+b in spec['seed_arrows'] for a,b in zip(cycle,cycle[1:]+cycle[:1]))
        p=list(range(4))
        for a,b in zip(cycle,cycle[1:]+cycle[:1]):p[LABELS.index(a)]=LABELS.index(b)
        return tuple(p)
    if op=='identity':return tuple(range(4))
    if op=='product':return compose(v[0],v[1])
    if op=='group':
        assert len(v)==len(set(v));return tuple(sorted(v))
    if op=='frame_point':return tuple(map(F,spec['frame'][args['index']]))
    if op=='area_action':
        # Explicit frame is checked against the source implementation before use.
        R=rotation(v[0]);s=det(R);return tuple(tuple(s*x for x in row) for row in R)
    if op=='act_point':return mv(v[0],v[1])
    if op=='mean_point':return mean(v)
    if op=='triangle':return transpose(tuple(v))
    if op=='mode':return zmv(v[0],(ONE,OMEGA,zmul(OMEGA,OMEGA)))
    if op=='mode_norm':return sum((znorm(z) for vector in v for z in vector),F(0))
    if op=='local_entry':
        vector=v[0];return zscale(zmul(vector[args['row']],zconj(vector[args['column']])),1/sum(znorm(z) for z in vector))
    if op=='transport_entry':
        block=mm(v[0],transpose(v[1]));return block[args['row']][args['column']]/len(v[2]),F(0)
    if op=='feedback_entry':return zscale(zmul(v[0][args['row']],zconj(v[1][args['column']])),1/v[2])
    if op=='cell':
        ids=list(inputs);a,b,c,d=v;volume=det(transpose((sub(b,a),sub(c,a),sub(d,a))))/6
        assert volume!=0
        if volume<0:ids[2],ids[3]=ids[3],ids[2];volume=-volume
        return {'vertices':ids,'volume':volume}
    if op=='empty_assembly':return {'chain':[],'volume':F(0),'cells':[]}
    if op=='attach_cell':
        state,cell=v;chain=Counter({tuple(face):n for face,n in state['chain']});bd=cell_boundary(tuple(cell['vertices']))
        if state['cells']:assert any(chain.get(f,0)==-n for f,n in bd.items())
        for face,n in bd.items():chain[face]+=n
        surface_check(chain)
        return {'chain':[[list(f),n] for f,n in sorted(chain.items()) if n], 'volume':state['volume']+cell['volume'],'cells':state['cells']+[inputs[1]]}
    if op=='comparison_graph':
        group=v[0];index={p:i for i,p in enumerate(group)};edges=set()
        for i,p in enumerate(group):
            for g in v[1:]:
                j=index[compose(g,p)]
                if i!=j:edges.add(tuple(sorted((i,j))))
        degree=[sum(i in e for e in edges) for i in range(len(group))]
        return {'edges':sorted(edges),'degree':degree,'denominator':max(degree)+1}
    if op=='comparison_entry':
        graph=v[0];i,j=args['row'],args['column'];den=graph['denominator']
        return F(1)-F(graph['degree'][i],den) if i==j else F(int(tuple(sorted((i,j))) in graph['edges']),den)
    raise ValueError('unknown primitive: '+op)

class Trace:
    def __init__(self,spec):self.spec=spec;self.events=[];self.values=[];self.head=digest_value(spec)
    def add(self,op,inputs=(),**args):
        assert all(0<=i<len(self.values) for i in inputs)
        value=evaluate(self.spec,op,args,inputs,self.values)
        event={'index':len(self.values),'op':op,'inputs':list(inputs),'args':args,'result':encode(value),'previous':self.head}
        self.head=digest_value(event);event['hash']=self.head
        self.events.append(event);self.values.append(value)
        return len(self.values)-1

def replay(spec,events):
    t=Trace(spec)
    for event in events:
        assert event['index']==len(t.events) and event['previous']==t.head
        index=t.add(event['op'],event['inputs'],**event['args'])
        assert t.events[index]==event,'changed result, dependency, order or chain'
    return t

def compile_trace(spec):
    assert spec['objects']==list(LABELS)
    assert [list(map(F,p)) for p in spec['frame']]==[list(POINTS[k]) for k in LABELS]
    t=Trace(spec);frame=[t.add('frame_point',index=i) for i in range(4)]
    gens=[t.add('cycle',cycle=c) for c in spec['cycles']];identity=t.add('identity')
    seen={t.values[identity]:identity};queue=[identity]
    for p in queue:
        for g in gens:
            q=t.add('product',(g,p));value=t.values[q]
            if value not in seen:seen[value]=q;queue.append(q)
    group=t.add('group',[seen[p] for p in sorted(seen)]);perms=t.values[group]
    actions=[t.add('area_action',(seen[p],)) for p in perms]
    action_by_perm=dict(zip(perms,actions))
    ident_action=action_by_perm[tuple(range(4))];swap_action=action_by_perm[t.values[gens[2]]]
    body={};coordinates={}
    for action in (ident_action,swap_action):
        for point in frame:
            record=t.add('act_point',(action,point));coordinates[t.values[record]]=record
    for s in (1,-1):
        for k,point in zip(LABELS,frame):body[s,k]=coordinates[tuple(s*x for x in t.values[point])]
    faces={}
    for s in (1,-1):
        for face in combinations(LABELS,3):faces[s,face]=t.add('mean_point',[body[s,k] for k in face])
    triangles=[];modes=[];signs=[]
    for p in perms:
        sign=int(det(rotation(p)));a,b,c=(LABELS[p[i]] for i in range(3));signs.append(sign)
        tri=t.add('triangle',(faces[sign,tuple(sorted((a,b,c)))],body[sign,a],body[sign,b]))
        triangles.append(tri);modes.append(t.add('mode',(tri,)))
    norm=t.add('mode_norm',modes)
    dense=[]
    for g,vector in enumerate(modes):
        for row in range(3):
            for column in range(3):dense.append((0,3*g+column,3*g+row,t.add('local_entry',(vector,),row=row,column=column)))
    for g in range(len(perms)):
        for h in range(len(perms)):
            for row in range(3):
                for column in range(3):
                    dense.append((1,3*h+column,3*g+row,t.add('transport_entry',(actions[g],actions[h],group),row=row,column=column)))
                    dense.append((2,3*h+column,3*g+row,t.add('feedback_entry',(modes[g],modes[h],norm),row=row,column=column)))
    center=t.add('mean_point',frame);midpoints={}
    for i,j in combinations(range(4),2):
        record=t.add('mean_point',(frame[i],frame[j]));midpoints[t.values[record]]=record
    gray=((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,-1,1),(-1,-1,-1),(-1,1,-1),(-1,1,1))
    core=[];tips={1:[],-1:[]}
    for s in gray:
        base=[midpoints[tuple(F(s[i] if j==i else 0) for j in range(3))] for i in range(3)]
        core.append(t.add('cell',[center]+base))
        tips[s[0]*s[1]*s[2]].append(t.add('cell',[coordinates[tuple(map(F,s))]]+base))
    state=t.add('empty_assembly')
    for cell in core+tips[1]+tips[-1]:state=t.add('attach_cell',(state,cell))
    graph=t.add('comparison_graph',[group]+gens);comparison=[]
    for i in range(len(perms)):
        for j in range(len(perms)):comparison.append((i,j,t.add('comparison_entry',(graph,),row=i,column=j)))
    return t,{'group':group,'triangles':triangles,'modes':modes,'norm':norm,'dense':dense,'assembly':state,'graph':graph,'comparison':comparison,'signs':signs}

def verify_endpoint(t,refs):
    group=t.values[refs['group']];assert len(group)==24 and t.values[refs['norm']]==160
    matrices=[[[ZERO for _ in range(72)] for _ in range(72)] for _ in range(3)];counts=Counter();parts=Counter()
    for stage,src,dst,record in refs['dense']:
        value=t.values[record];matrices[stage][dst][src]=value
        if value!=ZERO:
            counts[stage]+=1;parts['cross' if refs['signs'][src//3]!=refs['signs'][dst//3] else str(refs['signs'][src//3])]+=1
    assert [counts[i] for i in range(3)]==[216,1728,5184]
    assert parts=={'1':1836,'-1':1836,'cross':3456}
    # Exact independent block compositions GL=LG=N, including all zero entries.
    from check_twelve_triangle_positive_geometry import zmm
    for g in range(24):
        for h in range(24):
            block=lambda stage,a,b:tuple(tuple(matrices[stage][3*a+i][3*b+j] for j in range(3)) for i in range(3))
            assert zmm(block(1,g,h),block(0,h,h))==block(2,g,h)
            assert zmm(block(0,g,g),block(1,g,h))==block(2,g,h)
    assembly=t.values[refs['assembly']];assert assembly['volume']==4 and len(assembly['chain'])==24 and len(assembly['cells'])==16
    geom=set()
    for cell in assembly['cells']:
        ids=t.values[cell]['vertices'];geom.update((i,j) for i in ids for j in ids if i!=j)
    assert len(geom)==84
    sparse={(i,j):t.values[r] for i,j,r in refs['comparison'] if t.values[r]!=0}
    assert len(sparse)==144 and sum(i!=j for i,j in sparse)==120
    graph=t.values[refs['graph']];L=[[F(0)]*24 for _ in range(24)]
    for i,j in graph['edges']:L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    assert rank(L)==23
    return {'dense_stage_counts':[counts[i] for i in range(3)],'dense_arrows':sum(counts.values()),'dense_partition':dict(parts),'geometric_directed_edges':len(geom),'comparison_arrows_with_loops':len(sparse),'comparison_nonself_arrows':120,'positive_cells':16,'union_volume':'4','coupled_identity_dimension':1}

def validate_packet(packet):
    spec=json.loads((ROOT/SPEC).read_text())
    assert packet['schema']=='marici.voevodsky.record-instruction-trace.v1'
    assert packet['spec_sha256']==file_digest(SPEC)
    for p,h in packet['source_hashes'].items():assert file_digest(p)==h,p
    replayed=replay(spec,packet['events'])
    canonical,refs=compile_trace(spec)
    # Valid prefixes and alternative schedules are not complete canonical runs.
    assert packet['events']==canonical.events and packet['endpoint_refs']==encode(refs)
    assert packet['final_configuration_hash']==replayed.head==canonical.head
    return verify_endpoint(replayed,refs)

def main():
    spec=json.loads((ROOT/SPEC).read_text())
    for p,h in spec['source_hashes'].items():assert file_digest(p)==h,p
    t,refs=compile_trace(spec);endpoint=verify_endpoint(t,refs)
    replayed=replay(spec,t.events);assert replayed.head==t.head and replayed.values==t.values
    # Endpoint compatibility is checked only after construction, never used as input.
    old=json.loads((ROOT/'research/nima/results/pair-arrow-ledger.json').read_text())
    assert old['dense_1836_convention']['unique_arrows']==endpoint['dense_arrows']
    sources=dict(spec['source_hashes'])
    for p in (SPEC,BASE+'checkers/check_shared_seed_construction_trace.py','research/nima/checkers/check_triangle_half_phase.py','research/nima/checkers/check_collective_four_state_identity.py','research/nima/results/pair-arrow-ledger.json'):sources[p]=file_digest(p)
    packet={'schema':'marici.voevodsky.record-instruction-trace.v1','spec_sha256':file_digest(SPEC),'events':t.events,'endpoint_refs':refs,'final_configuration_hash':t.head,'source_hashes':sources}
    (ROOT/TRACE).write_text(json.dumps(packet,separators=(',',':'))+'\n')
    counts=Counter(e['op'] for e in t.events)
    report={'schema':'marici.voevodsky.shared-seed-construction-count.v1','verification_passed':True,'seed_id':spec['seed_id'],
        'configuration_transition_count':len(t.events),'visited_configuration_count':len(t.events)+1,'instruction_counts':dict(sorted(counts.items())),
        'initial_seed_arrows':len(spec['seed_arrows']),'initial_seed_is_supplied_not_executed':True,'endpoint_counts':endpoint,
        'evaluated_dense_coefficients':len(refs['dense']),'retained_dense_zero_results':len(refs['dense'])-endpoint['dense_arrows'],
        'evaluated_comparison_coefficients':len(refs['comparison']),'retained_comparison_zero_results':len(refs['comparison'])-len({(i,j) for i,j,r in refs['comparison'] if t.values[r]!=0}),
        'counting_unit':spec['counting_unit'],'scalar_arithmetic_counted':False,'primitive_mass_arrow_identification':None,'physical_mass_count_admitted':False,
        'trace':{'path':TRACE,'sha256':file_digest(TRACE),'final_configuration_hash':t.head},'source_hashes':sources,
        'scope':'Complete execution of the declared record-instruction grammar from supplied seed/frame/area/phase rules. Not a count derived from six bare arrows, not minimality, and not the mass-arrow count without a primitive-identity comparison.'}
    (ROOT/RESULT).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'record_instruction_transitions':len(t.events),'instruction_counts':dict(sorted(counts.items())),'endpoint':endpoint,'physical_mass_count_admitted':False},indent=2))

if __name__=='__main__':main()

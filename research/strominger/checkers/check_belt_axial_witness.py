"""A source-axis constructor and retained belt WG relation (exact arithmetic)."""
from copy import deepcopy
from itertools import product
import hashlib,json
from pathlib import Path
from check_belt_directed_incidence import (ROOT,BASE,F,read,hashes,mean,sub,dot,cross,sign,parity,addcell,clean,boundary,push,enc)
from assemble_real_complex_arrows import decode

def mv(a,x):return tuple(sum(v*w for v,w in zip(row,x)) for row in a)
def mm(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def add(*aa):return tuple(tuple(sum(a[i][j] for a in aa) for j in range(3)) for i in range(3))
def scale(q,a):return tuple(tuple(q*x for x in row) for row in a)
def rank(a):
    a=[list(r) for r in a];r=0
    for j in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][j]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];v=a[r][j];a[r]=[x/v for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                q=a[i][j];a[i]=[x-q*y for x,y in zip(a[i],a[r])]
        r+=1
    return r
I=tuple(tuple(F(i==j) for j in range(3)) for i in range(3))

def prepare(points,faces,axis):
    """The actual computation, independent of the desired branch store."""
    signs=[];chain={}
    from collections import defaultdict
    chain=defaultdict(int)
    for face in faces:
        a,b,c=[points[k] for k in face]
        beta=-dot(axis,cross(sub(b,a),sub(c,a)))
        if beta==0:raise ValueError('axis tangent to face: orientation undefined')
        s=sign(beta);signs.append(s);addcell(chain,('O',)+tuple(face),s)
    chain=clean(chain)
    return {'axis':axis,'signs':tuple(signs),'chain':chain,'boundary':boundary(chain),'history':()}

def valid_state(state,points,faces):
    expected=prepare(points,faces,state['axis'])
    return all(state[k]==expected[k] for k in ('signs','chain','boundary'))

def generate(request):
    """G(request)=(output,witness) for the explicitly declared relation."""
    output=prepare(request['points'],request['faces'],request['axis'])
    witness={'request':deepcopy(request),'output':deepcopy(output)}
    return output,witness

def verify_generation(request,output,w):
    return w['request']==request and w['output']==output and output==prepare(request['points'],request['faces'],request['axis'])

def step(state,perm,operation):
    out=deepcopy(state);out['chain']=push(state['chain'],perm);out['boundary']=push(state['boundary'],perm)
    # This instance's rotation fixes the axis and its induced face-sign field.
    out['history']=state['history']+(operation,)
    witness={'input':deepcopy(state),'output':deepcopy(out),'vertex_map':dict(perm),'operation':operation}
    return out,witness

def verify_step(a,b,w,perm,operation):
    if w!={'input':a,'output':b,'vertex_map':perm,'operation':operation}:return False
    return (b['axis']==a['axis'] and b['signs']==a['signs'] and
        b['chain']==push(a['chain'],perm) and b['boundary']==push(a['boundary'],perm) and
        b['boundary']==boundary(b['chain']) and b['history']==a['history']+(operation,))

def main():
    read('research/strominger/inputs/belt-axial-witness-protocol-v1.json')
    source=read('research/strominger/inputs/neutron-real-complex-arrows.json')
    geom=read('research/voevodsky/results/four_six_center_cones.json')
    decoded,pts,_=decode(source);R=tuple(tuple(map(F,row)) for row in decoded['generators'][0]['matrix'])
    assert mm(mm(R,R),R)==I
    P=scale(F(1,3),add(I,R,mm(R,R)))
    assert mm(P,P)==P and mm(R,P)==P and rank(P)==1 and rank(add(R,scale(-1,I)))==2
    seeds=[pts[s['vertex']] for s in source['seeds']]
    centers=[mv(P,s) for s in seeds]
    assert centers==[mean([mv(M,s) for M in (I,R,mm(R,R))]) for s in seeds]
    sourceaxis=sub(centers[1],centers[0]);assert sourceaxis!=(0,0,0) and mv(R,sourceaxis)==sourceaxis
    convert=lambda p:(p[2],p[0],p[1])
    axis=convert(sourceaxis);points={k:tuple(map(F,v)) for k,v in geom['belt_scaled_coordinates'].items()};faces=geom['belt_faces']
    request={'points':points,'faces':faces,'axis':axis,'axis_provenance':{'projection':P,'ordered_seeds':source['seeds'],'centers':centers}}
    state,w=generate(request);assert verify_generation(request,state,w) and valid_state(state,points,faces)
    target=read('research/voevodsky/results/opposite_branch_belt_store.json')
    assert state['signs']==tuple(target['face_signs'])
    reverse_request=deepcopy(request);reverse_request['axis']=tuple(-x for x in axis)
    reverse_request['axis_provenance']['ordered_seeds']=list(reversed(source['seeds']))
    reverse_request['axis_provenance']['centers']=list(reversed(centers))
    opposite,_=generate(reverse_request)
    assert opposite['signs']==tuple(-s for s in state['signs'])
    assert opposite['chain']=={k:-v for k,v in state['chain'].items()}
    # Coordinate covariance for a nonorthogonal positive-determinant chart:
    # det(S)=1 and the volume contraction, not Euclidean normal coordinates,
    # is the operation under test.
    S=((F(1),F(2),F(0)),(F(0),F(1),F(1)),(F(0),F(0),F(1)))
    changed=prepare({k:mv(S,v) for k,v in points.items()},faces,mv(S,axis))
    assert changed['signs']==state['signs'] and changed['chain']==state['chain']
    # The source's actual C3 action in the stored chart.
    lookup={v:k for k,v in points.items()}
    perm={k:lookup[convert(mv(R,(v[1],v[2],v[0])))] for k,v in points.items()}
    inverse={v:k for k,v in perm.items()}
    traces=[];s=state
    for i in range(3):
        t,ww=step(s,perm,'native_C3');assert verify_step(s,t,ww,perm,'native_C3') and valid_state(t,points,faces)
        traces.append(ww);s=t
    assert s['chain']==state['chain'] and len(s['history'])==3 and s!=state
    # Based backward action preserves chronology; it is not history erasure.
    t,back=step(s,inverse,'native_C3_inverse');assert verify_step(s,t,back,inverse,'native_C3_inverse')
    assert push(push(state['chain'],perm),inverse)==state['chain']
    assert traces[0]['input']==state
    owners={}
    from itertools import combinations
    for i,f in enumerate(faces):
        for face in combinations(('O',)+tuple(f),3):owners.setdefault(tuple(sorted(face)),[]).append(i)
    internal={k for k,v in owners.items() if len(v)==2}
    defects={k:v for k,v in state['boundary'].items() if k in internal}
    outer={k:v for k,v in state['boundary'].items() if k not in internal}
    defect_edges=boundary(defects)
    assert len(defects)==6 and defect_edges and boundary(outer)=={k:-v for k,v in defect_edges.items()}
    assert boundary(state['boundary'])=={}
    # No 3-chain can have boundary exactly the internal record alone:
    # its boundary is nonzero. An isolated internal-face filler would violate d²=0.
    bad=deepcopy(state);bad['boundary']=outer
    badw=deepcopy(w);badw['output']=bad
    assert not verify_generation(request,bad,badw)
    badstep=deepcopy(traces[0]);badstep['output']['boundary']=outer
    assert not verify_step(state,badstep['output'],badstep,perm,'native_C3')
    badhistory=deepcopy(traces[0]);badhistory['output']['history']=()
    assert not verify_step(state,badhistory['output'],badhistory,perm,'native_C3')
    checks={'fixed_axis_derived_from_native_C3':True,'ordered_source_seeds_determine_directed_axis':True,
      'axial_rule_generates_actual_target_signs':True,'seed_order_reversal_exchanges_branches':True,
      'positive_chart_covariance':True,'request_output_witness_verified':True,'retained_C3_transition_witnesses_verified':True,
      'three_step_return_retains_nonempty_history':True,'defect_deletion_and_history_erasure_rejected':True,
      'internal_defect_alone_is_not_a_cycle':True}
    for p in [Path(__file__),BASE/'checkers/check_belt_directed_incidence.py',BASE/'checkers/assemble_real_complex_arrows.py',ROOT/'research/nima/agda/TypedGeneratorLayers.agda']:
        hashes[p.relative_to(ROOT).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    for path,h in hashes.items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h
    out=BASE/'results/belt-axial-witness';out.mkdir(parents=True,exist_ok=True)
    def packet(x):
        return {'axis':list(map(str,x['axis'])),'signs':list(x['signs']),
                'chain':enc(x['chain']),'boundary':enc(x['boundary']),'history':list(x['history'])}
    retained={'request':{'points':{k:list(map(str,v)) for k,v in points.items()},'faces':faces,
                'axis':list(map(str,axis)),'ordered_seeds':source['seeds'],
                'seed_centers':[list(map(str,c)) for c in centers],
                'projection':[[str(v) for v in row] for row in P]},
              'generated_output':packet(state),
              'steps':[{'input':packet(t['input']),'output':packet(t['output']),
                        'vertex_map':t['vertex_map'],'operation':t['operation']} for t in traces+[back]]}
    (out/'witnesses.json').write_text(json.dumps(retained,indent=2)+'\n')
    result={'status':'pass','checks':checks,'source_hashes':hashes,'fixed_projection':[[str(v) for v in row] for row in P],
      'seed_centers':[list(map(str,c)) for c in centers],'axis_in_belt_chart':list(map(str,axis)),'signs':list(state['signs']),
      'signed_chain':enc(state['chain']),'complete_boundary':enc(state['boundary']),'internal_defects':enc(defects),
      'boundary_of_internal_defects':enc(defect_edges),'native_vertex_map':perm,
      'retained_transition_history':list(s['history']),
      'disposition':{'constructed':'Executable request/output witness and belt-native retained C3 transitions in the generic WG pattern',
      'not_constructed':'Agda formalization or an adapter from the distinct four-vertex Boolean seed WG',
      'remaining_rule':'Use the fixed-axis contraction rather than radial contraction; ordered seed roles select the sign, not the unpointed C3 action',
      'filling_obstruction':'Internal residual is not closed; it cannot alone be the boundary of an added 3-chain. Outer boundary or other interface data must change for cancellation.'}}
    (out/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','checks':len(checks),'axis':list(map(str,axis)),'signs':list(state['signs']),'internal_defect_boundary_edges':len(defect_edges),'history_length':len(s['history'])}))
if __name__=='__main__':main()

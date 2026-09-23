"""Separate persistent refinement, saturation and source-lift equality."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
import json,gzip,hashlib
from check_symbolic_tail_interface import Generator,RetainedInterface
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def image(t):return sum(t),sum(v*Q(1,128**j) for j,v in enumerate(t))
def decode(m,l):
    k=l['high_prefix'];h=Q(l['high_partial']);j=l['complement_prefix'];r=Q(l['complement_partial']);theta=Q(l['theta']);out=[]
    for n in range(m):
        cap=Q(100+2*n);high=cap if n<k else h if n==k else Q(0);comp=cap if n<j else r if n==j else Q(0)
        out.append((1-theta)*(cap-comp)+theta*high)
    return tuple(out)
def main():
    engine=Path(__file__).with_name('check_symbolic_tail_interface.py');own=OUT/'symbolic-tail-interface.json'
    contract={'schema':'symbolic-interface-coherence-levels-v1','engine_sha256':sha(engine),'owning_report_sha256':sha(own),
      'frame_family':['U<=50','U>=25','V<=U/2'],'orders':'all six permutations',
      'objectives':[['0','1'],['1','0'],['-1','0'],['1','-1']],'m_values':[2,3,16,64,1024],
      'saturation_control':'At m=3 use (0,128^-2,0), (128^-2,0,0), (0,0,1). Test the missing reverse middle by the source support oracle.',
      'lift_control':'At m=3 compare the engine lift at the midpoint of 0 and the first-two-full source image with the midpoint of the endpoint source lifts.',
      'claim':'Exact refinement answers compose. This does not assert permutability of observation kernels, source-lift equality across arbitrary constructions, or braid coherence.',
      'scope':'Owning normalized tail-face possibilities and fixed query semantics; no physical reverse execution or new source identity structure.'}
    cp=OUT/'symbolic-interface-coherence-levels-contract.json';save(cp,contract)
    frames=[((Q(1),Q(0)),Q(50)),((Q(-1),Q(0)),Q(-25)),((-Q(1,2),Q(1)),Q(0))]
    queries=[];groups=[]
    for m in contract['m_values']:
        for objective in map(lambda x:tuple(map(Q,x)),contract['objectives']):
            group=[];baseline=None
            for order in permutations(range(3)):
                state=RetainedInterface(m);snapshots=[state]
                for i in order:state=state.refine(*frames[i]);snapshots.append(state)
                assert [len(s.frames) for s in snapshots]==[0,1,2,3]
                answer=state.maximize(objective);assert answer['status']=='OPTIMAL'
                signature=(answer['point'],answer['value'],answer['lift'])
                if baseline is None:baseline=signature
                else:assert signature==baseline
                group.append(len(queries));queries.append({'m':m,'order':list(order),'frames':[{'a':list(map(str,a)),'b':str(b)} for a,b in state.frames],
                    'objective':list(map(str,objective)),'result':answer})
            groups.append(group)
    model=Generator(3);a=Q(1,128**2)
    start=(Q(0),a,Q(0));middle=(a,Q(0),Q(0));end=(Q(0),Q(0),Q(1))
    for t in (start,middle,end):assert all(0<=v<=100+2*j for j,v in enumerate(t))
    assert image(start)[0]==image(middle)[0] and image(middle)[1]==image(end)[1]
    reverse=(image(end)[0],image(start)[1]);denied=model.member(reverse)
    assert not denied['admitted']
    # Greedy certificate selection is not an affine transport of source lifts.
    left=(Q(0),)*3;right=(Q(100),Q(102),Q(0));visible=tuple((x+y)/2 for x,y in zip(image(left),image(right)))
    selected=model.member(visible);assert selected['admitted'];canonical=decode(3,selected['lift'])
    interpolated=tuple((x+y)/2 for x,y in zip(left,right))
    assert image(canonical)==image(interpolated)==visible and canonical!=interpolated
    assert canonical[2]>0 and interpolated[2]==0
    packet={'queries':queries,'order_groups':groups,
      'saturation_diamond':{'m':3,'start':list(map(str,start)),'middle':list(map(str,middle)),'end':list(map(str,end)),
        'reverse_middle_observables':list(map(str,reverse)),'reverse_membership':denied},
      'lift_routes':{'m':3,'left':list(map(str,left)),'right':list(map(str,right)),
        'observable_midpoint':list(map(str,visible)),'direct_certificate':selected,
        'direct_source_lift':list(map(str,canonical)),'interpolated_source_lift':list(map(str,interpolated)),
        'separating_undeclared_audit':'t_2<=0 (zero-based atom index 2)','not_a_braid_claim':True}}
    pp=OUT/'symbolic-interface-coherence-levels-packet.json.gz';pp.write_bytes(gzip.compress(json.dumps(packet,separators=(',',':')).encode(),mtime=0))
    result={'verdict':'REFINEMENT_EXACTNESS_SEPARATED_FROM_SATURATION_AND_LIFT_TRANSPORT',
      'contract_sha256':sha(cp),'packet_sha256':sha(pp),'exact_refinement_queries':len(queries),'order_groups':len(groups),
      'saturation_reverse_fiber':'EMPTY_WITH_SOURCE_SEPARATOR','source_lift_routes':'SAME_OBSERVABLE_POINT_DIFFERENT_ADMITTED_SOURCE_WITNESSES',
      'boundary':'The fixed engine selector agrees across these frame permutations. Other equally valid witness constructions need not agree; no witness-space interchange or braid coherence is inferred.',
      'scope':contract['scope']}
    save(OUT/'symbolic-interface-coherence-levels.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()

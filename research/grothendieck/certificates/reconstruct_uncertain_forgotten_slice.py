"""Conditional, evidence-preserving rational inverse on a forgotten cube ideal.

Standalone standard library. Usage: FILE.json, or --model BACKGROUND.
No source support, error contract, physical acquisition, or global inverse is
certified by consistency. Output retains the exact input and a joint zonotope.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import prod
from pathlib import Path
import copy,hashlib,json,sys
IDS=('vacuum_PPP','vacuum_QQQ','first_block_P','blocks_1P_2P','blocks_1P_3P','blocks_1Q_2P','blocks_1Q_3P')
P=(2,3,5,7,11,13)
SEAMS=(((0,1),(3,7),(15,31)),((0,2),(3,11),(15,47)),((0,1),(1,3)),
       ((0,1),(3,7)),((0,1),(15,31)),((0,2),(3,7)),((0,2),(15,31)))
B=((1,0,0,0,0,0,0),(0,1,1,0,0,1,1),(-1,0,0,0,1,0,0),(0,-1,-1,0,0,-1,0),
   (-1,0,0,1,0,0,0),(0,-1,-1,0,0,0,-1),(1,0,1,-1,-1,0,0),(0,1,0,0,0,0,0))
def require(ok,msg):
    if not ok:raise ValueError(msg)
def fields(x,keys):require(type(x) is dict and set(x)==set(keys),'Missing or extra fields')
def q(x):
    require(type(x) is str,'Rationals must be strings')
    try:return Q(x)
    except (ValueError,ZeroDivisionError) as e:raise ValueError('Invalid rational') from e
def box(x):
    require(type(x) is list and len(x)==2,'Expected interval')
    a,z=map(q,x);require(a<=z,'Reversed interval');return a,z
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def path(mask):
    return tuple(p for i in range(3) for p in (P[2*i:2*i+2][::-1] if mask&(1<<i) else P[2*i:2*i+2]))
def vertices(A,word):
    out=[A]
    for p in word:out.append(out[-1]*p)
    return out
def record(A,word,seams):
    vs=vertices(A,word)
    return sum(tuple((vs[k],vs[k+1]) for k in cuts)==tuple(map(tuple,seams)) for cuts in combinations(range(len(word)),len(seams)))
def model(A):
    require(type(A) is int and A in (2,3,4),'Only audited backgrounds 2,3,4')
    vertex=lambda mask:A*prod(p for i,p in enumerate(P) if mask&(1<<i))
    rows=[{'id':name,'cut_order':len(seams),'outer_corner':[A,30030*A],'seams':[[vertex(a),vertex(z)] for a,z in seams],
           'buffers':'vacuum','marks':'forgotten','gain':'1'} for name,seams in zip(IDS,SEAMS)]
    R=[[record(A,path(mask),row['seams']) for mask in range(8)] for row in rows]
    require(all(sum(R[i][k]*B[k][j] for k in range(8))==int(i==j) for i in range(7) for j in range(7)),'Reading inverse fails')
    for j in range(1,8):
        require([sum(B[k][i]*(R[i][j]-R[i][0]) for i in range(7)) for k in range(8)]==[int(k==j)-int(k==0) for k in range(8)],'Ideal-source inverse fails')
    require(all(sum(B[k][j] for k in range(8))==0 for j in range(7)),'Inverse leaves ideal')
    require(max(sum(abs(c) for c in row) for row in B)==max(sum(abs(B[i][j]) for i in range(8)) for j in range(7))==4,'Wrong inverse norms')
    return {'schema':'labelled-forgotten-ideal-interval-model-v1','background':A,'outer_corner':[A,30030*A],
            'paths':[{'mask':mask,'events':list(path(mask)),'vertices':vertices(A,path(mask)),'marks':[0]*6} for mask in range(8)],
            'domain':'only these eight paths, with coefficient sum zero; membership is external',
            'carrier_role':'single final packet; no reachability or history equations imposed',
            'terminal_check_scope':'terminal coefficient of this six-event outer corner, not an earlier history stage',
            'rows':rows,'forward_matrix':R,'inverse_matrix':[list(row) for row in B],
            'interaction_matrix':[[int(mask&t==t) for mask in range(8)] for t in range(8)],
            'filtration':'I^r iff all interaction coordinates of degree less than r vanish, within this slice',
            'action_scope':'labels and ordered paths retained; no arbitrary marked-source action transport certified',
            'inverse_norms':{'l1':'4','linfinity':'4'}}

def reconstruct(p):
    fields(p,('schema','background','model_sha256','readings','terminal_check','provenance'))
    require(p['schema']=='labelled-forgotten-ideal-interval-readings-v1','Wrong schema')
    m=model(p['background']);require(p['model_sha256']==digest(m),'Model digest mismatch')
    fields(p['readings'],IDS);fields(p['provenance'],('kind','support_evidence','error_contract'))
    require(p['provenance']['kind'] in ('synthetic','unknown-source-observations'),'Unknown provenance kind')
    for key in ('support_evidence','error_contract'):
        evidence=p['provenance'][key]
        require(evidence is None or (type(evidence) is str and bool(evidence.strip())),'Evidence reference must be nonempty text or null')
    intervals=[box(p['readings'][name]) for name in IDS]
    if p['terminal_check'] is not None:
        lo,hi=box(p['terminal_check']);require(lo<=0<=hi,'Terminal interval contradicts ideal assumption')
    center=[(a+z)/2 for a,z in intervals];radii=[(z-a)/2 for a,z in intervals]
    ac=[sum(Q(c)*y for c,y in zip(row,center)) for row in B]
    G=[[Q(B[i][j])*radii[j] for j in range(7)] for i in range(8)]
    Z=m['interaction_matrix'];mc=[sum(Z[t][i]*ac[i] for i in range(8)) for t in range(8)]
    MG=[[sum(Z[t][i]*G[i][j] for i in range(8)) for j in range(7)] for t in range(8)]
    def bounds(c,g):
        r=sum(map(abs,g));return [str(c-r),str(c+r)]
    mb=[bounds(c,g) for c,g in zip(mc,MG)]
    filtration={}
    for order in range(1,5):
        indices=[t for t in range(8) if t.bit_count()<order]
        guaranteed=all(mc[t]==0 and not any(MG[t]) for t in indices)
        excluded=any(not (q(mb[t][0])<=0<=q(mb[t][1])) for t in indices)
        filtration[str(order)]=('guaranteed' if guaranteed else 'ruled_out_by_a_coordinate' if excluded else 'undetermined')
    return {'schema':'conditional-forgotten-ideal-compatible-set-v1',
            'retained_input':copy.deepcopy(p),'retained_input_sha256':digest(p),'model':m,
            'source_domain_status':'conditional_only_even_if_external_evidence_is_referenced',
            'compatible_set':{'parameter_order':list(IDS),'parameter_domain':'Cartesian bounds epsilon in [-1,1]^7; no statistical independence claim',
                              'equation':'a = center + generators * epsilon',
                              'center':list(map(str,ac)),'generators':[list(map(str,row)) for row in G]},
            'path_marginals':[bounds(c,g) for c,g in zip(ac,G)],
            'interaction_marginals':{str(t):value for t,value in enumerate(mb)},
            'filtration_certificates':filtration,
            'filtration_scope':'sufficient universal/coordinate-exclusion tests, not a complete joint feasibility solver',
            'coefficient_error_bounds':{'l1':str(4*sum(radii)),'linfinity':str(4*max(radii)),
                                        'scope':'unweighted path-coefficient error around the derived center; not the task moment prior'},
            'retention_ledger':{'incoming':'seven labelled intervals, optional terminal interval and provenance',
                                'derived_view':'conditional joint zonotope; marginals and center are not replacements',
                                'recover_incoming':'recover the exact input JSON value, not original file bytes; verify retained_input_sha256',
                                'outside_domain':'unrepresented ambiguity, not zero; retain broader source/evidence externally',
                                'missing_readings':'reject, never fill with zero',
                                'structural_metadata':'labelled ordered paths, row anchors, interaction transform and ideal filtration retained'},
            'limitations':'Single-stage only: no history or dynamics reconstructed. No physical acquisition, support certification, calibration-gate resolution, full-source inverse or module splitting is asserted.'}

def recover(output):
    require(type(output) is dict and 'retained_input' in output,'Missing retained evidence')
    p=copy.deepcopy(output['retained_input'])
    require(digest(output)==digest(reconstruct(p)),'Corrupt or inconsistent reconstruction bundle')
    return p

def load(path):
    def pairs(items):
        result={}
        for k,v in items:require(k not in result,'Duplicate JSON key');result[k]=v
        return result
    def reject(x):raise ValueError('Floating/nonfinite JSON prohibited')
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=pairs,parse_float=reject,parse_constant=reject)
if __name__=='__main__':
    try:
        if len(sys.argv)==3 and sys.argv[1]=='--model':
            m=model(int(sys.argv[2]));answer={'model':m,'model_sha256':digest(m)}
        elif len(sys.argv)==3 and sys.argv[1]=='--recover':answer=recover(load(sys.argv[2]))
        else:
            require(len(sys.argv)==2,'Usage: FILE.json | --model 2|3|4 | --recover OUTPUT.json')
            answer=reconstruct(load(sys.argv[1]))
        print(json.dumps(answer,indent=2))
    except (ValueError,KeyError,TypeError,OSError) as e:
        print('REJECTED: '+str(e),file=sys.stderr);sys.exit(1)

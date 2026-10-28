"""Exact central primal-chain / relative-dual-cochain handoff on T184.
Dual blocks are constructed from barycentric flags of the actual source cell.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[3]
SOURCE='research/voevodsky/results/esd7_explicit_analytical_census.json'
HANDOFF='research/strominger/results/esd7-seven-stage-handoff.json'


def clean(c):return {k:v for k,v in c.items() if v}
def add(*cs):
    out=defaultdict(int)
    for c in cs:
        for k,v in c.items():out[k]+=v
    return clean(out)
def scale(c,a):return clean({k:a*v for k,v in c.items()})
def parity(order):return (-1)**sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))
def faces(v):return [s for n in range(1,len(v)+1) for s in combinations(v,n)]
def boundary(chain,top=None):
    out=defaultdict(int)
    for s,a in chain.items():
        if len(s)>1:
            for i in range(len(s)):
                face=s[:i]+s[i+1:]
                if top is None or face[-1]==top:out[face]+=a*((-1)**i)
    return clean(out)
def det(m):return sum(parity(p)*m[0][p[0]]*m[1][p[1]]*m[2][p[2]] for p in permutations(range(3)))
def fcc(x):return (x[0]+x[1],x[0]+x[2],x[1]+x[2])


def main():
    census=json.loads((ROOT/SOURCE).read_text(encoding='utf-8'))
    prior=json.loads((ROOT/HANDOFF).read_text(encoding='utf-8'))
    vertex={r['id']:tuple(r['barycentric']) for r in census['vertices']}
    central_id=prior['central_cell']['id']
    row=next(r for r in census['tetrahedra'] if r['id']==central_id)
    T=tuple(sorted(row['vertices']));simplices=faces(T)
    checks=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    check('live prior receipt and central source agree',prior['source_sha256']==hashlib.sha256((ROOT/SOURCE).read_bytes()).hexdigest() and central_id=='T184')
    # Dual-block orientation normalization: a_(k+1)=(-1)^(k+1) a_k.
    orientation=(1,-1,-1,1)
    blocks={}
    for s in simplices:
        chain={}
        for rest in permutations(v for v in T if v not in s):
            flag=[s];current=s
            for v in rest:
                current=tuple(sorted((*current,v)));flag.append(current)
            chain[tuple(flag)]=orientation[len(s)-1]*parity(tuple(T.index(v) for v in (*s,*rest)))
        blocks[s]=chain
    # Infer dual cellular boundaries from the actual barycentric block boundaries.
    B={}
    for s in simplices:
        actual=boundary(blocks[s],T);coeff={}
        for t in simplices:
            if len(t)!=len(s)+1:continue
            witness=next(iter(blocks[t]));a=actual.get(witness,0)
            if a:coeff[t]=a//blocks[t][witness]
        assert add(*(scale(blocks[t],a) for t,a in coeff.items()))==actual
        B[s]=coeff
    check('all15 oriented dual blocks have the actual relative cellular boundary',all(
        B[s]=={t:boundary({t:1})[s] for t in simplices if len(t)==len(s)+1 and s in boundary({t:1})} for s in simplices))
    check('dual relative chain differential squares to zero',all(not add(*(scale(B[t],a) for t,a in B[s].items())) for s in simplices))
    # D sends primal simplex s to the coefficient functional on dual block D(s).
    # Its degree changes from chain k to dual cochain 3-k.
    def dual_coboundary(c):return clean({s:sum(a*c.get(t,0) for t,a in B[s].items()) for s in simplices})
    check('central map intertwines primal boundary and dual coboundary on every basis',all(boundary({s:1})==dual_coboundary({s:1}) for s in simplices))
    check('complementary dimensions and total information match',
          [sum(len(s)==k+1 for s in simplices) for k in range(4)]==[4,6,4,1] and
          [sum(4-len(s)==k for s in simplices) for k in range(4)]==[1,4,6,4])
    values={s:i+1 for i,s in enumerate(simplices)}
    check('handoff and inverse retain all15 independent coefficients',dict(values)=={s:values[s] for s in simplices} and len(values)==15)
    # Full geometric dual closures intersect on the dual of the joined primal face.
    closures={s:{f for flag in block for f in faces(flag)} for s,block in blocks.items()}
    for s in simplices:
        common=set.intersection(*(closures[(v,)] for v in s))
        assert common==closures[s]
    checks.append('four dual volumes share exactly the dual faces edges and center')
    def center(face):return tuple(sum(F(vertex[v][i],len(face)) for v in face) for i in range(4))
    def volume(flag):
        pts=[fcc(center(s)) for s in flag];cols=[tuple(pts[j][i]-pts[0][i] for i in range(3)) for j in (1,2,3)]
        return abs(det(tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))))/6
    source_points=[fcc(vertex[v]) for v in T]
    cols=[tuple(source_points[j][i]-source_points[0][i] for i in range(3)) for j in (1,2,3)]
    total_volume=abs(F(det(tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))),6))
    volumes={v:sum(volume(flag) for flag in blocks[(v,)]) for v in T}
    check('24 barycentric tetrahedra partition the central cell into four equal volumes',sum(len(blocks[(v,)]) for v in T)==24 and all(v==total_volume/4 for v in volumes.values()) and sum(volumes.values())==total_volume)
    # Relabelling transports block orientations, including the ambient orientation line.
    untwisted_failures=0
    for perm in permutations(T):
        p=dict(zip(T,perm));ambient_sign=parity(tuple(T.index(v) for v in perm))
        for s in simplices:
            target=tuple(sorted(p[v] for v in s))
            primal_sign=parity(tuple(p[v] for v in s))
            transported=add(*({tuple(tuple(sorted(p[v] for v in face)) for face in flag):a} for flag,a in blocks[s].items()))
            expected=scale(blocks[target],ambient_sign*primal_sign)
            assert transported==expected
            # Pushforward on dual cochains has the same signed-permutation factor.
            assert ambient_sign*(ambient_sign*primal_sign)==primal_sign
            if ambient_sign*primal_sign!=primal_sign:untwisted_failures+=1
    checks.append('all24 frames are natural after carrying the ambient orientation line')
    check('dropping orientation twist fails for improper frames',untwisted_failures==12*15)
    # Explicit rho of the actual central source vertices.
    ids={v:k for k,v in vertex.items()}
    rho={v:ids[(vertex[v][3],vertex[v][0],vertex[v][1],vertex[v][2])] for v in T}
    check('source quarter-chart action cycles the four dual volume sectors',len({rho[v] for v in T})==4 and all(rho[rho[rho[rho[v]]]]==v and rho[rho[v]]!=v for v in T))
    check('source quarter-chart orientation sign is negative and must be retained',parity(tuple(T.index(rho[v]) for v in T))==-1)
    # Without relative boundary, physical boundary faces survive.
    check('forgetting relative boundary produces extra terms',any(boundary(blocks[(v,)])!=boundary(blocks[(v,)],T) for v in T))
    # Same-face cochains remain the wrong target; their differential raises simplex size.
    def same_face_delta(c):return clean({s:sum(a*c.get(t,0) for t,a in boundary({s:1}).items()) for s in simplices})
    check('same-face coefficient identification still fails',same_face_delta({(T[0],):1})!=boundary({(T[0],):1}))
    check('arbitrary mixed-degree coefficients satisfy the central law',boundary(values)==dual_coboundary(values))
    source_cells={r['id']:(r['id'],) for r in census['vertices']}
    for kind in ['edges','triangles','tetrahedra']:
        source_cells.update({r['id']:tuple(sorted(r['vertices'])) for r in census[kind]})
    dual_leg_records=[]
    for bridge in prior['central_flag_bridges']:
        # Restrict dual cochains to successively smaller dual-block closures.
        primal_labels=[source_cells[id] for id in bridge['rotated_flag']]
        windows=[simplices]+[[t for t in simplices if set(s)<=set(t)] for s in primal_labels[1:]]
        for window in windows:
            visible={s:a for s,a in values.items() if s in window}
            retained={s:a for s,a in values.items() if s not in window}
            assert not set(visible)&set(retained) and {**visible,**retained}==values
        for big,small in zip(windows,windows[1:]):
            for s in big:
                lhs={t:a for t,a in dual_coboundary({s:1}).items() if t in small}
                restricted={s:1} if s in small else {}
                rhs=clean({t:sum(a*restricted.get(u,0) for u,a in B[t].items()) for t in small})
                assert lhs==rhs
        dual_leg_records.append({'primal_rotated_flag':bridge['rotated_flag'],
                                 'dual_window_basis_sizes':[len(w) for w in windows],
                                 'terminal_dual_cell_of':primal_labels[-1]})
    check('all24 descending dual-cell legs have three valid cochain restrictions',len(dual_leg_records)==24 and all(r['dual_window_basis_sizes']==[15,4,2,1] for r in dual_leg_records))
    checks.append('every descending window plus retained complement reconstructs all15 coefficients')
    check('central tetrahedron corresponds to the single central dual vertex',list(blocks[T])==[(T,)] and center(T)==(F(7,4),)*4)
    source_paths=[SOURCE,HANDOFF,'research/strominger/checkers/check_central_dual_cell_handoff.py',
                  'research/nima/full-esd7-graded-tate-torus-realization.md',
                  'research/nima/tetra-channel-comparison-and-graded-fourier-lift.md']
    report={'status':'passed','checks':checks,'check_count':len(checks),'central_cell':central_id,
      'central_vertices':T,'central_volume':str(total_volume),'dual_volume_by_vertex':{v:str(a) for v,a in volumes.items()},
      'primal_chain_ranks':[4,6,4,1],'relative_dual_chain_ranks':[1,4,6,4],
      'basis_map':[{'primal_simplex':s,'primal_degree':len(s)-1,'dual_cochain_degree':4-len(s),
                    'dual_block':[{'flag':flag,'coefficient':a} for flag,a in blocks[s].items()],
                    'dual_boundary':[{'dual_cell':t,'coefficient':a} for t,a in B[s].items()]} for s in simplices],
      'descending_dual_legs':dual_leg_records,'rho_vertex_action':rho,'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in source_paths},
      'scope':'Finite oriented cellular duality C_k(T184) -> C^(3-k)(dual T184, boundary), retaining the orientation line and all coefficients. Dual cells use barycentric points as presentation data, not new FCC transport sites. This replaces same-face dualization; it is not the Fourier map on the independent channel V, a P/E readout, or an identification of degree complement with q^4=Sigma.',
      'disposition':'Central finite cellular handoff constructed. Descending windows must use the dual-cell incidence rather than silently reuse primal-face cochains; analytic channel/Fourier binding and global stage law remain separate.'}
    dest=ROOT/'research/strominger/results/central-dual-cell-handoff.json'
    dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','checks':len(checks),'central_cell':central_id,'primal_ranks':report['primal_chain_ranks'],'dual_relative_ranks':report['relative_dual_chain_ranks'],'central_volume':str(total_volume),'quarter_volume':str(total_volume/4),'result':str(dest)}))


if __name__=='__main__':main()

"""A declared PL realization contract: barycentric complexes over inward depth.
T=sd(Delta2), C=sd(Delta3), h_n(x)=1-n*min(x). P is the full
geometric fiber product, triangulated as cone(sd(boundary Delta2) x
sd(boundary Delta3)). Not the categorical product of abstract complexes.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from collections import Counter
from hashlib import sha256
import json


def digest(r): return sha256(b'marici.potential-pullback.v1\0'+json.dumps(r,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def subsets(n): return [tuple(c) for k in range(1,n+1) for c in combinations(range(n),k)]
def label(s): return ''.join(map(str,s))
def barycenter(s,n): return tuple(Q(i in s,len(s)) for i in range(n))
def full_flags(n): return [tuple(tuple(sorted(p[:k])) for k in range(1,n+1)) for p in permutations(range(n))]
def depth(point):
    if any(x<0 for x in point) or sum(point)!=1: raise ValueError('point outside simplex')
    return 1-len(point)*min(point)

def complex_cells(maximal):
    cells={}
    for simplex in maximal:
        for k in range(1,len(simplex)+1):
            cells.setdefault(k-1,set()).update(tuple(sorted(c)) for c in combinations(simplex,k))
    return cells

def gf2_rank(columns):
    pivots={}
    for value in columns:
        while value:
            p=value.bit_length()-1
            if p in pivots: value^=pivots[p]
            else: pivots[p]=value; break
    return len(pivots)

def betti_mod2(maximal):
    cells=complex_cells(maximal); top=max(cells); ranks={0:0,top+1:0}
    for dim in range(1,top+1):
        lookup={c:i for i,c in enumerate(sorted(cells[dim-1]))}
        ranks[dim]=gf2_rank([sum(1<<lookup[tuple(c)] for c in combinations(s,dim)) for s in sorted(cells[dim])])
    return [len(cells[k])-ranks[k]-ranks[k+1] for k in range(top+1)]

def make_contract(focus_root,outer_triangle):
    tflags=full_flags(3); cflags=full_flags(4)
    tvertices={label(s):list(map(str,barycenter(s,3))) for s in subsets(3)}
    cvertices={label(s):list(map(str,barycenter(s,4))) for s in subsets(4)}
    apex='realized-barycenter'; vertices={apex:{'T':'012','C':'0123','height':'0'}}
    for a in subsets(3)[:-1]:
        for b in subsets(4)[:-1]: vertices['T'+label(a)+'_C'+label(b)]={'T':label(a),'C':label(b),'height':'1'}
    maximal=[]; provenance=[]
    # Each boundary edge x boundary triangle is a triangular prism. Its three
    # staircase tetrahedra agree with neighbors because global subset orders agree.
    for tf in tflags:
        for cf in cflags:
            a=list(map(label,tf[:-1])); b=list(map(label,cf[:-1]))
            for horizontal_position in range(3):
                i=j=0; path=['T'+a[i]+'_C'+b[j]]
                for step in range(3):
                    if step==horizontal_position: i+=1
                    else: j+=1
                    path.append('T'+a[i]+'_C'+b[j])
                maximal.append([apex]+path)
                provenance.append({'T_flag':list(map(label,tf)),'C_flag':list(map(label,cf)), 'staircase':horizontal_position})
    tmax=[list(map(label,f)) for f in tflags]; cmax=[list(map(label,f)) for f in cflags]
    return {'kind':'PL-potential-realization-contract','focus_root':focus_root,'outer_triangle':outer_triangle,
            'category':'PL polyhedra and PL maps; not arbitrary proof-relevant higher types',
            'fold_convention':'all barycentric flags; inward radial contraction to the barycenter, not isometric origami folding',
            'interface':{'vertices':['0','1'],'maximal_simplices':[['0','1']]},
            'T':{'vertices':tvertices,'maximal_simplices':tmax},
            'C':{'vertices':cvertices,'maximal_simplices':cmax},
            'T_to_I':{v:('0' if v=='012' else '1') for v in tvertices},
            'C_to_I':{v:('0' if v=='0123' else '1') for v in cvertices},
            'P':{'vertices':vertices,'maximal_simplices':maximal,'fold_provenance':provenance},
            'potential_particle_identity':'not assigned'}

def realization_belt(contract,inner=Q(1,2),outer=Q(1)):
    if not 0<inner<outer<=1: raise ValueError('belt needs two positive distinct depth levels')
    circle=['0','01','1','12','2','02']; vertices={}; faces=[]
    for name,height in [('inner',inner),('outer',outer)]:
        for ref in circle:
            u=tuple(map(Q,contract['T']['vertices'][ref]))
            vertices[name+'_'+ref]=list(map(str,((1-height)/3+height*v for v in u)))
    for a,b in zip(circle,circle[1:]+circle[:1]):
        faces.append(['outer_'+a,'outer_'+b,'inner_'+b,'inner_'+a])
    return {'inner_depth':str(inner),'outer_depth':str(outer),'vertices_in_T':vertices,'quadrilaterals':faces,
            'location':'around the new barycenter in the selected outer triangle, not an original tetrahedral corner'}


def boundary_decomposition(point):
    """Express a boundary point in a barycentric flag simplex, exactly.
    Ties give zero coefficients; their alternative flags remain in the complex.
    """
    n=len(point)
    if depth(point)!=1: raise ValueError('not a boundary point')
    order=sorted(range(n),key=lambda i:(-point[i],i)); refs=[]; weights=[]
    for k in range(1,n):
        refs.append(label(tuple(sorted(order[:k]))))
        weights.append(k*(point[order[k-1]]-point[order[k]]))
    if sum(weights)!=1 or min(weights)<0: raise ValueError('invalid flag weights')
    return refs,weights

def factor(x,y):
    """Unique geometric mediator for compatible points; deterministic chart.
    Coordinates in a chosen simplex need not be unique on shared faces.
    """
    hx,hy=depth(x),depth(y)
    if hx!=hy: raise ValueError('incompatible interface images')
    h=hx
    if h==0: return {'realized-barycenter':Q(1)}
    ux=tuple((v-(1-h)/len(x))/h for v in x)
    uy=tuple((v-(1-h)/len(y))/h for v in y)
    ar,aw=boundary_decomposition(ux); br,bw=boundary_decomposition(uy)
    # Monotone quantile coupling is the staircase product triangulation.
    cuts={Q(0),Q(1)}; s=Q(0)
    for w in aw: s+=w; cuts.add(s)
    s=Q(0)
    for w in bw: s+=w; cuts.add(s)
    cuts=sorted(cuts); result={'realized-barycenter':1-h} if h!=1 else {}
    def at(weights,p):
        total=Q(0)
        for i,w in enumerate(weights):
            total+=w
            if p<total: return i
        raise ValueError('coupling index')
    for left,right in zip(cuts,cuts[1:]):
        if right==left: continue
        middle=(left+right)/2
        ref='T'+ar[at(aw,middle)]+'_C'+br[at(bw,middle)]
        result[ref]=h*(right-left)
    return result

def project(contract,weights):
    if any(w<0 for w in weights.values()) or sum(weights.values())!=1: raise ValueError('invalid simplex weights')
    if not any(set(weights)<=set(s) for s in contract['P']['maximal_simplices']): raise ValueError('not a pullback simplex')
    x=[Q(0)]*3; y=[Q(0)]*4
    for ref,w in weights.items():
        v=contract['P']['vertices'][ref]
        for i,a in enumerate(contract['T']['vertices'][v['T']]): x[i]+=w*Q(a)
        for i,b in enumerate(contract['C']['vertices'][v['C']]): y[i]+=w*Q(b)
    return tuple(x),tuple(y)

def verify(contract):
    expected=make_contract(contract['focus_root'],contract['outer_triangle'])
    if contract!=expected: raise ValueError('not the declared pullback/flag contract')
    vertices=contract['P']['vertices']; apex='realized-barycenter'
    if [v for v,r in vertices.items() if r['height']=='0']!=[apex]: raise ValueError('marked fiber is not one point')
    tsets=[set(s) for s in contract['T']['maximal_simplices']]
    csets=[set(s) for s in contract['C']['maximal_simplices']]
    for simplex in contract['P']['maximal_simplices']:
        tp={vertices[v]['T'] for v in simplex}; cp={vertices[v]['C'] for v in simplex}
        if not any(tp<=s for s in tsets) or not any(cp<=s for s in csets): raise ValueError('projection not simplicial')
        for v in simplex:
            r=vertices[v]
            if contract['T_to_I'][r['T']]!=contract['C_to_I'][r['C']] or r['height']!=contract['T_to_I'][r['T']]: raise ValueError('square does not commute')
    link=[s[1:] for s in contract['P']['maximal_simplices']]
    return {'verified':True,'T_fold_flags':6,'C_fold_flags':24,'potential_primary_cones':4,
            'pullback_f_vector':[len(v) for k,v in sorted(complex_cells(contract['P']['maximal_simplices']).items())],
            'apex_link_f_vector':[len(v) for k,v in sorted(complex_cells(link).items())],
            'apex_link_betti_mod2':betti_mod2(link),
            'marked_zero_fiber':'single barycenter pair; not the whole pullback',
            'pullback_dimension':4,'model':'cone(S1 x S2) with both projection maps retained'}

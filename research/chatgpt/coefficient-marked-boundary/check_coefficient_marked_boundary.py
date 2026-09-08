#!/usr/bin/env python3
"""Exact coefficient-marked octagon boundary computation.

Standard library only. Reconstructs the pinned Marici primitive-coefficient
loaded complexes; proves their reduction by explicitly checking integral
chain contractions, restrictions, totalization and relabelling.
Also enumerates the derived-section groups of the earlier NONCONSTANT
conductor diagram by negative Laurent support. These are distinct models.
No repository writes, no geometric upstream pipeline, no proof assistant.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict, deque
from itertools import combinations, product
import json
from pathlib import Path
from typing import Iterable

COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCES = {
 'research/voevodsky/check_n8_full_twisted_cut_cech_lift.py': 'de9502d39bb9501a6b2595ab858b4485c55cad7c',
 'research/voevodsky/check_n8_twisted_cut_cech_totalization.py': '9ae876491451a49ae21bf0ade69ce7cb7bd52fa9',
 'research/voevodsky/check_n8_multirees_conductor_stalk_kernel.py': 'adc1f08b8882f15bef05bec59afe5e119b67512c',
 'research/voevodsky/check_n8_framed_physical_line_rigidity.py': 'f70ba93909b5ae489bb7e2bed56fc87ca555be76',
 'research/voevodsky/check_physical_derived_pullback_after_transform.py': '7993b2b1bbdba03d05c3f443a45717d7b8efeec5',
}
Diagonal = tuple[int, int]
Face = tuple[Diagonal, ...]
Cell = tuple[Face, Face]
Vec = dict[Cell, int]
COUNTS: Counter[str] = Counter()


def check(ok: bool, category: str, detail=None) -> None:
    if not ok:
        raise AssertionError(f'{category}: {detail}')
    COUNTS[category] += 1


def pm(n: int) -> int:
    return -1 if n % 2 else 1


def normalized(a: int, b: int) -> Diagonal:
    return tuple(sorted((a % 8, b % 8)))


def crosses(a: Diagonal, b: Diagonal) -> bool:
    x,y = a; u,v = b
    return x < u < y < v or u < x < v < y


def faces(ds: tuple[Diagonal, ...]) -> tuple[Face, ...]:
    out = [()]
    def extend(cur: Face, start: int) -> None:
        for i in range(start, len(ds)):
            d = ds[i]
            if all(not crosses(d,e) for e in cur):
                nxt = cur + (d,)
                out.append(nxt)
                extend(nxt, i+1)
    extend((), 0)
    return tuple(sorted(out, key=lambda f:(len(f), f)))


def subsets(f: Face) -> Iterable[Face]:
    for n in range(len(f)+1):
        yield from combinations(f,n)


def add(a: dict, b: dict, scale: int=1) -> dict:
    ans = dict(a)
    for x,c in b.items():
        ans[x] = ans.get(x,0) + scale*c
        if not ans[x]: del ans[x]
    return ans


def apply(table: dict, v: dict) -> dict:
    out = {}
    for x,c in v.items(): out = add(out,table.get(x,{}),c)
    return out


def degree(c: Cell) -> int:
    return len(c[0])-len(c[1])


def project(v: Vec, cellset: set[Cell]) -> Vec:
    return {x:c for x,c in v.items() if x in cellset}


class Loaded:
    def __init__(self, ds: tuple[Diagonal,...]) -> None:
        self.ds = ds
        self.fs = faces(ds)
        self.cells = tuple((f,m) for f in self.fs for m in subsets(f))
        self.cellset = set(self.cells)
        self.radial: dict[Cell,Vec] = {}
        self.normal: dict[Cell,Vec] = {}
        self.h0: dict[Cell,Vec] = {}
        self.d: dict[Cell,Vec] = {}
        self.H: dict[Cell,Vec] = {}
        for c in self.cells:
            f,m = c
            rad = {}
            for e in ds:
                if e not in f and all(not crosses(e,z) for z in f):
                    target = (tuple(sorted(f+(e,))),m)
                    rad[target] = pm(sum(z < e for z in f))
            nor = {(f,tuple(z for z in m if z != e)):pm(4-len(f)+i)
                   for i,e in enumerate(m)}
            self.radial[c] = rad
            self.normal[c] = nor
            self.d[c] = add(rad,nor)
            if f and f[0] not in m:
                self.h0[c] = {(f,tuple(sorted(m+(f[0],)))):pm(4-len(f))}
            else:
                self.h0[c] = {}
        # Finite perturbation formula H = sum_j (-h0 radial)^j h0.
        for c in self.cells:
            term = dict(self.h0[c]); value = {}
            for j in range(7):
                value = add(value,term,pm(j))
                term = apply(self.h0,apply(self.radial,term))
                if not term: break
            check(not term,'perturbation_terminates',c)
            self.H[c] = value
        self.unit = {(f,f):pm(len(f)*(len(f)-1)//2) for f in self.fs}
        self.ranks = [sum(degree(c)==q for c in self.cells) for q in range(5)]

    def audit(self) -> None:
        empty = ((),())
        for c in self.cells:
            check(all(t in self.cellset and degree(t)==degree(c)+1 for t in self.d[c]),
                  'local_differential_degree',c)
            check(not apply(self.d,self.d[c]), 'local_d_squared',c)
            lhs0 = add(apply(self.normal,self.h0[c]),apply(self.h0,self.normal[c]))
            check(lhs0 == ({} if c==empty else {c:1}), 'normal_contraction',c)
            lhs = add(apply(self.d,self.H[c]),apply(self.H,self.d[c]))
            rhs = add({c:1},self.unit,-1) if c==empty else {c:1}
            check(lhs == rhs,'full_integral_contraction',c)
            check(not apply(self.H,self.H[c]),'contraction_square_zero',c)
            check(all(degree(t)==degree(c)-1 for t in self.H[c]),'contraction_degree',c)
        check(not apply(self.d,self.unit),'primitive_unit_closed')
        check(self.unit.get(empty)==1,'primitive_unit_normalized')
        check(not apply(self.H,self.unit),'contraction_kills_unit')


def act_diag(g: tuple[int,int], d: Diagonal) -> Diagonal:
    r,f = g
    return normalized(r+pm(f)*d[0],r+pm(f)*d[1])


def act_tuple(g: tuple[int,int], f: Face) -> tuple[Face,int]:
    vals = tuple(act_diag(g,d) for d in f)
    inv = sum(vals[i]>vals[j] for i in range(len(vals)) for j in range(i+1,len(vals)))
    return tuple(sorted(vals)),pm(inv)


def act_cell(g: tuple[int,int], c: Cell) -> tuple[Cell,int]:
    f,s = act_tuple(g,c[0]); m,t = act_tuple(g,c[1])
    return (f,m),s*t


def act_vec(g: tuple[int,int], v: Vec) -> Vec:
    out = {}
    for c,a in v.items():
        target,s = act_cell(g,c)
        out[target] = out.get(target,0)+a*s
    return {x:a for x,a in out.items() if a}


def graph_stats(vs, es):
    vs = set(vs)
    es = [e for e in es if set(e)<=vs]
    adj = defaultdict(list)
    for a,b in es: adj[a].append(b); adj[b].append(a)
    seen = set(); components = 0; tree = []
    for v in sorted(vs):
        if v in seen: continue
        components += 1; seen.add(v); queue=deque([v])
        while queue:
            u=queue.popleft()
            for w in adj[u]:
                if w not in seen:
                    seen.add(w); queue.append(w); tree.append(tuple(sorted((u,w))))
    return components,len(es)-len(vs)+components,tree


def unit_smith(matrix):
    a=[r[:] for r in matrix]
    m=len(a); n=len(a[0]) if m else 0; k=0; pivots=[]
    while k<min(m,n):
        hit=next(((i,j) for i in range(k,m) for j in range(k,n) if abs(a[i][j])==1),None)
        if hit is None: break
        i,j=hit; a[k],a[i]=a[i],a[k]
        for row in a: row[k],row[j]=row[j],row[k]
        if a[k][k]<0: a[k]=[-x for x in a[k]]
        for i in range(m):
            if i!=k and a[i][k]:
                c=a[i][k]; a[i]=[x-c*y for x,y in zip(a[i],a[k])]
        for j in range(n):
            if j!=k and a[k][j]:
                c=a[k][j]
                for i in range(m): a[i][j]-=c*a[i][k]
        pivots.append(1); k+=1
    residual=[r[k:] for r in a[k:]]
    return pivots,residual


def support_cohomology(neg: Face, cuts, edges):
    k=len(neg); internal=set(neg)&set(cuts)
    active={d for d in cuts if all(not crosses(d,n) for n in neg)}
    external=active-internal
    active_edges=[e for e in edges if set(e)<=active]
    e0=[e for e in active_edges if not(set(e)&internal)]
    e1=[e for e in active_edges if len(set(e)&internal)==1]
    e2=[e for e in active_edges if len(set(e)&internal)==2]
    rank1=len({next(iter(set(e)&internal)) for e in e1})
    b0,b1,_=graph_stats(external,e0)
    h=Counter()
    if internal or e2:
        h[k-1] += len(internal)-rank1+len(e2)
    h[k] += b0+len(e1)-rank1
    h[k+1] += b1
    return {q:r for q,r in sorted(h.items()) if r}


def main(path: Path) -> None:
    ds=tuple((a,b) for a in range(8) for b in range(a+1,8)
             if b-a not in (1,7))
    cuts=tuple(sorted({normalized(i,i+3) for i in range(8)}))
    edges=tuple(e for e in combinations(cuts,2) if not crosses(*e))
    check((len(ds),len(cuts),len(edges))==(20,8,12),'source_counts')
    check(not any(all(not crosses(a,b) for a,b in combinations(t,2))
                  for t in combinations(cuts,3)),'no_triple_cuts')
    charts={c:Loaded(tuple(d for d in ds if d!=c and not crosses(d,c))) for c in cuts}
    overlaps={e:Loaded(tuple(d for d in ds if d not in e and all(not crosses(d,c) for c in e))) for e in edges}
    for obj in list(charts.values())+list(overlaps.values()): obj.audit()
    for obj in charts.values(): check(len(obj.cells)==1075,'chart_cell_count')
    for obj in overlaps.values(): check(len(obj.cells)==125,'overlap_cell_count')
    escaping=0
    for edge,small in overlaps.items():
        for cut in edge:
            big=charts[cut]
            for c in big.cells:
                left=project(big.d[c],small.cellset)
                right=small.d.get(c,{})
                check(left==right,'restriction_chain_map',(edge,cut,c))
                check(project(big.H[c],small.cellset)==small.H.get(c,{}),
                      'restriction_contraction_naturality',(edge,cut,c))
                if c in small.cellset:
                    escaping += sum(t not in small.cellset for t in big.d[c])
            check(project(big.unit,small.cellset)==small.unit,'restriction_preserves_unit',edge)
    # Reconstruct all 10100 total generators and sparse total differentials.
    basis=[]; total_d={}; total_H={}; red={}; inc={}
    for i,c in enumerate(cuts):
        obj=charts[c]
        for cell in obj.cells:
            b=('v',i,cell); basis.append(b)
            total_d[b]={('v',i,t):a for t,a in obj.d[cell].items()}
            for j,e in enumerate(edges):
                if c in e and cell in overlaps[e].cellset:
                    total_d[b][('e',j,cell)]=-1 if c==e[0] else 1
            total_H[b]={('v',i,t):a for t,a in obj.H[cell].items()}
            red[b]={('v',i):1} if cell==((),()) else {}
        inc[('v',i)]={('v',i,t):a for t,a in obj.unit.items()}
    for j,e in enumerate(edges):
        obj=overlaps[e]
        for cell in obj.cells:
            b=('e',j,cell); basis.append(b)
            total_d[b]={('e',j,t):-a for t,a in obj.d[cell].items()}
            total_H[b]={('e',j,t):-a for t,a in obj.H[cell].items()}
            red[b]={('e',j):1} if cell==((),()) else {}
        inc[('e',j)]={('e',j,t):a for t,a in obj.unit.items()}
    reduced_d={('v',i):{('e',j):(-1 if c==e[0] else 1)
                         for j,e in enumerate(edges) if c in e} for i,c in enumerate(cuts)}
    reduced_d.update({('e',j):{} for j in range(len(edges))})
    for b in basis:
        check(not apply(total_d,total_d[b]),'total_d_squared',b)
        check(apply(red,total_d[b])==apply(reduced_d,red[b]),'total_reduction_chain_map',b)
        lhs=add(apply(total_d,total_H[b]),apply(total_H,total_d[b]))
        rhs=add({b:1},apply(inc,red[b]),-1)
        check(lhs==rhs,'total_integral_contraction',b)
    for b,v in inc.items():
        check(apply(red,v)=={b:1},'total_reduction_section',b)
        check(apply(total_d,v)==apply(inc,reduced_d[b]),'total_section_chain_map',b)
    # Relabelling on oriented face and mark factors. Homotopy need not be equivariant;
    # the augmentation and primitive section are strictly equivariant.
    all_models={('v',c):o for c,o in charts.items()}
    all_models.update({('e',e):o for e,o in overlaps.items()})
    groups=list(product(range(8),range(2)))
    for g in groups:
        for (typ,key),obj in all_models.items():
            newkey=act_diag(g,key) if typ=='v' else tuple(sorted(act_diag(g,d) for d in key))
            target=all_models[(typ,newkey)]
            for c in obj.cells:
                image,sign=act_cell(g,c)
                check(image in target.cellset,'dihedral_cell_preservation')
                check(act_vec(g,obj.d[c])=={t:sign*a for t,a in target.d[image].items()},
                      'dihedral_chain_equivariance')
            check(act_vec(g,obj.unit)==target.unit,'dihedral_unit_equivariance')
    # Primitive quotient graph and integral negative control without the Thom twist.
    matrix=[]; signless=[]
    for a,b in edges:
        row=[0]*8; row[cuts.index(a)]=-1; row[cuts.index(b)]=1; matrix.append(row)
        row=[0]*8; row[cuts.index(a)]=1; row[cuts.index(b)]=1; signless.append(row)
    units,res=unit_smith(matrix)
    check(len(units)==7 and not any(x for row in res for x in row),'graph_integral_smith')
    units_s,res_s=unit_smith(signless)
    check(len(units_s)==7,'untwisted_unit_factors')
    rem=[abs(x) for row in res_s for x in row if x]
    check(rem and set(rem)=={2},'untwisted_order_two_residue')
    check(all(sum(row)==0 for row in matrix),'normalized_global_unit')
    b0,b1,tree=graph_stats(cuts,edges)
    check((b0,b1)==(1,5),'graph_homology')
    total_ranks=[sum(degree(c)+(typ=='e')==q for typ,_,c in basis) for q in range(5)]
    check(total_ranks==[1080,3276,3648,1776,320],'total_ranks')
    # Degree ranks follow from the proved integral retraction, not a modular guess.
    dr=[]; prev=0
    for q,n in enumerate(total_ranks[:-1]):
        rank=n-prev-([1,5,0,0,0][q]); dr.append(rank); prev=rank
    check(dr==[1079,2192,1456,320],'total_differential_ranks')
    # Infinite Laurent coefficient diagram: finite exact support classification.
    # Coefficients depend on a monomial only through its negative exponent support.
    # Arbitrary exponents and all branch degrees are covered by the proof in the note.
    all_faces=faces(ds)
    support_table=[]
    hist=Counter(); aggregated=Counter()
    for neg in all_faces:
        cohom=support_cohomology(neg,cuts,edges)
        # Independently form every degree of the supportwise Cech map.
        active={c for c in cuts if all(not crosses(c,n) for n in neg)}
        active_edges=[e for e in edges if set(e)<=active]
        nset=set(neg)
        vdeg={c:len(nset-set((c,))) for c in active}
        edeg={e:len(nset-set(e)) for e in active_edges}
        ker=Counter(); coker=Counter()
        for q in range(6):
            vv=sorted(c for c in active if vdeg[c]==q)
            ee=sorted(e for e in active_edges if edeg[e]==q)
            mat=[[(-1 if c==e[0] else 1) if c in e else 0 for c in vv] for e in ee]
            units_q,res_q=unit_smith(mat)
            check(not any(x for row in res_q for x in row),'support_incidence_all_Smith_factors_unit')
            rank_q=len(units_q)
            ker[q]=len(vv)-rank_q; coker[q]=len(ee)-rank_q
        from_matrices={q:ker[q]+coker[q-1] for q in range(7) if ker[q]+coker[q-1]}
        check(from_matrices==cohom,'support_matrix_computation',neg)
        check(all(q>=0 and r>0 for q,r in cohom.items()),'support_degrees')
        check(cohom.get(0,0)==(1 if not neg else 0),'full_conductor_H0_support')
        check(all(q<=4 for q in cohom),'full_conductor_amplitude')
        hist[(len(neg),len(set(neg)&set(cuts)),tuple(cohom.items()))]+=1
        for q,r in cohom.items(): aggregated[q]+=r
        support_table.append({'negative_support':[list(d) for d in neg],
                              'cohomology_ranks':{str(q):r for q,r in cohom.items()}})
    check(len(all_faces)==903,'all_negative_support_types')
    check(support_cohomology((),cuts,edges)=={0:1,1:5},'constant_support_control')
    check(all(support_cohomology((d,),cuts,edges)=={1:5} for d in cuts),'single_cut_pole_control')
    check(all(support_cohomology(tuple(e),cuts,edges)=={1:3} for e in edges),'double_cut_pole_control')
    certificate={
      'source_commit':COMMIT,'source_blobs':SOURCES,
      'checks':dict(sorted(COUNTS.items())), 'total_checks':sum(COUNTS.values()),
      'physical_primitive_loaded_model':{
        'charts':8,'overlaps':12,'chart_generators_each':1075,'overlap_generators_each':125,
        'total_generators':len(basis),'cochain_ranks':total_ranks,'differential_ranks':dr,
        'restriction_escaping_arrows_projected_away':escaping,
        'integral_homology':{'0':'Z','1':'Z^5'},'integer_torsion':False,
        'normalized_marking_homotopy_type':'point',
        'relative_to_complete_graph_readout':'acyclic',
        'unframed_mapping_space_from_Z':'discrete Z',
        'source_dihedral_normalized_quotient':'B(D8), D8 has order 16',
        'untwisted_control':{'H0':'0','H1':'Z^4 + Z/2'},
        'cuts':[list(c) for c in cuts],'edges':[[cuts.index(a),cuts.index(b)] for a,b in edges],
        'reduced_incidence_matrix':matrix,'tree_edges':[[list(a),list(b)] for a,b in tree],
        'unit_formula':'coefficient on (F,F) is (-1)^(|F|(|F|-1)/2); all other cells zero',
      },
      'nonconstant_conductor_derived_sections':{
        'different_from_physical_primitive_projection':True,
        'admissible_negative_support_types':len(all_faces),
        'support_histogram':[{'support_size':k,'physical_cuts_in_support':r,
                             'cohomology_ranks':dict(p),'number_of_supports':n}
                             for (k,r,p),n in sorted(hist.items())],
        'rank_totals_one_formal_monomial_per_support':dict(sorted(aggregated.items())),
        'integral_torsion':False,
        'H0':'ker(R_empty[z_plus] + R_empty[z_minus] -> R_empty)',
        'higher_mapping_homotopy_from_Z':'zero',
        'cohomology_per_support':support_table,
      },
      'scope':[
        'Explicit contractions checked, not assigned zero deformation ranks.',
        'Physical primitive coefficient framing and Thom-sign choice are source inputs.',
        'No equivalence of the physical coordinate-projection Cech object with the earlier localization-diagram holim is asserted.',
        'Nonconstant conductor result is a separate exact computation; it is not collapsed to the primitive line.',
        'No reconstruction of omitted geometric relative functors, no RH conclusion, no proof-assistant verification.',
        'The nonconstant conductor normalization at common branch value 1 leaves independent positive branch polynomials.'
      ]
    }
    path.write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps({k:certificate[k] for k in ('total_checks','physical_primitive_loaded_model','scope')},indent=2))
    print('Nonconstant support histogram:')
    print(json.dumps(certificate['nonconstant_conductor_derived_sections']['support_histogram'],indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('coefficient_marked_boundary_certificate.json'))
    args=parser.parse_args()
    main(args.output)

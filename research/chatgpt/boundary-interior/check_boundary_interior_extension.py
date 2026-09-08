#!/usr/bin/env python3
"""Exact boundary-to-interior extension computation.

Helper routines retained from check_coefficient_marked_boundary.py.

Original helper scope:

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



class FullLoaded:
    """Full source sign convention D=5, conjugate to helper D=4 by (-1)^|M|."""
    def __init__(self, ds):
        helper=Loaded(ds)
        self.cells=helper.cells; self.fs=helper.fs; self.cellset=helper.cellset
        self.d={}; self.H={}
        for c in self.cells:
            s=pm(len(c[1]))
            self.d[c]={t:s*pm(len(t[1]))*a for t,a in helper.d[c].items()}
            self.H[c]={t:s*pm(len(t[1]))*a for t,a in helper.H[c].items()}
            f,m=c
            expected=dict(helper.radial[c])
            for i,e in enumerate(m):
                t=(f,tuple(z for z in m if z!=e))
                expected=add(expected,{t:pm(5-len(f)+i)})
            check(self.d[c]==expected,'source_dimension_five_sign',c)
        self.unit={c:pm(len(c[1]))*a for c,a in helper.unit.items()}
        self.ranks=[sum(degree(c)==q for c in self.cells) for q in range(6)]


def rho_cell(cut, cell):
    """Normalized extraction of the Cut's marked normal, with orientation sign."""
    f,m=cell
    if cut not in m: return {}
    ff=tuple(x for x in f if x!=cut)
    mm=tuple(x for x in m if x!=cut)
    s=-pm(sum(x>cut for x in ff)+sum(x>cut for x in mm))
    return {(ff,mm):s}


def rho_vec(cut,v):
    out={}
    for c,a in v.items(): out=add(out,rho_cell(cut,c),a)
    return out


def sparse_matrix_product_zero(left,right):
    return all(not apply(left,v) for v in right.values())


def main(path: Path) -> None:
    ds=tuple((i,j) for i in range(8) for j in range(i+1,8) if j-i not in (1,7))
    cuts=tuple(sorted({normalized(i,i+3) for i in range(8)}))
    edges=tuple(e for e in combinations(cuts,2) if not crosses(*e))
    interior=FullLoaded(ds)
    charts={c:Loaded(tuple(d for d in ds if d!=c and not crosses(d,c))) for c in cuts}
    overlaps={e:Loaded(tuple(d for d in ds if d not in e and all(not crosses(d,c) for c in e))) for e in edges}
    empty=((),())
    check(len(interior.cells)==12425,'full_generator_count')
    check(interior.ranks==[903,3140,4320,2940,990,132],'full_degree_counts')
    check(sum(len(o.cells) for o in charts.values())+sum(len(o.cells) for o in overlaps.values())==10100,'boundary_generator_count')
    for c in interior.cells:
        check(not apply(interior.d,interior.d[c]),'full_d_squared',c)
        lhs=add(apply(interior.d,interior.H[c]),apply(interior.H,interior.d[c]))
        rhs=add({c:1},interior.unit,-1) if c==empty else {c:1}
        check(lhs==rhs,'full_integral_contraction',c)
        check(not apply(interior.H,interior.H[c]),'full_contraction_square_zero',c)
    check(not apply(interior.d,interior.unit),'interior_unit_closed')
    check(not apply(interior.H,interior.unit),'interior_unit_contraction_zero')
    for obj in list(charts.values())+list(overlaps.values()): obj.audit()

    # Rebuild the entire signed boundary totalization, not only its graph.
    td={}; th={}; unit_b={}; augmentation={}
    for cut,obj in charts.items():
        for cell in obj.cells:
            key=('v',cut,cell)
            v={('v',cut,t):a for t,a in obj.d[cell].items()}
            for edge,ov in overlaps.items():
                if cut in edge and cell in ov.cellset:
                    v[('e',edge,cell)]=-1 if cut==edge[0] else 1
            td[key]=v
            th[key]={('v',cut,t):a for t,a in obj.H[cell].items()}
            augmentation[key]={('v',cut):1} if cell==empty else {}
        unit_b=add(unit_b,{('v',cut,c):a for c,a in obj.unit.items()})
    for edge,obj in overlaps.items():
        for cell in obj.cells:
            key=('e',edge,cell)
            td[key]={('e',edge,t):-a for t,a in obj.d[cell].items()}
            th[key]={('e',edge,t):-a for t,a in obj.H[cell].items()}
            augmentation[key]={('e',edge):1} if cell==empty else {}
    graph_i={('v',cut):{('v',cut,c):a for c,a in obj.unit.items()} for cut,obj in charts.items()}
    graph_i.update({('e',edge):{('e',edge,c):a for c,a in obj.unit.items()} for edge,obj in overlaps.items()})
    for c in td:
        check(not apply(td,td[c]),'boundary_total_d_squared',c)
        lhs=add(apply(td,th[c]),apply(th,td[c]))
        rhs=add({c:1},apply(graph_i,augmentation[c]),-1)
        check(lhs==rhs,'boundary_total_contraction',c)

    # All eight marked-normal maps are checked on every full generator.
    rhos={cut:{c:rho_cell(cut,c) for c in interior.cells} for cut in cuts}
    for cut,obj in charts.items():
        for c in interior.cells:
            check(apply(obj.d,rhos[cut][c])==rho_vec(cut,interior.d[c]),'marked_normal_chain_map',(cut,c))
        check(rho_vec(cut,interior.unit)==obj.unit,'marked_normal_unit',cut)

    # Delta rho is generally nonzero as a chain map. Fill it using H already
    # constructed on the existing full complex: ell = (Delta rho) H.
    defect={}; ell={}; phi={}
    for c in interior.cells:
        defect[c]={}
        for edge,ov in overlaps.items():
            l,r=edge
            v=add(project(rhos[r][c],ov.cellset),project(rhos[l][c],ov.cellset),-1)
            defect[c].update({('e',edge,t):a for t,a in v.items()})
    for c in interior.cells:
        ell[c]=apply(defect,interior.H[c])
        out={}
        for cut in cuts: out.update({('v',cut,t):a for t,a in rhos[cut][c].items()})
        phi[c]=add(out,ell[c])
    nonzero_defects=sum(bool(v) for v in defect.values())
    nonzero_ell=sum(bool(v) for v in ell.values())
    check(nonzero_defects>0,'overlap_homotopies_really_needed')
    check(nonzero_ell>0,'nonzero_overlap_homotopies_constructed')
    for c in interior.cells:
        # td on a pure edge vector is minus the internal overlap differential.
        lhs=add(apply(td,ell[c]),apply(ell,interior.d[c]),-1)
        check(lhs=={t:-a for t,a in defect[c].items()},'overlap_homotopy_equation',c)
        check(apply(td,phi[c])==apply(phi,interior.d[c]),'full_restriction_chain_map',c)
    check(apply(phi,interior.unit)==unit_b,'exact_normalized_boundary_extension')
    check(not apply(td,unit_b),'boundary_primitive_closed')

    # Phi is homotopic to the primitive map i_boundary epsilon, through Phi H.
    ph={c:apply(phi,interior.H[c]) for c in interior.cells}
    for c in interior.cells:
        lhs=add(apply(td,ph[c]),apply(ph,interior.d[c]))
        rhs=add(phi[c],unit_b,-1) if c==empty else phi[c]
        check(lhs==rhs,'restriction_homotopy_to_primitive',c)

    # Reduced relative complex: Z in degree 0 -> Z^8 in degree 1 -> Z^12
    # in degree 2. Last differential is minus graph incidence. All matrices
    # have unit Smith factors, and the constant vector generates ker(delta).
    delta=[]; vi={v:i for i,v in enumerate(cuts)}
    for a,b in edges:
        row=[0]*8;row[vi[a]]=-1;row[vi[b]]=1;delta.append(row)
    piv,res=unit_smith(delta)
    check(len(piv)==7 and not any(any(r) for r in res),'relative_unit_smith_factors')
    check(all(sum(row)==0 for row in delta),'relative_d_squared')
    comps,cycles,tree=graph_stats(cuts,edges)
    check((comps,cycles)==(1,5),'relative_h2_rank')
    # A spanning-tree incidence minor is unimodular, proving that every
    # integral cycle has an integral gauge and five primitive chord coordinates.
    tree_rows=[delta[edges.index(e)] for e in tree]
    minor=[row[1:] for row in tree_rows]
    pp,rr=unit_smith(minor)
    check(len(pp)==7 and not any(any(r) for r in rr),'primitive_cycle_coordinates')
    chords=[e for e in edges if e not in tree]
    check(len(chords)==5,'five_relative_generators')

    # Polynomial-localization extension. Each negative-support type N in the
    # full index has H^|N|=Z per monomial/mode. The earlier support theorem
    # computes boundary groups. A compatible physical Cut outside N gives a
    # unit restriction in that degree; if none exists, that target degree is
    # zero. This determines the integral relative groups without discarding
    # localization coefficients.
    support_records=[]; aggregate=Counter(); types=Counter()
    for neg in interior.fs:
        k=len(neg); internal=set(neg)&set(cuts)
        active={c for c in cuts if all(not crosses(c,n) for n in neg)}
        external=active-internal
        hb=support_cohomology(neg,cuts,edges)
        rel=Counter()
        if external:
            check(hb.get(k,0)>=1,'unit_patch_detects_interior_class',neg)
            rel[k]+=hb.get(k-1,0)
            rel[k+1]+=hb.get(k,0)-1
            rel[k+2]+=hb.get(k+1,0)
            mode='primitive_injection'
        else:
            check(hb.get(k,0)==0 and hb.get(k+1,0)==0,'no_equal_degree_target',neg)
            rel[k]+=1+hb.get(k-1,0)
            mode='zero_target'
        rel={q:n for q,n in sorted(rel.items()) if n}
        check(all(q>=2 and q<=5 and n>0 for q,n in rel.items()),'relative_positive_degrees',neg)
        # Long-exact-sequence Euler characteristic, with full H^k of rank one.
        chi_rel=sum(pm(q)*n for q,n in rel.items())
        chi_full=pm(k)
        chi_boundary=sum(pm(q)*n for q,n in hb.items())
        check(chi_rel==chi_full-chi_boundary,'relative_support_euler',neg)
        aggregate.update(rel);types[mode]+=1
        support_records.append({'negative_support':[list(x) for x in neg],
             'full_cohomology':{str(k):1},'boundary_cohomology':hb,
             'restriction_type':mode,'relative_cohomology':rel})
    check(len(support_records)==903,'all_laurent_supports')
    check(support_records[0]['relative_cohomology']=={2:5},'constant_support_relative_control')

    result={
      'status':'proved_for_explicit_cellular_and_formal_localization_models',
      'commit':COMMIT,
      'additional_source_blob':'14f1a7bdd09de6c462d927334f7407d84401e3e5',
      'source_scope':'Full signed loaded octagon, its computed link-chart boundary, and the separately specified polynomial-localization diagram. Not a reconstructed full physical period or Cousin comparison.',
      'integer_full_generator_count':len(interior.cells),
      'integer_boundary_generator_count':len(td),
      'integer_full_degree_ranks':interior.ranks,
      'integer_full_cohomology':{'0':1},
      'integer_boundary_cohomology':{'0':1,'1':5},
      'integer_relative_cohomology':{'2':5},
      'integer_relative_torsion':[],
      'overlap_defect_nonzero_columns':nonzero_defects,
      'overlap_homotopy_nonzero_columns':nonzero_ell,
      'primitive_extension_space':'contractible',
      'primitive_extension':'sum_F (-1)^(|F|(|F|+1)/2) [F,F]',
      'full_to_boundary_map':'Phi=(rho,(Delta rho)H)',
      'relative_reduced_differentials':{'d0':[[1] for _ in cuts],'d1':[[-x for x in row] for row in delta]},
      'cuts':[list(x) for x in cuts],
      'edges':[[list(a),list(b)] for a,b in edges],
      'spanning_tree':[[list(a),list(b)] for a,b in tree],
      'relative_chords':[[list(a),list(b)] for a,b in chords],
      'polynomial_extension_on_H0':'isomorphism; same unlocalized branch-polynomial pair',
      'polynomial_normalized_extension_each_fixed_boundary_marking':'contractible',
      'polynomial_relative_abelian_torsion':[],
      'support_aggregate_one_monomial_per_support_per_branch_mode':dict(sorted(aggregate.items())),
      'support_map_type_counts':dict(types),
      'support_records':support_records,
      'assertions':dict(sorted(COUNTS.items())),
      'total_exact_assertions':sum(COUNTS.values()),
      'proof_not_testing':'The contraction identities prove integral exactness in all displayed cellular degrees. Polynomial exponents are unbounded; the support/cubical-pair argument, unit restriction and long exact sequence provide the all-exponent result. No proof assistant was used.'
    }
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','integer_full_generator_count','integer_boundary_generator_count','integer_relative_cohomology','overlap_defect_nonzero_columns','overlap_homotopy_nonzero_columns','primitive_extension_space','support_aggregate_one_monomial_per_support_per_branch_mode','support_map_type_counts','total_exact_assertions']},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('boundary_interior_extension_certificate.json'))
    args=parser.parse_args()
    main(args.output)

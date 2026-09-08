#!/usr/bin/env python3
"""Audit and repair of source-local overlap homotopies.

Includes a declared independent-normal polynomial lifting test.

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



def pair_local(edge: tuple[Diagonal, Diagonal], cell: Cell) -> Vec:
    """Pair-supported replacement; spectators are unchanged."""
    face, marked = cell
    if not all(c in face for c in edge) or sum(c in marked for c in edge) != 1:
        return {}
    s = next(c for c in edge if c in marked)
    t = next(c for c in edge if c not in marked)
    ff = tuple(c for c in face if c not in edge)
    mm = tuple(c for c in marked if c not in edge)
    sign = -pm(sum(c > s for c in ff) + sum(c > s for c in mm)
               + sum(c < t for c in ff))
    return {(ff, mm): sign}


def overlap_defect(edge, overlap, cell):
    c, d = edge
    return add(project(rho_cell(d, cell), overlap.cellset),
               project(rho_cell(c, cell), overlap.cellset), -1)


# Polynomial coefficient monomials are sorted tuples of diagonal labels.
# An entry (cell, monomial) -> integer represents a free module vector over
# Z[w_d : d a diagonal]. No substitution or numerical sampling is used.
def monomial_product(a, b):
    return tuple(sorted(a + b))


def lift_poly(v, monomial=()):
    return {(cell, monomial): n for cell, n in v.items()}


def poly_apply(table, v):
    out = {}
    for (cell, mon), n in v.items():
        for (target, mon2), a in table.get(cell, {}).items():
            key = (target, monomial_product(mon, mon2))
            out[key] = out.get(key, 0) + n*a
            if not out[key]: del out[key]
    return out


def weighted_differential(obj):
    out = {}
    for cell in obj.cells:
        f, m = cell
        v = {}
        for target, n in obj.d[cell].items():
            ff, mm = target
            mon = () if ff != f else (next(c for c in m if c not in mm),)
            v[(target, mon)] = n
        out[cell] = v
    return out


def weighted_pair(edge, cell):
    v = pair_local(edge, cell)
    if not v:
        return {}
    s = next(c for c in edge if c in cell[1])
    return lift_poly(v, (s,))


def weighted_defect(edge, overlap, cell):
    c, d = edge
    return add(lift_poly(project(rho_cell(d, cell), overlap.cellset), (d,)),
               lift_poly(project(rho_cell(c, cell), overlap.cellset), (c,)), -1)


def localized(cell, forced=()):
    return (set(cell[0]) - set(cell[1])) | set(forced)


def act_poly(g, v, sign=1):
    out = {}
    for (cell, mon), n in v.items():
        target, s = act_cell(g, cell)
        mon2 = tuple(sorted(act_diag(g, c) for c in mon))
        key = (target, mon2)
        out[key] = out.get(key, 0) + sign*s*n
    return {k:n for k,n in out.items() if n}


def transformed_edge(g, edge):
    pair = tuple(act_diag(g, c) for c in edge)
    return tuple(sorted(pair)), (1 if pair[0] < pair[1] else -1)


def run_admissibility(output: Path) -> None:
    ds = tuple((i,j) for i in range(8) for j in range(i+1,8) if j-i not in (1,7))
    cuts = tuple(sorted({normalized(i,i+3) for i in range(8)}))
    edges = tuple(e for e in combinations(cuts,2) if not crosses(*e))
    groups = tuple(product(range(8),(0,1)))
    I = FullLoaded(ds)
    O = {e:Loaded(tuple(d for d in ds if d not in e and all(not crosses(d,c) for c in e)))
         for e in edges}
    empty = ((),())
    wi = weighted_differential(I)
    counts = Counter()
    samples = {}
    maps = {}
    defects = {}
    oldmaps = {}
    weighted_maps = {}
    for c in I.cells:
        check(not apply(I.d,I.d[c]), 'source_d_squared')
        check(not poly_apply(wi,wi[c]), 'independent_normal_d_squared')
        check(add(apply(I.d,I.H[c]),apply(I.H,I.d[c])) ==
              (add({c:1},I.unit,-1) if c==empty else {c:1}), 'source_contraction')
    for edge, ov in O.items():
        m = {c:overlap_defect(edge,ov,c) for c in I.cells}
        h = {c:pair_local(edge,c) for c in I.cells}
        h_old = {c:apply(m,I.H[c]) for c in I.cells}
        h_w = {c:weighted_pair(edge,c) for c in I.cells}
        dw = weighted_differential(ov)
        mw = {c:weighted_defect(edge,ov,c) for c in I.cells}
        maps[edge]=h; defects[edge]=m;oldmaps[edge]=h_old;weighted_maps[edge]=h_w
        difference={c:add(h[c],h_old[c],-1) for c in I.cells}
        second={c:{t:-a for t,a in apply(difference,I.H[c]).items()} for c in I.cells}
        for c in I.cells:
            check(add(apply(ov.d,h[c]),apply(h,I.d[c])) == m[c], 'pair_local_homotopy')
            # d(second)-second*d = new-old, a higher comparison in ordinary complexes.
            check(add(apply(ov.d,second[c]),apply(second,I.d[c]),-1)==difference[c],
                  'old_new_higher_comparison')
            check(add(poly_apply(dw,h_w[c]),poly_apply(h_w,wi[c])) == mw[c],
                  'independent_normal_weighted_homotopy')
            for t,a in h[c].items():
                counts['new_terms']+=1
                check(t in ov.cellset, 'target_actual_overlap')
                check(degree(t)==degree(c)-1, 'homotopy_degree')
                check(set(t[0])==set(c[0])-set(edge) and
                      set(t[1])==set(c[1])-set(edge), 'spectators_unchanged')
                check(localized(c)<=localized(t,edge), 'retained_cut_localizations')
                check(a in (-1,1), 'integral_unit_coefficients')
                s=next(q for q in edge if q in c[1])
                check(Counter(c[1])==Counter(t[1])+Counter([s]), 'weighted_mark_multigrading')
            for t,a in h_old[c].items():
                counts['old_terms']+=1
                if not set(t[0]) <= set(c[0])-set(edge):
                    counts['old_adds_spectator_face']+=1
                    samples.setdefault('old_adds_spectator_face', {'edge':edge,'input':c,'output':t,'coefficient':a})
                if not set(t[1]) <= set(c[1])-set(edge):
                    counts['old_adds_spectator_mark']+=1
                if not localized(c)<=localized(t,edge):
                    counts['old_illegal_coefficient_identity']+=1
                    samples.setdefault('old_illegal_coefficient_identity', {'edge':edge,'input':c,'output':t,'coefficient':a})
        check(not apply(h,I.unit),'unit_preserved')
        for g in groups:
            target_edge, esign = transformed_edge(g,edge)
            # Check support covariance separately; a relabelling bijects the
            # mixed-pair support. Then check all nonzero signed columns.
            source_support={c for c,v in h.items() if v}
            image_support={act_cell(g,c)[0] for c in source_support}
            expected_support={c for c in I.cells if pair_local(target_edge,c)}
            check(image_support==expected_support,'D8_pair_support_covariance')
            for c in source_support:
                gc,sg=act_cell(g,c)
                lhs={t:sg*a for t,a in pair_local(target_edge,gc).items()}
                rhs={t:esign*a for t,a in act_vec(g,h[c]).items()}
                check(lhs==rhs, 'D8_pair_local_equivariance')
                lhsw={t:sg*a for t,a in weighted_pair(target_edge,gc).items()}
                rhsw=act_poly(g,h_w[c],esign)
                check(lhsw==rhsw, 'D8_independent_normal_equivariance')

    found=False
    for edge in edges:
        if found:break
        for g in groups:
            if found:break
            te,sgn=transformed_edge(g,edge)
            for c in I.cells:
                gc,s=act_cell(g,c)
                lhs={t:s*a for t,a in oldmaps[te][gc].items()}
                rhs={t:sgn*a for t,a in act_vec(g,oldmaps[edge][c]).items()}
                if lhs != rhs:
                    samples['old_strict_covariance_failure']={'edge':edge,'g':g,'input':c,
                        'difference':[[t,a] for t,a in add(lhs,rhs,-1).items()]}
                    found=True;break
    check(found,'old_covariance_failure_found')

    for cut in cuts:
        chart=Loaded(tuple(d for d in ds if d!=cut and not crosses(d,cut)))
        chart_dw=weighted_differential(chart)
        sigmas={c:lift_poly(rho_cell(cut,c),(cut,)) for c in I.cells}
        for c in I.cells:
            check(poly_apply(chart_dw,sigmas[c])==poly_apply(sigmas,wi[c]),
                  'weighted_chart_chain_map')
            for target in rho_cell(cut,c):
                check(localized(c)<=localized(target,(cut,)), 'chart_coefficient_localization')
                check(Counter(c[1])==Counter(target[1])+Counter([cut]), 'weighted_chart_multigrading')

    omega_w = {((f,f),tuple(x for x in ds if x not in f)):
                   pm(len(f)*(len(f)+1)//2) for f in I.fs}
    check(not poly_apply(wi,omega_w),'weighted_global_cycle')
    obstructions=[]
    for edge,ov in O.items():
        mpoly={c:lift_poly(defects[edge][c]) for c in I.cells}
        image=poly_apply(mpoly,omega_w)
        observed={mon:n for (cell,mon),n in image.items() if cell==empty}
        c,d=edge
        expected={tuple(x for x in ds if x!=d):1,
                  tuple(x for x in ds if x!=c):-1}
        check(observed==expected and bool(observed), 'unweighted_maps_polynomial_obstruction')
        # The corrected weighted mismatch vanishes on this global cycle.
        corrected={x:weighted_defect(edge,ov,x) for x in I.cells}
        check(not poly_apply(corrected,omega_w),'weighted_boundary_agreement_on_cycle')
        check(not poly_apply(weighted_maps[edge],omega_w),'weighted_unit_overlap_zero')
        obstructions.append({'edge':edge, 'factor':'(w_c-w_d)*product_{a not in {c,d}} w_a'})

    forced=0
    for edge in edges:
        for cell,val in maps[edge].items():
            if not val:continue
            f,m=cell
            unmarked_cut=next(c for c in edge if c not in m)
            precursor=(tuple(c for c in f if c!=unmarked_cut),m)
            check(apply(maps[edge],I.d[precursor])==defects[edge][precursor],
                  'unique_pair_supported_coefficient')
            check(sum(bool(maps[edge].get(t)) for t in I.d[precursor])==1,
                  'unique_allowed_contribution')
            forced+=1

    e=((0,3),(0,5)); cell=(((0,4),),()); target=(((0,4),),((0,4),))
    check(oldmaps[e][cell].get(target)==1,'minimal_old_spectator_example')
    check((0,4) in localized(cell) and (0,4) not in localized(target,e),
          'minimal_illegal_inverse_example')
    check(not maps[e][cell],'new_map_removes_nonlocal_example')
    result={
        'status':'unit-coefficient pair-local repair; independent-normal factors require weighted chart maps',
        'commit':COMMIT,
        'scope':'Explicit signed loaded cellular complexes. Forced Cut localizations are retained in boundary coefficients. The independent-normal polynomial lift is a declared test, not an identified full physical PC/Rees correspondence.',
        'full_generators':len(I.cells),'compatible_pairs':len(edges),
        'old_new_term_counts':dict(counts),'counterexamples':samples,
        'local_coefficients_forced':forced,
        'new_homotopy_equation':'d_E ell_pair + ell_pair d_I = Delta rho',
        'new_support':'both Cuts present, exactly one marked; delete the pair; every spectator face and mark unchanged',
        'new_D8_covariance':'strict and integral; no averaging',
        'new_coefficient_localizations':'R_(F-M) -> R_(pair union (Fprime-Mprime)); inclusions only',
        'independent_normal_test':'d_w=radial+sum_b w_b normal_b, over Z[w_d]',
        'fixed_unweighted_chart_obstructions':obstructions,
        'weighted_repair':'sigma_c=w_c rho_c; ell_w on a mixed pair cell is w_(marked Cut) times ell_pair',
        'weighted_repair_multigrading':'deg(w_c)=e_c, deg([F,M])=sum_{m in M}e_m; all corrected maps degree zero',
        'specialization':'w_c=1 recovers unit-coefficient repair; no w_c was inverted or equated in the polynomial calculation',
        'limitations':['No source proof that d_w is the complete physical differential or that sigma_c is the complete physical residue.',
           'Fixed full Rees boundary values are not supplied by unit-coefficient normalization.',
           'No identification of the cellular conductor bicomplex with earlier derived-section polynomial model.',
           'No RH implication; no ordinary integer-prime obstruction asserted.'],
        'assertions':dict(sorted(COUNTS.items())), 'total_exact_assertions':sum(COUNTS.values()),
    }
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','full_generators','compatible_pairs','old_new_term_counts',
        'local_coefficients_forced','total_exact_assertions']},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('source_admissible_overlap_certificate.json'))
    args=parser.parse_args()
    run_admissibility(args.output)

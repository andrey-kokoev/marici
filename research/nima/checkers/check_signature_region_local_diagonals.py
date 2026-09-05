#!/usr/bin/env python3
"""Finite falsification of occupied-signature regional local-diagonal completeness."""
from itertools import combinations
import json
from pathlib import Path


def diagonals(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)
            if j != i+1 and not (i == 0 and j+1 == n)]

def crosses(a,b):
    i,j=a; k,l=b
    return (i<k<j<l) or (k<i<l<j)

def inside(c,v):
    return c[0] < v < c[1]

def witness(c,d):
    return d[1] if d[0] in c else d[0]

def signature(D,d):
    return tuple(inside(c,witness(c,d)) for c in D)

def boundary_signature(n,D,i):
    succ=(i+1)%n
    return tuple(inside(c, succ if i in c else i) for c in D)

def compatible(D,d):
    return d not in D and all(not crosses(d,c) for c in D)

def retained(n,c,side):
    return {v for v in range(n) if v in c or inside(c,v) == side}

def dissections(ds):
    out=[]
    def visit(k, chosen):
        if k == len(ds): out.append(tuple(chosen)); return
        visit(k+1,chosen)
        d=ds[k]
        if all(not crosses(d,c) for c in chosen):
            chosen.append(d); visit(k+1,chosen); chosen.pop()
    visit(0,[])
    return out

def check(nmax=9):
    checked_regions=checked_dissections=0
    boundaryless_regions=0
    checked_boundary_pairs=0
    comparable_constraint_pairs=0
    minimal_excluding_cuts_checked=0
    failures=[]
    for n in range(3,nmax+1):
        ds=diagonals(n)
        for D in dissections(ds):
            checked_dissections += 1
            opts=[d for d in ds if compatible(D,d)]
            boundary_signatures={boundary_signature(n,D,i) for i in range(n)}
            groups={}
            for d in opts: groups.setdefault(signature(D,d),[]).append(d)
            for sig,region_ds in groups.items():
                checked_regions += 1
                if sig not in boundary_signatures:
                    boundaryless_regions += 1
                vertices=[v for v in range(n) if all(
                    v in c or inside(c,v) == side for c,side in zip(D,sig))]
                retained_sides=[retained(n,c,side) for c,side in zip(D,sig)]
                for v in set(range(n))-set(vertices):
                    excluding=[(c,C) for c,C in zip(D,retained_sides) if v not in C]
                    minimum=min(len(C) for _,C in excluding)
                    for c,C in excluding:
                        if len(C) != minimum:
                            continue
                        minimal_excluding_cuts_checked += 1
                        if not set(c) <= set(vertices):
                            failures.append({"kind":"minimal_excluding_cut_not_active",
                                "n":n,"D":D,"signature":sig,"vertex":v,
                                "cut":c,"retained":sorted(C),"vertices":vertices})
                            return (checked_dissections,checked_regions,
                                boundaryless_regions,checked_boundary_pairs,
                                comparable_constraint_pairs,
                                minimal_excluding_cuts_checked,failures)
                for i,c in enumerate(D):
                    for e in D[i+1:]:
                        C=retained(n,c,sig[i])
                        E=retained(n,e,sig[D.index(e)])
                        if len(C & E) >= 2 and (set(range(n))-C) & (set(range(n))-E):
                            comparable_constraint_pairs += 1
                            if not (C <= E or E <= C):
                                failures.append({"kind":"incomparable_oriented_constraints",
                                    "n":n,"D":D,"signature":sig,"cuts":[c,e],
                                    "retained":[sorted(C),sorted(E)]})
                                return (checked_dissections,checked_regions,
                                    boundaryless_regions,checked_boundary_pairs,
                                    comparable_constraint_pairs,
                                    minimal_excluding_cuts_checked,failures)
                for k,a in enumerate(vertices):
                    b=vertices[(k+1)%len(vertices)]
                    edge=tuple(sorted((a,b)))
                    checked_boundary_pairs += 1
                    ambient=(edge[1] == edge[0]+1 or edge == (0,n-1))
                    if not ambient and edge not in D:
                        failures.append({"kind":"unclassified_boundary_pair",
                            "n":n,"D":D,"signature":sig,
                            "vertices":vertices,"boundary_pair":edge})
                        return (checked_dissections,checked_regions,
                            boundaryless_regions,checked_boundary_pairs,
                            comparable_constraint_pairs,
                            minimal_excluding_cuts_checked,failures)
                rank={v:i for i,v in enumerate(vertices)}
                realized={(rank[i],rank[j]) for i,j in region_ds}
                standard=set(diagonals(len(vertices)))
                if realized != standard:
                    failures.append({"kind":"local_diagonal_mismatch",
                        "n":n,"D":D,"signature":sig,
                        "vertices":vertices,"realized":sorted(realized),
                        "standard":sorted(standard),
                        "missing":sorted(standard-realized),
                        "nonstandard":sorted(realized-standard)})
                    return (checked_dissections,checked_regions,
                        boundaryless_regions,checked_boundary_pairs,
                        comparable_constraint_pairs,
                        minimal_excluding_cuts_checked,failures)
    return (checked_dissections,checked_regions,boundaryless_regions,
        checked_boundary_pairs,comparable_constraint_pairs,
        minimal_excluding_cuts_checked,failures)

if __name__ == "__main__":
    nd,nr,nb,npairs,ncomparable,nminimal,failures=check()
    result={"schema":"marici.signature_region_local_diagonals.v2",
            "n_max":9,"dissections_checked":nd,"occupied_regions_checked":nr,
            "boundaryless_occupied_regions":nb,
            "boundary_pairs_checked":npairs,
            "comparable_constraint_pairs_checked":ncomparable,
            "minimal_excluding_cuts_checked":nminimal,
            "status":"pass" if not failures else "fail","first_failure":failures[:1]}
    out=Path("research/nima/results/signature_region_local_diagonals.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result))
    raise SystemExit(0 if not failures else 1)

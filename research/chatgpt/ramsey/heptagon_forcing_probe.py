#!/usr/bin/env python3
"""Bounded SAT probes of the 22-vertex parity-closed-heptagon conjecture.
Run with: uv run --with python-sat==1.9.dev22 -- python <this file> --mode two-zero
A solver UNSAT response is not called independently certified unless a proof is checked.
"""
import argparse
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import threading
import time
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver
from pauli_realization_audit import binary_rank, encode_graph6, triangle_free, independent_witness
from heptagon_profile import PROFILE, profile_orbit, ordered_types

HERE=Path(__file__).resolve().parent

def build_formula(mode,n=22,strengthen=False,lex=False):
    assert n==22,'These modes and symmetry reductions are specific to order 22'
    pool=IDPool();pairs=list(combinations(range(n),2));edge={p:pool.id(('edge',)+p) for p in pairs}
    E=lambda i,j:edge[tuple(sorted((i,j)))]
    fixed={E(i,j):j-i==1 or(i==0 and j==6) for i,j in combinations(range(7),2)}
    zero_count=2 if mode=='two-zero' else 1
    for v in range(7,7+zero_count):
        for i in range(7):fixed[E(i,v)]=False
    clauses=[[v if value else -v] for v,value in fixed.items()]
    def add(literals):
        reduced=[]
        for lit in literals:
            if abs(lit) in fixed:
                if fixed[abs(lit)]==(lit>0):return
            else:reduced.append(lit)
        clauses.append(reduced)
    for triple in combinations(range(n),3):add([-E(i,j) for i,j in combinations(triple,2)])
    for seven in combinations(range(n),7):add([E(i,j) for i,j in combinations(seven,2)])
    # Outside neighbors in C7 are an independent even-sized set: only 0 or 2.
    types=[()]+[pair for pair in combinations(range(7),2) if not fixed[E(*pair)]]
    selectors={}
    for v in range(7,n):
        lits=[pool.id(('type',v,k)) for k in range(len(types))];selectors[v]=lits
        clauses.extend(CardEnc.equals(lits,bound=1,vpool=pool,encoding=EncType.seqcounter).clauses)
        for k,pair in enumerate(types):
            for i in range(7):add([-lits[k],E(i,v) if i in pair else -E(i,v)])
    if mode=='other-profile':
        for profile in profile_orbit():
            clauses.append([-selectors[v][k]for v,k in zip(range(7,n),ordered_types(profile))])
    elif mode=='fixed-profile':
        for v,k in zip(range(7,n),ordered_types()):clauses.append([selectors[v][k]])
    # Safe symmetry break: permute outside vertices so their C7-neighborhood types are sorted.
    for v in range(7,n-1):
        for a in range(len(types)):
            for b in range(a):clauses.append([-selectors[v][a],-selectors[v+1][b]])
    if lex:
        # Lex-leaders for adjacent transpositions within an equal-type block.
        # A lexicographically least upper-triangle adjacency string in each
        # type-preserving permutation orbit satisfies all these comparisons.
        for i in range(7,n-1):
            j=i+1;prefix=pool.id(('same-type',i))
            for k in range(len(types)):clauses.append([-selectors[i][k],-selectors[j][k],prefix])
            for position,v in enumerate(v for v in range(7,n)if v not in (i,j)):
                x,y=E(i,v),E(j,v);following=pool.id(('prefix-equal',i,position))
                clauses.extend([[-prefix,-x,y],[-prefix,x,y,following],[-prefix,-x,-y,following]])
                prefix=following
    # Triangle-free + no independent seven implies maximum degree six.
    for v in range(n):
        unknown=[E(v,u)for u in range(n)if u!=v and E(v,u) not in fixed]
        true_count=sum(fixed.get(E(v,u),False)for u in range(n)if u!=v)
        clauses.extend(CardEnc.atmost(unknown,bound=6-true_count,vpool=pool,encoding=EncType.seqcounter).clauses)
    if strengthen:
        # These redundant cuts use the known Ramsey bounds R(3,6)=18 and R(3,4)=9.
        # A vertex's nonneighbors cannot contain an independent six-set.
        for v in range(n):
            unknown=[E(v,u)for u in range(n)if u!=v and E(v,u) not in fixed]
            true_count=sum(fixed.get(E(v,u),False)for u in range(n)if u!=v)
            bound=n-18-true_count
            if bound>0:clauses.extend(CardEnc.atleast(unknown,bound=bound,vpool=pool,encoding=EncType.seqcounter).clauses)
        # Four outside vertices of the same nonzero type are independent, and
        # C7 minus that pair has an independent triple: forbid class size four.
        for k in range(1,len(types)):
            clauses.extend(CardEnc.atmost([selectors[v][k]for v in range(7,n)],bound=3,vpool=pool,encoding=EncType.seqcounter).clauses)
        # Common nonneighbors of an independent triple induce a (3,4)-graph,
        # hence have order at most eight.
        for triple in combinations(range(7),3):
            if any(fixed[E(i,j)]for i,j in combinations(triple,2)):continue
            common=[]
            for v in range(7,n):
                c=pool.id(('common',triple,v));common.append(c)
                for k,pair in enumerate(types):
                    clauses.append([-selectors[v][k],c if set(pair).isdisjoint(triple) else -c])
            clauses.extend(CardEnc.atmost(common,bound=8,vpool=pool,encoding=EncType.seqcounter).clauses)
    if mode=='sparse':
        # A non-6-regular graph with maximum degree six has at most 65 edges.
        unknown=[v for v in edge.values()if v not in fixed]
        clauses.extend(CardEnc.atmost(unknown,bound=65-sum(fixed.values()),vpool=pool,encoding=EncType.seqcounter).clauses)
    return clauses,pool.top,edge,types

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=['two-zero','sparse','baseline','other-profile','fixed-profile'],default='two-zero')
    parser.add_argument('--seconds',type=float,default=60);parser.add_argument('--save-cnf',action='store_true')
    parser.add_argument('--lex',action='store_true');parser.add_argument('--strengthen',action='store_true');parser.add_argument('--solver',choices=['glucose4','cadical195'],default='glucose4')
    parser.add_argument('--conflicts',type=int,default=1000000);args=parser.parse_args()
    suffix=args.mode+('-strengthened' if args.strengthen else '')+('-lex' if args.lex else '')+('-cadical' if args.solver=='cadical195' else '')
    started=time.monotonic();clauses,nvars,edges,types=build_formula(args.mode,strengthen=args.strengthen,lex=args.lex)
    text=f'p cnf {nvars} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n'for c in clauses)
    print(args.mode,'variables',nvars,'clauses',len(clauses),'building seconds',round(time.monotonic()-started,2),flush=True)
    artifacts=HERE/'results/heptagon-proofs';artifacts.mkdir(parents=True,exist_ok=True)
    cnf_path=artifacts/f'heptagon-{suffix}.cnf'
    if args.save_cnf:cnf_path.write_bytes(text.encode())
    with Solver(name=args.solver,bootstrap_with=clauses,with_proof=True)as solver:
        timer=None
        if args.solver=='glucose4':
            timer=threading.Timer(args.seconds,solver.interrupt);timer.daemon=True;timer.start()
        else:solver.conf_budget(args.conflicts)
        start=time.monotonic()
        try:answer=solver.solve_limited(expect_interrupt=timer is not None)
        finally:
            if timer is not None:timer.cancel()
        result={'mode':args.mode,'vertices':22,'strengthened':args.strengthen,'equal_type_lex':args.lex,
                'seconds_limit':args.seconds if timer else None,'conflict_budget':args.conflicts if not timer else None,
                'solve_seconds':time.monotonic()-start,
                'variables':nvars,'clauses':len(clauses),'cnf_sha256':sha256(text.encode()).hexdigest(),
                'status':'SAT' if answer is True else 'UNSAT' if answer is False else 'UNKNOWN_BUDGET',
                'solver':args.solver+' via python-sat 1.9.dev22','proof_independently_checked':False,'statistics':solver.accum_stats()}
        if answer:
            model={v for v in solver.get_model()if v>0};rows=[0]*22
            for(i,j),v in edges.items():
                if v in model:rows[i]|=1<<j;rows[j]|=1<<i
            assert triangle_free(rows)and independent_witness(rows,7)is None
            assert all((r&127).bit_count()%2==0 for r in rows)
            result.update(graph6=encode_graph6(rows),rank=binary_rank(rows),degrees=[r.bit_count()for r in rows],
                          zero_neighbor_vertices=[i for i in range(7,22)if not(rows[i]&127)])
        elif answer is False:
            proof=solver.get_proof();proof_path=artifacts/f'heptagon-{suffix}.drat'
            proof_bytes=('\n'.join(proof)+'\n').encode();proof_path.write_bytes(proof_bytes)
            cnf_path.write_bytes(text.encode())
            result.update(proof_file=proof_path.relative_to(HERE).as_posix(),cnf_file=cnf_path.relative_to(HERE).as_posix(),
                          proof_sha256=sha256(proof_bytes).hexdigest())
        (HERE/f'heptagon-{suffix}-probe.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()

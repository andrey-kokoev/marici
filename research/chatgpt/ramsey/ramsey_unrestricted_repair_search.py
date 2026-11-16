#!/usr/bin/env python3
"""Bound the old-edge edit cost of arbitrary Ramsey-preserving 21->22 repairs."""
import argparse
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from pysat.formula import IDPool
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver
from heptagon_near_extremal_counterexample import graph
from pauli_realization_audit import triangle_free, independent_witness, binary_rank, encode_graph6
HERE=Path(__file__).resolve().parent

def build(budget):
    base=graph();pool=IDPool();edges={p:pool.id(p)for p in combinations(range(22),2)}
    E=lambda i,j:edges[tuple(sorted((i,j)))]
    clauses=[[-E(i,j)for i,j in combinations(triple,2)]for triple in combinations(range(22),3)]
    clauses.extend([[E(i,j)for i,j in combinations(seven,2)]for seven in combinations(range(22),7)])
    for v in range(22):clauses.extend(CardEnc.atmost([E(v,u)for u in range(22)if u!=v],bound=6,vpool=pool,encoding=EncType.seqcounter).clauses)
    modifications=[-E(i,j)if base[i]>>j&1 else E(i,j)for i,j in combinations(range(21),2)]
    clauses.extend(CardEnc.atmost(modifications,bound=budget,vpool=pool,encoding=EncType.seqcounter).clauses)
    # Safe even for an isolated new vertex: if it has any neighbor, translate
    # the circulant so that 0 is one. Otherwise all these clauses are true.
    clauses.extend([[E(0,21),-E(i,21)]for i in range(1,21)])
    return clauses,edges,pool.top

def main():
    p=argparse.ArgumentParser();p.add_argument('--budget',type=int,default=11);p.add_argument('--conflicts',type=int,default=1000000);args=p.parse_args()
    clauses,edges,nvars=build(args.budget);print('formula',nvars,len(clauses),flush=True)
    with Solver(name='cadical195',bootstrap_with=clauses,with_proof=True)as solver:
        solver.conf_budget(args.conflicts);answer=solver.solve_limited()
        result={'vertices_before':21,'vertices_after':22,'old_edge_edit_budget':args.budget,'degree_regular_required':False,
                'variables':nvars,'clauses':len(clauses),'proof_independently_checked':False,
                'status':'SAT'if answer else'UNSAT'if answer is False else'UNKNOWN_BUDGET','statistics':solver.accum_stats()}
        if answer:
            model={v for v in solver.get_model()if v>0};rows=[0]*22;base=graph()
            for(i,j),v in edges.items():
                if v in model:rows[i]|=1<<j;rows[j]|=1<<i
            assert triangle_free(rows)and independent_witness(rows,7)is None
            added=[(i,j)for i,j in combinations(range(21),2)if not(base[i]>>j&1)and rows[i]>>j&1]
            removed=[(i,j)for i,j in combinations(range(21),2)if base[i]>>j&1 and not(rows[i]>>j&1)]
            assert len(added)+len(removed)<=args.budget
            result.update(graph6=encode_graph6(rows),added_old_edges_0based=added,removed_old_edges_0based=removed,
                          new_vertex_neighbors_0based=[v for v in range(21)if rows[21]>>v&1],
                          old_edge_edit_count=len(added)+len(removed),degrees=[r.bit_count()for r in rows],binary_rank=binary_rank(rows))
        elif answer is False:
            root=HERE/'results/ramsey-repair-proofs';root.mkdir(parents=True,exist_ok=True)
            cnf=root/f'unrestricted-repair-{args.budget}.cnf';proof=cnf.with_suffix('.drat')
            text=(f'p cnf {nvars} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n'for c in clauses)).encode()
            proof_bytes=('\n'.join(solver.get_proof())+'\n').encode();cnf.write_bytes(text);proof.write_bytes(proof_bytes)
            result.update(cnf_file=cnf.relative_to(HERE).as_posix(),proof_file=proof.relative_to(HERE).as_posix(),
                          cnf_sha256=sha256(text).hexdigest(),proof_sha256=sha256(proof_bytes).hexdigest())
        (HERE/f'ramsey-unrestricted-repair-{args.budget}.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()

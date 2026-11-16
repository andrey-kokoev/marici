#!/usr/bin/env python3
"""Enumerate the fixed-profile completions; certify exhaustion by fresh UNSAT.
No catalogue is read. Run in the pinned python-sat environment.
"""
from hashlib import sha256
import json
from pysat.solvers import Solver
from heptagon_forcing_probe import HERE, build_formula
from heptagon_profile import PROFILE, PAIRS
from pauli_realization_audit import encode_graph6, binary_rank, triangle_free, independent_witness
from pauli_low_cost_structure import parity_closed_heptagons, relation_certificate

def main():
    clauses,nvars,edges,_=build_formula('fixed-profile',strengthen=False,lex=True)
    records=[];blockers=[]
    with Solver(name='cadical195',bootstrap_with=clauses)as solver:
        while True:
            solver.conf_budget(1000000);answer=solver.solve_limited()
            if answer is None:raise RuntimeError('Budget exhausted; enumeration is NOT complete')
            if not answer:break
            model={lit for lit in solver.get_model()if lit>0};rows=[0]*22
            for(i,j),v in edges.items():
                if v in model:rows[i]|=1<<j;rows[j]|=1<<i
            assert triangle_free(rows)and independent_witness(rows,7)is None
            assert sorted(r.bit_count()for r in rows)==[6]*22
            rank=binary_rank(rows);assert rank==16
            heptagons,_=parity_closed_heptagons(rows);assert len(heptagons)==4
            records.append({'graph6':encode_graph6(rows),'rank':rank,
                            'parity_closed_cycles_0based':list(heptagons.values()),
                            'compression_certificate':relation_certificate(rows,heptagons)})
            blocker=[-v if v in model else v for v in edges.values()]
            blockers.append(blocker);solver.add_clause(blocker)
            print('completion',len(records),'rank',rank,flush=True)
    # Do NOT check a cumulative incremental proof against a mismatched formula.
    # Start a fresh proof-producing solve with ALL model blockers as input.
    complete=clauses+blockers
    with Solver(name='cadical195',bootstrap_with=complete,with_proof=True)as solver:
        solver.conf_budget(1000000);answer=solver.solve_limited()
        assert answer is False,'Fresh exhaustion check did not finish UNSAT'
        proof=('\n'.join(solver.get_proof())+'\n').encode();stats=solver.accum_stats()
    text=(f'p cnf {nvars} {len(complete)}\n'+''.join(' '.join(map(str,c))+' 0\n'for c in complete)).encode()
    root=HERE/'results/heptagon-proofs';root.mkdir(parents=True,exist_ok=True)
    cnf=root/'heptagon-profile-completions.cnf';drat=cnf.with_suffix('.drat')
    cnf.write_bytes(text);drat.write_bytes(proof)
    result={'scope':'Exhaustive labelled completions of one fixed cycle-incidence profile, modulo the stated equal-type lex symmetry. No nonisomorphism claim.',
            'strengthened':False,'equal_type_lex':True,
            'profile_pairs_0based':PAIRS,'profile':PROFILE,'completion_count':len(records),'records':records,
            'status':'UNSAT','meaning':'No additional edge assignments survive after blocking the listed complete graph assignments.',
            'solver':'cadical195 via python-sat 1.9.dev22','statistics':stats,
            'proof_independently_checked':False,'cnf_file':cnf.relative_to(HERE).as_posix(),
            'proof_file':drat.relative_to(HERE).as_posix(),'cnf_sha256':sha256(text).hexdigest(),'proof_sha256':sha256(proof).hexdigest()}
    (HERE/'heptagon-profile-completions.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Completed:',len(records),'labelled completions; fresh exhaustion proof saved.',flush=True)

if __name__=='__main__':main()

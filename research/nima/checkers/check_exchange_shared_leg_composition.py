"""Exact rectangle hostile for invertible shared-leg exchange factorization."""
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
out=ROOT/'research/nima/results/exchange-shared-leg-composition.json'
out.unlink(missing_ok=True)
# Rerun the exact raw-coordinate exchange/preparation checker and reuse its law.
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_matrix_leg_exchange_closure.py'))
exchange=prior['exchange']; anchor=prior['anchor']; budget=prior['budget']
count=0
for size,offset in ((11,0),(4,121)):
    def port(i,j): return offset+size*i+j
    for i in range(1,size):
        for j in range(1,size):
            # Hypothesis H_ij=Y_j X_i requires
            # H_ij^-1 H_0j H_00^-1 H_i0=I. Each exchange is self-inverse.
            history=[port(i,0),port(0,0),port(0,j),port(i,j)]
            assert len(set(history))==4
            z=[F(0)]*16; w=[F(0)]*137; w[history[0]]=1
            initial_z=z.copy(); initial_w=w.copy()
            initial_anchor=anchor(z,w); initial_budget=budget(z,w)
            for event in history:
                z,w=exchange(z,w,event)
                assert anchor(z,w)==initial_anchor
                assert budget(z,w)==initial_budget
            # The first port is emptied and never addressed again in this word.
            assert w[history[0]]==0 and initial_w[history[0]]==1
            assert (z,w)!=(initial_z,initial_w)
            # Actual temporal inversion, in reverse event order, DOES recover state.
            for event in reversed(history): z,w=exchange(z,w,event)
            assert z==initial_z and w==initial_w
            count+=1
assert count==109
result={
 'status':'passed',
 'classification':'exchange_slot_operators_fail_shared_leg_rectangle_factorization',
 'arithmetic':'exact rational',
 'checks':{'prior_exact_exchange_checker_rerun':True,'all109_rectangles_nonidentity':True,
           'anchor_and_budget_preserved':True,'true_reverse_history_recovers_state':True},
 'rectangle_count':count,
 'record_readout':{'initial_first_port':1,'after_rectangle':0,'after_reverse_history':1},
 'conclusion':'The addressed exchanges cannot be H_ij=Y_j X_i for invertible shared-leg maps on the same joint state space. They do compose as ordered experimental events with attached memory, not as that strict representation of native composite paths.',
 'scope':'Same-state-space invertible leg factorization with fixed reference; no exclusion of larger intermediate spaces, noninvertible/dilated maps or higher transported witness actions.',
 'next_falsifier':'Implement an explicit labelled-experiment compiler preserving source provenance, reference transport and event histories; reject any request to flatten a native rectangle into an identity pulse word.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

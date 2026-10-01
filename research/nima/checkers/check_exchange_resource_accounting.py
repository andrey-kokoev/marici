# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Ideal oscillator resource ledger; excludes unmodelled apparatus overhead."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import io
import json
import runpy
import numpy as np

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
out=ROOT/'research/nima/results/exchange-resource-accounting.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    audit=runpy.run_path(str(HERE/'check_source_exchange_end_to_end.py'))
ex=audit['ex']; prepared=audit['prepared']; final=audit['rectangle']; word=audit['word']
x0=ex.state(prepared); x1=ex.state(final); tol=1e-10
# X means with vacuum P means/covariance: coherent excitation N=||Xmean||^2/2.
N0=float(x0@x0/2); N1=float(x1@x1/2)
exact=sum((audit['gamma']*r)**2/F(2) for r in audit['raw'])
assert abs(N0-float(exact))<tol and abs(N1-N0)<tol
Nc=float(x1[:16]@x1[:16]/2); Nr=float(x1[16:]@x1[16:]/2)
assert Nc>1e-6 and abs(Nc+Nr-N0)<tol
# Reset records by swapping them with fresh vacuum environmental modes.
record_reset=np.r_[x1[:16],np.zeros(137)]
record_environment=x1[16:].copy()
assert abs(record_reset@record_reset/2+record_environment@record_environment/2-N0)<tol
assert np.linalg.norm(record_reset)>1e-6
# Repreparing records alone leaves the previously excited carrier behind.
naive_reprepare=np.r_[x1[:16],x0[16:]]
assert np.linalg.norm(naive_reprepare-x0)>1e-6
assert abs(naive_reprepare@naive_reprepare/2-(N0+Nc))<tol
naive_anchor=naive_reprepare[:16]+ex.U.T@naive_reprepare[16:]
assert np.linalg.norm(naive_anchor-prepared.anchor)>1e-6
# A full vacuum-ancilla swap resets the device but transfers its complete mean
# to the environment. It has not erased that state from the enlarged system.
device=np.zeros(153); environment=x1.copy()
assert abs(device@device/2+environment@environment/2-N0)<tol
assert np.max(np.abs(environment-x1))==0
# Reverse the recorded word instead: exact ideal recovery with no state discard.
recovered=ex.run(final,reversed(word))
assert np.max(np.abs(ex.state(recovered)-x0))<tol
assert len(recovered.history)==8

# H_control=hbar*kappa(t)*b^dagger b. For an isolated ideal pulse, occupation
# of b is constant. Ramping kappa from0 to k and back gives cancelling work;
# this is not a model of controller losses or phase-reference resources.
packet=prepared; switching=[]
for event in word:
    i=ex.index[event.instrument_label]
    x=ex.state(packet)
    d=np.r_[ex.U[i],-np.eye(137)[i]]/np.sqrt(2)
    occupation=float((d@x)**2/2)
    after=ex.run(packet,[event]); after_occupation=float((d@ex.state(after))**2/2)
    assert abs(after_occupation-occupation)<tol
    kappa=2.5  # declared angular-frequency unit; physical clock not inferred
    work_on=kappa*occupation; work_off=-kappa*occupation
    assert abs(work_on+work_off)<tol
    switching.append({'difference_mode_N':occupation,'work_on_over_hbar':work_on,'work_off_over_hbar':work_off})
    packet=after
# Simple loss dilation for the measured port preserves system+environment energy.
eta=audit['detector']['eta']; m=x0[16+audit['port']]
transmitted=np.sqrt(eta)*m; lost=np.sqrt(1-eta)*m
assert abs((transmitted**2+lost**2)/2-m*m/2)<tol

result={
 'status':'passed','classification':'conditional_exchange_preparation_reset_and_control_resource_ledger',
 'tolerance':tol,
 'coherent_excitation':{'initial_exact':str(exact),'initial':N0,'after_exchange':N1,
                        'carrier_after_rectangle':Nc,'records_after_rectangle':Nr,
                        'after_record_only_reset_and_reprepare':float(naive_reprepare@naive_reprepare/2)},
 'pulse_switching_ideal_work_over_hbar':switching,
 'checks':{'native_preparation_excitation':True,'record_only_reset_not_fresh':True,
           'reset_environment_budget':True,'reverse_history_recovery':True,
           'ideal_control_switching_work_cancellation':True,'detector_loss_dilation_budget':True},
 'conclusion':'Exchange conserves the declared oscillator excitation, not an entire apparatus resource budget. Record-only reset fails to restore the source preparation; full swap-reset transfers state and energy to an environment. Ideal pulse switching work cancels, but controller and phase-reference costs remain unmodelled.',
 'uncosted':['preparation inefficiency','vacuum ancilla production/reuse','environment disposal or recovery',
             'controller losses and timing','local oscillator/phase monitor','electronics and detector reset'],
 'physical_energy_contract':'For equal independently calibrated frequency omega: E_excess=hbar*omega*N. Unequal frequencies or pumped conversions require a different work model.',
 'next_falsifier':'Consolidate the checked conditional chain and explicitly report remaining native-selection and physical-normalization gates, without treating ideal reversible operations as a complete resource model.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

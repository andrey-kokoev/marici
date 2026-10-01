# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Conditional labelled-source adapter, reference transport and signed echo.

No physical identification of the supplied scalar amplitudes is assumed.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
import io
import json
import runpy
import numpy as np

ROOT=Path(__file__).resolve().parents[3]
output=ROOT/'research/nima/results/source-exchange-contract.json'
output.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    old=runpy.run_path(str(Path(__file__).with_name('check_137_closed_record_stationarity.py')))
tol=1e-10
G=10*np.eye(4)+np.ones((4,4))
metric=np.kron(G,G)
C=np.linalg.cholesky(metric).T
basis=np.eye(4)

def source(ref_a=(0,1),ref_b=(0,1)):
    ea=[e for e in product(range(4),repeat=2) if e[0]!=e[1] and e!=ref_a]
    eb=[e for e in product(range(4),repeat=2) if e[0]!=e[1] and e!=ref_b]
    labels=[('a',a,b) for a,b in product(ea,eb)]
    labels += [('s',a,b) for a,b in product(range(4),repeat=2)]
    features=[]
    for tag,a,b in labels:
        va=basis[a] if tag=='s' else basis[a[1]]-basis[a[0]]
        vb=basis[b] if tag=='s' else basis[b[1]]-basis[b[0]]
        features.append(np.kron(va,vb))
    features=np.array(features)
    norms=np.sqrt(np.einsum('ij,jk,ik->i',features,metric,features))
    return labels,features,(features@C.T)/norms[:,None],norms

labels,features,U,norms=source()
assert len(set(labels))==137
assert np.max(np.abs(U-old['U']))<tol
assert np.max(np.abs(norms[:121]-20))<tol
assert np.max(np.abs(norms[121:]-11))<tol
# Feature compression is not record identification: simultaneous arrow reversal
# gives exactly the same feature but a distinct retained record port.
i=labels.index(('a',(0,2),(0,2)))
j=labels.index(('a',(2,0),(2,0)))
assert i!=j and np.array_equal(features[i],features[j])

rng=np.random.default_rng(137)
z=rng.normal(size=16); w=rng.normal(size=137); q=C@z
assert np.max(np.abs(U@q-(features@metric@z)/norms))<tol
assert abs(q@q-z@metric@z)<tol

def event(q,w,k,u=U):
    delta=w[k]-u[k]@q
    nxt=w.copy(); nxt[k]-=delta
    return q+u[k]*delta,nxt

def word(q,w,history,u=U):
    q=q.copy(); w=w.copy()
    for k in history: q,w=event(q,w,k,u)
    return q,w

# Raw tensor update and whitened exchange agree, for every labelled port.
for k in range(137):
    delta=w[k]-U[k]@q
    z_next=z+features[k]*delta/norms[k]
    q_next,w_next=event(q,w,k)
    assert np.max(np.abs(C@z_next-q_next))<tol
    assert abs(w_next[k]-(features[k]@metric@z)/norms[k])<tol
    assert abs(q_next@q_next+w_next@w_next-(q@q+w@w))<tol
# Equal features still address different retained records and different operations.
qa,wa=event(q,w,i); qb,wb=event(q,w,j)
assert np.linalg.norm(np.r_[qa-qb,wa-wb])>1e-5

# Relabellings include moving the distinguished reference, not just its stabilizer.
transports=[((0,1,3,2),(0,1,2,3)),((1,2,3,0),(2,0,3,1)),((3,2,1,0),(1,0,2,3))]
for pa,pb in transports:
    refa=(pa[0],pa[1]); refb=(pb[0],pb[1])
    newlabels,_,newU,_=source(refa,refb)
    lookup={label:k for k,label in enumerate(newlabels)}
    def move(label):
        tag,a,b=label
        if tag=='s': return tag,pa[a],pb[b]
        return tag,tuple(pa[t] for t in a),tuple(pb[t] for t in b)
    perm=np.array([lookup[move(label)] for label in labels])
    A=np.eye(4)[:,pa]; B=np.eye(4)[:,pb]
    raw=np.kron(A,B); T=C@raw@np.linalg.inv(C)
    assert np.max(np.abs(T.T@T-np.eye(16)))<tol
    assert np.max(np.abs(newU[perm]-U@T.T))<tol
    wt=np.empty(137); wt[perm]=w
    for k in range(137):
        q1,w1=event(q,w,k)
        q2,w2=event(T@q,wt,perm[k],newU)
        assert np.max(np.abs(q2-T@q1))<tol
        assert np.max(np.abs(w2[perm]-w1))<tol
    history=[i,121,j,130,i]
    q1,w1=word(q,w,history)
    q2,w2=word(T@q,wt,[perm[k] for k in history],newU)
    assert np.max(np.abs(q2-T@q1))<tol
    assert np.max(np.abs(w2[perm]-w1))<tol
    anchor=q+U.T@w
    assert np.max(np.abs(T@anchor-(T@q+newU.T@wt)))<tol
    assert np.max(np.abs((wt-newU@(T@q))[perm]-(w-U@q)))<tol

# Noncommuting histories cannot be replaced by their unordered event multiset.
h1=word(q,w,[121,122]); h2=word(q,w,[122,121])
assert np.linalg.norm(np.r_[h1[0]-h2[0],h1[1]-h2[1]])>1e-5

# Preparation/readout contract: zero carrier, one signed record amplitude A.
# These are candidate controllable amplitudes, not derived physical observables.
k=121; amp=2.3
q0=np.zeros(16); w0=np.zeros(137); w0[k]=amp
q1,w1=event(q0,w0,k)
assert np.max(np.abs(U@q1-amp*(U@U[k])))<tol
q2,w2=event(q1,w1,k)
assert np.max(np.abs(q2-q0))<tol and np.max(np.abs(w2-w0))<tol
# Norm-preserving competing quarter-turn: (s,w)->(w,-s), same first pulse
# for this preparation, but opposite signed record amplitude after two pulses.
def rotation(q,w,k):
    s=U[k]@q; r=w[k]
    nxt=w.copy(); nxt[k]=-s
    return q+U[k]*(r-s),nxt
r1,t1=rotation(q0,w0,k); r2,t2=rotation(r1,t1,k)
assert np.max(np.abs(r1-q1))<tol and np.max(np.abs(t1-w1))<tol
assert abs(r2@r2+t2@t2-amp**2)<tol
assert abs(w2[k]/amp-1)<tol and abs(t2[k]/amp+1)<tol
# Matching-state nondisturbance selects swap, but is an additional operational axiom.
matched_q=amp*U[k]; matched_w=np.zeros(137); matched_w[k]=amp
mq,mw=event(matched_q,matched_w,k)
rq,rw=rotation(matched_q,matched_w,k)
assert np.linalg.norm(np.r_[mq-matched_q,mw-matched_w])<tol
assert np.linalg.norm(np.r_[rq-matched_q,rw-matched_w])>1

result={
 'status':'passed',
 'classification':'conditional_labelled_source_exchange_adapter_with_signed_echo_discriminator',
 'tolerance':tol,
 'checks':{'prior_fixture_rerun':True,'raw_to_whitened_all137_operations':True,
           'duplicate_features_keep_distinct_record_ports':True,
           'reference_transport_all137_events':True,'ordered_word_transport':True,
           'anchor_and_mismatch_transport':True,'unordered_history_hostile':True,
           'signed_echo_distinguishes_equal_first_pulse_models':True},
 'echo_ratios':{'exchange':float(w2[k]/amp),'quarter_turn':float(t2[k]/amp)},
 'conclusion':'Labelled tensor features admit a reference-covariant exchange adapter once independent record amplitudes, the metric and a local matched-state-nondisturbing orthogonal operation are supplied. Counts or budget alone do not force that operation.',
 'missing':['native preparation of q and independent w','physical sign-sensitive readout and pulse implementation',
            'mapping from matrix legs to tensor carrier','absolute coupling and physical units'],
 'next_falsifier':'Derive or experimentally test matched-state nondisturbance and the signed two-pulse echo for an actual source operation; retain reset and probe back-action costs.'
}
output.parent.mkdir(parents=True,exist_ok=True)
output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

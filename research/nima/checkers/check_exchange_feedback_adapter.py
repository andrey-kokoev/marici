# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Reduce the prior reversible exchange law and test the family-feedback bridge.

Exact formulas, floating-point fixture verification with explicit tolerances.
The obstruction concerns linear first-moment adapters, not arbitrary nonlinear
or history/covariance-enriched physical realizations.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from collections import defaultdict
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy
import numpy as np

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/exchange-feedback-adapter.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    old=runpy.run_path(str(Path(__file__).with_name('check_137_closed_record_stationarity.py')))
U=old['U']; n=137; d=153; tol=1e-10
D=np.vstack((U.T,-np.eye(n)))/np.sqrt(2)
L=np.hstack((-U,np.eye(n)))  # mismatch delta=w-Uq
S=D@D.T
M=np.eye(d)-S/n            # lazy schedule: half idle, half uniform exchanges
K=np.eye(n)+U@U.T
R=np.eye(n)-K/(2*n)
assert np.max(np.abs(L@M-R@L))<tol
assert np.max(np.abs(L@L.T-K))<tol
assert np.linalg.matrix_rank(D,tol=tol)==137
assert np.linalg.eigvalsh(K).min()>.99
assert np.linalg.eigvalsh(R).max()<1
assert np.linalg.eigvalsh(R).min()>0
assert np.linalg.matrix_rank(M-np.eye(d),tol=tol)==137

def channel(second_moment):
    XD=second_moment@D
    diagonal=np.sum(D*XD,axis=0)
    return second_moment-(S@second_moment+second_moment@S)/n+2*(D*diagonal)@D.T/n

def outcomes(x):
    return np.column_stack((x,x[:,None]-2*D*(D.T@x)[None,:]))
prob=np.r_[.5,np.full(n,1/(2*n))]
assert abs(prob.sum()-1)<tol

# Directly compare all138 schedule outcomes with the reduced mean and covariance.
x=np.zeros(d); x[16+121]=1
ys=outcomes(x)
assert np.max(np.abs(np.sum(ys*ys,axis=0)-x@x))<tol
# A faithful retained coordinate packet is (a=q+U^T w, delta=w-Uq).
# The16-vector a is fixed by every exchange; it must not be dropped.
W=np.vstack((np.eye(16),U))
G16=np.eye(16)+U.T@U
Kinv=np.eye(n)-U@np.linalg.solve(G16,U.T)
assert np.max(np.abs(Kinv@K-np.eye(n)))<tol
for value in (x,np.arange(d,dtype=float)/d):
    anchor=W.T@value; mismatch=L@value
    q=np.linalg.solve(G16,anchor-U.T@mismatch)
    reconstructed=np.r_[q,mismatch+U@q]
    assert np.max(np.abs(reconstructed-value))<tol
    budget=anchor@np.linalg.solve(G16,anchor)+mismatch@Kinv@mismatch
    assert abs(budget-value@value)<tol
assert np.max(np.abs(W.T@ys-(W.T@x)[:,None]))<tol
mismatches=L@ys
# Event-level back-action, prior to any averaging/scheduling approximation:
# delta'_j = delta_j - K_ji delta_i, with K_ii=2.
# For j!=i, K_ji=<u_j,u_i>; subsequent comparisons change through shared carrier.
assert np.max(np.abs(np.diag(K)-2))<tol
for value in (x,np.arange(d,dtype=float)/d):
    before=L@value
    after=L@outcomes(value)[:,1:]
    assert np.max(np.abs(after-(before[:,None]-K*before[None,:])))<tol
    assert np.max(np.abs(np.diag(after)+before))<tol
# A single initially excited record changes other mismatch readings whenever
# its source feature overlaps theirs; the event is still reversible.
offdiag=K-np.diag(np.diag(K))
assert np.max(np.abs(offdiag[:,121]))>tol
assert np.max(np.abs(mismatches[:,122]-(L@x-K[:,121])))<tol
print('PASS: every exchange flips its own mismatch and changes other readings by the source feature-overlap kernel.')
mismatch_budgets=np.sum(mismatches*(Kinv@mismatches),axis=0)
assert np.max(np.abs(mismatch_budgets-mismatch_budgets[0]))<tol
mu=M@x
assert np.max(np.abs(ys@prob-mu))<tol
centered=ys-mu[:,None]
Q=(centered*prob)@centered.T
assert np.linalg.eigvalsh(Q).min()>-tol
assert np.max(np.abs(Q-(channel(np.outer(x,x))-np.outer(mu,mu))))<tol
assert abs(np.trace(Q)-(x@x-mu@mu))<tol
assert np.trace(Q)>0

# The exact mean/covariance recursion also holds with a nonzero initial covariance.
basis=np.column_stack((np.arange(d)%3-1,np.arange(d)%5-2,np.arange(d)%7-3)).astype(float)/10
sigma=basis@basis.T/3
expected_sigma=channel(sigma)+Q
actual_second=np.zeros((d,d)); actual_mu=np.zeros(d)
for k in range(3):
    for sign in (-1,1):
        values=outcomes(x+sign*basis[:,k])
        actual_mu+=values@prob/6
        actual_second+=(values*prob)@values.T/6
assert np.max(np.abs(actual_mu-mu))<tol
assert np.max(np.abs(actual_second-np.outer(mu,mu)-expected_sigma))<tol
assert abs(np.trace(expected_sigma)+mu@mu-(np.trace(sigma)+x@x))<tol

initial_budget=float(np.trace(sigma)+x@x)
mean=x.copy(); cov=sigma.copy()
for _ in range(12):
    next_mean=M@mean
    noise=channel(np.outer(mean,mean))-np.outer(next_mean,next_mean)
    assert np.linalg.eigvalsh(noise).min()>-tol
    cov=channel(cov)+noise; mean=next_mean
    assert abs(np.trace(cov)+mean@mean-initial_budget)<tol

# Raw records alone are not an autonomous observed state: same w, different q
# produce different next record means. Mismatch, in contrast, closes exactly.
a=np.zeros(d); b=a.copy(); b[0]=1
assert np.array_equal(a[16:],b[16:])
assert np.linalg.norm((M@a)[16:]-(M@b)[16:])>1e-6

# Actual32 target families of the shared comparison fixture. Full calibration
# of the factorized leg model acts on slot values by this P; partial primitive
# relaxation need not be linear in slot values.
E=old['edges']; groups=defaultdict(list)
for i in range(11):
    for j in range(11): groups['a',E[i][1],E[j][1]].append(11*i+j)
for i in range(4):
    for j in range(4): groups['s',i,j].append(121+4*i+j)
P=np.zeros((n,n))
for indexes in groups.values(): P[np.ix_(indexes,indexes)]=1/len(indexes)
assert len(groups)==32 and np.linalg.matrix_rank(P,tol=tol)==32
assert np.max(np.abs(P@P-P))<tol
eta=.5
N=(1-eta)*np.eye(n)+eta*P
# Minimal hostile: a singleton state-family value is fixed by family feedback,
# but its mismatch value evolves under the original exchange schedule.
v=np.zeros(n); v[121]=1
assert np.array_equal(P@v,v) and np.array_equal(N@v,v)
assert abs((R@v)[121]-136/137)<tol
assert np.linalg.norm(R@v-v)>1e-6
# R has no unit eigenvectors; N has32. No invertible linear conjugacy exists.
assert np.linalg.matrix_rank(R-np.eye(n),tol=tol)==137
assert np.linalg.matrix_rank(N-np.eye(n),tol=tol)==105

result={
 'status':'passed',
 'classification':'exchange_mean_covariance_reduction_passes_family_mean_adapter_fails',
 'obligation':'route/readout compatibility between existing exchange and family-feedback laws',
 'stratum':'Prior16+137 reversible exchange fixture and its declared lazy uniform schedule; linear first-moment comparison with32-family slot projection',
 'tolerance':tol,
 'checks':{'old_exchange_fixture_rerun':True,'all_schedule_outcomes_norm_preserving':True,
           'closed_mismatch_mean_law':True,'faithful_anchor_mismatch_packet':True,
           'packet_budget_split_and_reconstruction':True,'mean_covariance_recursion':True,
           'covariance_innovation_positive':True,'total_second_moment_budget_preserved':True,
           'record_only_observation_not_closed':True,'singleton_family_counterexample':True},
 'dimensions':{'full_mean_fixed_space':16,'mismatch_mean_fixed_space':0,
               'family_slot_projection_fixed_space':32},
 'one_step_budget':{'mean_norm_squared':float(mu@mu),'generated_covariance_trace':float(np.trace(Q)),
                    'total':float(mu@mu+np.trace(Q))},
 'verdict':'The older model supplies an endogenous feedback law and exact averaged covariance bookkeeping. It is not the new family-mean relaxation under the natural linear slot identification.',
 'unsupported':['nonlinear or covariance-enriched adapter exclusion',
                'physical electromagnetic normalization','equivalence of scalar exchange and matrix-leg state spaces',
                'transfer of stationary1/137 result to the new feedback model'],
 'next_constructor':'Use the source-derived exchange kernel for this branch, or explicitly construct a larger packet adapter carrying invariant carrier information and covariance before claiming equivalence.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

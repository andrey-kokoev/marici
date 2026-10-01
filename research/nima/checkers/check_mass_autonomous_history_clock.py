"""Autonomous reversible execution is not autonomous mass selection or arrest."""
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import math
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_mass_history_locking_controller.py'))
N=prior['N']; tree=prior['tree']; L=len(tree); tol=1e-8
# History-basis Hamiltonian: off-diagonal spin-L/2 matrix elements. Each physical
# link is |t+1><t| tensor U_t, plus its Hermitian adjoint. U_t includes records
# and charge/work reservoirs from the previous construction.
j=[math.sqrt((t+1)*(L-t))/2 for t in range(L)]
def action(a):
    out=[0j]*(L+1)
    for t,g in enumerate(j):
        out[t]+=g*a[t+1]; out[t+1]+=g*a[t]
    return out

def amplitude(tau):
    if tau==0: return [1+0j]+[0j]*L
    if tau==math.pi: return [0j]*L+[(-1j)**(L%4)]
    c,s=math.cos(tau/2),math.sin(tau/2)
    assert c>0 and s>0
    return [(-1j)**(t%4)*math.exp(
        .5*(math.lgamma(L+1)-math.lgamma(t+1)-math.lgamma(L-t+1))
        +(L-t)*math.log(c)+t*math.log(s)) for t in range(L+1)]

max_residual=0.
for tau in (.4,1.2,2.4):
    a=amplitude(tau); ha=action(a)
    derivative=[a[t]*(-(L-t)*math.tan(tau/2)+t/math.tan(tau/2))/2 for t in range(L+1)]
    residual=max(abs(1j*derivative[t]-ha[t]) for t in range(L+1))
    max_residual=max(max_residual,residual)
    assert residual<tol
    probabilities=[abs(x)**2 for x in a]
    assert abs(sum(probabilities)-1)<tol
    mean_clock=sum(t*p for t,p in enumerate(probabilities))
    assert abs(mean_clock-L*math.sin(tau/2)**2)<tol
# Exact history resource table: distinct clock states make histories orthogonal.
charges=[0]*N; charges[0]=1; q=w=N; records=[]
for t,(parent,child) in enumerate(tree,1):
    old=charges[child]; new=charges[parent]
    records.append(old-new); charges[child]=new
    q+=old-new; w+=old*old-new*new
    assert sum(charges)==t+1 and sum(x*x for x in charges)==t+1
    assert q==N-t and w==N-t
    assert sum(x*x for x in charges)+w==N+1
assert charges==[1]*N and len(records)==L
final=amplitude(math.pi)
assert abs(final[-1])==1 and sum(abs(x)**2 for x in final[:-1])==0
# The target history is not an eigenstate: its clock immediately couples back.
assert abs(sum(abs(x)**2 for x in action(final))-L/4)<tol
assert L>0
# At time2*pi the spin rotation returns the original history up to global phase.
# sin(tau/2)^(2L) is the completion probability, not a permanent latch.
delta=.01
later_probability=math.cos(delta/2)**(2*L)
assert 0<later_probability<.99
# Even a two-step uniform clock illustrates dependence on designed couplings:
# endpoint probability=sin(tau/sqrt(2))^4, generally not1 at tau=pi.
uniform_two_step_at_pi=math.sin(math.pi/math.sqrt(2))**4
assert uniform_two_step_at_pi<.9
result={
 'status':'passed','classification':'autonomous_history_execution_not_source_selected_stable_mass',
 'channels':N,'clock_dimension':L+1,'encoded_gates':L,
 'tolerance':tol,'maximum_schrodinger_residual':max_residual,
 'completion_time_in_selected_clock_units':'pi',
 'completion_probability_at_pi':1,
 'completion_probability_at_pi_plus_0_01':later_probability,
 'terminal_departure_norm_squared':L/4,
 'checks':{'prior_chain_fresh':True,'time_independent_history_hamiltonian':True,
           'analytic_clock_trajectory_verified':True,'history_charge_and_energy_balance':True,
           'perfect_transfer_for_programmed_couplings':True,'terminal_state_not_stationary':True,
           'clock_couplings_are_additional_controls':True},
 'conclusion':'A time-independent history Hamiltonian autonomously executes the1835 reversible locking gates and completes the prepared1836-unit state at a designed time. It later reverses: autonomous execution does not select a stable particle, unit gap, initial charge or the programmed schedule.',
 'next_falsifier':'Find a source-derived protected particle sector and Hamiltonian rather than adding clock or latch controls. Stable preparation requires explicit scattering/storage/environment dynamics; the finite clock does not supply it.'}
out=HERE.parent/'results/mass-autonomous-history-clock.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

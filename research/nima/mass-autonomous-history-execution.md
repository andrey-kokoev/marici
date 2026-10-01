# Autonomous execution of the locking history is not mass selection

## Forward-realization scope

The prior reversible locking controller is freshly rerun. This trial removes
external gate timing by embedding its1835 gates in a time-independent history
Hamiltonian. It does not derive the programme, input charge, couplings or charging
law from the carrier. Autonomy of execution and autonomy of explanation are
separate obligations.

## Hamiltonian

Let U_t be the previous reversible gate, including its retained difference record
and reservoir shifts. Add clock states |t>, t=0,...,L, with L=1835. Define

    H_prop = sum_(t=0)^(L-1) j_t [|t+1><t| tensor U_t
                                + |t><t+1| tensor U_t^dagger],
    j_t = sqrt((t+1)(L-t))/2.

For a prepared input psi_0, let psi_t=U_(t-1)...U_0 psi_0. The history states
|t> tensor psi_t are orthogonal because their clock labels differ. On their span,
H_prop is the spin-L/2 J_x matrix. The full physical Hamiltonian may include
H_charge+H_reservoir+ kappa H_prop. The checked gate shifts conserve the first
two terms on the declared accessible histories, where their sum is1837.
Clock time below is tau=kappa*t with hbar=1.

This is an ideal history-space construction, not a microscopic local device.
The reservoirs have enough capacity on every checked history. An unrestricted
integer battery translation is not a claim of a globally bounded-below physical
battery. The finite invariant history block can be specified directly; extending
it to a local physical Hamiltonian with realistic batteries remains additional
work. The programmed gates and j_t coefficients are inputs.

## Executed trajectory

Starting at clock0, the exact clock amplitude is

    a_t(tau)=sqrt(binomial(L,t))
             *cos(tau/2)^(L-t)*[-i sin(tau/2)]^t.

At tau=pi only t=L remains, so the circuit finishes with unit probability.
The checker independently differentiates this expression and compares it to
-i H_prop a at three interior times. Maximum residual is approximately8.5e-11,
below the declared1e-8 tolerance for the1836-dimensional floating calculation.
Normalization and mean clock position are also checked.

At history t, exactly t+1 channels carry a unit charge and the work reservoir
contains1836-t units. Their charging-energy sum stays1837. In a clock
superposition,

    expected stored energy = 1+1835*sin(tau/2)^2.

The propagation interaction has zero expectation along this trajectory because
its initial expectation is zero and it is conserved. Reservoir accounting must
not be mistaken for omitting the propagation Hamiltonian from the model.

## No terminal latch

The completed history is not an eigenstate:

    ||H_prop |L,psi_L>||^2 = L/4 = 458.75.

At tau=pi+.01, completion probability has fallen to approximately.955161.
At tau=2*pi the history returns to its initial state up to phase, restoring the
charge/work reservoirs and undoing the preparation. This is reversible autonomous
execution, not a stable prepared particle.

A finite closed unitary system cannot take a distinct input into a stationary
full-system state and then leave it there forever: applying the inverse evolution
to that stationary state would make the original input the same state up to phase.
This is not a prohibition on stable particle eigenstates or preparation by
scattering against an environment. It prevents interpreting this finite clock's
completion point as an absorbing state without extra dynamics.

Perfect transfer also depends on the chosen clock couplings. Already for two
gates, a uniform-coupling clock has endpoint probability sin(tau/sqrt(2))^4,
which is not1 at tau=pi. Engineering execution is not deriving its timescale.

## What this does and does not establish

The source-incidence programme can be executed by an explicit autonomous
Hamiltonian while retaining records and accounting for charge and energy.
Exactly the same construction works for programmes of other lengths. It does
not privilege1836, derive the common gap, choose the initial unit charge, or
supply proton/electron statistics and conserved particle sectors.

The controller route has therefore reached its explanatory boundary: adding
another clock or latch is not evidence for a source-selected mass ratio. The
remaining task is to obtain an independently sourced Hamiltonian and protected
particle sector. A physical scattering/storage/environment construction would
be needed for stable preparation, not a hidden reset of this finite clock.

## Verification

    python research/nima/checkers/check_mass_autonomous_history_clock.py
    python research/aspect/scc/scc.py check nima-mass-autonomous-history-clock

The integer history resource table is exact; the large clock trajectory uses
floating arithmetic with explicit tolerance. Report:
`results/mass-autonomous-history-clock.json`. No measured mass value is fitted.

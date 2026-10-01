# Iteration 2: an oscillator preparation and measurement realization

## Reused source, not another replacement dynamics

Freshly read `137-gauge-adapter-and-complex-lift.md` already supplies the pulse
S_i(theta)=I+(exp(-i theta)-1)d_i d_i^T, with theta=pi giving the old exchange.
The previous iteration supplied labelled ports, reference relabelling and a
signed echo test. This iteration realizes that same pulse in standard bosonic
mode mechanics. That physical framework, its quantum measurement rule and its
controls are additional assumptions, not derived from retained comparisons.

## Modes and controlled Hamiltonian

Take16 carrier modes a_k and137 record modes r_i, with canonical bosonic
commutators. The source-normalized real vector u_i selects a carrier supermode
c_i=sum_k u_ik a_k. Define the normalized difference mode

    b_i = (c_i-r_i)/sqrt(2),
    H_i(t) = hbar*kappa_i(t)*b_i^dagger b_i,
    theta_i = integral kappa_i(t) dt.

In a common rotating frame, the annihilation-operator vector evolves by
S_i(theta_i). At theta_i=pi it swaps c_i and r_i and fixes orthogonal carrier
modes and all other records. The expansion

    H_i = (hbar*kappa_i/2)
          (c_i^dagger c_i+r_i^dagger r_i-c_i^dagger r_i-r_i^dagger c_i)

requires BOTH the indicated mode-frequency shifts and exchange coupling.
A coupling term alone generally yields a different phase convention; it must
not be called this pulse without its phase compensation.

This is an ideal passive linear network realization. Selecting the overlapping
supermode c_i, switching the control and matching mode frequencies are hardware
obligations, not consequences of the137 labels. In a degenerate-frequency model
total excitation number is conserved. With unequal physical frequencies or
pumped frequency conversion, number conservation does not establish conservation
of laboratory energy; pump/controller work must be included.

## State and retained packet

Prepare multimode coherent amplitudes (q,w). Their means obey the existing
complex pulse exactly. At real exchange endpoints each quadrature copy obeys
the original real law. The complex packet

    a=q+U^T w,   delta=w-Uq

remains faithful, and a is fixed throughout every selected pulse. There are
16 complex anchors and137 complex mismatches: two real copies, not a claim that
the original153-dimensional real state already contained canonical conjugates.
Between endpoints, both quadratures are needed. Keep ordered pulse histories;
schedule averaging additionally requires the earlier covariance channel.

A matched coherent preparation with c_i=r_i has zero difference-mode amplitude
and is unchanged by the pulse. This does not mean equal first moments make an
arbitrary quantum state invariant: nontrivial difference-mode fluctuations can
still evolve. The checker verifies amplitude nondisturbance and coherent-state
covariance, not that stronger and generally false assertion.

## Preparation, measurement and falsifier

Prepare the carrier in vacuum and one record in a coherent state of real
amplitude A relative to a retained phase reference. Standard coherent preparation
supplies the displacements; it does not follow from slot counting. For equal
mode frequency omega, the prepared excess energy is hbar*omega*A^2, excluding
preparation inefficiency and the phase-reference apparatus.

Read the record quadrature X=(r+r^dagger)/sqrt(2) by ideal balanced homodyne with
a phase-locked local oscillator. This uses the standard quantum readout law:
coherent states have mean sqrt(2)*Re(w) and variance1/2. Detector gain, efficiency,
electronic noise and local-oscillator resources require independent calibration.
The readout is a final destructive instrument, not a cost-free intermediate probe.

On separately prepared trials, two identical ideal pulses give

    exchange:     E[X_i]=+sqrt(2)*A,  Var(X_i)=1/2,
    quarter-turn: E[X_i]=-sqrt(2)*A,  Var(X_i)=1/2.

Both models agree on the first-pulse state for this preparation and on the final
excitation number. Thus energy-only detection misses the discriminator; signed,
phase-referenced readout detects it. These are theoretical apparatus predictions,
not experimental results.

With a pulse-area error theta=pi+epsilon on each of the two pulses, exchange
predicts the complex record amplitude

    w_i_final = A*(1+exp(-2i theta))/2,
    E[X_i]/(sqrt(2)*A) = cos(epsilon)^2.

The conjugate quadrature also records the corresponding phase error. Pulse-area
calibration and phase drift must be controlled before interpreting an echo failure.

## Normalization: vacuum is a necessary hostile control

For the joint vacuum, all X coordinates have covariance I153/2. Therefore

    Var(X_record_i-u_i^T X_carrier) = 1

for every port, and their normalized shares are1/137. No coherent excitation or
new interaction strength was derived: this share is present in vacuum already.
Vacuum-subtracted mismatch variances vanish, making their normalized ratio
undefined. The measurement contract must say whether it reports raw quadrature
variance, calibrated excess variance, or another ordered observable.

The endpoint fixes only integral kappa_i dt=pi. It does not fix kappa_i, duration,
omega, detector units, physical field stiffness or a charge/current coupling.
Those can be calibrated independently in an apparatus but are not determined by
the normalized slot fraction. In particular this oscillator implementation does
not derive the electromagnetic fine-structure constant.

## Verification and next obligation

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_exchange_oscillator_instrument.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-exchange-oscillator-instrument

The checker reruns the closed-record fixture, checks all137 Hamiltonian pulse
endpoints, canonical quadrature transport and coherent covariance at intermediate
and endpoint angles, conserved anchors, signed echo, pulse error, duration
freedom and the vacuum hostile. Tolerance1e-10; no sampled experimental data.

We now have a conditional physical preparation/readout model, not a derivation
that the intended rung source selects it. Next close the native matrix-leg to
full tensor/mode-state mapping, or falsify it. The prior complex-lift note already
warns that a product of two four-component states is not closed under comparison.
That closure failure must be addressed before identifying the native preparation
with an arbitrary16-mode amplitude and137 independent record displacements.

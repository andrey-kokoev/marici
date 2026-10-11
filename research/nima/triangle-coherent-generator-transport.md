# Coherent transport repairs the stagewise rotor-generator mismatch

## What changed

The preceding continuous lift chose the inherited-metric minimal section
independently at each stage. That policy was not coherent with native word
extension. Its failure did not show that every section policy would fail.

Keep the same initial section, the same actual endpoint reader P_n, the
same native extension F_n, and the same previous rotor A and tick C. Instead
of re-minimizing, TRANSPORT the section:

    E_(n+1)=F_n E_n C^-1.

This is an explicit realization policy, determined by the initial section
and existing operation. No path coefficients, occurrence counts or native
composition rules change.

## Algebraic proof of compatibility

The actual endpoint-count reader satisfies

    P_(n+1) F_n=C P_n,
    P_n E_n=I,
    AC=CA.

Therefore P_(n+1) E_(n+1)=I. For L_n=E_n A P_n,

    L_(n+1) F_n
      =F_n E_n C^-1 A C P_n
      =F_n L_n.

Similarly, N_n=I-E_n P_n gives

    N_(n+1) F_n=F_n N_n.

Consequently the full continuous realizations

    W_n(theta)=N_n+E_n V(theta)P_n

satisfy W_(n+1)(theta)F_n=F_n W_n(theta) for EVERY theta. This includes hidden
coordinates, rather than merely equality after observing them.

The endpoint-reader identity is also checked on all four endpoint-count
coordinates. The above argument applies inductively wherever the registered
extension and reader identities hold. Finite executable tests instantiate
four stages; this is not claimed as a new Agda all-stage analysis theorem.

## The rotor-compatible metric also transports

Keep G_n as the original decoder-induced history metric and H=diag(3,1).
It already satisfies F_n^T G_(n+1) F_n=G_n, while C^T H C=H. Thus the
previously declared compatible metric

    Grot_n=P_n^T H P_n+N_n^T G_n N_n

now satisfies

    F_n^T Grot_(n+1) F_n=Grot_n.

The full generator is Grot-skew, and each stage's hidden component retains
its inherited norm. The original G_n alone remains incompatible with the
rotor reader; this construction does not erase that earlier obstruction.
Grot is an explicit conditional realization metric, not newly derived
physical geometry.

## Actual triangle-composition trajectory

| Path length | Frame words | Words per role | Quadratic Hamiltonian | Hidden squared norm | Total Grot squared norm |
|---|---|---|---|---|---|
|2|10|2|12|11/10|131/10|
|3|16|3|12|11/10|131/10|
|4|26|5|12|11/10|131/10|
|5|42|8|12|11/10|131/10|

Both operands and their identities remain recoverable at every composition.
The actual hidden component is transported rather than discarded. All these
norms use declared realization conventions; neither the hidden norm nor the
total norm is silently identified with physical energy.

## What is closed and what is not

Closed: the previous cross-stage generator mismatch and compatible-metric
mismatch, for this coherently transported realization. Continuous rotor
readout, hidden coefficients and native extension now form commuting squares.
The existing clock attachment is unchanged; no new scheduler is needed to
obtain these identities.

Not claimed: an autonomous Hamiltonian that creates the next discrete history
stage, a nondegenerate symplectic form on all history coordinates, physical
selection of the initial section/metric, physical seconds, or a charge/recoil
coupling. We do not take a direct-limit quotient identifying a longer history
with its prefix. Stage labels and complete retained paths stay explicit.

## Verification

    uv run --with sympy python research/nima/checkers/check_triangle_coherent_generator_transport.py

78 exact checks pass, rerunning the preceding continuous generator and
Hamiltonian/clock integration suites. The all-theta square is verified by
its constant, cosine and sine coefficient identities.
Receipt: `results/triangle-coherent-generator-transport.json`.

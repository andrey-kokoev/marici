# Bipartite Krylov-history composition gate: WP1081

## Question

Does adding Krylov history to WP1080's bipartite carrier derive a temporal
signed production law?

## Conditional Krylov mechanism

For one seed \(x\) and one source evolution \(A\), retain the depth-typed
history

\[
(0,x),\qquad (1,Ax),\qquad (2,A^2x).
\]

The alternating observer is

\[
\Omega_A(x)=\det[x,Ax,A^2x].
\]

For the exact witness

\[
A=\operatorname{diag}(1,2,3),
\qquad
x=(1,1,1)^T,
\]

the determinant is

\[
\Omega_A(x)=2.
\]

Exchanging depths one and two gives \(-2\).

## Required history gates

A destructive chain leaves only \(A^2x\), so the ternary observer cannot run.
Same-state fan-out gives

\[
\det[x,x,x]=0.
\]

Only a history-retaining constructor exposes the three depth-typed ports.

## Projective obstruction

A seed ray can be rephased by \(\zeta=e^{i\pi/3}\). Then

\[
\Omega_A(x)\longmapsto \zeta^3\Omega_A(x)=-\Omega_A(x).
\]

Thus the signed determinant does not descend to the projective physical
quotient. The positive observer

\[
\Omega_A(x)^2
\]

does descend, but reports only cyclicity. A signed relational observable
requires an independently derived volume reference \(\rho\) of phase weight
\(-3\), so that

\[
\rho\Omega_A(x)
\]

has total phase weight zero.

## WP1080 supply audit

WP1080 supplies:

- the \(3\times3\) bipartite pairing;
- the two \(\epsilon_3\) alternating carriers.

It does not supply:

- source evolution \(A\);
- seed ray \(x\);
- history-retaining constructor;
- volume reference \(\rho\) of weight \(-3\).

## Classification

Bipartite-Krylov composition gate. F1 is narrowed to four exact missing
constructors: \(A\), \(x\), retained history, and \(\rho\). The signed
production law remains open.

Checker: `research/flavor/checkers/wp1081_bipartite_krylov_history_composition_gate.py`

Result: `results/wp1081_bipartite_krylov_history_composition_gate.json`

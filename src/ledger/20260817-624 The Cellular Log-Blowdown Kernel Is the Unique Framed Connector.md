---
id: 421
date: 2026-08-17
title: The Cellular Log-Blowdown Kernel Is the Unique Framed Connector
---

# The Cellular Log-Blowdown Kernel Is the Unique Framed Connector

Entries 396--400 constructed the geometric connector by normalized
blowdown from the marked logarithmic expansion. Entries 417--420 independently
constructed and characterized the filtered PC/Čech connector. These are not
two remaining candidates.

Their complete frozen boundary signatures agree:
\[
\begin{array}{c|c|c}
\text{datum}&\text{log-blowdown kernel}&\text{filtered connector}\\ \hline
\text{generic }Q\text{ roof}&+1&+1\\
\text{generic Rees factor}&x_D&x_D\\
\text{closed Cartier residue}&+1&+1\\
\text{endpoint comparison}&
\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}&
\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\\
\text{Tor}_1\text{ suspension orientation}&+1&+1\\
\text{Čech residual}&0&0\\
\text{Cartier commutator}&0&0.
\end{array}
\]
Their reflection defect and Jordan associator also both vanish.

Entry 388 proves that, after freezing the generic, Cartier, lower-Čech, and
endpoint faces, the local relative deformation group is
\[
D_{03}^0=0.
\]
Thus the admissible local connector space is either empty or a singleton.
It is nonempty because the normalized blowdown explicitly supplies a
connector (Entries 396--397). Hence it has one component.

Globally, Entry 413 gives
\[
H^1_{\rm twist}(X;\mathbb F_3)=0,\qquad
H^0_{\rm twist}(X;\mathbb F_3)=0,
\]
so neither an order-three lift choice nor a residual automorphism can
separate the two constructions after three-road and Jordan assembly.
Therefore
\[
\boxed{
\text{cellular log-blowdown kernel}
=
\text{finite framed filtered connector}
}
\]
up to the unique admissible homotopy.

## Consequence

The finite cellular realization problem is complete. The constructed class
has:

- the actual normalized-log geometric provenance;
- the occurrence/Čech target;
- the external Gysin-shifted Cartier packet;
- the primitive nonzero \(Q\)-roof;
- both endpoint and Tor grades;
- global \(D_3\), reflection, and Jordan coherence; and
- both mandatory ordinary-forgetting ablations.

The remaining phrase “full geometric realization” must now be used more
narrowly. What is absent is not another cellular connector or coefficient
map. It is a ringed algebraic six-functor lift identifying the raw
normalization-sheet/DNC geometry and its relative dualizing trace with this
finite Alexandrov/cellular model. The finite model fixes the value that such
a lift must realize, but does not construct the algebraic \(p^*(-)\otimes
q^!(-)\) correspondence itself.

The next high-information test is therefore categorical: geometrize the
Entry-143 PC/Čech cosheaf as a ringed finite-space target, lift normalized
blowdown to a morphism of ringed finite spaces, and check whether its
left-Kan/proper pushforward and finite Verdier dual reproduce the connector.
Only after that finite six-operation lift succeeds should one compare it
with the raw algebraic normalization-sheet space.

The executable audit is
\`research/voevodsky/check_cellular_log_kernel_framed_identification.py\`.

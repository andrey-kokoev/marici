# Reciprocal incidence arrows require a sewing transversality cell

## Bounded question

If the direct theta sector supplies \(p:F_+\to Y_+\) and the reciprocal sector
supplies \(q:Y_-\to F_-\), what additional datum makes them one closed
incidence system?

## Typed sewing data

The arrows cannot be composed merely because \(Y_+,Y_-\) and \(F_+,F_-\)
have equal dimensions. A sewing comparison consists of source-derived
isomorphisms

\[
U:Y_+\longrightarrow Y_- ,
\qquad
V:F_+\longrightarrow F_- .
\]

Transport the reciprocal arrow to the direct carrier:

\[
\widehat q=V^{-1}qU:Y_+\longrightarrow F_+.
\]

Because \(Y_+\) is one-dimensional, the closed incidence is the scalar

\[
\kappa_{U,V}=pV^{-1}qU\in\operatorname{End}(Y_+)\simeq\mathbf C.
\]

This scalar is defined only after sewing. It is the minimal transversality cell
for the two directional constructors.

## Closure theorem

Assume \(p\ne0\) and \(q\ne0\). The sewn loop is nondegenerate exactly when

\[
\kappa_{U,V}\ne0,
\]

equivalently

\[
V^{-1}(\operatorname{im}qU)\not\subseteq\ker p.
\]

Nonzero sectorwise arrows do not imply this condition when \(\dim F_+=2\).
The reciprocal image is a line and the direct kernel is a line; sewing may
identify them.

The Clark direct endpoint sensor can make \(Y_+\) observable without supplying
\(q\). Likewise, direct transport supplies \(p\) without choosing \(V\).
Feature faithfulness and closed incidence remain distinct.

## Coherent basis invariance

Let \(G\) and \(H\) change forcing coordinates in the direct and reciprocal
sectors. Then

\[
p\mapsto pG^{-1},
\quad
q\mapsto Hq,
\quad
V\mapsto HVG^{-1}.
\]

The scalar \(pV^{-1}qU\) is unchanged. Thus \(\kappa\) is independent of
coordinate presentation once the sewing map is transported coherently. It is
not independent of choosing a different sewing map.

## Hostile sewing choices

Take

\[
p=(1,0),\qquad q=(1,0)^{\mathsf T}.
\]

Identity sewing gives \(\kappa=1\). The swap sewing

\[
V=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

gives \(\kappa=0\). Both are unitary isomorphisms, and the sectorwise norms and
ranks of \(p,q\) are identical. Therefore ranks, norms, and scalar sector
readouts do not determine the closed current.

Even with identity sewing, the nonzero arrows

\[
p=(1,0),\qquad q=(0,1)^{\mathsf T}
\]

have \(\kappa=0\). This is the smallest orthogonality hostile.

## Completion-stable transversality

Finite closure requires \(\kappa_N\ne0\). Stable completion requires a lower
bound in the chosen normalizations:

\[
|\kappa_N|\ge c>0.
\]

This does not follow from uniformly bounded invertible sewing. For
\(\varepsilon_N=1/N\), take

\[
V_N^{-1}=
\begin{pmatrix}
\varepsilon_N&1\\
1&0
\end{pmatrix},
\qquad
p=(1,0),\quad q=(1,0)^{\mathsf T}.
\]

Both \(V_N\) and \(V_N^{-1}\) remain uniformly bounded, but

\[
\kappa_N=\varepsilon_N\longrightarrow0.
\]

Uniform carrier equivalence is not uniform incidence transversality.

## Sheet frame and orientation

Changing the scalar sewing \(U\) by a phase multiplies \(\kappa\) by that
phase. In particular a sheet sign changes the sign of the closed current while
leaving sectorwise Gramians unchanged. A tensor unit, vacuum, endpoint
orientation, or other source reference must fix this frame before \(\kappa\)
can carry orientation. Nonzero magnitude alone is not an RH sign theorem.

## Sewing coherence gates

A completion-ready sewing family must satisfy:

1. source identity of the \(Y\) and \(F\) carriers on both sectors;
2. invertible, cutoff-natural \(U_N,V_N\);
3. compatibility with Fourier–Tate transport and sheet character;
4. coherent action on tail, seam, primitive, square, and archimedean rows;
5. a cutoff-independent transversality lower bound;
6. a source-fixed phase frame if a signed current is claimed.

## Exact audit and falsifiers

The checker rejects unsewn typed composition, verifies coherent basis
invariance, reproduces identity-versus-swap and orthogonality hostiles, checks
sheet-phase action, and proves the uniformly bounded sewing collapse family.

The closed-current theorem is falsified by \(\kappa=0\), by cutoff-dependent
phase, by failure of a sewing coherence square, or by \(|\kappa_N|\to0\).

## Claim boundary

This is a finite sewing and completion compiler theorem. It does not derive
the Fourier–Tate sewing maps, theta sheet frame, signed arithmetic current,
uniform transversality, conservative realization, zero orientation, or RH.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The alternatives were automatic closure of nonzero sector arrows and a
separate sewing/transversality scalar. Typing, coherent basis change, sewing
choice, orthogonality, phase, and uniform collapse were frozen measurements.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Automatic closure was eliminated. One scalar transversality cell was
constructed, shown coordinate-invariant but sewing-dependent, and separated
from uniform carrier equivalence. Fourier–Tate sewing and phase authority
remain unresolved.

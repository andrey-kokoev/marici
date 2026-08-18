---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 705 — The Residue Branch Discriminants Have Diagonal Second-Normal Initial Forms

## Hard-to-vary claim

The three residue branch-collision discriminants have diagonal second-normal
initial forms

\[
\nu_1^2,\qquad\nu_2^2,\qquad\nu_3^2,
\]

and not square-free initial forms in

\[
N_2=\langle\nu_1\nu_2,\nu_1\nu_3,\nu_2\nu_3\rangle.
\]

Consequently \(N_2\) does not directly supply the smoothing parameters for
these three collisions. This claim concerns discriminant normal directions,
not an embedding of the six nearby-cycle classes into a three-dimensional
monomial space.

## Branch specialization

Entries 702 and 704 established that all four marked lines on the generic
\(q_{\mathcal G_{12}}\)-residue surface meet the Cayley--Menger branch
divisor in four distinct points. On the generic nonsoft homogeneous locus,
their square-free branch degrees specialize as

\[
\boxed{(4,4,4,4)\longrightarrow(2,2,2,4)}
\]

in source order \((L_1,L_2,L_3,L_{23})\). Symbolically, the restrictions on
the first three lines become exact squares of quadratics. The fourth remains
a square-free quartic.

Therefore the puncture losses are

\[
(2,2,2,0),
\]

which reproduce the restricted-rank change

\[
26-20=6.
\]

## Labelled conormal discriminants

Write

\[
P_i^2=X_i^2+\nu_i
\]

before taking each restricted quartic discriminant. Exact polynomial
expansion at two independent generic homogeneous points gives stable first
nonzero conormal monomials:

\[
\operatorname{in}_I\operatorname{Disc}(K|_{L_1,q_G})
\sim\nu_1^2,
\]

\[
\operatorname{in}_I\operatorname{Disc}(K|_{L_2,q_G})
\sim\nu_2^2,
\]

\[
\operatorname{in}_I\operatorname{Disc}(K|_{L_3,q_G})
\sim\nu_3^2.
\]

For \(L_{23}\), the discriminant already has nonzero normal order zero.
The two rational witnesses used were

\[
(X_1,X_2,X_3)=(2,3,4),\qquad(3,5,6),
\]

both away from signed-energy degeneracies. At each witness the complete
leading-monomial support is a singleton with exponent vectors

\[
(2,0,0),\qquad(0,2,0),\qquad(0,0,2),
\]

respectively. This proves the generic leading coefficients are nonzero and
guards against accidental cancellation.

## Separation from the lower algebraic-letter module

The degree-two conormal space decomposes as

\[
\operatorname{Sym}^2(I/I^2)
=
\langle\nu_1^2,\nu_2^2,\nu_3^2\rangle
\oplus
N_2.
\]

The three direct discriminant smoothing parameters occupy the first
summand. Hence, at the discriminant level,

\[
\boxed{
N_2\cap
\langle\operatorname{in}_I\operatorname{Disc}(K|_{L_i,q_G})\rangle
=0.
}
\]

The generic lower two-pole radicals of Entry 698 occupy the square-free
summand. They therefore cannot directly smooth the three residue branch
collisions, even before testing \(\mathcal Q\).

## Consequence for derived base change

The Euler-rank change from Entry 702 splits as

\[
25=(34-15)+(26-20)=19+6.
\]

The present result types the direct smoothing parameters underlying the
three collision packets. It does not type the normal location of the six
cohomological classes, construct the corresponding vanishing-cycle complex,
or prove that those classes survive without cancellation in
\(\operatorname{Cone}(\beta_{\rm GM})\).

The square-free module \(N_2\) can now contribute, if at all, through the
remaining rank-19 lower-deletion comparison or through a derived extension
mixing diagonal and square-free normal sectors. It cannot contribute as a
direct residue-collision smoothing parameter.

## Consequence for \(\mathcal Q\)

No \(\mathcal Q\)-valuation is taken. The direct collision smoothings are
excluded from the candidate square-free route by conormal type. The nearby
cycles may still carry derived extensions mixing diagonal and square-free
normal sectors; that question remains open.

## Evidence

- `research/benincasa/check_residue_branch_specialization_defect.py`;
- `research/benincasa/residue-branch-specialization-defect.json`;
- Entries 596, 698, 701, 702, and 704;
- allocator claim `seqclaim-f46916614c51c5374c8b98ef`.

## Next falsifier

First construct the three local nearby-cycle cones and test whether their
six classes inherit only the diagonal smoothing directions or acquire a
derived square-free extension. In parallel, perform the conormal
decomposition of the rank change

\[
34\longrightarrow15
\]

in the four-pole lower deletion. Determine whether its first derived
base-change defect contains the square-free summand \(N_2\). If it does not,
the entire generic-lower route to \(\mathcal Q\) closes at second normal
order. If it does, construct that labelled comparison before computing any
\(\mathcal Q\)-support.

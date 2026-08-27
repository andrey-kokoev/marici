# RH invariant moment form forces reciprocal doubling

## Result

The infinite moment observer cannot carry a nonzero bilinear form preserved by the positive-scale spectral generator alone.

At a finite labelled cutoff, let

\[
D=\operatorname{diag}(u_1,\ldots,u_N)
\]

with every \(u_i>0\). A bilinear form \(Q\) preserved infinitesimally by spectral transport must satisfy

\[
D^TQ+QD=0.
\]

Entrywise,

\[
(u_i+u_j)Q_{ij}=0.
\]

Since every sum is positive, \(Q=0\). No nondegenerate one-sector form exists.

## Reciprocal repair

Double the spectrum:

\[
\widetilde D=
\operatorname{diag}(u_1,\ldots,u_N,-u_1,\ldots,-u_N).
\]

Now entries pairing \(u_i\) with \(-u_i\) are permitted. The canonical symmetric form is

\[
Q=
\begin{pmatrix}
0&I\\
I&0
\end{pmatrix}.
\]

It is nondegenerate and satisfies

\[
\widetilde D^TQ+Q\widetilde D=0.
\]

Thus reciprocal two-sector doubling is forced by preservation, not merely suggested by the functional equation.

## Crucial limitation

The cross-sector form is indefinite. Each pure-sector vector is null:

\[
Q((x,0),(x,0))=0,
\qquad
Q((0,y),(0,y))=0.
\]

Therefore the form supplies sewing and conservation but not scalar orientation. A distinguished scalar pairing may still vanish for two nonzero states.

This precisely matches the current RH boundary:

- one sector cannot support the invariant geometry;
- two reciprocal sectors support a canonical cross-pairing;
- the cross-pairing alone does not prevent destructive endpoint cancellation.

## Relation to the seam-jet tower

Grothendieck's exact formula shows that spectral differentiation and prime shifts commute only after adjoining every seam jet. The natural completed carrier is therefore a reciprocal pair of pro-moment modules with a complete seam-jet boundary object.

The form must be tested on that full carrier. Finite truncations are not closed because their top moment produces a wall residual.

## DPC verdict

Candidate: a preserved nondegenerate form on the single positive-scale moment module.

Verdict: impossible by the entrywise preservation equation.

Candidate: reciprocal doubling with the canonical cross-form.

Verdict: source-compatible and nondegenerate, but insufficient for zero exclusion because it is indefinite and pure-sector states are null.

Surviving target: derive an additional source operation selecting an admissible cone, real structure, polarization, or positive Lagrangian relation inside the doubled module. It must be preserved by prime transport, spectral flow, seam jets, and completion, and it must reject hostile symmetric multipliers.

## Finite falsifier

At a labelled cutoff, compute the proposed form \(Q_X\) and test

\[
D_X^TQ_X+Q_XD_X=0
\]

and the analogous prime-shift identity including seam incidence. A nonzero two-label minor closes preservation. If preservation holds, exhibit a nonzero admissible pure-sector or cross-sector state with zero endpoint pairing; unless the proposed orientation excludes it source-locally, the form adds no RH-bearing information.

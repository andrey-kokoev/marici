# RH spectral differentiation forces an infinite moment observer

## Result

For the native theta/Fourier transform, spectral differentiation inserts the scale variable. Repeated differentiation therefore generates the full moment orbit

\[
1,\ u,\ u^2,\ u^3,\ldots.
\]

If the source has infinitely many support points with an accumulation point, these directions are linearly independent. Any finite relation would give a polynomial vanishing on the source support, hence the zero polynomial.

Therefore the endpoint evaluation covector does not span an invariant line or any finite-dimensional invariant dual module under the native spectral generator. Its orbit is forced infinite.

## Exact finite witnesses

At a cutoff containing \(N\) distinct scale labels \(u_1,\ldots,u_N\), the first \(N\) moment readouts form the Vandermonde matrix

\[
V_{jk}=u_j^k.
\]

Its determinant is

\[
\det V=\prod_{i<j}(u_j-u_i),
\]

which is nonzero for distinct labels. The checker verifies exact ranks \(1\) through \(8\) over the rationals. Because the rank grows with every enlarged set of labels, no fixed finite closure law exists.

## Consequence

The regular-parallel-line route closes for the native moment prolongation.

The full source state may have a regular spectral generator, but the endpoint scalar is an observation of an infinite-dimensional transported state. Its zeros can arise from cancellation among moment directions without any singularity in the state connection.

This returns the geometric picture to its correct form:

- an off-seam zero is not necessarily a puncture of the full state bundle;
- it is first a null of one distinguished scalar projection;
- excluding it requires an orientation or noncancellation law on the infinite observable module.

## What could evade the no-go

Only a source-derived quotient or recurrence could collapse the moment orbit. It must be constructed before endpoint projection and preserve every finite labelled cutoff. A recurrence inferred from the scalar transform is circular.

Finite support would also give finite closure, but it is incompatible with the completed theta source.

## DPC verdict

Candidate: prolong the source under spectral differentiation and obtain a rank-one endpoint line.

Verdict: rejected by Vandermonde rank growth.

Candidate: obtain a fixed finite-rank endpoint system.

Verdict: rejected under infinite source support unless an independent source relation identifies moment directions.

Surviving architecture: an infinite moment observer coupled to arithmetic transport, moving seam, and boundary anomaly data. Any RH-bearing theorem must control scalar cancellation on this completed module without assuming scalar positivity or inspecting zeros.

## Next finite question

The smallest useful source test is no longer orbit rank. It is whether the two-sector sewing supplies a bilinear or Clifford form on the moment module that is:

1. preserved by the spectral multiplication operator;
2. preserved by labelled prime transport and moving-seam incidence;
3. nondegenerate after completion;
4. strong enough to prevent the endpoint covector from annihilating a nonzero admissible state off seam.

A two-label or three-label Gram minor violating preservation is the immediate falsifier.

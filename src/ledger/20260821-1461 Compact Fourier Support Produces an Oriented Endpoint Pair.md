---
author: marici.Nima
---

# 1461 — Compact Fourier Support Produces an Oriented Endpoint Pair

## Status

Exact support-sensitive instance of Entry 1460's vertexwise Fourier
pushforward. A compact coefficient support produces two projected endpoint
singularities with opposite orientations. They are the boundary of the
support chain, not a new carrier incidence operation.

## Frozen coefficient density

At one labelled vertex choose the admissible compact Fourier density

\[
\widetilde\lambda(\epsilon)
=\mathbf 1_{[0,\Lambda]}(\epsilon),
\qquad
\Lambda>0.
\]

The translated source wall remains the Entry 1460 family

\[
q+\epsilon=0.
\]

Against one simple universal-integrand pole, its coefficient pushforward is

\[
\boxed{
F_\Lambda(q)
=\int_0^\Lambda\frac{d\epsilon}{q+\epsilon}
=\log(q+\Lambda)-\log q.
}
\]

No pole or endpoint has been fitted after integration: both endpoints are
the image of the frozen boundary \(\partial[0,\Lambda]\).

## Exact logarithmic connection

Differentiation gives

\[
dF_\Lambda
=-\frac{\Lambda}{q(q+\Lambda)}dq.
\]

Its oriented residues are

\[
\operatorname{Res}_{q=0}dF_\Lambda=-1,
\qquad
\operatorname{Res}_{q=-\Lambda}dF_\Lambda=+1,
\qquad
\operatorname{Res}_{q=\infty}dF_\Lambda=0.
\]

Thus

\[
\boxed{(-1,+1)=\partial[0,\Lambda].}
\]

The apparent branch interval \(q\in[-\Lambda,0]\) is the Betti image of the
translated wall over the support chain. Algebraically, only its two endpoint
images enter the logarithmic singular divisor.

## Beck–Chevalley classification

Before pushforward, resolved Cut acts on the universal integrand and retains
the labelled vertex and Fourier occurrence. The compact map is proper on the
chosen support. After pushforward, the two endpoint Gysin terms reproduce the
oriented boundary of that same support. Therefore the support-sensitive
comparison closes in the relative coefficient category:

\[
\boxed{
\text{translated existing wall}
+
\text{compact coefficient chain}
+
\text{its oriented endpoint Gysin pair}.
}
\]

No additional energy-incidence generator or Cut primitive is required.

## What ordinary scalarization would miss

Treating \(F_\Lambda\) as merely a multivalued scalar forgets the interval
whose boundary fixes the relative sign. It would leave two apparently
unrelated logarithmic walls. The source coefficient support supplies their
coherence.

## Scope boundary

This is the one-wall, one-vertex compact-support test. It does not prove
base change for overlapping regional denominators or for a Fourier density
with an internal singularity or Stokes boundary.

## Next falsifier

Use a density with one internal jump inside a compact support. Determine
whether subdivision additivity makes the internal contributions cancel, or
whether the jump carries an additional supported coefficient object under
resolved Cut.

## Durable evidence

- `research/nima/check_box_fourier_pushforward_boundary.py`;
- `research/nima/results/box-fourier-pushforward-boundary.json`;
- allocator claim `seqclaim-ae5a98f9a83bb180f96b183d`.

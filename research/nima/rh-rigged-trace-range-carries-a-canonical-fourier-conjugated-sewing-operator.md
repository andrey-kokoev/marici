# The RH rigged trace range carries a canonical Fourier-conjugated sewing operator

Author: `marici.Nima`

Date: 2026-08-26

Status: algebraic operator lift on the source trace range; closability remains

## Why the Hilbert restriction failed

The ideles have additive Haar measure zero inside the adeles. Consequently an
additive (L^2) equivalence class has no well-defined restriction to the
idelic boundary.

This blocks a bounded Hilbert trace. It does not block restriction of
continuous Schwartz--Bruhat functions before completion.

## Density and injectivity

The ideles are dense in the adeles for the restricted-product topology. A
basic adelic neighborhood constrains only finitely many local coordinates;
all unconstrained coordinates can be chosen to be local units. Hence every
adele is approximated by ideles.

Let

\[
\tau:\mathcal S(\mathbb A)
\longrightarrow
\mathcal T(\mathbb A^\times)
\]

be restriction to the idelic trace space. Since Schwartz--Bruhat functions
are continuous and the ideles are dense, (	au) is injective on its source
domain.

Thus every element of the trace range has a unique source representative.

## Canonical sewing on the range

Let $\mathcal F$ be additive adelic Fourier transform. Define an operator on
the trace range by

\[
J_0(\tau\phi)=\tau(\mathcal F\phi).
\]

Injectivity of (	au) makes this definition unambiguous. No scalar Tate
factor or completed zeta function is used.

Because Fourier transform is invertible on the Schwartz--Bruhat source,

\[
J_0^{-1}(\tau\phi)
=
\tau(\mathcal F^{-1}\phi).
\]

Therefore (J_0) is an exact source-derived reciprocal operator on

\[
\operatorname{Ran}\tau.
\]

This is the operator whose scalar Mellin matrix coefficients produce the Tate
transition factors.

## What has been gained

The global operator lift no longer lacks algebraic genesis. Its constructor
sequence is explicit:

```text
Schwartz--Bruhat source
  -> injective idelic trace
  -> additive Fourier transform on the unique source representative
  -> idelic trace of the transformed source
```

The reciprocal inverse is inherited from inverse Fourier transform.

Scalar gamma reciprocity is downstream of this operator, rather than the
authority used to manufacture it.

## Remaining analytic gate

The range (operatorname{Ran}\tau) is not yet equipped with the completed
boundary topology required by primitive, square, seam, and archimedean
currents. The exact questions are:

1. Is (J_0) closable in the proposed rigged trace topology?
2. Does its inverse remain densely defined after completion?
3. Do arithmetic cutoff maps preserve its graph?
4. Does its operator supply cocycle extend continuously?
5. Does the completed trace retain every source direction needed for
   observability?

The earlier Hankel--Volterra range-density obstruction is one concrete form of
this closability problem.

## Compression hostile

If the trace map is replaced by a noninjective scalar readout, the conjugated
operator need not be well defined. Two source states can have the same visible
trace while their Fourier transforms have different traces.

This is precisely why the completed scalar Tate integral cannot reconstruct
(J_0). The complete rigged trace range must be retained.

## Reciprocal-sewing consequence

On the algebraic trace range, the two sector maps are already inverse Fourier
transports. Their operator supply residuals cancel by the reciprocal cocycle.

The RH-bearing frontier is now completion stability and strict observability,
not existence of an abstract operator formula.

## Finite falsifiers

A proposed finite trace model fails if:

- its trace map has a kernel not preserved by Fourier transform;
- the induced sewing depends on the chosen source representative;
- forward and inverse sewing fail to compose to the identity on the trace
  range;
- scalar compression is substituted for the injective trace carrier.

# Gamma-Bockstein is projectively unique before source normalization

## Question

Does the two-prime rank-one result already make the gamma-Bockstein the unique constructor resolving the conductor descent defect?

## Intrinsic quotient

Let (R) be the two-dimensional exact-relation space and (K\subset R) its root-invisible line. The root-visible quotient (R/K) is one-dimensional. Benincasa's calculations at primes 32009 and 32003 show that the gamma-Bockstein vanishes on (K) and has rank one on (R/K).

Once the target image line (L) is fixed, every linear constructor with those properties has the form

\[
\beta_\lambda(k,v)=\lambda v,
\qquad \lambda\ne0.
\]

Therefore the kernel, quotient, and image data determine one projective constructor class. They do not determine its absolute scale.

## Hostile rescaling

Rescale the declared normal coordinate by a nonzero factor. Its derivative rescales contravariantly, while the invisible kernel, visible quotient, rank-one image, and all zero-versus-nonzero tests remain unchanged. The existing two-prime checks cannot distinguish this family.

This does not defeat the gamma-Bockstein. It identifies its last authority port. An absolute constructor requires:

1. a source-declared normal coordinate;
2. a source-declared generator of the target coherence line;
3. the chain or residue convention fixing their pairing;
4. covariance of the scalar under labelled conductor chart transitions.

With that unit fixed, the requirements

\[
\beta(K)=0,
\qquad
\beta(v)=u_L
\]

determine the constructor uniquely.

## Deutsch verdict

The explanatory content already forced is the direction: only the root-odd normal class can repair descent. The magnitude is not yet hard to vary. It becomes explanatory only when the gamma normalization and target-line unit are derived from the source and transported covariantly between conductor charts.

The next falsifier is a normal-coordinate rescaling. Any absolute uniqueness claim that leaves the rescaling unrecorded fails; a correctly typed claim transforms the Bockstein coefficient and preserves the underlying projective constructor.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_gamma_bockstein_projective_uniqueness.py
```

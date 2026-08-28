# Reciprocal gluing is a Real structure before low-grade completion

## Prime-orbit return pair

For a real source \(\phi\), the shell returns satisfy

\[
\beta_{p,j}(-it)=\overline{\beta_{p,j}(it)}.
\]

The direct and reciprocal prime weights on the centered seam are

\[
q_p^+=p^{-1/2-it},
\qquad
q_p^-=p^{-1/2+it}
=\overline{q_p^+}.
\]

Consequently every cyclic grade has an exact conjugate pair:

\[
u_{p,j,k}^-
=
\overline{u_{p,j,k}^+},
\qquad
u_{p,j,k}^{\pm}=(q_p^{\pm})^k\beta_{p,j}(\pm it).
\]

This defines an antiunitary exchange on the doubled Markov-return carrier.

## The seam is the isometric locus

At centered parameter \(z=x+it\), reciprocal weights have moduli

\[
|q_p^+|=p^{-1/2-x},
\qquad
|q_p^-|=p^{-1/2+x}.
\]

Their norms agree for every nonzero prime block exactly when \(x=0\).
Thus the centered seam is the locus where reciprocal exchange is an isometry
of the actual boundary-return realization, not merely of scalar Euler factors.

This explains the seam's unitary role. It does not prove nonvanishing of a
global section there or exclusion of zeros elsewhere.

## Completion order

The all-prime filtration makes the order of operations compulsory.

For \(k=1\), the return family is not Hilbert–Schmidt. For \(k=2\), it is
Hilbert–Schmidt but not trace class. These grades cannot be independently
completed into ordinary determinants and only afterward paired.

The lawful order is:

1. form the finite direct/reciprocal Real pair;
2. retain its symmetric and antisymmetric boundary quadratures;
3. apply source-authorized paired counterterms;
4. verify the counterterms respect conjugate exchange;
5. take the completed relative limit.

For \(k\geq3\), the trace-class tail may be completed ordinarily and then
equipped with the induced Real structure.

## Counterterm coherence

Let \(r_X^+\) and \(r_X^-\) be finite-cutoff low-grade counterterms. Real
sewing requires

\[
r_X^-=\overline{r_X^+}.
\]

Independent subtraction on the two sheets can preserve separate finite
convergence while destroying the exchange law. Equality of final scalar
determinants cannot repair that lost orientation.

The primitive and square boundary currents are therefore coherence data for
the paired completion. They are not disposable divergences.

## DPC verdict

Resolved:

- exact conjugate matching of every finite prime-orbit Markov grade;
- the centered seam as the unique isometric reciprocal locus;
- the required order of Real pairing and low-grade renormalization;
- a finite counterterm-coherence falsifier.

Withheld:

- source construction of the paired primitive and square counterterms;
- convergence of their all-prime relative limit;
- the archimedean comparison;
- the zero-state-to-flux bridge.

The smallest falsifier is one finite cutoff at which the two counterterms fail
the conjugacy relation. Such a failure rejects reciprocal completion even if
both scalar renormalizations converge.

## Verification

The checker `check_reciprocal_real_markov_gluing.py` verifies finite conjugate
matching through six cyclic grades, loss of isometry off the centered seam,
and failure under independently chosen counterterms.

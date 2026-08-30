# Prime-power cumulants are not independent Schur boundary ports

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: source-typing obstruction and revised global target

## Proposed lift

The minimal doubled-tail realization has a scalar boundary Schur complement.
A natural next proposal is to enlarge its boundary space by adjoining separate
ports for the primitive, prime-square, connected-tail, and archimedean
channels.

The arithmetic source rejects this direct-sum interpretation.

## One primitive loop, many cyclic readouts

In the Euler chamber, put

\[
 \mathcal H_{\mathrm{pr}}=\ell^2(\mathbb P)
\]

and define the primitive diagonal loop

\[
 L_s e_p=p^{-s}e_p.
\]

Then

\[
 \det(I-L_s)^{-1}
 =\prod_p(1-p^{-s})^{-1},
\]

and its logarithm is

\[
 -\log\det(I-L_s)
 =\sum_{k\ge1}\frac1k\operatorname{Tr}(L_s^k)
 =\sum_{p,k\ge1}\frac{p^{-ks}}k.
\]

Therefore the three regularity levels

\[
 k=1,\qquad k=2,\qquad k\ge3
\]

are not independent state channels.  They are cyclic word lengths of the
same primitive feedback operator.  Their source-authorized composition is
the relative determinant

\[
 \det(I-L_s)
 =\det_3(I-L_s)
 \exp\left(
 -\operatorname{Tr}L_s
 -\frac12\operatorname{Tr}(L_s^2)
 \right),
\]

with the overall signs reversed if the reciprocal determinant convention is
used.

Adjoining one Hilbert-space boundary coordinate for every cumulant would
replace cyclic reconstruction by operator addition.  It would introduce
cross terms absent from the source and double-count repeated returns of one
prime mode.

## Two legitimate realizations of different variance

The theta realization is additive and entire:

\[
 S_\partial^{\theta}(z)
 =G_+(0;z)+G_-(0;z).
\]

The Euler realization is multiplicative and labelled:

\[
 S^{\mathrm{Euler}}(s)
 =\det(I-L_s)^{-1}.
\]

They agree, after the archimedean line and normalization are included, in the
Euler chamber and hence define the same scalar completed section by analytic
continuation.  But they are not related by a linear compression between
boundary state spaces:

- the theta Schur complement sums propagated source amplitudes;
- the Euler determinant exponentiates connected cyclic traces;
- the archimedean factor is an independent determinant-line extension;
- global Poisson sewing acts before Euler factorization and has no
  finite-Euler constructor.

The comparison therefore belongs at determinant-line or correspondence
level, not as an ordinary block enlargement of the theta boundary space.

## Grading route closes locally

The natural Euler grade does not make the primitive feedback strictly
raising.  The operator (L_s) is diagonal in the prime label, and every
power (L_s^k) is a closed return to the same primitive mode.  Prime-power
degree records loop length, not a well-founded state grade.

Consequently the proposal that (L_s) strictly raises grade is false for the
source-native Euler realization.  Turning cyclic length into
an independent state grade would manufacture the desired triangularity.

## Revised target

The missing unaggregated object is not a larger scalar Schur matrix with four
manually adjoined ports.  It is a source-derived comparison

\[
 \alpha_s:
 \mathcal L_{\theta}(s)
 \longrightarrow
 \mathcal L_{\infty}(s)
 \otimes
 \operatorname{Det}_{\mathrm{rel}}(I-L_s)
\]

between the additive theta boundary line and the multiplicative graded Euler
determinant line.

Section rigidity requires (\alpha_s) to be an isomorphism wherever both
presentations are constructed.  RH-strength content would require an
additional source law on this comparison that is not already lost under the
determinant functor.

The sharp falsifier for any proposed lift is now:

1. does it reconstruct the cyclic factor (1/k\) without treating (k\) as an
   independent source state;
2. does it retain the first two cumulants as typed boundary coordinates;
3. does it avoid finite-Euler Poisson sewing;
4. does it derive, rather than assume, the determinant-line comparison;
5. does any claimed grade survive the closed prime loops (L_s^k\)?

## Result

The naive unaggregated Schur lift is ill-typed.  Arithmetic labels survive in
the primitive loop, while prime-power levels survive as cyclic cumulants of
that loop.  The entire theta Schur section and the labelled Euler determinant
meet only through a nonlinear determinant-line comparison.  Constructing that
comparison before scalarization is the next legitimate global problem.

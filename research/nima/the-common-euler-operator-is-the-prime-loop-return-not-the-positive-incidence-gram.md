# The common Euler operator is the prime-loop return, not the positive incidence Gram

## The provenance question

The determinant bridge requires one operator whose first two traces are the
primitive and square anomaly coordinates and whose regularized determinant
contains the connected grades.

The weighted arithmetic-to-analytic incidence

\[
\mathcal I e_{p,k}
=
\frac1k p^{-k/2}u_{p,k}
\]

is already source-derived. It is tempting to use its positive Gram
\(\mathcal I^*\mathcal I\) as the common determinant operator. That cannot
produce the required linear Euler currents.

## Gram mismatch

On a prime-diagonal source core,

\[
\langle \mathcal I e_{p,k},\mathcal I e_{p,k}\rangle
=
\frac1{k^2}p^{-k}\|\Phi\|_2^2.
\]

Thus the diagonal of \(\mathcal I^*\mathcal I\) contains squared coefficients.
Its trace begins with

\[
\sum_{p,k}\frac1{k^2}p^{-k},
\]

whereas the connected Euler logarithm uses

\[
\sum_{p,k}\frac1k p^{-ks}.
\]

No source-independent normalization converts all squared incidence weights
back to the linear coefficients. Taking a square root after forming the Gram
would discard phase, orientation, and endpoint typing.

Therefore the positive incidence Gram can supply Green energy, but it cannot
be the determinant-provenance operator.

## Prime-loop return operator

In the absolute convergence region \(\operatorname{Re}s>1\), define on the
prime label space

\[
L(s)e_p=p^{-s}e_p.
\]

Then \(L(s)\) is trace class and

\[
\operatorname{Tr}L(s)^k
=
\sum_p p^{-ks}.
\]

Consequently

\[
-\log\det(I-L(s))
=
\sum_{k\ge1}\frac1k\operatorname{Tr}L(s)^k
=
\sum_{p,k}\frac1k p^{-ks}
=
\log\zeta(s).
\]

The three determinant strata are now powers of one common operator:

\[
P_1(L)=\operatorname{Tr}L,
\qquad
P_2(L)=\frac12\operatorname{Tr}L^2,
\]

and

\[
\det(I-L)^{-1}
=
e^{P_1(L)+P_2(L)}
\det_3(I-L)^{-1}.
\]

This is the exact common-operator provenance required by the finite
third-order boundary character.

## Why this is still not the RH pencil

The diagonal prime-loop return is source-arithmetic and non-tautological, but
it exists as an ordinary trace-class determinant only for
\(\operatorname{Re}s>1\). Near the critical strip,

\[
\sum_p|p^{-s}|
\]

diverges, so \(L(s)\) is not trace class. At the half-density it is not even
Hilbert--Schmidt because

\[
\sum_p p^{-1}=\infty.
\]

Only the square and connected strata acquire their stronger Hilbert and
trace-ideal control after separate typing. The primitive stratum remains
distributional.

Hence there is no ordinary prime-Hilbert Fredholm determinant
\(\det(I-L(s))\) available across the critical strip. Analytic continuation of
the scalar Euler product does not extend the operator automatically.

## Required completed lift

A meaningful completed pencil must lift the prime-loop return into the
three-stratum boundary carrier:

\[
L_{\mathrm{comp}}(s):
\mathcal B^{(1)}
\oplus
\mathcal B^{(2)}
\oplus
\mathcal B^{(3)}
\longrightarrow
\mathcal B^{(1)}
\oplus
\mathcal B^{(2)}
\oplus
\mathcal B^{(3)},
\]

where:

- the primitive trace is a distributional boundary functional;
- the square trace is a Hilbert pairing;
- the connected return is determinant-class;
- seam and archimedean lines trivialize the first two anomaly coordinates;
- reciprocal sewing supplies the closed boundary relation.

The completed determinant is therefore a relative determinant-line section,
not the ordinary Fredholm determinant of a bounded prime-space operator.

## Relation to the Green pencil

The source architecture now contains two distinct descendants of the same
linear incidence:

1. the positive quadratic descendant \(\mathcal I^*G\mathcal I\), which carries
   Green coercivity;
2. the ordered prime-loop descendant \(L\), whose powers carry determinant
   multiplicities.

The missing spectral-identification theorem must construct them as two
functorial shadows of one labelled source system and prove that their kernel
and determinant defects coincide after boundary reduction.

Identifying them directly is impossible: one is quadratic and positive, the
other is linear and ordered.

## Kernel-state consequence

In \(\operatorname{Re}s>1\), \(I-L(s)\) is invertible because
\(|p^{-s}|<1\) primewise. Its determinant gives the zero-free Euler region.
This is a genuine source-derived spectral fact but does not approach the
nontrivial zeros.

Any critical-strip kernel state must arise only after seam, archimedean, and
reciprocal completion. It cannot be a primewise eigenvector of the diagonal
operator \(L(s)\), since \(p^{-s}\ne1\) there.

Thus the completed zeta zeros are necessarily global boundary defects, not
local prime-loop resonances.

## Hostiles

1. Use \(\mathcal I^*\mathcal I\) and claim its trace is the primitive Euler
   current.
2. Analytically continue \(\det(I-L(s))\) as a scalar and call the continued
   value an operator determinant.
3. Treat primitive, square, and connected currents as traces of different
   unrelated operators.
4. Search for \(p^{-s}=1\) as the local origin of nontrivial zeta zeros.
5. Manufacture a rank-one Xi determinant after scalar aggregation.

## Verdict

The unique elementary common operator behind the Euler determinant strata is
the ordered prime-loop return \(L(s)\), not the positive incidence Gram. Its
powers exactly generate the primitive, square, and connected coefficients in
the Euler region.

The critical-strip problem is now sharply typed: construct a source-derived
three-stratum relative lift of \(L(s)\), with seam and archimedean anomaly
trivialization, and compare its global boundary kernel to the positive Green
pencil.

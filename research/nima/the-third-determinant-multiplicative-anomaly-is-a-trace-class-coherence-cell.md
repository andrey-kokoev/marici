# The third-determinant multiplicative anomaly is a trace-class coherence cell

## Product composition

Write the product of two perturbation factors as

\[
(I-A)(I-B)=I-(A\star B),
\]

where

\[
A\star B=A+B-AB.
\]

Ordinary determinants multiply. The third regularized determinants do not
multiply strictly because their low-grade counterterms change under
composition.

Define the logarithmic anomaly

\[
\alpha_3(A,B)
=
\log\det_3(I-(A\star B))
-\log\det_3(I-A)
-\log\det_3(I-B).
\]

## Exact formula

The ordinary determinant terms cancel. Expanding the primitive and square
counterterms and using cyclicity of trace gives

\[
\alpha_3(A,B)
=
-\operatorname{Tr}(A^2B)
-\operatorname{Tr}(AB^2)
+\frac12\operatorname{Tr}((AB)^2).
\]

Every term begins at total degree three. If \(A\) and \(B\) lie in the
third Schatten class, Hölder's inequality places the cubic products in trace
class; the quartic term is trace class as well.

Thus the anomaly is defined exactly where the ordinary grade-three determinant
tail becomes available. It is not another primitive or square divergence.

## Coherence law

The product operation \(\star\) is associative because operator
multiplication is associative. The anomaly satisfies

\[
\alpha_3(A,B)
+\alpha_3(A\star B,C)
=
\alpha_3(B,C)
+\alpha_3(A,B\star C).
\]

This is the additive 2-cocycle law. Exponentiating gives the comparison cell
that coheres the two parenthesizations of three regularized factors.

The anomaly should therefore be retained as a lawful coherence cell, not
treated as failure of multiplicativity and not canceled by a fitted scalar.

## Reciprocal dagger

Dagger reverses product order:

\[
((I-A)(I-B))^*
=(I-B^*)(I-A^*).
\]

Accordingly,

\[
\alpha_3(B^*,A^*)
=
\overline{\alpha_3(A,B)}.
\]

The reciprocal sector carries the conjugate anomaly with reversed route
order. This is the required Real typing of the composition cell.

## Meaning for the prime attachment

Direct sums of independent prime blocks have no multiplicative anomaly.
An anomaly appears only when source operations are composed as interacting
operator factors. Its value therefore detects genuine route structure that a
flat Euler product presentation omits.

For the theta–Euler comparison, the next source calculation is no longer
whether an anomaly exists abstractly. It is:

1. identify the actual ordered relative-transfer factors;
2. compute their \(\alpha_3\) cells;
3. test whether cross-prime cells vanish, telescope, or survive;
4. verify reciprocal order reversal;
5. control the cocycle under the restricted-product limit.

## DPC verdict

Resolved:

- the exact third-determinant multiplicative anomaly;
- its trace-class degree;
- its 2-cocycle coherence law;
- reciprocal conjugacy with reversed order.

Withheld:

- source identification of the theta–Euler factorization route;
- cross-prime anomaly values;
- completed cocycle summability;
- archimedean and zero-state bridges.

The finite falsifier for a proposed strict product law is any pair with
nonzero \(\alpha_3(A,B)\). The falsifier for a proposed coherencer is failure
of the three-factor cocycle identity.

## Verification

The checker `check_det3_multiplicative_anomaly.py` verifies the closed formula,
the cocycle law on exact rational matrices, nonzero strictness hostiles, and
dagger order reversal.

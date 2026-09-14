# The semilocal logarithmic divergence is an infinite-rank identity feature and cannot be identified with the Eisenstein radical without a new intertwiner

## Divergent term in the trace theorem

For a convolution square

\[
h=g*g^*,
\]

Connes's semilocal trace theorem gives

\[
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h))
=
2\log\Lambda\|g\|^2
+
W_S(h)
+
o(1).
\]

The divergent quadratic form is therefore

\[
D_\Lambda(g)
=
2\log\Lambda\langle g,g\rangle.
\]

Its polarization is

\[
D_\Lambda(g_1,g_2)
=
2\log\Lambda\langle g_1,g_2\rangle.
\]

Thus its Gram operator is exactly

\[
\boxed{
2\log\Lambda I.
}
\]

It is not rank one and is not an endpoint evaluation.

## Any asymptotic feature is an isometric copy of the source

Suppose one realizes the divergence by a feature map

\[
\Xi_\Lambda:\mathcal H_{obs}	o\mathcal K_\Lambda
\]

such that

\[
\|\Xi_\Lambda g\|^2
=
2\log\Lambda\|g\|^2.
\]

Then

\[
\Xi_\Lambda^*\Xi_\Lambda
=
2\log\LambdaI,
\]

and hence

\[
\frac1{\sqrt{2\log\Lambda}}
\Xi_\Lambda
\]

is an isometry on the entire observer Hilbert space.

Therefore the divergent feature has infinite rank whenever the observer space is infinite-dimensional:

\[
\boxed{
\operatorname{rank}\Xi_\Lambda
=
\dim\mathcal H_{obs}.
}
\]

It cannot be identified with one scalar vacuum line merely because its coefficient is `h(1)`.

## The Eisenstein map

In the archimedean discussion of Connes--Consani--Moscovici, the map is

\[
E=w\mathcal E,
\qquad
(\mathcal E f)(x)
=
\sum_{n\ge1}f(nx).
\]

Its natural Schwartz domain is restricted by the two conditions

\[
f(0)=0,
\qquad
\widehat f(0)=0
\]

(or the equivalent integral condition in the chosen normalization).

For their special prolate/Hermite vectors, Proposition 3.6 proves

\[
\mathcal F_\mu(Ef)(s)
=
R_f(s)\xi(1/2+is),
\]

where `R_f` is an entire/polynomial factor. The quotient by the closure of these images has multiplication spectrum at the nontrivial zeta zeros.

This is a zeta-bearing range selected by endpoint-vanishing conditions. It is not identified in the cited theorem with the universal identity divergence of the cutoff trace.

## Domain mismatch

The logarithmic divergence occurs for every compactly supported observer `g` and depends only on

\[
\|g\|^2.
\]

The Eisenstein map is defined on a source subspace satisfying two endpoint conditions and its image depends arithmetically on the sum over positive integers.

Thus an equality of the form

\[
\Xi_S(g)=E(g)
\]

is not even typed on the unrestricted observer space without:

1. a projection enforcing the two endpoint conditions;
2. a choice of preimage for the remaining endpoint coordinates;
3. proof that the resulting `E`-norm equals `||g||`;
4. compatibility with the semilocal cutoff geometry.

None of these is supplied by Theorem 4 or Proposition 3.6.

## A positive quotient cannot be asserted from a scalar subtraction

The finite part

\[
W_S(h)
=
\operatorname*{FP}
\operatorname{Tr}(P_\Lambda\widehat P_\Lambda U_S(h))
\]

is defined by subtracting the positive scalar form

\[
2\log\Lambda\|g\|^2.
\]

To realize this subtraction as a Hilbert quotient, one would need an orthogonal feature decomposition

\[
F_\Lambda g
=
\sqrt{2\log\Lambda}J_\Lambda g
\oplus
F_\Lambda^{fin}g,
\]

where `J_Lambda` is an isometry and the first summand lies in a common closed subspace independent of `g` except through that isometric copy.

The scalar trace asymptotic determines only

\[
\|F_\Lambda g\|^2
-
2\log\Lambda\|g\|^2,
\]

not such an orthogonal vector decomposition. Correlated cross terms can contribute to the same scalar asymptotic.

Therefore quotienting a guessed divergent subspace would be another tautological completion unless the source provides the feature-level intertwiner.

## Relation between the two infinite-rank spaces

Both the divergence feature and `ran E` are infinite-dimensional, so rank alone does not rule out an intertwiner. But equality of dimensions is insufficient. One needs a concrete operator

\[
J_{S,\Lambda}:
\mathcal H_{obs}	o
\overline{\operatorname{ran}E_S}
\]

satisfying

\[
J_{S,\Lambda}^*J_{S,\Lambda}=I
\]

and an asymptotic factorization of the cutoff operator through `J_S,Lambda`.

The zeta factorization

\[
\mathcal F_\mu E(f)
=
R_f\xi
\]

makes such an isometry highly nontrivial: the natural `L2` norm contains `|xi|^2`, not the source norm, unless compensated by the dual Hardy--Titchmarsh weight.

This points back to the two-space canonical/dual pairing rather than an ordinary one-space quotient.

## Correct revised target

One must distinguish two operations:

1. **universal volume renormalization**, removing the identity divergence `2 log Lambda I`;
2. **arithmetic conditioning**, quotienting or orthogonalizing against `overline{ran E_S}`.

They may ultimately be implemented by one larger construction, but they cannot be identified without proof.

A correctly typed target is a source-derived asymptotic unitary colligation

\[
\mathcal U_{S,\Lambda}:
\mathcal H_{obs}
	o
(\mathcal H_{vol,S}
\oplus
\mathcal H_{arith,S}),
\]

such that:

\[
P_\Lambda\widehat P_\Lambda U_S(g)

=
\sqrt{2\log\Lambda}J_{vol,S}g
\oplus
F_{arith,S}(g)
+
o(1)
\]

at feature level, with

\[
J_{vol,S}^*J_{vol,S}=I
\]

and the arithmetic component conditioned by `ran E_S`.

The displayed feature equality is not proved by the scalar trace theorem; it is the new theorem required.

## Disposition

The proposed direct identification

\[
\text{cutoff divergence}
=
\overline{\operatorname{ran}E_S}
\]

is unsupported and generally mistyped. The divergence is an infinite-rank identity feature on the entire observer space, while the Eisenstein range is an arithmetic subspace generated from endpoint-vanishing data.

The next construction must first lift Connes's scalar trace asymptotic to a feature-level asymptotic colligation. Only then can one test whether its finite arithmetic component is the semilocal Eisenstein/Sonin quotient and whether positivity survives.

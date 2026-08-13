# Yang–Mills as a Multi-Normal Residue

## Record

Date: 2026-08-12

Status: established scaffolding construction; intrinsic jet interpretation proposed with a precise qualification.

## Result

The Yang–Mills branch is naturally interpreted as

\[
\mathrm{YM}
=
H_{\mathrm{gauge}}\!\left(
\mathbb J_{\mathfrak f}\mathrm{Scalar}
\right),
\]

where \(\mathbb J_{\mathfrak f}\) is the component of multidegree \((1,\ldots,1)\) in the fusion-normal variables. It is not the ordinary first jet of the total fusion ideal.

## Fusion geometry

For paired scaffold scalars \((2a-1,2a)\), the fusion locus puts

\[
q_a=p_{2a-1}+p_{2a}
\]

on shell. The polarization information is represented by

\[
\epsilon_a\sim p_{2a}-p_{2a-1},
\qquad
\epsilon_a\sim\epsilon_a+\alpha q_a.
\]

The corresponding physical state fiber is

\[
E_a
=
q_a^\perp/\langle q_a\rangle.
\]

This state object is intrinsic to the kinematic scalar master geometry, not to the topology of the marked surface alone.

## What the first jet actually is

If \(D_a=(s_a=0)\), the intrinsic datum for a surface function is its class modulo \(s_a^2\). There is no canonical decomposition into value plus normal derivative without a splitting of the first-neighborhood sequence.

The scaffolding construction supplies a stronger object: a canonical form locally of the shape

\[
\frac{ds_a}{s_a^2}F(s_a).
\]

Its residue selects the coefficient linear in \(s_a\). Consecutive residues select

\[
\mathbb J_{\mathfrak f}F
=
[s_1s_2\cdots s_n]F
\in
\bigotimes_{a=1}^nN_{D_a}^{\vee}.
\]

Thus “first normal jet” should mean either a conormal-line-valued symbol or this coordinate-invariant normal residue. A bare scalar derivative is too strong.

## Cut relation

For one common normal parameter, first jets satisfy the Leibniz rule:

\[
\Delta_Cj^{[1]}F_\Sigma
=
j^{[1]}F_L\,F_R
+
F_L\,j^{[1]}F_R
\]

when the internal sewing kernel is deformation-independent. If it deforms, its first jet contributes a third term.

The formula

\[
\Delta_CJ^1=(J^1\otimes J^1)\Delta_C
\]

is therefore false as an untruncated tensor identity. It becomes correct only in the algebra of first principal parts after diagonal pullback and truncation to total degree one.

For the all-leg multi-normal residue, a cut that partitions complete fusion pairs gives

\[
\Delta_C\mathbb J_{\mathfrak f}
=
\mathbb J_{\mathfrak f_L}
\otimes
\mathbb J_{\mathfrak f_R},
\]

with the appropriate coevaluation on new internal flags.

## First geometric failure

Naive factorization fails when:

1. a cut separates the two members of a fusion pair;
2. fusion and cutting meet nontransversely;
3. a nonseparating cut turns an external normal direction into an internal state flag;
4. the internal state metric itself varies along the fusion divisor.

The expected repair uses derived normal jets together with an explicit state-space coevaluation.

## Loop status

The scalar-scaffolding proposal is formulated at arbitrary loop order and has nontrivial leading-singularity checks through two loops. The published proof that a loop cut matches tree gluing modulo a total derivative is, however, strictly a one-loop argument.

This distinction must be retained:

\[
\text{all-loop proposal and checks}
\neq
\text{all-loop proof of strict surface-cut naturality}.
\]

## Next falsification tests

1. Construct the fusion divisors and their normal bundles independently of a chosen triangulation.
2. Express the scaffolding residue as a Poincaré or logarithmic residue on the surface moduli object.
3. Check the multi-normal base-change square for cuts crossing newly created internal flags.
4. Determine whether total-derivative equivalence forms a hereditary cut-and-sew ideal.
5. Test whether the local metric \(g\) is flat along every fusion divisor.

## Prohibited overclaims

Do not claim that:

- the raw normal derivative is intrinsic for an arbitrary function;
- \(J^1\otimes J^1\) is a first-order operation without diagonal truncation;
- the one-loop total-derivative proof establishes strict all-loop equality;
- gauge cohomology follows from surface topology without kinematic state data.

## Source

- [Scalar-Scaffolded Gluons and the Combinatorial Origins of Yang-Mills Theory, v3](https://arxiv.org/html/2401.00041v3)

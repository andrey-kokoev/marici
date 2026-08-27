# Holomorphy protects the wrong operator class: WP766

## Question

Can supersymmetric nonrenormalization fix the additive threshold boundary that
destroys WP765's numerical portal prediction?

## Claim boundary

Embed the relevant fields in \(N=1\) chiral superfields \(N\) and \(X\). The
selected CP-even real-norm portal is represented by

\[
\int d^4\theta\,
(N^\dagger N)(X^\dagger X).
\]

This is an operator-typing question. Standard superpotential
nonrenormalization applies to holomorphic chiral integrands under
\(d^2\theta\), not to arbitrary full-superspace Kähler operators. Explicit
one-loop corrections to general \(N=1\) Kähler potentials were computed by
[Brignole](https://arxiv.org/abs/hep-th/0001121).

## Exact typing

Each norm bilinear has zero R-charge,

\[
R(N^\dagger N)=0,
\qquad
R(X^\dagger X)=0.
\]

Their product is therefore an allowed R-neutral real D-term. But it contains
antichiral fields and cannot be a holomorphic superpotential monomial. The
ordinary superpotential theorem does not constrain its renormalized Kähler
coefficient.

Consequently the allowed boundary

\[
c_K=-\frac{9}{50}
\]

cancels the WP764 value in the unit matching convention without violating
\(N=1\) superspace typing.

## Extended-supersymmetry dichotomy

WP751 already computed the strongest nearby repair. Exact \(N=2\) ties the
hypermultiplet interaction to the gauge metric but forces the extra
nondecoupling portal to vanish. Breaking to \(N=1\) restores a nonzero portal
only together with an independently variable Wilson coefficient and breaking
scale.

On the exact \(N=2\) branch,

\[
\Delta_{\mathrm{extra}}=0.
\]

On the broken \(N=1\) branch, the portal can be nonzero but carries an
independent coefficient:

\[
\Delta_{\mathrm{extra}}\neq0.
\]

## Disposition

Holomorphy protects the wrong operator class. It cannot fix WP765's additive
CP-even D-term boundary. Exact extended supersymmetry normalizes the theory at
the price of removing the desired portal; the breaking required to restore it
reopens the coefficient fiber.

A progressive successor needs a D-term-specific exact relation—a conserved
current multiplet, localization identity, or complete UV matching theorem—that
fixes rather than forbids the portal. Its operator, state domain, and physical
instrument must be explicit. Merely citing supersymmetry or holomorphy is not
sufficient.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp766_holomorphy_protects_wrong_operator_class.py

Generated result:
research/flavor/results/wp766_holomorphy_protects_wrong_operator_class.json

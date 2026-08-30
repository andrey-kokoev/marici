# Flavor bounded-control Chebyshev optimum

## Question

Assuming a frozen formal budget \(|Q|,|R|\le B\), which three targets
maximize the symmetric invariant-error radius?

## Claim boundary

The budget is an explicit assumption, not a source-derived physical norm.
The result optimizes formal target placement inside that square and does not
authorize the corresponding actuators.

## Exact optimum

For the commuting and rank-two regions, the targets

\[
(-B,-B),\qquad (B,-B)
\]

have radius \(B\), which is optimal because their sign constraints already
give \(r\le -Q\le B\) and \(r\le Q\le B\).

For the full-rank region, balance its two robust margins:

\[
\frac{R+3087Q}{3088}
=
\frac{R-24696Q}{24697}.
\]

With \(R=B\), this gives

\[
Q=-\frac{7B}{49401},
\qquad
r_{\rm full\text{-}rank}=\frac{B}{5489}.
\]

This is globally optimal. A positive convex combination of the two full-rank
margins cancels \(Q\) and equals \(R/5489\), hence every target in the
budget square satisfies \(r\le R/5489\le B/5489\).

Therefore the joint optimum is

\[
r_*^{\rm opt}(B)=\frac{B}{5489}.
\]

WP994's ray target \((0,B)\) gives only \(B/24697\); it is suboptimal by
the exact factor \(24697/5489\).

## Disposition

A frozen control budget converts WP995's scale ambiguity into a well-posed
conditional optimization and improves the formal controller. It still does not
produce a physical selector. The remaining constructor is a source-derived
control norm and bound \(B\), together with a calibrated closed-loop error
packet expressed in its dual invariant units.

## Verification

- `research/flavor/checkers/wp996_bounded_control_chebyshev_optimum.py`
- `research/flavor/results/wp996_bounded_control_chebyshev_optimum.json`

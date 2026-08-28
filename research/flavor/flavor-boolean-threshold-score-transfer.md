# Boolean threshold-score transfer

Work package: WP932

## Transfer question

Benincasa's finite deletion theorem says that a complete labelled score tower
is a Boolean zeta transform and is inverted exactly by Möbius inversion.  Does
that construction provide flavor with a new source-generated selector?

The candidate flavor labels are the three Spin7 bulk multiplets
\(8_a,8_b,21\).  Their eight formal deletion sectors index coefficients
\(v_S\), and complete scores would obey

\[
M_T=\sum_{S\supseteq T}v_S,
\qquad
v_S=\sum_{T\supseteq S}(-1)^{|T|-|S|}M_T.
\]

## Exact result

For three labels the \(8\times8\) Boolean zeta matrix has determinant one.
Its Möbius matrix is an exact integer inverse, so the complete tower has zero
algebraic kernel on the labelled coefficient packet.

This is identification, not selection.  The transform reconstructs whatever
route values the source already has; it supplies no law choosing those values
and no map to a distinguished `physical16` point.

More importantly, the complete tower is not presently a flavor operation.
WP884 authorizes only a rank-one threshold matching constraint.  Treated as a
single aggregate on eight route coefficients, it leaves a seven-dimensional
kernel.  The declared Spin7 packet does not provide three independently
executable, gauge-consistent multiplet deletion controls or an eight-route
calibrated instrument.

The smallest hostile pair differs by \((1,-1,0,0,0,0,0,0)\).  The authorized
aggregate collapses the pair, while the formal complete score tower separates
it.

## Verdict

Boolean score closure transfers cleanly as a conditional source-story
identifier.  It does not transfer as a flavor selector.  Algebraic
faithfulness on labelled routes cannot be promoted to physical faithfulness
until the deletion operations are source-derived, contact/background sectors
are independently typed, and the resulting scores descend to the chosen
physical quotient.

The next gate is concrete: determine whether the Spin7 bulk action contains
three independent mass controls whose decoupling limits realize the Boolean
routes without breaking the admitted gauge and boundary structure.

## Reproduction

```powershell
uv run --with sympy python research/flavor/checkers/wp932_boolean_threshold_score_transfer.py
```

The generated result is
`research/flavor/results/wp932_boolean_threshold_score_transfer.json`.

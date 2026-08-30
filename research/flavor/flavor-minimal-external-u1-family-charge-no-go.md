# The minimal anomaly-free external U(1) cannot flux a complete SU(6) family: WP779

## Question

Can the external \(U(1)_F\) window left by WP778 assign a common-sign flux
index to \(15+2\overline6\) without new matter or a Green--Schwarz sector?

## Exact charge lattice

Assign charges \(x,y,z\) to \(15,\overline6_1,\overline6_2\). Since
\(T(15)=2\) and \(T(6)=1/2\), the mixed non-Abelian and gravitational
conditions are

\[
4x+y+z=0,
\qquad
15x+6y+6z=0.
\]

Their difference forces

\[
x=0,
\qquad z=-y.
\]

The cubic coefficient \(15x^3+6y^3+6z^3\) then vanishes identically. The
primitive integral charge lattice is only \((0,1,-1)\) and its reverse.

## Flux and tadpole consequences

At flux \(m=3\),

\[
(mx,my,mz)=(0,3,-3).
\]

The \(15\) has no chiral zero modes, while the antifundamentals have opposite
indices and form a vectorlike pair. Requiring the common charge
\(x=y=z=q\) instead forces \(q=0\).

The dimension-weighted linear charge also vanishes. Hence this packet cannot
supply the nonzero oriented source \(Q_{\mathrm{loc}}=-3c\) required by
WP778.

## Classification

The minimal external \(U(1)_F\) is neither a complete-family selector nor a
tadpole selector. It only rigidifies an oppositely oriented vectorlike pair.
A surviving construction must add \(SU(6)\)-charged matter or an independently
derived Green--Schwarz sector, then prove that the enlargement forces the
common-sign charge and signed tadpole rather than accommodating them.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp779_minimal_external_u1_family_charge_no_go.py

Generated result:
research/flavor/results/wp779_minimal_external_u1_family_charge_no_go.json

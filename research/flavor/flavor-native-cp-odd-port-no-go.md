# Native CP-odd port no-go: WP678

## Question

Does the admitted unpolarized two-step cascade itself generate a CP-odd third
port that removes the WP677 conjugation ambiguity?

## Exact obstruction

In the parent rest frame, the three final momenta obey

\[
p_n+p_q+p_X=0.
\]

Consequently the only momentum-only pseudoscalar is identically zero:

\[
p_n\mathbin{\cdot}(p_q\mathbin{\times}p_X)=0.
\]

The native rate and signed chirality moment depend on the relative phase only
through \(\cos\phi\) or not at all. They are invariant under
\(\phi\leftrightarrow-\phi\). The phase kernel found in WP677 therefore
survives every native momentum observable of this unpolarized three-body
record.

## Relational repair

An oriented parent-spin or beam vector would permit a signed pseudoscalar and
a port proportional to

\[
S=D\sqrt{uv}\sin\phi.
\]

Together with the WP677 rate and chirality ports, this response has generic
rank three. But the oriented vector is an added reference port. It defines a
new polarized relational experiment over the stabilizer groupoid of that
reference; it does not recover an absolute phase of the original unpolarized
cascade.

## Disposition

The admitted cascade contains no genuine source-generated CP-odd third port.
The smallest repair is a source-derived polarized production process followed
by a calibrated signed triple-product analysis in the physical pole basis.
Until that constructor and instrument exist, complex source identification is
not authorized.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp678_native_cp_odd_port_no_go.py

Generated result: results/wp678_native_cp_odd_port_no_go.json.

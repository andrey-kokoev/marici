# Oriented quantized-tadpole singleton gate: WP760

## Question

Can quantized boundary data turn WP759's continuous boundary-ratio fiber into
a genuine singleton selector?

## Claim boundary

This is a typed candidate, not an established flavor compactification theorem.
Assume positive integer boundary charges

\[
(n_0,n_\pi)\in\mathbb Z_{>0}^2,
\]

a source-fixed total

\[
n_0+n_\pi=T,
\]

and an independently labelled orientation \(n_0>n_\pi\). The stabilized
boundary ratio is

\[
r=\frac{n_0}{n_\pi}.
\]

The ordered pair is the faithful coordinate. Neither the total alone nor the
unordered endpoint orbit carries the labelled portal sign.

## Exact fiber theorem

For fixed \(T\), the number of positive oriented asymmetric partitions is

\[
N(T)=\left\lfloor\frac{T-1}{2}\right\rfloor.
\]

The fiber is a singleton exactly for \(T=3\) and \(T=4\):

\[
T=3:(n_0,n_\pi)=(2,1),
\qquad
T=4:(n_0,n_\pi)=(3,1).
\]

Composed with WP759, these predict

\[
\Delta_{T=3}=\frac{9}{50},
\qquad
\Delta_{T=4}=\frac{8}{25}.
\]

This is real selection conditional on the source fixing the exceptional total
and the orientation. It is stronger than continuous stabilization.

But finite does not mean singleton. At \(T=5\), the two admissible pairs are

\[
(3,2),
\qquad
(4,1),
\]

with distinct contrasts

\[
\frac{25}{338},
\qquad
\frac{225}{578}.
\]

Quantization by itself therefore discretizes the fiber without generally
selecting a point.

## Disposition

This is the first candidate in the wall branch capable of fixing the portal
ratio rather than merely stabilizing an input-dependent value. Its authority
is sharply conditional: the admitted flavor source does not yet derive a
topological tadpole \(T=3\) or \(T=4\), nor an oriented endpoint labeling.

The integer packet could be RG-stable, but that does not prove threshold
survival of the low-energy portal. Boundary operators, wall and Kaluza–Klein
thresholds, and supersymmetry breaking can add continuous matching terms.
The ordered charge also needs a map to the labelled `physical16` quotient and
a calibrated experimental channel.

The next search is consequently finite and hostile: derive an actual flavor
index or tadpole from the existing representation grammar, test whether it
forces \(T=3\) or \(T=4\), and reject any construction that chooses the total
after seeing the desired contrast.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp760_oriented_quantized_tadpole_singleton_gate.py

Generated result:
research/flavor/results/wp760_oriented_quantized_tadpole_singleton_gate.json

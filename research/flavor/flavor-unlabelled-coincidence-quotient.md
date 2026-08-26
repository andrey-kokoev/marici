# Unlabelled coincidence quotient (WP293)

## Physical groupoid

WP292's complete labelled tower assumes three independently addressable domain
ports. If the source experiment instead identifies domains under the full
$S_3$ permutation groupoid, the faithful state coordinate is the count law

\[
q_r=P(R=r),\qquad r=0,1,2,3,
\]

where $R$ is the number of failed local selectors.

The executable unlabelled order tower is

\[
M_k=\frac{E\binom{R}{k}}{\binom{3}{k}},
\qquad k=0,1,2,3.
\]

Its exact transform from $q_r$ is triangular and invertible. Therefore the
complete order tower is faithful on the four-dimensional count-law quotient.

## Label kernel

It is not faithful on the eight-dimensional labelled packet. The literal laws
concentrated at $(1,0,0)$ and $(0,1,0)$ are different but share the same
count law and every unlabelled coincidence order. The labelled-to-count linear
projection has a four-dimensional kernel.

This is not a defect when $S_3$ permutations are admitted physical
equivalences. If labels are installed as addressable reference ports, the
experiment changes: its groupoid is reduced to the stabilizer of those ports.
The ports create relational observables; they do not reveal pre-existing
absolute domain identities.

## Classification

The unlabelled tower is a faithful risk readout on its declared quotient. It
does not select a flavor point and does not recover labelled source stories.
Any labelled refinement requires a source-derived port family and calibrated
coincidence instrument.

Run `uv run --with sympy python
research/flavor/checkers/wp293_unlabelled_coincidence_quotient.py` to regenerate
the exact quotient and inversion audit.

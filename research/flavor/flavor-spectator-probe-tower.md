# Spectator probe tower (WP395)

## Bounded question

Can a complete family of independently accessible spectator probes remove
WP394's symmetry-extension ambiguity, and would that make the constructor a
source selector?

## Finite extension fiber

Extend one fixed flavor reflection by three labelled spectator parities. The
extension packet is

\[
\sigma=(\sigma_1,\sigma_2,\sigma_3),
\qquad \sigma_i\in\{-1,+1\}.
\]

There are eight distinct extensions with exactly the same flavor restriction.
A central readout such as $\sigma_1+\sigma_2+\sigma_3$ has four classes with
fiber sizes $1,3,3,1$. It is not faithful.

## Complete labelled tower

For every labelled subset $T$, measure the parity character

\[
\chi_T(\sigma)=\prod_{i\in T}\sigma_i.
\]

The resulting response matrix is the order-eight Walsh matrix $H$. Exact
calculation gives

\[
HH^T=8I,
\qquad |\det H|=4096.
\]

Consequently the complete labelled tower reconstructs every extension weight
by

\[
p=\frac18H^TM.
\]

This is the spectator analogue of the finite contextual-faithfulness results
elsewhere in the programme. Context closure is not automatically faithful,
but the complete source-labelled character family is faithful on this finite
packet.

## Deletion and authority

Deleting any one labelled single-spectator probe leaves pairs of extensions
indistinguishable. Aggregate parity or the full three-body product is also
insufficient. The labels and their instruments carry the separating power.

Even the complete tower only identifies which extension is present. It does
not select one extension, derive its probability, or explain why its spectator
signs accompany the flavor reflection. Using observed spectator outcomes to
choose the constructor after the fact would repeat WP393 at a larger scale.

## Disposition

WP395 repairs WP394's finite identification problem conditionally: complete
labelled spectator characters have singleton contextual fibers. It does not
repair the explanatory selector problem. The probe tower must be
source-generated and executable, and the constructor must predict its
spectator record before measurement.

The smallest exact falsifier for incomplete instrumentation is deletion of one
labelled probe, which leaves four two-element fibers.

Run `uv run --with sympy python
research/flavor/checkers/wp395_spectator_probe_tower.py` to regenerate the
result.

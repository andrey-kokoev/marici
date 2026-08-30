# Lookup-selector no-go (WP396)

## Bounded question

Does WP395's complete, faithful spectator probe tower make a simple positive
selector of the observed extension explanatory?

## Universal selector grammar

For every target extension $\tau\in\{-1,+1\}^3$, define

\[
V_\tau(\sigma)=\frac12\sum_{i=1}^3(1-\tau_i\sigma_i).
\]

This is the Hamming distance between the observed extension $\sigma$ and the
chosen target $\tau$. It is nonnegative and has the unique zero
$\sigma=\tau$.

All eight selectors have the same coefficient norm and the same energy
spectrum,

\[
0,1,1,1,2,2,2,3.
\]

Sign relabellings act transitively on them. Positivity, uniqueness, polynomial
degree, coefficient norm, and spectrum therefore fail to privilege any one
target.

## Faithfulness does not help selection

The complete Walsh tower reconstructs the observed extension exactly. But
after reconstruction, the rule

\[
\tau\longmapsto V_\tau
\]

manufactures an equally simple selector for whatever record was observed.
Perfect identification makes the post-hoc lookup easier; it does not provide
source authority.

The hostile pair $\tau=(1,-1,1)$ and $\tau'=(-1,1,-1)$ is fully separated by
the probe tower. Each is nevertheless the unique minimum of its own isomorphic
positive potential, and each potential maximally rejects the other target.

## Deutschian diagnosis

An explanation must be hard to vary because its selector coefficients follow
from an independently constrained constructor. Syntactic simplicity within a
transitive family is insufficient. A finite faithful record can always be
inserted into a lookup potential of this kind.

The selector coefficients must therefore be computed from source data frozen
before the record, and the same computation must entail at least one outcome
not used to define those coefficients. Otherwise the constructor is only a
compressed encoding of the observation.

## Disposition

WP396 separates three notions exactly: the Walsh tower identifies the state;
the Hamming potential selects a state; neither explains why its target is the
physical one. Every target has an equally simple selector.

The smallest falsifier is the isomorphic hostile pair above. The remaining
gate is a non-transitive source grammar whose independently fixed data choose
one coefficient packet and generate a novel spectator or threshold
prediction.

Run `uv run --with sympy python
research/flavor/checkers/wp396_lookup_selector_no_go.py` to regenerate the
result.

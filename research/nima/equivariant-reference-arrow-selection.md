# Can the direct reference select two local arrows?

## Selection criterion

For a reference datum d and local-arrow output set O, a relabelling-equivariant
selection must choose an output fixed by every automorphism stabilizing d.
On a transitive reference-data orbit this condition is also sufficient: choose
a stabilizer-fixed output and extend by relabelling. The checker enumerates
stabilizers and fixed ordered arrow pairs for two four-element carriers.

## Bare four-element carriers

| Reference data | Stabilizer | Fixed local-arrow pairs |
|---|---:|---:|
| Cross-carrier edge selecting one point on each side | S3 x S3, size36 | 0 |
| Carrier bijection, no marked point | diagonal S4, size24 | 0 |
| Rooted carrier bijection | diagonal S3, size6 | 0 |
| Two ordered endpoint anchors per carrier | S2 x S2, size4 | 4 |

A rooted bare carrier has no distinguished second point: its three other
points are interchangeable. Thus a single cross-carrier endpoint reference
cannot select an ordered nonidentity local arrow equivariantly. A correspondence
between carriers, even with a root, leaves the same obstruction.

Two distinct ordered anchors on each side leave four arrow-pair choices, from
the two orientations in each carrier. Requiring each arrow to start at its
first anchor makes the output unique. A rooted bijection plus one additional
source anchor can transport the extra anchor to the other carrier.

These statements concern the declared reference types and their symmetries.
A map with additional numeric or geometric data can have a smaller stabilizer.

## The retained Bool x Bool structure changes the answer

The existing state description explicitly uses Bool x Bool. If this retains
the square's Hamming adjacency, rather than just naming four labels, its
relabellings form the square automorphism group D8 (eight elements).

Fixing a root leaves the root and its opposite vertex fixed; the two adjacent
vertices are exchanged. Therefore the rule

    selected arrow = root -> antipode(root)

is equivariant and unique among arrows starting at the root. In binary labels,
antipode(a)=a xor 3. It leaves exactly11 of the12 directed nonidentity arrows
on each carrier eligible for comparison. The checker verifies the rule under
all square automorphisms and all endpoint roots.

Selecting one of the two adjacent arrows still needs an axis choice. If the
Boolean factors are individually named and must be preserved, that naming is
additional structure and offers further selection rules. The tested uniqueness
uses coordinate exchange as an allowed symmetry and requires root-to-other
orientation.

The earlier arbitrary mark(0,1) is square-adjacent under the usual binary
encoding, whereas(0,3) is antipodal. They are equivalent under bare-set S4
relabelling, but not under square automorphisms. Applying the square selection
rule therefore requires preserving or explicitly transporting the Boolean
structure together with labels.

## What the audit establishes

The local-arrow adapter depends on the retained carrier type:

- Four-element sets with a direct endpoint reference: no equivariant selection.
- Rooted Boolean squares with exchangeable axes: the outward antipodal arrow
  supplies a unique selection and the11-leg complement.

The subsequent [carrier-symmetry source audit](reference-choice-family-under-carrier-symmetry.md)
finds an explicit S4 finite-set definition with no retained coordinates or metric.
Thus the square selector requires additional carrier structure. Under the
declared symmetry, the admissible outward selectors form a nine-context family
once roots are supplied. The direct matrix map d:A->B also needs a carrier
interpretation before it supplies a state-pair datum.

At recursive levels the selection must be transported alongside the state
product structure. Excluding the one newly selected composite arrow and
propagating every earlier factorwise exclusion are distinct policies; the
current test establishes the local selector, not that recursive masking rule.

## Verification

    python research/nima/checkers/check_reference_arrow_selection.py

Exact permutation enumeration, fixed-output and orbit counts, exhaustive
ordered-anchor equivariance, a label-order negative control, and exhaustive
root-to-antipode equivariance under square symmetries. No numeric tie-breaker,
carrier metric fit or reference value is used to select the arrows.

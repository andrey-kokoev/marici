# Retain the reference-choice family under the declared carrier symmetry

## Source resolves the square-structure question

The carrier definition in docs/theory-page.md, section1, states:

> The carrier is a finite set with no metric, no coordinates, no topology.
> The only structure is the cardinality N and the automorphism group S_N.

The same section calls Bool x Bool the canonical four-label choice. Under this
explicit definition the labels do not retain square adjacency. The antipodal
selector from the preceding audit is available only after adding structure
and reducing the allowed relabellings. It is not selected by the declared
carrier. Swapping labels1 and3 while fixing0 takes the proposed antipodal
arrow(0,3) to(0,1), demonstrating failure under an allowed S4 relabelling.

## What a reference can index

Even granting the direct reference one root in each carrier, its stabilizer is
S3 x S3. Under an explicit outward-local-arrow convention, there are three
choices of second endpoint on each side, hence nine possible local reference
contexts. Each context selects one local arrow per carrier and has
11^2+4^2=137 counted slots.

The stabilizer acts transitively on those nine contexts and fixes none. A
specific context is extra data; selecting it reduces the stabilizer from36
to4, the S2 x S2 symmetry used by the earlier137-slot reference audit.

The nine-context count assumes outward arrows from the supplied roots.
Different orientation/incidence conventions require their own context domain.
The direct matrix map d:A->B still requires an adapter to supply state roots.

## Equivariant family in place of an arbitrary selection

Retain all admissible contexts with their slot memberships. Independent carrier
relabelling transports the whole family and each context's mask exactly. The
checker verifies this under all24^2=576 relabellings, including root movement.

There are9*137=1233 context-tagged records. Forgetting the context leaves160
possible underlying slots:144 arrow pairs and16 state pairs. Arrow pairs with
both legs starting at the respective roots occur in four contexts; pairs with
one such leg occur in six; the others occur in all nine. State pairs occur in
all nine.

| Multiplicity | Underlying slots |
|---:|---:|
| 4 | 9 |
| 6 | 54 |
| 9 | 97 |

The slot count137 is thus well-defined in every fibre even though no preferred
fibre has been selected. Fresh labels and retained membership can expose this
family using the existing record architecture.

## Optional measure, separate from the construction

Uniform averaging over nine contexts, with uniform137-slot weights within each,
gives each underlying slot its multiplicity divided by9*137. The arrow and state
block masses remain121/137 and16/137. Underlying slot weights are unequal.
This is an explicitly tested measure choice; retaining the family does not
require averaging or interpreting these weights as a coupling.

## Structural consequence and remaining choice

The declared symmetry rules out the proposed canonical single-arrow adapter.
It admits an equivariant family of adapters. Choosing a context, providing a
witness that chooses it, or retaining the full dependent family are distinct
architectural operations.

The next comparison should keep context identity and ask whether readouts and
return actions descend across relabellings between contexts. If an observable
is context-independent, it can be evaluated without a preferred local-arrow
selection. If it varies, its reference context belongs in the physical input.
This tests the need for a chosen reference rather than adding an undeclared
Boolean geometry to manufacture one.

## Verification

    python research/nima/checkers/check_reference_choice_family.py

Exact context counts, transitive stabilizer action with no fixed context,
576 relabelling covariance checks, context-tagged versus underlying slot counts,
exact weighted marginalization, stabilizer reduction and an S4 antipode
negative control. The existing bare-carrier definition is unchanged.

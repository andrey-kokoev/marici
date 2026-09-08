# v13: concrete 199-state endpoint-relative coefficient complex

**Superseded interface status:** see
[`rzk-coefficient-interface-v14.md`](rzk-coefficient-interface-v14.md). The
coefficient complexes and comparison maps are now packaged as checked
congruence-preserving setoid morphisms with composition.

This checkpoint closes the endpoint-quotient packaging gate without assuming a
quotient higher inductive type or identifying evaluation-setoid equality with
Rzk identity.

## New checked modules

- `rzk/22-endpoint-relative-cech-complex.rzk.md`
  defines a fresh 199-constructor cell datatype, retaining exactly the loaded
  cells outside the two complete eight-state endpoint packets. Its dependent
  coefficient stalk at each cell is the same legal Laurent stalk as in the
  full 215-state Cech complex. The differential contains precisely the arrows
  whose targets remain in the quotient.
- `rzk/23-endpoint-relative-cech-square.rzk.md` proves square-zero on all 199
  generator columns and extends it to every finite integral coefficient
  expression using the module-18 column-square theorem.
- `rzk/24-endpoint-quotient-projection.rzk.md` defines the explicit projection
  from the 215-state Cech presentation: endpoint atoms map to zero and retained
  atoms map to their corresponding 199-state atoms. It proves the projection
  commutes with the two concrete differentials, first on every loaded basis
  element and then on arbitrary finite integral coefficient expressions.

Fresh headless transitive closure checks passed; the Rzk LSP was not used:

- module 22: passed (bounded 900-second process);
- module 23: passed in 693.08 seconds;
- module 24: passed in 178.35 seconds.

Evidence is in the corresponding `results/*.closure.json`,
`results/*.typecheck.json`, and bounded stdout/stderr logs.

## Status of the coefficient foundation

The following are now concrete Rzk theorems rather than external matrix checks:

1. full 215-state finite and Cech coefficient carriers;
2. legal stalk-dependent normal inverses;
3. both full square-zero laws;
4. the full finite-to-Cech chain law;
5. a literal 199-state endpoint-relative carrier and differential;
6. its square-zero law;
7. the explicit 215-to-199 quotient projection and chain law.

Equality remains the evaluation relation on finite integral sums. This is an
intentional setoid-native coefficient model. The next bridge should therefore
package setoid morphisms and setoid Hom complexes directly; it must not claim
that the relation is an identity type without a quotient construction.

Still outside this checkpoint are the K-projective localization theorem and the
normalization/Gysin physical left leg.

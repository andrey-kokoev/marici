# v14: setoid-native coefficient morphisms

**Next checkpoint:** [`rzk-coefficient-interface-v15.md`](rzk-coefficient-interface-v15.md)
constructs and checks the 16-state supported local `Z[u,s,t]` receiving
complex and its chain-level Bockstein relation.

The representation bridge is now explicit without making the false assertion
that evaluation equality is Rzk identity.

`rzk/25-setoid-coefficient-interface.rzk.md` defines:

- a setoid morphism as a function paired with a congruence proof;
- identity and composition;
- pointwise setoid equality of morphisms;
- the generic finite-sum linear extension as a setoid morphism;
- the full finite differential, full Cech differential, and 199-state relative
  differential as concrete setoid endomorphisms;
- Lambda and the 215-to-199 endpoint projection as concrete setoid morphisms.

The module passed a fresh 74-file headless transitive closure check in 183.43
seconds. Evidence: `results/25-setoid-coefficient-interface.typecheck.json`.
The Rzk LSP was not used.

Square-zero and chain-map compatibility remain the already checked theorems of
modules 20, 21, 23, and 24. Module 25 packages the same underlying functions
with congruence proofs, so downstream work can consume them in the
setoid-native category rather than coercing them to identity-based functions.
The large proof modules remain separately certified to avoid a single closure
whose repeated normalization exceeded 2400 seconds; no timeout is counted as a
success.

## Foundation status

The concrete coefficient foundation is complete at the setoid-complex level:

1. legal finite and Laurent carriers;
2. complete differentials and square-zero proofs;
3. coherent integer indexing;
4. finite-to-Cech comparison and chain law;
5. literal endpoint-relative complex, quotient projection, and chain law;
6. congruence-preserving morphism packaging and composition.

The next objective is no longer a coefficient-foundation task. It is the
semantic realization layer: construct a completion/localization functor from
these setoid complexes to the intended identity-based or derived category,
prove the finite free sources are K-projective there, and then instantiate the
normalization/Gysin comparison. No derived-Hom equivalence is claimed here.

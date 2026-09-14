# v96: physical amplitude model equivalence

`rzk/124-physical-amplitude-model-equivalence.rzk.md` strengthens the pointwise
bridge to an explicit equivalence criterion. A physical supported model can be
identified with the coefficient amplitude fixture only by supplying encode and
decode maps, both inverse laws, and compatibility of supported residue with the
calibrated coordinate formula.

Every such equivalence canonically induces the physical/coefficient amplitude
bridge. The coefficient fixture has a self-equivalence whose induced bridge is
judgmentally the canonical bridge, providing an end-to-end normalization test.

This prevents Voevodsky's ordinary source equivalence from being misused as an
amplitude theorem: source equivalence alone does not supply the supported
residue coordinate law.

The transitive closure contains ten files. A fresh combined Rzk check passes all
166 declarations (178 checker steps including parameter/assumption commands).
The target module adds no `#assume` declarations.

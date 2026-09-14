# v97: supported residue coordinate factorization

`rzk/125-supported-residue-coordinate-factorization.rzk.md` removes an
unnecessarily strong requirement introduced at v96. Full equivalence of the
physical supported object with the three-coordinate fixture is not needed for
amplitudes.

The minimal sufficient datum is a map from supported classes to `(a,b,c)` plus
the pointwise residue law `residue(s) = - beta (a + (b + c))`. Composing these
coordinates with the physical Gysin map canonically constructs the physical
amplitude bridge. No decoder or inverse laws are required.

The coefficient model inhabits this weaker factorization, and its induced
bridge is judgmentally the canonical coefficient bridge.

The transitive closure contains ten files. A fresh combined Rzk check passes all
167 declarations (179 checker steps including parameter/assumption commands).
The target module adds no `#assume` declarations.

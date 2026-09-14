# v95: inhabited coefficient amplitude model

`rzk/123-coefficient-amplitude-model-inhabitant.rzk.md` supplies an actual
inhabitant of the pointwise amplitude bridge for the exact three-coordinate
coefficient model.

The model uses the identity Gysin map on `(a,b,c)` and defines residue by
`- beta (a + (b + c))`. Its bridge proof and evaluation theorem are
judgmental equalities. A general constructor also shows that any physical
coordinate map satisfying this pointwise law produces the required bridge.

This fixture demonstrates that the Rzk bridge and amplitude definitions are
jointly inhabitable and normalized. It does not identify the fixture with the
physical supported object; the physical bridge remains open.

The transitive closure contains nine files. A fresh combined Rzk check passes
all 157 declarations (169 checker steps including parameter/assumption
commands). The target module adds no `#assume` declarations.

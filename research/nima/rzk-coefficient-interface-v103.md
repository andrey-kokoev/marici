# v103: complete relative physical-amplitude witness type

`rzk/131-physical-amplitude-witness.rzk.md` combines the two decisive pieces
into one dependent type: a simultaneous five-direction physical lift and a
three-detector supported residue law.

An inhabitant contains one physical point satisfying endpoint, Cech,
normal-cube, group, and operation-bar comparison equations, together with
primary, reciprocal, and relation detectors whose residue is
`- beta (a + (b + c))`. The module extracts the physical point, evaluates its
supported amplitude, and proves that value equals the calibrated formula.

This is now the exact Rzk target for concrete amplitude existence. The current
coefficient/native-bar candidate supplies only a proper subset of its fields;
no physical inhabitant is claimed.

The transitive closure contains thirteen files. A fresh combined Rzk check
passes all 193 declarations (205 checker steps including parameter/assumption
commands). The target module adds no `#assume` declarations.

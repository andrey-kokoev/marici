# Testing a common projector field for T

The prior native sources already obey one protocol law:

```
L and G are commuting metric-orthogonal projectors
return operator = G L = L G
defect operator H = 2I-L-G
```

Here L/G are local/alignment operators; neither is automatically identified with
configuration M/C or realization coordinates. The return operator's historical
symbol N must not be confused with neutron species N.

This test recomputes that law from the exact source matrices and examines the
four simultaneous projector sectors. Their dimensions are:

| Species | Both L,G | L only | G only | Neither | Total |
|---|---:|---:|---:|---:|---:|
| P | 1 | 11 | 2 | 22 | 36 |
| N | 1 | 2 | 11 | 22 | 36 |
| E | 2 | 2 | 0 | 4 | 8 |

## Proton/neutron result

P and N exchange the L-only and G-only sectors exactly. Both have return rank
1 and defect spectrum 0^1,1^13,2^22. The finite-dimensional joint spectral
theorem therefore supplies a metric-unitary equivalence between their projector
pairs after exchanging L/G. This is stronger than matching the numbers 12/3.

No source-geometric preferred intertwiner was constructed. Choosing matching
orthonormal bases in each joint sector supplies many possible intertwiners;
geometry, marked histories and native operator dictionaries could constrain
them further.

## Electron obstruction and minimal enlargement

The electron's common image has dimension 2. It cannot be a reducing-subspace
restriction of a single native P or N field, whose common image has dimension
1. Relabelling coordinates or choosing an invertible basis cannot remove this
obstruction under that particular restriction hypothesis.

Two copies of the P field have capacities (2,22,4,44), sufficient to contain an
E pair with sector dimensions (2,2,0,4). Two is the minimum number of identical
baryon copies for such a multiplicity embedding. This is an existence/counting
result, not a reason to select that common field as T.

In particular one must choose 2 directions from a 22-dimensional L-only sector
and 4 from a 44-dimensional neither sector. The projector pair alone cannot
canonically make those choices: its internal unitary symmetries act within
each degenerate sector. Additional geometric/boundary structure must select
the electron field. An arbitrary chosen subspace would fit rather than derive
its native matrices.

## Consequence for T

There is a common projector protocol, and the P/N pair has the exact exchange
structure expected of two presentations. A common parent that also realizes E
as an invariant restriction must have at least a two-dimensional shared image.
The simplest identification of that parent with the existing 36-dimensional
baryon field fails. This does not rule out other kinds of section/pullback maps
or a larger common field on the glued simplex.

The outstanding construction is a source-defined geometric field and restriction
maps producing L and G, including their metrics and marked readouts. The
universal algebraic formula is already known; the new T geometry has not yet
derived its native inputs. Production/viewer unchanged.

```sh
python research/strominger/checkers/check_T_projector_field.py
```

Evidence: `results/T-projector-field/verification.json`.

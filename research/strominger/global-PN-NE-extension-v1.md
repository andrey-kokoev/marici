# Extending the boundary map: global PN and NE constraints

## PN cannot remain confined to the six-component face

The normalized P return places 1/4 of its norm in the chosen incoming face's
six tangential components. The normalized native N return places 1/6 in its
corresponding face. These values were recomputed as exact projector traces:

```
tr(F_P N_P)=1/4
tr(F_N N_N)=1/6.
```

F_P and F_N are the metric-orthogonal projections onto the actual six-component
face subspaces. If a metric-unitary global S mapped one such face subspace
onto the other and intertwined the full return projectors, those traces would
have to agree. They do not.

Therefore the previously constructed conditional face unitary cannot remain a
closed block of a globally return-preserving PN unitary. The global connection
must mix face and complementary components, or abandon one of those properties.
The 1/12 difference is in the fraction of the normalized full return norm, not
a newly measured energy or a claim about a unique physical flow direction.

The native local/alignment compressions give an additional obstruction:

| Restricted operator rank | P face | N face |
|---|---:|---:|
| L | 3 | 1 |
| G | 2 | 6 |
| Return | 1 | 1 |

Even exchanging L/G does not match these restricted ranks. Routing only the
three discarded ambient normal components elsewhere would not solve the
face-supported intertwining requirement.

## NE cannot be a surjective return-preserving map from one native N field

The native raw spaces have dimensions 36 and 8, and their return ranks are
1 and 2 respectively. For a complex-linear S obeying

```
S N_N = N_E S,
```

the return-image block has rank at most 1 and the complementary block at most
6. Thus `rank(S)<=7`, with kernel dimension at least 29. Such a map cannot
reach all eight E coordinates or both independent E return directions.

To populate the full E return image while retaining exact linear return
intertwining requires another independent incoming return channel. Alternatively,
the interaction must not preserve these particular return projectors. Neither
option is supplied automatically by a relabelling or a frame change, since
projector rank is invariant under invertible coordinate changes.

## What remains valid

The six-component PN boundary map still correctly transports the **normalized
conditional face modes**. The new test explains why it does not by itself
extend to the requested whole-field connection. Abstract full P/N projector
pair equivalence also remains valid when spatial face support is not required.

These are conditional extension obstructions, not claims that actual physical
PN/NE transfers must be unitary, surjective, face-supported or projector
intertwiners. The native five-coefficient permutation rules are untouched.
A complete source-derived 36-component PN/NE field connection has not been
constructed.

```sh
python research/strominger/checkers/check_global_PN_NE_extension.py
```

Evidence: `results/global-PN-NE-extension/verification.json`.
Production/viewer unchanged.

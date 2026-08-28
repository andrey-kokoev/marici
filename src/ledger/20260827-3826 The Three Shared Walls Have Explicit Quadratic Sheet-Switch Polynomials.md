# 3826 — The Three Shared Walls Have Explicit Quadratic Sheet-Switch Polynomials

> **Prior-art correction.** Entry 594 already proved that all three shared
> wall restrictions are exact squares and used their conductor resultants.
> The increment here is narrower: it exports the explicit quadratic roots,
> discriminants, and sample switch points needed for literal segment
> selection. It is an independent replication, not the first square-root
> theorem.

## Construction

On each of the three source-face marks, the residue-surface equation restricts
to an exact square:

```text
K|g_i = R_i^2,  i=1,2,3.
```

With `a=y23`, `b=y31`, the source-fixed roots are

```text
R1 = -x a^2 + x^2 y + x^2 z + x y^2 + 2xyz + 2xz^2
     - y^3 - y^2z + yz^2 + z^3,

R2 = y b^2 + x^3 - x^2y + x^2z - xy^2 - 2xyz - xz^2
     - y^2z - 2yz^2 - z^3,

R3 = -z a^2 + a x^2 - a y^2 - a z^2 + x^2z + 2xyz
     + 2xz^2 + 2yz^2 + z^3.
```

Each is quadratic in its wall coordinate. The positive source sheet obeys

```text
W = |R_i|.
```

Therefore its component label can switch only at the two roots of `R_i`.

At `(x,y,z)=(2,3,4)` the three polynomials are

```text
R1 = 207-2a^2,
R2 = 3(b^2-94),
R3 = -4a^2-21a+288.
```

Their six exact roots are exported in the result packet.

## Narrow conclusion

The boundary-sheet ambiguity is now reduced to a finite labelled set of six
switch sections. No additional wall or carrier component is required. Away
from these roots, each physical wall segment lies on one fixed component of
the split double cover.

This does not yet select which analytically continued segments occur in the
source relative chain. That selection must be transported from the original
signed-minor chamber. The quadratic roots merely make the required transport
finite and explicit.

## Artifacts

- `research/benincasa/checkers/check_rank26_shared_wall_sheet_switch_polynomials.py`
- `research/benincasa/results/rank26-shared-wall-sheet-switch-polynomials.json`

Allocator claim: `seqclaim-01c1192ca4dbbc459e73641a`.

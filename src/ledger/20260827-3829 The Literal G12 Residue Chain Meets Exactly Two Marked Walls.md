# 3829 — The Literal G12 Residue Chain Meets Exactly Two Marked Walls

## Source geometry

The exact tetrahedral Cayley–Menger matrix has loop-to-vertex lengths
`(a,b,c)` and opposite external edges `(x,y,z)`. Its determinant is `-2K`.
After the ordered `q_G12` residue, the measure depends on `c^2=E^2`, so the
literal Euclidean chamber uses the positive length

```text
c=E=x+y+z.
```

Assume strict positive external-triangle kinematics:

```text
x,y,z>0,
x<y+z, y<x+z, z<x+y.
```

## Wall incidence

The signed-minor inequalities give exactly two nonempty marked-wall segments:

```text
g1: b=y+z,  x+z <= a <= y+2z,
g2: a=x+z,  y+z <= b <= x+2z.
```

The other three marks have no literal real incidence:

```text
g3:  a+b+z=0             has no positive solution,
g23: b=x                  would require x>=y+z,
g31: a=y                  would require y>=x+z.
```

## Sheet sequence

On the `g1` interval, `R1` is strictly decreasing. Its endpoint values factor
with opposite signs under the strict triangle inequalities, so it has exactly
one switch:

```text
D_plus -> D_minus,
```

with residue orientation `-da`.

On the `g2` interval, `R2` is strictly increasing and likewise has exactly one
switch:

```text
D_minus -> D_plus,
```

with residue orientation `+db`.

At `(x,y,z)=(2,3,4)`, the switch points are

```text
a=3 sqrt(46)/2,
b=sqrt(94).
```

## Narrow conclusion

The literal real residue-chain incidence is now completely selected: two
oriented intervals, each split once. The algebraic five-wall Čech cocycle of
Entry 3824 remains necessary for coefficient descent, but only its `g1` and
`g2` walls meet the literal real chain.

This does not assign winding to the three nonincident pole walls under a
further complex continuation. Such winding is a separate relative-homology
datum and cannot be inferred from algebraic wall residues.

## Artifacts

- `research/benincasa/checkers/check_rank26_literal_residue_chain_wall_segments.py`
- `research/benincasa/results/rank26-literal-residue-chain-wall-segments.json`

Allocator claim: `seqclaim-6de630cc2f458a3a5520ab8a`.

# 3819 — The Five-Wall Leray Residues Have a Canonical Oriented Corner Packet

## Frozen convention

Use the residue chart coordinates

```text
a = y23,  b = y31
```

with ambient orientation `da wedge db` and Poincaré convention

```text
dq_i wedge Res_i(Omega) = Omega.
```

The five source marks are

```text
g1  : b-y-z
g2  : a-x-z
g3  : a+b+z
g23 : b-x
g31 : a-y.
```

## Wall maps

The source-oriented simple residues of `da wedge db / q_i` are

```text
Res_g1  = -da
Res_g2  =  db
Res_g3  =  db
Res_g23 = -da
Res_g31 =  db.
```

Each identity reconstructs the ambient orientation exactly when wedged on the
left with its labelled `dq_i`.

## Corner maps

Two pairs are parallel and have no finite corner:

```text
(g1,g23), (g2,g31).
```

Every other pair has affine Jacobian `+1` or `-1`. Therefore all eight finite
iterated residues are integral units. Reversing the residue order changes the
sign exactly:

```text
Res_j Res_i = - Res_i Res_j.
```

The machine-readable packet records every labelled intersection point,
Jacobian, ordered residue coefficient, and the signed wall-to-corner Čech
incidence.

## Narrow conclusion

The local wall and corner maps required by Entry 3816 are now fixed without a
period fit, basis projector, or normalization choice. No denominator or
fractional index appears in the incidence layer: all corner transition units
are `+1` or `-1`.

What remains is physical activation. These residue maps specify how a form
restricts when a labelled wall or corner is used; they do not prove that the
source relative cycle has nonzero incidence with every such support. The next
gate must transport the published negative-imaginary prescription to the five
wall tubes and determine its winding/linking vector before applying these
maps.

## Artifacts

- `research/benincasa/checkers/check_rank26_five_wall_corner_residue_packet.py`
- `research/benincasa/results/rank26-five-wall-corner-residue-packet.json`

Allocator claim: `seqclaim-4be4aaffa03b7378c0860596`.

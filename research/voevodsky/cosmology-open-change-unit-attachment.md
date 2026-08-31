# Unit attachment gate for open-changing source geometry

## Theorem

Model an added face by an integral chain map from one degree-two generator to the primitive boundary cycle:

`Z --m--> Z`.

After attachment, first homology is `Z/mZ`, with `m=0` interpreted as `Z`. The primitive class is killed integrally exactly when `m=+1` or `m=-1`.

Consequently a finite boundary cover, root construction, or ramified attachment of degree greater than one does not supply the horn filler. It replaces the free obstruction by nonzero torsion. This is insufficient for the required primitive integral column.

## Disposition

The open-change attachment leaf is completed. Any admissible enlargement must contain an oriented unit-degree face. The remaining problem is provenance: derive that face from an actual source incidence correspondence and construct its chain map to the resolved/logarithmic carrier. Without those data, the unit face is exactly the abstract `tau_p` cell under another name.

The theorem classifies a one-face attachment. A multi-cell complex could kill the primitive class only if the gcd of its attaching degrees is one; that extension is the next algebraic gate before testing candidate geometries.

## Verification

- `research/voevodsky/check_cosmology_open_change_unit_attachment.py`
- `research/voevodsky/results/cosmology_open_change_unit_attachment.json`

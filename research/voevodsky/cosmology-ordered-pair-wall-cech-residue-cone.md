# Ordered pair-wall Čech residue cone for the denominator obstruction

## Question

Can the residue vector obstruction be canceled by the smallest source-derived ordered pair-wall Čech module?

## Claim boundary

This packet constructs only a residue-level relative cone from the ordered wall nerve. It does not construct a chain map into the full logarithmic denominator complex, a logarithmic one-form primitive, resolved/Rees compatibility, Cayley--Menger face compatibility, a global contour, or a physical period.

## Disposition

Use the ordered vertices

\[
q_1,
\quad q_2,
\quad q_3
\]

and ordered pair faces

\[
q_1q_2,
\quad q_1q_3,
\quad q_2q_3.
\]

For the oriented Čech simplex

\[
\sigma_{123}=[q_1,q_2,q_3],
\]

its boundary in the pair-face basis is

\[
\partial\sigma_{123}=(1,-1,1).
\]

The edge-to-vertex boundary and face-to-edge boundary compose to zero. Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), the face-to-edge rank is \(1\), the edge-to-vertex rank is \(2\), and the composite rank is \(0\).

The denominator residue vector from the previous packet is also

\[
(1,-1,1).
\]

Therefore the opposite orientation \(-\sigma_{123}\) supplies the required canceling boundary

\[
(-1,1,-1),
\]

and the residue sum is zero over both finite fields.

This identifies the minimal possible relative cancellation object: the oppositely oriented ordered Čech 2-simplex. It is not a circuit quotient, because it adds a face boundary rather than setting the circuit row to zero in the denominator carrier.

The remaining blocker is now sharper. One must construct a source-derived chain map from this Čech residue cone into the full logarithmic denominator carrier or a resolved/Rees carrier. Without that map, the residue cancellation does not yet produce a one-form primitive \(H_p^{\log}\) or a relative Bockstein class.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_ordered_pair_wall_cech_residue_cone.py`

Result:

- `research/voevodsky/results/cosmology_ordered_pair_wall_cech_residue_cone.json`

Command:

- `python research/voevodsky/check_cosmology_ordered_pair_wall_cech_residue_cone.py`

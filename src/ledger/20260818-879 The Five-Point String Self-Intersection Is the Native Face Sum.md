# 879 — The Five-Point String Self-Intersection Is the Native Face Sum

## Record

Date: 2026-08-18

Status: exact finite five-point calibration against the primary string twisted-cycle result. This entry opens the `/string` sector independently of the scalar-derived finite-\(\alpha'\) regulator line. It does not claim an all-arity theorem or a string completion of the scalar occurrence complex.

## Frozen source object

Use the identity twisted cycle in the blown-up real moduli space

\[
\widetilde{\mathsf C}(12345)\subset \widetilde{\mathcal M}_{0,5}(\mathbb R)
\]

with its rank-one Koba--Nielsen loading. Mizera's primary calculation, arXiv:1706.08527, Section 4.3, equation (4.15), expresses its self-intersection as contributions from the whole pentagon, its five facets, and its five vertices.

Write

\[
q_E=e^{2\pi i\alpha' s_E},
\qquad
h_E=(q_E-1)^{-1}.
\]

The five source facets are

\[
(12),(23),(34),(45),(51).
\]

Their compatible pairs are

\[
((12),(34)),\quad
((12),(45)),\quad
((23),(45)),\quad
((23),(51)),\quad
((34),(51)).
\]

No scalar occurrence coefficient is imported.

## Native face calculation

The generalized-Pochhammer normal-torus calculus assigns:

- \(1\) to the open two-cell;
- \(h_E\) to a boundary facet \(E\);
- \(h_Eh_F\) to a compatible codimension-two face \(E\cap F\).

Therefore the native face sum is

\[
\boxed{
1+
\sum_E h_E+
\sum_{E\sim F}h_Eh_F.
}
\]

The exact face census is

\[
1+5+5=11,
\]

and the five quadratic terms are exactly those printed in source equation (4.15). Thus

\[
\boxed{
\langle\widetilde{\mathsf C}(12345),
\widetilde{\mathsf C}(12345)\rangle
=
1+
\sum_E\frac1{q_E-1}
+
\sum_{E\sim F}\frac1{(q_E-1)(q_F-1)}.
}
\]

At every vertex the coefficient product is symmetric, while the ordered normal contractions obey

\[
\iota_E\iota_F=-\iota_F\iota_E.
\]

Hence the string coefficient pairing and the Marici Cut/Gysin normal orientation use the same local sign calculus without identifying their coefficient objects.

## Narrow conclusion

Established at five-point self-intersection level:

\[
\boxed{
\text{associahedral carrier}
+
\text{normal Koszul/Gysin calculus}
+
\text{Koba--Nielsen coefficients}
}
\]

reproduces the primary finite-\(\alpha'\) twisted-cycle result. No new carrier cell is required.

This supports the sector architecture

\[
\text{shared carrier and support calculus}
+
\text{string-specific twisted coefficients}.
\]

It does **not** establish:

- the off-diagonal five-point intersection matrix;
- a relation to the scalar occurrence coefficients;
- the missing alternating-conductor BRST chain lift of Entries 89--93;
- an all-arity KLT theorem inside Marici.

## Next falsifier

Freeze the two-dimensional twisted-cycle basis and reconstruct an off-diagonal five-point entry from shared-face incidence, induced boundary orientation, and Koba--Nielsen half-monodromy. The sharp representative is

\[
\langle\widetilde{\mathsf C}(12345),
\widetilde{\mathsf C}(13245)\rangle.
\]

The source result contains the factor

\[
-\left(\frac{i}{2}\right)^2
\frac1{\sin(\pi s_{23})}
\left(
\frac1{\tan(\pi s_{45})}
+
\frac1{\tan(\pi s_{51})}
\right).
\]

Derive its minus sign, half-monodromy, and four-point boundary self-intersection independently. Failure would show that shared normal-torus cells do not by themselves determine the string intersection pairing.

## Certificate

Run:

```text
cargo run --quiet --bin string_five_point_face_intersection
```

from `research/benincasa/marici-gm`.

Artifacts:

- `research/benincasa/marici-gm/src/bin/string_five_point_face_intersection.rs`
- `research/benincasa/string-five-point-face-intersection.json`

## Dependencies

- Entry 38: finite-\(\alpha'\) normal-torus and facewise Pochhammer/Cousin calculus, with its explicit warning that the scalar-derived construction is not a string completion.
- Sebastian Mizera, *Combinatorics and Topology of Kawai--Lewellen--Tye Relations*, arXiv:1706.08527, Section 4.3, equation (4.15).

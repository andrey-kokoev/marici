# 2780 — The Marked-Pole Multiplication Relations Have a Canonical First Syzygy Differential

## Source relation map

For marked denominator occurrence (i), let

\[
R_i(\ell,e)
=
E_{\ell,e}-q_iE_{\ell+e_i,e}
\]

denote the labelled multiplication relation at pole-depth label \(\ell\) and numerator monomial \(e\).

For every pair of distinct occurrences (i,j), multiplication commutativity gives the square

\[
R_i(\ell,e)
+q_iR_j(\ell+e_i,e)
-R_j(\ell,e)
-q_jR_i(\ell+e_j,e)
=0.
\]

This formula retains the occurrence labels and both routes through the pole-depth cube.

## Complete ambient-14 audit

The raw identity is checked for:

- all ten unordered pairs among five marked occurrences;
- all eight assignments of the other three pole-depth labels;
- all three Cayley--Menger pole depths;
- all 91 two-variable numerator monomials of degree at most 12.

The resulting census is

\[
10\cdot8\cdot3\cdot91=21{,}840
\]

labelled squares. Every square vanishes before quotient reduction. There are no failures.

## Narrow result

The complete marked-pole relation map possesses a source-derived first Koszul syzygy differential. This is the correct domain in which a source-labelled Euler nullhomotopy could live.

The result does not yet identify the Euler commutator preimages with the image of this syzygy map. It therefore does not restore the superseded homotopy-flatness claim of Entry 2764.

No new carrier or coefficient primitive is introduced. The new object is a higher differential in the existing labelled relation resolution.

## Artifacts

- `research/benincasa/check_rank26_marked_pole_first_syzygies.py`
- `research/benincasa/rank26-marked-pole-first-syzygies.json`

## Next falsifier

Construct the quotient of commutator preimages by the image of this canonical first syzygy differential. Test whether the three Euler commutators define a unique class there, without selecting a Gaussian-elimination section.

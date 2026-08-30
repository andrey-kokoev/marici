# 3994 — The Rank-Five Infinity Image Is Canonically Contained in the Transported Seven-Plane

## Result

The source-defined rank-five anti-invariant infinity map from Entry 3990 has dual image
\[
L_5=\operatorname{im}(q^-_\infty)^*
\subset V_{26}^*.
\]

After transporting \(L_5\) into the exact coordinate convention used by the independently constructed source-jet annihilator \(A_7\), the two-prime calculation gives
\[
\dim L_5=5,
\qquad
\dim A_7=7,
\]
\[
\dim(L_5+A_7)=7,
\qquad
\dim(L_5\cap A_7)=5.
\]

Therefore
\[
L_5\subset A_7
\]
at both tested exact fibers.

No complementary two-plane was selected or fitted.

## Coordinate typing

The rank-five checker and Nima's annihilator packet initially use different free-coordinate conventions.

The comparison does not equate their coordinate indices. Each rank-five covector is first evaluated on the twenty-six original free monomial classes used by the annihilator packet. Only then are ranks and intersections computed.

Thus the inclusion is a quotient-invariant statement, not an artifact of matching basis labels.

## Occurrence inversion on the target

Under the labelled inversion
\[
t'=\frac1t,
\qquad
W'=t'^2W,
\]
the anti-invariant target basis
\[
(\omega_0,\omega_2,\alpha_0,\alpha_{-1},\alpha_\infty)
\]
transports by
\[
U=
\begin{pmatrix}
-1&0&0&-z&0\\
0&-y^2/x^2&0&0&0\\
0&0&0&0&-1\\
0&0&0&1&0\\
0&0&-1&0&0
\end{pmatrix}.
\]

The Poincaré-residue chart transition contributes a separate sign \(-1\).

The only non-obvious compact reduction is source-derived:
\[
L\left(\frac1{x^2t'}\right)
=
-\frac1{t'^2}
+\frac{y^2}{x^2}t'^2,
\]
where
\[
L(S)=FS'+\frac12F'S.
\]

Both geometric and signed transports are exactly involutive when composed with the reverse chart matrix.

The zero and infinity residue directions exchange. The minus-one direction is retained with its required compact \(\omega_0\) shift.

## Interpretation

Five of the seven transported annihilator directions now have a canonical geometric origin:

- two compact elliptic classes;
- three sheet-antisymmetric puncture classes.

The residual quotient
\[
A_7/L_5
\]
has rank two.

This rank equals the unavailable deck-invariant logarithmic sector, but equality is not established. The invariant source constructor remains absent, so the residual quotient must be treated as unclassified.

## Remaining gates

1. Construct the rank-five source map independently in the target occurrence chart.
2. Verify the full naturality square
   \[
   q^-_{\infty,\mathrm{target}}T
   =
   U^-q^-_{\infty,\mathrm{source}}.
   \]
3. Compute the transported action on \(A_7/L_5\).
4. Test its deck character.
5. Reject identification with invariant logarithmic classes unless a source map into those classes is derived.

## Scope

The target transport is exact over the rationals. The inclusion \(L_5\subset A_7\) is verified at two finite-field fibers. Full source-map naturality and characteristic-zero inclusion remain open.

## Artifacts

- \`research/benincasa/checkers/check_rank5_infinity_occurrence_inversion.py\`
- \`research/benincasa/results/rank5-infinity-occurrence-inversion.json\`
- \`research/benincasa/checkers/check_rank26_anti_invariant_infinity_map.py\`
- \`research/benincasa/results/rank26-anti-invariant-infinity-map-p32009.json\`
- \`research/benincasa/results/rank26-anti-invariant-infinity-map-p32003.json\`

Sequence claim: \`seqclaim-78e4930d1781735a17b5b24e\`.

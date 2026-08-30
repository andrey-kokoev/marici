# 1356 — The Cubic Infinity Coset Is a Deck-Complement Gluing Obstruction

## Status

Supported modular structure at the maximal observed rank fiber. Characteristic-zero certification remains open.

## Localization by radial growth

At the Entry 1349 fiber

\[
(p,z)=(1019,7),
\qquad
\dim\ker A=769,
\]

split the radial boundary map by the exact deck growth strata:

\[
10\times R^{-2},
\qquad
20\times R^{-4},
\qquad
2\times R^{-9}.
\]

The restricted results are

\[
\begin{array}{c|c|c}
\text{growth}&
\operatorname{rank}(B|_{\ker A})&
\text{boundary-zero affine primitive exists?}\\
\hline
2&574&\text{yes}\\
4&769&\text{no}\\
9&34&\text{yes}.
\end{array}
\]

Therefore the nonzero coset is supported entirely on the twenty growth-four sheets.

## Cyclic occurrence decomposition

The growth-four sheets form four free \(C_5\)-orbits:

\[
\begin{aligned}
\mathcal O_1&=(1,2,4,8,16),\\
\mathcal O_2&=(3,6,12,24,17),\\
\mathcal O_3&=(7,14,28,25,19),\\
\mathcal O_4&=(15,30,29,27,23).
\end{aligned}
\]

Their Hamming weights are respectively

\[
1,2,3,4.
\]

Every individual orbit has

\[
\operatorname{rank}(B_{\mathcal O_i}|_{\ker A})=360
\]

and admits a boundary-zero affine primitive. Thus no single occurrence orbit carries the obstruction.

## Deck-complement pairs

Deck complement exchanges

\[
\mathcal O_1\leftrightarrow\mathcal O_4,
\qquad
\mathcal O_2\leftrightarrow\mathcal O_3.
\]

For each pair,

\[
\operatorname{rank}(B_{1,4}|_{\ker A})
=
\operatorname{rank}(B_{2,3}|_{\ker A})
=
550.
\]

Since \(\dim\ker A=769\), each pair admits a nonempty affine torsor of local trivializations with translation space of dimension

\[
769-550=219.
\]

But for all four orbits together,

\[
\operatorname{rank}(B_{1,2,3,4}|_{\ker A})=769
\]

and the inhomogeneous boundary-zero system is inconsistent.

## Result

\[
\boxed{
\text{each deck-complement sector is separately trivializable, but their trivialization torsors do not intersect.}
}
\]

The cubic modular class is therefore not a local residue on one sheet, one cyclic orbit, or one complement pair. It is a gluing obstruction between the two complement-pair sectors.

A suitable derived description is the Čech-type class

\[
\boxed{
[\tau_{1,4}-\tau_{2,3}]
}
\]

where \(\tau_{1,4}\) and \(\tau_{2,3}\) are any local boundary trivializations. Their difference is independent of simultaneous affine-gauge translation modulo the common image.

## Architectural meaning

This is stronger evidence for the Carrier comparison calculus than a raw nonzero boundary rank:

- local coefficient data close on each declared sector;
- the failure appears only in compatibility across existing occurrence overlaps;
- no new infinity divisor or carrier cell is required;
- the nontrivial datum is a sector-gluing extension class.

This has the same type as earlier supported comparison failures:

\[
\text{local exactness}
\not\Rightarrow
\text{global relative exactness}.
\]

## Exact-certification target

The characteristic-zero dual certificate should now be sought on the much narrower complement-pair comparison, not on all 1921 primitive coefficients.

Construct a functional on the difference of the two local trivialization torsors that:

1. annihilates the common cubic affine-gauge image;
2. is invariant under \(C_5\) and deck complement;
3. evaluates nontrivially on the inhomogeneous derivative class;
4. reconstructs over multiple primes and verifies exactly.

Failure of such a functional would retract the modular gluing interpretation without affecting the raw rank packet.

## Artifacts

- `research/benincasa/results/five-site-asymmetric-cubic-boundary-localization.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_kummer_resolved_ibp_pilot.rs`

Allocator claim: `seqclaim-76745b062e3789b9cf4ec671`.

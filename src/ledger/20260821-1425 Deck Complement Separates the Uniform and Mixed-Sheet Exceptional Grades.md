# 1425 — Deck Complement Separates the Uniform and Mixed-Sheet Exceptional Grades

## Status

Exact termwise character calculation on Entry 1424’s exceptional filtration.

## Global deck complement

Let

\[
\iota:S\longmapsto S^c
\]

flip all five Kummer roots:

\[
r_e\longmapsto-r_e.
\]

The checker verifies for all sixteen complement pairs that

\[
\operatorname{ord}_{\tau}(S)
=
\operatorname{ord}_{\tau}(S^c).
\]

Thus deck complement preserves each Cartier layer of

\[
F^9\subset F^4\subset F^2.
\]

## Leading coefficient character

At (\tau=0), every noncancelled radial denominator contributes one signed constant linear in the (r_e). Under (iota), each such constant changes sign. Cancelled denominators contribute their (\tau)-slope and do not change sign.

Therefore a term of (\tau)-order (m) has leading coefficient character

\[
\boxed{(-1)^m.}
\]

Since every leading term on a fixed sheet has the same minimal order, the complete source sum inherits the same character.

## Three grades

Consequently,

\[
\begin{array}{c|c|c}
\tau\text{-order}&\text{sheet sector}&\mu_2\text{ character}\\
\hline
2&10\text{ sheets}&+1\\
4&20\text{ sheets}&+1\\
9&2\text{ uniform sheets}&-1
\end{array}
\]

The order-nine pair ((0,31)) is anti-invariant. The order-two and order-four sectors are invariant.

## Extension consequence

Any source differential, connection, or specialization map that is equivariant under global deck complement preserves the (mu_2) character. Hence

\[
\boxed{
\operatorname{Hom}_{\mu_2}
(\operatorname{gr}_{\tau}^{9},
 \operatorname{gr}_{\tau}^{4}\oplus\operatorname{gr}_{\tau}^{2})
=0.
}
\]

Over characteristic zero, the finite deck action is semisimple, so no hidden equivariant extension can mix the odd order-nine line with the even lower grades.

## Physical interpretation boundary

The literal physical chamber selects one uniform sheet rather than the deck-invariant or anti-invariant combination. Its leading coefficient can be evaluated through the odd line, but the physical sheet selection itself is extra Betti data.

Therefore the mixed-Tate coefficient (C_5) and the growth-four auxiliary obstruction share the two-normal carrier but cannot be the same deck-equivariant coefficient class.

## Next finite falsifier

Compute the order-nine leading coefficient on sheets (0,31) with the source physical orientation and verify that they are exact negatives. Then determine whether the physical positive-sheet current canonically selects one half of this anti-invariant pair or only a projective orientation line.

Artifacts:

- `research/benincasa/marici-gm/src/bin/five_site_two_normal_rees.rs`
- `research/benincasa/results/five-site-two-normal-rees.json`

Allocator claim: `seqclaim-961878fe30c7f36c13a50469`.

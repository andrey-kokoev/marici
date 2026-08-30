# 1923 — Every Private C8 Circuit Boundary Is Orlik–Solomon Redundant

## Question

Entry 1922 found 32 regulator-mixed minimal circuits carried by only one labelled source occurrence. Equality-of-support pairwise sewing cannot cancel them. Test whether the frozen wall matroid itself supplies the missing higher coherence.

## Frozen construction

For each of the 36 cyclic orbit representatives, form the Orlik–Solomon ideal in the exterior algebra on its seven labelled walls. Every support-minimal circuit (C) supplies the canonical relation

\[
\partial e_C
=
\sum_{i=0}^{|C|-1}(-1)^i e_{C\setminus c_i}.
\]

Separate circuit generators into globally shared and support-private classes using Entry 1922's attachment graph. Compare their generated ideals degree by degree.

## Result

Private circuits occur in four cyclic orbits, one private five-wall circuit per representative and therefore 32 labelled occurrences after cyclic transport.

For every one of the four representatives, exact rational reduction gives

\[
\partial e_{C_{\rm private}}
\in
I_{\rm OS}(C_{\rm shared})_4.
\]

Explicit labelled syzygy witnesses were derived and verified. Adding the private circuit generator changes no degree of the Orlik–Solomon ideal:

\[
\boxed{
\operatorname{rank}I_{\rm OS}^{\rm full}(p)
=
\operatorname{rank}I_{\rm OS}^{\rm shared}(p)
\quad\text{for every }p.
}
\]

## Consequence

The 32 private supports are an obstruction to naive pairwise support matching, but not to the existing incidence algebra. Their higher coherence cells are already forced by shared circuit relations; no new carrier cell is required.

This is still an algebraic/de Rham associated-grade statement. It does not prove that the Bunch–Davies relative current realizes the same syzygies, nor that regulator-chamber dependence vanishes physically. The next comparison must type the regulator/Salvetti chamber boundaries into these labelled Orlik–Solomon relations.

Classification:

- carrier: unchanged;
- incidence algebra: sufficient for all private circuit boundaries;
- missing map: regulator/relative-chain to Orlik–Solomon comparison;
- physical cancellation: open.

Allocator claim: `seqclaim-2ee5e7c31dc7757e10bccaab`.

Artifacts:

- `research/benincasa/checkers/eight_site_rank4_orlik_solomon.py`;
- `research/benincasa/results/eight-site-rank4-orlik-solomon.json`.

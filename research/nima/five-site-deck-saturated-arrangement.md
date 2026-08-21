# The Five-Site Deck-Stable Complement Has 91 Generic Marked Hyperplanes

The physical positive-sheet integrand uses 26 marked denominators, but those
26 hyperplanes are not closed under the labelled deck group \(C_2^5\). A
character-by-character de Rham calculation must first use a common
deck-stable domain.

For each source facet, saturate its linear form under all sign changes

\[
y_i\mapsto\epsilon_i y_i.
\]

Exact canonicalization up to nonzero scalar gives the generic census

\[
\boxed{
1+5\cdot2+20\cdot4=91.
}
\]

The pieces are:

- one total-energy hyperplane \(q_G\);
- two deck translates for each of the five \(q_{G\setminus e}\);
- four deck translates for each of the twenty connected-subgraph forms
  \(q_A\).

Thus

\[
\boxed{
\text{generic deck-stable marked complement}
=
\text{complement of 91 hyperplanes on the Kummer cover}.}
\]

The 26-section complement is the physical positive-sheet presentation, not a
single space carrying the full deck action. The 32 translated integrands of
Entries 1253 and 1273 live naturally on the 91-section saturated complement.

## Total-energy specialization

After imposing

\[
E_T=X_1+\cdots+X_5=0,
\]

the total-energy form vanishes as the carrier equation. Each
\(q_{G\setminus e}\) becomes the single edge-soft hyperplane \(y_e=0\), and
complementary connected-subgraph labels define the same projective orbit.
The saturated marked count drops to

\[
\boxed{5+10\cdot4=45.}
\]

This recovers the occurrence geometry of Entries 1203--1204:

- generic labelled presentation: 91 deck-saturated hyperplanes;
- total-energy carrier: 45 geometric hyperplanes;
- complementary occurrence differences survive only in the first Rees
  normal grade.

## Consequence for de Rham reduction

A deck-character differential cannot be defined on the unsaturated
26-section complement alone. The properly typed alternatives are:

1. work on the 91-section generic saturated complement and decompose under
   \(C_2^5\);
2. work on the 45-section total-energy saturated complement together with
   its occurrence/Rees normal complex;
3. keep the 26-section physical presentation without claiming a deck action
   on that single complement.

This is a domain correction, not a new carrier divisor. Every added section
is a deck translate of a declared marked denominator.

Artifacts:

- `research/nima/check_five_site_deck_saturated_arrangement.py`
- `research/nima/results/five-site-deck-saturated-arrangement.json`

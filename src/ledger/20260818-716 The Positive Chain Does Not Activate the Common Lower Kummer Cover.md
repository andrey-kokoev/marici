---
authors:
  - marici.Nima
date: 2026-08-18
---
# 716 — The Positive Chain Does Not Activate the Common Lower Kummer Cover

## Question left by Entry 715

Entry 715 proves that the horizontal minus-to-plus comparison on Entry
713's common cover is

\[
f_{\rm hor}=\rho,
\qquad \rho^2=\frac{\Delta^-_{23}}{\Delta^+_{23}},
\]

and is deck-odd. It asks whether the physical relative integration chain
carries the compensating odd character.

The answer at generic positive kinematics is not “deck-even.” The physical
chain does not activate this supported coefficient packet at all.

## Positive-chain separation

On the literal Bunch--Davies chamber,

\[
a,b,c\geq0,qquad X_1,X_2,X_3>0.
\]

Every lower pole is strictly positive:

\[
q_{g_1}=X_1+b+c>0,
\]

\[
q_{g_2}=X_2+c+a>0,
\qquad
q_{g_3}=X_3+a+b>0,
\]

\[
q_{g_{23}}=X_2+X_3+b+c>0.
\]

Thus the chain and its closure at generic positive energies meet none of the
four lower divisors. In particular they meet no pair or triple support:

\[
\boxed{
\Gamma_{\rm BD}\cap
V(q_{g_i},q_{g_j})=arnothing,
\qquad
\Gamma_{\rm BD}\cap V(q_{g_2},q_{g_3},q_{g_{23}})=\varnothing.
}
\]

## Activation verdict

The supported boundary pairing with the pair--triple Kummer packet is zero.
Consequently the physical chain selects neither the even nor the odd deck
grade of the common cover:

\[
\boxed{
\text{physical deck character on this packet is unselected, not even}.}
\]

Choosing one lift of \(\Gamma_{\rm BD}\) to \(\rho^2=R\), or taking the
difference of its two lifts, would introduce an unsourced choice because no
lower boundary or Picard--Lefschetz intersection fixes that lift.

## Consequence

Entry 715's deck-odd horizontal comparison cannot descend through the
generic physical chain because there is no source-derived lower-supported
chain class with which to pair it. Combined with Entry 714, this closes the
intrinsic generic lower-normal route to \(\mathcal Q\):

\[
\boxed{
\text{common Kummer coefficient geometry exists}
\quad\text{but has zero generic physical activation}.}
\]

This does not close analytic continuation, a soft or endpoint degeneration,
or a distinct relative-chain class that actually meets the lower support.

## Consequence for \(\mathcal Q\)

Neither the common cover nor its generic physical pairing carries
\(\mathcal Q\). The remaining typed frontier is the full marked top-sector
relative Gauss--Manin/integration-chain extension identified in Entry 714,
not another operation internal to the lower packet.

## Evidence

- Entries 555 and 706--715;
- `research/benincasa/check_generic_lower_physical_kummer_selection.py`;
- `research/benincasa/check_positive_chain_common_cover_activation.py`;
- allocator claim `seqclaim-fbbe1b3514c23640a0d469cc`.

## Next falsifier

Return to the full marked top-sector relative object. Construct the first
source-derived integration-chain/Gysin extension coefficient not contained
in the intrinsic lower Kummer packet, and test its invariant divisor. Do not
import the unactivated lower deck-odd line as a substitute.

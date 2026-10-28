# Prior inverse-compositor mate: direction and application to F736

## New directly relevant prior source

Read in full: `research/aspect/forward-backward-adjunction-and-mate-coherence.md`.

This source was not among the previous Voevodsky/Nima imports. It gives the precise categorical statement needed to distinguish the desired inverse mate from polarity reversal or a physical Hilbert adjoint.

For forward realization functors F_f,F_g,F_gf and a compositor

    alpha:F_g F_f => F_gf,

the right-adjoint mate has direction

    alpha_star:(gf)_star => f_star g_star.

When alpha is invertible, invert its mate to obtain the backward compositor

    f_star g_star => (gf)_star.

The source limits this explanation to the representable adjoint sector. General attachment correspondences need not have the required adjoint realization functors. Its finite tests check adjoint composition and hostile nonrepresentability; they do not implement the general analytical 2-cell mate formula.

No tests were run in this search.

## 1. Exact match of the F736 directions

Set

    f=C23 : E2 -> E3,
    g=C34 : E3 -> E4,
    h=C24 : E2 -> E4,
    alpha=H234 : g f => h.

For the source-generated EQUIVALENCE sector, choose the specified quasi-inverses

    f_bar=C32,
    g_bar=C43,
    h_bar=C42.

The source mate has direction

    alpha_star:C42 => C32 C43.

The geometric occurrence5 triangle in F736 asks for the OPPOSITE direction:

    beta=(alpha_star)^(-1):C32 C43 => C42.

Thus H234's inverse compositor mate, not an unchanged H234 label, is the required categorical candidate. No source-star action, endpoint exchange or Hilbert adjoint is needed to state this equivalence-level construction.

The notation star on alpha_star in this paragraph means categorical mate, NOT convolution involution, polarity dagger or operator adjoint. This distinction is essential given the different reversal operations found in v8.

## 2. Explicit unit/counit pasting

Let eta_h:I_E2=>h_bar h be the unit for h with chosen quasi-inverse h_bar, and let epsilon_f:f f_bar=>I_E3 and epsilon_g:g g_bar=>I_E4 be the corresponding counits.

Then the inverse mate is the typed composite

    f_bar g_bar
      --eta_h * (f_bar g_bar)--> h_bar h f_bar g_bar
      --h_bar * alpha^(-1) * (f_bar g_bar)--> h_bar g f f_bar g_bar
      --h_bar g * epsilon_f * g_bar--> h_bar g g_bar
      --h_bar * epsilon_g--> h_bar,

with associators/unitors inserted according to the chosen target convention.

Every route is E4->E2. This pasting is the concrete conditional calculation already outlined abstractly in v3, now matched to the direction-reversed compositor statement in the prior Aspect research.

For strict source-image chart equivalences, the chosen unit/counit maps reduce to source reconstruction identities. That simplifies the underlying edge maps, but does not delete a separately retained finite-regulator face representative. The actual analytical alpha must still be specified in the same target before this expression is its mate.

## 3. What prior analytical sources supply for the premises

The previously inspected source-rooted Cech tetrahedron supplies complete-form equivalences generated from a common source and coherent inverse/unit laws:

`research/voevodsky/the-rank-one-v1-supported-coherence-cell-is-a-four-chart-cech-tetrahedron.md`.

The complete-response and spectral reconstruction notes supply C32,C43,C42 on their admitted essential images. The master analytical note supplies complete-form/operator/feature transport in the source-transported topology.

The recovered H234 note supplies an analytical modification in the signed asymptotic realization target, represented by the cutoff-minus-spectral remainder:

`research/voevodsky/the-recovered-face-234-is-an-admissible-invertible-modification-in-the-rapid-decay-asymptotic-quotient.md`.

Its composition stability supplies the explicit conditional word pullback from v7. Invertibility of that modification is in the rapid-decay quotient. Neither alpha^(-1) nor the unit/counit pasting may therefore be presented as inversion of a finite physical scalar trace.

The remaining premise is a witness-preserving comparison identifying that alpha and its two boundary transformations with the chosen complete-form equivalence diagram. Naming all of them C23,C34,C24 is insufficient if those names refer to different carriers or different kinds of transformations.

## 4. Test the boundary identification before taking the mate

The concrete acceptance data are:

1. Identify the observer-indexed spectral composite transformation g f with the declared spectral functional/presentation route, including full source data.
2. Identify h with the centered cutoff transformation/presentation route in the SAME target, with the actual ordered projections and normalization.
3. Supply the comparison carrying the source H234 modification to alpha:g f=>h, preserving its representative remainder and endpoint/placement coordinates.
4. Supply units/counits for f,g,h in that target, not merely inverse maps on unrelated graph sets.

Only then does the pasting above yield the required beta. The unit/counit laws certify the mate boundary; they do not independently establish those analytical identifications.

This is a finite list of actual diagram maps and equations, not an additional generic mate-existence conjecture.

## 5. Retain the finite representative without guessing an inverse formula

For the v7 pulled-back representative

    H_w,Lambda = centered_cutoff_Lambda o r_w - spectral o r_w,

the source estimate and exact candidate-edge transport are already available under the declared bounded-packet hypotheses.

The mate acts on the modification and its boundary transformations through the chosen whiskers. A formula such as minus H_w,Lambda is not automatically its representative: that requires a specified additive realization model and the correct whiskering maps. Taking a categorical inverse in the asymptotic target does not by itself prescribe a unique finite-cutoff representative.

Consequently the analytical deliverable must return the representative together with its target, boundary maps and comparison, not just a signed scalar.

## 6. Both bottom/filler pairs follow the same shared face

After beta is identified at occurrence5, retain the independent occurrence4 C21 map and adjacent-occurrence links to obtain one shared H736.

The actual tetrahedral equations remain

    H732 o (H745 * e511) = H736 o (e539 * H731),
    H735 o (H760 * e513) = H736 o (e539 * H734).

Use the paired completion construction for both missing bottom faces with this same H736; do not choose separate inverse mates in T324/T325 merely because their generic filler spaces are contractible. The fixed-boundary presentation bridge can translate both pairs using the same context-independent common-face map.

## Disposition

The desired direction C32 C43=>C42 is explicitly the inverse right-adjoint compositor mate of H234 in the source-generated equivalence sector. This categorical mechanism is present in prior research and admits the concrete typed unit/counit pasting above.

The remaining analytical calculation is its boundary/witness identification and finite representative under the exact source maps. This search does not assert that identification, finite-cutoff inverses, a physical dagger, or the completed native F736 package. No source file outside this search record was changed.

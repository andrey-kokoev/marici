# A consistent calculus exists, but marking transport is state-dependent

ramsey_row_center_calculus.py constructs the affine seed graph G, its literal row image RG, and center transfer T independently on each by pulling back the unique full-orbit operation from a verified catalogue isomorphism. The uniqueness/C5 invariance of the five-switch set makes this graph operation independent of the five choices of identification.

Verified as equality of labeled adjacency matrices:
R^2 G=G, T^2 G=G, T(RG)=R(TG).
The four states therefore form a commuting square of graph updates. R fixes the current physical root/hub vertices; T exchanges which is the unique structural Hall center.

Typed markings require a further distinction. All graph isomorphisms K:G->TG carry center0 to hub3, neighbors to new ground labels, and duads/partition flags into valid new incidence roles. There are exactly five such maps, obtained from one by composing with the C5 automorphisms of G (the unique center forces every graph automorphism to fix it). Every K is an involution. However NONE of the five commutes with the literal row permutation R as a permutation of the22 fixed vertex labels. Exact permutations and tests are in the JSON.

Nevertheless, choose any one K on the initial side and use K_R=R K R on the row-related side. Then K_R maps RG to T(RG), and K_R R=R K. Thus the typed marking obtained by row-then-transfer agrees exactly with transfer-then-row. Since K and K_R are involutions, the inverse transfers also transport marks consistently. The resulting correspondence is explicit once the initial phase K is chosen.

Interpretation: commutativity of STATE UPDATES does not imply that both can be represented by a single pair of commuting fixed vertex permutations. The row operation changes the required marking-transport map. This supplies a finite state-dependent (moving-frame) calculus while retaining the distinction between physical labels and incidence roles.

What is not fixed: the five possible initial transports K. The bare graph transfer has no such ambiguity, but carrying a particular entry/exit frame across it does. An extra operational rule or anchor is needed to select one. Simply demanding K^2=1 does not choose among them: all five are involutions. Nor can one demand a constant K commuting with R: there is none. No claim is made that this new calculus is already the originally intended seed dynamics.

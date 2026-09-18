# Maximal free flavor presentation over the A3 Coherent Resolution

## Question

What flavor-labeled descent can be constructed after the boundary completion supplies all 21 A3 coefficient ratios?

## Corrected coefficient boundary

`research/nima/results/n8-boundary-completed-cluster-transport.json` supersedes the earlier 14-edge coefficient blocker at the selected `n=8` stage. It supplies three exact negative-simple weights, defines all 21 mutation ratios, and has unit holonomy on all nine square or pentagon faces. The surviving exchange defect is explicitly separate from this rank-one flat line.

## Constructed maximal free target

Let \(CR_\bullet\) be the cellular A3 complex with bases \(V,E,R,T\) of 14 triangulations, 21 flips, nine relation cells, and one top cell. Define the maximal source-derived free flavor presentation

\[
F_k^{\rm free}=\mathbb Z\langle f_x:x\in CR_k\rangle,
\qquad d_F(f_x)=f_{d_{CR}x}.
\]

Its admissible equivalences are only the cellular boundary relations already present in \(CR_\bullet\). Its augmentation sends each \(f_v\) to 1. The generator map

\[
\Phi_k(x)=f_x
\]

is the degreewise identity after relabeling. Exact matrix tests cover all 14 vertices, 21 edges, nine faces, and the top cell. They give \(d_F\Phi=\Phi d_{CR}\), zero kernel, full image, and an isomorphism on augmented homology. Since the augmented source and target are exact, that homology is zero in every degree.

This construction is a presentation object, not a physical flavor quotient. The symbols \(f_x\) name Carrier cells; they do not name Yukawa orbits.

## Flat coefficient line

The completed mutation ratio has the form \(r(C,C')=W(C')/W(C)\). Multiplication by \(W(C)\) is a vertex gauge conjugacy from the weighted rank-one cellular line to the untwisted one. Unit face holonomy supplies path independence on the A3 polytope. Thus the flat coefficient transport is removed at the presentation level. This does not remove the separately reported nonzero exchange defect and does not turn the gauge into a weak-basis quotient.

## Deliberate false descent

Keep the vertex map equal to the identity but multiply one edge generator by 2. For that edge \(e:a\to b\),

\[
d_F(2f_e)-\Phi_0(d_{CR}e)=f_b-f_a\ne0.
\]

The checker records two nonzero residual entries. Hence arbitrary edge rescaling does not define a chain map even though the true relabeling map does.

## Physical quotient gate

The flavor source defines the physical domain as weak-basis orbits of Yukawa pairs. It defines

\[
c_{16}:[(Y_u,Y_d)]_{\rm WB}\to X_{16}
\]

as faithful and \(\pi_{10}:X_{16}\to X_{10}\) as a nonfaithful measured projection. The A3 sources contain no map from a triangulation, flip, relation cell, or top cell to a Yukawa pair or weak-basis orbit. Therefore neither \(c_{16}\circ\Phi\) nor \(\pi_{10}\circ c_{16}\circ\Phi\) is typed.

No `physical16` faithfulness test or `physical10` fiber census can be performed on this presentation. The first absent relation is not a cellular relation: it is a source-derived assignment from Carrier vertices to weak-basis Yukawa orbits, coherent with edges and relation cells. Without it, presentation multiplicity is the 14-cell Carrier basis while physical multiplicity is undefined; these cannot be identified.

## Dispositions

Constructed descent: accepted for the maximal free presentation. It is a degreewise chain isomorphism and the completed flat coefficient line is gauge-trivial there.

Quotient faithfulness: deferred. `physical16` remains faithful on its independently declared Yukawa quotient, but no comparison map gives it a Carrier domain.

Remaining source obstruction: a covariant generator assignment \(V\to[(Y_u,Y_d)]_{\rm WB}\), edge transports between those orbits, and coherence on all nine relation cells. Acceptance requires explicit images and a checker composing them with `physical16`; only then may `physical10` residual fibers be enumerated.

## Claim boundary

The construction is exact at finite A3 and uses the selected `n=8` boundary completion. It does not promote to all cutoffs, construct a Yukawa quotient, or infer physical identity from the free presentation.

Verification:

- `research/figueiredo/checkers/check_coherent_resolution_maximal_free_flavor_presentation.py`
- `research/figueiredo/results/coherent-resolution-maximal-free-flavor-presentation.json`

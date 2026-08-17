# D03 Ringed Carrier Requires Normal-State Grothendieck Lift

## Defect and repair

Entry 352 defines the ringed target on 215 points (x=(S,H)), with
(H\subseteq S). Entry 356 instead declares (G_{03}) to be the
581-point barycentric face carrier and describes its blowdown only by the
initial face (S). A face alone does not select the target normal state
(H). Consequently the face-only arrow asserted there does not type the
verified 1,169-generator loaded pullback as a literal inverse image.

The checker already supplies the minimal repair. Replace (G_{03}) by the
normal-state Grothendieck carrier

\[
\widetilde G_{03}
=\{(\sigma,H):H\subseteq b(\sigma_0)\},
\]

and define

\[
\widetilde b(\sigma,H)=(b(\sigma_0),H).
\]

Its cellular boundary deletes either one flag vertex or one element of
(H). Deleting the initial flag vertex applies the radial localization;
deleting another flag vertex maps to the identity target incidence; and
deleting a normal mark maps to the target normal-deletion incidence. Thus
every boundary cover maps to a target incidence or identity.

The exact census is

\[
|X|=215,qquad |G_{03}|=581,qquad |\widetilde G_{03}|=1169.
\]

## Consequence for q-shriek

The dualizing calculation begun for the face-only map computes the wrong
correspondence for the loaded Entry-352 module. The actual repaired
pre-quotient correspondence is

\[
\widetilde Z_{03}^{\rm pre}
=\widetilde G_{03}\times I_{\rm occ},
\qquad
\widetilde q=\widetilde b\circ\operatorname{pr}_{\widetilde G},
\qquad
\mathcal O_{\widetilde Z}=\widetilde q^{-1}\mathcal O_X.
\]

The occurrence-interval right-adjoint calculation remains valid after
replacing (G_{03}) by (widetilde G_{03}). Hence

\[
\omega_{\widetilde q}
\simeq\operatorname{pr}_{\widetilde G}^{!}
   (\widetilde b^{!}\mathcal O_X),
\]

and perfectness is reduced to the corrected
(omega_{\widetilde b}=\widetilde b^!\mathcal O_X).

All earlier statements that only establish existence of a right adjoint
for a supplied finite-ringed map remain formal. Statements identifying the
face-only (b) with the loaded pullback are superseded by this repair.

## Evidence boundary

`research/voevodsky/check_d03_ringed_carrier_typing.rs` independently
reconstructs all 45 old faces, 51 blowup faces, 581 barycentric cells, 215
target normal states, and 1,169 corrected carrier points, and checks every
cellular boundary cover against the target incidence relation.

This entry repairs the domain and map. It does not yet compute
(omega_{\widetilde b}), prove it perfect, or compare it with Entry 176.

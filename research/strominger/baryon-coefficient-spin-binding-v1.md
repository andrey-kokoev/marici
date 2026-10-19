# Actual36-mode baryon transport and the doubled spin square

Iteration7 constructs the actual coefficient transport for all three source affine generators, rather than assigning identity because the return is fixed. This fills the mathematical action cell left by iteration6. Source-supported lift/frame selection and charge/magnetic/internal laws remain open.

## Proton: the real source dictionary

Bind source0,e1,e2,e3 to native A,B,C,D, respectively, with the retained native tetrahedral coordinates. The affine linear adapter V has those native edge columns and satisfies V^T V=M_source. Conjugating each actual source generator gives its native spatial rotation R=V T V^-1. Its vertex permutations are exactly

    generator0: (A,B,C,D)->(B,C,A,D),
    generator1: (A,B,C,D)->(D,A,C,B).

Using the actual sorted twelve triangle placements, R maps each placement rotation R_t to R R_t. The36-mode action moves the corresponding triangle block and applies R to its three vector coefficients. Port ordering is checked against the actual common-assembler packet, not inferred from equal dimensions.

## Neutron: transport through the actual plane embedding

The existing Cartesian frame V_n maps the actual mode-neutron source rotation to the native cyclic coordinate rotation (x,y,z)->(z,x,y), with V_n^T V_n=(8/3)M_source. The source seeds match the retained belt vertices. Propagate this actual rotation to all eighteen ordered triangle modes.

Let W contain the stored real plane-column numerators and d the intrinsic metric denominators. In the actual numerator-coordinate convention,

    Emb=W diag(1/d), Dec=W^T,
    Dec Emb=I36,
    P_intrinsic=Dec P_ambient Emb,
    P_ambient Emb=Emb P_intrinsic.

Fresh exact multiplication gives the familiar one-step sector shift among the three12-coordinate sectors. That shift is now DERIVED from this source generator and retained embedding, not assumed from its order or matching support count.

## Source-bound return character and spin square

For every actual36-mode action P, the checker verifies

    P^3=I, P^sharp=P^2, P L=L P, P G=G P,
    P K=K, D P=D, P N=N P=N.

Thus all three actual spatial-alignment line characters are chi=1. These actions are NOT the local triangle-character cycles, whose phase law is a different source operation. No local omega phase is substituted for a spatial alignment action.

Combine P with BOTH metric-Clifford lifts U from iteration6:

    (P tensor (+/-U)) K_tilde=K_tilde (+/-U),
    D_tilde (P tensor (+/-U))=(+/-U) D_tilde.

These are the actual doubled encoding squares for this explicit tensor candidate. No physical lift is selected; the chosen source/spin frames and enlarged carrier remain explicit. Numeric primitive transport cost and physical coupling are not inferred.

## Hostile: return covariance alone would accept the wrong action

Every P differs from I36, but both P and I36 fix K. Therefore the return-line square alone cannot reject replacing actual mode transport by identity. The checker exports a concrete coordinate-basis input and coefficient reader for each generator on which P and identity give different next values. Both routes still have the same final return projection because NP=N.

This tests the SOURCE attachment on a broader mode-reader task. It does not claim that the normalized return-state packet reconstructs arbitrary raw inputs; that extraction was deliberately image-scoped. The additional retained source/action data is what keeps the broader question available.

## Net disposition and next executable work

The spin/coupling node remains open but is removed from the actionable frontier: its remaining inputs are source-supported lift/frame and interaction/resource records already requested from Nima. Repeating the request or guessing a law is not a new experiment.

The native-protocol cost/compression comparison can run independently of those missing physical inputs. The net explicitly records the research-prerequisite revision and freezes its scope before that test: actual coefficient occurrences, endpoint versus retained-stage/mode interface, explicit sharing/archive policy, no physical units. The root STILL requires the positive coupling gate; this planning change supplies no bypass or closure.

## Verification

    python research/strominger/checkers/check_baryon_coefficient_spin_binding.py
    python research/aspect/scc/scc.py check baryon-coefficient-spin-binding-v1
    python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1

Nine fresh exact checks pass. Receipt `research/strominger/results/baryon-coefficient-spin-binding-v1.json` exports all three sparse36-mode action matrices, construction dictionaries, line characters and raw-mode hostiles. Native sources/stores/receipts remain unchanged; no owner producer or proof compiler is run. Formal outcomes remain null; no physical coupling, mass, cost or time claim is made.

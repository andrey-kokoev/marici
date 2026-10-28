# Prior joint construction of the bottom feature and polarized filler

## Search result

The closest prior result is not merely a Schur criterion. It constructs the internal common-face Gram from a commuting positive cell with orthogonal face decompositions. An explicit Hadamard feature gives the finite ordered relative realization. The external physical comparison remains a separate theorem.

This refines `f736-bottom-face-coupled-construction-clues-v1.md`: do not describe all joint bottom/filler construction as open. Distinguish internal feature construction from its binding to F736 and independently normalized external carriers.

## 1. Exact internal construction

Read: `research/voevodsky/strict-cell-commutativity-proves-the-common-remainder-gram-identity.md`.

At a regulated coordinate alpha, assume the positive cell retains target isometries and orthogonal decompositions

    U_T X_T = B_T direct_sum Xhat_T,
    U_0 X_0 = B_0 direct_sum Xhat_0.

Its shared-face maps give the SAME source-labelled feature

    B = r_T X_T = r_0 X_0.

Then calculate the feature and Gram together:

    G_T = B*B + Ghat_T,
    G_0 = B*B + Ghat_0,

hence

    G_T - Ghat_T = B*B = G_0 - Ghat_0 >= 0.

The bottom/common feature is B itself. Its positive Gram is not guessed by subtracting signed trace values. The isometries, orthogonal inclusions and equal common-face maps are part of the same cell datum.

The theorem does not construct those ingredients from an arbitrary signed diagram. Its statement expressly requires the full positive cell, and excludes unrelated external prolate/Widom features unless installed by an isometric comparison.

The common face in this metric decomposition must also be explicitly identified with whichever simplicial bottom face is intended; the word 'bottom' alone does not identify B with F745 or F760.

## 2. Explicit physical cross-polarized feature

Read in full: `research/voevodsky/hadamard-polarization-gives-the-complete-physical-cross-feature-for-the-ordered-relative-form.md`.

At finite regulation let

    P=P_Lambda,
    A=P_R-P_Lambda,
    R=P+A,
    q in {T,0}.

For the actual observer operator U_g define

    x_q(g)=Q_q P U_g,
    y_q(g)=Q_q R U_g,
    X_q_plus=(x_q+y_q)/2,
    X_q_minus=(x_q-y_q)/2.

All displayed Hilbert--Schmidt rows require the declared finite regularization. Their difference of Grams is the Hermitian cross pairing H_q, not a false diagonal compression.

The complete relative legs are

    X_cross_T = X_T_plus direct_sum X_0_minus,
    X_cross_0 = X_T_minus direct_sum X_0_plus.

Thus exactly

    G_cross_T - G_cross_0 = H_T-H_0 = D_ordered.

This construction retains the inside--annular cross seam. The annular squares arise as common positive mass in the Hadamard legs; they are not fitted equal summands.

The note identifies these residual Grams with the eight-leg residual Grams only with the SAME exact transported regulator, source legs and Hadamard normalization. This is an explicit alignment condition, not a consequence of equality of arbitrary signed differences.

If an extensive shared row B is included, set

    X_physical_T = B direct_sum X_cross_T,
    X_physical_0 = B direct_sum X_cross_0.

The common-remainder identity then follows with common Gram B*B. Identification of B with an independently normalized physical mismatch/volume row is the additional absolute-feature theorem. The paper explicitly describes the construction as a metric filler over the FULL presentation tetrahedron at fixed regulator, not one isolated depth-indexed sub-tetrahedron.

## 3. Why naive channel Grams do not calculate this cell

Read: `research/voevodsky/the-naive-physical-tate-reference-channel-grams-miss-the-ordered-cross-seam.md`.

The diagonal rows (Q_q P U_g, Q_q A U_g) give

    U* (P DeltaQ P + A DeltaQ A) U,

whereas the ordered Hermitian relative form is

    U* [P DeltaQ P + (P DeltaQ A + A DeltaQ P)/2] U.

Their difference contains the cross seam and need not vanish. Orthogonality PA=0 does not imply P DeltaQ A=0. Therefore a joint calculation must start from the complete cross-polarized rows, not from separately positive diagonal channels that omit their interaction.

These Hermitian feature formulas do not authorize deleting the skew part of the ordered product. The F736 deliverable still retains its separately typed skew-placement channel.

## 4. The authoritative index resolves apparently conflicting prior statuses

Read completely: `research/voevodsky/positive-coherence-authoritative-frontier-index.md`.

Its section4 states:

- finite-cutoff internal polarized cell commutativity is closed;
- internal common-face Gram identity is not an additional asymptotic theorem;
- identifying external, independently normalized Widom Grams is separate;
- equality of signed forms loses common positive summands.

Section10 states the signed Sonin Green/endpoint coupling is constructed; positive endpoint control still requires the Schur--Douglas estimate. It also rules out treating isometric dyadic refinement as new positive capacity.

Accordingly the negative conclusion in `the-physical-common-remainder-cannot-be-derived-from-the-current-signed-transport-results.md` must not reopen the INTERNAL positive cell. It warns against deriving an independently physical common remainder from signed transport alone. The distinction is the chosen positive carrier, not just chronology or matching notation.

## 5. A proposed induction is conditional, not an available shortcut

Read: `research/voevodsky/the-k-successor-four-simplex-turns-positive-filling-into-a-base-case-plus-defect-square-induction.md`.

It proposes a valid implication if a genuine source-defined orthogonal new defect row Y_k satisfies

    C_(k+1)=S_k* C_k S_k + Y_k*Y_k,
    B_(k+1)=S_k* B_k S_k.

But the authoritative index says the existing dyadic Halmos refinement is isometric and conserves total Gram; it does not supply positive accretion by itself. The proposed Y_k must be independently identified, not defined from the desired positive margin. This is not a proved induction closing the external Schur gate.

## 6. Application to the F736 coupled patch

Keep the actual simplicial equations from the preceding search:

    H732 o (H745 * e511) = H736 o (e539 * H731),
    H735 o (H760 * e513) = H736 o (e539 * H734).

The prior results suggest the following concrete extraction rather than another independent face choice:

1. Instantiate ONE retained positive/relative feature cell on the actual regulated source domain, with the complete ordered rows and separately retained skew channel.
2. Identify its actual common-face maps, orthogonal inclusions and target isometries with the F736 patch presentations. Do not assume generic census labels supply them.
3. Calculate the shared feature B and its Gram simultaneously from those face maps; carry the existing analytical H234 representative and its mate in the same realization target.
4. Obtain H745,H760,H736 and the two tetrahedral comparisons as restrictions/pastings of that same cell, not independent fitted witnesses.
5. Only if an external physical normalization is required, prove the corresponding isometric feature comparison and endpoint Schur bound. Internal common-face closure is not that external theorem.

The remaining F736 task is therefore extraction and witness-preserving binding of an existing internal construction. No exact F745/F760 analytical face formula was found outside the prior generic incidence records and the current Strominger extraction in this search. This is a bounded search observation, not proof of absence.

No tests or analytical certifications were run. No prior source was edited.

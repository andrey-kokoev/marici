# Prior exact cutoff-boundary comparison and its retained calibration field

## Search result

Prior research contains an exact finite-regulator comparison of the physical ordered relative cutoff product with its Hardy/eight-leg presentation. It also contains source-derived volume features and actual signed, defect-augmented comparisons between Hermitian-form presentations.

Together these give a concrete boundary-level calculation for the proposed K(eta24), rather than another abstract graph inverse. They do NOT, without further source and target identifications, give a natural higher realization comparison K for the native F736 diagram.

No tests or formal builds were run. The algebraic centered-boundary decomposition below is extracted here from the independently defined source traces; it is not claimed as a fresh analytical convergence theorem or a verbatim theorem from the source.

## Sources freshly inspected

- `research/voevodsky/exact-regulator-transport-aligns-the-physical-product-cutoff-with-the-eight-leg-hardy-readout.md` — characterwise physical-to-Hardy unitary, exact regulator/observer placement, finite trace identity, reference calibration and logical-circle warning.
- `research/voevodsky/h123-and-h124-have-canonical-positive-lifts-before-centered-finite-part.md` — regulated cutoff feature plus an independent Plancherel-volume feature; centering as a fixed signed readout, not positivity of the centered form.
- `research/voevodsky/moving-prolate-placement-volume-splits-into-an-exact-source-cocycle-and-an-asymptotically-natural-boundary.md` — exact volume successor and finite placement transport; asymptotic relative-boundary qualifications.
- `research/voevodsky/the-semilocal-geometry-to-trace-edge-has-an-eight-node-factorization-following-connes-theorem-4.md` — actual source eta24 operations and centered trace family.
- `research/voevodsky/the-source-authorized-suzuki-to-semilocal-comparison-is-defect-augmented-and-does-not-supply-a-positive-lattice-edge.md` — an actual signed Hermitian-presentation comparison retaining an independently defined defect.
- `research/voevodsky/trace-class-localization-makes-transported-regulator-removal-automatic.md` — precise strong/trace-norm compression criterion and endpoint-index split.
- `research/voevodsky/correction-translation-strong-convergence-leaves-an-observer-hardy-commutator-remainder.md` — an interior Hardy projection cannot be treated as an exterior factor of the observer-sandwiched trace-class operator; preserve the commutator remainder.
- `research/nima/forward-realization-comparison-commutes-with-projective-graph-completion.md` — extension of a defined labelled forward comparison; no reverse equivalence or semantic intertwiner follows automatically.

Some of these are already evidence for verified imports in the net. This note narrows their application; repeated discovery does not count as another independent analytical result.

## 1. Actual finite operators are already compared, not merely their terminal values

On each admitted character sector, the source provides a unitary U_chi, with L=log Lambda, such that

    U_chi P_Lambda U_chi^* = Pi,
    U_chi Q_Lambda^T U_chi^* = Q_(L,chi)^T,
    U_chi A_h U_chi^* = M_(m_h,chi),
    Z_tilde = U_chi Z_physical U_chi^*.

The pure reference is also defined on that SAME carrier:

    Q_L^0 = M_(exp(2iLs)) Pi M_(exp(2iLs))^*,
    Q_(Lambda,chi)^0 = U_chi^* Q_L^0 U_chi.

Thus conjugation transports the complete ordered operator string, including the actual outer/angular regulator. At finite regulator,

    Tr(Z P_Lambda (Q_Lambda^T-Q_Lambda^0) A_h Z)
      = Tr(Z_tilde Pi (Q_L^T-Q_L^0) M_mh Z_tilde).

The comparison is not obtained by moving the observer through Pi, replacing Z_tilde with a symmetric Mellin window, or fitting a scalar Gram. At finite character cutoff it assembles by finite direct sum.

The source also supplies an eight-leg cross-polarized feature with fixed Hermitian and skew readouts for this relative ordered product. Unequal left/right regulated observer legs must stay unequal where required. This is an actual operator/factorization comparison, stronger than a coincidental scalar readout equality.

It still has a declared semilocal source and regulator system. It is not automatically the compact-physical one-sector F736 realization or a presentation-functor comparison on all of its constructors.

## 2. Exact centered eta24 data: keep the reference calibration

For the SAME source observer h, source sector and finite regulator alpha=(Lambda,R,N), write

    T_alpha^T(h) = Tr(Z P_Lambda Q_Lambda^T A_h Z),
    T_alpha^0(h) = Tr(Z P_Lambda Q_Lambda^0 A_h Z),
    D_alpha(h)   = T_alpha^T(h)-T_alpha^0(h),
    delta_alpha^0(h) = T_alpha^0(h)-2 L h(1).

All traces and the source trace-density convention must be admitted at these types. Then, by subtraction,

    T_alpha^T(h)-2 L h(1)
      = D_alpha(h)+delta_alpha^0(h).                 (CENTERED)

This is exact at finite regulator. It exposes the missing field if one tries to identify the centered eta24 boundary with the relative eight-leg readout D_alpha alone.

The source trace theorem centers by 2 L h(1). The Hardy relative-projection formula subtracts the actual pure-reference trace. These are different finite operations. The defect delta_alpha^0 is independently determined by that source reference and volume trace; it is not a free scalar selected to enforce an identity.

For a spectral/source readout V(h)=W_S(h), the inherited finite remainder consequently decomposes, on matching admitted data, as

    E_alpha(h)
      = [D_alpha(h)-V(h)] + delta_alpha^0(h).        (REMAINDER)

At finite outer/angular regulator this notation denotes the regulated discrepancy. It is not silently identified with the unregulated E_Lambda of the parent theorem. That identification requires the prescribed regulator-removal comparison and conventions.

The same subtraction works for the OTHER ordered placement, keeping that placement's source trace, reference trace and calibration together. Under adjoint, transport the full ordered string, including observer and regulator legs. Do not assume a finite regulator commutes with the observer merely to rewrite the adjoint as a more convenient placement.

## 3. The volume coordinate already has a source-authorized feature

The canonical Plancherel trace satisfies

    tau_S(lambda_S(h)) = h(1).

On polarized source pairs its positive volume feature is

    X_vol,L(g)=sqrt(2L) j_S(g),

with the source ordering convention for the paired Plancherel Gram. The H124 lift retains the cutoff feature and X_vol as separate coordinates, using a fixed signed readout to recover the centered expression.

The affine source law is exact:

    V_(L')-V_L = 2(L'-L) tau_S.

This provides a typed way to carry the counterterm through a presentation comparison. It does not make the centered cutoff positive, nor prove that delta_alpha^0 is zero.

Thus a plausible target for K(eta24) must carry either the full centered trace family or the pair (relative boundary, reference calibration), together with its source-volume provenance. Replacing that pair by only the relative boundary loses finite data.

## 4. Limits: do not turn o(1) into the parent's rapid ideal

The exact regulator-transport paper separates finite conjugation identities from analytical reference calibration. A later compression theorem says that a uniformly bounded strongly/adjoint-strongly convergent regulator family preserves the trace of an ACTUAL S_1 operator in the limit. Character assembly additionally needs a summable trace-norm majorant. Endpoint/index channels must be retained separately when the regular kernel alone does not contain them.

These are sufficient hypotheses for the indicated OUTER relative regulator removal, not arbitrary-domain or arbitrary-path convergence. The moving-placement note's stronger polarized cutoff-translation argument has a separate correction: moving an interior Hardy projection past the left observer produces an observer--Hardy commutator remainder. Trace-class membership of the sandwich and strong convergence alone do not prove that remainder vanishes. Nothing here imports that uncorrected claim or identifies outer-regulator removal with cutoff-translation convergence. Existing regular-kernel and one-sector results may discharge parts on their declared sources; a new native identification must cite the matching version rather than reopen them generically or extend them without proof.

Even after suitable limits yield

    T_Lambda^0(h)=2 L h(1)+o(1),

this gives delta_Lambda^0=o(1), not an independently proved rapid-decay bound. The parent theorem gives rapid decay of the TOTAL cutoff-minus-Weil error. In (REMAINDER), neither summand inherits that rate from the total without a separate estimate; cancellation may matter.

The trace-norm-null quotient used for relative-boundary convergence is also not automatically identical to Fam(E_S)/N_S, the scalar rapid-decay quotient carrying the parent H234 representative.

The exact transport note warns against a circular argument: do not use Connes's cutoff formula and reference calibration to prove the same relative trace limit that was needed to derive that calibration.

## 5. A prior presentation-level defect augmentation exists, but on another comparison

The Suzuki comparison note defines independent source pullback forms q_arith and q_Suz and their actual difference delta. It then forms a defect-augmented presentation whose represented form is q_Suz+delta=q_arith. The resulting signed comparison is an equality of represented forms with different retained factorization data, in the Hermitian-presentation category.

This is a genuine precedent for adding a source-derived comparison field to a presentation; the target need not be merely a set of graph vectors. But it is an external comparison cone, not a replacement canonical tetrahedral vertex or a positive edge. Erasing its defect changes the represented form unless the source theorem gives absorption or vanishing.

For eta24, the analogous disciplined step is to retain the actual delta_alpha^0 from (CENTERED), not declare it zero or introduce a new residual chosen from desired face equations. The Suzuki result supplies no F736-specific higher comparison or physical positivity theorem.

## 6. What is still required to promote this to K(eta24)

The search has located a concrete finite boundary calculation and operator transport. To make it the requested natural realization comparison, one must still:

1. identify the source observer maps and regulator conventions of the parent eta24 with those in the candidate retained F736 presentations;
2. type the full centered boundary, or (D_alpha,delta_alpha^0), as regularization/factorization data of those observer-indexed presentations;
3. prove compatibility of the actual constructor/observer arrows with this data, not merely equality on a chosen source input;
4. compare both placements and endpoint/volume conventions without erasing the calibration field;
5. place eta23,eta34 and H234 in the SAME enhanced target, with composition/unit comparisons and recovery of the total finite remainder;
6. then apply the inverse mate and calculate both bottom/filler pairs over one H736.

Forward continuity can extend an ALREADY defined labelled comparison through projective graph completion, as Nima's note proves. It cannot supply a missing semantic naturality equation or promote the forward map to an inverse. Likewise, finite conjugation of operators is not by itself the higher functor K.

## Narrowed next calculation

Write the candidate centered eta24 boundary in the retained chart. Check (CENTERED) against its actual coordinate definitions, including delta_alpha^0 and the common source-volume trace. Then state the naturality square for one actual native observer/constructor map and verify it with the true transported regulator.

If the proposed boundary currently contains only D_alpha, the exact missing finite field is delta_alpha^0. If it already retains the full centered trace, that field is accounted for algebraically and the next missing datum is the presentation/arrow identification—not another volume or remainder estimate.

No claim is made that this calibration field is the sole F736 obstruction, or that the native higher comparison or positive filler has been completed.

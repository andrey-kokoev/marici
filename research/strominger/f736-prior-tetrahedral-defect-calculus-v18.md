# Prior tetrahedral defect calculus: compute shared face and bottoms on the same boundary

## Fresh discovery

Read the section **Higher simplicial realization and coherence defects** in

`research/voevodsky/the-full-analytical-system-is-the-joint-graph-realization-of-the-regular-and-endpoint-channels.md`.

It supplies a direct operator boundary identity that was not yet extracted in the preceding F736 search records. Also inspected `research/aspect/constructor-permutohedron-bianchi-closure.md` for the distinction between full transported boundaries and products of scalar observations.

No tests or certifications were run.

## 1. The master source distinguishes strict retained charts from output defects

For source-retaining presentations J_i(x)=(x,T_i x), the source defines

    C_ij=J_j projection_source.

These compose strictly and form a source-reached pair groupoid represented by complemented graphs. This is the appropriate existing description of the v17 candidate carrier/word diagram.

For INDEPENDENTLY COMPLETED output carriers W_i and actual comparison maps

    D_ij:W_i -> W_j,

the source instead defines

    Omega_ijk=D_ik-D_jk D_ij : W_i -> W_k.

When all maps/composites have the stated common bounded graph domains, it proves

    Omega_ikl - Omega_ijl
      + D_kl Omega_ijk - Omega_jkl D_ij = 0.          (B)

This is the tetrahedral Bianchi identity for presentation defects. The retained-source groupoid is its zero-defect sector; a general output realization can retain nonzero Omega as face data.

Thus a nonzero triangular defect can be part of an exactly closed tetrahedral boundary. Face defect and higher boundary closure must be calculated together, not each independently set to zero.

## 2. Exact specialization to the F736 patch

Use the actual geometrically ordered vertices:

    T324: (V104,V105,V111,V113),
    T325: (V104,V110,V111,V113).

Write D_ID for the actual map on the named edge and Omega_ID for its triangular discrepancy. Their definitions are

    Omega736 = D515 - D539 D514,

    Omega731 = D514 - D519 D511,
    Omega732 = D515 - D521 D511,
    Omega745 = D521 - D539 D519,

    Omega734 = D514 - D535 D513,
    Omega735 = D515 - D536 D513,
    Omega760 = D536 - D539 D535.

Every expression must be typed between the actual indicated vertex carriers. Substitute into (B):

    Omega736 - Omega732
      + D539 Omega731 - Omega745 D511 = 0,          [T324]

    Omega736 - Omega735
      + D539 Omega734 - Omega760 D513 = 0.          [T325]

Equivalently,

    Omega732 + Omega745 D511
      = Omega736 + D539 Omega731,

    Omega735 + Omega760 D513
      = Omega736 + D539 Omega734.

These are the ADDITIVE defect-boundary versions of the two previously recorded face-modification pasting equations. They do not identify vertical composition of arbitrary modifications with scalar addition unless that additive model is explicitly supplied.

## 3. Bottom and shared-face calculation are coupled explicitly

Where the actual edge D511 is an admitted equivalence on its image, its bottom defect is forced by

    Omega745
      =(Omega736-Omega732+D539 Omega731) D511_inverse.

Likewise, where D513 has the required admitted inverse,

    Omega760
      =(Omega736-Omega735+D539 Omega734) D513_inverse.

The inverse/domain hypotheses are essential; they cannot be supplied by inverting a scalar trace. Without them, retain the whiskered equations instead of asserting a unique unwhiskered bottom.

The same Omega736 occurs in both equations, because F736 is literally a shared face with the same D514,D539,D515 boundary. This is the exact algebraic constraint needed when calculating both bottom/filler pairs together.

## 4. Why strict word maps do not identify the finite analytical remainder

For the v17 source-transported maps T_uv=I_v r_u,

    T_vz T_uv=T_uz,

so their Omega defects are identically zero. The candidate carrier simultaneously retains the actual finite scalar cutoff remainder E_Lambda, which is not assumed zero.

Therefore it is not legitimate simply to write

    Omega736=E_Lambda

for those strict maps without specifying a different enhancement, boundary operation or realization comparison. Their types differ as well: Omega736 is an operator between vertex carriers, whereas the v16 E_Lambda is an observer-indexed scalar functional/family.

A witness comparison must say how the analytical H234 representative is realized as a modification over the chart triangle, or how it maps to an operator defect in an actual output realization. Equal scalar evaluations on the source do not supply that type conversion.

This is an exact description of the remaining mismatch, not a claim that the inherited analytical modification is unavailable or that no enhancement can realize it.

## 5. Which calculation can legitimately be performed next

Two well-typed routes are visible in prior research:

### Source-retaining modification route

Keep the strict chart edges, but define/use a realization target whose 2-cells retain the actual cutoff/spectral comparison and finite representative. Supply the boundary identification, then use the inverse-compositor mate and paired Missing123 constructors. Do not call the zero Omega itself the regulator-dependent witness.

### Actual output-defect route

Supply the independently defined D511,D519,D514,D539,D521,D515 and the analogous T325 maps on their actual graph domains. Compute the Omega expressions above. Then compute the two bottom defects and the full tetrahedral boundary in the SAME operator target, including any source-to-defect map from the inherited analytical H234 representative.

The equations (B) hold algebraically once these composites are genuinely typed; they do not manufacture the D maps or a primitive in an unrelated DG complex. In particular a closed defect boundary does not automatically construct an independently specified higher homotopy or positive feature lift.

The native interface U_NE that crosses F736 is not automatically any of the triangle's D514,D539,D515 arrows. The prior face-identification and readout-covariance tests explicitly distinguish those roles.

## 6. Scalar and full-boundary evidence are different

The Aspect permutohedron note emphasizes that products of projected scalar matrix elements are not matrix elements of a product of full transports. Its Bianchi fixture concerns reconstructed full operators, with physical tomography not performed.

For the present task this is a useful guard: physical readout covariance, one scalar error or endpoint matching cannot replace the full typed boundary maps and their transported defect data. It does not add a new physical measurement requirement to the mathematical carrier construction.

## Refined disposition

Prior research already supplies a concrete tetrahedral defect calculus, not only generic horn or mate vocabulary. On the actual F736 incidence it yields the two exact coupled equations displayed above.

The next construction must choose the modification enhancement of strict source charts or actual output-defect maps, and identify the inherited analytical remainder at that type. Both choices preserve one shared F736 witness and require the two bottoms/higher comparisons to agree with it.

The direct operator identity is a useful partial boundary calculation. It is not a completed native analytical filler, an assumption that every fixed surface fills, or a positivity theorem. No tests, formal builds or source mutations beyond this record were performed.

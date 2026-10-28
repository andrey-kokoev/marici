# F736: the specific arrow correspondence, without convolution execution

## The two diagrams being compared

There are two different directions in the existing retained grid:

1. Horizontal: three fine edges between observer-word presentations.
2. Vertical: the actual native NE transfer from context5 to context15.

NE is not one of the three horizontal edges. Convolution is an observer operation on the source, not the NE transfer. The v30 norm obstruction concerned an added convolution-as-native-execution requirement and does not obstruct this fixed-observer comparison.

This note leaves the net unchanged.

## 1. Exact horizontal table

The following orientation is the retained refinement orientation in `results/f736-correlated-word-edges/realization.json`, not the reverse geometric orientation.

| Fine edge | Source word | Target word | Changed occurrences | Existing coordinate formula |
|---|---|---|---|---|
| E539 | V113=(1,1,1,1,1,2,4) | V111=(1,1,1,1,1,3,4) | occurrence5:2->3 | S3 R2 at occurrence5 |
| E514 | V111=(1,1,1,1,1,3,4) | V104=(1,1,1,1,2,4,4) | occurrence4:1->2; occurrence5:3->4 | S2 R1 at occurrence4; S4 R3 at occurrence5 |
| E515 | V113=(1,1,1,1,1,2,4) | V104=(1,1,1,1,2,4,4) | occurrence4:1->2; occurrence5:2->4 | S2 R1 at occurrence4; S4 R2 at occurrence5 |

Thus the horizontal composite is E514 after E539. At occurrence5 its parent comparison is eta34 after eta23 versus eta24. Occurrence4 and adjacent occurrence links also belong to the full face.

For the carrier realization, all arrows are the already defined source-preserving maps

    H_e(x,I_u(Phi_c x))=(x,I_v(Phi_c x)).

These maps transport a representation of the same observer. They do not apply convolution to that observer.

## 2. What corresponding means for each parent arrow

The parent arrows are natural comparisons of Hermitian-form presentations. Their candidate fine-edge coordinate formulas act on factorization/source-coordinate charts. The following checks distinguish those roles.

### eta23 versus the occurrence5 part of E539

- Parent role: geometric-to-compatible-spectral presentation comparison.
- Candidate underlying coordinate map: A_h -> (Omega_plus h,Omega_minus h), using source recovery R2.
- Available: the represented source inverse and compatible spectral chart on their admitted common domain.
- Remaining: identify this coordinate map, its form comparison and the actual factorization records with the parent eta23 component on that domain.

### eta34 versus the occurrence5 part of E514

- Parent role: differentiated spectral/connection presentation versus the finite-part trace presentation, including its local distribution and endpoint convention.
- Candidate underlying coordinate map: compatible spectral data -> R(F_phys h), using R3.
- Available: the full response coordinate, source-recovered form, and separately retained cutoff/spectral records.
- Remaining: identify the target as the intended finite-part presentation WITH those records, and identify the map as its parent spectral-to-trace comparison. The bare response tuple does not contain that arrow identification.

### eta24 versus the occurrence5 part of E515

- Parent role: the geometric cutoff-trace presentation construction.
- Candidate underlying coordinate map: A_h -> R(F_phys h), using R2.
- Available: the source recovery and full response, together with independently evaluated cutoff regularization records.
- Remaining: identify this decorated coordinate change with the parent cutoff-trace presentation comparison.

Here the finite trace is evaluated on the represented observer h, or on g*k_star for the polarized form. It is not the underlying map h->R(F_phys h), and no trace inverse is required.

For all three rows, the intended equation is an identification of presentation comparisons after the object comparisons. No equation equates a scalar functional with a vector-valued chart map.

## 3. Exact vertical comparison

The actual native operation is

    U_NE:F5 -> F15,
    Phi_c=E_packet D_c,
    Phi_15 U_NE=Phi_5.

At each word w its lift is

    N_w(x,I_w(Phi_5 x))=(U_NE x,I_w(Phi_5 x)).

Both orders around each mixed square send (x,I_u(Phi_5 x)) to

    (U_NE x,I_v(Phi_5 x)).

This is the available native comparison. For paired observations the same equation holds for both source labels. There is no demand that the five-packet source be closed under every convolution or that NE execute a convolution.

## 4. Existing parent records can already be pulled back as records

Let B(h) denote the complete admitted parent boundary/cell/regularization record evaluated at its source label; use B(g,k) where the presentation is pair-indexed. Define

    B_c(x)=B(Phi_c x)

or B_c(x,y)=B(Phi_c x,Phi_c y). Then

    B_15(U_NE x)=B_5(x)

with the analogous pair identity. Every supplied parent pasting equation remains true after this substitution. The source cell itself is retained, not reconstructed from its scalar representative.

This is a pointwise pullback of the supplied package. It does not claim an action of all source observer morphisms on F_c, nor that a newly defined native higher-cell category has been independently identified. At fixed observer/packet strength, this record transport already follows from the actual decoder equation.

The remaining horizontal problem is that B(h) has parent presentation-arrow boundaries, whereas the implemented H_e have carrier/word-map boundaries. Rows 2 above state the required identification. Once that identification preserves pasting, source coherence can be transported with it.

## 5. What the inspected native face record actually provides

The realization artifact records F736 with two local contexts:

- T324, registry esd7:5,4,5, role H134;
- T325, registry esd7:4,5,5, role H134.

Both have the prototype description `regulator-transport face with Hermitian and skew placement coordinates`. The artifact explicitly has

    comparisonDischarged=false,
    homotopyInstalled=false.

These are registry roles and a prototype specification, not two supplied native H134 inhabitants against which a transported face can already be checked. In these inspected artifacts, there is therefore no second concrete H134 formula with which to form a difference or test equality. This is a bounded inspection result, not a claim that no other repository source could supply one.

The construction task is to instantiate the required presentation-level face on the declared edge carriers, preserving the prototype's regulator/placement requirements, and use it consistently in both contexts. It should not demand agreement with an imagined already implemented native modification.

## 6. Bounded outcome and next calculation

The current evidence establishes:

- the exact fine-edge/parent-occurrence matching;
- source-preserving carrier maps for those edges;
- actual NE compatibility at unchanged observer;
- pullback transport of the existing parent record as a record.

The unprovided datum is the presentation-level comparison in rows eta23/eta34/eta24, particularly the Q4 target retaining the actual finite-part form and cutoff record alongside the response chart. The missing native face is currently specified by its boundary and prototype, not by an independent explicit formula.

The next calculation should define this Q4 presentation on the retained carrier and give the eta24 and eta34 comparison records on it. Their source form, cutoff observation, endpoint convention and composition are the fields to check. If the intended morphisms require a feature isometry or another stronger operation, that requirement must be stated explicitly and tested separately.

Only after the forward comparison is typed can its actual inverse-adjoint mate be formed in the geometric orientation. Then use one shared face for both dependent completions. No convolution-as-native-execution condition enters this sequence.

## Sources

- `f736-correlated-word-edges-result-v1.md`;
- `results/f736-correlated-word-edges/realization.json`;
- `f736-prior-native-word-retained-comparison-grid-v25.md`;
- `f736-prior-parent-modification-signature-v20.md`;
- `f736-prior-inverse-compositor-mate-v9.md`;
- `f736-parent-native-arrow-table-attempt-v29.md`.

This is a source-linked typing calculation, not a new analytical estimate or formal build. No net status was changed.

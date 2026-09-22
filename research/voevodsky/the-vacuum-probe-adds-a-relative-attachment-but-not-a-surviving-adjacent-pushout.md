# The vacuum probe adds a relative attachment, but not a surviving adjacent pushout

## Result

For Nima's new all-vacuum cubic probe, adjoined with its source-action saturation at stage three:

1. The adjacent cubic class STILL has zero pushout into the enlarged transition kernel. The explicit old-line nullhomotopy survives.
2. The vacuum scalar attachment itself is NONZERO and independent of the retained-feature scalar attachment.
3. The new saturated vacuum module has a NONSPLIT transition to O_1. Hence the enlarged stage-three observer cannot split over O_1 either.
4. In the enlarged kernel's image/cokernel construction, the vacuum and residual readouts give two independent nonzero relative boundary classes.

Thus the new measurement supplies genuine additional degree-one attachment information, but not as a surviving pushout of the adjacent class into the whole saturated kernel. That distinction remains essential.

O_2->O_1 is unchanged and remains split. The new nonsplit map to O_1 starts at the new vacuum module (and at the enlarged stage three), not at stage two.

Inputs:
- `../nima/a-vacuum-channel-distinguishes-sources-the-residual-observer-tower-cannot-see.md`
- `the-corrected-observer-kills-the-adjacent-cubic-class-but-retains-the-full-extension.md`
- `the-lost-cubic-attachment-survives-as-a-relative-observer-boundary.md`

## 1. Objects and the declared augmentation

Let

    B=G_3, A=J_2/J_4, G=G_2,
    0 -> B --i--> A --q--> G -> 0,
    e_2:G -> B[1].

Let nu=chi D3 be the new source functional selecting the existing all-vacuum row with seams 2->4, 12->60 and 420->4620. Its support is the fixed six-event corner c_3, in retained degree zero.

Adjoin Sat(nu) to the specified corrected Omega_3 and retain it at later stages. Denote the new stage by O_3^+, with

    pi_+:O_3^+ -> O_2,
    K_+=ker(pi_+), f_+:B->K_+.

Earlier stages are not modified. All stages and maps remain the finite-support source-bimodule constructions already admitted. This is new observer information, not an invertible frame correction.

## 2. Why the adjacent pushout remains zero

The old image of G_2 in O_2 is the single line

    Q=span(Obs_2(v_2)),
    v_2=mixed(2,3) forgotten(5,7).

The previous theorem constructed an equivariant lift of this line through the corrected stage-three map. It covered the original, two-private, sixteen-private, and matched full-optimal observer extensions.

The new vacuum probe cannot disturb that lift. Every path in v_2 has one retained feature. Concatenating source contexts cannot decrease retained degree. The all-vacuum row therefore annihilates every contextual v_2, including under source-action saturation. Thus

    j_+:Q->O_3^+,
    j_+(Obs_2(v_2))=Obs_3^+(v_2)

is still a source-module section over Q. It is finite-dimensional and bounded.

Let B_+:A->O_3^+ be source evaluation and w:G->Q the old graded evaluation. Define

    H_+=B_+-j_+ w q.

Then pi_+ H_+=0 and H_+ i=f_+. Hence H_+:A->K_+ is an explicit bounded equivariant nullhomotopy on the usual extension roof. Therefore

    (f_+)_* e_2=0 in Ext1(G_2,K_+).

This vanishing is for the entire adjacent class, not just its vacuum restriction. A nonzero acquired value nu(k) does not contradict it.

## 3. The vacuum scalar attachment is nonzero

Put

    k=a_0 b_0 c_0,

where all three diamonds are forgotten. The owning source calculation gives

    nu(k)=1.

Let L_c be the one-dimensional corner module at c_3, with positive-length paths acting as zero, and let lambda_v:B->L_c be nu restricted to B. This restriction is equivariant: a positive-length context cannot fit a minimal six-event I^3 source into the detector's fixed six-event corner.

Then lambda_v[1] e_2 is NONZERO. On the finite six-event restriction, the source roof [I^3->I^2] is a bounded one-sided projective model. A nullhomotopy h:I^2->L_c would give

    lambda_v(k)=h(a_0 b_0 c_0)=a_0 h(b_0 c_0)=0,

contradicting nu(k)=1. The finite strict restriction transfers this obstruction to the completed source category, as in the residual attachment proof.

Let lambda_r be the old residual scalar functional on B and v_3 its two-feature witness. The exact values are

    lambda_v(k)=1, lambda_r(k)=0,
    lambda_v(v_3)=0, lambda_r(v_3)=d_3>0.

The same nullhomotopy obstruction applied to these two products proves that lambda_v[1]e_2 and lambda_r[1]e_2 are linearly independent degree-one morphisms G_2->L_c[1]. This is independence of two observed scalar components of the existing source attachment, not the creation of a new higher Ext degree.

## 4. A nonsplit transition intrinsic to the vacuum channel

Define the finite source module

    V=(Sat(nu))^*.

It has a canonical restriction onto O_1. Indeed, on the source ideal,

    nu(x b_0 c_0)=ell_1(x).

Only x in the initial two-event vacuum corner can contribute, and the two functionals agree there on the forgotten diamond a_0. This proves Omega_1 is contained in Sat(nu), not merely equality on one arbitrary scalar input.

At that initial corner, V is one-dimensional: the vacuum test and its contexts see only the forgotten diamond, not the mixed one. A section O_1->V would therefore have the forced value

    Obs_1(a_0) |-> Obs_V(a_0).

But O_1 is annihilated by all positive-length paths, while

    Obs_V(a_0) b_0 c_0=Obs_V(k)!=0.

This contradicts equivariance. Thus

    0 -> ker(V->O_1) -> V -> O_1 -> 0

is nonsplit.

The inclusion Sat(nu) subset Omega_3^+ gives a surjection O_3^+->V over O_1. Any section of O_3^+->O_1 would induce a section of V->O_1. Therefore the full composite O_3^+->O_1 is nonsplit as well.

This must not be confused with O_2->O_1, which has not changed. Nor does it assert that every possible prior stage-three augmentation had a split composite to O_1: the nonsplitting here is proved directly through the new vacuum module, independently of any other obstruction.

## 5. Locate the added derived information inside the enlarged kernel

Set

    L_+=im(f_+) subset K_+, C_+=K_+/L_+.

Both retained scalar functionals factor through L_+ because they are coordinates in the new observer. Write their factorizations as

    lambda_bar_v, lambda_bar_r : L_+ -> L_c.

Push out the finite exact sequence

    0 -> L_+ -> K_+ -> C_+ -> 0

along these two maps. This gives boundary classes

    chi_v, chi_r in Ext1(C_+,L_c).

The nullhomotopy H_+ descends modulo L_+ to H_bar_+:G_2->C_+. Extension naturality gives

    chi_v H_bar_+=lambda_v[1]e_2,
    chi_r H_bar_+=lambda_r[1]e_2.

Both are nonzero, and they are linearly independent: any relation between chi_v and chi_r would pull back to the impossible relation in section 3.

Before the vacuum addition, the old source evaluation annihilated k. Consequently lambda_v could not factor through the old observed graded image. The new channel makes this vacuum boundary readout available in the finite observer-internal construction. This is a precise additional derived readout, rather than an inference from frame agreement.

It still does not give an equivariant ordinary scalar map K_+->L_c extending lambda_bar_v. In fact

    f_+(k)=H_+(a_0 b_0 c_0)=a_0 H_+(b_0 c_0) in I K_+,

whereas lambda_bar_v(f_+(k))=1. Every equivariant map to L_c kills I K_+. The relative boundary, rather than a degree-zero module readout, is necessary.

## 6. Scope and verification

The new observation distinguishes genuine realizable sources as proved by its owning note. The present result additionally determines its degree-one module consequences:

- the adjacent pushout into the entire kernel stays null;
- a vacuum scalar attachment is detected;
- the vacuum module's projection to O_1 is nonsplit;
- the enlarged image/cokernel boundary has an additional independent scalar class.

No full source faithfulness, new higher associator, uniform depth bound, or experimental acquisition is inferred. The source, pairing and previous attachment classes are unchanged.

Run:

    uv run --with sympy python research/voevodsky/checkers/check_vacuum_probe_extension_class.py

The checker verifies the actual eight-term forgotten source, lower-derivative annihilation, all eight relevant right contexts for the old graded-line lift, the initial two-dimensional ideal corner, the forced vacuum-lift obstruction, and the independent vacuum/residual witness values. The bounded nullhomotopy is the explicit formula H_+=B_+-j_+wq; derived nonvanishing uses the finite source restriction, not a numerical rank extrapolation.

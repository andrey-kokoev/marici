# Whole-row calibration gains transport the filtered attachment, but internal reweighting need not

## Result

There is a coherent, source-evaluation-compatible transport of the filtered attachment under positive gains on WHOLE saturated detector families. It preserves K, M, N, L, the filtered extension class, and the intrinsic relative boundary classification. The comparison maps satisfy the cocycle identity exactly.

Positivity of calibration factors alone does NOT establish this conclusion. Diagonal calibration on a restricted coefficient task can conceal changes in the full observer's source kernel. Reweighting sectors inside an aggregated detector provides an explicit counterexample to the inference.

Thus the 270 private single-block rows, with the lower observer and other seed functionals unchanged, admit coherent gain transport. The numerical diagonal-task certificates do not by themselves prove that an arbitrary calibration variation has this whole-source property.

This distinguishes three operations:

1. refining an enclosure around a FIXED actual calibration: the actual observer has not changed;
2. changing coordinate gains on fixed detector functionals: coherent transport is proved below;
3. changing the detector functionals themselves: a source-kernel audit is required.

## 1. The precise source-kernel criterion

Work first at the fixed finite convex packet with its actual source algebra S. Let X be a common source bimodule supporting the two evaluation stages. For calibration/presentation c, write

    epsilon_(r,c):X -> E_(r,c), r=2,3,
    R_(r,c)=ker epsilon_(r,c).

Evaluations are surjective. The stages are compatible, so R_(3,c) is contained in R_(2,c), and the transition is induced by the identity on X.

There exists an isomorphism U_r(d,c) satisfying

    U_r(d,c) epsilon_(r,c)=epsilon_(r,d)

if and only if R_(r,c)=R_(r,d).

Necessity follows by applying the isomorphism to an evaluated source. Conversely, equality of kernels makes

    [x]_c |-> [x]_d

well defined and invertible. It is a source-bimodule map. Finite-dimensionality supplies boundedness. It is UNIQUE with this evaluation compatibility.

Consequently, whenever these kernels remain constant,

    U_r(e,d) U_r(d,c)=U_r(e,c),
    pi_d U_3(d,c)=U_2(d,c) pi_c.

These are exact identities, not independently selected pointwise isomorphisms. In the completed setting one also needs the admitted bounded strict quotient realizations; equality of abstract kernels alone is not a general assertion about arbitrary completed quotient topologies.

## 2. Whole-row gains imply constant saturated kernels

Let the fixed seed functionals be lambda_(r,j). Their saturation includes

    x |-> lambda_(r,j)(a x b)

for every admitted source context. Suppose calibration changes them by

    lambda_(r,j,c)=g_(r,j)(c) lambda_(r,j), g_(r,j)(c)>0,

as identities on the ENTIRE source domain, not merely on the selected cubic witness space.

Then every contextual functional in seed family j acquires the SAME gain. Its kernel is unchanged. Intersecting these kernels proves that R_(r,c) is independent of c. Redundant rows cause no problem.

In saturated readout coordinates, the comparison is diagonal:

    (U_r(d,c)y)_(j,a,b)=g_(r,j)(d)/g_(r,j)(c) * y_(j,a,b).

It restricts to an isomorphism of the actual evaluation images. Source actions are transported with the coordinates. In a chosen matrix presentation,

    action_d(s)=U_r(d,c) action_c(s) U_r(d,c)^(-1).

Holding the old action matrices fixed while multiplying state coordinates by arbitrary diagonal numbers is generally NOT a bimodule automorphism.

For finitely many seed families, these maps and inverses are bounded. In the same inherited Euclidean or maximum readout norm, their operator norms are bounded by the largest gain ratio and inverse ratio. A positive compact gain box gives a uniform bound at this fixed packet. This supplies no all-depth or all-background conditioning estimate.

## 3. Transport the actual filtration and the pushout

Put

    K_c=ker pi_c, M_c=I E_(3,c),
    L_c=I^2 E_(3,c), N_c=K_c intersect M_c.

Equivariance and transition compatibility give

    U_3 K_c=K_d, U_3 M_c=M_d,
    U_3 L_c=L_d, U_3 N_c=N_d.

Therefore U_3 restricts to an isomorphism of the inherited flags

    (K_c,N_c,L_c,0) -> (K_d,N_d,L_d,0).

Keep the source extension B->A->G fixed. Evaluation compatibility implies

    U_K(d,c) f_c=f_d.

The filtered pushout comparison is explicit:

    [k,a]_c |-> [U_K(d,c)k,a]_d.

It carries the relation (f_c(b),-i(b)) to (f_d(b),-i(b)). It preserves every filtration level, including

    F^2 P_c=(N_c direct_sum A)/graph(f_c,-i).

Hence, in the declared filtered exact category,

    tau_d=(U_K(d,c))_* tau_c.

This transports the actual extension class, not just its nonzero status. Its level-two obstruction transports as well. The underlying class remains zero under the exact forgetful functor.

For a private seed lambda_(j,c)=E_j(c) psi_j, the normalized functional is

    P_(j,c)=raw_readout_j/E_j(c).

It satisfies P_(j,d) U_3(d,c)=P_(j,c). In particular the same normalized witness has value one, and the same right-ideal image is annihilated, in every gain presentation.

## 4. Transport the relative completeness classification

The short exact sequence

    0 -> L_c -> N_c -> N_c/L_c -> 0

is carried isomorphically to its d-presentation. The properties I N=L and the proper containment N I subsetneq L are preserved by these source-bimodule isomorphisms.

For a fixed coefficient module V and alpha_c:L_c->V, set

    alpha_d=alpha_c U_L(d,c)^(-1).

Writing U_bar for the induced map N_c/L_c->N_d/L_d, naturality of pushout and pullback gives

    U_bar^* delta_d(alpha_d)=delta_c(alpha_c).

The relative pullback kernels defining the completeness theorem transport in the same diagram. Thus whole-row recalibration does not change either the filtered obstruction or the intrinsic N/L relative classification.

This does not identify the filtered class in Ext1(G,N) with a relative class in Ext1(N/L,V); these remain different classes related only by the already declared comparison maps.

## 5. Apply the sufficient condition to the 270 private rows

Each declared private row selects one fixed seam block with vacuum buffers. On any source input, not only on I^3, its projected analytical record is an exact source coefficient multiplying a fixed analytical tensor for that block. Its scalar response is therefore

    lambda_(j,c)(x)=E_j(c) psi_j(x).

The normalized coefficient functional psi_j is fixed by the source labels. Replacing the nonzero scalar E_j by another positive gain, and multiplying the complete saturation of that row consistently, satisfies section 2.

Keep O_2 unchanged and keep any other seed functionals unchanged. Those other families have gain one. This covers the fixed declared observer augmented by independently rescaled private readings, even when its readout list has linear redundancies.

It does NOT say that arbitrary physical changes in an aggregated four-sector or matched-optimal detector merely multiply that entire detector by one scalar. If several analytical blocks change relative weight, one must audit their full source functionals or acquire them separately. Checking only their values on the 270 cubic columns is insufficient.

The old lower-filtration nullhomotopy also transports when its chosen source lift is retained. Its normalization is

    c=ell_2(v_2)/ell_2(x).

Multiplying the whole old functional by a common gain leaves this ratio unchanged; freezing O_2 does so in particular. The same x then yields coherent j_new and H_new under evaluation-compatible maps. This is naturality of the CHOSEN homotopy, not a claim that no other source lift can be chosen.

## 6. Counterexample: diagonal on the graded task is not diagonal on the whole observer

Use the two actual four-event source shapes

    x_early=path(2_retained,3_forgotten) b_0,
    x_late =path(2_forgotten,3_retained) b_0,

where b_0 is the forgotten (5,7) relation. Their old two-sector coefficient vectors are respectively (1,0) and (0,1). On this full four-event corner only the uncontextualized old depth-two detector can contribute.

Consider its combined functional

    ell_(a,b)=-a * early_sector + b * late_sector,

with positive sector factors a,b. Choose (a,b)=(1,3) and (2,3). Both gaps b-a are positive. But for

    h=3 x_early+x_late

one has

    ell_(1,3)(h)=0,
    ell_(2,3)(h)=-3.

Since the remaining old saturated coordinates vanish on this full corner, the old evaluation kernels differ. By section 1 there is NO source-evaluation-compatible isomorphism between these two old observers.

On the graded witness v_2, in contrast, the common sector coefficient is one, so the observed value is simply b-a: a positive scalar changing from two to one. A one-coordinate diagonal model of that graded task sees only a gain change. It does not see the kernel change on lower-filtration sources such as h.

Thus a positive diagonal task model alone cannot justify a full filtered source comparison. If the early and late sectors were independently acquired and retained, their separate gain change would instead be invertible. Combining them first loses that conclusion.

This is an algebraic counterexample to the unrestricted inference. It is NOT a claim that these two numerical sector settings occur in the actual correlated theta-calibration family. Determining which physical parameter changes preserve the full detector kernels would require the corresponding analytical family and a new audit.

## 7. Relation to calibration-dependent source policies

The inverse-calibration policy x_i(E)=d_i/E_i proves a pointwise existence statement for a declared numerical task. It does not supply the identities of saturated functionals required by section 2.

The comparisons proved here instead satisfy

    U(d,c) epsilon_c(x)=epsilon_d(x)

for the SAME source x. Their coherence follows from source evaluation, not from selecting a feasible source separately at every parameter value.

If calibration refinement merely narrows an enclosure around the fixed actual detector, neither its source kernel nor its intrinsic filtered class changes at all. There is no physical family of changing sources or detectors to infer from successive numerical enclosures.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_calibration_transport_of_filtered_attachment.py

The exact fixture includes nontrivial left/right actions, I N=L but N I=0, an unfiltered nullhomotopy, and a nonzero level-two obstruction. Four rational gain presentations yield 16 coherent pair comparisons and 64 cocycle checks. It verifies transported actions, transitions, flags, pushout relations and normalized witness values, and checks the internal-sector kernel counterexample.

The fixture does not determine which alternative physical calibrations are realizable. The theorem's full-source gain hypothesis and the counterexample's scope are explicit.

# Cubic recalibration preserves nonsplitting but changes the source-marked observer tower

## Result

Compare the IDEAL original four-sector, two-private-row, and sixteen-private-row cubic detectors, extended by their specified response tests after D3 to the full filtered source.

1. All three still give a NONSPLIT transition O_3 -> O_2, with the first two detector stages held fixed.
2. They do NOT give the same source-compatible observer quotient at stage three. Explicit lower-filtration source elements distinguish all three saturated modules.
3. The differences descend to the previous full filtered source F_2=J_1/J_3, but are NOT already observed by the original O_2.
4. Adding precisely the source-action-saturated differences to the lower observer module produces one common augmented transition. This is a controlled enlargement of the observed lower-stage data, not an invertible frame change of the original tower.

Thus qualitative nonsplitting is robust here, while the actual source-marked extension diagrams depend on the off-cubic extension of the detector. No assertion of abstract module nonisomorphism, or of inequality of Ext classes with unidentified coefficient modules, is made.

Inputs:
- `saturated-observer-transitions-split-first-and-retain-later-filtered-extensions.md`
- `../nima/cubic-observer-frames-are-coherent-on-the-common-visible-source-quotient.md`
- `../grothendieck/private-row-redundancy-improves-cubic-norms-and-reduces-full-optimization-to-LP.md`

## 1. Freeze the extension convention

Use A=2, y=3 and gamma=1, with the actual six-prime packet (2,3,5,7,11,13). The arguments also apply wherever the displayed residual factors are positive. No rational calibration defect is included: these are the EXACT ideal coefficients.

Write lambda_o, lambda_p and lambda_16 for the three scalar source functionals. Each is obtained by applying its declared labelled response test to D3 on the full source. The retained rows have vacuum buffers; all other shapes are assigned zero. In particular this specifies an extension beyond the cubic layer instead of leaving that extension implicit.

All scalar formulas below are divided by the common positive w_seam^2. Use a linear convention, or conjugate all source coefficients consistently with the existing first-slot convention.

Let

    g_A=mu_A2-mu_A1, g_B=mu_B2-mu_B1,
    u_A=mu_A1-L, u_B=mu_B1-L,
    S=g_A g_B/(2y^2),
    S_x=-u_A(u_B+g_B)/(2y^2).

All three functionals agree on the ENTIRE two-feature cubic corner V: their values are S and S_x on its two visible basis products and zero on its other 268 products.

Each is supported at the same six-event outer corner c_3, in feature degree two. Consequently their pairwise differences kill all J_3, not just the displayed positive witness: at that corner J_3 is precisely the enumerated cubic component in the relevant feature degree, and outside that corner/degree the tests vanish. The differences therefore descend continuously to F_2=J_1/J_3.

## 2. An actual lower-filtration discrepancy

Let a be the mixed diamond in the initial (2,3) block. Following it, take the SINGLE marked path with successive events (5,7,11,13), retaining only the event 5. Define

    x=a * path(5_retained,7_forgotten,11_forgotten,13_forgotten).

This is an actual source in I. Its D1 image is nonzero, so it is not in I^2. Let x' be the same source except that the final two forgotten events are ordered (13,11).

The original four-sector coefficients on D3(x) are (1,0,1,0). Its scalar value is therefore

    lambda_o(x)=U=-g_A u_B/(2y^2)<0.

The two-private-row coefficients are (1,0), so

    lambda_p(x)=S>0.

For the sixteen-row test, only two rows contribute: either first retained seam of the initial diamond, the retained 12->60 seam, and the forgotten 420->4620 seam. With the source signs included, put

    R=S * k_(12,5) / [2(k_(12,5)+k_(12,7))].

Here k_(T,p) is the positive norm-one residual response of the actual window T->pT, as in the sixteen-row theorem. Then

    lambda_16(x)=R,  0<R<S/2.

Reversing the last two events gives the additional identities

    lambda_o(x')=lambda_p(x')=0,
    lambda_16(x')=-R.

The latter test includes the forgotten-first-13 row with its actual negative source sign. The first two tests use only forgotten-first-11 rows and cannot see x'.

Finally on the positive cubic witness v_0 all three values are S. Thus the evaluation matrix on (v_0,x,x') is

    [ S  U   0 ]
    [ S  S   0 ]
    [ S  R  -R ].

Its determinant is -R S(S-U), which is nonzero. These are three linearly independent extensions on the full source corner, despite their identical restriction to I^3.

## 3. Saturation does not remove the discrepancy

Keep the original Omega_2, and define

    Omega_3^f=Omega_2 + Sat(lambda_f), f in {o,p,16},
    O_3^f=(Omega_3^f)^*.

Sat denotes the span of the actual left/right source contexts. At the ENTIRE six-event corner c_3, a nonidentity context cannot fit into a six-event detector. The older detectors have smaller outer corners and cannot see this corner at all. Hence the c_3 component of Omega_3^f is exactly the line spanned by lambda_f restricted to I_c3.

By section 2 these three lines are distinct. Therefore the three saturated modules are distinct submodules of the source dual, and their evaluation kernels are distinct.

For example, the explicit source

    z=S x-U v_0

is in the kernel of the original saturated stage-three evaluation, but its private evaluations are

    lambda_p(z)=S(S-U)>0,
    lambda_16(z)=S(R-U)>0.

All other saturated coordinates on this full corner are multiples of the corresponding detector. Thus this is a kernel distinction for the WHOLE stage-three source evaluation, not just for one selected scalar row.

There can be no isomorphism O_3^o -> O_3^p commuting with their evaluations from the FIXED source F_3=J_1/J_4. Such an isomorphism would force equality of the evaluation kernels. The same argument, using the three independent lines, separates every pair of the three source-marked quotients.

This is the relevant obstruction to promoting cubic-layer frame coherence to the saturated tower. It does not rule out an abstract isomorphism after forgetting the source evaluation, nor does it compare Ext classes without identifying their different kernels.

## 4. Nevertheless every transition remains nonsplit

Let K_f=ker(O_3^f->O_2). The initial two-event ideal corner has dimension two, generated by its forgotten and mixed diamonds. The fixed O_2 already detects both, as proved in the transition note. Adding any of the cubic detectors cannot increase this corner dimension. Thus each map O_3^f->O_2 is an isomorphism at that initial corner.

The lift of Obs_2(a), for the initial mixed diamond a, is consequently forced to be Obs_3^f(a). Let b be the mixed (5,7) diamond followed by the forgotten (11,13) diamond. Then b belongs to I^2 and

    Obs_2(a)b=0,
    Obs_3^f(a)b=Obs_3^f(v_0)!=0.

The latter is detected by the common value S>0. An equivariant section would contradict these two equations. Thus all three transitions are nonsplit.

The same forced-lift argument shows that the pullback of each transition to F_2 is nonzero. Equivalently each retains a nonzero pushout of the FULL filtered source extension

    0 -> G_3 -> F_3 -> F_2 -> 0.

This qualitative survival depends only on the common nonzero cubic witness and the already fully observed initial corner, not on the off-layer values calculated above. It is not a statement about equality of the three resulting extension classes or their adjacent restrictions.

## 5. A common refinement over the unchanged O_2

Set

    Omega_3^cup=Omega_3^o+Omega_3^p+Omega_3^16,
    O_3^cup=(Omega_3^cup)^*.

Restriction gives canonical surjections O_3^cup->O_3^f commuting with source evaluation and with projection to O_2. With K_cup=ker(O_3^cup->O_2), each transition class is the pushout of the common class

    tau_cup in Ext1(O_2,K_cup)

along the corresponding K_cup->K_f. These are actual finite-dimensional module extension diagrams, so ordinary exact pushout comparison applies.

The maps are NOT isomorphisms: on the full corner c_3, the common observer has dimension three whereas each individual observer has dimension one. This is a coherent noninvertible comparison, not the invertible genuine-image frame transition from the fixed cubic-layer theorem.

## 6. The exact lower-stage enlargement that restores a common presentation

Define the two lower-filtration defects

    delta_p=lambda_p-lambda_o,
    delta_16=lambda_16-lambda_o,
    Delta=Sat(delta_p,delta_16).

Since the defects kill J_3 and J_3 is an ideal, every element of Delta also kills J_3. Thus Delta is a finite-dimensional source submodule of F_2^*. It is NOT contained in the old Omega_2: the defects are nonzero at c_3, where Omega_2 is zero.

Now set

    Omega_2^+=Omega_2+Delta,
    Omega_3^+=Omega_3^o+Delta.

By the exact identities lambda_p=lambda_o+delta_p and lambda_16=lambda_o+delta_16 and by saturation,

    Omega_3^+=Omega_3^p+Delta=Omega_3^16+Delta=Omega_3^cup.

Accordingly all three frames give the SAME augmented observer transition

    (Omega_3^+)^* -> (Omega_2^+)^*.

The lower enlargement is precisely the smallest source-stable enlargement containing the two displayed defects. At c_3 it adds two lower-filtration coordinates; the common upper observer has three coordinates there. This does not alter the source ideal, the pairing, or the physical outputs. It records additional lower-filtration data that the old O_2 did not observe.

This augmented transition is still nonsplit: its base is a quotient of F_2 and is therefore annihilated on the right by I^2; its initial corner is still already completely observed; and its upper stage still detects v_0. The same forced-lift proof applies.

The price of this exact common presentation is an ENLARGED base observer. It cannot be described as frame invariance of the original fixed-base tower.

## 7. Boundary and verification

The answer separates three notions:

- Equality of the cubic source functional: yes, on all 270 cubic basis products.
- Nonsplitting of the first nontrivial observer transition: invariant among these three choices.
- Equality of the source-compatible saturated extension diagram: no, unless the explicitly missing lower-filtration observations are added.

No finite-noise advantage is being claimed from synthetic frame conversion, and no calibration approximation is used in the module argument.

Run:

    uv run --with sympy python research/voevodsky/checkers/check_cubic_recalibration_tower_defect.py

The checker uses the actual ordered recorder, verifies equality on every cubic basis product, verifies the exact values on x,x',v_0 and their nonzero determinant, and checks the explicit source-kernel discrepancy. The saturation, completion, pushout and nonsplitting statements follow from the finite-support module arguments above, not from treating formal potential keys as independent analytic noise channels.

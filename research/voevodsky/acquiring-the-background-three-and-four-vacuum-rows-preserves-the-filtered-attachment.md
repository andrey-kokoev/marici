# Acquiring the background-three and four vacuum rows preserves the filtered attachment

## Result

Adjoin the actual acquired unit-vacuum rows at backgrounds 3 and 4, together with their source-action saturations, to the fixed 270-row stage-three observer. Keep O_2 unchanged.

Then:

1. The enlarged observer restricts surjectively to the old observer, compatibly with the inherited filtration.
2. Its adjacent filtered extension class lifts the old class and is NONZERO.
3. Its underlying unfiltered class is still ZERO: the old retained-feature source lift supplies a compatible nullhomotopy.
4. Exactly TWO new top-layer directions become observable, represented by k_3 and k_4. They lie in both left and right ideal images of the enlarged N.
5. Left relative completeness survives, while the right ideal image still misses exactly the old private direction.

This is a structural acquisition result for these two labelled rows. No detector is installed for the unacquired T_5 tail, and no scalar aggregation is treated as an equivariant quotient.

## 1. Define the enlargement over the same source

Let Omega be the specified old saturated stage-three detector module, with

    E=Omega^*, pi:E->O_2,
    K=ker pi, M=I E, L=I^2 E, N=K intersect M.

Let chi_A denote the selected all-vacuum D3 row at background A. Define

    Omega^+=Omega+Sat(chi_3,chi_4), E^+=(Omega^+)^*.

These are the same unit-vacuum rows used to interpret the acquired b_3 and b_4 coordinates. Saturation is required for a source observer; it is not a claim that one scalar measurement determines every saturated coordinate.

Work in the fixed global labelled source algebra, or in a common finite convex support containing all three packets. In particular the common source extension must include the new backgrounds; it is not limited to the old background-two corner. The old evaluation extends on this common source by its original finite support.

The new rows have length six and kill J_4. They therefore define a valid finite stage-three enlargement without changing the source ideal. Restriction gives

    rho:E^+ -> E, pi^+=pi rho.

Write K^+,M^+,L^+,N^+ for the analogous enlarged modules.

## 2. Restriction preserves the complete inherited flag

Surjectivity and source equivariance imply

    rho(M^+)=M, rho(L^+)=L.

Also rho(K^+)=K: any lift of k in K has pi^+=0. If n lies in N, choose a lift in M^+; its pi^+ value is pi(n)=0. Hence

    rho(N^+)=N.

Thus rho_K is a surjective, levelwise strict morphism

    (K^+,N^+,L^+,0) -> (K,N,L,0).

At finite support these are bounded finite-dimensional maps. The owning strict finite-support interpretation supplies the completed comparison. No equality of the ungraded observer dimensions is asserted.

## 3. The filtered class lifts and remains nonzero

For the common source extension

    0 -> B=G_3 -> A=J_2/J_4 -> G=G_2 -> 0,

let f^+:B->K^+ be enlarged source evaluation. It lands in L^+, and

    rho_K f^+=f.

Push out in the levelwise exact filtered category. Naturality gives

    (rho_K)_* tau^+ = tau.

The old tau is nonzero, detected on the old background-two packet by the exact level-two functor. Therefore tau^+ cannot be zero.

Equivalently, pull back the old normalized private covector:

    P_y^+=P_y rho.

Since rho(N^+ I) is contained in N I,

    P_y^+(N^+ I)=0, P_y^+(f^+(v_y))=1.

An equivariant extension A->N^+ would contradict these identities. This is the same ordinary Ext1 obstruction at filtration level two, not an inference from improved scalar precision.

Only this specified class is lifted; no general surjectivity claim about maps of Ext groups is made.

## 4. The unfiltered nullhomotopy survives

The old construction used

    x=path(2_forgotten,3_retained) b_0,
    c=ell_2(v_2)/ell_2(x),
    j_new(u)=c epsilon(x), u=Obs_2(v_2).

Every path term of x has one retained feature. Source multiplication can add features but cannot remove that retained degree. Each new vacuum row selects zero retained degree in every seam and coefficient buffer. Therefore

    chi_A(p x q)=0

for EVERY admitted context p,q and A=3,4.

The old positive-length-action annihilation of epsilon(x) consequently remains true for epsilon^+(x). Define

    j^+(u)=c epsilon^+(x).

O_2 and its calibration are unchanged, so pi^+ j^+=id_Q on Q=I O_2. The same endpoint character and action argument makes j^+ equivariant. Moreover rho j^+=j_new.

With B_ev^+:A->E^+ and the unchanged old graded evaluation w, set

    H^+=B_ev^+-j^+ w q.

Then pi^+ H^+=0 and H^+ i=f^+. Thus the underlying pushout splits, and

    rho H^+=H_new.

The filtered obstruction proves that H^+ cannot land in N^+. Acquisition adds information without removing the distinction between filtered nonvanishing and unfiltered vanishing.

## 5. Exactly two new top-layer directions

A nonzero I^3 input needs at least six events. A length-six detector can therefore see it only through zero-length contexts and at its own outer corner. Accordingly the new saturated families restrict to B through only their uncontextualized rows chi_3 and chi_4.

At each new corner, the exact audit checks all 720 minimal cubic relation products: 90 ordered pair partitions and eight retained/forgotten choices. The chosen vacuum row has coefficient one on the canonical all-forgotten product k_A and zero on the other 719 products.

The old rows have background-two outer support and annihilate k_3,k_4. The two new rows satisfy

    chi_A(k_B)=delta_(A,B), A,B in {3,4}.

Consequently

    0 -> span(epsilon^+(k_3),epsilon^+(k_4))
      -> L^+ --rho--> L -> 0

is exact. In particular dim L^+=dim L+2.

Without the old background-two vacuum line, this is 270->272. With that line already retained, it is 271->273. This counts TOP-layer directions only. The subsequent audit `the-two-acquired-vacuum-rows-add-a-canonical-split-thirty-dimensional-increment.md` computes the full saturated increment: dimension 30 with filtration dimensions (30,12,2,0), a canonical source-bimodule splitting, and zero new adjacent filtered components.

## 6. Audit both ideal images and relative completeness

Write k_A=a_A b_A c_A as its three forgotten diamonds.

The two-relation tail b_A c_A ends at 30030 A. For A=3,4 these endpoints are 90090 and 120120, outside the support of O_2, whose old four-event endpoint is 420. Therefore

    epsilon^+(b_A c_A) in N^+,
    epsilon^+(k_A) in I N^+.

For the right action, a_A b_A ends at 210 A, namely 630 or 840. Neither endpoint lies in the old O_2 packet. Thus

    epsilon^+(a_A b_A) in N^+,
    epsilon^+(k_A) in N^+ I.

The old left-tail witnesses still have zero O_2 evaluation; the old top directions remain independent and have zero values under the two new full-corner rows. They therefore lift to the same left-ideal generators in the enlargement. Together with the two new directions this proves

    I N^+=L^+.

Likewise the old right-prefix witnesses lift for every old top direction except the previously excluded private one. The two new vacuum directions are in N^+ I, while P_y^+ still excludes that old private direction. Hence

    codim_(L^+)(N^+ I)=1.

The intrinsic relative completeness theorem therefore applies to N^+, using the same hypotheses I N^+=L^+ and I V=0.

The two new top directions have DIFFERENT endpoint characters from the old scalar coefficient module. Their addition does not imply a two-dimensional increase of Ext with the old fixed background-two target V. To count their relative covectors, one must specify coefficient modules supporting those new endpoints. No such target change is hidden in the dimension statement above.

## 7. Relation to the numerical acquisition history

The endpoint-resolved constraint realization keeps the physical source fixed and treats b_3,b_4 intervals as new constraints. The present construction describes the corresponding formal source-stable enlargement when their labelled detector families are retained.

These are complementary statements:

- numerical task certificates check feasibility and positivity under acquired intervals and a prior;
- the saturated observer construction identifies newly visible source directions and transports the particular extension class.

Neither says that all saturated response coordinates have been measured, nor that an unacquired aggregate tail is a source-module coordinate. T_5 remains a prior-bounded scalar functional.

## Verification

    python research/voevodsky/checkers/check_acquired_vacuum_rows_preserve_filtered_attachment.py

The checker freshly verifies the old independent obstruction certificate; audits all 720 minimal cubic products for the new vacuum selector; checks the actual new endpoints and old-support exclusions; and verifies the eight closing contexts of the retained source lift. The all-context vacuum annihilation follows from retained-degree homogeneity, not extrapolation from those eight tests.

Artifact: `results/acquired-vacuum-rows-filtered-attachment.json`.

The levelwise strict comparison, exact pushout transport, whole ideal-image claims and completed interpretation use the proofs above and their owning finite-support results. No new physical calibration integral is required for the unit-vacuum rows.

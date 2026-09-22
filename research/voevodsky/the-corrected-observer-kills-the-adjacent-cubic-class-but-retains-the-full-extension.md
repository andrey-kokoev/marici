# The corrected observer kills the adjacent cubic class but retains the full extension

## Result

The adjacent cubic class

    e_2:G_2 -> G_3[1]

has ZERO pushout under the actual source-evaluation map

    f:G_3 -> K, K=ker(O_3^sharp -> O_2).

An explicit bounded source-equivariant nullhomotopy is constructed below. This holds for the corrected original/two-private/sixteen-private tower, and also after including Grothendieck's NEW 449-block full-optimal continuous observer and its source-action correction.

In contrast, the full filtered extension over F_2=J_1/J_3 still has nonzero pushout into K. Its restriction to G_2 vanishes. More precisely, its observed class is pulled back from an extension over a quotient of G_1.

Thus a nonzero scalar detection of the cubic witness, even by the norm-optimal observer, does not imply preservation of the adjacent cubic derived attachment in the saturated transition kernel.

Inputs:
- `saturated-observer-transitions-split-first-and-retain-later-filtered-extensions.md`
- `cubic-recalibration-preserves-nonsplitting-but-changes-the-source-marked-observer-tower.md`
- `../nima/lower-filtration-corrections-make-saturated-observer-frames-coherent.md`
- `../grothendieck/matched-private-corrections-attain-the-full-cubic-observer-norm.md`

## 1. Fix the corrected convention and the maps

Use the correction convention that leaves O_1 and O_2 unchanged and retains the cubic frame discrepancies at stage three and above. Including another ideal cubic observer means retaining its actual extension on F_3=J_1/J_4 together with its source-action saturation and the differences from the other frames. All such differences here kill J_3 by the exact all-270-column equality.

Write

    G_r=J_r/J_(r+1),
    A=J_2/J_4,
    pi:O_3^sharp -> O_2,
    K=ker(pi).

The adjacent source extension is

    0 -> G_3 --i--> A --q--> G_2 -> 0.

Let B:A->O_3^sharp be the restriction of Obs_3^sharp, and let w:G_2->O_2 be the restriction of Obs_2. Compatibility says pi B=w q. On G_3, B has image in K; denote that restriction by f.

The task is not to test f(v_3)!=0, which is already known. It is to determine whether f extends equivariantly from G_3 to A.

## 2. The old graded image is just one corner line

Let

    v_2=mixed(2,3) forgotten(5,7),
    u=Obs_2(v_2), Q=span(u).

The positive old detector has value d_2>0, so u!=0.

Every functional in Omega_2 is a context of a detector supported at two or four events. A source in I^2 has at least four events. The two-event detector and every positive-length context of the four-event detector therefore vanish on I^2. Only the uncontextualized ell_2 can contribute, at its fixed four-event corner and feature degree one.

Consequently

    image(w)=Q.

This is a one-dimensional source bimodule supported at that corner. Every positive-length source path acts as zero. The argument applies to the entire completed G_2 by finite-corner continuity, not just to the displayed witness.

## 3. The line lifts equivariantly through the corrected stage

Set u_tilde=Obs_3^sharp(v_2). We prove that it has the SAME corner action as u. Then

    j:Q -> O_3^sharp, j(u)=u_tilde

is a bounded source-bimodule map with pi j=id_Q.

For the original, two-private and sixteen-private cubic detectors, every tested row requires TWO retained features inside the first four event positions. The old witness v_2 has only ONE retained feature there. Appending later events cannot supply the missing feature inside this initial interval.

There is no contributing nonidentity left context: the source and all these detectors begin at the same fixed initial vertex. All contributing right contexts have to fill the remaining two-event (11,13) interval. Its two orders and four marking patterns give exactly eight possibilities. All nineteen distinct selected rows in the union of these three protocols vanish on D3(v_2 times context).

This also proves vanishing for their source-action saturations: subdividing the total left/right context does not change the resulting source path. Corrections are differences of these same tests. The older detectors vanish on every positive-length context of v_2 by their shorter support. Hence u_tilde is annihilated by all positive-length actions, as required.

### The new full-optimal observer requires a separate audit

Its 449 analytical blocks include memory slots. The preceding seam-only retained-feature argument is not silently applied to them.

The additional checker reconstructs the EXACT matched-private norming support: 256 crossed-image blocks, 192 correction blocks, and the reserved positive block. It then computes D3(v_2 times context) directly from marked source paths, retaining actual ordered forcing windows in memory and seam slots, for all eight possible right contexts.

Every selected analytical block is zero, BEFORE applying its norming waveform or its coefficients. Thus the full-optimal observer and all its saturated contexts also vanish there. This is an exact source-support result; it does not depend on theta approximations or the numerical enclosure of the optimal norm.

Therefore the same j exists after this observer is included in the correction family. We use its declared continuous-response-dual realization and make no claim about a smaller smooth test core or a finite acquisition implementation.

## 4. Explicit bounded nullhomotopy

Since w has image in Q, define

    H=B-j w q : A -> O_3^sharp.

Its image lies in K:

    pi H=w q-(pi j)w q=0.

All maps are bounded source-bimodule maps. On G_3 one has q i=0, so

    H i=B i=f.

This is the requested explicit nullhomotopy of the degree-minus-one map on the extension roof

    [G_3 -> A] -> K[1].

It proves

    f_* e_2=0 in Ext1(G_2,K).

No splitting of A->G_2, no projectivity of a completed ideal, and no inverse of a physical pairing is used. The only section is the finite-dimensional equivariant lift of the actually observed line Q.

The cubic witness still satisfies f(v_3)!=0. Its nonzero scalar observation is compatible with H i=f: the larger saturated target has enough source action to extend f across A. The original ideal-annihilated attachment receiver did not have this property.

## 5. Locate the nonzero full filtered class

Let tau be the observer transition class of

    0 -> K -> O_3^sharp -> O_2 -> 0.

It remains nonzero, and its pullback along Obs_2:F_2->O_2 remains nonzero, by the forced initial mixed-corner lift and the positive cubic witness. Retaining the new optimal detector does not change that proof: the original initial corner was already fully observed and the original cubic readout is still retained.

But the lifted submodule j(Q) is disjoint from K and maps isomorphically onto Q. Quotienting it gives a strict finite-dimensional extension

    0 -> K -> O_3^sharp/j(Q) -> O_2/Q -> 0.

Call its class eta. The square with the original observer transition is cartesian, so

    tau=(O_2->O_2/Q)^* eta.

In particular eta is nonzero, since otherwise tau would split.

The composite F_2->O_2->O_2/Q kills G_2 and factors through

    F_2/G_2=G_1.

Therefore the nonzero full-source observed class is pulled back from an extension over this quotient of G_1. Its nonzero value on the full F_2 and zero restriction to G_2 are now explained by an actual extension diagram, not merely by an abstract possibility in an Ext exact sequence.

This does not identify eta with the first original source attachment. Its coefficient module is the different, action-sensitive K, and its observer quotient is O_2/Q.

## 6. Corollary for the specified all-depth tower

Keep the original higher detectors and only the declared cubic frame corrections, including the optimal cubic observer if desired. Then the same mechanism shows that EVERY adjacent class has zero pushout into its observer transition kernel, although the full filtered classes remain nonzero from stage two onward.

For r>=3, all cubic corrections kill I^r, including after contexts. The image of G_r in O_r is the single old witness line: detectors of smaller depth vanish, and nontrivial contexts cannot fit a minimal 2r-event I^r source into the depth-r detector. The witness v_r has r-1 features in its first 2r events; the next original detector requires r features there. Thus its line lifts through O_(r+1) with the same corner action. Applying H=B-j w q gives zero pushout of e_r. The cases r=1 and r=2 are the previous vacuum lift and the construction above.

This corollary is specific to these retained original higher detectors and these cubic corrections. An arbitrary future higher-frame extension must have its line-lift property checked; graded functional equality alone does not establish it.

## 7. Relation to the full norm theorem

Grothendieck's new theorem settles the ideal FULL finite-background norm problem, not just a restricted residual family. Its exact optimum and its all-prime numerical enclosure are separate from this derived calculation.

Here we independently audit the combinatorial support relevant to the extension class. The result is that even the optimal continuous observer, incorporated with the required source-action corrections, does not preserve the adjacent cubic class under the map to K.

Optimizing a scalar functional on I^3 and preserving its original derived target class are distinct tasks. Neither the 449-block norming certificate nor the present nullhomotopy changes the source ideal or the already established nonzero attachment into its original receiver.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_corrected_adjacent_cubic_nullhomotopy.py
    uv run --with sympy python research/voevodsky/checkers/check_optimal_cubic_observer_line_lift.py

The first checker verifies the full minimal four-event relation-product audit, all eight right contexts against the nineteen distinct earlier cubic rows, nonzero cubic observation, and the analogous quartic support fixture.

The second rebuilds the owning analytical-shape audit and exact matched-private support, then checks all eight contexts against all 449 optimal-observer blocks. It does not rerun the expensive Acb norm enclosure; no numerical norm claim is added here.

Both pass. The completed nullhomotopy is the explicit bounded formula H=B-j w q, supported by these exhaustive finite-context checks.

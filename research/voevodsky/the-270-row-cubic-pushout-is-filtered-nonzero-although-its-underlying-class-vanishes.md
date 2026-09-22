# The 270-row cubic pushout is filtered-nonzero although its underlying class vanishes

## Result

With the inherited ideal-depth filtration retained, the 270-row adjacent cubic pushout is NONZERO in a precisely specified filtered derived category.

This is stronger than failure of the previously displayed filtered homotopy. Evaluation at filtration level two is an exact functor and sends the class to a NONZERO ordinary source-bimodule Ext1 class. Therefore no admissible filtered quasi-isomorphism or replacement can kill it.

Forgetting the filtration sends the same class to ZERO, by the explicit lower-filtration nullhomotopy already constructed. That nullhomotopy leaves the required filtration level and is not admissible as a filtered nullhomotopy.

Thus the richer acquisition protocol retains additional degree-one attachment information when its ideal-depth placement is part of the comparison. This is a new, explicitly declared categorical statement, not a reversal of the previous unfiltered result.

Inputs:
- `the-270-row-enlargement-preserves-left-relative-completeness-but-breaks-the-old-line-lift.md`
- `a-lower-filtration-lift-nullifies-the-270-row-adjacent-cubic-pushout.md`

## 1. Specify the filtered exact category

First restrict to the finite six-event convex source packet and its actual marked-path algebra S. Use finite-dimensional S-bimodules with a decreasing flag

    F^1 X=X superset F^2 X superset F^3 X superset F^4 X=0.

Morphisms preserve every level. A sequence is a conflation exactly when it is exact at EVERY level. This is the standard exact category of finite flags: viewed as diagrams of modules with injective transition maps, these objects are extension-closed in the abelian diagram category.

All maps are bounded in the finite-stage topologies. The functors X|->F^p X are exact. They therefore induce functors on bounded derived categories formed by inverting the quasi-isomorphisms for this exact structure. In particular they preserve all admissible acyclic refinements.

The same definition uses closed strict flags in the owning completed source category. The admitted finite convex restriction is bounded and exact level by level. A nonzero finite restriction therefore obstructs vanishing of the completed filtered class. No completed projective resolution is assumed.

The flags below are the actual inherited ideal-depth flags, not weights fitted to a test. They satisfy the expected left/right ideal-raising inclusions. The exact category just defined permits arbitrary finite source-module flags; it does not silently impose an additional unresolved exact structure on a smaller class of filtered objects.

## 2. Give every object its flag

Let

    B=G_3, A=J_2/J_4, G=G_2,
    0 -> B --i--> A --q--> G -> 0.

Their source flags are

    B: (B,B,B,0),
    A: (A,A,i(B),0),
    G: (G,G,0,0).

Here the entries list levels 1,2,3,4. The source extension is a conflation in the filtered category.

For the fixed 270-row observer with unchanged O_2, put

    E=O_3^270, K=ker(E->O_2),
    M=I E, L=I^2 E, N=K intersect M.

E has the flag (E,M,L,0), and K has its INHERITED flag

    K: (K,N,L,0).

These are not an identification of N with the independently defined intrinsic ideal power I K. We retain the actual subobject filtration from E.

The observed map f:B->K has image in L, so it is a filtered morphism. We can therefore push out the filtered source extension along f.

## 3. Explicit filtered pushout

Its underlying middle module is

    P_f=(K direct_sum A)/{(f(b),-i(b)):b in B}.

Its filtration is

    F^1 P_f=P_f,
    F^2 P_f=(N direct_sum A)/{(f(b),-i(b)):b in B},
    F^3 P_f=(L direct_sum B)/{(f(b),-b):b in B} ~= L,
    F^4 P_f=0.

The inclusions are actual submodule inclusions. All three levels give exact sequences, so

    0 -> K -> P_f -> G -> 0

defines a degree-one class tau_filtered in the declared filtered exact category.

At level two, it is exactly the ordinary pushout of

    0 -> B -> A -> G -> 0

along f_N:B->N. Denote that ordinary class by tau_2 in Ext1_(S-S)(G,N).

## 4. Prove the level-two class nonzero

The owning 270-row audit established

    P_y(N I)=0,
    P_y(f(v_y))=1,

where P_y is the normalized existing private coordinate for

    v_y=v_2 c_1,
    v_2=mixed(2,3) forgotten(5,7),
    c_1=mixed(11,13) in I.

Suppose tau_2 were zero. The elementary pushout splitting criterion would give a source-bimodule map

    H_2:A->N, H_2 i=f_N.

Then right equivariance forces

    f(v_y)=H_2(v_2 c_1)=H_2(v_2)c_1 in N I.

Applying P_y gives 1=0. This is impossible. Thus tau_2 is nonzero.

This proof excludes EVERY equivariant extension A->N, not only a section factoring through the old one-dimensional graded image. It uses the actual private source coefficient identity and the full audited right ideal image.

Since the level-two functor is exact,

    F^2(tau_filtered)=tau_2 !=0.

Consequently tau_filtered is nonzero in the filtered derived category. A filtered replacement making it zero would make its image under F^2 zero as well, contradicting this ordinary Ext1 obstruction.

This is the step that upgrades a chain-homotopy obstruction to derived nonvanishing without presuming a filtered projective model.

## 5. Forgetting filtration still kills the class

The previously constructed map

    H_new:A->K, H_new i=f

uses the late-retained source path and gives an unfiltered nullhomotopy. It identifies the underlying pushout with K direct_sum G through

    [k,a] |-> (k+H_new(a),q(a)).

The inverse section of the extension sends q(a) to [-H_new(a),a], which is well defined because H_new i=f.

But H_new cannot have image in N, by section 4. Therefore this section and nullhomotopy do not preserve filtration level two. The exact forgetful functor sends the nonzero filtered class to zero, just as the earlier unfiltered theorem states.

For the earlier smaller protocol, the old nullhomotopy DID land in N and restricted on B to L. It was filtration-preserving for these same depth conventions. The distinction arises from the 270-row enlargement, not from relabelling an old proof as a new category.

## 6. Locate the nontrivial filtration inside the split underlying module

Modulo N, H_new kills B. It therefore induces

    beta:G -> K/N.

Under the unfiltered splitting P_f ~= K direct_sum G from section 5, the second filtration level is exactly the graph pullback

    F^2 P_f = {(k,g): k mod N=beta(g)},
    F^3 P_f = L direct_sum 0.

Thus the underlying object is split, but its filtration is not the split direct-sum filtration.

The level-two extension is the pullback along beta of

    0 -> N -> K -> K/N -> 0.

Since tau_2 is nonzero, beta cannot lift to an equivariant map G->K. Changing the unfiltered splitting changes beta by such a lift, so this nonzero obstruction is independent of the particular displayed unfiltered splitting.

This gives a concrete description of the class: it is the obstruction to making the lower-filtration escape of H_new compatible with the retained level-two submodule.

Even the associated graded extension is split at every level: its degree-two middle term is (N/L) direct_sum G, while the other quotient levels have zero source quotient. Therefore neither the unfiltered object nor its separate graded pieces capture this attachment. The exact level-two extension retains the needed gluing information.

## 7. Refinements, frames and scope

All admissible filtered refinements remain subject to the level-two detector. The common-flag comparison theorem is compatible with this statement: it supplies coherent nullhomotopies of consecutive Yoneda PRODUCTS, not a nullhomotopy of each individual connecting class.

Admitted corrected frame isomorphisms preserve the source action and the transition map. They carry M,L,N to the corresponding modules, hence are filtered isomorphisms and preserve the class. An unrelated protocol enlargement or an uncorrected frame identification is not assumed to have that property. Coherent transport under positive gains on entire saturated detector families is proved in `whole-row-calibration-gains-transport-the-filtered-attachment-but-internal-reweighting-need-not.md`. That result also explains why diagonal calibration only on a restricted source task is insufficient: internal detector reweighting can change the full source kernel.

The optional single vacuum probe and the admitted matched-optimal scalar rows do not remove the P_y obstruction: the owning audit of N I and the separating private coordinate remains valid for the declared union. The conclusion is at the fixed finite packet with O_2 unchanged; translated or enlarged stage-two protocols require a new support audit.

No topology on all Ext groups, no acquisition guarantee, no new source ideal and no new higher Ext degree are asserted. The result is a degree-one nonvanishing statement in an explicitly declared filtered category, detected by an exact functor.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_filtered_cubic_pushout_nonvanishing.py
    uv run --with sympy python research/voevodsky/checkers/check_270_row_ideal_action_gate.py

Both pass. The first verifies a finite bimodule model of the left/right asymmetry, the unfiltered nullhomotopy, the nonsplit level-two extension and its graph filtration. The second freshly verifies the actual 270-row source identity and right-ideal obstruction used in section 4.

The decisive derived argument is exactness of F^2 plus the actual nonzero level-two extension, not extrapolation from the fixture or failure of one chosen homotopy.

The finite source obstruction now also has a portable exact certificate and a standalone standard-library verifier; see `filtered-cubic-nonvanishing-has-a-portable-source-certificate-and-independent-verifier.md`. It independently checks local relation-kernel spanning, every relevant prefix/right-action generator, the private coefficient matrix and the nonzero witness. Its stated boundary retains the physical nonvanishing and exact filtered-category hypotheses rather than silently claiming to verify them numerically.

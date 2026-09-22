# The 270-row enlargement preserves left relative completeness but breaks the old line lift

## Result

For the ACTUAL 270-private-row enlargement at the fixed six-event packet, with O_2 unchanged, the structural gate has a nontrivial answer:

    I (ker(O_3->O_2) intersect I O_3)=I^2 O_3.

Thus the left ideal-action hypothesis needed by the relative completeness theorem survives.

However, the old equivariant graded-line lift does NOT survive. Moreover the right-hand equality fails:

    (ker(O_3->O_2) intersect I O_3) I is a proper subspace of I^2 O_3.

Without the optional vacuum row, these spaces have dimensions

    dim L=270, dim(IN)=270, dim(NI)=269.

With the one specified vacuum probe, the dimensions are 271,271,270. The unique missing mixed direction on the right is

    v_y=mixed(2,3) forgotten(5,7) mixed(11,13).

This is a new proof of the left-action gate, not a transfer of the earlier line-lift argument. The old nullhomotopy formula depending on that lift must not be reused for this enlargement.

## 1. Freeze the finite protocol

Use the fixed A=2 six-event packet and exactly the 270 first-seam private rows from

`../nima/joint-cubic-kernel-survives-vacuum-addition-but-private-mixed-rows-separate.md`.

Adjoin their finite source-action saturations at stage three. Retain the previously specified cubic observers/corrections and, optionally, the single all-vacuum probe. Stage two stays the ORIGINAL O_2 supported on subcorners of the initial four-event packet (2,3,5,7).

This is not a simultaneous enlargement of O_2 by all translated four-event detectors. Such a protocol would change the support argument below and requires its own audit. Nor do the optional vacuum dimension counts refer to adjoining every possible vacuum row.

Let

    E=O_3^270, E_2=O_2, pi:E->E_2,
    K=ker(pi), M=I E, L=I^2 E, N=K intersect M.

Surjective source evaluation gives, as in the module audit,

    M=epsilon_3(J_2/J_4), L=epsilon_3(J_3/J_4).

These identities do not need the old line lift. Every private scalar factor E_j is positive; after division by its own fixed factor the 270 top-layer readouts form the identity matrix on the two-feature cubic basis. This division is used only to state coordinates, not to change the acquisition norm or assert uniform inverse conditioning.

## 2. The left ideal image is the whole top layer

Write any of the 270 minimal cubic basis products as

    v_j=a_j b_j c_j.

Its two-relation tail b_j c_j belongs to I^2. Its terminal vertex is the FULL six-event endpoint 60060. Every row in Omega_2 is supported on a subcorner of the smaller four-event packet, whose terminal vertices divide 420. Consequently

    Obs_2(b_j c_j)=0.

This is a statement about the complete saturated stage-two module, not just one scalar row: no positive path context can turn an input ending at 60060 into one ending inside that smaller packet.

Therefore epsilon_3(b_j c_j) belongs to N, and

    epsilon_3(v_j)=a_j epsilon_3(b_j c_j) belongs to I N.

The 270 images span the two-feature part of L. Conversely I N is contained in I M=L. This proves I N=L on that part.

If the vacuum probe is retained, its new top direction is the image of a_0 b_0 c_0. The same tail argument puts it in I N. All earlier cubic scalar frames have top-layer values in the span of the private coordinates and add no further top directions. Hence the equality holds on the entire declared L.

The proof uses exact typed endpoints. Seam/vacuum-buffer keys alone do not record the terminal endpoint of a vacuum buffer; ignoring that label would invalidate this support argument.

## 3. Audit the right ideal image separately

For right multiplication the relevant prefix is a_j b_j. It has four events. If its endpoint is not the old four-event endpoint 420, the old O_2 cannot see it. If its endpoint is 420, only the uncontextualized depth-two detector can contribute: a nonidentity context would exceed four events, and the lower detector kills I^2.

The complete minimal-prefix audit shows that this old functional has exactly one nonzero basis value, on

    v_2=mixed(2,3) forgotten(5,7).

Thus every cubic basis product EXCEPT v_y has a prefix whose evaluated state lies in N. Multiplying that prefix by its last relation proves that the other 269 independent mixed top directions lie in N I.

To exclude v_y itself, let P_y be its normalized private coordinate. The checker verifies on EVERY minimal I^2 prefix in the old four-event corner that

    P_y(epsilon_3(x) c_1)=ell_2(x)/d_2,

where c_1 is the mixed (11,13) diamond and d_2=ell_2(v_2)>0. This is an exact source coefficient identity, independent of numerical amplitude approximations.

A contributing element of N I must, for this row, be a four-event prefix ending at 420 times a two-event ideal element in the last diamond. Longer products exceed the fixed six-event support. The last element is a combination of the forgotten and mixed diamonds; only the mixed part can contribute to P_y. For a prefix representing a state in N, ell_2(x)=0. Therefore

    P_y(N I)=0,
    P_y(epsilon_3(v_y))=1.

It follows that N I has exactly codimension one in the mixed part of L. If the vacuum probe is present, its top direction is in N I as well: its forgotten two-relation prefix has zero old retained-feature observation. This gives the stated dimensions 269/270 and 270/271.

The left and right ideal actions need not give identical images on N. The equality I E=E I for the whole source-quotient observer does not imply I N=N I for this submodule.

## 4. The old line cannot lift into M

Let Q=I E_2, the old one-dimensional graded witness line, and u=Obs_2(v_2). Suppose there were an equivariant section

    j:Q->M, pi j=id_Q.

Vertex equivariance puts j(u) in the old four-event corner. Represent it by x in that I^2 corner. The section condition gives ell_2(x)=d_2. By the identity in section 3,

    P_y(j(u)c_1)=1.

But Q is annihilated by positive-length paths, so equivariance requires

    j(u)c_1=j(u c_1)=0.

Contradiction. This proves failure of the actual graded-line-lift hypothesis, not merely failure of its previous chosen witness representative.

It also follows abstractly from the asymmetry: such a section would give a bimodule projection M->N equal to the identity on L and force BOTH I N=L and N I=L, contrary to section 3.

## 5. What still extends: relative completeness

The relative classification needs only

    I N=L and I V=0.

It does not require N I=L or an equivariant section Q->M. Therefore it applies to this enlarged finite module:

    Hom_(S-S)(L,V)
      ~= ker[Ext1_(S-S)(N/L,V)->Ext1_(S-S)(N,V)].

For the scalar six-event corner module V, every top covector is equivariant. The relative kernel has dimension 270 without the extra vacuum line, or 271 with it. The independently retained normalized private coordinates, with the vacuum coordinate when present, give a basis through the boundary map.

This is algebraic completeness for that relative pullback kernel. It supplies neither a practical acquisition guarantee at the very small private amplitudes nor a dimension for the full Ext1 group.

## 6. What does NOT transfer automatically

The earlier formula

    H=source_evaluation-j w q

for an adjacent nullhomotopy requires the section j that has just been ruled out. It cannot be reused for the 270-row tower.

This audit alone does not decide whether some DIFFERENT equivariant map J_2/J_4->K extends the observed G_3 map. Such a map need not have image in N. Thus failure of the M-valued line lift alone is not a proof that the adjacent pushout has become nonzero.

Subsequent resolution: `a-lower-filtration-lift-nullifies-the-270-row-adjacent-cubic-pushout.md` constructs that alternative map explicitly. It uses an actual I-but-not-I^2 source, whose observed line lies outside M. The adjacent pushout remains zero in the declared strict source-module category; the asymmetry and failed M-valued lift proved here remain unchanged.

Similarly, identifying the new intrinsic boundary classes with pullbacks of source attachment classes would require an appropriate new comparison map G_2->N/L; the old H-based construction does not supply it here.

The audited conclusion is precise: the richer protocol passes the left ideal-action gate and relative classification, while breaking the earlier symmetric line-lift mechanism. These are distinct claims.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_270_row_ideal_action_gate.py

The checker freshly verifies the entire 270-by-270 private coefficient matrix, all 270 tail generators, all 24 minimal prefix products, the unique exceptional right-action column, and the optional vacuum direction. It explicitly gates the shorter-prefix readout by its outer endpoint.

The completed statements follow from the finite observer images and the declared source multiplication/density, not from assigning formal potential keys independent response norms.

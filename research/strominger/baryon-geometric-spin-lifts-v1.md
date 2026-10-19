# Actual affine baryon generators: metric Clifford spin lifts

Iteration6 fills the source-vector/Clifford comparison for every generator of the existing proton and neutron geometric fixtures. It does not yet fill their native36-mode coefficient or coupling squares.

## Source, centering and frame

Read `research/voevodsky/inputs/relative-proton.json` and `research/voevodsky/inputs/mode-neutron.json` directly. Write their affine generators as v->T_g v+t_g, with source metric M. The common fixed centers are c_p=(1/4,1/4,1/4) and c_n=0. Fresh checks verify T_g c+t_g=c and T_g^T M T_g=M. Thus centered displacements transform linearly; translation is not misreported as a spin rotation.

Choose an explicit positive-diagonal Cholesky frame B with B^T B=M:

    B_proton=[[2sqrt(2),sqrt(2),sqrt(2)],
              [0,sqrt(6),sqrt(6)/3],
              [0,0,4sqrt(3)/3]],
    B_neutron=diag(sqrt(3),1,1).

These are declared coordinate conventions, not a physical spin-frame selection. The whitened generator R_g=B T_g B^-1 is orthogonal, has order3 and trace0.

## Derived lift and checked square

Use the same quaternion-unit Clifford matrices E_a as the spinor packet. Set

    q0=1/2,
    q=(R32-R23,R13-R31,R21-R12)/(4q0),
    U_g=q0 I+sum_a q_a E_a.

The checker verifies U_g* U_g=I and, on every basis vector and hence every source vector,

    U_g E(Bv) U_g*=E(B T_g v), E(w)=sum_a w_a E_a.

The opposite lift -U_g satisfies the same square. Both signs are exported. Every inspected geometric generator returns after three applications, but

    U_g^3=-I, (-U_g)^3=+I.

The actual geometric return therefore does not select the spin amplitude return. A selected lift sign and its history cannot be dropped when the task retains full amplitudes/reference pairing.

| Source | Geometric group closure | Positive-scalar generator lift closure | Lifts per geometric rotation |
|---|---:|---:|---:|
| Proton, both actual generators |12|24|2|
| Neutron, actual generator |3|6|2|

The finite closures and projection multiplicities are checked exactly. The neutron opposite generator alone has order3 rather than6; the table deliberately refers to the exported positive-scalar branch. It does not assert that the source chooses that branch.

In this declared Cholesky frame, neither sign of any of the three generator lifts belongs to the earlier electron native24 matrix dictionary. This is frame-dependent, not an invariant obstruction to a shared frame. It prevents silently importing that dictionary's admission/cost policy before constructing an explicit frame/alignment comparison. Matching group size is insufficient.

## The still-missing coefficient square

The Clifford square concerns geometric vectors. The tensor-doublet extension instead uses the native36-mode line encoding K and its enlarged K_tilde. To bind a geometric request there, one must compute its actual coefficient action T_g_coefficient and test

    T_g_coefficient K=K chi_g,
    (T_g_coefficient tensor U_g) K_tilde=K_tilde (chi_g U_g),

when the source action preserves that line. A nontrivial chi_g changes the logical spin action. If the line is not preserved, a larger transported carrier is needed. Neither outcome is supplied by assigning identity to T_g_coefficient.

This turn assigns no coefficient action, discards no line phase, selects no physical lift and supplies no charge, magnetic or internal law. The spin/coupling net gate stays open. The vector-level map is a partial construction, not a renamed completion of that gate.

## Verification

    python research/strominger/checkers/check_baryon_geometric_spin_lifts.py
    python research/aspect/scc/scc.py check baryon-geometric-spin-lifts-v1
    python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1

Ten fresh exact checks pass. Receipt `research/strominger/results/baryon-geometric-spin-lifts-v1.json` exports source matrices, chosen frames/centers, both lifts and closure sizes, with current source hashes. Prerequisite pins and native stores/receipts remain unchanged; no native producer or formal proof compiler is run. No primitive-cost, physical time, coupling or mass inference is made.

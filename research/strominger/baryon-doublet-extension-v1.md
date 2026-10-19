# Explicit proton/neutron doublets: construction is not source coupling

Iteration5. Both existing rank-one native return sources admit an explicit tensor-doublet extension. This implements a candidate identified in Voevodsky's pairing note for the proton and now tests the corresponding neutron source with its actual metric. The net's spin/coupling gate remains OPEN because the required source-generator and coupling maps are still absent.

## Declared enlargement and exact recovery

Start with each source's actual N=KD, DK=1 from the rank-one extraction. Supply a new C² factor:

    K_tilde=K tensor I2, D_tilde=D tensor I2,
    D_tilde K_tilde=I2, K_tilde D_tilde=N tensor I2.
    L_tilde=L tensor I2, G_tilde=G tensor I2,
    M_tilde=M tensor I2.

The original metric is retained on the first factor. K_tilde* M_tilde K_tilde=rho I2, so the existing symbolic normalization tag rho gives normalized spinors without a field approximation. For each of the24 source electron logical rotations U, the supplied baryon spin action S_U=I36 tensor U obeys S_U K_tilde=K_tilde U and D_tilde S_U=U D_tilde.

This is a new carrier and operation dictionary, not derivation of S_U from a baryon geometric generator. The old line cannot have a complex-linear two-sided recovery of an independent doublet: any F:C²->im(K) factors as K a for a one-row a, so G F=(G K)a has rank at most one and cannot equal I2.

| Measure | Old proton | Extended proton | Old neutron | Extended neutron |
|---|---:|---:|---:|---:|
| Raw complex coordinates |36|72|36|72|
| Return rank |1|2|1|2|
| L support |108|216|432|864|
| G support |432|864|108|216|
| N support |1296|2592|1296|2592|
| Total transfers |1836|3672|1836|3672|

These are source-fixed support counts of this chosen tensor protocol, not minimal primitive cost or mass. Its normalized rank-two return fiber is S3; the earlier S1 result remains correct for the UNEXTENDED native return.

## Conditional pair and charge tests

Use the actual native electron decoder D_e and epsilon=[[0,1],[-1,0]]. The supplied logical singlet is

    B(p,e)=p^T epsilon e=p0 e1-p1 e0.
    B_raw(X,Y)=(D_tilde X)^T epsilon (D_e Y).

For both enlarged sources, expansion produces576 nonzero raw bilinear monomials. Exact decoded/raw agreement passes on declared sample pairs; U^T epsilon U=epsilon is checked as a matrix equation for all24 rotations. The actual decoder coefficients and normalizers are retained in the prerequisite receipts. Conversion from scaled raw numerators to normalized raw vectors multiplies the contraction by a common normalization factor; it does not turn the576 binary terms into ordinary one-input arrows.

A neutral scalar output requires q_left+q_right=0. Supplying q_p=+1,q_e=-1 passes. Supplying q_n=0,q_e=-1 gives output weight-1, not a neutral neutron/electron singlet. Neither the invariant spin contraction nor a particle label supplies these electromagnetic charge assignments.

Likewise neutral charge does not determine magnetic response. In the declared tensor extension, both zero magnetic operator and a supplied sigma_z action are compatible with the same stage-defect constraint on the return. The checker verifies H K_tilde=0 and H S_z K_tilde=0. Selecting a nonzero magnetic coefficient or a baryonic/internal interaction needs an independent source law, not an inference from these zero constraints.

## Exact blockers and reopening

The inspected neutron bridge binds real/complex arrows to the actual modes, native coefficients, seam projectors and conditional occupation law; it explicitly supplies no spin-doublet selection rule. Nima's existing electron spin-binding packet still lists proton source-generator spin actions as unbound. These are bounded interface findings, not a claim that the repository lacks every possible spin construction.

Required maps:

1. Actual proton geometric generator -> spin action/lift, with covariance through its real source encoding.
2. Actual neutron geometric generator -> spin action/lift, under its original metric/frame conventions.
3. Neutral neutron magnetic/internal coupling and resource law.
4. A source-supported charge representation and preparation if a physical comparison is requested.

Reopen the positive coupling claim when these maps/records are supplied; compare them with this or another explicit enlarged carrier. A change of rank, selected lift, operation availability or primitive cost must remain visible. The algebraic tensor construction alone does not close this gate.

## Verification

    python research/strominger/checkers/check_baryon_doublet_extension.py
    python research/aspect/scc/scc.py check baryon-doublet-extension-v1
    python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1

Thirteen fresh exact checks pass; receipt `research/strominger/results/baryon-doublet-extension-v1.json`. Source pins, native packets and stores are unchanged. Native producers and formal proof compilers are not run; no physical coupling, rest energy or calibrated mass is claimed. Net remains three obligations open, with conditional progress and exact blockers recorded on the spin/coupling node.

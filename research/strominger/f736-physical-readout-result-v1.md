# A source physical readout comparison across F736

Registered in revision40 before execution:
`contracts/f736-physical-readout-attempt.v1.json`.

## Physical inputs, not toy regulator matrices

Use the previously evaluated real archimedean even sector on L2(R_+,dx):

    P_Lambda=1_(0,Lambda], Q_Lambda=C P_Lambda C*,
    Z_R=P_R (R>=Lambda), Q0=J0 P_Lambda J0.

The source's corrected ordered placement is retained. In this sector
`Z_R^2 P_Lambda=P_Lambda` exactly; no regulator is commuted through an observer.
The inversion reference is the declared physical model, not a newly proved
identification with every source Hardy-reference construction.

At Lambda=2,4,8, combine the source's20 ordered off-diagonal enclosures with
its5 equal centered-diagonal enclosures. This gives75 entry enclosures in total,
not75 independent measurements or newly computed quadrature values. The common
diagonal is retained with its broad finite-part bounds; it is not set to zero.
The reference subtraction remains `2 log(Lambda) d I5` in packet coefficients,
not the encoder's observation Gram matrix.

## Orientation and both placements

The source entry T_ij multiplies `a_i conjugate(b_j)`. With pairings linear in
the first observer, the matrix in `b* M a` is therefore **M_ji=T_ij**.

    H=(M+M*)/2, K=(M-M*)/(2i), M=H+iK.

The artifact retains rational enclosures for H and for the real numerator
`S=(M-M*)/2`, so `K=-iS`. The skew diagonal is exactly zero. Off-diagonal skew
bounds use both ordered entries and their common-limit error estimates. They
are not replaced by zero merely because the limiting matrix is symmetric.
An ordered matrix-unit control detects the wrong transpose and shows that
retaining only H loses the ordered cross-observer readout. This control is an
algebra test, not substituted physical data.

## Actual native pullbacks

The identified face is F736, H134 in T325 and T324. Its native crossing is
NE5->15. Use the frozen finite-packet decoders D_5,D_15 and the actual U_NE.
Exact arithmetic verifies on all44 field inputs

    D_15 U_NE = D_5.

For every one of the25 matrix units E_ij it verifies the factored pullback square,
hence for any source packet matrix M,

    G_a(M)=D_a* M D_a,
    U_NE* G_15(M) U_NE = G_5(M).

This gives exact native covariance separately for H and K of the enclosed
physical ordered readout. The artifact retains both decoders and the source
interval matrices, without pretending the interval endpoints are exact physical
matrix entries. The decoders interpret fields through the declared finite packet;
this is not full-observer faithfulness of a44-dimensional state space.

## Result and boundary

**47 checks pass.** A bounded, one-sector physical readout comparison across the
actual native presentations of F736 is established, with no changed encoder,
regulator replacement, endpoint-only reduction or positivity inference.

Still missing: source-bound operators for E514,E539,E515 on their actual
fine-vertex presentations and the intended H134 homotopy/recovery witness.
Covariance of the physical readout between incident tetrahedral presentations
is not the triangle's two-edge-versus-direct-edge filler. The actual fine-face
comparison node therefore remains undischarged.

Next isolate that witness-level obligation using the source H134 law, keeping
finite-cutoff remainder, Hermitian/skew placements and domain assumptions
explicit. A strict-chart identity or this covariance certificate cannot erase
the finite remainder. All semilocal sectors, full Pb construction and physical
evolution remain open.

## Reproduce

```sh
python research/strominger/checkers/check_f736_physical_readout.py
```

Artifacts: `results/f736-physical-readout/readout.json` and
`results/f736-physical-readout/verification.json`.

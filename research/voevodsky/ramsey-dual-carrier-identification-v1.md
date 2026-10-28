# Canonical dual-carrier identification inside the existing joint44 candidate

Node: `T-seam-based-port-readout-binding`.

## Result

The complete reversed presentations can be identified with the canonical P/N/E bindings of the existing joint44 candidate, not merely renamed while retaining zero in the old E block. The identification preserves all five coefficient readouts, has an exact based inverse, and commutes with the reversed edge transports.

This is conditional on the prior candidate's field maps, marked port construction and five-column coupling. It does not independently derive those choices or alter native geometric admission.

## Use the actual N port map, not a fitted complement

Let U_N be the full36-coordinate map from the fresh marked-port test, and let U_bar=U_N direct-sum I8. Its full metric unitarity and square identity are checked directly.

Write P for the existing full PN field map, extended by identity on E8, and W for the existing joint NE exchange. The three canonical frames are

    F0=I, F1=P, F2=W P.

The coefficient alignment required by Q and the two native permutations is

    H=Q Pi_NE Pi_PN=[1,0,2,4,3].

Rather than choose an arbitrary isometry extending H, use

    G=P^-1 U_bar P.

This acts as H on the prepared root five-space and inherits its action on every other direction from the actual prior port map. No new39-dimensional complement fit is made. The existing E8 spectator block is retained by identity in U_bar.

For old species index i=0,1,2 (P,N,E), define

    D_i=F_(2-i) G F_i^-1.

After cancellations:

    D_P = W U_bar P,
    D_N = U_bar,
    D_E = P^-1 U_bar W.

Thus the middle carrier identification is exactly the already tested marked N-port map on the entire field, not just an agreement on the prepared columns.

## Binding, readout and inverse checks

For the unchanged canonical bindings B_i and their metric-adjoint readouts R_i:

    D_i B_i = B_(2-i) Q,
    R_(2-i) D_i = Q R_i.

All three binding equations are checked exactly. All three readout equations are checked as complete5-by44 matrix identities through metric-adjoint inverse images.

The maps are metric-unitary because they compose the existing metric-isometric candidate frames and U_bar. Since U_bar squared is identity,

    D_(2-i) D_i=I44.

The whole-field inverse and edge coherence follow by exact factor cancellation, with independent exact dense-probe regressions. For example,

    D_N W = P D_E,
    D_P P^-1 = W D_N.

These are the reverse-old-edge/forward-dual-edge comparison squares. No expansion of a huge dense radical44-by44 product is substituted for the algebraic cancellation proof.

## What becomes the native E carrier

Under D_P the original prepared P field becomes B_E Q. Its output has the saved rank2 E plus rank3 retained-baryon split, and all five coefficients recover.

The inverse image of the FULL canonical raw E8 space is explicitly constructed and isometric. It consists of:

- two directions from the original baryon contrast subspace;
- six directions from the already retained old E8 complement.

The native E RETURN doublet pulls back exactly to the PN-pulled-back N contrast plane. It does NOT pull back to the old P rank-one return. The rank-one/rank-two objection therefore does not apply to this particular contrast-conversion construction.

Erasing the old E complement leaves only rank2 rather than a full raw8 carrier and fails recovery. No additional modes or second baryon copy are introduced; the construction uses the previously declared44-coordinate retained carrier. For the five-dimensional preparation those six spectator directions are unexcited, but they remain available on the full field.

## Scope and remaining obligations

This closes the tested canonical-carrier comparison within the existing enlarged candidate. It is not an isomorphism between an isolated primitive36-coordinate P law and an isolated8-coordinate E law, or a spatial rigid symmetry.

The prior window-to-sector seed, pointed port conventions, PN completion and joint NE interaction are still model inputs. The result shows their compatibility with the complete reversal, not their unique physical/source selection.

Geometry is unchanged. Sixteen of the24 reversed P bodies inherit split old-E geometry and remain outside the unchanged forward regular-P guard. They are permitted by the already stated experimental negative-direction policy; no new forward operation was installed. Larger assemblies and global coherence are separate from this three-packet comparison.

## Verification

    python research/voevodsky/checkers/check_ramsey_dual_carrier_identification.py

Final fresh execution passes. Receipt: `results/ramsey-dual-carrier-identification-v1.json`, including the raw8 and return-doublet preimages, exact source pins and controls. The checker rejects identity root alignment and loss of the six retained spectator directions.

During implementation, a trace calculation initially tried to cast each radical diagonal entry to a rational before summation; this was corrected to sum the exact diagonal first. The final construction also uses the actual full N-port map rather than an independently chosen complement extension.

No owner sources, prior receipts, native generator rules, conjecture-net outcomes or graph admission were changed.

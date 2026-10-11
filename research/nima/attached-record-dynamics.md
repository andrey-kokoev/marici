# Restart iteration 3: the selected attachment extends to arbitrary evolving banks

## Fresh implementation boundary

Freshly read `checkers/check_four_packet_record_feedback.py`. Its update is exchange after a carrier half-turn and bank mixer. Repairing the bank mixer alone does not establish covariance of this full update.

Write x:0->2 and t in Hom(1,2) tensor Hom(0,1). Retain endpoint-relative orientations o02 and o12. Define

    U_o = E diag(o02 Ad_J, o12 L).

Under independent orthogonal endpoint frames, o02 transforms by det(Q2)det(Q0), and o12 by det(Q2)det(Q1). The compatible marked Boolean source from iteration 2 supplies both signs. They remain attachment data as the numerical bank evolves; no new edge factorization is asserted.

## Whole-state result

The sewing map satisfies C Gamma = H02 C, where H02(x)=Q2 x Q0^T. Since these are orthogonal actions, its adjoint satisfies the corresponding intertwining identity. Therefore the exchange is equivariant. The two-dimensional identity Q J Q^T=det(Q)J supplies the transformation laws for both rotated blocks. Together these prove

    U_(g.o) H_g = H_g U_o.

Exact full-matrix controls pass for all 64 combinations of I,e1,e2,J at the three endpoints. Repairing only the bank block fails on 32 of those assignments. The written intertwining argument, rather than the finite sample alone, supports the general orthogonal-frame statement for this declared representation.

All four sign choices preserve the full counting norm. They are related by endpoint frame changes, not four experimentally distinct gravitational normalizations.

## Nonfactorized evolution is not an obstruction

From the empty-bank unit-carrier preparation, the first new bank is C^T(1). Its 4-by-4 tensor flattening has rank four. It cannot be represented as a single V tensor U.

Nevertheless the attached linear update remains well-defined: neither o02 nor o12 is re-extracted from that bank. Exact transformed trajectories agree through all three permitted advances and preserve total budget. No longer fixture execution is authorized or used.

This closes the earlier narrow gap about extending the repaired mixer beyond factorized source banks. It does not prove that the full WG constructor selects this numerical update or that numerical bank evolution updates the underlying tetrahedral package.

## Time-dependent physical frames remain a separate question

A fixed-coordinate transformation conjugates the update. A changing coordinate frame instead requires

    U'_n = H_(n+1) U H_n^-1.

Replacing the attachment signs at a single time gives a same-time conjugation, which is not generally this expression. An exact middle-fiber-flip control distinguishes the two. Thus retaining two orientation signs is enough for static covariance, but does not supply an inter-time connection or physically select its transport.

A coordinate change needs only the declared comparison H_(n+1)H_n^-1; its mere existence is not a missing physical law. The physical selection question is which source-derived frame history/transport is realized, rather than whether matrices can be transformed between supplied charts.

The recovered characteristic Einstein construction already provides such a transport conditionally from a shape history and corner data. The next nonredundant comparison is to inspect that actual transport against the instantaneous bank law: determine whether it can furnish the necessary endpoint connections without identifying unrelated two-dimensional spaces by fiat. Its supplied geometry and Einstein assumptions must remain visible.

## Physical normalization

No new mass, spatial distance, action scale or source stress tensor enters this extension. Conservation and frame covariance therefore do not select G. The previous calibration/readout audit remains unchanged; sign choices cannot be relabelled as gravitational coupling constants.

## Verification

`python research/nima/checkers/check_attached_record_dynamics.py` passes. Receipt: `results/attached-record-dynamics.json`. Exact matrix covariance, four norm-preserving attachment choices, tensor-rank control, and three-advance trajectory comparisons were freshly checked. No original dynamics source, Agda proof, physical-source artifact or historical receipt was changed.

# A decorated shared-face record reconstructs every native pair coupling

## Question

Can the exact cross-sector operators be carried by a source-selected shared-face record that preserves the data lost by tangent-plane restriction?

## Construction

For proposed constituent tetrahedra Oabc and Oabd, use their common face Oab. With O at the origin, take the rational basis

    B_ab = (a, b, a cross b).

The first two coordinates span the face plane and the third records its normal component. Add a separately tagged collective scalar. The four-component record is therefore a full frame expressed relative to the face, plus the scalar needed by the independent N-stage input. It is not tangent-face data alone.

For each of the twelve directed sector pairs:

- Extract G's common-frame vector by sum_h R_h^T x_h /12, then apply B_ab^-1.
- Lift it to target slots with R_g B_ab.
- Independently extract the N scalar by u_source^dagger y/80 and lift with u_target.

Here x occupies local-input ports and y occupies aligned-input ports. The two domains are retained separately. Block-diagonal assembly gives a map from eighteen source coefficient slots through four interface components to eighteen target slots. Its product equals the original diag(G,N) coefficient block entry by entry. No coefficient was fitted or rescaled.

The full operator has rank four; both extraction and lifting have rank four. This attains the linear-interface lower bound from the previous test. Deleting the normal component or deleting the collective scalar breaks reconstruction for every directed pair.

## Frame compatibility

For face charts f and g, the interface transition is

    T_gf = diag(B_g^-1 B_f, 1).

All six identity checks, thirty-six inverse checks and 216 triple-chart cocycle checks pass exactly. These are changes of coordinates on one four-component interface. They are not compositions of the native G/N stage maps, nor a theorem about higher Cubical fillers.

## Disposition

The earlier plain-face-plane obstruction is repaired by retaining the missing normal and stage-distinct collective data. The six pair interfaces now have an explicit coefficient-preserving realization and mutually consistent frame changes.

What this does not yet construct is the complete interior subdivision with native edge and central-vertex records, or independent constituent dynamics and a mass readout. The four sectors remain the sectors of the original 1836-arrow operator. Passing to a smaller intrinsic face interface would again require proving which retained data can be discarded.

## Verification

`python research/nima/checkers/check_decorated_face_interface.py` passed via structured-command execution `structured_command_execution:e_32876_1791219649038480300_16`. Exact arithmetic is over Q(sqrt(-3)); face-frame entries are rational. Results: `results/decorated-face-interface.json`, including source digests, all twelve pair checks and the cocycle count. No publication or commit is claimed.

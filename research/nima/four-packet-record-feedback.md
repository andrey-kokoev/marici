# Four-packet record feedback: conservative return, not particle binding

## Result

An explicit adapter of the existing reversible carrier-record exchange law gives a closed system with four carrier coefficients and sixteen record coefficients. Record data that Clifford multiplication alone cannot read can return to the carrier. The full twenty-dimensional map is orthogonal, has exact order six, and has a six-dimensional fixed space.

Consequently nonzero full states persist and perturbation distances remain constant. This is neutral stability, not attraction, spatial localization or proton binding. No charge, spin, mass, baryon number or color interpretation is constructed.

The price is explicit: this is a fixed-bank feedback replacement for the previous nonlinear cycle, NOT a conservative implementation of repeated fresh outward squaring. The square can prepare the initial bank once; its preparation budget is supplied. Subsequent steps rotate and exchange that bank without overwriting it.

## Reused law and new adapter

`comparison-update-dynamics-and-energy-normalization.md`, section "Exact memory lift of the projection", already supplies a reversible exchange between a normalized carrier component and a retained record. It proves conservation of carrier-plus-record squared norm and states that closed reuse gives recurrence, not an attracting settled state.

`four-packet-cycle-prototype.md` supplies the Clifford sewing map mu: R^16 -> R^4 and the existing half-turn R=diag(1,-1,-1,1).

The new choices here are to apply the prior exchange to the Clifford sewing row space, rotate the left tensor factor before exchanging, and use the same R on the incoming carrier. These choices are explicit mathematical adapters, not owner-selected physical dynamics. The square slots are coefficient coordinates, not automatically endpoint-typed physical packets.

## Normalize the sewing port, not the state

In the orthonormal ordered basis e_i tensor e_j, each row of mu has four coefficients of magnitude one. Its rows have disjoint support. Hence

    mu mu^T = 4 I_4.

Define

    C = mu/2,  C C^T = I_4,  P = C^T C.

P is the orthogonal projection onto the four-dimensional readable record space. This constant port normalization is required by the supplied Euclidean coefficient metrics. It is NOT normalization of each evolving state to unit length. The raw old output mu(t) is 2*C(t); changing the port is a declared change of readout.

Keeping raw mu as a block of an isometry with these same metrics is impossible: t=C^T e_0 has unit norm but mu(t)=2 e_0 has norm two. A nonnegative extra record budget cannot absorb a negative deficit. Similarly the old fresh nonlinear cycle on x=2*1 produces 4*1; with an empty bank its carrier budget would jump from 4 to 16. Preserving both that unrestricted update and a positive additive closed budget is impossible.

## Derive the exchange

Decompose the bank uniquely as

    t = C^T a + k,   a=Ct,   Ck=0.

The existing component exchange generalizes directly to

    E(x,t) = (Ct, C^T x + (I-P)t).

It swaps x and a while preserving k. Therefore E^2=I and

    ||x_next||² + ||t_next||² = ||x||² + ||t||².

Exchanging without any record mixing would leave all twelve kernel directions permanently unread. Merely retaining them would not solve the feedback question.

## Rotate the bank so hidden records return

Use the existing carrier rotation R and its left-factor lift

    L = R tensor I_4.

L is orthogonal and L^2=I. In the Clifford coefficient basis,

    C L C^T = 0.

Thus L moves the readable four-dimensional record space into a four-dimensional subspace of ker C. Conversely it returns that hidden subspace to the readout port.

Apply the rotations first and the exchange second:

    x_next = C L t,
    t_next = C^T R x + (I-P)Lt.

The full update U=E diag(R,L) is orthogonal. Its inverse is diag(R,L)E. For example,

    x=0, t=L C^T e_0

has Ct=0, but one step gives x_next=e_0 and t_next=0. This is actual record-to-carrier return, not just a retained witness attached to an otherwise unchanged map.

The unilateral L need not preserve the meaning of a fresh R(x) tensor x square. After exchanges the bank is generally a sum of tensors. It must be treated as a general retained coefficient bank, not silently re-factorized or overwritten with a new square.

## Exact return and remaining invisible data

The two readable ports give the orthogonal decomposition

    a=Ct,  b=CLt,
    t=C^T a + L C^T b + k,
    Ck=CLk=0.

The residual k has dimension eight. The cycle becomes

    (x,a,b,k) -> (b,Rx,a,Lk).

After three applications, each of x,a,b is transformed by R and k by L. Since R²=L²=I, U^6=I. The checker also verifies U^n != I for 1<=n<6; individual states can have smaller periods.

The eight-dimensional residual remains unread forever under this particular schedule. We have activated four of the twelve original kernel directions, not all of them. No information is destroyed: the residual remains in the bank and contributes to its budget.

The fixed conditions are a=b=x, Rx=x, Lk=k. R has a two-dimensional +1 eigenspace. L has a four-dimensional +1 eigenspace on the residual, giving a six-dimensional full fixed space. A concrete nonzero fixed preparation is

    x=e_0, t=C^T e_0 + L C^T e_0,

with total budget three. Its amplitude is arbitrary, and it is not an attractor.

For an empty bank and x=e_0, the carrier sequence over the allowed three advances is

    e_0 -> 0 -> 0 -> e_0.

The budget is in the record bank during the two zero-carrier stages. This is persistence of the COMBINED state, not a proof of a continuously visible nonzero four-vector. Orthogonality preserves the distance between any two trajectories, so no open set can converge to one selected fixed state.

## Preparation and depth

A one-time seed t_0=R(x_0) tensor x_0 connects this experiment to the preceding square trial. Its initial budget is

    B_0=||x_0||²+||x_0||^4.

That formula accounts for the supplied prepared bank; it does not derive a budget-preserving process that creates it from x_0 alone. The zero-bank and balanced-bank preparations are also tested separately.

The retained state wrapper allows three advances and refuses a fourth, preserving all parent states. U^6=I is verified as an exact operator identity, not by bypassing the retained-history limit. No general depth-three truncation or resource-free record reset is introduced.

## Fresh verification

    python research/nima/checkers/check_four_packet_record_feedback.py

Exact Fraction checks cover the coisometry, isometric lift, record decomposition, orthogonality of the 20x20 update, inverse, order six, fixed-space dimension six, readable-record rank eight, a hidden-record return, a permanently unread control, a balanced fixed state, perturbation-distance conservation and six preparations through three retained advances.

Artifact: `results/four-packet-record-feedback.json`.

## What this resolves and what it does not

Follow-up: [four-packet-complex-response.md](four-packet-complex-response.md) extracts this same operator's exact 60/120-degree complex sectors and tests a phase-sensitive outer-factor readout. Phase alone preserves its magnitude and supplies no mass correction.

Resolved within the declared adapter: retained record feedback is possible without damping, target fitting or state renormalization; it supports bounded nonzero combined states and exact recurrence.

Not resolved: retaining repeated independent dimensional growth while exchanging a fixed bank; selecting this adapter or preparation from native packet operations; deriving a distinguished persistent object rather than a continuum of neutral states; physical localization or binding; and all proton quantum numbers and energy normalization. A sixth-order return is not evidence of proton spin or a physical 60-degree rotation.

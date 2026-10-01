# Four-packet cycle: first explicit algebraic trial

## Question and disposition

Can a four-component retained carrier, outward squaring and multiplication support a nonzero stable configuration before any proton identification is imposed?

This first trial makes those operations explicit and is mechanically executable through three retained cycles. Its four-component observable has only two real fixed points, zero and the scalar unit. The unit is unstable; a neighborhood of zero contracts to zero. Thus this trial supplies no nonzero attracting fixed point. It does **not** classify periodic or relative-periodic states, nor exclude other cycle laws. No proton has been produced.

## Reused research versus new choices

Reused:

- `clifford-retained-order-recursion.md`: the real Cl(2,0) basis 1,e1,e2,J, signed multiplication and retained order.
- `recursive-independent-family-comparison.md`: ordered parent pairs, Cartesian square slots and separate retention versus readout.
- `cayley-product-transport.md`: an active transformation must respect a specified product or explicitly transport it. Unit/norm preservation alone is insufficient.
- `proton-electron-shared-state-comparison-hypothesis.md`: four-state comparison counts are not bound-state energies or particle identifications.

New trial choices:

1. Use the existing Clifford observable algebra as the coefficient readout of four packet channels. This does not identify arbitrary endpoint-typed packets with Clifford basis vectors.
2. Use its existing signed rotor J as an active implementer: R(X)=J X J^-1. This is a half-turn on the (e1,e2) coefficient plane. It is not a selected physical angle or a rotation around a spatial identity eigenvector.
3. Form the ordered square R(X) tensor X, keeping left and right parent roles.
4. Sew by the fixed Clifford multiplication, in that order. Do not renormalize, add damping, fit a target mass, or discard the square record.

The scalar unit is fixed by R, but it is an algebraic identity, not an established spatial axis. This trial is a precise candidate interpretation to test, not a derivation of the user's dimensional-growth operation from the native packet calculus.

## Carrier and multiplication

Write the coefficient vector as x=(s,q,p,z), with

    X = s*1 + q*e1 + p*e2 + z*J.

The matrices are

    1 = [[1,0],[0,1]],  e1 = [[1,0],[0,-1]],
    e2 = [[0,1],[1,0]], J = [[0,1],[-1,0]].

For basis index a+2b representing e1^a e2^b,

    (e1^a e2^b)(e1^c e2^d)
      = (-1)^(bc) e1^(a xor c) e2^(b xor d).

This supplies an associative bilinear product with unit. Clifford multiplication is NOT automatically composition of directed packet endpoints; that would need a separate typed adapter.

## Four stages

1. **Present:** retain x and its existing history.
2. **Rotate:** r=(s,-q,-p,z), obtained from Ad_J.
3. **Outward square:** form all sixteen ordered coefficient slots t_ij=r_i*x_j. Slots live in the independent tensor carrier V tensor V. The two coefficient operands here come from the same state; the resulting pure tensor is NOT sixteen independently adjustable amplitudes.
4. **Multiply:** apply mu(t)=sum_ij t_ij e_i e_j, retaining t, r and the complete parent state alongside the four-component output.

The resulting observable map is exactly

    F(s,q,p,z) = (s²-q²-p²-z², 2pz, -2qz, 2sz).

The sixteen-dimensional tensor carrier is additional coefficient capacity, not a proof of sixteen spatial dimensions. This trial also does not identify that carrier dimension with the 2,4,8-dimensional sphere-product models of the relational experiment.

Multiplication has rank four: mu(1 tensor e_i)=e_i makes it surjective. Its kernel therefore has dimension twelve. In particular,

    mu(1 tensor 1) = mu(e1 tensor e1) = 1,

although the inputs are different retained pair records. Keeping only the final vector would erase that distinction.

## Budget test

Use the existing positive coefficient norm

    ||X||² = s²+q²+p²+z² = Tr(X^T X)/2.

Rotation preserves this norm, and the tensor-product norm gives

    ||R(X) tensor X||² = ||X||^4.

Sewing is not an isometry and has the bound

    ||F(X)|| <= sqrt(2) ||X||²,

from Frobenius submultiplicativity. Therefore if ||X_0|| < 1/sqrt(2), the subsequent norms go to zero: for r_n=sqrt(2)||X_n||, r_(n+1)<=r_n². No conserved energy or positive stationary budget follows from this map. The norm has no physical energy calibration.

## Complete real fixed-point calculation for the observable

At a fixed point,

    q=2pz,  p=-2qz,  z=2sz,
    s=s²-q²-p²-z².

The first two equations imply (1+4z²)q=0; over the reals, q=p=0. If z is nonzero, the third equation forces s=1/2, while the last requires z²=-1/4, impossible. Hence z=0 and s²=s. The only real fixed points are X=0 and X=1.

The derivative at X=1 in (s,q,p,z) coordinates is diag(2,0,0,2). More directly, the scalar ray obeys s_next=s²: any s>1 grows without bound and any 0<s<1 tends to zero. Thus the nonzero fixed point is not stable to arbitrary small coefficient perturbations. Fixing s=1 or normalizing after every step would change the dynamics and must not be inserted silently.

Even a fixed observable keeps accumulating new cycle history. No exact fixed point of the complete history-bearing packet is asserted.

## Retention limit

The prototype refuses a fourth advance. It does not run indefinitely with silently truncated ancestry. Each of the three allowed advances retains the previous state, rotated operand, all sixteen square slots, product order and output. This implements a bounded experiment, not a claim that depth-three memory closes the dynamics of a physical object.

## Verification

    python research/nima/checkers/check_four_packet_cycle.py

Fresh checks pass: basis associativity; unit and signed-generator identities; rotation as conjugation and algebra automorphism; independent 2x2 matrix multiplication; 256 exact rational cycle samples; tensor and sewing budgets; distinct pair inputs with equal outputs; five three-step retained histories; strict depth refusal; zero/unit fixed-point controls and scalar instability. The all-real fixed-point and small-norm convergence arguments are algebraic proofs above, not conclusions inferred from sampled trajectories.

Result: `results/four-packet-cycle.json`.

## Next discriminating question

Follow-up: [four-packet-record-feedback.md](four-packet-record-feedback.md) constructs a conservative fixed-bank exchange adapter with exact six-step return. It is a replacement for repeated fresh squaring, not a stabilization of the unchanged nonlinear map. It gives neutral persistence, not proton binding.

The square contains information that the four-component multiplication readout does not. This trial retains it for reconstruction but does not feed it back into the next update. A next candidate should derive a feedback/return map from existing source operations and ask whether it preserves a positive budget and admits a persistent nontrivial observable. Do not choose that map solely to manufacture stability.

Spatial localization, binding against separated constituents, a charge operator, spin representation, baryon number, color neutrality and physical mass remain undefined. Four coefficients or a persistent algebraic orbit alone would not establish a proton.

# Three consecutive two-packets generate a complex plane and half-phase lift

## Result

Start with the triangle itself, represented by three consecutive directed two-endpoint packets,

    p=(p01,p12,p20).

No fourth identity packet or distinguished reference vertex is inserted. Endpoint composability determines the cyclic successor operator C. With the declared equal counting metric on packet coefficients, C determines:

- a one-dimensional common mode;
- its two-dimensional contrast plane;
- a complex structure J on that plane;
- complex eigenmode identity projectors E±=(P∓iJ)/2;
- a short-branch half-phase operator S with S²=C and phase ±60 degrees.

There are TWO meaningful halves here: the factor 1/2 in the eigenprojectors, and half the cyclic eigenphase. Multiplying an eigenvector by 1/2 is neither operation.

The primitive supports three-step cyclic return and six-step lifted return. It does NOT support the previous suggestion that successive arity squaring 1 -> 2 -> 4 closes to identity. That suggestion belonged to a different half-turn primitive and cannot be transferred silently.

## Scope and relation to the prior experiments

This replaces the *starting point of the trial*, not all existing source definitions: the primitive is a triangle of three packets rather than an externally chosen identity plus three components. `table-fibration.md` and `arrow-history-window.md` still explain how labelled packet presentations can retain ancestry. `retained-rotor-history-clock.md` still explains why endpoint/lift return must not erase a route.

The new checker derives finite coefficient operators from triangle incidence. It does not yet replace the two-orientation half-turn ledger with a native triangle-history implementation, prove a geometric/fibration identification in Agda, or assign physical particle properties.

Equal packet weights and real scalar coefficients are explicit mathematical choices. Counting supplies a simple metric, not a derived physical energy metric. The triangle's plane below is a plane of packet coefficients, not automatically the spatial plane of an embedded triangle.

## Cyclic successor from the packets

Each packet's target is the next packet's source. In the displayed ordering,

    C(x0,x1,x2)=(x1,x2,x0),
    C = [[0,1,0],[0,0,1],[1,0,0]].

C is orthogonal in the counting metric and C³=I. Its eigenvalues are 1, omega, conjugate(omega), where

    omega=-1/2+i*sqrt(3)/2 = exp(2*pi*i/3).

Corresponding eigenvectors are (1,1,1), (1,omega,omega²) and its conjugate. Their common norm is sqrt(3) before normalization. Scaling an eigenvector by 1/2 leaves its eigenvalue unchanged and divides its squared norm by four; it does not select a half-angle or a canonical identity.

## Derive common and contrast subspaces

Set

    Q=(I+C+C²)/3,
    P=I-Q.

Q is the rank-one orthogonal projector onto the common mode span{(1,1,1)}. P is the rank-two projector onto x0+x1+x2=0. Neither singles out a triangle vertex. A normalized common vector has entries 1/sqrt(3), up to sign; its amplitude is not selected by being fixed.

Here I is the identity of the already typed coefficient space, not a separately supplied physical identity packet. Deriving an invariant mode or projector is different from creating a new labelled record.

## Intrinsic complex structure

Write A=C-C^T. Exact identities are

    A^T=-A, A²=-3P, AQ=0.

Thus

    J=A/sqrt(3),
    J²=-P, J^T J=P.

On the contrast plane, J is a quarter-turn and P is the identity. On the common mode, J vanishes. Consequently

    identity_on_plane = -J².

The cyclic order fixes J's sign. Reversing that order sends J to -J. No external imaginary amplitude, normal vector or fourth packet was chosen to construct it.

## A literal half-weight identity: eigenprojectors

On the complexification define

    E_plus  = (P-iJ)/2,
    E_minus = (P+iJ)/2.

They satisfy

    E_plus²=E_plus, E_minus²=E_minus,
    E_plus E_minus=0,
    E_plus+E_minus=P.

Each is a Hermitian rank-one projector and acts as identity on its own complex eigenline. Also

    C E_plus=omega E_plus,
    C E_minus=conjugate(omega) E_minus.

This provides a precise reading close to "identity as one-half of a complex-plane object": it is half of P minus/plus iJ, an OPERATOR, not half an eigenvector. The factor 1/2 is forced by idempotence and the decomposition into conjugate eigenmodes. The sum of both mode identities recovers the real plane identity.

These projectors are newly constructed mathematical identity operators on subspaces. They are not yet newly promoted packet identities or independently selected physical states.

## Half the phase

The cyclic eigenphase is ±120 degrees. A half-phase lift fixing the common mode is

    S = Q + P/2 + (C-C^T)/2
      = Q + P/2 + sqrt(3)*J/2.

Its eigenvalues on the two complex modes are 1/2±i*sqrt(3)/2. Exactly,

    S²=C, S^T S=I, SQ=Q.

S has rational matrix entries despite the complex spectral description:

    S=(1/3)*[[ 2, 2,-1],
             [-1, 2, 2],
             [ 2,-1, 2]].

The root equation alone is insufficient to choose it. C² is another real orthogonal square root of C that fixes the common mode; its plane phase is -120 degrees rather than +60 degrees in the chosen orientation. The short root is selected by requiring positive symmetric part: (S+S^T)/2=Q+P/2, while the alternative has Q-P/2.

This is an explicit branch rule. It is not information supplied by the eigenvalue equation alone. Reversing cyclic orientation conjugates the short root to S^T.

## Which cycle closes?

For consecutive applications of the cyclic step and its paired half-phase lift:

| Number of steps k | Cyclic endpoint C^k | Half-phase reading S^k |
|---:|---|---|
| 1 | C | S |
| 2 | C² | S²=C |
| 3 | I | Q-P: minus identity on the contrast plane |
| 6 | I | I |

This is the finite two-to-one lift of the three-cycle by the six-cycle. Calling its phases spatial angles or spin rotations would require an independent realization. A continuous winding interpretation also needs the declared short-arc interpolation rather than only the discrete endpoint permutations.

In particular, iterated squaring is different:

    S -> S²=C -> S⁴=C² -> S⁸=C -> S¹⁶=C² -> ...

For S^(2^n) to equal I, six would have to divide 2^n, which never happens. Powers of two omit the factor three. The test therefore does not confirm a three-level 1,2,4 arity closure for the triangle primitive. Directly traversing its three composable packets and recursively squaring an operation are different programs.

The returned operators also do not erase the actual ordered packet histories. A retained-history adapter must preserve the distinction between zero steps, three cyclic steps and six lifted steps even when the selected endpoint reading agrees.

## Verification

    python research/nima/checkers/check_triangle_half_phase.py

Fresh exact checks pass for packet composition and malformed-input rejection, C³=I, common and contrast projectors, complex structure, both complex eigenpairs, half-weight eigenprojectors and their identities, short and long square-root branches, common-mode amplitude freedom, all six coefficient relabellings, three/six-step return and failure of arity-four squaring closure.

Arithmetic uses rational matrices and Q(i*sqrt(3)) pairs. No approximate eigenvalue solver, measured mass, fitted angle or external package is used. Higher exponent checks are 3x3 operator calculations, not construction of a large graph or an extension of the retained-depth limit.

Artifact: `results/triangle-half-phase.json`.

## Next choice

Spectral promotion is now implemented in [record4-spectral-promotion.md](record4-spectral-promotion.md): a retained nested triangle return supplies the cyclic packet-slot operator, and its three mode projectors become fresh identity records with recoverable parent histories. Mode choice is explicit.

Follow-up: [two-triangles-shared-edge-half-phase.md](two-triangles-shared-edge-half-phase.md) couples two such triangles through a shared edge. It derives one common fixed mode and distinguishes incompatible independent updates, ordered serial actions and a synchronized subspace with explicit occurrence accounting.

The triangle now supplies a common mode, a complex plane and mode identities without a fourth seed packet. The next operation to specify is whether the desired "new identity" is the common-mode projector Q, a complex eigenline projector E±, the plane identity P=-J², or a freshly labelled retained closure record. These have different types and should not be merged by notation. Once selected, it can be connected to the existing history-window interface without discarding the cyclic path.

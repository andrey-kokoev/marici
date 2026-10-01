# Two triangle primitives sharing an edge

## Setup

Take the two three-packet primitives

    T1=(AB,BC,CA),
    T2=(BA,AD,DB).

They have four vertices, five undirected edge supports and six directed triangle occurrences. AB and BA retain different directed roles over the same shared edge. This is the diamond graph (K4 missing CD), not a filled tetrahedron.

This is also the graph shape found after one line-graph promotion of the paw in `minimal-line-graph-growth.md`. That coincidence does not identify the present cyclic coefficient update with the earlier promotion operation.

Each triangle uses the cyclic matrix C and short half-phase S derived in `triangle-half-phase-primitive.md`, with C³=I, S²=C and S⁶=I. No fourth identity packet is added to either triangle.

## Shared-edge coefficient convention

Use the five real cochain coordinates

    x=(x_AB,x_BC,x_CA,x_AD,x_DB).

The local restrictions are

    R1 x=(x_AB,x_BC,x_CA),
    R2 x=(-x_AB,x_AD,x_DB).

The minus sign is the declared oriented-cochain convention BA=-AB. It does not erase the two original packet occurrences or assert that all possible complex arrow responses must obey this convention. Each restriction obeys R_i R_i^T=I_3.

The two local triangle planes overlap rather than being independent orthogonal factors. Their embedded plane projectors P_i=R_i^T P R_i satisfy

    tr(P1 P2)=4/9,
    P1 P2 != P2 P1.

Thus composing local operations can change the result; sharing an edge is not the same as the independent tensor product of two triangle systems.

## A common identity-like mode is derived

For both local cyclic operations to fix the same cochain, each restriction must be a constant triple. This forces

    x=a*(1,1,1,-1,-1).

The common fixed space is exactly one-dimensional. Its magnitude a remains arbitrary. The two triangles' common-mode amplitudes are opposite in their chosen local orientations because they read the shared edge oppositely.

This is a shared invariant coefficient mode, not an additional vertex, an absolute scalar normalization, or a new retained identity label. Local histories can still distinguish the two constructions.

## Simultaneous independent updates do not generally glue

Let x=(0,1,0,0,0). Under local C updates:

- the left triangle proposes new AB=1;
- the right triangle proposes new AB=0 after converting BA back to AB.

Under local S updates, the proposals are 2/3 and 0. The same shared edge cannot take both values. Consequently "apply both triangle cycles simultaneously" is not a well-defined generic update without a compatibility rule, shared-edge arbitration, or duplicated independent edge variables.

The experiment tests separate protocols rather than silently choosing one.

## Protocol A: ordered full cyclic steps

Embed each local T into the five-dimensional carrier, fixing unused edge coordinates:

    T_i=I_5+R_i^T(T-I_3)R_i.

For T=C these are orthogonal signed permutations C1,C2, each of order three. They do not commute. The serial update

    G=C2 C1

has characteristic polynomial lambda^5-1 and exact order five. Thus two three-cycle operations coupled through one edge can give a five-cycle serial return. Reversing the schedule changes the operator even though its spectral type agrees.

This period belongs to the specified serial protocol. It is not a universal period forced by the diamond graph alone.

## Protocol B: ordered local short half-phase steps

For T=S the embedded S1,S2 are orthogonal and obey S_i²=C_i. However,

    U=S2 S1,
    U² != C2 C1.

Multiplying local square roots is not the square root of their product when the operations do not commute.

Exact calculation gives

    tr(U)=28/9,
    det(lambda I-U)
      =(lambda-1)*(lambda^4-(19/9)lambda^3
                     +(25/9)lambda²-(19/9)lambda+1).

U has infinite order. Proof: a finite-order rational matrix has eigenvalues that are roots of unity. Its trace is therefore both a rational number and an algebraic integer, hence an integer. The nonintegral trace 28/9 excludes finite order; this is not an inference from a finite search for repetition.

Apart from the common fixed line, the two rotation pairs have

    cos(theta_±)=(19±sqrt(109))/36,

approximately 35.1362 and 76.2451 degrees. These decimals only illustrate exact algebraic values. They are not fitted geometric or physical angles.

U preserves norm and perturbation distance. Its failure to have a common finite return does not imply instability, unbounded growth, dissipation or particle binding. Nor does it say that every initial state moves: the common fixed line remains fixed.

## Protocol C: synchronized compatible triangles

There is an exact three-dimensional synchronized subspace:

    x=(a,b,c,-b,-c)=K(a,b,c).

Then R1 K=I_3 and R2 K=-I_3. Applying the same local C or S to both triples remains compatible at every step. For full cyclic updates this condition is also necessary for compatibility through a complete cycle: the first two seam equations are

    x_BC+x_AD=0,
    x_CA+x_DB=0.

On this subspace a synchronized update is K v -> K C v or K v -> K S v, retaining period three or six respectively. This is not the serial extension C2 C1 or S2 S1.

Its conserved norm depends on what is counted. If both original triangle occurrences are retained, the metric is

    M=R1^T R1+R2^T R2=diag(2,1,1,1,1),
    K^T M K=2 I_3.

The shared edge is counted twice, once for each triangle role. This paired-occurrence budget is preserved by the synchronized C and S updates. Counting each of the five edge supports only once instead gives K^T K=diag(1,2,2), which is not preserved by C: the state K(1,0,0) has norm squared one, while K C(1,0,0) has norm squared two.

Thus synchronizing the shared edge also requires stating whether the budget belongs to retained packet occurrences or deduplicated edge supports. The same display graph does not determine that accounting choice.

## Verification

    python research/nima/checkers/check_two_triangle_half_phase.py

Fresh exact Fraction checks pass for packet closure and counts, restrictions, plane overlap, common fixed-space dimension, explicit incompatible seam proposals, noncommuting schedules, individual square-root laws, serial period five, exact characteristic polynomial and infinite-order trace obstruction, mirror synchronization, both metrics and an edge-orientation gauge-change control.

Artifact: `results/two-triangle-half-phase.json`. Higher powers are fixed-size operator identities, not new retained-history executions or a large graph expansion. No mass, spatial embedding, tetrahedral filling or physical coupling is assumed.

## Interpretation

Sharing an edge couples the two triangle-derived structures. A single shared fixed mode survives, but two independent local cycles do not automatically form one synchronized cycle. We now have explicit alternatives: serial action with order dependence, or compatible synchronized action with the paired-occurrence metric. Choosing which represents the intended packet process is the next model decision, not something to hide inside an animation or an identity label.

# Machian calculation as body → eigenlines → body

## Completed dynamics result

The [completed stability and radial-response calculation](machian-cycle-completed-calculation.md) finds two unstable shape modes in the full-update rule and proves that normalized eigenlines erase radial scale. A continuous alignment alternative preserves positive geometry in the tested deformation family. The finite source response below is an alignment construction; a gravitational force law has not been derived.

## Calculated cycle

    body B
      -> rest-of-body sources K_p
      -> source-selected eigenlines P'_p
      -> reconstructed body B'
      -> collective identity line of B'.

Inputs are four labelled seed states, the cycles (ABC) and (ADB), the counting inner product on their state records, and positive source weights. The trial response law selects the lowest eigenline on the three-dimensional contrast space. It is a specified law to test, not a fitted gravitational normalization.

## Build the first body from the seed

The two cycles generate twelve permutations. Averaging their four-state permutation matrices gives

    E=J_4/4, H=I-E.

E is the common identity line and H is the rank-three contrast projector. From the retained state labels define

    q_p=H e_p,
    P_p=(4/3) q_p q_p^T.

The four q_p sum to zero, have squared norm 3/4, and form a regular simplex in the contrast space. Their volume in the counting metric is 1/3. Coordinates in an independently supplied spatial atlas are unnecessary for this construction.

## The rest of the body selects the local line

Define the source seen at anchor p by

    K_p=sum_(q != p) w_q P_q.

At equal weights,

    sum_p P_p=(4/3)H,
    K_p=(4/3)H-P_p.

On the contrast space, K_p has eigenvalues

    1/3 along P_p,
    4/3 on the two transverse directions.

Its unique lowest eigenline is precisely the local line. Reconstructing the point by

    q'_p=P'_p e_p

returns the original body. This establishes an exact symmetric fixed point of the cycle.

The eigenvalue is a dimensionless source-response readout. A physical inertial mass or gravitational field requires a further operational identification.

## Remote-source calculation

Change the source weight of B from one to two. At each other anchor p,

    K'_p=(4/3)H + D_p,
    D_p=P_B-P_p.

The exact relation

    D_p^3=(8/9)D_p

gives contrast-space eigenvalues

    (4-2*sqrt(2))/3, 4/3, (4+2*sqrt(2))/3.

The selected eigenprojector is

    P'_p=(9/16)D_p²-(3*sqrt(2)/8)D_p.

The checker verifies symmetry, rank-one idempotence, and the eigenvalue equation over Q(sqrt(2)). The selected lines at A, C and D change. B's source excludes its own contribution, so its line stays fixed during this update.

Reconstruct the new points from P'_p e_p. The new oriented volume is

    V' = 119/768 + (7/64)*sqrt(2) > 0.

The changed source thus produces a concrete change of the assembled geometry. Re-centering its four points gives a rank-three Gram matrix whose kernel is the new body's common identity line, span(1,1,1,1).

## Stagewise geometric positivity

All source matrices remain strictly positive on the contrast space. Each is a sum of three positively weighted source projectors spanning that space.

The source stage retains a complete algebraic reconstruction of its input body. From the current K_p and weights:

    S=(sum_p K_p)/3,
    P_p=(S-K_p)/w_p,
    q_p=P_p e_p.

The eigenline stage similarly carries the new body through P'_p e_p. Both decoders use the seed labels and the current operators.

The new simplex is the image of the old one under an explicitly computed positive-determinant affine map. Its two transverse scales and its axial scale about B are positive. Consequently the affine interpolation from the original body to the new one also has positive determinant throughout.

Subdividing each boundary face into its three centroid-edge triangles gives twelve positive interior cones. Each has volume V'/12; their shared boundaries cancel exactly. This verifies the actual geometric realization and an orientation-preserving transition between the two bodies.

Removing a remote source is a negative control: the remaining two projectors give a singular local contrast metric, which fails strict three-dimensional source positivity.

## Verification and next calculation

    python research/nima/checkers/check_machian_thing_eigenline_cycle.py

Artifact: `results/machian-thing-eigenline-cycle.json`.

The calculation establishes a finite source-dependent geometric response and a symmetric cyclic fixed point. Remaining calculations are repeated-cycle stability, a source-distance/force law, physical normalization, and the full primitive-arrow cost of constructing and applying these operators. No 1836-arrow or physical mass claim is made by this experiment.

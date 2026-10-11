# Existing generator construction applied to actual retained triangle families

## Reused inputs

The checker reruns the prior fixed-Gram generator/intertwiner checker and
the actual-composition Hamiltonian/clock bridge. It uses the unchanged
registered path-family continuation and actual endpoint reader, not a
convenient circular spatial adapter or a supplied new oscillator.

For each of the ten-, sixteen- and twenty-six-word stages, O reads endpoint
counts. Let B be the old six-occurrence rotor plane and R its target reader.
Write R_B=RB and use its exact left inverse to define

    P=(R_B^T R_B)^-1 R_B^T O.

P reads the old rotor coordinates from the actual retained family. The
actual LR-RL families lie in the required endpoint sector; no fitted input
coefficients are introduced.

## Continuous generator lift

With G the diagonal history metric inherited from the existing averaging
decoder, choose the metric-minimal right inverse

    E=G^-1 P^T (P G^-1 P^T)^-1,    PE=I.

The checks also establish O E=R_B at these stages. Set N=I-EP, and reuse
the previous angular rotor generator and flow:

    A=[[0,2/sqrt(3)],[-2sqrt(3),0]],
    V(theta)=exp(theta A).

The existing projection-extension construction gives

    L=EAP,
    W(theta)=N+E V(theta) P.

Exactly:

    P L=A P,
    P W(theta)=V(theta) P,
    N W(theta)=N,
    W(-theta)W(theta)=I.

These are symbolic ALL-theta identities, not agreement only at tick endpoints.
For each actual role-difference vector x, O Nx=0, so

    O W(theta)x = R_B V(theta)Px.

This fixes the earlier swap construction's intermediate-readout failure.
The hidden coefficient component stays available, and the labelled path
records remain retained alongside the continuous realization. Within-stage
coefficient transport is not asserted to create new word records.

## Metric compatibility is a real condition

The existing decoder metric does NOT make this rotor lift an isometry.
More strongly, any G-skew lift satisfying PL=AP would require

    A C_G + C_G A^T=0,    C_G=P G^-1 P^T.

The measured C_G matrices are

    [[2,2],[2,12]], [[5,5],[5,33]], [[14,14],[14,90]],

and each fails that necessary condition. Thus merely choosing a different
right inverse cannot repair the inherited-metric mismatch.

A DECLARED rotor-compatible alternative is

    G_rot=P^T diag(3,1) P + N^T G N.

It is positive definite: x decomposes uniquely into E(Px)+Nx, and both
quadratic terms are positive on their respective components. It retains
the old hidden-sector norm and gives L^T G_rot+G_rot L=0. This is an explicit
realization metric, not a physical metric deduced from the source decoder.
It does not silently overwrite G or change occurrence counts.

## Hamiltonian and clock scope

The pulled-back quadratic Hamiltonian is

    H(x)=(Px)^T diag(3,1)(Px).

It equals 12 on the actual source-derived states and is conserved by W.
The pulled-back old symplectic form has rank TWO; hidden coordinates are
fixed parameters, not additional canonical pairs. This is a presymplectic
realization with conserved hidden data, not a claim of a nondegenerate
Hamiltonian structure on every history coordinate. The prior phase lift
adds its existing kappa constant and reads T=theta.

No new physical duration or autonomous source scheduling is introduced.

## Cross-stage distinction remains visible

For actual native copy extension F_n, the checker obtains

    P_(n+1) F_n = C P_n,

where C=V(pi/3). Thus native extension and the old clock agree under the
cyclic observer. However

    L_(n+1) F_n != F_n L_n

at the tested stage transitions. Their difference is invisible to P_(n+1).
Therefore the continuous within-stage realizations are observer-compatible,
not one proven globally coherent Hamiltonian acting on the entire growing
history carrier. Retaining histories does not require claiming that stronger
identification, and the checker records rather than suppresses its failure.

## Verification

    uv run --with sympy python research/nima/checkers/check_triangle_continuous_generator_lift.py

58 exact checks pass, including the earlier suites. All-theta identities are
symbolically verified on the three stated path-family stages. No new Agda
real-analysis theorem or arbitrary-stage completion is claimed.
Receipt: `results/triangle-continuous-generator-lift.json`.

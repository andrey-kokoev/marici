# Witnessing clock and overlap phase: different roles, compatible evolution

## Compare the actual ports

Reuse the six seed ports in the existing tensor-state exchange adapter and
the unchanged prior comparison/phase-backreaction model. Its curved metric is

    K(phi)=conjugate(G_A(phi)) tensor G_B,
    G_A(A,B)=exp(i phi),  G_B=10I+J.

At phi=0 it is exactly the bound source metric. Each selected state-port
feature remains normalized. For the ACTUAL port triangle AB,BC,CA, the
product of normalized overlaps is exactly

    <u_AB,u_BC><u_BC,u_CA><u_CA,u_AB>=exp(-i phi)/121^3.

A common metric-preserving transport or independent phase redefinition of
the three directions preserves this product. The existing fixed-port
witness/rotor construction has the constant value 1/121^3: it does not
already change those overlap data.

Consequently setting phi equal to the witnessing angle does not identify
the constructions. The products agree at 0 and 2pi but disagree at all
five intermediate tick angles. This is a same-port invariant obstruction,
not a comparison inferred from dimensions or phase notation. The prior
model's numerical square-root frame independently reproduces the exact
six-port overlaps.

## Correct the proposed phase identification

There is no need to force the two variables to coincide:

- T is the lifted witnessing CLOCK, with unit rate in the selected angular
  convention and a full-cycle increment 2pi.
- phi is a dynamical OVERLAP COORDINATE with its own conjugate momentum p.

The existing model already says dphi/dt=beta*p, not phi=t. In its unchanged
fixture phi starts at .4 and its initial rate is .07. Calling both variables
"phase" does not give them the same mathematical role.

The reuse tested here sets the prior model's dimensionless evolution
parameter to T. This is an explicit parameter attachment, not a claim that
the old action is derived from the witnessing Hamiltonian or that its field
coordinate is the witnessing angle. The current source does not provide
an independently calibrated conversion to seconds.

## Execute the existing backreaction through a whole witnessing cycle

Keep the original Hamiltonian, preparation and kappa=.3, beta=.7, mu=.2.
Advance its state continuously from T=0 to T=2pi, using the actual retained
full-turn packet's seven tick angles as checkpoints. No state reset or new
force is added when the witness returns.

At the completed witness:

    phi=-0.1240152212705491,
    p=-0.21203952266901616,
    record norm=0.36830670281930394.

The interaction has changed while the signed witness has completed its
return. This is consistent with an attached-state action rather than
identifying the entire physical fiber with the returned endpoint.

RK4 with 128 substeps per clock interval gives maximum Hamiltonian error
2.96e-10 and global phase-norm error 1.18e-10. Halving the resolution supplies
an independent refinement check. Those are numerical errors, not an exact
proof that the implementation conserves quantities to arbitrary precision;
the prior Hamiltonian identities give the analytic conservation laws.

The norm here is the prior model's global phase quantity, not newly identified
electric charge. This simultaneous curved-comparison action is not silently
substituted for the original ordered exchange schedule.

## Outcome

The failed direct phase identification is now explicit. The more appropriate
clock-to-trajectory attachment works without changing the prior model:
one retained full turn organizes a nontrivial collective state/field evolution.

What remains to identify is the source origin of the curved overlap and
coupling action—not another clock, and not a requirement that the field
coordinate itself complete exactly one revolution per witnessed cycle.
The same-port calculation explains why curvature cannot be obtained merely
by renaming the already constructed fixed-geometry rotor angle.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run --with sympy --with 'numpy>=2,<3' python research/nima/checkers/check_witness_clock_overlap_phase_bridge.py

23 exact/numerical checks pass, rerunning the retained full-turn attachment,
original seed-port exchange and old phase-backreaction fixture. Exact
statements concern port identities and the holonomy mismatch; trajectory
statements use the stated numerical refinement and error bounds.
Receipt: `results/witness-clock-overlap-phase-bridge.json`.

# Recovered source → Q → canonical coordinates and lifted clock

## What was recovered, not newly invented

The earlier rotor programme already had:

1. An active-sector intertwiner from the independent source swaps in
   `agda/RetainedComparisonSeries.agda` to Clifford adjoint actions.
2. A conditional continuous rotor and a derived Hamiltonian generator.
3. A module-compatible phase lift.
4. A history-sensitive unwrapped angular clock.

Sources: `clifford-retained-order-recursion.md`,
`retained-rotor-generator.md`, `retained-rotor-phase-transport.md`, and
`retained-rotor-history-clock.md`.

All three existing rotor/phase/clock checkers were freshly rerun and pass.
Our recent discussion should not say that no canonical pair or clock
construction existed. What remains missing is native selection, physical
calibration, and its identification with the intended rung-4 readout.

## Exact source-coordinate map

Let `v=e00`, `d=e01-e10`, and let B have columns

    v⊗v, v⊗d, d⊗v, d⊗d.

The 16-coordinate source contains this four-dimensional active sector.
Its inherited counting Gram is

    B^T B = diag(1,2,2,4).

Define `C=(B^T B)^(-1) B^T`. Then `CB=I`, and `BC` is the orthogonal
projector onto the active sector. Thus for `X=B(s,q,p,z)`,

    (s,q,p,z)=CX,
    Q=sI+q e1+p e2+zJ.

In zero-based tensor-array coordinates:

    s = X0,
    q = (X1-X2)/2,
    p = (X4-X8)/2,
    z = (X5-X6-X9+X10)/4.

For arbitrary X, these read the active projection; they do not encode the
remaining twelve coordinates. The full retained source must not be discarded.
The checker parses the actual source swap codes and verifies their action
on B against both Clifford adjoint involutions.

## Dynamics and the metric distinction

The DECLARED rotor `U(theta)=cos(theta)I+sin(theta)J` yields

    D(Q)=[J,Q],   q'=2p,   p'=-2q,   s'=z'=0.

The previous Clifford reversion metric supplies
`Omega=dq∧dp-ds∧dz` and `H=q²+p²+C`.

The new audit also keeps the actual source counting metric visible. Its
restriction to the active q,p plane is `2I`. With the declared oriented
quarter-turn J this supplies

    Omega_count=2 dq∧dp,
    H_count=2(q²+p²),

up to an additive constant. A canonical coordinate choice is

    q_c=q,  p_c=2p,
    Omega_count=dq_c∧dp_c,
    H_count=2q_c²+p_c²/2.

The resulting equations reproduce the SAME angular flow. This is a
normalization-sensitive identification, not an independently derived action
unit. The pulled-back active form on all 16 source coordinates has rank two
and a 14-dimensional radical; it is not a nondegenerate form on the whole
source. The two discrete source involutions reverse the form.

The full counting Gram still differs from the Clifford coefficient metric.
No isometric identification of the full four-dimensional sector is asserted.
Nor do we silently replace the previously constructed phase/contact model
with this rescaled Hamiltonian: constructing a correspondingly rescaled
phase lift would be another obligation.

## Clock recovered from the existing phase branch

For the previously declared Clifford phase model,

    F=(qp+sz)/2,
    T=F/kappa-phi=-psi.

Its already constructed lifted action has

    phi' = phi + (F(Q')-F(Q))/kappa - theta,

so `T'=T+theta`. This is a derived angular reading WITHIN that model.
An entire 2pi rotation returns both the algebra observable and signed matrix
to their starting values but advances T by 2pi. Therefore it is not a
function of Q or the matrix endpoint alone. The phase path, starting lift,
orientation and winding choices matter. Physical seconds are not supplied.

## Where this reconnects—and where it does not

The recovered chain is

    source active sector → Clifford Q → canonical active plane
        → specified rotor/phase lift → unwrapped angular clock.

The missing bridge to the tower is now sharper: identify the rung-4 object
and its transport map with this particular active sector, preserving the
source swap action and whichever metric/phase normalization is intended.
Neither the 137-row comparison fixture nor the ancestry-coordinate fixture
has been identified with B merely because it has a four-component readout.

A literal separate uppercase P from the remembered `Q,P,T → q,p,t` notation
has not been located in this chain. Here Q is algebra-valued, p is one of
its coefficients, and T is a lifted phase-frame reading. This is not evidence
that the remembered construction does not exist elsewhere.

## Fresh verification

    uv run --with sympy python research/nima/checkers/check_retained_rotor_generator.py
    uv run --with sympy python research/nima/checkers/check_retained_rotor_phase_transport.py
    uv run --with sympy python research/nima/checkers/check_retained_rotor_history_clock.py
    uv run --with sympy python research/nima/checkers/check_source_rotor_coordinate_trace.py

The new trace passes 20 exact/symbolic checks. Result:
`results/source-rotor-coordinate-trace.json`. These are symbolic Python
checks, not a new Agda proof or a physical identification theorem.

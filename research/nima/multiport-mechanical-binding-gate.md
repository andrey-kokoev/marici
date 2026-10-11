# A per-port elastic readout does not supply one global scalar-body model

## Frozen candidate

Test the next physical identification, rather than choosing another mass basis
independently for each event: one scalar carrier body of mass M, six scalar
partner bodies of positive masses m_i, ordinary elastic collisions at the
six bound seed ports, and ONE metric-preserving linear realization valid
for all events. Inactive spectator coordinates are allowed. This is a test
of the declared port adapter, not of every possible WG realization.

## A simultaneous invariant

The established exchange reflections have unit normals with Gram

    C_ij=(delta_ij+f_i^T H f_j)/2.

All six normals are independent. Their off-diagonal overlaps in the bound
state-port fixture are 1/22 or 1/242, depending on shared tensor indices.

For a common scalar carrier body and scalar partners, normalized collision
normals in mass-weighted momentum coordinates have the form

    n_i=sqrt(m_i/(M+m_i))*e0 - sqrt(M/(M+m_i))*e_i.

Consequently their off-diagonal Gram entries factor as

    C_ij=v_i*v_j, v_i=sqrt(m_i/(M+m_i)).

Every four-distinct-index tetrad must therefore vanish:

    C_ij C_kl - C_ik C_jl = 0.

One global isometry preserves reflection-normal Gram data up to independent
normal signs. Those signs multiply both tetrad terms by the same sign; they
cannot turn a nonzero residual into zero. Extra inactive coordinates cannot
change these inner products either.

## Exact rejection

For the bound ports AB, BC, AD, DB, the residual is

    C_AB,BC C_AD,DB - C_AB,AD C_BC,DB
      = 1/242² - 1/(22*242)
      = -5/29282.

Thus NO choice of positive masses or common linear isometry makes this port
family the proposed scalar collision star. Each isolated port still admits
the previous arbitrary-positive-mass elastic readout. Those separate views
cannot be assumed to agree on what the shared physical body is.

The rejected architecture is narrow. Vector-valued bodies, internal modes,
non-isometric readouts, nonlinear interpretations, and other interaction
architectures have not been classified here. The result also depends on
the previously declared tail/head tensor-slot adapter and inherited metric;
it does not prove those choices are source-selected or physically necessary.

## Charge clue revisited

The prior `continuation-charge-character.md` does give a positive result:
a linear effect into a neutral answer carries the inverse phase character.
But it explicitly does NOT construct an independently interacting matter
object or select a force law. `unrealized-path-charge-character.md` rejects
using an unexecuted-path tag alone as opposite charge.

Those results cannot be used to insert a signed-charge impulse into this
charge-blind exchange. A matter coupling and its conservation/interface laws
remain necessary. They were read here, not freshly formally reverified.

## Disposition for the end-to-end programme

Keep the exchange as a conditional retained-mode/back-action model.
Do not promote its per-port elastic analogy to a global two-body mechanics
or assign masses independently at each port. The next interpretation must
state what shared physical carrier and internal degrees of freedom it uses,
then satisfy all port actions simultaneously. The tested scalar-body route
is closed negatively; a source-selected alternative has not been supplied.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run --with sympy --with 'numpy>=2,<3' python research/nima/checkers/check_multiport_mechanical_binding.py

35 exact global-binding checks pass, including all 16 normal-sign controls
for the first nonzero tetrad. The preceding 267-check source-port adapter
and its imported fixtures rerun. Receipt:
`results/multiport-mechanical-binding.json`, including port order, full Gram
and every detected tetrad violation. No new physical-source theorem is claimed.

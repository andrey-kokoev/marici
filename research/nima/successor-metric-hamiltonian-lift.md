# Whole-history successor: an induced metric, but not yet the same Hamiltonian

## Reuse the existing retained successor and decoder

The previous rotor attachment proves a Hamiltonian evolution of the cyclic
endpoint observer, not of every growing path-family coordinate. To test the
latter, import the existing copy extension E and averaging decoder D directly
from `retained_path_successor.py`, with DE=I.

Begin with unit diagonal root weights. For each child j of parent i with
d_i admissible continuations, define g_child(j)=g_parent(i)/d_i. This is the
UNIQUE diagonal child metric making the existing D the weighted adjoint of E:

    G_child E = D^T G_parent,
    E^T G_child E = G_parent.

Thus the existing whole-family extension IS isometric in this inherited
metric, although not in the unweighted counting metric. No coefficient,
word, operand role or reader has been changed. These weights are not a
source-derived Born distribution or a physical mass assignment.

For the actual LR and RL indicator families their initial weighted squared
norms are each one and remain one under extension. Their retained difference
has squared norm two. This is not the prior rotor Hamiltonian value twelve;
the two quantities live in different specified realizations.

## A bounded whole-register Hamiltonian realization

A standard added parent/child direct-sum register permits the involution

    S = [ 0    D    ]
        [ E   I-ED  ].

With block metric diag(G_parent,G_child), S is self-adjoint and S²=I. It
swaps a parent vector (x,0) with its exact retained extension (0,Ex), fixing
the orthogonal child-detail complement.

For a supplied positive duration tau,

    H=(pi/tau)(I-S)/2

is weighted-self-adjoint and positive, and exp(-i tau H)=S. This establishes
existence of a Hamiltonian implementation on an ADDED register. It does not
derive the register, choose its logarithm, determine tau, or make repeated
swaps advance indefinitely. A second swap returns to the parent register.
The earlier `mass-autonomous-history-execution.md` similarly distinguishes
implementability of a supplied programme from source selection of its law.

## Decisive compatibility control

Even setting tau to the previous rotor tick pi/3 would only match endpoints.
At half a tick, the swap Hamiltonian has amplitudes

    (1-i)/2 on the parent and (1+i)/2 on the child image.

Under the actual endpoint-amplitude reader on both registers, its output is
NOT the prior rotor's half-tick reading, even up to a common complex scalar:
the two output vectors have joint rank two. Therefore this convenient
whole-register construction must NOT be substituted for the previously
attached Hamiltonian.

This exposes the remaining obligation concretely: a whole-history lift must
intertwine the existing continuous rotor reader BETWEEN ticks, not merely
implement the same discrete successor at a selected endpoint.

## Result

The unweighted-norm objection is not an absolute obstruction to a Hilbert
realization: the existing decoder induces a compatible diagonal metric.
A generic whole-register Hamiltonian can implement one extension. But the
one constructed here fails continuous compatibility with the existing
rotor clock. It is a control, not a newly selected physical dynamics.

The prior actual-composition/rotor-clock bridge remains valid on its stated
cyclic observation sector. Physical seconds and a compatible full-history
Hamiltonian remain unestablished.

## Verification

    uv run --with sympy python research/nima/checkers/check_successor_metric_hamiltonian_lift.py

50 exact checks pass across four registered stage transitions, with the prior
Hamiltonian/clock integration rerun. Tests cover positivity, induced adjoints,
isometry, detail orthogonality, involution, actual role transfer, and the
failed intermediate rotor compatibility.
Receipt: `results/successor-metric-hamiltonian-lift.json`.

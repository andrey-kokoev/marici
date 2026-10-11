# Filled bonds can retain the memory through an explicit history register

## Constructed result

The 21-amplitude memory can now be reversibly transferred to the existing
all-filled bond sector **without losing its amplitudes**, provided a separate
quantum history register is retained. A finite two-level battery accounts for
the released energy. This uses the actual seam projectors and the existing
zero-mixing occupation law, not new fitted energy weights.

The added history is substantive structure, not a relabelling that makes the
previous dimensional obstruction disappear. It stores exactly the distinctions
that the all-filled occupation pattern cannot store.

## Encoding and inverse

Let w span the native coherent return N. The previous one-hot memory states are
w tensor |one_hot_j>, j=1,...,21. Add a history register with a ready label 0
and 21 orthogonal labels j, and a battery with energy levels 0 and Delta.

On the coherent sector, exchange the following pairs:

    |one_hot_j, history=0, battery=0>
        <-> |all_filled, history=j, battery=Delta>.

All other pointer basis states are fixed. Distinct pairs are disjoint, so this
is an involutive permutation W. On the full carrier use

    C = N tensor W + (I-N) tensor I.

It is a metric-unitary involution. The coherent control is global: this is not
a proof of a microscopically local device.

For arbitrary complex amplitudes c_j, the retained-memory branch transforms as

    w tensor sum_j c_j |one_hot_j,0,0>
        -> w tensor |all_filled> tensor sum_j c_j |j,Delta>.

All 21 bonds are occupied, while every relative amplitude and phase survives
in history. Applying C again recovers the complete original state and the ready
history/battery. No measurement or erasure is inserted.

The checker respects the earlier non-normalized bit frames. If their squared
norms are r_j=h_j/||w||^2, history label j is assigned coordinate-basis norm
r_j/product(r). Both sides then have precisely the same inherited tensor norm.
In orthonormal physical bases this is simply an equal-norm exchange; the frame
choice changes no physical gap.

## Existing energy law and finite battery

Retain epsilon=1/4, J=1/2, kappa=1 and g=0. History has a declared degenerate
zero Hamiltonian. Its readiness, isolation and physical realization are not
thereby derived to be free resources.

On the coherent carrier:

    E_one_hot = 20*J + epsilon = 41/4,
    E_all_filled = 21*epsilon = 21/4,
    Delta = E_one_hot-E_all_filled = 5.

The battery gap is derived from these already declared parameters. Filling the
bonds releases energy here: relieving twenty consistency penalties costs less
than leaving those bonds empty. The released five units charge the battery.
The original one-hot state was already an excited, prepared resource; no empty
state is charged from nothing. The ready empty pattern is fixed by the gate.

The exact full-carrier energy check is stronger than a check on one vector.
Write P_sum=sum_e P_e and K for the existing native positive carrier matrix.
For one-hot label j and all-filled registers, respectively,

    H_j = K + (kappa-J)*P_sum + 2*J*P_j + (20*J+epsilon)*I,
    H_filled = K + (kappa+J)*P_sum + 21*epsilon*I.

Then

    H_filled + Delta*I - H_j = 2*J*sum_(e!=j) P_e.

Every term annihilates N on both sides. The N-controlled exchange therefore
commutes with the bare carrier/register/battery Hamiltonian globally. A bare
pointer swap without this control would not generally conserve energy outside
the coherent sector. All 21 actual operator-block identities are checked;
noncommuting seams have not been replaced by commuting proxies.

The existing uniform generator pi*(I-C)/2 implements the exchange in unit pulse
time and commutes with the bare energy. Bare-energy conservation therefore holds
during the ideal pulse, not merely at endpoints. Control timing and switching
are still supplied; no autonomous controller or cost-free apparatus is inferred.

## Holding and reading

With the exchange pulse switched off, the all-filled coherent state, charged
battery and degenerate history form a stationary sector of the hold law. Every
history amplitude acquires the same phase, preserving recoverability. Reading
reverses the exchange and discharges the battery to restore the initial one-hot
state. No negative or unbounded battery levels are needed on this constructed
transition.

Leaving the exchange generator on causes return motion. This is controlled
storage, not a newly derived autonomous latch. Nonzero transverse mixing, noise
on history and microscopic control locality remain untested.

## Exact checks

    python research/voevodsky/checkers/check_filled_bond_history_storage.py

Fresh execution passed after the final edits. Receipt:
`results/filled_bond_history_storage.json`.

Checks include all 21 native energy-intertwining blocks, tensor metric matching,
42-dimensional exchange/projector identities, 1012 pointer-label cases, an exact
superposition with all 21 complex amplitudes nonzero, recovery, occupation change
from one to 21, and conservation of the complete bare energy. Source snapshots
and preceding receipts are hash-bound. No enormous full tensor matrix is
numerically diagonalized; the general extension follows the displayed block and
permutation identities.

## Understanding and boundary

- Simultaneous occupation and lossless memory are compatible **when history is
  retained separately**.
- The history dimension is not optional: merging its labels sends 21 orthogonal
  memory directions into one pointer pattern and destroys reversibility.
- The all-filled energy does not encode the information content. The degenerate
  history carries the information while the bond Hamiltonian sets sector energy.
- This supplies a constructive witness, not proof that the source uniquely
  selects the history resource, its degenerate Hamiltonian or the control.

Next physical gates are local control implementation, history isolation and
stability under perturbations, and a supplied or constructed controller/latch.
No particle mass, isotope binding/stability or electron five-cell transport is
established. Previous mass-comparison failures remain valid.

# A reversible charge-locking interaction with retained history and work

## Forward realization

The freshly rerun path-port checker supplies a connected undirected incidence
graph, not a physical charge constraint. This trial supplies an explicit
interaction on the charged registers at those addresses. It uses an externally
chosen spanning-tree schedule, not a new claim that source readouts are invertible.
The construction is mathematical; no apparatus or autonomous carrier Hamiltonian
has been implemented.

## Difference recording and feedback

For parent charge a, child charge b, and a ready integer record r=0, first record
r<-r+b-a without changing either charge. Then shift the child by -r. The result is

    |a,b,0> -> |a,a,b-a>.

This is reversible because the old b is retained. A full extension on arbitrary
integer record inputs is

    (a,b,r) -> (a,a-r,r+b-a).

Its inverse recovers b=b_new+r_new and r=a-b_new. It is a bijection of Z^3 and
therefore a unitary permutation on the corresponding charge basis. The checker
also exhausts the modular three-level version on all27 basis states. Modular
charges are only a finite gate test; the full network uses integer differences.

One ideal physical coupling for the syndrome step is

    H_measure(t)=g(t)*(n_child-n_parent)*p_record,

where the record is a continuous pointer, hbar=1, and its coordinate translates
by the charge difference when the integrated gain is1. Equal parent/child gains
are required. Exact orthogonal integer syndrome registers are an idealized
alternative; a finite-width continuous pointer has finite resolution and is not
an exact projector. The checker verifies the ideal register circuit, not that
measurement approximation.

Feedback shifts the child according to the retained syndrome. Original path
histories can be retained as spectator registers, and the operation address and
syndrome appended to a history tape. The tested inverse recovers all initial
charges. It does not reconstruct a discarded source path: no such erasure is
allowed in the first place. These gates use path incidences as coupling addresses;
they do not themselves implement all carrier traversal dynamics.

This operation is not cloning an arbitrary quantum state. For superposed inputs,
records become correlated with the charges. Keeping them is essential; tracing
them out generally dephases the retained subsystem.

## Charge and energy reservoirs

A shift b->b_new requires a charge reservoir and, under the chosen quadratic
charging energy, a work reservoir. Retain their updates explicitly:

    Q_res,new = Q_res + b-b_new,
    W_res,new = W_res + b^2-b_new^2.

Both total charge and total charging energy are conserved on every tested step.
These ideal shift reservoirs have adequate capacity for the declared input
window. This accounting is not a microscopic autonomous battery Hamiltonian or
a full thermodynamic model. Pointer preparation, timing, gate control and eventual
record erasure are not free resources certified by this calculation. Records
are NOT erased in the tested protocol.

## Full1836-channel preparation

Choose a rooted spanning tree of the source incidence graph. Set one root charge
to1 and the other1835 charges to0. Visit each child once after its parent:

-1835 gates produce charges (1,...,1);
-1835 difference records retain the old charges;
-all15174 edge equalities hold at the end;
-the charge and work reservoirs each supply1835 units;
-the final stored charging energy is1836 units;
-reversing the recorded gates restores the initial state and reservoirs exactly.

The tree choice is a controller schedule, not a symmetry-derived law. The input
root value is also chosen: roots0,-1,2 produce uniform charges0,-1,2 with energies
0,1836,7344 respectively. Nothing in the circuit selects the positive unit sector.

Energy input is normal for state preparation and does not disprove a physical
mass mechanism. The failure as a derivation is that the gap, charging Hamiltonian,
matched gains and desired sector were supplied externally, not selected by the
carrier dynamics. Replacing equal gaps by the previously tested unequal gaps
would change the stored energy while this same charge-locking circuit still works.

## Measurement alone is insufficient

QND difference recording leaves charge populations unchanged. Postselecting all
zero syndromes on a uniform independent three-level product preparation succeeds
with probability3^(-1835). It accepts the vacuum as well as the two uniform
nonzero modular configurations. Without postselection or feedback, it does not
prepare equal charges.

A sensor with unequal gains measures, for example, 2*n_parent-n_child. Its zero
syndrome accepts charges1 and2, not equality. The incidence graph does not fix
these coupling coefficients.

## Verification and residual

    python research/nima/checkers/check_mass_history_locking_controller.py
    python research/aspect/scc/scc.py check nima-mass-history-locking-controller

Finite-register reversibility, integer network updates and reservoir balances
are exact. Report: `results/mass-history-locking-controller.json`.

We now have a concrete history-retaining INTERACTION that can prepare the proposed
complete charge pattern. We do not yet have an autonomous source law deriving
that interaction, protecting a particle sector, or selecting its energy ratio.
Those are not consequences of a successful driven preparation circuit.

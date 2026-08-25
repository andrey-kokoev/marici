# Executable fault-tolerance final verdict

Owner: `marici.Kitaev`

Status: executable stabilizer subcompiler complete; full compiler obstructed in
the frozen source theory by identified nonstabilizer gates.

## Verdict

The distance-three architecture cannot be promoted to a complete executable
compiler from the frozen interfaces alone.

This is not because the code or recovery remained abstract.  Both are now
explicit.  It is because full `D(S3)` sector extraction contains operations
outside the admitted stabilizer resource theory, and no verified magic-state
source or code-switching surface was supplied.

## What is executable

The finite construction now contains:

- explicit `[[5,1,3]]_2` and `[[5,1,3]]_3` stabilizers and logical bases;
- complete 15-entry qubit and 40-entry qutrit recovery tables;
- five-rail six-level and eight-level encoded buses;
- transversal coordinate inversion;
- verified encoded Choi teleportation for `H`, `F3`, qubit SUM, and qutrit
  SUM, with all 110 Bell branches and Pauli corrections checked;
- explicit verified-cat preparation of those Clifford Choi resources;
- explicit generalized Shor recovery for every component block;
- a 26-contact order with recovery after every contact;
- all 78 macro single faults and all 3,081 macro pairs enumerated.

All macro single faults are contained.  The pair table has 220 malignant
pairs under the conservative support automaton.

## Exact source obstruction

Three independent failures occur.

First, full `S3` multiplication needs qubit-controlled qutrit inversion.  It
is not Clifford for the product Pauli structure.  Choi teleportation produces
non-Clifford feed-forward in 32 of 36 branches; the four easy branches give
only a `1/9` postselected experiment.

Second, binary record-label phases for controlled powers one and two are
non-Clifford.  They require controlled-`T`-type and controlled-`S`-type
resources.  Power four is Clifford.

Third, the holonomy-conditioned transporter, class-conditioned choice of
`H/F3`, and coherent flux/charge-to-label lookup are controlled multiplexors.
The individually executable Clifford targets do not make their coherent
selection a stabilizer operation.

The transporter is explicit, not merely typed: the six-entry table chooses
`t(h)` with `t(h) h t(h)^-1` equal to the frozen class representative, and the
36-state alignment is `|h,x> -> |h,t(h)x>`.  Its product-Pauli normalizer test
fails.  The eight-sector residue lookup is likewise frozen bit-for-bit.
Once those three bits exist, label-to-label XOR copy is three executable
logical SUMs and cleans itself on all 64 source/target cases; the unavailable
operation is coherent projector-controlled creation of the bits.

Stabilizer ancillas, Pauli measurements, Clifford Choi resources, and Pauli
feed-forward cannot deterministically supply these gates.  Declaring their
magic states “available” would add a new coefficient/source lens rather than
derive an apparatus from the frozen one.

## Resource accounting

The encoded acquisition core uses:

- 20 rails for four encoded data blocks;
- 15 rails for holonomy, relative, and label buses;
- 15 rails for three encoded acquisition-record qubits;
- 50 quantum rails total before transient ancillas;
- six classical bits for the separately established final record code.

The pre-expansion schedule has 49 macro gates, 26 contacts, and 26 recovery
layers per controlled power.  A six-level recovery consumes 105 cat--data
contacts; an eight-level recovery consumes 144.  Fourier and SUM Choi
verification consume 36 and 90 cat--data contacts respectively, before final
component recovery.

Full physical gate count, depth, and magic-ancilla count are **undefined**, not
zero: the required factories do not exist in the source theory.  The precise
answer to the requested full resource census is therefore an obstruction.

## Distance statement

Distance three is necessary and sufficient for the explicit stabilizer
subcompiler at the audited one-macro-fault level.  If every missing magic or
lookup module were later supplied as a one-fault-tolerant exRec with the same
one-rail output contract, the 26-contact support audit would make distance
three sufficient for the extended compiler.

It is not correct to call distance three executable for the current *full*
compiler, because no full circuit exists.  Nor does the no-go restore the old
distance-five or distance-nine bounds; those belonged to different direct or
unrecovered apparatuses.

## Assumptions and falsifiers

The constructive statements assume independent encoded blocks, one physical
Bell pair per rail, accepted adjacent-verified cats, and the explicit
single-rail stochastic/adversarial support model in the checkers.

Falsifiers include:

- failure of either exhaustive distance-three stabilizer certificate;
- a colliding single-rail syndrome;
- a claimed Clifford gate whose Pauli/stabilizer conjugates leave the tested
  normalizer;
- a Bell branch without the recorded Pauli correction;
- an accepted nonglobal cat shift;
- a macro single fault producing two rail errors in one block;
- an admitted verified nonstabilizer source already present in the frozen
  interfaces.

The last item would supersede the no-go and trigger factory construction and a
microscopic malignant-pair count; it would not invalidate the finite
stabilizer calculations.

## Exact evidence

Run:

```text
python research/kitaev/checkers/check_s3_executable_ft_frontier_audit.py
```

The digest-bound result is
`research/kitaev/results/s3-executable-ft-frontier-audit.json`.  It binds nine
component results covering codes, transversality, transporter/lookup,
teleportation, Choi
verification, magic obstructions, recovery, and the exRec fault table.

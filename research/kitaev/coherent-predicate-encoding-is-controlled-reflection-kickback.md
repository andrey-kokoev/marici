# Coherent predicate encoding is controlled-reflection kickback

Owner: `marici.Kitaev`

## Bounded question

What is the minimal known constructor equivalent to the coherent predicate
encoders required by the reusable qutrit-bus interface?

## Verdict

For every projector `P`, coherent binary encoding of its value is exactly
equivalent, up to one-qubit Hadamards and clean ancillas, to a controlled
application of the reflection

\[
R_P=I-2P.
\]

The missing bus incidence is therefore not a new species of constructor. It
is the same controlled-reflection boundary already encountered in coherent
syndrome extraction and Wilson phase kickback.

Destructive access to `P`, uncontrolled evolution by `R_P`, or knowledge of
its spectrum remains insufficient.

## From controlled reflection to coherent encoding

Let the pointer qubit begin in `|0>`. Define

\[
C(R_P)
=
|0\rangle\langle0|\otimes I
+
|1\rangle\langle1|\otimes R_P,
\]

with the pointer as control and the source as target.

Apply a Hadamard to the pointer, then `C(R_P)`, then another Hadamard. On an
arbitrary source vector `psi`, the result is

\[
(I-P)|\psi\rangle\otimes|0\rangle
+
P|\psi\rangle\otimes|1\rangle.
\]

This is the desired coherent nondemolition encoder. It preserves arbitrary
coherence between the two source sectors as coherence between pointer
branches.

No eigenstate promise is used, so the equality remains valid after adjoining
an arbitrary untouched reference system.

## From coherent encoding to reflection kickback

Let `E_P` be an encoder satisfying the displayed isometry on a ready pointer.
Apply pointer `Z` between encoding and uncomputation:

\[
E_P^\dagger(I\otimes Z)E_P
=
R_P
\]

on the source with the pointer returned to `|0>`.

Thus a clean coherent encoder supplies the source reflection by phase
kickback. If the encoder itself is available conditionally or its pointer is
retained as a coherent control, it supplies the corresponding controlled
interface.

The two constructions establish resource equivalence relative to clean
pointer preparation, Hadamard, pointer phase, and exact uncomputation.

## Instrument interpretation

Discarding or measuring the pointer after `E_P` gives the Lüders instrument
with branches

\[
\rho\longmapsto P\rho P
\]

and

\[
\rho\longmapsto(I-P)\rho(I-P).
\]

Retaining the pointer gives its Stinespring dilation. Uncomputing the pointer
after a phase or bus interaction converts the recorded distinction back into
a coherent source operation.

These are different uses of one dilation:

```text
measure pointer       -> objective record and dephasing
retain pointer        -> coherent predicate control
phase then uncompute  -> source reflection
couple then uncompute -> predicate-conditioned actuator
```

This explains why an available measurement does not automatically authorize
the bus compiler. The physical apparatus must expose the premeasurement
pointer coherently and permit reversal before irreversible amplification.

## Relation to the pinned Wilson construction

The established coherent Wilson phase-kickback packet assumes controlled loop
evolutions in order to extract a joint spectral signature without dephasing.
It then uses compute, phase, and uncompute to synthesize sector projectors.

The present binary theorem is its smallest instance. It shows that the
reusable bus predicate encoder and the Wilson spectral extractor share the
same unresolved physical typing:

- an uncontrolled Wilson or reflection operator is not enough;
- destructive spectral measurement is not enough;
- a coherent controlled action plus clean uncomputation is enough.

Thus the two research lanes should share one constructor audit rather than
counting their coherent encoders as independent primitives.

## Relation to toric-code syndrome extraction

For a binary stabilizer `S`, choose

\[
P=(I-S)/2.
\]

Then

\[
R_P=S.
\]

Ordinary coherent stabilizer-syndrome extraction is exactly the controlled
reflection construction above. The toric-code star and plaquette syndrome
circuits are therefore the Abelian executable instance of the same interface.

The non-Abelian difficulty is not the abstract dilation formula. It is deriving
a controlled reflection for a fusion, charge, or frame predicate from the
microscopic ribbon and gauge operations without erasing the protected sector.

## Minimal compiler target

The qutrit-bus programme can now state its source obligations using one shared
type:

1. derive a controlled reflection `C(R_P)` for the anyonic predicate;
2. derive a controlled reflection `C(R_Q)` for the coherent flag predicate;
3. route the resulting pointer branches through one reusable non-scalar
   port-to-bus actuator;
4. uncompute both pointers exactly;
5. delay irreversible record formation until complementary recombination is
   complete.

For the flag predicate, the controlled reflection may already be elementary
if the flag is a native qubit with coherent two-qubit control. For the anyonic
fusion predicate, physical source derivation remains the substantive gate.

## Fault implications

An imperfect encoder creates two distinct errors:

- wrong predicate assignment in the pointer basis;
- residual source-pointer entanglement after uncomputation.

The second is invisible to a test restricted to correct classical outcomes on
predicate eigenstates. The minimal fault test must include a superposition of
the two predicate sectors and verify both source coherence and clean pointer
return.

Because the same encoder can be used for measurement and actuation, a common
calibration error may corrupt both diagnosis and correction consistently. An
independent phase-sensitive reference remains necessary to expose that
common-mode displacement.

## Falsifiers

- The Hadamard-controlled-reflection-Hadamard sequence fails to implement the
  coherent encoder for some source superposition.
- Encode, pointer phase, and uncompute fails to implement `I-2P` on the ready
  subspace.
- A destructive projective measurement preserves every off-diagonal block
  between the `P` and `I-P` sectors.
- Uncontrolled access to `R_P` alone creates a source-pointer correlation.
- The pinned Wilson spectral construction already derives its controlled loop
  evolutions physically rather than assuming them.
- A non-Abelian fusion predicate has an executable controlled reflection in
  the frozen lattice source with clean uncomputation and bounded fault spread.

## Claim boundary

This packet proves a finite resource equivalence. It does not construct the
non-Abelian controlled reflection, assert that every measurement apparatus is
reversible, or identify a microscopic coupling Hamiltonian.

Its new structural result is that coherent predicate encoding, controlled
reflection kickback, nondemolition syndrome dilation, and the reusable bus
incidence are one constructor family viewed at different ports. The remaining
problem is physical access to that family for the anyonic predicate.

No build, checker, or Git operation was used.

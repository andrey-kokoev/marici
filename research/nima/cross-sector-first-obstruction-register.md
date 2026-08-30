# Cross-sector first-obstruction register

## Purpose

This packet applies the unified obstruction tower to currently pinned examples.
It reports the earliest decisive blocker for each precise claim. "Earliest" is
defined by logical prerequisite, not chronology or numerical gate label. Later
claims are not credited when one of their prerequisites is still open.

## What "first" means

The gates form a dependency graph, not an unconditional total order. For a
declared reconstruction claim, a blocker is first when:

1. it is failed or unresolved;
2. every prerequisite needed to state it has been established;
3. no failed or unresolved predecessor already prevents the claimed conclusion;
4. repairing only downstream properties would leave this blocker untouched.

There can be several incomparable first blockers. For example, once a typed map
exists, global fibre multiplicity and completion instability can both be proved
independently. Both should be reported if neither depends on the other for the
claim at hand.

The status vocabulary is:

- **established:** the gate is proved for the declared claim;
- **failed:** an explicit witness violates it;
- **unresolved:** the gate is meaningful but neither proved nor falsified;
- **not reached:** a prerequisite map or quotient is not yet defined;
- **not applicable:** the declared claim does not require that gate.

In particular, an undefined operator lift is a typing blocker. It does not prove
that later injectivity or completion gates fail; those gates are not reached.

## Gate legend

| Gate | Question | Canonical witness |
|---|---|---|
| 0. Typing | Does the contextual map descend through exactly the authorized source quotient? | gauge-dependent output or an undefined source-to-target map |
| 1. Ramification | Is the local derivative faithful modulo gauge? | nonzero tangent vector with zero contextual derivative |
| 2. Multiplicity | Does one record have several non-gauge source preimages? | distinct source classes with identical records |
| 3. Monodromy | Do local inverse branches glue globally? | closed observation loop returning on another source sheet |
| 4. Escape | Is the inverse stable in the admitted completion and resource regime? | normalized source sequence with vanishing record, divergent inverse norm, or nonclosed graph |

## Register

| Sector and claim | Established | Earliest decisive blocker | Exact missing evidence | Legitimate repair class |
|---|---|---:|---|---|
| Smallest-torus logical sector from local syndrome | Cellular and commutation-derived syndrome structure; four logical classes remain | 2 | two errors in different logical classes have the same local syndrome | add two independent noncontractible loop contexts |
| Smallest-torus logical sector from syndrome plus two loops | joint finite faithfulness modulo stabilizer repairs | none for the finite algebraic state claim | no unresolved finite fibre | no repair needed; do not enlarge the claim to decoder or implementation |
| Decoder selected by syndrome | syndrome does not select a preferred repair | 2 | different decoders agree on syndrome while differing in repair realization | add an authorized cost, locality, or noise-response criterion; a logical probe alone does not choose a decoder |
| Growing-torus executable logical readout | algebraic loop labels remain meaningful | 4 | no uniform noise- and size-dependent criticism margin has been proved | fault-tolerant measurement construction and scaling bound |
| One-qubit Clifford action from Pauli conjugation | conjugation determines the Clifford action modulo scalar phase | 2 | representatives differing by global phase have identical conjugation action | controlled interference or a source-authorized phase reference |
| One-qubit Clifford action with controlled phase context | finite phase distinction is exposed | none for the finite represented action | physical implementation remains a separate claim | retain the controlled context and its frame typing |
| \(D(S_3)\) central Wilson readout as endpoint-block reconstruction | centre has dimension 8 while the endpoint block algebra has dimension 36 | 2 | a 28-dimensional block-algebra complement is invisible to central data | flux-resolved endpoint ports |
| \(D(S_3)\) block algebra from one flux port | one port reaches at most dimension 24 | 2 | at least 12 block directions remain outside the generated algebra | add a port from the missing conjugacy type |
| \(D(S_3)\) block algebra from transposition and three-cycle ports | the two ports generate all 36 block dimensions and are minimal | none for abstract block generation | executable physical control is not proved | a physical actuator/compiler theorem, not another algebraic port |
| \(D(S_3)\) ambient Hermitian reconstruction from the endpoint block algebra | block algebra spans 36 of 256 ambient Hermitian dimensions | 2 if ambient reconstruction is claimed | 220 ambient directions lie outside the block algebra | either narrow the claim to block control or authorize additional ambient contexts |
| Additive scalar readout of a determinant-line phase | additive value is defined | 2 | opposite phase or orientation sheets can share one scalar value | tensor unit, vacuum orientation, or interference reference |
| Determinant-line readout of ordered holonomy | determinant phase is defined | 2 | nonconjugate ordered products may share the determinant | ordered endpoint or sequential composition contexts |
| Scalar Tate section as reconstruction of the tail--seam operator pair | scalar finite incidence and scalar Tate evaluation exist on the source test space | 0 | the operator-valued lift and its source/target rigging are not yet defined and proved compatible | derive the Schwartz-to-boundary trace correspondence before inversion |
| Tate restriction after additive \(L^2\) completion | additive-Haar-null obstruction is established | 0 | restriction is not a bounded map from additive \(L^2(\mathbb A)\) to idelic \(L^2\) | restrict on Schwartz--Bruhat space before completion and audit closability |
| Finite Euler coherence as proof of nonvanishing after completion | every finite transition is invertible and typed residuals vanish | 4 | inverse norms or normalized states may escape at the restricted-product limit | properness, closed-graph, or uniform lower-bound theorem in the authorized topology |
| Finite Clark feature Gram positivity as state observability | feature-space positivity is available on the selected outputs | 1 for state reconstruction, then 4 | possible invariant state in the feature kernel; possible vanishing smallest observability eigenvalue | compute the dynamical observability Gramian, then prove a cutoff-uniform quotient bound |
| Tail-only Clark observability | finite feature maps may be injective | 4 | tail-translation escape can make tail output vanish while seam output persists | retain the independently derived seam row and prove a uniform augmented bound |
| Arithmetic Gram completion preserving exact-label predicates | adjacent label vectors collapse analytically | 0 or 4, depending on formulation | parity, divisibility, and prime typing can have persistent jumps on collapsing pairs | retain the minimal authorized discrete port; do not demand preservation of unauthorized predicates |
| Primitive and square current incidence | finite incidence \(I_k(p,k)=k^{-1}p^{-k/2}\delta_{k\log p}\) is supplied | 0 for the operator lift | finite scalar incidence does not define the global tail--seam correspondence | construct the typed operator-valued trace lift with asymmetric \(P/Q\) topology |

## Immediate deductions

### 1. No universal repair observable

Each gate has a different repair type. Adding more rows can repair multiplicity
or ramification. It cannot repair a map that is not typed, and finite rows do not
by themselves repair completion escape.

### 2. Claim narrowing is sometimes the correct repair

The 36-dimensional endpoint block algebra is already complete for block control.
Its failure to span 256 ambient Hermitian directions is not a defect unless the
programme claims ambient control. Likewise syndrome plus loops is complete for
finite logical classification but not for decoder choice.

### 3. Scalar-to-operator reconstruction is presently blocked earliest

In the theta/Tate lane, the first obstruction is not a mysterious zero or a weak
positivity estimate. It is Gate 0: the rigged source-to-boundary operator
correspondence must be defined and shown to respect the typed quotient. Only
then do fibre, monodromy, and completion questions become well-posed.

### 4. Finite coherence and completion faithfulness are orthogonal

Exact finite-stage identities remove algebraic residuals. They do not establish
properness or a bounded inverse. The canonical hostile witness is an invertible
sequence with smallest singular value tending to zero.

### 5. References kill fibres, not arbitrary state dimensions

A phase bit, tensor unit, vacuum orientation, or loop probe can select a finite
sheet. It does not reconstruct an unrestricted operator or continuous amplitude
unless its context family is independently shown to be fully abstract for that
larger object.

## Programme triage

The next theorem for each active lane should be selected by its earliest
decisive blocker:

1. **Toric finite logical sector:** closed; use it as the reference example.
2. **Growing toric implementation:** quantify Gate 4 scaling.
3. **\(D(S_3)\) endpoint block algebra:** closed algebraically; separate physical
   actuation authority.
4. **Three-lens reconstruction:** compute the exact fibres of the two forgetful
   maps.
5. **Theta/Tate operator reconstruction:** define Gate 0 trace correspondence;
   do not jump to scalar positivity.
6. **Restricted-product completion:** formulate and attack Gate 4 properness or
   graph-closure criteria only after Gate 0 is typed.

## Minimal reporting schema

Every milestone report should include:

```json
{
  "claimed_object": "...",
  "authorized_gauge": "...",
  "contextual_map": "...",
  "earliest_blockers": [
    {
      "gate": "typing | ramification | multiplicity | monodromy | escape",
      "status": "failed | unresolved | not_reached"
    }
  ],
  "witness": "...",
  "repair_class": "...",
  "repair_authority": "source-derived | mathematical-template-only | physical-implementation-needed",
  "later_gates_not_yet_claimed": ["..."]
}
```

## Bottom line

The useful output is a triage discipline. It tells the programme when to add a
probe, when to add a frame, when to define a missing constructor, when to prove a
completion theorem, and when merely to narrow an overlarge claim.

The minimal failed or unresolved gates in the prerequisite graph are the
research frontier. Everything depending on them is conditional.

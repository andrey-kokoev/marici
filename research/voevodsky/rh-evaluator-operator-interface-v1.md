# Iteration3: actual operator test for the retained RH evaluator

## New result

The term-bearing evaluator now has explicit reversible operators, directed
histories and a complete comparison register. It is no longer just a table of
finished quadratic forms.

The straightforward finite coherent-amplitude implementation is **rejected**:
the evaluator's addition operators cannot be injected into the inherited
norm-preserving pulses or native projector stages as the same processing.
The obstruction persists for vertex-dependent encoders around closed loops.

A countably infinite computational-basis bank gives a faithful unitary model
of the rational evaluator. The same new processor can accompany either native
structure. But it is an explicitly imported spectator processor, **not evidence
that the original seed triangles execute the arithmetic**.

## 1. Correct the two-root ledger into a composable history

Iteration2 listed

    AB,BC,CA | BA,AD,DB.

These are two individually valid cycles rooted at A and B respectively. They
are not one chronological execution: CA ends at A whereas BA begins at B.

For a shared root A the spectral cycle must be cyclically reordered:

    arithmetic: A->B->C->A, word AB,BC,CA,
    spectral:   A->D->B->A, word AD,DB,BA.

The combined six-occurrence history is therefore

    AB,BC,CA,AD,DB,BA.

The checker uses the live source occurrence registry, rejects the old
concatenation as a single history, and verifies forward and reverse recovery
for 18 exact configurations. Recovery uses inverse/dagger arrows; it does not
pretend all inverse edge directions are primitive arrows in the seed.

The raw mirrored coefficient convention from iteration2 still identifies the
polarized query. A right-cycle reindexing requires retaining its basis labels;
it must not change which test a coefficient denotes.

## 2. Explicit evaluator register space

Use a15-coordinate rational score configuration:

- six coefficients of the polarized Gaussian test;
- three endpoint/gamma/prime registers;
- arithmetic output;
- finite spectral register and spectral output;
- full-divisor remainder;
- arithmetic midpoint correction;
- finite-scout correction.

The last three are independent **formal input registers**, not assigned actual
zero. They separate the unknown zero remainder from approximation errors.
The arithmetic coefficients are the previous certificate's rational midpoint
representatives. The spectral coefficients are independently read from the
finite zero scout, then rationally rounded. They are not exact analytic values.

For fixed query weights w, write the arithmetic rows e,g,p and finite spectral
row z. The nontrivial edge operations are reversible additions:

    BC: (r_e,r_g,r_p) += (e.w,g.w,p.w),
    CA: q_a += r_e+r_g+r_p+epsilon_a,
    AD: r_z += z.w,
    DB: q_z += r_z+tail+epsilon_z.

AB and BA transport the complete query configuration unchanged; their typed
vertex locations differ. Each operation is S=I+N with N²=0, so its exact inverse
is I-N. All inputs and intermediate registers remain retained.

Prepared queries have blank score registers but retain their query and
correction registers. Repeated cycles intentionally accumulate records;
restarting a query would require a separately specified reset/preparation.

## 3. What the common edge identifies—and does not identify

In the typed configuration model AB and BA are inverse adjoint transports.
They identify the retained test and all accompanying record/correction slots.
They do not assert that the arithmetic and spectral outputs are equal.

The full comparison is exactly

    q_a-q_z=(e+g+p-z).w +epsilon_a-epsilon_z-tail.

The checker computes this covector on the whole prepared query space. The
three correction coefficients are +1,-1,-1 with the indicated order; no
unknown contribution is silently dropped.

The arithmetic and spectral loop operators commute in this declared register
model. Nevertheless the comparison covector is nonzero as a formal expression.
Therefore commuting loops and lossless shared-edge transport still do not
force the RH comparison. Determining the actual corrections from independent
source computations remains essential. Defining tail from the arithmetic
residual would make equality tautological and is not done.

## 4. Why a finite coherent record bank does not implement these operators

Freshly reconstruct the inherited source pulse matrices from their live
receipt. Each is an involution E_i with

    E_i²=I, E_i^T K E_i=K,

where K is positive. Positivity is checked by symmetry and strict positive
diagonal dominance. The existing neutron52-coordinate bank realizes those
same pulses and retains their positive norm law; it does not change them into
an arithmetic addition instruction.

For a single global linear amplitude encoder J, the proposed intertwining

    E_i J=J S_i

would imply J(S_i²-I)=0. But S_i²-I=2N_i!=0 for BC,CA,AD,DB. Injection is
impossible. An idempotent-stage substitution similarly requires JN_i=0.

That individual-edge argument assumes one encoder at both endpoints. A
stronger closed-loop test covers vertex-dependent encoders too:

- both evaluator loops are nontrivial unipotents;
- their powers are I+nN+n(n-1)N²/2 with N³=0;
- on a pure first-test query, their output grows as
  n(n+1)/2 times a nonzero source coefficient;
- the corresponding valid inherited pulse loops remain metric-unitary.

An injective linear encoder at the common root induces a positive metric on
the finite score space. Norm equivalence forces the unipotent orbit to become
unbounded, whereas the target unitary orbit is norm-constant. Hence no such
encoder exists. Native idempotent return processing fails the loop polynomial
test as well. A finite recurring frame register cannot remove the growth.

This excludes the particular **linear coherent-amplitude semantics**, not
all quantum measurements, nonlinear encodings, externally controlled
calculations or alternative evaluator algorithms.

## 5. A faithful explicit completion, with a different meaning of records

Let X=Q^15 and use

    H_record=l2(X),
    U_i |x>=|S_i x>.

Since every S_i is a bijection of rational configurations, U_i permutes an
orthonormal basis and is unitary. For typed locations use one copy over each
source vertex A,B,C,D; an edge is a unitary between its source and target
subspaces and a partial isometry on the direct sum.

This is not a contradiction to the finite-amplitude obstruction. The numerical
score coordinates x are now **basis labels**, not coherent amplitudes. The map
x->|x> is not the linear encoder required above. Coordinate values can grow
while the ket norm remains one.

Every edge, its inverse and superposition inner products are checked. The
shared edge AB and reverse BA are true adjoints on this new carrier.
Countability supplies a separable mathematical bank, not a finite-memory or
physical device claim.

## 6. Does that processing survive in both structures?

One may tensor either complete native36-coordinate carrier with this same
record bank and act by

    I_native tensor U_i.

The proton metric and neutron denominator metric are retained. Every native
coordinate is a spectator, and the same typed record computation, recoveries
and inner products survive in both extended contexts.

This is a **conditional yes for the new bank computation**, not a yes for the
old seed's local arithmetic. No native pulse or L/G/N operator is replaced.
Nor is a native-geometry vertex map to the four source registry labels inferred.
Attaching an identical computer to both structures cannot demonstrate that
either structure supplied the computer's arithmetic law.

The finite term coefficients remain externally source-computed inputs. The
full divisor and analytic corrections remain unresolved. No RH result is
promoted by the successful unitary configuration simulation.

## 7. Verification and next executable gate

    python research/voevodsky/checkers/check_rh_evaluator_operator_interface.py

Passed: live occurrence types, correction covector, all edge inverses,
18 composable retained histories, inherited pulse identities, per-edge and
closed-loop obstructions, exact unipotent growth, typed configuration
unitarity, shared-edge adjointness and both metric-retaining spectator contexts.

An initial import-path defect prevented loading the Strominger helper; the
read-only helper path was added and the checker refrozen. No scientific
acceptance condition or source operator was changed. Shared stores remain
read-only.

SCC fingerprint:
`15077f33fb8088a1cda5cc0f65fdc24ae8bb707e45595d03e71e6136245624aa`.

- Contract: `inputs/rh-evaluator-operator-interface-v1.json`.
- Receipt: `results/rh-evaluator-operator-interface-v1.json`.
- Model: `scc-models/rh-evaluator-operator-interface-v1.json`.

**Next:** generate the labelled arithmetic operations from the actual source
kernels—rather than loading finished term matrices—and independently verify
the shared explicit-formula convention. This is a nonredundant step toward
source-derived computation. An imported spectator processor cannot close it.

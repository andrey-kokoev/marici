# Bool structural pilot: binding to the programme register

## Scoped disposition

Accept `structural-pilot-programme-binding` at the existing finite structural verification level. The accepted Bool witness is now explicitly bound to source `native-bool-square-pilot`, version `native-bool-retained-programme-fragment.v1`, registered view `bool.delta-retained.C4.v1` and map `bool-retained-linearization`.

This is a **same-source programme binding**, not an embedding into the optical Fock candidate. The source register remains source-indexed. No physical recovery, common physical witness, new kernel theorem or formal outcome is asserted.

Contract: `contracts/physics-structural-pilot-binding.v1.json`.
Receipt: `results/physics-structural-pilot-binding-v1.json`.

## Maps and all-word proof

Order labels as 00,01,10,11. Send each label s to its delta vector e_s, and each native LEFT/RIGHT flip to the registered column permutation P_j. Direct calculation on four basis labels gives `P_j e_s=e_(j.s)`.

A path is represented by its source ID, initial label, complete operation word, ordered permutation product and delta-vector trace. This is exactly the existing registered retained map. Add occurrence ID independently; two executions of the same word need not have the same occurrence identity.

The inverse reads the initial label and full word and validates the product and trace. The empty word is identity. For endpoint-matched paths p,q, representation of p followed by q concatenates words/traces and multiplies matrices in execution order. The primitive action squares and this concatenation rule prove preservation for **all finite words by induction**. Equal matrix products or endpoints do not identify paths.

The complex state is the registered delta state; the real state is its image under `r(z)=(Re z,Im z)`. Arbitrary complex amplitudes belong to the accepted linear/analytic presentation, not to a claim that every amplitude is a native Bool label. The real presentation retains the same source/word/trace/occurrence record.

## Analytic and scale transport

Use the accepted witness unchanged:

`Q_j=(I-P_j)/2`, `H_j=pi Q_j`,
`U_j(t)=(I-Q_j)+exp(-i*pi*t) Q_j`.

Since `Q_j²=Q_j=Q_j*`, this formula is unitary for every real t and has the accepted generator. It is not inferred from finitely many phase fixtures. Its parameter convention remains `theta=pi*t`.

For any complex matrix `A+iB`, block multiplication proves

`R(A+iB)=[[A,-B],[B,A]]`,
`r(Mz)=R(M)r(z)`, `R(MN)=R(M)R(N)`, `R(M*)=R(M)^T`.

With `J=R(-iI)`, the normalized generator satisfies

`R(-i Q_j)=J R(Q_j)`.

Restoring the same symbolic pi gives the real Hamiltonian generator for `E_H(x)=x^T R(H)x/2`. Thus `z*H z=2 E_H(r(z))`; no new generator or factor-of-two energy convention is introduced. Pi and the time parameter remain analytic conventions, not apparatus units.

The complex-to-real map is injective, preserves squared norm and transports every Hermitian quadratic form. Coordinate intensities become `q_j²+p_j²`. These polynomial identities hold for all amplitudes by their coefficient identities; equal scalar readouts still cannot replace full states or retained records.

## Schedule and positive return transport

Retain both ordered Tick schedule tags at a fixed Bool source. Each forward route reaches the both-flipped source. Its return executes the forward word in reversed order with **positive phase**, so at the first integer-time endpoint it reaches the schedule-specific seam and at the second returns to the original source. The two unequal schedules have distinct seams, although their endpoints agree.

Realification commutes with each leg and consequently with their ordered composition, giving the same complete piecewise return. Continuity and interior generator laws are inherited from the accepted witness. No differentiability at the switching seam is claimed. The finite Python Tick tags use the existing Bool specialization; they do not replay dependent native Tick terms or classify arbitrary path histories.

## Verification and review

Fresh verification resolves the accepted overlap pointer through its live admission checker and checks every pinned input before and after execution. Exact controls cover:

- 508 retained paths through length six and 3076 composition splits;
- all 16 source/ordered-Tick-tag bindings;
- eight unit-phase controls, normalized generator and energy transport;
- 576 Hermitian quadratic coefficient identities, reused from the accepted readout audit;
- occurrence preservation and rejection of foreign source, corrupted real state, missing occurrence and erased word.

The all-word induction and block/projector calculations above are the unrestricted arguments; finite fixtures corroborate the adapter. Acceptance is scoped written/exact-algebra plus the existing live mixed-level import, not new kernel certification.

```
python research/nima/checkers/check_physics_structural_pilot_binding.py
python research/aspect/scc/scc.py check physics-programme-v18
```

Remaining programme tasks include independent optical source-law justification, optical/detector common-source comparisons, physical overlap coherence and reviewed assembly. This binding does not discharge any of those cross-source obligations.

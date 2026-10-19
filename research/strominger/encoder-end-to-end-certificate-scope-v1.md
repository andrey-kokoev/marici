# Matrix proximity alone fails; a source-bound free-storage certificate survives

## Question and tested rivals

The proposed common certification interface should certify an implementation
through encoding, storage, contact readout and recovery. Test whether its only
substantive numerical field, encoder error delta, could suffice by itself.

It cannot. Two exact counterexamples below have delta=0 but fail a downstream
stage. These refute the matrix-error-only interpretation, not the previously
stated source-bound conjecture, which requires compatible storage and contacts.
The actual source's corresponding prerequisites pass the exact checks.

## Exact counterexamples

1. Encode one source mode by J=(0,1)^T. This is an exact isometry. The old reader
   (1,0) returns zero, while the transported reader J^T returns one. Zero
   encoding error gives no readout guarantee for an untransported contact.
2. Encode two source modes into coordinates 0 and 2 of a three-coordinate
   target. Let source K=0 and target H=diag(0,0,1). The encoder is exactly
   isometric, but HJ-JK is nonzero. At parameter pi, decode the stored input
   (1,1): the result is (1,-1). After normalization the ideal and actual states
   are orthogonal. This is a failure of storage compatibility, not synthesis
   accuracy or numerical rounding.

Both controls are computed with rational matrices; the declared parameter-pi
flow in the second fixture is the exact diagonal sign matrix. They are abstract
hostiles, not substitute neutron Hamiltonians.

## Actual source prerequisites

The checker independently reconstructs S=Bsharp B, A0=H_native/4, the actual
five-column bright basis E, its metric g, and its reduced generator Kb. It
verifies exactly

    A0 E=0,
    S E=E Kb,
    Kb^T g=g Kb.

The actual two raw rim columns are the first two columns of E and have Gram 3I.
Dividing them by sqrt(3) gives a metric isometric contact map C into the bright
space. No physical gain is inferred from this normalization.

The existing polar identities, together with these equalities, give ideal
isometry J with H_after J=J K on the bright sector. H_after is the unchanged
storage operator, not one fitted to a candidate word. The exact algebraic
prerequisites are freshly checked; the polar functional-calculus implication
is reused from its written construction.

## Source-bound sufficiency theorem for free storage

Let E0 be ready-memory inclusion and V an actual permitted metric-unitary word.
Set A=V E0 on the bright space and assume a certificate

    ||A-J|| <= delta.

For unit bright input x and any real storage parameter t, ideal intertwining
and source invariance give

    ||exp(-it H_after) A x - J exp(-it K)x|| <= delta.

There is no factor growing with t: both states use the same fixed target
Hamiltonian, and the ideal encoded subspace is exactly invariant. Applying Vsharp
and comparing to ready-memory recovery yields

    ||Vsharp exp(-it H_after) V E0 x - E0 exp(-it K)x|| <= 2 delta.

The first term in the triangle inequality is the initial encoding discrepancy
transported unitarily; the second is
Vsharp(J-A)exp(-it K)x, bounded by delta because the source stays bright.

Use candidate contact AC and ideal contact JC. Their difference has norm at
most delta. Each contact has norm one, and both evolved states have norm one,
so the contact-amplitude discrepancy is at most 2 delta, uniformly in t.
At the write endpoint, candidate co-transport preserves its own readout exactly:
(AC)sharp A x=Csharp x. That alone would not prove stored dynamics agree.

For any fixed bounded energy/observation operator O on the stored carrier,
expectation differences are at most 2||O||delta for the encoded free-hold states.
These inequalities are written norm estimates, not consequences of finitely
sampled storage parameters.

## Scope and correction to the next task

A source-bound certificate must carry or reference: the permitted-word and
metric-unitarity proof, exact source/target Hamiltonian identities, the ready
bright domain, transported contacts, and the certified proximity bound. A scalar
error estimate detached from those objects is insufficient.

The free-storage result is stronger than the earlier suggestion that a bounded
storage-duration range is always necessary: it is uniform in the mathematical
storage parameter under these exact hypotheses. It does not automatically cover
ongoing lead coupling with changed contact operators, arbitrary initial memory,
new noise channels, or controller/work accounting. Those introduce different
maps or generators and need their own composition bounds.

No accepted control word, compiler, or WG term is produced here. The broader
certified-interface conjecture remains unrefuted; its free-storage sufficiency
has the conditional theorem above. The next implementation should reference
these source identities instead of trying to certify downstream behavior from
matrix proximity alone.

## Verification

    python research/strominger/checkers/check_encoder_end_to_end_certificate_scope.py

Fresh execution passes the source identities and both expected counterexamples.
Receipt: `results/encoder-end-to-end-certificate-scope.json`. Source/checker hashes
are retained and checked unchanged; predecessor suites were not rerun. The
inequalities are written mathematics, not a formal-kernel certificate. No graph
publication, commit or push.

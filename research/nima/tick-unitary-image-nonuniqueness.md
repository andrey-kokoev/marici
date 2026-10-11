# Does unitary composition remove the Tick interpolation ambiguity?

## Frozen question — iteration 3

The full Bool Tick classification and the existing native-square Hamiltonian
realization are the starting points, not targets to reconstruct. The stochastic
image obstruction is already closed in its own class. The remaining question
here is whether adding commuting unitary composition, nonnegative autonomous
axis generators and axis-interchange symmetry leaves only a change of parameter
or an overall phase.

Freeze the following class of **retained unitary annotations** of a fixed-source
Bool Tick t:

- Keep the entire t as the structural component; use its actual ordered schedule
  tags for the two route annotations. Repeated tags remain allowed.
- Use the existing labelled C^4 linearization, counting inner product, and exact
  L,R bit-flip matrices from `native-square-controlled-hamiltonian.md`.
- Supply commuting Hermitian nonnegative H_L,H_R, exchanged by the existing
  tensor-factor swap, with exp(-i*pi*H_L)=L and exp(-i*pi*H_R)=R.
- Set E(a,b)=exp(-i*a*H_L)exp(-i*b*H_R). Keep the two ordered boundary routes and
  the whole reflected square E(pi-a,pi-b), not merely its final endpoint.
- No tensor-locality condition on the INTERMEDIATE axis operators, principal
  logarithm, rate, physical clock or analytic interpretation of the dependent
  Agda return section is assumed. Retaining that section as part of t does not
  itself construct such an interpretation.

SCC obligations: forward realization, route compatibility and comparison of
readouts within this declared annotation class. Its angles are dimensionless
parameters. This is not a claim that native Tick syntax supplies analytic laws.

**Conjecture tested:** these added unitary requirements identify the image of
the existing projector square, up to parameter substitution and overall phase.
Closure is either an image-classification proof or an admissible rival with a
state outside that whole image. A comparison at equal parameter values alone
is insufficient. Source labels and the state encoding are fixed.

**Rivals:** all differences are rates; the obstruction only reflects stochastic
noninvertibility; positivity or interchange symmetry eliminates it; a stronger
locality requirement would exclude the rival but is absent from this class.

**Frozen test:** reuse the actual native checker and its joint projectors.
Compare H_L=P_L,H_R=P_R with H_L=P_L+2*P_L*P_R,
H_R=P_R+2*P_L*P_R. Check the complete unitary-group formula, corner attachments,
axis swap and reflected return. Use the determinant of the 2-by-2 amplitude
matrix as an all-parameter image invariant. A failed admissibility gate rejects
the rival; it is not repaired by weakening the class after testing.

## Admissibility on the unchanged source

Write J_lr for the existing four rank-one orthogonal joint projectors of
P_L,P_R. They sum to I. For k=0 or k=2, the entire family is

\[
E_k(a,b)=\sum_{l,r\in\{0,1\}}
 e^{-i[a(l+klr)+b(r+klr)]}J_{lr}.
\]

This proves unitarity and the additive two-parameter group law for every real
a,b, not just the exact regression grid. The two generator eigenvalues in
sector (l,r) are l+klr and r+klr, hence nonnegative. The factor swap interchanges
them. Since k is even, their exponentials at angle pi equal L and R, so all
four corner operators and both schedule orders agree with the existing source.

The complete return comparison is

\[
E_k(\pi-a,\pi-b)=LR\,E_k(a,b)^\dagger.
\]

It holds throughout the square, not only at its endpoints. Both assignments
can accompany the same full t and either of its actual schedule tags. This
is membership in the frozen annotation class, not an analytic interpretation
of t's dependent return-section field.

## An image invariant eliminates every parameter substitution

Arrange a vector psi in the fixed labelled basis as a 2-by-2 amplitude matrix
Psi. For k=0 and every encoded source basis vector, the operator factorizes
into one operation on each tensor factor. Consequently

\[
\det\Psi_0(a,b)=0
\]

for ALL real angles, even outside the original square. The checker verifies
the stronger coefficient identity for independent complex variables z,w.
It also holds for the previously tested uniform generator rescaling; that
rescaling alone does not leave this enlarged product-state image.

For k=2, source e00, a=pi/3 and b=0, set z=exp(-i*pi/3). The actual state is

\[
\psi_2=\frac14(1+z,\;1+z,\;3-z,\;-1-z)^T,
\qquad
\det\Psi_2=-\frac{1+z}{4}=-\frac38+\frac{i\sqrt3}{8}.
\]

Thus its determinant has squared modulus 3/16, not zero. No choice of ANY
baseline real angle pair produces this state, even after multiplying by an
overall phase: that only multiplies the determinant by the phase squared.
The same obstruction holds for every source and either schedule, with the
appropriate row/column permutation. It therefore excludes reparameterization
of the paths and even arbitrary substitutions into the whole baseline square.
It is not a discrepancy observed only at equal parameter values.

## The additional assumption exposed by the test

The rival is not tensor-local at intermediate first-axis parameters. Let
Z_R=I tensor diag(1,-1). The baseline P_L commutes with Z_R, whereas
P_L+2*P_L*P_R does not. A requirement that every first-axis operator act only
on the first factor would exclude this rival. It was explicitly absent from
the frozen class. The result does not assert that a separately specified
functorial/locality interpretation lacks such a requirement.

Conversely, making the mixed coefficient odd fails a source corner: the
checker retains this inadmissible rival as a rejection control. Positivity,
unitarity or endpoint agreement alone are never substituted for all gates.

## Disposition and stopping condition

**Closed by underdetermination:** commuting unitary composition, nonnegative
axis generators, interchange symmetry, corner data and the reflected-return
law do not determine even the path image in this declared class. This is
strictly beyond a missing rate or an overall-phase convention.

Keep the earlier Hamiltonian existence result, full Bool classification,
stochastic non-uniqueness and Poisson obstruction at their separate scopes.
Do not generate further members of this class as attempts to select a physical
law. Selection needs an independently justified restriction, such as a stated
intermediate-locality contract, or a new source/readout comparison. Merely
imposing the desired restriction would not derive it from Tick.

## Verification and evidence repair

- Fresh headless closures of `TickRetainedStructure` and
  `NativeSquareHamiltonianSkeleton` both exit 0 using the existing Agda runner:
  executions `e_38524_1791391384422786800_22` and
  `e_38524_1791391488408038700_23`. No formal source was changed.
- `checkers/check_native_square_controlled_hamiltonian.py` reruns its existing
  exact checks. Its only code change exports the checked algebra for reuse;
  the new checker does not reconstruct a substitute source.
- `checkers/check_tick_unitary_image_nonuniqueness.py` checks spectral
  admissibility, polynomial image identities and eight exact obstructions.
  Its receipt is `results/tick-unitary-image-nonuniqueness.json`. The real-angle
  analytic argument above is not claimed as a new Agda analysis theorem.
- Frozen SCC challenge `e_38524_1791391788518401300_26` exits 0 with the
  preregistered meaning **falsifies image uniqueness**. Its exit-code-only
  wrapper is not the mathematical evidence. Final scoped check
  `e_38524_1791392028373067100_28` passes with 384 exact controls; execution
  `e_38524_1791392143499635400_29` verifies current source hashes, archived
  artifact integrity and the quarantine receipt.

Fresh reading also found the old `check_general_square_generator.py` reporting
four continuous parameters after integer-parity constraints and listing 3H0
among candidates after imposing a=1. Those are not valid conclusions. Its
original code and receipt are hash-preserved under
`quarantine/20261007-general-square-generator/`. The entrypoint now refuses
verification with exit 2 (execution `e_38524_1791391788575531300_27`); the old
receipt is a quarantine notice. Correct commutant facts remain available in
the current `source-to-generator-audit.md`; quarantining the old narrative
does not withdraw those facts or the independently checked native realization.

Current-disposition pointers were added to the native Hamiltonian, full Tick
classification, prior-continuity search and source-to-generator packets.
Graph report and criticism: `ev-000000015818-7caf3799-c04b-4c40-be09-6c593d359209`,
proposal `ep_7b0c47bb-323a-499a-ae1c-54a34f415dca`. This turn's [15818,15818]
and the preceding audit/correction interval [15815,15817] remain uncommitted.
No commit, push or publication occurred; graph admission is not truth certification.

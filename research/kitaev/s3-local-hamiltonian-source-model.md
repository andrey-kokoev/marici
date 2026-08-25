# A local source model for the finite `D(S3)` control audit

Owner: `marici.Kitaev`

Status: source-typed finite theorem for one square plaquette and its base
vertex; physical availability of non-native pulses remains conditional.

## Bounded question

What is the smallest microscopic source model in which the previously found
endpoint ports can be tested without declaring endpoint matrices to be
controls?

Fix an oriented square with vertices `v0,v1,v2,v3`, edges

\[
e_0:v_0\to v_1,\quad e_1:v_1\to v_2,\quad
e_2:v_3\to v_2,\quad e_3:v_0\to v_3,
\]

and Hilbert space `C[S3]^{\otimes 4}`.  In the labelled edge basis, the
holonomy based at `v0` is

\[
h=g_0g_1g_2^{-1}g_3^{-1}.
\]

The based gauge action at `v0` is

\[
U_x|g_0,g_1,g_2,g_3\rangle
=|xg_0,g_1,g_2,xg_3\rangle,
\]

and the flux effect is the diagonal projector

\[
B^g|\mathbf g\rangle=\delta_{g,h(\mathbf g)}|\mathbf g\rangle.
\]

These are derived edge operations, not abstract endpoint blocks.  They obey

\[
U_xB^gU_x^{-1}=B^{xgx^{-1}}.
\]

The fixed-point Hamiltonian uses only the Haar vertex projector and flatness
projector,

\[
A=\frac1{6}\sum_xU_x,\qquad B^e,
\qquad H_0=(1-A)+(1-B^e).
\]

Both are commuting Hermitian projectors.  This is the native source surface.

## Port classification

An individual `B^g` is a four-edge Hermitian projector, so
`exp(-i theta B^g)` is an exact four-edge diagonal pulse **if** the apparatus
admits based, element-resolved holonomy control.  That conditional is not
empty notation: for every noncentral `g`,

\[
[A,B^g]\ne0.
\]

Thus neither the transposition nor three-cycle port is a term of the native
commuting-projector Hamiltonian.  On the full vertex-invariant excitation
space, turning either on can leave the gauge-invariant subspace.  This does
**not** imply vacuum-code leakage: orthogonality gives

\[
B^tB^e=B^cB^e=0,
\]

so both pulses act identically on the flat ground sector.  Their useful action
and their gauge-breaking risk begin only after a nontrivial-flux endpoint has
been prepared.  By contrast, the conjugacy-class sums

\[
B^{C}=\sum_{g\in C}B^g
\]

commute with `A`, but they retain only class membership.  They cannot supply
the element-resolved endpoint atoms used by the 36-dimensional associative
closure theorem.

The exact disposition is therefore:

- locality: proved, with support four on the frozen square;
- Hermitian pulse form: proved;
- membership in the native Hamiltonian: falsified for both noncentral ports;
- availability under an enlarged based-holonomy apparatus: conditional;
- flat vacuum-code action: exactly trivial;
- preservation of the larger vertex-invariant excitation space: generically
  falsified by the nonzero commutator.

## Carrier versus coefficient lens

Carrier geometry supplies the oriented boundary, its base vertex, edge
incidences, and the four-edge support.  The quantum coefficient lens supplies
`C[S3]`, left multiplication, inversion on oppositely traversed edges,
delta-function flux effects, Haar averaging, Hermitian exponentiation, and
the gauge-invariance/code-space test.  Removing the basepoint changes an
element flux into a conjugacy-class effect; that is a loss of coefficient
resolution, not a harmless geometric relabelling.

## Preregistered optionality snapshot

At objective start there are four source possibilities for each noncentral
port: native commuting term, gauge-breaking local pulse, ribbon-compiled
effective pulse, or obstruction.  This packet eliminates the first branch,
retains the second conditionally, and leaves ribbon compilation versus a
physical obstruction open.  No claim is promoted beyond the finite square.

Process calibration, pre phase: excitement `9/10`, because the endpoint
algebra now meets a sharp microscopic gauge constraint; confidence `6/10`
that both ports admit useful fault-tolerant compilations; expected information
gain `9/10`.  Confounds: the model is exactly solvable and the finite square
may understate geometric scheduling and hardware constraints.  These ratings
are process observations, not evidence.

## Verification and falsifiers

Run:

```text
python research/kitaev/checkers/check_s3_local_source_model.py
```

The dependency-free checker enumerates all `6^4=1296` edge states, performs
`6*6*1296=46656` conjugation checks, verifies the exact projector ranks and
gauge orbits, and computes exact rational Frobenius norms for the relevant
commutators.  The result is written to
`research/kitaev/results/s3-local-source-model.json`.

The packet is falsified by a failure of the conjugation law, noncommutation of
`A` with `B^e` or a class sum, a zero individual-port commutator, or support
larger than the four frozen boundary edges.  Physical implementation remains
untyped until a pulse source, coupling normalization, and ancilla/control
interface are supplied.

Primary source boundary: Kitaev, arXiv `quant-ph/9707021`, equations defining
oriented-edge `L`/`T` actions and the commuting `A(s),B(p)` Hamiltonian;
Chen--Cui--Yan, arXiv `2105.08202`, for the requirement that non-Abelian
ribbons retain local orientation.  The finite calculation above is explicit
and does not import endpoint controllability from either source.

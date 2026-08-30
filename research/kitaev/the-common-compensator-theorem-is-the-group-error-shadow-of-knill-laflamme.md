# The common-compensator theorem is the group-error shadow of Knill–Laflamme

Owner: \`marici.Kitaev\`

## Question

Does the record-fiber common-compensator theorem survive for coherent quantum
error spaces, and which higher constructor cell replaces an ordinary decoder
partition?

## Claim boundary

This packet states the exact finite-dimensional quantum error-correction
criterion and identifies the group-error specialization. It does not derive a
microscopic recovery channel or establish fault tolerance.

## Quantum error span

Let \(P\) project onto a code subspace \(\mathcal C\). Let
\(\{E_a\}_{a\in A}\) span the admitted error space. Perfect correction by one
quantum channel exists exactly when there is a Hermitian matrix
\(\alpha=(\alpha_{ab})\) such that

\[
P E_a^\dagger E_b P
=
\alpha_{ab}P
\]

for all \(a,b\).

This is the Knill–Laflamme condition. The compressed relative errors contain no
logical-state information: every pair acts on the code as a scalar overlap.

The matrix \(\alpha\) is the coherent error Gram matrix. A classical partition
of the labels \(a\) does not retain its off-diagonal entries.

## Why detector fibers are insufficient

A measurement can assign the same classical record to several error operators.
For classical alternatives, one asks whether one correction works on every
member of that record fiber.

For coherent superpositions

\[
E=\sum_a z_aE_a,
\]

correctability must also preserve cross terms. Their code compression is

\[
P E^\dagger E P
=
\sum_{a,b}\overline z_a z_b\,
P E_a^\dagger E_b P.
\]

Hence diagonal success on each error separately is insufficient. The entire
pair matrix must be scalar on the code.

This is the higher constructor cell requested by the SCC hierarchy: a
positive-semidefinite coherent overlap matrix compatible with one recovery
channel.

## Group-error specialization

Suppose each \(E_a\) is a unitary group error. Two errors are code-equivalent
when

\[
P E_a^\dagger E_b P
=
\lambda_{ab}P
\]

for some scalar \(\lambda_{ab}\).

For Pauli stabilizer errors, this means their relative Pauli acts as a
stabilizer phase on the code. They may share a syndrome and one recovery
representative because they differ only by a code-trivial action.

If instead \(E_a^\dagger E_b\) acts as a nontrivial logical operator, the
compressed relative error is not scalar. Merging the two errors into one
decoder fiber violates Knill–Laflamme.

Thus the earlier safe-subgroup criterion is the discrete group shadow of the
scalar-compression law:

- safe subgroup element: acts trivially on the protected quotient;
- scalar compressed relative error: acts trivially on every code ray;
- common compensator: one recovery for the entire correctable class.

## Syndrome does not select a logical decoder

For a toric code, equal local syndrome means two Pauli chains have the same
boundary. Their relative product is a cycle.

- If that cycle is contractible, it is stabilizer-equivalent and the two errors
  are jointly correctable by one syndrome representative.
- If it is noncontractible, it acts as a logical Wilson loop and the compressed
  relative operator is not scalar.

Therefore local syndrome fibers are larger than Knill–Laflamme correctable
classes. Two additional logical loop coordinates refine the smallest-torus
fiber to the protected equivalence required for exact recovery.

This derives, rather than merely declares, why syndrome detects endpoints yet
does not choose a preferred decoder.

## Detection remains a lower cell

An error-detection condition only requires

\[
P E_a P
=
\lambda_a P.
\]

It says that one error has no nontrivial action within the code when conditioned
on remaining there. Correction of an error family requires the pairwise
condition on \(E_a^\dagger E_b\).

Hence:

\[
\text{individual detection}
\quad\not\Rightarrow\quad
\text{joint correction}.
\]

The failure of pairwise scalar compression is a failure of the recovery cell,
not a retroactive failure of the lower detector interaction.

## Minimal hostile pair

Choose two errors \(E_1,E_2\) that are individually detectable but satisfy

\[
P E_1^\dagger E_2 P
\]

non-scalar on \(\mathcal C\). A binary alarm may report “error” for both. Each
may have an individually tailored inverse. Nevertheless, no single recovery
channel corrects their coherent span.

For the toric code, take two same-syndrome chains differing by a
noncontractible logical loop. Their relative compression is that logical
operator, giving an exact hostile witness.

## Compatibility graph before quotient

Define pairwise compatibility by

\[
E_a\mathrel{\Gamma_{\mathcal C}}E_b
\quad\Longleftrightarrow\quad
P E_a^\dagger E_b P
\text{ is scalar on }\mathcal C.
\]

For arbitrary errors this relation need not be transitive, so it must not be
called an equivalence or quotient without a separate proof. A correctable error
family is a clique whose scalar coefficients assemble into the
positive-semidefinite Gram matrix \(\alpha\).

For Pauli stabilizer errors within a fixed syndrome sector, compatibility does
reduce to equivalence modulo the stabilizer: relative products are again Pauli
operators, and the protected-trivial subgroup supplies transitivity.

For general linear error spaces, an ordinary set quotient loses both possible
nontransitivity and coherent weights. The correct object is the compatibility
graph together with the Gram form on each correctable span.

## SCC schema consequence

The three SCC verdicts require different data:

- algebraic nonclosure: relation-to-kernel residual map;
- observable nonclosure: tester identity fiber and authorized context closure;
- correctable nonclosure, classical/group case: full record partition and
  fiberwise common compensators;
- correctable nonclosure, coherent quantum case: the compressed matrices
  \(P E_a^\dagger E_b P\), the scalar Gram matrix \(\alpha\), and an authorized
  recovery channel.

A checker that stores only residual labels and record partitions cannot certify
quantum correction.

## Deutschian explanation

The reason one recovery can correct many quantum errors is not that the
measurement identifies which error occurred. It is that all pairwise relative
errors are incapable of carrying logical-state information.

This is harder to vary than the slogan “measure the syndrome and invert the
error.” Degenerate errors may remain deliberately indistinguishable and still
be correctable; distinguishable errors may fail jointly because their coherent
cross term acts logically.

## Falsifiers

- Individually correctable errors are declared jointly correctable without
  pairwise compression.
- A classical record partition is used to certify a coherent error span.
- Same syndrome is treated as stabilizer equivalence.
- A noncontractible relative cycle is absorbed into a local repair class.
- The scalar matrix \(\alpha\) is fitted without verifying every compressed
  operator equality.
- Mathematical Knill–Laflamme correctability is promoted to an authorized,
  local, fault-tolerant recovery implementation.

## Disposition

The common-compensator theorem is exact for discrete group residuals. Its
quantum completion is the Knill–Laflamme scalar-compression condition. The
higher correction cell is the coherent error Gram matrix plus a recovery
constructor, not a finer alarm bit alone.

No checker, build, or Git operation was run for this research-only packet.

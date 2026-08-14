# The All-Arity A-Type Circuit Resolution

## Record

Date: 2026-08-13

Status: the marked-theta circuit resolution is the \(m=3\) case of an
all-arity integral theorem for \(K_{2,m}\).  Its graph homology is the root
lattice \(A_{m-1}\), and the \(m\) cyclic adjacent-road circuits give a
canonical nonsplit dihedral resolution

\[
\boxed{
0\longrightarrow\mathbb Z_{\chi_{\rm rel}}
\xrightarrow{\Delta}
\mathbb Z^m_{\rm tags}
\xrightarrow{B}
A_{m-1}
\longrightarrow0.}
\]

The unique cyclic-equivariant rational splitting has exact denominator \(m\).
The intrinsic integral object is the unsplit resolution, not that rational
section.

The algebraic proof is valid for every \(m\ge2\).  The Rust certificate audits
all ranks, Smith data, symmetry actions, and section identities for
\(2\le m\le12\).

Reproducible certificate:

    research/nima/check_k2m_circuit_resolution.rs

## Graph homology

Orient every edge of \(K_{2,m}\) from its core vertex to its road vertex.
Every cycle has the form

\[
(a_0,-a_0,\ldots,a_{m-1},-a_{m-1}),
\qquad
\sum_{i=0}^{m-1}a_i=0.
\]

Therefore

\[
\boxed{
H_1(K_{2,m};\mathbb Z)
\cong
A_{m-1}
=
\left\{
a\in\mathbb Z^m:\sum_i a_i=0
\right\}.}
\]

## The cyclic tag presentation

Let \(t_0,\ldots,t_{m-1}\) be formal oriented adjacent-road circuit tags and
define

\[
B(t_i)=e_i-e_{i+1},
\]

with indices modulo \(m\).  In coordinates,

\[
B(x)_i=x_i-x_{i-1}.
\]

The image is contained in \(A_{m-1}\).  Conversely, for any
\(a\in A_{m-1}\), the recurrence

\[
x_i=x_{i-1}+a_i
\]

has an integral cyclic solution because \(\sum_i a_i=0\).  Thus \(B\) is
surjective.  Its kernel consists exactly of constant vectors, proving the
saturated exact sequence

\[
0\longrightarrow\mathbb Z
\xrightarrow{1\mapsto(1,\ldots,1)}
\mathbb Z^m
\xrightarrow{B}
A_{m-1}
\longrightarrow0.
\]

This is the cellular chain sequence of the cyclic road graph, now interpreted
as a circuit-tag presentation of the Ward homology.

## Why the equivariant denominator is exactly \(m\)

Let

\[
A_{m-1}^{\rm tag}
=
\left\{
x\in\mathbb Z^m:\sum_i x_i=0
\right\}.
\]

The restriction

\[
B|_{A_{m-1}^{\rm tag}}:
A_{m-1}^{\rm tag}\longrightarrow A_{m-1}
\]

has finite cokernel.  Given \(a\in A_{m-1}\), choose any integral lift
\(x\) with \(Bx=a\).  Changing \(x\) by a constant vector changes
\(\sum_i x_i\) by a multiple of \(m\).  Hence

\[
\rho(a)=\sum_i x_i\pmod m
\]

is a well-defined surjection with kernel
\(B(A_{m-1}^{\rm tag})\).  Therefore

\[
\boxed{
A_{m-1}/B(A_{m-1}^{\rm tag})
\cong\mathbb Z/m.}
\]

Equivalently,

\[
\operatorname{SNF}(B|_{A_{m-1}^{\rm tag}})
=(1,\ldots,1,m).
\]

Over \(\mathbb Q\), rotation has no invariant functional on \(A_{m-1}\), so
every rotation-equivariant section of \(B\) must land in the sum-zero tag
space.  There \(B\) is invertible, giving a unique equivariant rational
section.  The cokernel above proves its denominator divides no proper divisor
of \(m\); an explicit root has a numerator coefficient equal to one, so the
exact denominator is \(m\).

Thus:

\[
\boxed{
\text{no integral }D_m\text{-equivariant splitting exists for }m\ge2.}
\]

No physical operation should therefore select such a split unless additional
pointing or symmetry-breaking data is present.

## Symmetry characters

With the induced orientation on tags, the diagonal relation line has
characters

\[
\chi_{\rm rel}(\text{rotation})=+1,
\qquad
\chi_{\rm rel}(\text{reflection})=-1,
\qquad
\chi_{\rm rel}(\text{core swap})=-1.
\]

On graph homology,

\[
\boxed{
\det(g|_{H_1})
=
\operatorname{sgn}(g|_{\rm roads})
(-1)^{(m-1)\operatorname{core\ swap}(g)}.}
\]

The two characters are generally different.  The relation cell therefore
carries its own orientation local system; it is not automatically the
determinant line of graph homology.

## Exact audit

For every \(2\le m\le12\), the certificate verifies:

- \(\operatorname{rank}H_1=m-1\);
- \(\operatorname{SNF}(B)=(1^{m-1},0)\);
- \(\operatorname{SNF}(B|_{A_{m-1}^{\rm tag}})
  =(1^{m-2},m)\);
- restricted determinant/index \(m\);
- 5,500 exact dihedral/core-swap covariance checks in total;
- 2,310 rational-section and denominator checks in total.

The \(m=3\) result reproduces entry 59 exactly: three tags, one diagonal
relation, index three, the \(1/3\) section numerator, and the reflected-tag
orientation sign.

## Consequence for the operation algebra

The residual Ward sector is not an arbitrary graph-dependent correction.  On
the family \(K_{2,m}\), it carries the canonical \(A_{m-1}\) root-lattice
resolution.  This suggests that the coefficient side of the scalar master
contains familiar integral representation-theoretic complexes before any
amplitude evaluation:

\[
\text{oriented circuit tags}
\longrightarrow
A\text{-type Ward homology}
\longrightarrow
\text{resolved surface coefficients}.
\]

The claim beyond the lattice theorem remains open.  Neither the existence of
the tags as scalar-derived physical generators nor their Cut-natural
realization follows from graph homology alone.

## Evidence boundary

Proved for all \(m\ge2\):

- the \(A_{m-1}\) graph-homology identification;
- the saturated cyclic tag resolution;
- the cyclic quotient \(\mathbb Z/m\);
- Smith type \((1,\ldots,1,m)\);
- uniqueness and exact denominator \(m\) of the equivariant rational section;
- the stated symmetry characters.

Independently checked by exact finite arithmetic for \(2\le m\le12\).

Not proved:

- a scalar-derived circuit-tag coefficient system for general \(m\);
- a physical Ward-to-tag chain map;
- Cut or modular compatibility;
- a relation between these \(K_{2,m}\) carriers and arbitrary ribbon graphs.

## Next falsifier

Construct the scalar first-jet coefficient map for \(K_{2,4}\), the first
case beyond the marked theta.  It must land in the unsplit four-tag resolution,
carry the relation character, and commute with one edge deletion

\[
K_{2,4}\longrightarrow K_{2,3}
\]

and one nonseparating Cut.  Any construction that requires choosing a
\(1/4\) section has discarded the integral carrier too early.

## Internal dependencies

- Entry 57: general flag-incidence Ward exact sequence.
- Entries 59--60: the \(m=3\) circuit bridge and integral state resolution.
- Working context: research/nima/ward_brauer_math_context.md.

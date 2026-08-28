# Determinant-preserving attachment needs vanishing mixed return moments

## Coupling can corrupt the Euler grammar

Let \(A\) be the acyclic boundary transport, let \(q\) be one primitive
Euler loop, and let \(b,c\) be incidence and return maps. The coupled state
operator is

\[
M=
\begin{pmatrix}
A&b\\
c&q
\end{pmatrix}.
\]

Even when \(A\) is nilpotent, bidirectional coupling can create new closed
walks that pass through the boundary and return to the primitive loop. Those
walks contribute additional cyclic traces and are not prime powers of the
original Euler loop.

## Exact Schur gate

Since \(I-A\) is invertible,

\[
\det(I-M)
=
\det(I-A)
\left(
1-q-c(I-A)^{-1}b
\right).
\]

For acyclic \(A\), \(\det(I-A)=1\). Define the mixed return transfer

\[
h=c(I-A)^{-1}b.
\]

The primitive Euler factor \(1-q\) is preserved exactly when \(h=0\).

The parameterized version is stronger. Because \(A^N=0\),

\[
c(I-tA)^{-1}b
=
\sum_{j=0}^{N-1}t^j cA^jb.
\]

It vanishes identically exactly when every mixed return moment vanishes:

\[
cA^jb=0
\]

for \(0\leq j<N\).

## Two lawful outcomes

There are only two correctly typed cases.

First, all mixed return moments vanish. The boundary incidence may carry state
and comparison data, but it does not alter the Euler determinant. The
primitive loop remains the sole source of its prime-power cyclic grades.

Second, some mixed return moment is nonzero. Then the attachment creates a
genuine relative determinant factor. That factor must be retained and derived
as part of the Euler–theta comparison; it cannot be silently absorbed into
the primitive Euler loop.

Thus the previous phrase “incidence-and-return feedback” needs qualification.
The primitive loop supplies its own authorized feedback. Boundary coupling is
external comparison data unless a source theorem authorizes the additional
mixed cycles.

## Finite hostile

Take \(A\) to be a length-\(N\) shift. Couple the loop into the terminal
boundary state and return from the initial state. Then

\[
cA^{N-1}b=1.
\]

The attachment creates one new cycle of length \(N+1\). All lower finite
checks can remain unchanged while the first contaminated cyclic trace appears
only at that depth.

This is a delayed hostile: checking only primitive and square grades does not
certify a long attachment.

## DPC verdict

Resolved:

- the exact determinant-preserving attachment condition;
- its equivalent finite family of mixed return moments;
- the distinction between comparison incidence and a new relative
  determinant;
- a delayed-cycle falsifier invisible below its return length.

Withheld:

- the source values of \(b\) and \(c\);
- whether the theta moving-seam comparison produces zero or nonzero mixed
  moments;
- locally uniform completion bounds;
- the zero-state-to-flux bridge.

The next source calculation is finite at every cutoff: construct the actual
incidence and return maps, then compute \(cA^jb\) before taking any
determinant or scalar projection.

## Verification

The checker `check_determinant_preserving_attachment.py` verifies a
moment-free nontrivial attachment and a delayed hostile whose first extra
cyclic trace occurs at the predicted return length.

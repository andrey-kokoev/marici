# Spin-two grade-three constructor-rigidity falsifier

## Question

Do rotation covariance, fourth differential order, input spin two, and output
spin four force the 21-dimensional kernel of \(\bar\eth\eth^3\)?

No. These data admit four words containing three raising steps \(E=\eth\) and
one lowering step \(B=\bar\eth\). To avoid composition-order ambiguity, words
below list operations in the order in which they act on the source.

## Exact word census

For a current spin \(t\), the squared ladder factors are

\[
E_t^2=(l-t)(l+t+1),\qquad
B_t^2=(l+t)(l-t+1).
\]

Starting at spin two gives:

| Acting word | Conventional composite | Kernel degrees | Kernel dimension | Cokernel dimension | Index |
|---|---|---:|---:|---:|---:|
| `EEEB` | \(\bar\eth\eth^3\) | \(2,3,4\) | 21 | 9 | 12 |
| `EEBE` | \(\eth\bar\eth\eth^2\) | \(2,3\) | 12 | 0 | 12 |
| `EBEE` | \(\eth^2\bar\eth\eth\) | \(2,3\) | 12 | 0 | 12 |
| `BEEE` | \(\eth^3\bar\eth\) | \(2,3\) | 12 | 0 | 12 |

All four words have the same leading symbol: in the flat-symbol limit the
raising and lowering derivatives commute. On the sphere they differ by
curvature commutators, which are lower-order terms. Those lower-order terms
decide whether the target endpoint representation \(l=4\) is killed or
reached.

## What is invariant

The Fredholm index remains 12. Moving the lowering step leftward in the
conventional composite removes the nine-dimensional \(l=4\) kernel block and
simultaneously fills the nine-dimensional lowest target block. Thus ordering
changes kernel and cokernel separately while preserving their difference:

\[
(21,9)\longrightarrow(12,0),
\qquad
21-9=12-0.
\]

This is the unexpected stable object. The index is protected by the principal
symbol class; the 21-dimensional kernel is protected only by the ordered
constructor.

## Explanatory consequence

The earlier endpoint theorem remains exact conditional on
\(\bar\eth\eth^3\), but covariance, order, and spin typing do not derive that
word. A physical explanation of 21 must supply a source law selecting the
ordering, or an equivalent condition that forbids the other three words. A
numerical observation of 21 cannot itself authorize the selection.

The next source-side candidates are:

1. a variational or adjoint factorization fixing the ordered word;
2. a conservation law demanding annihilation of the complete \(l=4\) block;
3. a boundary-domain condition under which only `EEEB` is closed or
   admissible;
4. a gauge complex whose differential composition is exactly `EEEB`.

Absent one of these, the strongest statement is a conditional kernel theorem
plus an index-rigidity theorem, not constructor rigidity.

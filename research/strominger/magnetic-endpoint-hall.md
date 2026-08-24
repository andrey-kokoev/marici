# Hall deficiency isolates the magnetic circuit blocks

Companion to `checkers/magnetic_endpoint_hall_checks.py` (8/8, exit 0) and
`results/magnetic_endpoint_hall.json`. This packet executes Nima's directed
event 2707. It remains combinatorial and does not reconnect potentials,
residues, logarithms, or physics.

## 1. Reflected blocks as interval-supported matrices

For fixed grade \(g\), pole set \(A_k=\{0,2,\ldots,2k\}\), and reflected
distance \(q>0\), the component contains the two source vertices

\[
(a,1-g-q-a),\qquad(a,1-g+q-a)
\]

for every \(a\in A_k\). Their canonical columns are finite weighted paths in
one integer row coordinate. Deleting zero coefficients gives the actual
bipartite support graph; filling gaps between the first and last nonzero rows
gives its interval hull.

A complete matching supplies distinct candidate pivot rows. Failure of Hall's
condition certifies rank deficiency independently of coefficient values.

## 2. Wide Hall classification

Exact support matching was performed for

\[
2\le g\le30,\qquad0\le k\le15,\qquad1\le q\le60,
\]

a total of 27,840 reflected blocks. There are exactly 29 deficient blocks:

- \(g=2,q=1\) for every \(0\le k\le15\);
- \(g=2,q=7\) for every \(3\le k\le15\).

Every deficiency is one. Moreover, the actual nonzero support and its interval
hull have the same matching number in every block. Internal coefficient gaps
therefore introduce no extra Hall obstruction in the tested range.

These are exactly the two families already carrying the primitive circuits

\[
E_1=1-\bar z^{-2},
\qquad
E_2=\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6}.
\]

## 3. Internal-cancellation falsifier

A complete matching is a support statement, not automatically a nonzero
determinant: multiple determinant permutations might cancel. The directed
falsifier asks for a block with complete support matching but deficient exact
rank.

For each \(2\le g\le20\), \(1\le q\le30\), the maximal pole block
\(A_{10}\) was reduced exactly, 570 blocks total. A full-rank maximal block
implies every smaller pole block is independent because it is a column subset.
Only \((g,q)=(2,1),(2,7)\) lose rank, and both already fail Hall. No
complete-matching/internal-cancellation block occurs in this exact range.

The two singular maximal blocks were also checked at every smaller
\(0\le k\le10\). Their dependencies appear exactly when the full circuit
support is admitted.

## 4. Why raw endpoints are not enough

The phrase "endpoint pivot" must not be weakened to "all left endpoints are
distinct" or "all right endpoints are distinct." The smallest counterexample
to that shortcut is

\[
(g,k,q)=(2,1,3).
\]

Its four source vertices are

\[
(0,-4),(0,2),(2,-6),(2,0).
\]

The canonical supports have left endpoints \((0,3,-4,0)\) and right
endpoints \((1,4,-1,1)\), so both raw endpoint lists collide. Nevertheless a
Hall matching selects rows \((1,3,-4,0)\), and the corresponding maximal
minor has

\[
\det=-6{,}912{,}000\ne0.
\]

Thus raw extremes do not provide the desired triangular proof. The correct
object is a matching of the full consecutive support intervals, followed by a
noncancellation argument for the selected minor.

## 5. Smith/kernel cores

The deficient cores reduce exactly to

\[
(-40,-40)
\]

and

\[
\begin{pmatrix}-120&0&60\\-160&-40&20\end{pmatrix}.
\]

Their primitive kernel vectors are \((-1,1)\) and \((1,-3,2)\). For the
second block, the gcd of the signed maximal minors is \(2400\), recovering the
primitive circuit coordinate canonically up to sign.

## 6. Demonstrated strength

This is a finite-range endpoint-Hall theorem and a negative result for the
internal-cancellation falsifier over the exact rank range. It does not prove
unbounded injectivity.

The remaining proof obligation has two precise parts:

1. prove for arbitrary \((g,k,q)\) that Hall deficiency occurs only in the
   two displayed grade-2 families;
2. prove that a Hall-selected maximal minor cannot cancel internally outside
   those families.

A resultant or signed-network argument may close the second part, but no such
symbolic noncancellation theorem is claimed here.

## Verification

`uv run --with sympy python -u research/strominger/checkers/magnetic_endpoint_hall_checks.py`
passes 8/8. Coverage: 27,840 Hall blocks, 570 exact maximal-block ranks, 22
exceptional subset ranks, the smallest endpoint-shortcut counterexample and
its exact minor, and both primitive circuit cores.

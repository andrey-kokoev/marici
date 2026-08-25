# Sheet-equivariant observability decomposes by character

## Theorem

Let \(R^2=I\) act on a finite-dimensional state space over a field of
characteristic different from two, and suppose

\[
[A,R]=0.
\]

Then

\[
V=V_+\oplus V_-,
\qquad R|_{V_\pm}=\pm I,
\]

and both parity subspaces are invariant under \(A\).

If an output has character \(\chi\),

\[
JR=\chi J,
\qquad \chi\in\{+1,-1\},
\]

then it kills the opposite state sector. For example, if \(J_+R=J_+\) and
\(v\in V_-\),

\[
J_+v=J_+Rv=-J_+v,
\]

so \(J_+v=0\). Since \(A^kv\in V_-\), every Krylov output also vanishes:

\[
J_+A^kv=0\quad\text{for all }k.
\]

Thus a purely even Clark channel can never observe an odd invariant state,
no matter how long the system evolves. The dual statement holds for a purely
odd output.

## Orbit-versus-character theorem

For an arbitrary output \(J\), its sheet orbit is \((J,JR)\). Define

\[
J_+=\frac{J+JR}{2},
\qquad
J_-=\frac{J-JR}{2}.
\]

The orbit pair and the character pair are related by the invertible Hadamard
row transformation

\[
\begin{pmatrix}J\\JR\end{pmatrix}
=
\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\begin{pmatrix}J_+\\J_-\end{pmatrix}.
\]

Consequently they have exactly the same observability content. Two
sheet-related measurements add information only if both character projections
are nonzero and dynamically observable on their respective blocks. Duplicating
a pure even output gives no new rank.

## Minimality is dynamical

The number of extra physical rows need not equal the dimension of the hidden
sector. One scalar odd row can observe a multi-dimensional odd block when

\[
J_-,J_-A_-,\ldots
\]

span its dual. The correct minimum is therefore the least output rank whose
restricted Krylov matrix has full rank, or equivalently the maximum PBH
geometric multiplicity that must be separated—not the raw hidden dimension.

## Exact model

Take identical nilpotent two-dimensional dynamics on both parity blocks:

\[
A_+=A_-=
\begin{pmatrix}0&1\\0&0\end{pmatrix},
\qquad
R=\operatorname{diag}(1,1,-1,-1).
\]

The even row \((1,0,0,0)\) observes the complete even block but has total
rank two. The odd row \((0,0,1,0)\) similarly observes the complete odd
block. Together their observability rank is four. Hence one additional odd
row repairs a two-dimensional hidden sector through dynamics.

## Theta/Tate audit protocol

For every source-derived cutoff:

1. Verify \([A_X,R_X]=0\). A nonzero commutator is a typed symmetry-breaking
   residual, not something to discard.
2. Form the actual output character projections
   \(J_{X,\pm}=(J_X\pm J_XR_X)/2\).
3. Compute observability and PBH ranks separately on \(V_{X,+}\) and
   \(V_{X,-}\).
4. Determine whether the seam, primitive, and square-current rows introduce
   new restricted Krylov rank or merely duplicate an existing character row.
5. Bound both restricted Gramians uniformly through completion.

If the decomposition is orthogonal and the output Gramian has no parity-mixed
terms, the full lower bound is the minimum of the two block lower bounds. A
collapse in either character sector defeats completion-stable observability.

## Source boundary

This theorem explains exactly what the sheet symmetry would imply. It does
not prove that Grothendieck's completed tail generator commutes with the Clark
involution, nor assign characters to the actual seam and current rows. Those
are source calculations. If \([A_X,R_X]\ne0\), parity mixing may dynamically
reveal a nominally hidden sector, and the full unsplit observability matrix
must be used.

## Verification

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_c2_observability_decomposition.py
```

The checker verifies the invariant blocks, character blindness, PBH witness,
Hadamard equivalence, and one-row dynamical repair using exact rational
matrices.

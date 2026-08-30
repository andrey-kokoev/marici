# The Five-Channel Relative Clifford Form Is Degree-Global

## Question

The split five-channel carrier repairs the first relative degree comparison.
Does one quadratic form work for every adjacent degree map?

Yes. The same invariant family works symbolically for all \(j\ge0\).

## Adjacent relative map

Let

\[
\widetilde M_j=
\operatorname{diag}(M_j,b_j^{-1},c^{-1}),
\qquad
b_j=\frac32\left(j+\frac54\right).
\]

The adjacent comparison is

\[
R_j=\widetilde M_{j+1}\widetilde M_j^{-1}.
\]

Exact simplification gives

\[
R_j=
\begin{pmatrix}
\dfrac{4j+9}{4j+5}&-\dfrac{14}{4j+5}&-\dfrac{4}{c(4j+5)}&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&\dfrac{4j+5}{4j+9}&0\\
0&0&0&0&1
\end{pmatrix}.
\]

Its spectrum is

\[
\left\{
1,1,1,
\frac{4j+9}{4j+5},
\frac{4j+5}{4j+9}
\right\}.
\]

The expansion and contraction remain exact reciprocal partners at every
degree.

## One invariant family for all degrees

For arbitrary real parameters \(a,b,d,e,f,g,u\), define

\[
Q=
\begin{pmatrix}
0&0&0&-cu&0\\
0&a&b&7cu/2&d\\
0&b&e&u&f\\
-cu&7cu/2&u&0&0\\
0&d&f&0&g
\end{pmatrix}.
\]

Then the symbolic identity

\[
R_j^TQR_j=Q
\]

holds for every \(j\). Its determinant is

\[
-c^2u^2
\left(
-f^2a+2fbd+gae-gb^2-d^2e
\right).
\]

Nondegenerate specializations therefore exist. Every finite product

\[
R_{k-1}\cdots R_{j+1}R_j
\]

preserves the same form.

## Why the fifth channel mattered

The fourth determinant-dual channel recovered only the product of two dual
responses. Splitting it into tail-area dual and wall dual exposes:

- a reciprocal expansion-contraction pair;
- three neutral modes;
- the fixed shear incidence coupling the tail, wall, and comparison sectors.

The coefficient \(7/2\) in the invariant form is not fitted separately at
each degree. It is forced by the constant ratio between the two shear entries
of \(R_j\).

## Geometric interpretation

The degree direction now carries a genuine relative orthogonal connection.
Individual source transfers \(\widetilde M_j\) need not be isometries of one
fixed fiber metric. Their adjacent comparisons are isometries of a common
five-dimensional form. This is a groupoid statement: geometry belongs to
comparisons between presentations, not to any isolated presentation.

No sixth channel is requested by degree transport. The remaining freedom is
the seven-parameter invariant-form family. A physical metric still requires
source selection through the Mellin residue pairing, positivity or signature
typing, endpoint orientation, or compatibility with exponent transport.

## Relation to the four-rung tower

The result does not identify five carrier coordinates with five categorical
rungs. Instead it exhibits the four-rung pattern operationally:

1. source fibers carry the tail and wall state;
2. degree transfer relates successive fibers;
3. the two comparison ports make those relations coherently orthogonal;
4. scalar or blade readouts may be taken only after this closure.

## Next falsifier

Benincasa's proposed Pearson-shift, residue-restriction, and scalar-pushforward
square supplies the missing second direction. Transport its action to the
five-channel carrier and test whether it preserves the same \(Q\), preserves
only its conformal class, or produces a typed anomaly. That loop test can
select or reject the remaining metric parameters.

## Verification

The checker
`research/grothendieck/checkers/five_channel_degree_global_clifford.py`
verifies the symbolic all-degree identity, reciprocal characteristic
polynomial, nonzero determinant specialization, and finite-product
invariance.

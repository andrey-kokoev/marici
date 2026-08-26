# The Mellin–Rees Gysin Sequence Is Exact and Degree-Natural

## Question

Exponent transport is singular on every square finite-jet truncation. What is
the smallest correctly typed replacement, and does it remain coherent with
source degree transport?

The replacement is a short exact sequence. It is natural under the exact
Gamma degree shift and remains exact under formal jet completion.

## Wall-germ sequence

Let \(A\) be the algebra of analytic germs at \(y=0\). Multiplication by the
wall coordinate and evaluation at the wall give

\[
0\longrightarrow A
\xrightarrow{\;y\;}
A
\xrightarrow{\;\operatorname{ev}_0\;}
\mathbb R
\longrightarrow0.
\]

Multiplication by \(y\) is injective. Its image is exactly the ideal of germs
vanishing at the wall, which is the kernel of evaluation. Evaluation is
surjective. Hence the sequence is exact.

The quotient

\[
A/yA
\simeq
\mathbb R
\]

is the boundary/Gysin grade. Under Mellin continuation it is the first
residue coordinate.

## Correct finite jets

Let

\[
A_N=\mathbb R[y]/(y^{N+1}).
\]

The square map \(A_N\xrightarrow{y}A_N\) is nilpotent and loses the terminal
jet. The correctly typed finite sequence changes dimension:

\[
0\longrightarrow A_{N-1}
\xrightarrow{\;y\;}
A_N
\xrightarrow{\;\operatorname{ev}_0\;}
\mathbb R
\longrightarrow0.
\]

Its dimensions are \(N\), \(N+1\), and one. Multiplication by \(y\) has rank
\(N\), is injective on \(A_{N-1}\), and its image is precisely the
codimension-one evaluation kernel.

The missing boundary coordinate is therefore not repaired by wrapping the
last jet back to the first. It is represented by the explicit quotient.

## Degree naturality

The source germs obey

\[
f_{j+1}(y)=ce^y f_j(y).
\]

Let \(D\) denote multiplication by \(ce^y\). Since scalar multiplication of
germs commutes,

\[
D(yf)=yD(f).
\]

At the boundary,

\[
\operatorname{ev}_0(Df)
=c\operatorname{ev}_0(f).
\]

Thus degree transport gives a chain map of the short exact sequence: it acts
by \(D\) on both germ terms and by multiplication by \(c\) on the Gysin
quotient. The wall scaling \(W_{j+1}=cW_j\) is forced by this naturality
square.

This is the source-derived coherence that the earlier five-channel matrix
could only encode as a wall comparison mode.

## Completion

The truncation maps

\[
A_N\longrightarrow A_{N-1}
\]

are surjective and commute with the finite exact sequences. The inverse
system therefore satisfies the Mittag–Leffler condition. Its first derived
limit vanishes, and inverse-limit exactness yields

\[
0\longrightarrow\mathbb R[[y]]
\xrightarrow{\;y\;}
\mathbb R[[y]]
\xrightarrow{\;\operatorname{ev}_0\;}
\mathbb R
\longrightarrow0.
\]

So the polar formal completion does not create a hidden cohomology class.
The earlier completion obstruction belongs to unbounded logarithmic
translations on the global entire-germ carrier, not to this local Rees
sequence.

## Relation to the five-channel geometry

The wall comparison channel now has source provenance: it is dual to the
Gysin quotient and transforms contragrediently to the boundary scaling \(c\).
The tail-area comparison channel remains tied to the determinant of the
two-dimensional Pearson tail block.

The five-channel split is therefore no longer merely a successful spectral
completion. Its two comparison modes arise from two different exact objects:

1. determinant dual of the invertible tail plane;
2. dual of the noninvertible exponent-shift cokernel.

## Remaining gate

The local polar sequence is exact and degree-natural. What remains is to
attach its analytic regular Mellin strip and the Pearson pushforward without
losing the five-channel pairing. The first falsifier is a nonzero chain
homotopy residual when the meromorphic Pearson identity is totalized with
this Gysin sequence.

## Verification

The checker
`research/grothendieck/checkers/mellin_rees_gysin_exact_sequence.py` verifies
finite exactness, degree naturality under truncated multiplication by
\(ce^y\), and compatibility of truncation maps through jet order twelve.

# The full extended target restores site exchange but mixes routes with support

## Question

Although the two added support vectors are not setwise invariant, does natural site exchange lift to the complete four-generator target enlargement?

## Claim boundary

This constructs an exact integral symmetry of the algebraic enlargement. It does not identify that symmetry with a physical exchange operation or prove the added generators are geometric boundary strata.

## Ambient site exchange

In the occurrence basis \((++,+-,-+,--)\), natural wall exchange is

\[
T=\begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix}.
\]

It swaps the middle two occurrence points. The ambient comparison into the extended target is the unimodular matrix

\[
P=\begin{pmatrix}
0&0&0&1\\
0&1&0&0\\
1&0&0&-1\\
0&0&1&-1
\end{pmatrix},
\qquad \det P=1.
\]

Therefore site exchange has a unique transported action

\[
A=PTP^{-1}
=
\begin{pmatrix}
1&0&0&0\\
1&0&0&1\\
0&0&1&0\\
-1&1&0&0
\end{pmatrix}.
\]

It is integral and involutive:

\[
A^2=I_4.
\]

## Compatibility with the differential

Let the extended generators be

\[
(f_{\log},f_{\rm face},s_1,s_2)
\]

with differential columns

\[
D_{\rm ext}=(r,-r,q_1,q_2).
\]

If \(S\) swaps the first two enhanced residue coordinates, then

\[
D_{\rm ext}A=SD_{\rm ext},
\qquad
AP=PT.
\]

Thus the full ambient chain comparison is naturally site-equivariant.

## Route/support mixing

The action on generators is

\[
A f_{\log}=f_{\log}+f_{\rm face}-s_2,
\qquad
A f_{\rm face}=s_2,
\]

\[
A s_1=s_1,
\qquad
A s_2=f_{\rm face}.
\]

Natural site exchange therefore does not preserve the two-dimensional span of the original Aspect route generators. It exchanges the face leg with one support generator and sends the logarithmic leg to a mixed representative.

The closed two-leg combination is nevertheless fixed:

\[
A(f_{\log}+f_{\rm face})
=f_{\log}+f_{\rm face}.
\]

This separates invariant closed content from non-invariant route presentation. Removing the support sectors destroys the site action even though the closed sum survives.

## Speculative interpretation

The rank-two support completion may be required not only for ambient descent but also for symmetry closure: route labels and boundary-support labels form one integral representation, while only their closed combination is invariant. This resembles the relative totalization in which a bulk or one-boundary representative acquires deeper boundary components under comparison.

The analogy remains unverified because no physical source map assigns \(s_1,s_2\) to actual strata.

## Disposition

The previous failure of setwise invariance applies to the isolated support pair, not to the full extended target. The full four-generator completion restores natural site exchange exactly, at the cost of mixing one Aspect route with support. Any physical interpretation that insists the two routes form an invariant subspace is incompatible with this minimal ambient completion.

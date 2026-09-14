# The total-energy parameter match lands on a triple relative divisor

## Question

Does the total-energy Kummer-coordinate match define a pullback of the selected relative Gauss–Manin subconnection to the conductor locus?

## Claim boundary

This analyzes the support arrangement reached by the previously derived parameter formulas. It does not construct nearby cycles or choose a transverse deformation.

## Forced divisor intersection

On the conductor total-energy component, the derived relative coordinates are

\[
X_{1,\mathrm{rel}}=Y_{\mathrm{rel}},
\qquad
X_{2,\mathrm{rel}}=-Y_{\mathrm{rel}}.
\]

Therefore three factors of the relative arrangement vanish simultaneously:

\[
B=X_1-Y=0,
\qquad
C=X_2+Y=0,
\qquad
E=X_1+X_2=0.
\]

The proposed parameter map lands entirely in the triple intersection \(B=C=E=0\), not in the complement on which the logarithmic connection is an ordinary bundle connection.

Consequently the expressions

\[
d\log B,
\qquad d\log C,
\qquad d\log E
\]

have no ordinary pullback along this map. The scalar identity \(Y_{\rm rel}=\pm2xy\) therefore cannot by itself define the desired connection comparison.

## Transverse residue family

Let a deformation coordinate \(q\) approach the triple intersection with vanishing orders

\[
B\sim q^{m_B},
\qquad
C\sim q^{m_C},
\qquad
E\sim q^{m_E}.
\]

The resulting normal residue on the selected relative subconnection is

\[
R(m_B,m_C,m_E)=m_BR_B+m_CR_C+m_ER_E.
\]

Its characteristic polynomial is

\[
\lambda(\lambda-2m_E)(\lambda-m_B-m_C).
\]

Thus every such normal approach has a one-dimensional common kernel. The specialization can create exactly the flat-line dimension missing from the generic relative subconnection.

For equal vanishing orders,

\[
m_B=m_C=m_E=1,
\]

the combined residue is

\[
R_{\rm eq}=
\begin{pmatrix}
2&0&0\\
-1&1&1\\
1&1&1
\end{pmatrix},
\]

with eigenvalues \(0,2,2\). This resembles the one-flat-plus-two-equal-Kummer shape expected when the two conductor discriminants coincide.

## Why this is not yet the comparison

The integers \((m_B,m_C,m_E)\) are additional normal-approach data. The exact total-energy map does not choose them. Different values change the two nonzero residue eigenvalues, so the limiting connection is path-dependent until a deformation or nearby-cycle functor is specified.

Moreover the normal residue measures loop transport around the relative divisor intersection. The conductor Kummer form varies along its own parameter base through \(xy\). Equality of residue eigenvalue patterns does not identify normal loop transport with tangential conductor variation.

## Required source object

A valid specialization now requires a source-derived map from a normal deformation of the conductor total-energy locus to the relative arrangement, including:

- vanishing orders of \(B,C,E\);
- orientation of the normal loop;
- a nearby-cycle or Deligne-extension prescription;
- a comparison between the resulting limiting connection and the conductor Kummer connection.

## Disposition

The total-energy parameter match resolves the generic flat-line obstruction only at the level of a path-dependent normal residue. It does not define an ordinary pullback connection. The first missing typed object is the normal-deformation and nearby-cycle map at \(B=C=E=0\).

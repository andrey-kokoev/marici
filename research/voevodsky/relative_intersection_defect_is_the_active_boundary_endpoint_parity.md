# The relative intersection defect is the active-boundary endpoint parity

## Question

What concrete mod-two functional detects the index-two defect of the mined relative intersection matrix, and does it respect the source's boundary-stratum labels?

## Claim boundary

This identifies the unique mod-two cokernel character in the displayed basis. Its interpretation as an integral parity observable remains conditional on those differential-form bases carrying source-authorized integral lattices.

## Labelled basis

The source orders its dual relative basis as one class on the active one-boundary \(S_3\), followed by the three point classes:

\[
(\delta_3\phi_1,\delta_{12}(1),\delta_{23}(1),\delta_{13}(1)).
\]

For the displayed intersection matrix

\[
C=
\begin{pmatrix}
0&-1&1&0\\
1&0&0&0\\
1&1&0&1\\
-1&0&1&-1
\end{pmatrix},
\]

reduction modulo two has rank three.

## Unique cokernel character

The unique nonzero row character annihilating \(C\) modulo two is

\[
\ell_{\rm rel}=(1,0,1,1).
\]

Indeed,

\[
\ell_{\rm rel}C=0\pmod2.
\]

Therefore an integer vector in the image of \(C\) must satisfy

\[
y_{S_3}+y_{S_{23}}+y_{S_{13}}=0\pmod2.
\]

The coefficient of \(S_{12}\) is zero. The arithmetic defect therefore involves exactly the active one-boundary and its two incident endpoint strata, while excluding the point stratum not incident to \(S_3\).

This matches the support pattern in equations (3.39)–(3.40): the two restrictions to \(S_{23}\) and \(S_{13}\) are active, while the \(S_{12}\) coefficient vanishes.

## Conductor comparison

The elementary conductor factors have mod-two cokernel characters

\[
\ell_1=(1,0,1),
\qquad
\ell_2=(0,1,1).
\]

Their product imposes both relations, equivalently

\[
u=v=w\pmod2.
\]

Thus each conductor parity factor has the same abstract form as one boundary-incidence parity constraint, and site exchange swaps the two characters.

## Candidate parity-sensitive record

If an integral relative lattice is derived, the minimal parity-sensitive record is not a complex period. It is evaluation of the corresponding cokernel character modulo two. For the mined example this record tests whether the active-boundary coefficient and its two endpoint coefficients have even total parity.

A conductor realization would need two wall-labelled versions of this test whose transported characters are \(\ell_1\) and \(\ell_2\).

## Strongest falsification attempt

The mod-two character is basis-specific until integrality and normalization of the displayed relative basis are proved. A half-rescaling can remove or relocate the apparent parity relation over the coefficient field. Therefore this calculation supplies an acceptance test for a future integral pairing, not an already physical binary record.

## Disposition

The relative index-two defect is localized exactly to active-boundary endpoint incidence parity. The remaining constructor is an integral cycle/form lattice and comparison transporting this character to each conductor wall.

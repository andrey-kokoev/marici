# PDF clue: the missing route period is a local residue pairing

## Source

`references/pdfs/Cosmology meets cohomology - 2308.03753.pdf`, PDF pages 17–18 and Appendix A, PDF pages 38–39.

## Clue

The paper treats dual relative twisted classes supported on boundaries as residue operators. Its equation (A.1) reduces pairing with a boundary class \(\delta_I(\check\varphi_I)\) to pairing \(\check\varphi_I\) with \(\operatorname{Res}_I\varphi\). Equation (A.2) then computes the latter as a sum of ordinary local residues at maximal-codimension intersection points \(z_*\in\operatorname{Int}_I\).

Two useful consequences are stated explicitly:

1. the pairing vanishes when the dual boundary form and the residue of the primal form share no singular point;
2. dependent boundary operators can be detected by the rank of their intersection matrix (PDF pages 34–35 give an example where residue operators are identified this way).

## Application to the pyramid gate

This provides a route around the unavailable global marked-reflection square. For the reflected split fiber

\[
q=-(y+z),
\]

use its two components

\[
C_2^\pm:\quad W=\pm Q_2
\]

and represent the oriented difference \(d_2=[C_2^+]-[C_2^-]\) by the corresponding dual relative boundary class. Then compute

\[
\langle d_2,v_{\rm alg}\rangle
=
\sum_{\epsilon=\pm}\epsilon
\sum_{z_*\in\operatorname{Int}(C_2^\epsilon)}
\operatorname{Res}_{z_*=0}
\left(
\frac{\operatorname{Res}_{C_2^\epsilon}(\varphi_{v_{\rm alg}})}
{\prod_i\check\alpha_i}
\right),
\]

with the local twist coefficients \(\check\alpha_i\) fixed by the dual connection, as in (A.2).

Only local equations at the reflected components and a logarithmic representative \(\varphi_{v_{\rm alg}}\) are needed. A global Betti marking is unnecessary for deciding zero versus nonzero.

## Concrete next computation

1. Extract the de Rham representative of
   \[
   v_{\rm alg}=x^2y^2((x^2-y^2)e_7+2e_8-2e_9).
   \]
2. Restrict it to \(C_2^+\) and \(C_2^-\).
3. Enumerate maximal intersections of each component with its remaining polar divisors and infinity.
4. Evaluate the local residues with orientation signs \((+1,-1)\).
5. If no singularities are shared, the route is null immediately. Otherwise the signed residue sum gives the required normalization.

This is the first source-backed computational method found for the missing route period.
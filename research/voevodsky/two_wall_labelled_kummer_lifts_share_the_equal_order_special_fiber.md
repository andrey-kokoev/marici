# Two wall-labelled Kummer lifts share the equal-order special fiber

## Question

Can the first-order split of the two conductor square roots be accommodated by two explicit relative parameter maps while retaining the required equal-order nearby residue?

## Claim boundary

This constructs parameter maps on the two oriented Kummer covers. It does not construct relative cycles, a Deligne extension, or a physical contour.

## Wall-labelled covers

For each conductor wall let

\[
Y_i(E)^2=\Delta_i(E),
\qquad i\in\{1,2\},
\]

with orientation chosen so that on the total-energy fiber

\[
Y_1(0)=Y_2(0)=Y_0=2xy.
\]

The two functions have different first normal jets when \(x\ne y\), so retain their wall labels.

## Relative parameter maps

For each \(i\), define

\[
\Phi_i:
\quad
Y_{\rm rel}=Y_i(E),
\qquad
X_{1,\rm rel}=Y_i(E)+E,
\qquad
X_{2,\rm rel}=-Y_i(E)+E.
\]

Then the three vanishing relative factors pull back exactly as

\[
\Phi_i^*(X_1-Y)=E,
\qquad
\Phi_i^*(X_2+Y)=E,
\qquad
\Phi_i^*(X_1+X_2)=2E.
\]

These formulas are independent of the first derivative of \(Y_i\). Therefore both wall-labelled maps have the same primitive equal-order normal residue

\[
(m_B,m_C,m_E)=(1,1,1).
\]

The complementary factors become

\[
\Phi_i^*(X_1+Y)=2Y_i(E)+E,
\]

\[
\Phi_i^*(X_2-Y)=-2Y_i(E)+E,
\]

and remain nonzero near \(E=0\) away from \(xy=0\).

## Common special fiber and split jets

At \(E=0\), both maps reduce to

\[
(Y_{\rm rel},X_{1,\rm rel},X_{2,\rm rel})
=(Y_0,Y_0,-Y_0).
\]

Their special fibers agree, while their normal jets differ only through

\[
\partial_E(Y_1-Y_2)|_{E=0}=2(x-y).
\]

Hence they are naturally two deformations glued on one relative triple-divisor fiber, rather than one deformation with an inconsistent common square root.

## Site exchange

The conductor site exchange swaps \(\Delta_1\) and \(\Delta_2\), hence swaps the two oriented covers and the maps \(\Phi_1,\Phi_2\). The shared normal coordinate \(E\) and the equal-order residue are fixed.

## Consequence

The parameter-level two-copy construction is now explicit:

- each wall has its own Kummer root and relative lift;
- both lifts yield the same normal residue and index-two eigenlattice;
- they meet on the common total-energy special fiber;
- site exchange interchanges them.

This supplies the parameter maps required by the two elementary conductor factors. It does not yet prove that the selected relative cycle/form pairing pulls back to the conductor basis, because the oriented Kummer covers have not been equipped with source-derived contour cycles or integral Deligne lattices.

## Disposition

Two compatible wall-labelled parameter lifts are constructed algebraically. The first remaining geometric object is the nearby-cycle and contour realization of the selected integral pairing on each lift.

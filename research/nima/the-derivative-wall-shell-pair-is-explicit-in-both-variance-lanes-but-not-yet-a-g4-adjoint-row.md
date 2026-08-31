# The derivative–wall shell pair is explicit in both variance lanes but not yet a G4 adjoint row

## Question

Does the endpoint totalization close the regular-derivative and wall rows of the five-port locator table?

## Claim boundary

It closes their combined native shell value against the Evans state in both the Hermitian Green lane and the holomorphic analytic-transpose lane. It does not yet identify that scalar with the corresponding row of G4's arithmetic adjoint because the final centered source coefficient, transported port metric, and G4 target placement remain undeclared.

## Native combined shell value

For consecutive primes \(p<q\), put

\[
a=\log p,
\qquad
b=\log q.
\]

The closed first-order Green identity gives

\[
I_{p,q}^{(1)}(z)+I_{p,q}^{({\rm wall})}(z)
=
\Phi(b)\overline{u_z(b)}-
\Phi(a)\overline{u_z(a)}
\]

in the Hermitian lane.

The analytic-transpose lane required for multiplicity jets is

\[
I_{p,q,{\rm an}}^{({\rm end})}(z)
=
\Phi(b)u_z(b)-
\Phi(a)u_z(a).
\]

Using

\[
u_z(x)=-e^{zx}\int_x^\infty e^{-zr}\Phi(r)\,dr,
\]

the latter is an explicit holomorphic shell function. Every parameter jet is obtained by differentiating this endpoint formula.

## What is closed

The following former unknowns are resolved on the native closed graph:

1. the regular derivative and wall terms have no independent interior remainder;
2. their relative sign is fixed by the first-order Green identity;
3. the wall distribution is already included and produces no extra jet term;
4. Hermitian and analytic-transpose variance are separated explicitly;
5. the complete shell value and all analytic parameter jets are computable from endpoint tails.

They should therefore be treated as one evaluated endpoint pair in future source-level shell decompositions.

## What remains open

The five-port arithmetic residual is

\[
B_\Sigma^\dagger y
=
\sum_j B_j^\dagger y_j.
\]

A native endpoint scalar becomes its derivative–wall summand only after G4 provides:

1. the centered source coefficient multiplying both derivative and wall pieces;
2. the target metric or orientation operator in each port;
3. the comparison transporting the native closed graph into the G4 Green output;
4. confirmation that the holomorphic transpose lane, rather than the Hermitian lane, is used for Xi multiplicity jets;
5. the return placement relative to arithmetic codiagonalization.

Changing any of these data changes the adjoint row. The endpoint identity does not choose them.

## Reconciled locator status

The prior locator phrase “unevaluated against full Evans state” is superseded at the native-graph level by the endpoint formula above. Its stronger phrase “no frozen complete-shell expression against the Evans state in the final common carrier” remains correct because the final G4 metric transport is absent.

The five-port frontier is now:

- ordinary row: explicit and nonzero;
- derivative–wall native pair: explicit in both variance lanes, G4 transport open;
- reciprocal row: response intertwining open;
- linking row: polarized two-output metric identity open.

## Consequence for candidate one

The source-level residual can be reduced to

\[
\mathcal S_{p,q}(z)
=
I_{p,q}^{(0)}(z)
+I_{p,q}^{({\rm end})}(z)
+I_{p,q}^{({\rm recip})}(z)
+I_{p,q}^{({\rm link})}(z).
\]

This reduces the number of unevaluated native shell functions from four to two. It does not reduce the SCC antichain: reciprocal response and global polarized linking still feed the two declared RH-bearing frontier cells.

## Disposition

The active reconciliation succeeds partially. The derivative–wall shell pair is source-explicit and jet-ready, but promotion to a G4 adjoint row is blocked by metric and comparison data. No RH conclusion is authorized.

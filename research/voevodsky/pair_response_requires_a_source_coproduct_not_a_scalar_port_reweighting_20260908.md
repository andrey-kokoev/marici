# Pair response requires a source coproduct, not a scalar port reweighting

Date: 2026-09-08

## Type of the radial response

The radial source is an ordered-pair correlation:

\[
\rho_{f,g}(t)=\int_a^b f(u)g(u+t)\,du.
\]

It is bilinear in `(f,g)`.  The Wronskian and endpoint responses are bilinear
as well.  Therefore the function-valued response is linear only after passing
to the pair carrier

\[
\mathcal H_\theta\widehat\otimes\overline{\mathcal H_\theta}.
\]

By contrast, the existing arithmetic incidence is a linear column

\[
B_\Sigma:U_{\rm ar}\to H_G.
\]

Changing a scalar coefficient or metric on one of its five output ports cannot
supply the missing ordered-pair input.  The mismatch is categorical, not a
normalization problem.

## Required source cell

To attach the radial response to the joint-column adjoint, one needs a
source-authorized diagonal/coproduct

\[
\Delta_{\rm pair}:U_{\rm ar}
\longrightarrow
U_{\rm pair}
\]

and a pair incidence

\[
B_{\rm rad}:U_{\rm pair}\to\mathcal G_{\rm pair,rad}
\]

such that the composite adjoint produces the source-fixed combined response
`R+2E`.  The pair carrier must retain product degree, ratio displacement,
ordered orientation, prime/grade labels, and shell concatenation.

The assignment `f -> f tensor conjugate(f)` is quadratic and is not itself a
linear coproduct.  It becomes linear on a density/Fock-square source object,
but introducing that object requires an independently declared source
coalgebra or quadratic functor.  Polarizing after evaluating the desired
response does not provide one.

## Unchanged-Evans constraint

Adding a paired reservoir to the conservative column generally changes the
first-row history equation.  For the unchanged Evans state, injectivity of the
centered incidence forces the existing arithmetic coordinate to zero.  Hence a
valid pair extension must do one of the following:

1. construct a boundary-only pair channel together with the correct
   hyperbolic/Green adjoint structure;
2. construct a modified history and prove a divisor- and multiplicity-
   preserving chain comparison with the original Evans complex;
3. prove that a source-derived pair coordinate lies in an authorized forward
   null relation without destroying its lower response.

The third option is impossible in an ordinary positive Hilbert adjoint if the
forward map literally vanishes; a nontrivial realization would need a relative
or boundary pairing.

## Relation to the conditional cancellation

Radial Stokes proves exactly what the response must be once the pair source is
admitted.  It does not construct `Delta_pair`, `B_rad`, or a divisor-preserving
modified history.  Therefore the formula `R+2E` is not a permissible
reweighting of the old scalar linking port.

## Sharpened frontier

The first nonredundant construction is the pair-source incidence cell, not
another shell integral:

\[
U_{\rm ar}
\xrightarrow{\Delta_{\rm pair}}
U_{\rm pair}
\xrightarrow{B_{\rm rad}}
\mathcal G_{\rm pair,rad}.
\]

It must be compatible with the Mellin source ideal and Xi-adic filtration, or
else its modified conservative pencil need not preserve the Xi divisor.

No such coproduct/chain comparison was located in prior research.

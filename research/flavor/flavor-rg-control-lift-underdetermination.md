# RG-to-control lift underdetermination: WP999

## Question

Can the declared one-loop flavor RG operation supply the transverse drift left
open by WP998 and thereby generate the missing control direction by an ordered
bracket?

## Typed objects

The RG vector field of WP61 acts on the Yukawa-pair carrier and descends to the
faithful `physical16` quotient. The coordinates (q,k), and hence the shifted
coefficients (Q=q+u), (R=k+v), parameterize the WP978 invariant energy
functional. They are not coordinates of `physical16`.

Therefore an RG field (F_X) on the physical quotient (X) and an actuator
(X_u=\partial_Q) on the coefficient plane (C) do not yet inhabit a common
tangent object. Their bracket is undefined until a source-authorized lift

\[
\widetilde F:X\times C\longrightarrow T(X\times C)
\]

is supplied. The flow parameter used to define this derivation is not asserted
to be physical time.

## Exact nonuniqueness witness

Let the physical RG projection be any fixed (F_X). Two extensions to the
product have the same projection:

\[
\widetilde F_0=(F_X,0,0),
\qquad
\widetilde F_1=(F_X,0,Q).
\]

Both project to (F_X), so all admitted RG data on `physical16` agree. But for
the one-port coefficient actuator (X_u=\partial_Q),

\[
[\widetilde F_0,X_u]_C=0,
\qquad
[\widetilde F_1,X_u]_C=-\partial_R.
\]

The first extension retains rank one; the second generates rank two at bracket
depth two. Hence quotient RG transport alone determines neither answer.

## First missing arrow

The missing constructor is not another Lie-rank calculation. It is a
source-derived common-substrate interface specifying how the energy
coefficients transform under the RG operation. It must include normalization,
scheme and threshold domain, full weak-basis descent, and an executable
interpretation of coefficient intervention. Only then is the bracket typed.

## Classification

The declared RG operation remains invertible transport on `physical16`. It is
neither a selector nor a presentation rigidifier. It cannot presently serve as
a drift actuator on the WP978 coefficient plane. The conditional extension
(widetilde F_1) is a capacity witness only and has no source or instrument
authority.

## Smallest exact falsifier

The pair (widetilde F_0,widetilde F_1) is the smallest exact falsifier of
the inference that an admitted RG projection fixes control accessibility. They
have identical physical projection and opposite bracket-rank conclusions.

## Claim boundary

WP999 proves underdetermination from the currently admitted objects. It does
not prove that RG can never act on (q,k), nor that a UV completion cannot
derive such action. It does not identify RG scale with physical time or assign
a finite laboratory cost to RG transport.

## Disposition

Close RG-as-transverse-drift for the current packet. Reopen only when a source
action derives the common-substrate lift and its coefficient component before
the desired bracket rank is inspected.


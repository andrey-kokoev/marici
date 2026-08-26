# The primitive theta forcing norm is a canonical reservoir current

## First typed defect

After the two Clark bulks are combined, the one-chart Green identities retain
the negative primitive forcing line

\[
 -2|f(q)|^2
\]

pointwise, or `-2 integral |f|^2` after integration. This term is not part of
the Gram bulk and must not be erased by scalar simplification.

It is also distinct from the arithmetic connected `k=1` prime current. Here
“primitive” refers to the undeformed continuous source forcing in the tail
flow. The two objects may later couple, but their labels must remain distinct.

## Canonical source reservoir

Define the tail energy of the fixed forcing

\[
 J_{\rm force}(q)
 =2\int_q^\infty|f(v)|^2\,dv.
\]

This current is constructed from `f` alone, before selecting a spectral
parameter, state, or zero. Direct differentiation gives

\[
 \partial_qJ_{\rm force}(q)=-2|f(q)|^2.
\]

Therefore the entire negative forcing-norm defect is an exact source-local
boundary current.

For a decaying square-integrable forcing,

\[
 J_{\rm force}(\infty)=0,
 \qquad
 J_{\rm force}(0)=2\int_0^\infty|f(v)|^2\,dv.
\]

The norm has not disappeared: it is retained as a finite reservoir charge at
the primitive endpoint.

## Why this is not the fake-antiderivative shortcut

The forbidden construction would define a current by integrating the full
spectral residual after it is known. The forcing reservoir is different:

1. its density `|f|^2` is a fixed source observable;
2. it is independent of `z`, `G_z`, and any zero condition;
3. it is functorial under truncation of the labelled forcing;
4. it has a canonical terminal normalization `J_force(infinity)=0`;
5. its endpoint value is the already declared primitive norm line.

Thus it is a genuine boundary constructor available before the doubled Green
calculation.

## Finite-cutoff compatibility

For a labelled cutoff source `f_X`, define

\[
 J_{{\rm force},X}(q)
 =2\int_q^\infty|f_X(v)|^2\,dv.
\]

Then

\[
 \partial_qJ_{{\rm force},X}=-2|f_X|^2
\]

exactly at every cutoff. If cutoff inclusions preserve `f_X` in the chosen
source topology and `f_X` converges in `L^2`, the reservoir endpoints converge
continuously. Cross-label terms remain inside `|f_X|^2`; they are not silently
discarded as diagonal prime contributions.

## Residual ledger after this closure

The typed doubled defect now separates as

\[
 R_X^{\rm defect}
 =\partial_qJ_{{\rm force},X}
 +R_{k=1,X}^{\rm arith}
 +R_{k=2,X}^{\rm arith}
 +R_{\infty,X}
 +R_{{\rm seam},X}
 +R_{{\rm Jordan},X}.
\]

The forcing reservoir closes only its named first term. It makes no claim
about the arithmetic primitive current, prime-square current, mixed seam, or
Clark Jordan coupling.

## Falsifiers

This closure fails if the actual completed forcing is not square-integrable on
the tail chart, if the chosen labelled cutoffs do not converge in the source
topology, or if the Green defect contains a spectrally weighted forcing norm
rather than the fixed `|f|^2` density.

The smallest machine witness should identify the unmatched coefficient of
`|f_X|^2`; for the derived Clark identity that coefficient is exactly closed
by `J_force,X`.

## Present result

One universal non-bulk defect is now typed and closed:

The negative primitive forcing norm is the flux of the canonical source-energy
reservoir.

The RH-bearing audit advances to the arithmetic `k=1`, `k=2`, mixed-seam,
Jordan, and archimedean endpoint channels.

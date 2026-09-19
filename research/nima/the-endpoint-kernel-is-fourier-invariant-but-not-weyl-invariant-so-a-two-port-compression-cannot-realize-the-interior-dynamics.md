# The endpoint kernel is Fourier invariant but not Weyl invariant, so a two-port compression cannot realize the interior dynamics

## Question

Can the finite-conductor additive Tate return factor through only the endpoint
observer pair `(epsilon,mu)`?

## Exact finite hostile

Work on the additive group `A=Z/3Z` with counting normalization. Define

\[
\epsilon(f)=f(0),
\qquad
\mu(f)=\sum_{x\in A}f(x),
\]

and take

\[
f=\delta_1-\delta_2.
\]

Then

\[
\epsilon(f)=0,
\qquad
\mu(f)=0,
\]

so `f` lies in the kernel of the endpoint observation.

This kernel is invariant under the discrete Fourier transform. Indeed Fourier
exchanges evaluation at zero and total sum up to the declared normalization,
so both endpoint coordinates still vanish on `Ff`.

It is not invariant under translations. For

\[
(T_hf)(x)=f(x-h)
\]

and `h=1`,

\[
\epsilon(T_1f)=f(-1)=f(2)=-1.
\]

Thus a state invisible at the endpoint becomes endpoint-visible under the
local Weyl operation.

## Consequence

There is no autonomous two-port state realization of the full additive
Tate/Weyl dynamics whose quotient map is only `(epsilon,mu)`. Such a quotient
would require the endpoint kernel to be invariant under every interior
operation. Fourier invariance alone is insufficient.

A valid architecture has only two options:

1. retain the growing nonspherical additive state and use the two-port packet
   solely as an external observation;
2. prove that the particular interior operator used by the Green return lies
   in a smaller algebra preserving the endpoint kernel.

The second option requires a source formula for `S_Tate,p(s)`. It cannot be
inferred from the Fourier exchange square.

## Disposition

The endpoint cylinder is a valid Fourier observer quotient but not a Weyl
state quotient. The proposed fixed four-port boundary block can therefore be
an input/output transfer function only after a hidden-state realization and
an invariance or minimality theorem are supplied. The first discriminating
question is now exact: does the actual local Green interior operator include
translations or modulations that fail endpoint-kernel invariance?
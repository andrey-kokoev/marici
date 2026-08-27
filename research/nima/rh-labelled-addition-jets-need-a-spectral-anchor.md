# RH labelled-addition jets need a spectral anchor

## Result

Agreement of every labelled-addition jet does not identify the endpoint Evans section with the determinant section. It determines the comparison only up to a factor constant in the cutoff direction.

Let (t) represent a source-addition parameter and (z) the spectral coordinate. Define

\[
S(t,z)=1+tz
\]

and

\[
F(t,z)=(1-z^2)(1+tz).
\]

The division-free source-jet residual vanishes identically:

\[
(\partial_tF)S-F(\partial_tS)=0.
\]

The sections also agree at the normalized point (t=0,z=0). Nevertheless, (F) has the additional zeros (z=\pm1).

Thus source-direction naturality plus one scalar normalization does not determine the spectral divisor.

## Missing direction

The comparison problem is two-dimensional:

- arithmetic direction: changes under labelled source additions;
- spectral direction: variation over the complex parameter.

The labelled-addition jet controls only the first direction. A cutoff-independent hostile multiplier is invisible to it.

The bridge therefore needs one of two stronger anchors:

1. a source-derived comparison of the complete base sections over the spectral domain;
2. a source-derived spectral evolution equation with enough boundary data and uniqueness to determine the comparison section.

A value at one spectral point is insufficient unless the spectral evolution theorem makes it determining.

## Categorical formulation

Arithmetic naturality makes the comparison a horizontal section along the cutoff category. The remaining ambiguity is an automorphism or endomorphism pulled back from the spectral base. Horizontal transport cannot remove that vertical factor.

The desired comparison must therefore be natural over the product of the cutoff category and the spectral domain, or over a fibred category carrying both directions. Its mixed square must commute:

\[
\nabla_{\mathrm{spectral}}\nabla_{\mathrm{source}}
=
\nabla_{\mathrm{source}}\nabla_{\mathrm{spectral}}.
\]

This is not a demand for another fitted coherencer. It is a demand that both transports originate from the same source colligation.

## DPC verdict

Candidate: compare the first labelled-addition jets at every finite cutoff.

Verdict: necessary but insufficient.

Candidate: add equality at one normalized spectral point.

Verdict: still insufficient, rejected by the exact hostile.

Surviving candidate: derive a spectral transport or a full base-section comparison, then prove compatibility with labelled-addition transport and unit-preserving completion.

## Immediate finite test

At one cutoff, derive the spectral differential or difference law satisfied by both the boundary determinant section and the endpoint Evans section. Compare its coefficients and boundary data before using their scalar values. A mismatch closes the bridge; a common uniquely solvable law removes the cutoff-constant hostile factor.

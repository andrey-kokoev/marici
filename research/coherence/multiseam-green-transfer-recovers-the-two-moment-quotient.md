# Multiseam Green transfer recovers the two-moment quotient

## Global transfer

For seams \(x_i\), write \(y_i=e^{x_i}\) and let \((J_i^0,J_i^1)\) be their value/flux jumps. Linearity of the Green resolvent gives

\[
q_-=-\frac12\sum_i\frac{J_i^0+J_i^1}{y_i},
\]

\[
q_+=\frac12\sum_i y_i(J_i^0-J_i^1).
\]

Because the local two-channel transfer at any one seam is invertible, the global map

\[
\bigoplus_i
(\mathbb C_{x_i}^{\rm value}\oplus\mathbb C_{x_i}^{\rm flux})
\longrightarrow
L_-\oplus L_+
\]

is surjective for every nonempty seam set. For \(n\) seams its kernel has dimension \(2n-2\).

## Green flux sector

Green kernel packets occupy the flux-only subspace \(J_i^0=0\). Their charges reduce to

\[
q_-=-\frac12\sum_iJ_i^1/y_i,
\qquad
q_+=-\frac12\sum_iJ_i^1y_i.
\]

For distinct positions, this map has rank

\[
\min(2,n).
\]

When \(n\ge2\), its kernel is exactly

\[
\sum_iJ_i^1/y_i=0,
\qquad
\sum_iJ_i^1y_i=0.
\]

These are the same two moment conditions previously found as the kernel of the asymptotic observation on finite Green packets.

## Closed comparison loop

The constructions now agree along the complete route:

```text
finite Green packet coefficients
-> flux jumps under the massive operator
-> multiseam Green resolvent
-> incoming/outgoing asymptotic charges
```

The composite is the original two-charge quotient, including its exact kernel.

## Rank interpretation

For \(n\) Green contexts:

```text
local Green state dimension       = n
local flux-seam dimension         = n
stationary asymptotic dimension   = min(2,n)
complete labelled-context rank    = n
```

The hyperbolic rank reset occurs when local seam identities are forgotten and only the two ends of the line remain observable. Keeping independently addressable seams prevents that collapse.

This gives a concrete authorization criterion:

- endpoint-only protocols may pass to the two-charge quotient;
- seam-addressable protocols must retain the full flux family;
- complete shift contexts require its Green Gram geometry as well.

## Verification

```text
python research/coherence/check_multiseam_asymptotic_quotient.py
```

The exact-rational checker verifies the ranks and nullities for one through six distinct seams.

Artifacts:

- `check_multiseam_asymptotic_quotient.py`
- `multiseam-asymptotic-quotient.v1.json`

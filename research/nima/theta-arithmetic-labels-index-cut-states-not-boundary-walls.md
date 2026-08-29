# Arithmetic labels index exact cut states; they are not boundary walls

## Exact source identity

For a translation length $p\ge 0$, define

$$
g_p(t)=\Phi(t+p),
\qquad
h_p(t)=\mathbf 1_{0\le t\le p}\Phi(p-t).
$$

The pair $u_p=(g_p,h_p)$ is the source-derived tail-seam state associated with
the label $p$. At the internal cut,

$$
g_p(0)=h_p(0)=\Phi(p).
$$

The derivatives have opposite orientation:

$$
g_p'(0)=\Phi'(p),
\qquad
h_p'(0)=-\Phi'(p).
$$

With outward normals on the two pieces, the fluxes sum to zero. Thus value
continuity and Kirchhoff flux cancellation are exact for every $p$, including
$p=\log 2$.

The other seam endpoint satisfies $h_p(p)=\Phi(0)$. It returns to the physical
source endpoint; it is not a prime-local boundary value.

## Typing correction

The arithmetic atom at $p=\log n$ does not attach to a newly created wall at
that coordinate. It selects the entire cut state $u_{\log n}$. Prime,
prime-square, and connected typing belongs to the coefficient and constructor
module that selects and combines these states.

Consequently, the correct source map is a synthesis map

$$
U:c\longmapsto\sum_n c_n u_{\log n},
$$

or its continuous packet analogue. Arithmetic reciprocal transport acts on
the labelled coefficient module. Seam reflection acts on the synthesized
carrier. The required action square is naturality of synthesis:

$$
J\,U_+=U_-\,R.
$$

This replaces the false seam-to-prime endpoint attachment.

## What is already exact

At each label:

- tail and seam values agree at the cut;
- outward flux cancels;
- the full tail-seam norm retains translated source norm;
- reciprocal reflection preserves the carrier graph structure.

No additional local coherencer is needed for these identities.

## What remains

The global square still requires a frozen coefficient topology and exact
definitions of $R$, $U_+$, and $U_-$. Existing results show why this is not
automatic:

- a pure analytic Gram quotient erases divisibility and prime-power type;
- unrestricted coefficient packets destroy closed range;
- arithmetic constructors require a pro-Gram or valuation/Fock topology;
- scalar Tate completion does not reconstruct the operator-valued synthesis.

The next finite test is therefore labelwise naturality on the primitive and
square states for prime two, followed by the two-step comparison at
$0,\log 2,2\log 2$. The prime-four state must retain its prime-power type
instead of being treated as an independent primitive.

## Falsifier

For each admitted label, compute

$$
\Delta_n=J u_{\log n}^{+}-u_{\log n}^{-}R.
$$

Any nonzero typed component of $\Delta_n$ rejects the proposed action. If all
finite residuals vanish, completion still requires a uniform synthesis margin
for the constructor-indexed operational quotient.

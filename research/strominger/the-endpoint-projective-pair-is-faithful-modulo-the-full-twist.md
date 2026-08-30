# The Endpoint-Projective Pair Is Faithful Modulo the Full Twist

## Question

Does the binary central lift terminate the four-zero braid-coherence tower?

## Two exact sequences

The spherical braid group maps onto the four-punctured-sphere mapping class
group with central kernel:

\[
1\longrightarrow\langle\Omega\rangle
\longrightarrow B_4(S^2)
\longrightarrow M(0,4)
\longrightarrow1,
\qquad
\Omega=(\sigma_1\sigma_2\sigma_3)^4.
\]

The hyperelliptic projective map

\[
\rho:M(0,4)\longrightarrow PSL_2(\mathbb Z)
\]

has Klein-four kernel \(N\). In the chosen half-twist coordinates, one
nontrivial kernel element is

\[
a=\sigma_1\sigma_3^{-1},
\]

and a second is its \(\sigma_2\)-conjugate. Their endpoint permutations,
together with their product, are the three double transpositions

\[
(12)(34),\qquad(13)(24),\qquad(14)(23).
\]

Therefore endpoint permutation is injective on \(N\).

## Joint faithfulness

Let \(p:M(0,4)\to S_4\) be the puncture-permutation map. If

\[
p(x)=1,
\qquad
\rho(x)=1,
\]

then \(x\in N\), while injectivity of \(p|_N\) forces \(x=1\). Hence

\[
\ker(p,\rho)=1.
\]

Pulling the pair back along \(B_4(S^2)\to M(0,4)\) gives

\[
\ker(\text{endpoint},\rho)=\langle\Omega\rangle\cong\mathbb Z/2.
\]

Thus one binary central lift is both necessary and sufficient for
faithfulness in this four-zero spherical-braid model.

## Interpretation

The coherence tower terminates at three complementary pieces:

```text
endpoint permutation        sees the Klein-four projective kernel
projective PSL2 monodromy    sees the infinite nonabelian quotient
central binary lift         sees the full twist
```

No one piece is faithful. Their joint packet is faithful.

This is a theorem for the four-zero spherical-braid model. It does not assert
the same three-port termination for higher numbers of zeros.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/joint_endpoint_projective_faithfulness_checks.py
```

## Source

Jules Martel, *The non semi-simple TQFT of the sphere with four punctures*,
Section 2, gives the hyperelliptic projective description of \(M(0,4)\) and
identifies its Klein-four kernel.

# Distinct seam walls make the centered incidence injective and exclude an exact theta lift

## Centered primitive columns

On the positive folded chart,

\[
b_p(u)
=
p^{-1/2}\Phi(u)\mathbf1_{[0,\log p]}(u),
\]

with the jump at \(u=\log p\) retained in its own seam wall port.

For a source packet \(x\), the interior synthesis has the form

\[
(B_\Sigma x)(u)
=
\Phi(u)
\sum_{p\ge e^u}p^{-1/2}x_p.
\]

The wall coordinate at \(\log p\) is proportional to
\(p^{-1/2}x_p\Phi(\log p)\).

## Injectivity

If

\[
B_\Sigma x=0
\]

in the wall-extended carrier, every distinct wall coordinate vanishes. Since
the theta profile is nonzero at the prime seams,

\[
p^{-1/2}x_p\Phi(\log p)=0
\]

for every prime, hence

\[
x_p=0.
\]

Therefore

\[
\ker B_\Sigma=0.
\]

The same conclusion follows from the jumps of the interior tail-sum function,
but the wall-port proof preserves the declared source typing.

## No exact theta lift

Suppose

\[
B_\Sigma x=\Phi.
\]

The target \(\Phi\) has no prime-seam wall jumps. Equality in the wall-extended
carrier again forces \(x_p=0\) for every prime. Then \(B_\Sigma x=0\), a
contradiction.

Thus

\[
\Phi\notin\operatorname{ran}B_\Sigma.
\]

Combined with the one-prime approximants,

\[
B_\Sigma(p^{1/2}e_p)
=
\Phi\mathbf1_{[0,\log p]}
\longrightarrow\Phi,
\]

this gives the strict range classification

\[
\Phi
\in
\overline{\operatorname{ran}B_\Sigma}
\setminus
\operatorname{ran}B_\Sigma.
\]

## Three-port consequence

The theta forcing must enter through its own port

\[
V:
\mathbb C_\theta\to H,
\qquad
V1=\Phi.
\]

For the unchanged Evans history \(u_z\), the first row of the three-port pencil
is

\[
(A-z)u_z=V1+B_\Sigma x.
\]

Since the Evans history already satisfies \((A-z)u_z=V1\), injectivity forces

\[
x=0.
\]

Its conservative promotion initially presents the lower residuals

\[
V^\dagger u_z=0,
\qquad
B_\Sigma^\dagger u_z=0.
\]

Because \(\Phi\in\overline{\operatorname{ran}B_\Sigma}\), the second implies
the first. Promotion therefore reduces to the single vector condition

\[
B_\Sigma^\dagger u_z=0.
\]

The arithmetic law \(D_U\) does not enter because its source coordinate is
zero.

## Modified histories

A nonzero arithmetic coordinate is possible only if the history itself is
changed to solve

\[
(A-z)u_{z,x}=V1+B_\Sigma x.
\]

Its seam mismatch is then not the original Evans section \(\tau\). Preserving
the Xi divisor requires a separate chain comparison between the modified and
original matching complexes.

## Disposition

The centered seam incidence is injective, while the theta forcing belongs to
its closure but not its exact range. The unchanged Evans lift cannot acquire a
nonzero arithmetic source state. Its Green promotion is exactly the pair of
theta and arithmetic adjoint residuals above, an RH-bearing condition. No RH
conclusion is authorized.

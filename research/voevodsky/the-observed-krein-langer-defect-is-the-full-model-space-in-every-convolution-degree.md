# The observed Krein--Langer defect is the full model space in every convolution degree

## Objective

Compute the defect space observed by the completed generic degree-\(r\) boundary map

\[
\mathcal O_r:
\mathscr G_r
\to
\operatorname{Hol}(\mathfrak S)
\oplus
\mathscr H_{end}.
\]

Let \(B\) be the inner denominator in the Krein--Langer factorization of the reflected boundary multiplier. Let

\[
K_B=H^2\ominus BH^2
\]

be its model space after conformally identifying the strip with a standard Hardy domain.

The observed interior defect is

\[
\mathcal D_{r}^{KL}
=
\overline{
P_{K_B}
\mathcal O_r^{hol}(
\mathscr G_r)
}^{K_B}.
\]

## Gaussian convolution family

Fix a Gaussian scale \(\tau>0\). Degree-one translated Gaussian observers have boundary amplitudes

\[
m_{a,1}(t)
=c_1e^{-\tau t^2}e^{iat},
\qquad a\in\mathbb R.
\]

Convolving \(r\) such observers gives degree-\(r\) amplitudes

\[
m_{a,r}(t)
=c_re^{-r\tau t^2}e^{iat},
\qquad a\in\mathbb R,
\]

because the individual translations may be chosen with arbitrary total translation \(a\).

These amplitudes extend holomorphically to the critical strip and belong to every inner-strip Hardy graph.

## Density theorem

For every \(r\ge1\),

\[
\overline{
P_{K_B}
\operatorname{span}
\{m_{a,r}:a\in\mathbb R\}
}^{K_B}
=
K_B.
\]

Therefore

\[
\mathcal D_r^{KL}=K_B.
\]

## Proof

Let \(f\in K_B\) be orthogonal to every projected degree-\(r\) Gaussian amplitude. Since \(P_{K_B}\) is the orthogonal projection onto \(K_B\),

\[
0
=
\langle f,
P_{K_B}m_{a,r}
\rangle
=
\langle f,m_{a,r}\rangle
\]

for every \(a\in\mathbb R\).

On the real boundary this becomes

\[
0
=
c_r
\int_{\mathbb R}
\overline{f(t)}
e^{-r\tau t^2}
e^{iat}
\frac{dt}{2\pi}.
\]

The function

\[
\overline{f(t)}e^{-r\tau t^2}
\]

belongs to \(L^1(\mathbb R)\). This follows from Cauchy--Schwarz because \(f\in L^2\) and the Gaussian belongs to \(L^2\).

Its Fourier transform vanishes for every real frequency \(a\). Fourier uniqueness gives

\[
\overline{f(t)}e^{-r\tau t^2}=0
\]

almost everywhere. The Gaussian never vanishes, so

\[
f=0.
\]

Thus the orthogonal complement of the projected Gaussian span in \(K_B\) is zero. The projected span is dense.

## Finite and infinite divisors

The proof does not require \(B\) to be a finite Blaschke product. It uses only that \(K_B\) is a closed Hardy model space with its boundary \(L^2\) realization.

Consequently the result applies to:

1. finite Blaschke products;
2. infinite Blaschke products satisfying the Hardy bounded-type assumptions;
3. model spaces with zero accumulation only at the boundary;
4. multiplicities, without a separate jet argument.

The earlier finite evaluation theorem is recovered as a finite-dimensional corollary.

## Projective graph compatibility

Every translated Gaussian lies in the analytic core of every inner-strip aperture. Hence its image defines a compatible element of the projective graph \(\mathscr G_r\).

The density proof takes place in the target model-space norm. It is therefore unaffected by strengthening the source topology from one aperture to the full projective graph.

No assertion is made that the Gaussian span is dense in the source projective topology. Only target defect detection is required here.

## Endpoint sector

The Krein--Langer model space records interior meromorphic defect directions. The completed endpoint swap block contributes an independent negative odd line

\[
\mathscr H_{end}^{odd}.
\]

Therefore the total observed negative carrier of the endpoint-augmented boundary system is

\[
\mathcal D_r^{obs}
=
K_B
\oplus
\mathscr H_{end}^{odd},
\]

when the endpoint line is not already included as a boundary singular factor in the chosen generalized model-space convention.

If the endpoint is incorporated into the generalized inner denominator, the same statement is read as the corresponding direct decomposition of the generalized model space into interior and boundary-index parts.

## Degree naturality

Convolution by an admitted multiplier acts on the Hardy boundary by multiplication. Since the observation in every degree is dense in \(K_B\), degree successors do not shrink the observed defect carrier.

Thus

\[
\mathcal D_r^{KL}=K_B
\]

for every \(r\ge1\).

The convolution degree changes the source ancestry and multiplier action, but not the closed defect space detected by the source.

## Consequence for odd-parity absorption

The odd endpoint projection can absorb the full observed negative carrier only when

\[
K_B=\{0\}
\]

in the separate-endpoint convention.

More generally, if one endpoint direction is included in \(K_B\), odd parity is complete only when the generalized model space has negative dimension one and is exactly that endpoint direction.

If \(K_B\) contains any additional direction, the translated Gaussian source detects it in every convolution degree.

## Hostile audit

For a hostile fixture with a prescribed nontrivial Blaschke factor, the completed source observation must report the full model-space defect. A construction reporting only endpoint odd parity fails target faithfulness.

This audit does not make absence of the defect an objective. It verifies that the completed observation does not erase it.

## Step-2 result

The observed Krein--Langer defect space is computed:

\[
\mathcal D_r^{KL}=K_B
\]

for every positive convolution degree \(r\).

On the endpoint-augmented carrier, the total negative observation is the full model-space defect together with the odd endpoint line according to the selected endpoint convention.

## Disposition

Step 2 of the completion programme is closed. The generic convolution-degree source is target-faithful for the entire Krein--Langer defect carrier.

The next step cannot use odd parity alone except in the index-one endpoint-only case. It must construct an independently contractive operation capable of absorbing the full observed model space \(K_B\), or retain that model space explicitly as an unresolved negative feature.

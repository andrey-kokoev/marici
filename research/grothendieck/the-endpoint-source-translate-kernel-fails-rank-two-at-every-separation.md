# The endpoint source-translate kernel fails rank two at every separation

## Exact endpoint kernel

After the verified imaginary-character crossing, the endpoint contribution to the fixed-width source difference kernel is, up to a positive width-dependent constant,

\[
K_{\rm end}(d)=e^{\sigma/2}\cosh(d/2).
\]

For two translates at separation `d`, its Toeplitz Gram matrix is

\[
\begin{pmatrix}
K_{\rm end}(0)&K_{\rm end}(d)\\
K_{\rm end}(d)&K_{\rm end}(0)
\end{pmatrix}.
\]

Its determinant is

\[
e^\sigma\left(1-\cosh^2(d/2)\right)
=-e^\sigma\sinh^2(d/2)<0
\]

for every nonzero `d`.

## Consequence

The completed endpoint channel is not a positive-definite anchor perturbed by gamma and prime corrections. It fails at the smallest coupled rank for every separation. The failure is not small when translates separate, since the hyperbolic cosine grows.

Therefore none of the following proof patterns is admissible:

1. prove endpoint PSD and dominate the other sectors;
2. treat endpoint, gamma, and prime terms as orthogonal positive measures;
3. use absolute smallness of the prime term against the endpoint diagonal.

At minimum, endpoint and gamma contributions must be combined before any positive-definite baseline can be sought. The prime sector must then be controlled relative to that completed coupled form, with confluent null directions retained.

## Relation to scalar heat

At zero separation the endpoint diagonal is positive, which is why scalar order-zero heat positivity does not expose this obstruction. Translation characters reveal the forbidden hyperbolic growth immediately. This is another exact distinction between diagonal heat values and nonlocal Gram positivity.

## Disposition

Reject endpoint-dominance and sectorwise Gram factorizations. Any source proof must exhibit cancellation of the endpoint's negative two-translate direction inside the complete endpoint--gamma--prime kernel before asserting positivity.

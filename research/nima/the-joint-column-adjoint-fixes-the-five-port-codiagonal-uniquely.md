# The joint-column adjoint fixes the five-port codiagonal uniquely

## Question

After separating the five residual ports, is their arithmetic codiagonal an
additional free constructor?

## Claim boundary

No. Once the source joint incidence, port metrics, and reciprocal signs are
fixed, its adjoint uniquely determines the codiagonal. The remaining theorem is
that this fixed sum is divisible by the Xi section. This does not establish
that the currently proposed port normalizations have all been source-identified.

## Joint incidence

Let

\[
 H_G=H^{(0)}\oplus H^{(1)}\oplus H^{({\rm wall})}
 \oplus H^{({\rm recip})}\oplus H^{({\rm link})}
\]

be the typed Green output, with its frozen direct-sum metric. Write the joint
arithmetic incidence as

\[
 B_\Sigma x
 =\bigl(B_0x,B_1x,B_{\rm wall}x,
 B_{\rm recip}x,B_{\rm link}x\bigr).
\]

The reciprocal and ordered signs belong inside the component maps or the
metric. They are not inserted after taking the adjoint.

For \(y=(y_0,y_1,y_{\rm wall},y_{\rm recip},y_{\rm link})\), the defining
adjoint identity gives

\[
 \langle B_\Sigma x,y\rangle_{H_G}
 =\left\langle x,
 B_0^\dagger y_0+B_1^\dagger y_1
 +B_{\rm wall}^\dagger y_{\rm wall}
 +B_{\rm recip}^\dagger y_{\rm recip}
 +B_{\rm link}^\dagger y_{\rm link}
 \right\rangle_U.
\]

Therefore

\[
 B_\Sigma^\dagger y
 =B_0^\dagger y_0+B_1^\dagger y_1
 +B_{\rm wall}^\dagger y_{\rm wall}
 +B_{\rm recip}^\dagger y_{\rm recip}
 +B_{\rm link}^\dagger y_{\rm link}.
\]

There is no adjustable coefficient once the five component maps and metrics
are fixed.

## Saturated observer versus arithmetic equation

The saturated observer is

\[
 \widetilde B^\dagger y
 =\bigl(B_0^\dagger y_0,B_1^\dagger y_1,
 B_{\rm wall}^\dagger y_{\rm wall},
 B_{\rm recip}^\dagger y_{\rm recip},
 B_{\rm link}^\dagger y_{\rm link}\bigr)
 \in U^5.
\]

The arithmetic equation is obtained by the source sum

\[
 \Sigma_U:U^5\to U,
 \qquad
 \Sigma_U(x_0,\ldots,x_4)=x_0+\cdots+x_4,
\]

so that

\[
 B_\Sigma^\dagger=\Sigma_U\widetilde B^\dagger.
\]

The map \(\Sigma_U\) has a large kernel. Thus cancellation in the arithmetic
equation is compatible with a nonzero saturated observer. It is not compatible
with calling the five-port observer itself zero.

## Metric dependence

If a port metric contains a source weight or orientation operator \(G_j\), the
corresponding term is

\[
 B_j^*G_jy_j.
\]

Changing \(G_j\) changes the adjoint codiagonal. Therefore each proposed
normalization must be derived before the residual identity is tested. Positivity
or determinant agreement does not choose \(G_j\).

In particular, a coefficient imported from the first-Adams block into G4 is
valid only after the declared comparison transports both the port and its
metric.

## Evans residual

For the split Evans section \(\widehat u(z)\), let \(y(z)\) denote its complete
five-port Green image. The fixed arithmetic residual is

\[
 r_U(z)=B_\Sigma^\dagger y(z)
 =\sum_j B_j^\dagger y_j(z).
\]

The ordinary summand is nonzero at every parameter. Promotion therefore
requires a genuine cancellation among the fixed remaining terms:

\[
 r_U(z)=\tau(z)h_U(z).
\]

No alternate codiagonal may be selected after evaluating \(r_U\) on the Xi
divisor.

## Cutoff naturality

At a finite prime cutoff \(X\), the same identity holds with source projection
\(P_X\):

\[
 (B_\Sigma P_X)^\dagger
 =P_XB_\Sigma^\dagger.
\]

Hence the consecutive-prime shell residuals test the fixed source adjoint at
every cutoff. A failed shell cannot be hidden by redefining the completion map.

## Disposition

The five-port codiagonal is not an additional degree of freedom: it is the
adjoint of the frozen joint column. The current open constructor is exact Xi
divisibility of that fixed adjoint residual, with all port normalizations first
source-identified. No RH conclusion is authorized.

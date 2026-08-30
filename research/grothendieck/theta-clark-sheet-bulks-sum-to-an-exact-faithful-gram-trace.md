# Clark-sheet bulks sum to an exact faithful Gram trace

## Bounded finite audit

Packet 151 proves that Clark-sheet exchange reverses the oriented Wronskian.
Nima isolated three remaining finite gates: equal coefficients, absence of a
third quadratic component, and faithfulness of the symmetric trace. For the
positive Clark bulk, all three follow from one parallelogram identity.

## Native Clark shear

Let the differentiated source-tail feature be

\[
 H_a=G+ia\,\partial_zG,
 \qquad
 H_{-a}=G-ia\,\partial_zG.
\]

The source Green identity uses the forced features `H_a+f` and `H_-a+f`.
Put

\[
 X=G+f,
 \qquad
 Y=a\,\partial_zG.
\]

Then

\[
 H_a+f=X+iY,
 \qquad
 H_{-a}+f=X-iY.
\]

The Hilbert parallelogram law gives pointwise

\[
 \boxed{
 |H_a+f|^2+|H_{-a}+f|^2
 =2|G+f|^2+2a^2|\partial_zG|^2.}
\]

No spectral zero, determinant phase, or inequality is used.

## Resolution of the finite bulk gates

Expanding either sheet separately produces an even trace and an odd cross
term:

\[
 |X\pm iY|^2
 =|X|^2+|Y|^2
 \pm2\operatorname{Im}(X\overline Y).
\]

Therefore:

1. the two sheets have exactly equal trace coefficients;
2. the spin-two/cross component reverses exactly;
3. their sum contains no third quadratic representation;
4. the summed bulk is the Gram trace of the labelled pair `(X,Y)`.

In its real four-coordinate representation, the matrix is twice the identity
on the `X` coordinates and twice the identity on the `Y` coordinates, with
the source scale `a^2` already included in `Y`.

## Faithfulness

For real nonzero `a`, the summed pointwise bulk vanishes exactly when

\[
 G+f=0,
 \qquad
 \partial_zG=0.
\]

Thus it is faithful on the two-feature amplitude packet

\[
 (G+f,a\partial_zG).
\]

For an admissible two-endpoint zero-state, proving strict integrated
positivity reduces to excluding simultaneous vanishing of these two source
features almost everywhere. Since `G` obeys its forced first-order flow, such
simultaneous vanishing would impose an additional differential identity on
`f`; it is not a generic null quadrature.

The case `a=0` is a separate degeneration: the Clark shear disappears and
the second feature is intentionally lost. Any theorem using this packet must
state whether `a` is fixed nonzero or how the unsheared sector is handled.

## Cutoff exactness

The identity is labelwise and pointwise. Hence at every finite Euler cutoff
`X`, summing the retained labels gives

\[
 \boxed{
 E_{+,X}^{\rm bulk}+E_{-,X}^{\rm bulk}
 =2T_X^{\rm Gram}.}
\]

No equality appears only after sheet transport or scalar aggregation: both
features are written in the common labelled `(G,f,partial_z G)` module before
the two forms are added.

## What remains outside the theorem

The full Green identity also contains:

- primitive norm/seam lines;
- the `k=1` distributional current;
- the `k=2` Hilbert non-trace-class current;
- archimedean endpoint terms;
- right--left mixed reflection-coboundary terms.

The parallelogram theorem proves native strictness of the **positive Clark
bulk**. It does not prove that every defect channel cancels, becomes boundary
flux, or is dominated after restricted-product completion.

Prime two is retained inside the labelled source features; no claim of
primewise scalar positivity is made.

## Revised residual

The finite hostile residual no longer needs to audit bulk coefficient
equality. It is entirely the non-bulk packet

\[
 R_X^{\rm defect}
 =\text{full doubled Green form}-2T_X^{\rm Gram}
 -\text{declared completed boundary current}.
\]

The route survives only if this residual vanishes as a typed distribution or
is itself an independently positive source form. Any new indefinite bulk
component falsifies representation completeness.

## Present result

For the native Clark-differentiated bulk, equal coefficients,
spin-two cancellation, representation completeness, and Gram faithfulness on
the two-feature packet are exact finite theorems. The RH-bearing frontier has
moved entirely to the declared defect and completion channels.


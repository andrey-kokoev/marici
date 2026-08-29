# The completion differential annihilates the wall, so the common carrier must be relative

## Exact source identity

The theta precursor is

\[
h(u)
=
e^{u/2}
\left(
\frac12+
\sum_{n\ge1}e^{-\pi n^2e^{2u}}
\right),
\]

and the completed positive source is

\[
\Phi(u)
=
\left(
\partial_u^2-\frac14
\right)h(u).
\]

The zero-mode wall is

\[
h_0(u)=\frac12e^{u/2}.
\]

It satisfies

\[
\left(
\partial_u^2-\frac14
\right)h_0=0.
\]

Therefore the completion differential annihilates the universal wall carrier exactly.

## Dilation-coordinate calculation

Set

\[
y=e^{2u}-1
\]

and write

\[
h(u)=e^{u/2}f(y).
\]

Conjugating the completion differential by the quarter-density gives

\[
e^{-u/2}
\left(
\partial_u^2-\frac14
\right)
e^{u/2}
=
4(1+y)^2\partial_y^2
+
6(1+y)\partial_y.
\]

Call this operator \(\mathcal C_y\). Then

\[
\mathcal C_y(1)=0.
\]

So in the length-three Jordan presentation, the constant grade is not mapped to a scaled seam wall or to a higher-grade mixture. It lies in the kernel of completion.

## Consequence for the history comparison

The window-history constant overlap cannot be transported through completion into the \(\Phi\)-causal history as an identity term. The candidate diagram

\[
e_{\mathrm{wall}}
\longmapsto
\lambda I_{\mathrm{seam}}
\]

has

\[
\lambda=0
\]

if the arrow is literally the completion differential.

Thus the scalar shifted-history square

\[
\frac12(I+H_\Phi^{*}H_\Phi)
\pm
\frac{i}{2}(H_\Phi-H_\Phi^{*})
\]

does not arise by applying completion to one precursor Gram. Its identity term must be retained as relative kernel data rather than as an image component.

## Correct categorical carrier

The common object should be the relative or mapping-cone system

\[
\ker\mathcal C
\longrightarrow
\mathcal H_{\mathrm{precursor}}
\xrightarrow{\mathcal C}
\mathcal H_{\mathrm{completed}}.
\]

The wall belongs to \(\ker\mathcal C\); the causal seam history belongs to the completed image. They can coexist in a relative Green complex, but not as two coordinates in the completed image alone.

A minimal block therefore has at least three typed sectors:

\[
\text{wall kernel}
\oplus
\text{precursor history}
\oplus
\text{completed seam history}.
\]

Schur elimination may later create an effective identity contribution, but it must pass through the relative connecting map.

## Jordan-grade meaning

For each nonzero label, the completion differential maps the exponential precursor into the positive length-three packet

\[
e^{-\lambda_n}
\left(
A_{0,n}+A_{1,n}y+A_{2,n}y^2
\right)e^{-\lambda_n y}.
\]

The zero label is exceptional: it is killed rather than becoming another positive Jordan packet. Hence the wall and nonzero theta labels have categorically different completion behavior.

This is exactly why a scalar normalization triple could not yet be extracted.

## Hostiles resolved

1. **Pure-wall transport hostile:** completion sends the wall to zero, disproving any direct unit-wall comparison.
2. **Scalar square hostile:** adjoining \(I\) after completion creates a split extension not supplied by the differential.
3. **Label-smearing hostile:** treating the zero mode as the \(n=0\) member of the positive length-three family ignores its annihilation.
4. **Post-hoc graph norm:** graph energy is analytically canonical but source-authorized only after constructing the relative extension that retains the kernel wall.

## Revised earliest theorem

Construct the relative Green identity for the completion complex

\[
\ker\mathcal C
\to
\operatorname{Dom}\mathcal C
\to
\operatorname{Ran}\mathcal C.
\]

The required result must show how the wall kernel couples to causal/anti-causal completed histories through a boundary or connecting morphism. Only the Schur return of this relative block may be compared with the shifted-history Gram.

The normalization problem has therefore become an extension problem: the wall is not a missing scale in the completed carrier; it is a killed precursor class that completion must retain relatively.

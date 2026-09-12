# Log-prime shifts select a varying broken-graph bundle

## Fixed-domain obstruction

A fixed broken Sobolev line is not the correct completion. Closure under both forward and backward shifts by \(\log2\) and \(\log3\) would require breakpoints in

\[
\Gamma=\{m\log2+n\log3:m,n\in\mathbb Z\}\cap\mathbb R_+.
\]

The ratio \(\log2/\log3\) is irrational, since a rational ratio would imply \(2^a=3^b\) for nonzero integers. Hence \(\Gamma\) is dense. There is no locally finite interval decomposition with all these breakpoints.

Thus the requested object cannot be one invariant scalar broken-Sobolev domain.

## Varying fibers

For a finite breakpoint set \(B\subset\mathbb R_+\), define

\[
\mathcal D_B
=
\bigoplus_{I\in\pi_0(\mathbb R_+\setminus B)}H^1(I),
\]

with the sum of interval \(H^1\) norms and retained left/right traces at every \(b\in B\).

A left shift by \(a\) maps between fibers according to

\[
R_a:\mathcal D_B\longrightarrow\mathcal D_{R_aB},
\qquad
R_aB=\{b-a:b\in B,\ b>a\}.
\]

A right zero-extension maps according to

\[
S_a:\mathcal D_B\longrightarrow\mathcal D_{S_aB},
\qquad
S_aB=\{a\}\cup\{a+b:b\in B\}.
\]

The new breakpoint at \(a\) is exactly the half-line window boundary. The shifts are therefore well typed as arrows between graph fibers, even though they are not endomorphisms of one graph domain.

## Dual-valued derivative and Green form

For \(f\in\mathcal D_B\), its distributional derivative is

\[
\partial f
=
\partial_{\rm pw}f
+
\sum_{b\in B}[f]_b\,\delta_b,
\qquad
[f]_b=f(b+)-f(b-).
\]

Integration by parts on every component gives the boundary form

\[
\mathfrak b_B(f,g)
=
-f(0+)\overline{g(0+)}
+
\sum_{b\in B}
\left(
 f(b-)\overline{g(b-)}
-f(b+)\overline{g(b+)}
\right),
\]

assuming the terminal contribution at infinity vanishes. This retains rather than suppresses every seam jump created by \(S_a\).

Hence

\[
\partial_B:\mathcal D_B\to\mathcal D_B'
\]

and the Green identity are defined fiberwise. Transport naturality is a square between different \(B\)'s.

## Four-prime cube

For one traversal of the four-prime cube, take the finite set of positive subset sums

\[
B_4=
\left\{
\sum_{i\in U}\log p_i:
\varnothing\ne U\subseteq\{0,1,2,3\}
\right\}.
\]

It has fifteen breakpoints. Every face path lands in a finite graph fiber obtained by the displayed \(R\)- and \(S\)-rules. The accompanying checker verifies all target breakpoint sets remain finite.

The right categorical object is therefore

\[
B\longmapsto\mathcal D_B,
\]

not a single \(D\). The four-cup acts on the corresponding cubical diagram and its readout lands in the direct sum of the face trace spaces.

## Consequence

The analytic completion now has a precise form:

\[
\boxed{
\text{log-prime valuation cube}
\longmapsto
\text{varying broken-graph bundle}
\longmapsto
\text{dual-valued Green boundary system}.
}
\]

For arbitrary iteration the breakpoint set becomes dense, but this does not invalidate finite cells: it says the infinite object must be a projective/inductive diagram of finite graph fibers rather than a locally finite partition of one scalar line.

## Verification

Run:

```text
python research/coherence/check_four_prime_varying_graph.py
```

Artifacts:

- `check_four_prime_varying_graph.py`
- `four-prime-varying-graph.v1.json`

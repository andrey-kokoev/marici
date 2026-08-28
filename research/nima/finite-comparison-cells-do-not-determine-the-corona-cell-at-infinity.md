# Finite comparison cells do not determine the corona cell at infinity

## Question

Can the missing comparison 2-cell between Mertens renormalization and
theta--Tate completion be assembled solely from compatible finite-cutoff
comparison cells?

## Corona model

Let \(c_0\) be the sequences converging to zero and consider the corona

\[
\ell^\infty/c_0.
\]

For each cutoff \(N\), define the finite prefix sequence

\[
u^{(N)}=(\underbrace{1,\ldots,1}_{N},0,0,\ldots).
\]

Every \(u^{(N)}\) lies in \(c_0\), so its corona class is zero. For each fixed
coordinate, however, \(u^{(N)}\) eventually equals the constant sequence

\[
u=(1,1,1,\ldots).
\]

The limit sequence has nonzero corona class and

\[
\|[u]\|_{\ell^\infty/c_0}=1.
\]

The convergence is coordinatewise and on every fixed finite window, but not
uniform:

\[
\|u-u^{(N)}\|_\infty=1
\]

for all \(N\).

## Categorical meaning

Finite stages form a pro-diagram. A compatible family of finite comparison
cells controls every bounded coordinate restriction. It does not automatically
define a comparison cell after a completion functor that detects the corona.

The missing datum is a continuity or descent theorem saying that the
comparison transformation commutes with the chosen completion. Without it, a
phantom 2-cell may vanish at every finite stage and survive only at infinity.

In the RH lane:

- finite Euler/Mertens cells see the prefix data;
- theta--Tate completion sees the boundary corona;
- the BSY discrepancy is a candidate corona class;
- RH is the assertion that the distinguished completed class vanishes.

This formulation does not prove RH. It locates why finite naturality alone
cannot prove it.

## Exact gate

Let \(\eta_N\) be the finite comparison cells and \(C\) the boundary
completion functor. A valid global comparison cell requires more than
compatibility under restriction. It requires a uniform descent statement such
as

\[
\|C(eta)-C(eta_N)\|\longrightarrow0
\]

in a topology that detects the boundary anomaly.

Equivalently, the induced corona class of the residual family must vanish.
This is a Beck--Chevalley-at-completion condition: base change and boundary
completion must commute not just on finite objects but on their completed
pro-limit.

## Hostile

The prefix family \(u^{(N)}\) passes:

- exact finite support;
- compatibility on every previously exposed coordinate;
- pointwise convergence;
- convergence on every fixed finite window;
- zero corona class at each individual finite stage.

It fails uniform convergence, and its completed limit has corona norm one.
Any proposed local-to-global comparison theorem admitting this family is
false.

## Verdict

The Mertens--completion 2-cell cannot be manufactured by merely composing
finite prime-addition cells. The programme needs a source-derived uniform
Beck--Chevalley theorem, or an equivalent tightness estimate, proving that the
residual corona class vanishes. The completed anomaly lives exactly where
finite local coherence stops seeing.


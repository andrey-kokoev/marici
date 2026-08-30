# 2862 — The Soft Logarithmic Primitive Is an Affine Residue Torsor

> **Scope refinement.** This entry classifies the local germ. The complete
> oriented chain has a second endpoint at the source-normalized coordinate
> \(t=2\), which may point the torsor by imposing \(F(2)=0\). The subsequent
> entry constructs that candidate pointing and leaves chart naturality as its
> acceptance gate.

## Surviving loophole from Entry 2860

Entry 2860 excluded a rational primitive for the \(\xi\)-density. A logarithmic primitive remains locally possible.

Set

\[
t=\xi+1.
\]

At a generic bulk value of \(a\), the Cayley–Menger kernel is a unit at \(t=0\). The source density therefore has local form

\[
\left(
\frac{R}{t}
+\text{regular}
\right)dt,
\]

where

\[
R=
\frac{a+p}
{2p(a-p)^2(a+3p)
\sqrt{K_{\rm exc}(a,\kappa,-1)}}.
\]

The local primitive is

\[
F=R\log t+\text{holomorphic}.
\]

## Monodromy

Continuation once around the marked endpoint sends

\[
\log t\longmapsto\log t+2\pi i,
\]

and hence

\[
F\longmapsto F+2\pi iR.
\]

The residue \(R\) and the translation law are canonical. The value of \(F\) is not.

## Subtraction-scale dependence

Writing the primitive as

\[
R\log(t/\mu)+\text{regular}
\]

requires a dimensionless subtraction scale \(\mu\). Changing \(\mu\) shifts the finite part by a multiple of \(R\).

The source \(i\epsilon\) orientation can choose a side of the logarithmic cut. It does not, by itself, select an affine origin or finite subtraction scale.

## Classification

The logarithmic primitive is not a scalar coefficient line. Its values form an affine torsor under the residue line:

\[
\mathcal P_{\log}
\text{ is a torsor for }
\mathbb C R.
\]

This is the correct surviving endpoint object:

- canonical residue;
- canonical additive monodromy;
- no canonical primitive value;
- no source-authorized scalar endpoint sum.

Therefore the scalar-combination route remains closed under the frozen source. Reopening requires a declared renormalization or physical relative-cycle prescription that fixes the affine origin and is invariant under admissible regulator changes.

## Durable artifacts

- research/benincasa/check_soft_endpoint_log_primitive_torsor.py
- research/benincasa/soft-endpoint-log-primitive-torsor.json

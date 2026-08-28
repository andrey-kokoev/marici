# Fixed-diagnostic leakage converges without uniform strictification

## Question

The cutoff leakage cells add coherently over refinement shells. Does their
infinite refinement converge, and does that make the finite diagnostic system
asymptotically strict?

## Fixed diagnostic theorem

Let \(F\) be a bounded operator on a Hilbert space and let \(P_n\) be
increasing finite-rank orthogonal projections converging strongly to the
identity. Fix one finite diagnostic projection \(P_m\). Its outer leakage
after refinement to \(n\) is

\[
R_{m,n}=P_mF(I-P_n).
\]

The operator \(P_mF\) has finite rank and is therefore compact. Strong
convergence of \(I-P_n\) to zero is uniform after composition with a compact
operator. Hence

\[
\lVert R_{m,n}\rVert\longrightarrow0
\qquad(n\to\infty).
\]

For each fixed diagnostic window, the shell cocycle therefore converges in
operator norm to its complete leakage.

## Why this does not make the system strict

Uniform convergence over growing windows would require

\[
\sup_m\lVert P_mF(I-P_m)\rVert\longrightarrow0,
\]

or an equivalent quasi-locality estimate. Boundedness of \(F\) does not imply
this.

Take the backward unilateral shift on the standard basis. Every growing
cutoff has one unit-strength edge entering from the next omitted coordinate:

\[
\lVert P_mF(I-P_m)\rVert=1
\]

for every nonterminal \(m\). Yet for each fixed \(P_m\), refinement beyond
that edge makes \(P_mF(I-P_n)=0\).

Thus pointwise completion and uniform strictification are different claims.

## Categorical meaning

The lax diagnostic functor is complete at every fixed observer, but the family
of observers need not become a strict natural transformation uniformly. The
moving boundary can continue to carry a nonvanishing defect even though every
stationary observer is eventually reconciled.

This is the precise form of a relationship whose location escapes while its
effect does not disappear. The defect is not a hidden state at infinity; it
is a uniformly moving incidence boundary.

## Consequence for the source programme

To pass from finite diagnostics to the restricted-product source, one needs a
source-derived off-diagonal estimate stronger than bounded sewing. Possible
forms include compactness relative to the cutoff filtration, summable shell
norms, or a pro-Gram domination inequality.

Without such an estimate, fixed-cutoff convergence cannot authorize:

- uniform completion stability;
- interchange of cutoff limit with sewing;
- disappearance of the leakage cell;
- or a finite controller interpreted as the completed source.

## DPC verdict

Resolved: norm convergence of the leakage cocycle for each fixed finite
diagnostic under bounded completed sewing.

Falsified: the inference from fixed-diagnostic convergence to uniform
strictification.

Open: a source-local quasi-locality or summability law for the actual
Fourier–Tate boundary filtration.

## Verification

The checker `check_fixed_vs_uniform_leakage.py` verifies the exact shift
family: every fixed diagnostic residual eventually vanishes, while the moving
cutoff residual has norm one at every stage.


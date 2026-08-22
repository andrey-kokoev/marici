# Bare-Carrier Naturality No-Go

## Target

Can one source-natural witness/localization calculus derive a nontrivial
filtration from the bare common Carrier alone?

## General argument

Let (F(V)\subseteq V) be a subspace assigned naturally to every vector space
and every linear map. If (0\neq v\in F(V)), then for any vector (w\in W)
there is a linear map (f:V\to W) with (f(v)=w). Naturality gives

\[
w=f(v)\in F(W).
\]

Hence (F(W)=W) for every (W). Otherwise (F=0). The identity functor on
bare vector spaces therefore has no nonzero proper natural subfunctor.

## Bounded exact control

For (V=\mathbf F_5^2), all six candidate lines were enumerated, along with all

\[
|\mathrm{GL}_2(\mathbf F_5)|=480
\]

automorphisms. No line is invariant under the full group. Only (0) and (V)
survive universal symmetry.

## Falsification

\[
\boxed{
\text{bare Carrier}+\text{full naturality}
\not\Rightarrow
\text{nontrivial sector filtration}.
}
\]

Thus “one calculus” cannot mean a functor of the unadorned Carrier alone. A
nontrivial grade requires additional source-defined structure that reduces the
symmetry: support, marking, polarization, coefficient object, boundary
condition, or physical pairing.

## Surviving Deutsch--Popperian conjecture

There is a shared **indexed calculus**, not a universal output functor:

\[
\mathfrak W(\mathcal C;\mathcal K,\mathcal S,\mathcal P)
\]

where \(\mathcal C\) is the common Carrier, \(\mathcal K\) a sector coefficient
object, \(\mathcal S\) source-defined support/marking data, and \(\mathcal P\)
an admitted pairing or record interface. The operations and coherence laws of
\(\mathfrak W\) are shared; its nontrivial filtrations are indexed by the extra
data and must be natural only under maps preserving that data.

This is falsifiable: freeze the indexed inputs in each sector, derive the
filtration without fitting its ranks, and test the same localization and
Beck--Chevalley laws across sectors.

## Reproduction

```text
python research/nima/checkers/check_bare_carrier_naturality_no_go.py
```

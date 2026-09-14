# The minimal Suzuki endpoint completion is the cokernel projection and is tautological until arithmetically identified

## Two-term defect complex

Start with the linearized Suzuki leakage

\[
H_0\xrightarrow{L}H_1,
\qquad
H_0=H_1=H_+.
\]

Its odd harmonic obstruction is

\[
\ker L^*=(\overline{\operatorname{ran}L})^\perp.
\]

There is a canonical minimal endpoint space

\[
E=\ker L^*
\]

and a canonical boundary differential

\[
R=P_E:H_1\longrightarrow E.
\]

Because `E` is orthogonal to `ran L`,

\[
RL=0.
\]

Thus

\[
\boxed{
0\longrightarrow H_0
\xrightarrow{L}
H_1
\xrightarrow{P_{\ker L^*}}
\ker L^*
\longrightarrow0
}
\]

is a Hilbert complex defined solely from `L`.

## Cohomology

The degree-zero cohomology is

\[
H^0=\ker L.
\]

At degree one,

\[
\ker R=(\ker L^*)^\perp
=\overline{\operatorname{ran}L}.
\]

Hence the reduced degree-one cohomology vanishes:

\[
\bar H^1
=
\ker R/\overline{\operatorname{ran}L}
=0.
\]

Since `R` is onto `E`, degree-two cohomology also vanishes. Therefore the minimal endpoint completion kills the odd **reduced** harmonic sector exactly.

If `ran L` is closed, the unreduced complex is exact at `H_1` as well:

\[
\ker R=\operatorname{ran}L.
\]

If the range is not closed, a non-Hausdorff quotient `closure(ran L)/ran L` remains. This recovers the closed-range gate in homological form.

## Completed supersymmetric Laplacians

Let

\[
d_0=L,
\qquad d_1=R.
\]

The Hodge Laplacians are

\[
\Delta_0=L^*L,
\]

\[
\boxed{
\Delta_1=LL^*+R^*R
=LL^*+P_{\ker L^*},
}
\]

and

\[
\Delta_2=RR^*=I_E.
\]

The added endpoint term is positive and acts as the identity precisely on the former cokernel harmonic sector. Thus it removes the zero mode there without altering `closure(ran L)`.

When `ran L` is closed and `L` is bounded below on `(ker L)^perp`, `Delta_1` is bounded below on all of `H_1`. The endpoint completion then produces a genuine coercive odd Laplacian.

## Minimality

Suppose another bounded endpoint differential

\[
R':H_1\to E'
\]

satisfies `R'L=0` and is injective on `ker L*`. Since it annihilates `ran L`, it factors through the cokernel. On the harmonic sector this gives an injective map

\[
\ker L^*\hookrightarrow E'.
\]

Therefore

\[
\dim E'\ge\dim\ker L^*
\]

in finite defect models. The choice `E=ker L*` and `R=P_E` has the smallest possible endpoint dimension and unit norm.

## Why this is not yet an arithmetic repair

The construction defines the endpoint space to be the obstruction itself. Consequently its success is formal:

\[
\text{cokernel}
\xrightarrow{\mathrm{id}}
\text{a newly declared copy of the cokernel}.
\]

It does not show that the actual zeta endpoint--gamma source carries this space or this projection. In particular, the arithmetic endpoint contribution is highly constrained: it has fixed rank, normalization, translation law, and coupling to the prime sector. The abstract space `ker L*` may have incompatible dimension or representation type.

Therefore identifying

\[
P_{\ker L^*}

=
R_{endpoint\text{--}gamma}
\]

is the new comparison theorem, not a consequence of Hodge completion.

## Finite-Blaschke obstruction count

For `Theta=S/B` with finite Blaschke degrees `m,n`,

\[
\dim E
=
\dim\ker L^*
=
\max(n-m,0).
\]

Thus the minimal endpoint rank changes with the excess forbidden divisor degree. A fixed rank-one zeta endpoint cannot realize this completion uniformly for arbitrary finite generalized-inner symbols.

For the actual completed-zeta symbol, a rank match would require a theorem controlling the Toeplitz cokernel before the endpoint is identified. If the cokernel contains multiple independent off-axis orbit channels, a scalar endpoint cannot kill them all.

## Translation representation

The canonical endpoint `E=ker L*` inherits the compressed translation representation of the cokernel. Off-axis divisor components remain hyperbolic/Krein under bilateral translation. Although `P_E` is a bounded orthogonal projection, declaring `E` positive changes their original arithmetic cross-polarization. Recovering the Weil form requires a Green identity proving that the physical endpoint norm has exactly this sign and representation.

The earlier covariance obstruction therefore reappears at identification time rather than at construction time.

## Exact acceptance test

A valid source completion must provide a Hilbert space `E_src`, a boundary map `R_src`, and a unitary identification `U:E_src -> ker L*` such that

\[
UR_{src}=P_{\ker L^*}
\]

on the common source domain, while independently deriving:

1. `R_src L=0`;
2. positivity of the endpoint norm;
3. the exact completed Weil Green identity;
4. translation and conjugation compatibility;
5. sufficient rank to cover the full cokernel.

Without this comparison, the minimal endpoint completion is only the universal formal mapping cone.

## Disposition

A canonical positive endpoint completion exists abstractly:

\[
\boxed{
H_+
\xrightarrow{L}
H_+
\xrightarrow{P_{\ker L^*}}
\ker L^*.
}
\]

It kills the reduced odd harmonic defect and yields the positive Laplacian

\[
\Delta_1=LL^*+P_{\ker L^*}.
\]

But it does so by copying the cokernel into a newly declared endpoint. The substantive unresolved theorem is identification of this minimal endpoint with the fixed endpoint--gamma--prime source. Rank and translation type provide immediate falsifiers for that identification.

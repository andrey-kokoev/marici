# The renormalized local heat supertrace extracts the finite-prime Weil current

## Supersymmetric pair

For a finite set of primes `S`, let

\[
A_S(s)=\operatorname{Im}\log M_S(s),
\qquad
V_S=A_S'.
\]

Because every local inverse Euler factor

\[
1-p^{-1/2-is}
\]

stays a positive distance from zero on the real axis, one may choose a smooth real phase branch locally, and its derivative is globally well-defined. For finite `S`, `A_S` and all of its derivatives are bounded after choosing a continuous branch modulo constants.

Let

\[
D=-i\partial_s,
\qquad
Q=D+iA_S,
\qquad
Q^*=D-iA_S.
\]

The partner Hamiltonians are

\[
H_+=Q^*Q=D^2+A_S^2+V_S,
\]

\[
H_-=QQ^*=D^2+A_S^2-V_S.
\]

Both are nonnegative self-adjoint operators under their standard closed realizations.

## Localized supertrace

Let `chi` be a smooth compactly supported real multiplier. Define

\[
\operatorname{Str}_\chi(t)
=
\operatorname{Tr}(M_\chi e^{-tH_+})
-
\operatorname{Tr}(M_\chi e^{-tH_-}).
\]

For `t>0`, each localized heat operator is trace class in one dimension. The individual traces are nonnegative when `chi>=0`, but their difference has no fixed sign.

## Small-time extraction

For a scalar Schrödinger operator

\[
H=-\partial_s^2+U(s),
\]

the diagonal heat kernel has local expansion

\[
K_H(t;s,s)
=
(4\pi t)^{-1/2}
\left(1-tU(s)+O(t^2)ight)
\]

uniformly on compact sets when `U` is smooth with bounded derivatives there.

Here

\[
U_+=A_S^2+V_S,
\qquad
U_-=A_S^2-V_S.
\]

Subtracting cancels both the free coefficient and the quadratic Euler phase:

\[
K_{H_+}(t;s,s)-K_{H_-}(t;s,s)
=
-2t(4\pi t)^{-1/2}V_S(s)
+O(t^{3/2}).
\]

Since

\[
2t(4\pi t)^{-1/2}=
\sqrt{t/\pi},
\]

integration against `chi` gives

\[
\operatorname{Str}_\chi(t)
=
-\sqrt{t/\pi}
\int_\mathbb R\chi(s)V_S(s)ds
+O(t^{3/2}).
\]

Therefore

\[
\boxed{
\int_\mathbb R\chi(s)V_S(s)ds
=
-\lim_{t\downarrow0}
\sqrt{\pi/t}
\operatorname{Str}_\chi(t).
}
\]

This is the desired localized heat-supertrace identity for the finite-prime current.

## Prime-power expansion

Substituting

\[
V_S(s)=
\sum_{p\in S}(\log p)
\sum_{k\ge1}p^{-k/2}\cos(ks\log p)
\]

yields

\[
\boxed{
-\lim_{t\downarrow0}
\sqrt{\pi/t}
\operatorname{Str}_\chi(t)
=
\sum_{p\in S}(\log p)
\sum_{k\ge1}p^{-k/2}
\int\chi(s)\cos(ks\log p)ds.
}
\]

Thus the renormalized graded heat coefficient reproduces exactly the complete finite-place von-Mangoldt tower paired with the observer `chi`.

No zero data or prime truncation in the power index `k` is used; convergence is geometric for each finite prime set.

## Cross-prime terms cancel at the extracted order

The square

\[
A_S^2=
\sum_pA_p^2+
2\sum_{p<q}A_pA_q
\]

contains all cross-prime products. It appears identically in `H_+` and `H_-`, so it cancels in the first graded heat coefficient. The surviving derivative is additive:

\[
A_S'=
\sum_pA_p'.
\]

This matches the logarithmic nature of the Weil prime distribution. The `2x2` supersymmetric tower therefore performs the required product-to-logarithm conversion through graded heat asymptotics.

## Naturality under adjoining a prime

If `q notin S`, then

\[
A_{S\cup\{q\}}=A_S+A_q
\]

up to a phase constant, and

\[
V_{S\cup\{q\}}=V_S+V_q.
\]

The extracted functional consequently obeys

\[
\mathcal W_{S\cup\{q\}}^{prime}(\chi)
=
\mathcal W_S^{prime}(\chi)
+
\mathcal W_q^{prime}(\chi).
\]

Prime additions commute, so the renormalized supertrace coefficient forms a coherent additive tower.

## Why this still is not positive

The identity writes the prime functional as a **difference** of two positive localized heat traces followed by a singular rescaling. Neither operation preserves positivity:

\[
\operatorname{Tr}(M_\chi e^{-tH_+})
-
\operatorname{Tr}(M_\chi e^{-tH_-})

greaterless
0.
\]

Moreover, the common positive leading divergence cancels before multiplication by `t^{-1/2}`. The resulting finite coefficient is a local anomaly, not a positive trace.

Thus the construction realizes the exact prime current and its tower coherence, but not Weil positivity.

## Archimedean and endpoint additions

The same local heat-coefficient mechanism applies formally to a smooth archimedean phase primitive `A_infinity`, producing its phase derivative. A complete proof must establish symbol bounds for the gamma phase and show that localized heat differences remain trace class.

The endpoint/pole term is not a smooth phase derivative on the real spectral line. It must enter as a boundary condition, finite-rank extension, or eta-type correction. The completed target is therefore

\[
W_S(\chi)
=
-\lim_{t\downarrow0}
\sqrt{\pi/t}
\operatorname{Str}_\chi(t;A_\infty+A_S)
+E_{endpoint}(\chi),
\]

with the global explicit-formula sign fixed by convention.

## Rung-four implication and remaining gate

The construction provides a source-derived realization of the linear endpoint-free local current at every finite place stage, natural under the prime and contratowers. To obtain rung-four cone admission one still needs to reorganize the **completed** expression as an ordinary positive trace or prove that the endpoint plus gamma sector dominates the signed anomaly on every convolution-square observer.

The archimedean Connes--Consani theorem accomplishes such domination on a restricted support space. No corresponding estimate is known after `A_S` includes prime phases.

## Disposition

The localized supertrace experiment succeeds algebraically:

\[
\boxed{
V_S=A_S'
=
-\lim_{t\downarrow0}
\sqrt{\pi/t}
\left[
K_{H_+}(t;s,s)-K_{H_-}(t;s,s)
\right]
}
\]

in the distributional/localized sense after integration against a smooth compact observer.

This gives the sought finite-place `2x2` realization from Euler factors to the additive prime-power Weil current. Its failure mode is now isolated: the extracted quantity is a signed heat anomaly, not a positive trace. Endpoint--gamma completion must supply the positivity theorem.

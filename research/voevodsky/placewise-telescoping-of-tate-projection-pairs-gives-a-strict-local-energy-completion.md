# Placewise telescoping of Tate projection pairs gives a strict local-energy completion

## Ordered finite place set

Let

\[
S
=
\{v_1,
\ldots,
v_r\}
\]

be a finite semilocal place set with a declared ordering. On one compatible angular character sector, write the product Tate phase as

\[
\boxed{
\Gamma_S
=
\gamma_{v_1}
\gamma_{v_2}
\cdots
\gamma_{v_r}.
}
\]

All factors are unimodular multiplication operators on the unitary Mellin axis.

## Partial products

Define

\[
\Gamma_0
=1,
\]

\[
\Gamma_k
=
\prod_{j=1}^{k}
\gamma_{v_j}
\]

and the corresponding Hardy projections

\[
\boxed{
Q_k
=M_{\Gamma_k}
\Pi
M_{\Gamma_k}^*.
}
\]

Then

\[
Q_0
=\Pi,
\qquad
Q_r
=Q_{\Gamma_S}.
\]

## Exact telescoping

The full semilocal projection difference is

\[
\boxed{
Q_{\Gamma_S}-\Pi
=
\sum_{k=1}^{r}
(Q_k-Q_{k-1}).
}
\]

This is an exact finite operator identity.

Define the local increment

\[
\boxed{
\Delta Q_{v_k}^{(k-1)}
=Q_k-Q_{k-1}.
}
\]

## Conjugation to one local phase

Since

\[
\Gamma_k
=
\Gamma_{k-1}
\gamma_{v_k},
\]

one has

\[
\boxed{
\Delta Q_{v_k}^{(k-1)}
=
M_{\Gamma_{k-1}}
\left(
M_{\gamma_{v_k}}
\Pi
M_{\gamma_{v_k}}^*
-\Pi
\right)
M_{\Gamma_{k-1}}^*.
}
\]

Thus each increment is a unitary conjugate of a single-place relative projection pair.

Observer Mellin multipliers commute with `M_(Gamma_(k-1))`, so this conjugation does not change observer placement or Schatten norms.

## Local Hadamard rows

For each place, form projection features for `Q_k` and `Q_(k-1)` and take their Hadamard difference row

\[
\boxed{
D_{v_k}^{(k-1)}
=
\frac12
(F_{Q_k}-F_{Q_{k-1}}).
}
\]

Its observer-localized positive Gram is

\[
\boxed{
(D_{v_k}^{(k-1)})^*
D_{v_k}^{(k-1)}
=
\frac12
(\Delta Q_{v_k}^{(k-1)})^2.
}
\]

By unitary conjugation, its Hilbert--Schmidt norm is the single-place phase energy.

## Local phase-energy density

Define

\[
\boxed{
\kappa_{v_k,\chi}(t)
=
\frac1{4\pi^2}
\int
\frac{
|\gamma_{v_k,\chi}(s)-
\gamma_{v_k,\chi}(t)|^2
}{|s-t|^2}ds.
}
\]

Then

\[
\boxed{
\|D_{v_k}^{(k-1)}M_m\|_2^2
=
\frac12
\int
\kappa_{v_k,\chi}(t)
|m(t)|^2dt.
}
\]

The preceding product phase `Gamma_(k-1)` drops out of the norm.

## Orthogonal local direct sum

Define the semilocal difference feature

\[
\boxed{
D_S^{loc}M_m
=
\bigoplus_{k=1}^{r}
D_{v_k}^{(k-1)}M_m.
}
\]

Its positive Gram is the sum of local phase energies:

\[
\boxed{
\|D_S^{loc}M_m\|_2^2
=
\frac12
\sum_{v\in S}
\int
\kappa_{v,\chi}(t)
|m(t)|^2dt.
}
\]

This is positive and contains no cancellation among places.

## Signed cross readout

For each increment, the common/difference cross identity gives

\[
C_{v_k}^*J_2D_{v_k}
+D_{v_k}^*J_2C_{v_k}
=
Q_k-Q_{k-1}.
\]

Take the orthogonal direct sum of local common/difference pairs and sum their signed readouts. Exact telescoping yields

\[
\boxed{
\sum_{k=1}^{r}
(Q_k-Q_{k-1})
=
Q_{\Gamma_S}-\Pi.
}
\]

Thus the local positive feature realizes the same full semilocal relative projection current.

## Tate logarithmic derivative

The signed trace of the `k`-th increment is

\[
\boxed{
\frac1{2\pi i}
\int
\overline{m_h}
m_g
\partial_s
\log\gamma_{v_k}ds
+
e_{end,v_k}(g,h).
}
\]

Summing places gives

\[
\begin{aligned}
\sum_{v\in S}
\partial_s
\log\gamma_v
&=
\partial_s
\log
\left(
\prod_{v\in S}
\gamma_v
\right)\\
&=
\partial_s
\log\Gamma_S
\end{aligned}
\]

with winding branches tracked by the sum of local index terms.

Therefore the signed local-energy completion has exactly the global Tate--Weil readout.

## Avoiding derivative cancellation

For the product phase, large local derivatives may cancel:

\[
\partial_s
\log\Gamma_S
=
\sum_v
\partial_s
\log\gamma_v.
\]

A differential inequality for the product phase can then fail even when every local phase is regular.

The local direct-sum norm instead uses

\[
\boxed{
\sum_v
\kappa_{\gamma_v}
}
\]

and therefore retains every local absolute energy before signed summation.

No cancellation can weaken the positive control norm.

## Local derivative domination

Suppose each local phase satisfies

\[
|	heta_v''|
\le
M_v
(1+|\theta_v'|)^2.
\]

Then the inverse-slope lemma gives

\[
\boxed{
|	heta_v'|
\le
C_v
(1+\kappa_{\gamma_v}).
}
\]

For fixed finite `S`, summing gives

\[
\boxed{
\left|
\sum_{v\in S}
\theta_v'
\right|
\le
C_S
\left(
1+
\sum_{v\in S}
\kappa_{\gamma_v}
\right).
}
\]

Thus the full semilocal Tate form is continuous in the local-energy graph norm.

## Local-energy graph domain

Define

\[
\boxed{
\mathcal D_{loc,S}
=
\left\{
(m_\chi):
\sum_\chi
\int
\left[
1+
\sum_{v\in S}
\kappa_{v,\chi}(t)
\right]
|m_\chi(t)|^2dt
<\infty
\right\}.
}
\]

This weighted `L2` space is a positive Hilbert graph domain. The local difference feature is bounded into the direct sum of Hilbert--Schmidt ideals, and the signed Tate form is continuous on it under the local derivative estimates.

## Ramified conductors

For a ramified local phase

\[
\gamma_{v,\chi}(s)
=
e^{-if(\chi_v)
\log q_vs}
\times
\text{constant},
\]

\[
\boxed{
\kappa_{v,\chi}
=
\frac{
f(\chi_v)
\log q_v
}{2\pi}.
}
\]

Hence the local-energy graph norm automatically contains the additive conductor weight

\[
\sum_{v\in S_f}
f(\chi_v)
\log q_v.
\]

This is exactly compatible with placewise addition.

## Place enlargement

Let

\[
S'
=S\cup\{v_{r+1}\}.
\]

Choose the ordering extending that of `S`. Then

\[
\boxed{
D_{S'}^{loc}
=
D_S^{loc}
\oplus
D_{v_{r+1}}^{(r)}.
}
\]

The old positive feature embeds orthogonally and the new place contributes one new local row. Therefore place enlargement is a strict isometry on the existing local-energy carrier.

The signed readout adds exactly the new local Weil distribution.

## Ordering dependence

The individual conjugated increments depend on the order of places through `Gamma_(k-1)`. Their Hilbert--Schmidt norms do not, because preceding multiplication phases are unitary and commute with observer multipliers.

Different place orderings have the same source Gram because every preceding factor acts by a commuting multiplication unitary. Hence their observer-generated positive feature ranges are unitarily equivalent by polar comparison. Writing a canonical adjacent-transposition intertwiner on the full unused carrier would require an additional choice and is not asserted.

The summed signed operator is order independent by telescoping to `Q_(Gamma_S)-Pi`.

Thus ordering is presentation data, not boundary data.

## Endpoint additivity

Each place carries its own normalized principal-value/index channel. Under telescoping, endpoint terms add:

\[
\boxed{
E_{end,S}
=
\sum_{v\in S}
E_{end,v}.
}
\]

This agrees with the additive local Weil distribution and prevents global branch ambiguities from being hidden inside one product logarithm.

## Cutoff translation

The common cutoff phase `e^(2iLs)` multiplies the full product projection. It can be conjugated out before placewise telescoping. Every local difference row is then cutoff independent.

The left-placement projection remains the only moving cutoff component, and its observer commutator is handled by the same Riemann--Lebesgue argument place by place.

## Dyadic refinement

Each local projection pair increment may be Halmos-decomposed and dyadically refined. Taking the orthogonal sum over places commutes with these refinements.

Thus the full positive carrier is filtered by:

- place index;
- angular conductor;
- dyadic depth;
- finite outer regulator.

All place and depth successor maps are strict isometries on existing rows.

## Comparison with the single product-phase row

The single product-phase difference row has norm controlled by

\[
\kappa_{\Gamma_S}.
\]

The local direct-sum row has norm controlled by

\[
\sum_v
\kappa_{\gamma_v}.
\]

They have the same signed readout but generally different positive norms. The local direct sum is larger and more coercive because it prevents cancellation among place deformations.

The realization-functor principle favors the local sum: adding a place appends a source-derived row rather than globally changing one nonlinear phase-energy density.

## Disposition

The full semilocal projection difference has the exact placewise positive presentation

\[
\boxed{
Q_{\Gamma_S}-\Pi
=
\sum_{k=1}^{|S|}
(Q_k-Q_{k-1}),
}
\]

with positive relative norm

\[
\boxed{
q_{loc,S}(g)
=
\frac12
\sum_{v\in S}
\sum_\chi
\int
\kappa_{v,\chi}
|m_{g,\chi}|^2.
}
\]

This local-energy completion controls conductor and archimedean growth without requiring a differential inequality for the product phase. Place enlargement is strict orthogonal row addition, and the signed readout is exactly the additive semilocal Weil form.

# The local phase-energy completion turns the Tate form into a bounded self-adjoint multiplier

## Place-resolved positive weight

For a finite semilocal set `S`, define

\[
\boxed{
\kappa_{loc,S}(\chi,t)
=
\sum_{v\in S}
\kappa_{v,\chi}(t).
}
\]

Let

\[
\boxed{
e_S(\chi,t)
=1+
\kappa_{loc,S}(\chi,t).
}
\]

This is measurable and satisfies

\[
e_S
\ge1.
\]

## Energy Hilbert space

Define

\[
\boxed{
\mathscr E_S
=
\bigoplus_\chi
L^2
\left(
\mathbb R,
e_S(\chi,t)
\frac{dt}{2\pi}
\right).
}
\]

Its norm is

\[
\boxed{
\|m\|_{\mathscr E_S}^2
=
\sum_\chi
\int
 e_S(\chi,t)
|m_\chi(t)|^2
\frac{dt}{2\pi}.
}
\]

The `1` controls the Plancherel source norm; `kappa_(loc,S)` controls the positive Hilbert--Schmidt norm of all local difference rows.

## Signed Tate multiplier

Let

\[
\boxed{
w_S(\chi,t)
=
\sum_{v\in S}
w_{v,\chi}(t),
\qquad
w_{v,\chi}
=
\frac1i
\partial_t
\log\gamma_{v,\chi}.
}
\]

After endpoint/index extraction, `w_S` is real almost everywhere.

Assume the local inverse-slope estimates yield

\[
\boxed{
|w_S(\chi,t)|
\le
C_S
 e_S(\chi,t)
}
\]

on the admitted place/conductor class.

## Bounded normalized multiplier

Define

\[
\boxed{
a_S(\chi,t)
=
\frac{
w_S(\chi,t)
}{
e_S(\chi,t)
}.
}
\]

Then `a_S` is real and essentially bounded:

\[
\boxed{
|a_S|
\le
C_S.
}
\]

Let

\[
\boxed{
\mathcal A_S
=M_{a_S}
}
\]

on `E_S`. It is a bounded self-adjoint operator with

\[
\boxed{
\|\mathcal A_S\|
\le
C_S.
}
\]

## Representation of the Tate form

The energy-space inner product is

\[
\langle m,n\rangle_{\mathscr E_S}
=
\sum_\chi
\int
\overline{n_\chi}
m_\chi
 e_S
\frac{dt}{2\pi}.
\]

Therefore

\[
\begin{aligned}
\langle
m,
\mathcal A_S n
\rangle_{\mathscr E_S}
&=
\sum_\chi
\int
\overline{m_\chi}
n_\chi
 e_S
\frac{w_S}{e_S}
\frac{dt}{2\pi}
\end{aligned}
\]

up to the chosen linear-slot convention. Equivalently,

\[
\boxed{
q_{Tate,S}(m,n)
=
\langle
m,
\mathcal A_S n
\rangle_{\mathscr E_S}
}
\]

with the inner-product slots ordered consistently.

Thus the formerly unbounded Tate multiplication form becomes bounded on the positive phase-energy completion.

## Jordan legs

Define bounded positive operators

\[
\boxed{
\mathcal A_{S,+}
=
\max(\mathcal A_S,0),
\qquad
\mathcal A_{S,-}
=
\max(-\mathcal A_S,0).
}
\]

Their square roots are bounded:

\[
\|\mathcal A_{S,\pm}^{1/2}\|
\le
\sqrt{C_S}.
\]

The ordinary two-polarity boundary feature is

\[
\boxed{
\Phi_S^{energy}(m)
=
\left(
\mathcal A_{S,+}^{1/2}m,
\mathcal A_{S,-}^{1/2}m
\right)
\in
\mathscr E_S
\oplus
\mathscr E_S.
}
\]

Its positive Gram is

\[
\boxed{
\|\Phi_S^{energy}(m)\|^2
=
\langle
m,
|\mathcal A_S|m
\rangle_{\mathscr E_S}
}
\]

and its signed readout is

\[
\boxed{
\langle
\Phi_S^{energy}(m),
J
\Phi_S^{energy}(n)
\rangle
=q_{Tate,S}(m,n).
}
\]

This is an ordinary finite-norm Hilbert feature on the energy completion.

## Relation to the original multiplication operator

On the Plancherel carrier, the Tate operator is

\[
A_S
=M_{w_S}
\]

with form domain `D(|A_S|^(1/2))`.

Let

\[
U_e:
\mathscr E_S
\to
\mathscr H_S
\]

be multiplication by `e_S^(1/2)`. It is unitary from weighted `L2(e_S dt)` to ordinary `L2(dt)`.

Under this unitary,

\[
\boxed{
U_e
\mathcal A_S
U_e^{-1}
=M_{a_S}
\]

as a bounded multiplier, while the original form is recovered by inserting the energy embedding rather than identifying `A_S` itself with `M_(a_S)` on Plancherel space.

The distinction is metric: `w_S` is unbounded in the Plancherel metric but bounded relative to `e_S`.

## Form-domain comparison

If

\[
e_S
\asymp
1+|w_S|
\]

without destructive place cancellation, then

\[
\boxed{
\mathscr E_S
=
D(|A_S|^{1/2})
}
\]

with equivalent norms.

The placewise construction generally gives the stronger weight

\[
1+
\sum_v|w_v|
\]

rather than

\[
1+
|\sum_vw_v|.
\]

Hence `E_S` continuously embeds into the minimal product Tate form domain and retains local energy canceled by signed assembly.

## Difference-row embedding

The placewise Hilbert--Schmidt difference feature satisfies

\[
\boxed{
\|D_S^{loc}M_m\|_2^2
=
\pi
\sum_\chi
\int
\kappa_{loc,S}
|m_\chi|^2
\frac{dt}{2\pi}
}
\]

with the factor determined by the earlier kernel normalization.

Thus the map

\[
m
\longmapsto
D_S^{loc}M_m
\]

is bounded from `E_S` to the direct sum of Hilbert--Schmidt ideals.

The energy norm simultaneously controls the observer source and the positive relative deformation.

## Endpoint completion

Let `H_(end,S)` be the finite-dimensional or graph endpoint carrier obtained after splitting winding/pole terms. Define

\[
\boxed{
\mathscr E_S^{completed}
=
\mathscr E_S
\oplus
\mathscr H_{end,S}.
}
\]

If the endpoint form is bounded on its declared graph norm, adjoining its Jordan square roots gives a bounded completed boundary feature.

The regular multiplier and endpoint rows remain separately typed.

## Conductor behavior

For a ramified character,

\[
e_S
\ge
1+
\frac1{2\pi}
\sum_{v\in S_f}
f(\chi_v)
\log q_v.
\]

Meanwhile

\[
|w_S|
\le
\sum_v|w_v|
\]

has the same conductor growth. Therefore `a_S=w_S/e_S` remains uniformly bounded across conductor in the placewise energy metric even though `w_S` is not semibounded in unweighted Plancherel space.

This removes the earlier need to require `L>=F+C_S` merely to define the limiting Tate boundary. That inequality remains relevant to a physical finite-cutoff common-Plancherel-edge subtraction, not to the energy-space boundary itself.

## Place enlargement

Adding a place changes the energy metric:

\[
e_{S\cup\{v\}}
=e_S+
\kappa_v.
\]

The identity map from the stronger new energy space to the old one is contractive:

\[
\boxed{
\mathscr E_{S\cup\{v\}}
\hookrightarrow
\mathscr E_S.
}
\]

Thus place enlargement is naturally contravariant at the level of completed graph domains, while the resolved local difference feature enlarges covariantly by orthogonal row addition.

The complete structure is a correspondence between:

- covariant positive feature rows;
- contravariant energy domains.

## Packet compatibility

The global bounded multiplier `mathcal A_S` is formed before packet restriction. Therefore its positive and negative square roots restrict coherently to every finite observer packet.

This avoids the failure of compressed Jordan parts to commute with packet inclusion.

## Positivity criterion

The negative energy leg vanishes exactly when

\[
\mathcal A_{S,-}^{1/2}m
=0.
\]

Since `e_S>0`, this is equivalent to

\[
w_S(\chi,t)
\ge0
\]

on the spectral support of `m`.

The construction packages signed Tate positivity but does not prove it globally.

## Relation to the relative module filler

The relative module feature `(C,D)` remains the exact finite-regulator/physical presentation. The bounded energy feature is its graph completion/minimalization on the deformation domain.

There is a bounded map from the local difference row into the energy carrier and a bounded signed observation there. The divergent common row is no longer represented as a Hilbert--Schmidt vector; its effect is encoded in the bounded multiplier `mathcal A_S`.

Thus the two constructions serve different levels:

- `(C,D)`: exact regulator-relative physical dilation;
- `Phi_S^(energy)`: ordinary finite-norm boundary completion.

## Remaining comparison

To claim that physical regulated positive features converge strongly to `Phi_S^(energy)`, one still needs a non-isometric graph-domain quotient/minimalization map. The bounded boundary construction alone does not give strong convergence of raw common rows.

What is now established is existence of an ordinary Hilbert realization of the limiting signed form on a source-derived positive phase-energy domain.

## Disposition

With

\[
\boxed{
e_S
=1+
\sum_{v\in S}
\kappa_{\gamma_v},
\qquad
\mathcal A_S
=M_{w_S/e_S},
}
\]

the semilocal Tate form is represented by a bounded self-adjoint operator on the positive Hilbert space `E_S`. Its Jordan square roots give compatible finite-norm positive and negative boundary legs. This is the ordinary Hilbert completion of the regulator-relative `C_34` boundary on the local phase-energy graph domain.

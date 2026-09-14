# Finite-character Mellin--Schwartz observers are dense in the local phase-energy completion

## Energy carrier

For a finite semilocal place set `S`, let

\[
e_S(\chi,t)
=1+
\sum_{v\in S}
\kappa_{v,\chi}(t)
\]

and define

\[
\mathscr E_S
=
\bigoplus_\chi
L^2
\left(
\mathbb R,
e_S(\chi,t)
\frac{dt}{2\pi}
\right).
\]

Assume:

1. `e_S(chi,t)` is finite almost everywhere;
2. it is locally integrable in `t` for every `chi`;
3. on each finite conductor set it has at most polynomial growth in `t`;
4. conductor truncations exhaust the angular dual.

These conditions follow from the regular divided-difference estimates for local Tate phases after endpoint/index extraction.

## Finite-character compact spectral core

Define

\[
\boxed{
\mathcal C_S
=
\left\{
(m_\chi):
\begin{array}{l}
 m_\chi\in C_c^\infty(\mathbb R),\\
 m_\chi=0
 \text{ for all but finitely many }\chi
\end{array}
\right\}.
}
\]

Then

\[
\boxed{
\mathcal C_S
\subset
\mathscr E_S.
}
\]

Indeed, each component has compact support and `e_S` is locally integrable.

## Angular truncation

Let

\[
m
=(m_\chi)
\in
\mathscr E_S.
\]

Since the energy norm is a countable/nonnegative direct sum, for every `epsilon>0` there is a finite character set `Xi` such that

\[
\boxed{
\sum_{\chi\notin\Xi}
\int
 e_S(\chi,t)
|m_\chi(t)|^2
\frac{dt}{2\pi}
<\frac{\varepsilon^2}{3}.
}
\]

Thus finite angular support is dense.

## Radial cutoff

For each `chi in Xi`, monotone convergence gives a radius `R` such that

\[
\boxed{
\sum_{\chi\in\Xi}
\int_{|t|>R}
 e_S(\chi,t)
|m_\chi(t)|^2
\frac{dt}{2\pi}
<\frac{\varepsilon^2}{3}.
}
\]

Multiplication by a smooth cutoff equal to one on `[-R,R]` and supported in a slightly larger interval approximates `m` in energy norm.

Hence compact radial support is dense.

## Smooth approximation

On a fixed compact interval and finite character set, the measure

\[
e_S(\chi,t)dt
\]

is finite and absolutely continuous with positive density. Standard truncation followed by mollification shows

\[
C_c^\infty(\mathbb R)
\]

is dense in

\[
L^2(e_S(\chi,t)dt).
\]

Choose one smooth approximation for each of the finitely many retained characters so that the total remaining error is below `epsilon/sqrt(3)`.

Combining angular truncation, radial cutoff, and mollification gives

\[
\boxed{
\overline{\mathcal C_S}^{\|\cdot\|_{\mathscr E_S}}
=
\mathscr E_S.
}
\]

## Mellin inverse

For

\[
m_\chi
\in
C_c^\infty(\mathbb R),
\]

its inverse Fourier transform in logarithmic radius is Schwartz:

\[
\boxed{
\mathcal F^{-1}m_\chi
\in
\mathcal S(\mathbb R).
}
\]

Finite angular support gives a smooth finite Fourier sum on the compact angular group. Therefore inverse angular Mellin transform sends `C_S` into the semilocal radial/angular Schwartz observer class.

Thus the energy completion is generated densely by explicit test observers, not by formal spectral vectors alone.

## Relation to Bruhat--Schwartz functions

At finite places, finite angular support corresponds to invariance under a compact open subgroup, hence to bounded conductor level. Locally constant compactly supported finite-place factors produce finite character expansions after quotienting by the chosen unit subgroup.

At archimedean/logarithmic radius, inverse transforms of spectral `C_c^\infty` functions are Schwartz but need not be compactly supported. They lie in the natural Schwartz enlargement of Connes's compact-support test algebra.

Therefore two source cores must be distinguished:

1. the original compact-support convolution algebra;
2. its Mellin--Schwartz graph closure.

The density theorem is immediate for the second. Density of the first in the same energy norm requires a cutoff approximation argument in physical logarithmic coordinates.

## Physical cutoff approximation

Let `g` be a Schwartz logarithmic observer and choose smooth physical cutoffs `chi_R` with

\[
\chi_Rg
\to g
\]

in Schwartz topology. Their Mellin transforms converge to `m_g` in every polynomially weighted `L2` norm.

If `e_S` has at most polynomial growth on the observer's finite conductor support, then

\[
\boxed{
\|\mathcal M(\chi_Rg)-m_g\|_{\mathscr E_S}
\longrightarrow0.
}
\]

Each `chi_Rg` is compactly supported in logarithmic radius. Hence compact radial observers are dense in the energy domain under the polynomial weight hypothesis.

## Endpoint graph rows

If endpoint/index channels are finite-dimensional, append their graph norm to `E_S`. Density then requires convergence of the corresponding endpoint evaluations.

Choose cutoff approximations preserving the finitely many endpoint moments, or correct them by finite-rank compactly supported packets. Standard finite-codimension adjustment yields a dense compact observer core in the completed graph norm.

This step must follow the exact source endpoint convention.

## Core for the bounded Tate multiplier

The normalized Tate operator

\[
\mathcal A_S
=M_{w_S/e_S}
\]

is bounded on `E_S`. Since `C_S` is dense, `mathcal A_S` and its Jordan square roots are uniquely determined by their values on `C_S`.

Therefore the finite-norm boundary feature

\[
\Phi_S^{energy}
=(\mathcal A_{S,+}^{1/2},
\mathcal A_{S,-}^{1/2})
\]

is the unique continuous extension of its test-observer restriction.

## Difference-row closure

The map

\[
m
\longmapsto
D_S^{loc}M_m
\]

is bounded from `E_S` into the direct sum of Hilbert--Schmidt ideals. Hence its graph closure from `C_S` is exactly its extension to `E_S`.

No additional hidden difference-row vectors appear at completion.

## Place enlargement and density

For `S subset S'`, the new energy weight is stronger:

\[
e_{S'}
=e_S+
\sum_{v\in S'\setminus S}
\kappa_v.
\]

The same finite-character spectral core lies densely in both weighted spaces. Therefore the contravariant domain inclusion

\[
\mathscr E_{S'}
\hookrightarrow
\mathscr E_S
\]

has a common dense test core, which is essential for comparing signed forms under place enlargement.

## Countable core

Choose rational linear combinations of:

- finite angular characters;
- spectral bump functions with rational endpoints and rational polynomial coefficients;
- a countable family of mollifiers.

This produces a countable dense subspace

\[
\boxed{
\mathcal C_S^{count}
\subset
\mathscr E_S.
}
\]

It may be used in the cofinal diagonal regulator construction.

## What remains conditional

The density proof requires only local integrability for the abstract weighted space. Identifying its compact physical inverse transforms with the exact source test algebra additionally requires:

1. the source's Radon--Nikodym unitary convention;
2. polynomial energy-weight growth on finite conductor sectors;
3. endpoint moment control;
4. compatibility with quotienting by semilocal units.

These are domain-identification checks, not positivity assumptions.

## Disposition

Finite-character Mellin--Schwartz observers are dense in the positive local phase-energy space:

\[
\boxed{
\overline{
\bigoplus_{\chi}^{finite}
C_c^\infty(\mathbb R)
}^{\mathscr E_S}
=
\mathscr E_S.
}
\]

Under polynomial weight growth, compact logarithmic observers are also dense by physical cutoff approximation. Hence the ordinary Hilbert boundary completion is generated by the admitted test-level Tate data and supports a countable core for simultaneous regulator diagonalization.

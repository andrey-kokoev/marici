# The canonical primewise parity flip exists but its uniform margin collapses

## Character and displacement pairing

Fix an odd prime \(p\), a conductor-\(m\) parameter

\[
\eta=p^{-m}u,
\qquad
u\in\mathbb Z_p^\times,
\]

and choose the minimal source-relative displacement

\[
h_\eta=p^{m-1}u^{-1}.
\]

Then

\[
\eta h_\eta=p^{-1}.
\]

For the standard additive character convention,

\[
\psi_p(\eta h_\eta)
=
e^{2\pi i/p}.
\]

Thus the character parameter itself supplies a natural parity-changing displacement; no spectral zero data are used.

## Exact finite-difference action

Let

\[
f_\eta^{\mathrm{odd}}
=
\frac{f_\eta-f_{-\eta}}{2i},
\qquad
f_\eta^{\mathrm{even}}
=
\frac{f_\eta+f_{-\eta}}2,
\]

and define

\[
P_\eta=T_{h_\eta}-T_{-h_\eta}.
\]

Because \(h_\eta\in\mathbb Z_p\), translation preserves the support \(\mathbb Z_p\). Moreover,

\[
T_{\pm h_\eta}f_{\pm\eta}
=
\psi_p(\pm\eta(\pm h_\eta))f_{\pm\eta}.
\]

Direct calculation gives

\[
P_\eta f_\eta^{\mathrm{odd}}
=
2\sin\left(\frac{2\pi}{p}\right)
f_\eta^{\mathrm{even}}.
\]

Hence the previously dark odd port has an exact source-relative incidence into the even local Tate channel.

This is the finite-place analogue of differentiation sending sine to cosine.

## Primewise nonvanishing

For every odd prime,

\[
\sin\left(\frac{2\pi}{p}\right)\ne0.
\]

Therefore the parity-changing incidence is nonzero at every finite prime. The local constructor exists without fitting.

The first nontrivial phase gate is passed pointwise.

## Uniform collapse

As \(p\to\infty\),

\[
2\sin\left(\frac{2\pi}{p}\right)
\sim
\frac{4\pi}{p}.
\]

Thus the primewise odd-to-even observer coefficient tends to zero.

Every finite cutoff has a faithful odd port, but the all-prime lower frame bound vanishes:

\[
\inf_p
2\left|\sin\left(\frac{2\pi}{p}\right)\right|
=
0.
\]

This is exactly the finite-faithful/completion-dark hostile anticipated by the observer programme.

## Renormalization cost

One may define the normalized finite difference

\[
\widetilde P_\eta
=
\frac{T_{h_\eta}-T_{-h_\eta}}
{2\sin(2\pi/p)},
\]

so that

\[
\widetilde P_\eta f_\eta^{\mathrm{odd}}
=
f_\eta^{\mathrm{even}}.
\]

But the normalization grows like

\[
\frac{p}{4\pi}.
\]

After the primitive Euler half-density \(p^{-1/2}\), the effective size behaves like

\[
p^{-1/2}
\frac1{2\sin(2\pi/p)}
\asymp
p^{1/2}.
\]

Therefore the normalized all-prime primitive synthesis is worse than the original harmonic boundary. It cannot be inserted into the existing Hilbert or trace-ideal completion without a new compensating source weight.

The normalization repairs observability by destroying the current summability budget.

## No free phase choice

A displacement satisfying

\[
\eta h=\frac{r_p}{p}
\]

would produce phase \(e^{2\pi i r_p/p}\). Choosing \(r_p\) near \(p/4\) would keep the sine uniformly large.

But such a prime-dependent residue is additional source data. The distinguished spherical vacuum and the conductor parameter do not select a quarter-residue frame.

Using \(r_p\) solely to improve the margin would fit the topology.

The canonical prime-field unit \(r_p=1\) gives the collapsing coefficient above.

## Dyadic sector

At \(p=2\), conductor one has no nonzero antisymmetric pair. At deeper conductor one can choose \(\eta\) and \(h\) so that \(2\eta\notin\mathbb Z_2\) and the phase is nonreal.

This produces a finite dyadic parity flip, but it does not affect the large-prime collapse.

## Consequence for the RH feedback

The operator-valued mixed return can now be nonzero locally:

\[
V_{\mathrm{wj}}^*
(I-S_{\mathrm{even}})^{-1}
P_\eta
U_{\mathrm{odd}}.
\]

However, this construction cannot by itself supply a uniform completion margin across primes.

The programme must choose among:

1. accept a rigged, non-Hilbert odd observer;
2. derive an additional compensating prime weight;
3. construct a collective observer whose cross-prime geometry restores a lower frame;
4. find a different source operation with a uniformly separated phase.

None follows from local nonvanishing.

## Hostiles

1. Promote pointwise nonzero sine coefficients to a uniform lower bound.
2. Normalize by their inverse without re-auditing Euler summability.
3. choose a quarter-residue \(r_p\) without source authority;
4. ignore the dyadic conductor-one collapse;
5. infer all-prime observability from finite-cutoff rank.

## Verdict

The character conductor canonically supplies a local parity-changing finite difference, and it maps the divisor-free odd port to the even Tate channel exactly.

But its coefficient is \(2\sin(2\pi/p)\), which decays like \(p^{-1}\). The local constructor is solved while completion-stable odd observability fails in the raw source normalization.

# The Widom trace coefficient shows that fixed dyadic defect layers still have logarithmically divergent positive edge mass

## Classical trace law

For a one-dimensional prolate concentration operator `B_c` with large time--band parameter `c`, the classical Landau--Widom trace asymptotic has the schematic normalized form

\[
\boxed{
\operatorname{Tr}f(B_c)
=
N(c)f(1)
+
C_W\log c
\int_0^1
\frac{
f(t)-tf(1)
}{t(1-t)}dt
+
O_f(1).
}
\]

Here:

- `N(c)` is the Shannon/bulk counting term;
- `C_W>0` depends on Fourier/window normalization;
- the integral is the universal plunge coefficient;
- the formula is asserted for fixed sufficiently regular `f` with `f(0)=0`.

Exact constants are not needed for the conclusions below.

## One dyadic defect

At dyadic level `j`, set

\[
m=2^j
\]

and

\[
\boxed{
f_m(t)
=t^m(1-t^m).
}
\]

Since

\[
f_m(1)=0,
\]

the bulk counting term vanishes. The Widom coefficient is

\[
\begin{aligned}
I_m
&=
\int_0^1
\frac{t^m(1-t^m)}{t(1-t)}dt\\
&=
\int_0^1
t^{m-1}
\frac{1-t^m}{1-t}dt\\
&=
\sum_{k=0}^{m-1}
\int_0^1
t^{m+k-1}dt\\
&=
\sum_{k=0}^{m-1}
\frac1{m+k}\\
&=
H_{2m-1}-H_{m-1}.
\end{aligned}
\]

Therefore

\[
\boxed{
I_m
=H_{2m-1}-H_{m-1}
\longrightarrow
\log2
}
\]

as `m->infinity`.

For every fixed level `j`,

\[
\boxed{
\operatorname{Tr}
\left(
B_c^{2^j}
(I-B_c^{2^j})
\right)
=
C_W
(H_{2^{j+1}-1}-H_{2^j-1})
\log c
+
O_j(1).
}
\]

Thus one positive dyadic defect layer already diverges like `log c`.

## Finite accumulated residual

The first `n` levels telescope to

\[
B_c-B_c^{2^n}.
\]

Set

\[
m=2^n.
\]

The residual test function is

\[
\boxed{
r_m(t)
=t-t^m.
}
\]

Again `r_m(1)=0`. Its Widom coefficient is

\[
\begin{aligned}
J_m
&=
\int_0^1
\frac{t-t^m}{t(1-t)}dt\\
&=
\int_0^1
\frac{1-t^{m-1}}{1-t}dt\\
&=
H_{m-1}.
\end{aligned}
\]

Hence for fixed `n`,

\[
\boxed{
\operatorname{Tr}
(B_c-B_c^{2^n})
=
C_WH_{2^n-1}\log c
+
O_n(1).
}
\]

As `n` grows,

\[
H_{2^n-1}
=n\log2+O(1).
\]

So the formal fixed-function coefficient grows linearly with dyadic depth.

## Nonuniformity warning

The Widom formula above is for fixed `f`, hence fixed `n`, followed by `c->infinity`. It cannot be summed uniformly to depths comparable with the extremal prolate scale.

Indeed an expression of order

\[
n\log c
\]

must eventually violate the total trace bound if extrapolated to `n` of order `c`. The remainder and validity range become nonuniform before then.

Nevertheless the fixed-level conclusion is rigorous within the classical theorem's scope:

\[
\boxed{
\text{positive plunge mass persists at order }\log c
\text{ even after exact volume-bulk removal}.
}
\]

## Observer-weighted consequence

For an observer-weighted measure, the corresponding target asymptotic has the form

\[
\operatorname{Tr}
\left(
A_h^*
f(B_c)
A_g
\right)
=
C_W\log c
\mathcal G_f(g,h)
+
\mathcal F_f(g,h)
+
o(1),
\]

where `G_f` is the weighted universal plunge Gram form and `F_f` is the finite scattering-dependent part.

Even if `f(1)=0`, the `log c` plunge term generally remains. Therefore removing only the eigenvalue-one/near-one volume bulk does not produce convergent Hilbert--Schmidt boundary legs.

## Correction to the absolute-Gram target

A previous target asked for raw residual Gram convergence

\[
K_\Lambda^{res}
\longrightarrow
q_{|A_S|}.
\]

The Widom coefficient shows that this is generally too strong and likely false without a second subtraction/removal:

\[
\boxed{
K_\Lambda^{res}
=
(\log c_\Lambda)
G_{edge}
+
K_{finite}
+
o(1).
}
\]

The finite Tate absolute form, if physically realized, can only occur after the universal positive plunge feature is removed or recentered.

## Two distinct bulk layers

The positive geometry contains at least two asymptotic bulk scales:

1. **volume bulk**, of order `N(c)`, from eigenvalues near one and `f(1)`;
2. **edge bulk**, of order `log c`, from the Landau--Widom plunge coefficient.

The dyadic defect tower removes the first from each `f_m` because `f_m(1)=0`, but retains the second.

Thus “bulk-removed” must specify which layer has been removed.

## Reference-edge feature

Let `B_c^0` denote the pure cutoff/reference prolate pair with the same translation phase but no Tate scattering phase. A plausible positive recentering is not scalar subtraction, but comparison against a common reference edge feature:

\[
R_c^{Tate}
\oplus
R_c^{ref}.
\]

One seeks an orthogonal/common-submodule identification of their universal `sqrt(log c)` edge components. Removing that shared feature can leave finite residual legs.

At the signed trace level this is ordinary relative projection cancellation. At the positive feature level it requires a Douglas/isometric matching of the two universal edge Gram forms.

## Normalized edge limit

Before finite recentering, the canonical positive theorem to seek is

\[
\boxed{
\frac1{\log c_\Lambda}
K_{\Lambda,n}^{res}
\longrightarrow
G_{edge,n}
}
\]

for each fixed depth `n`, with

\[
G_{edge,n}
\]

carrying the harmonic-number coefficients above in the unweighted scalar model.

This normalized theorem identifies the universal edge feature that must be removed from both Tate and reference regulators.

## Arithmetic finite part

Only after constructing an isometry

\[
U_\Lambda:
\mathcal H_{edge}^{ref}
\to
\mathcal H_{edge}^{Tate}
\]

between the leading positive edge features can one define a genuine residual such as

\[
\boxed{
R_\Lambda^{finite}
=
R_\Lambda^{Tate}
-
U_\Lambda
R_\Lambda^{ref}
}
\]

or, preferably, the orthogonal complement of their common embedded edge submodule.

The norm of a vector difference includes cross terms and must be source-derived; it is not determined by subtracting Gram matrices entrywise.

## Relation to the Hardy relative trace

The relative Hardy formula automatically subtracts the pure translation projection at the signed trace level:

\[
\Pi_{e^{2iLs}\gamma}
-
\Pi_{e^{2iLs}}.
\]

This removes the universal linear spectral-flow density and exposes the gamma derivative.

The Widom calculation shows what the positive lift of that operation must do: identify and remove the common `sqrt(log c)` plunge feature, not merely the `sqrt(N(c))` volume feature.

## Revised positive `C_34` gates

The physical positive boundary now requires:

1. observer-weighted Widom asymptotics for fixed dyadic test functions;
2. angular summability of the edge Gram forms;
3. identification of a universal reference-edge feature;
4. a cutoff-compatible isometry between Tate and reference edge bulks;
5. convergence of the orthogonal finite residual to the global `|A_S|` boundary;
6. separate treatment of exact `H_11` and Sonin `H_00` atoms.

## Disposition

For fixed dyadic level `j`, the universal plunge coefficient is

\[
\boxed{
H_{2^{j+1}-1}
-
H_{2^j-1}
\longrightarrow
\log2.
}
\]

Therefore raw positive dyadic defects have logarithmically divergent edge mass. The earlier absolute-Gram convergence target must be understood only after both volume-bulk and universal edge-bulk removal. The next positive theorem is an observer-weighted Widom law and a positive reference-edge matching, not direct convergence of the uncentered defect cloud to `|A_S|`.

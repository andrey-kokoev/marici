# Ramified local Tate epsilon factors force conductor-filtered positive edge removal

## Local nonarchimedean gamma factor

Let `v` be a finite place with residue cardinality

\[
q=q_v.
\]

For a unitary multiplicative character `chi_v` of conductor exponent

\[
f=f(\chi_v)
\ge0,
\]

the local Tate gamma factor on the unitary axis has the standard structure

\[
\boxed{
\gamma_v
(\chi_v,
\tfrac12+is,
\psi_v)
=
\epsilon_v
(\chi_v,
\tfrac12+is,
\psi_v)
\frac{
L_v(\chi_v^{-1},
\tfrac12-is)
}{
L_v(\chi_v,
\tfrac12+is)
}.
}
\]

It is unimodular after the unitary normalization.

## Conductor phase

Up to a constant unimodular Gauss-sum phase, the epsilon factor contains

\[
\boxed{
q^{-f is}
}
\]

in the convention displayed above. Therefore

\[
\frac1i
\partial_s
\log q^{-fis}
=-f\log q.
\]

Thus the real Tate connection multiplier contains the conductor term

\[
\boxed{
w_{v,\chi_v}^{cond}
=-f(\chi_v)\log q_v.
}
\]

If the opposite gamma convention is used, the sign reverses. The magnitude and its unbounded growth with conductor are convention-independent.

## Ramified characters

For a ramified character, the local Euler `L` factor is trivial:

\[
L_v(\chi_v,s)=1.
\]

Hence the spectral derivative is exactly the conductor constant, apart from any fixed additive-character normalization shift:

\[
\boxed{
w_{v,\chi_v}(s)
=-f(\chi_v)\log q_v
+
c_{\psi_v}.
}
\]

It is independent of `s` but unbounded below as the character conductor grows.

Therefore

\[
\boxed{
\inf_{\chi_v,s}
w_{v,\chi_v}(s)
=-\infty
}
\]

in this orientation.

## Failure of global Plancherel-edge domination

The global common-edge criterion for a Plancherel edge is

\[
A_{S,-}
\le
LI.
\]

On a ramified character sector,

\[
A_{S,-}
\ge
f(\chi_v)\log q_v
-
C_S.
\]

For every finite cutoff `L`, choose `chi_v` with

\[
f(\chi_v)\log q_v
>L+C_S.
\]

Then

\[
\boxed{
LI-A_{S,-}
\]

is negative on that angular sector.

Consequently no finite cutoff admits one global positive common-edge Gram on the full unweighted angular Plancherel carrier.

## Unramified check

For an unramified unitary character, write its Euler parameter as `alpha` with `|alpha|=1` and set

\[
r=q^{-1/2}.
\]

The logarithmic derivative of the Euler ratio is a bounded Poisson-type function. In one standard phase convention its lower bound has magnitude at most

\[
\boxed{
2\log q
\frac{r}{1-r}
=
\frac{2\log q}{\sqrt q-1}.
}
\]

Thus the unramified sector is uniformly semibounded for each fixed finite set of places. The obstruction comes from unbounded ramification, not from large Mellin frequency in the spherical sector.

Exact signs depend on whether the local gamma factor or its inverse is assigned to the chosen Hardy polarity.

## Archimedean sector

At an archimedean place, the real logarithmic derivative is a digamma combination. Stirling asymptotics give

\[
w_{\chi_\infty}(s)
=
C\log(1+|s|)
+O(1)
\]

with positive leading sign in the standard completed orientation. Since there are only finitely many parity/angular types at a real place, the regular archimedean multiplier is bounded below after endpoint poles are separated.

Thus the decisive global negative tail is nonarchimedean conductor growth.

## Why smooth observers remain admissible

A Bruhat--Schwartz observer at a finite place is locally constant under some compact open subgroup. Its angular Fourier transform therefore occupies only characters up to a finite conductor level.

For each fixed observer `g`, there is

\[
F(g)<\infty
\]

such that

\[
m_{g,\chi}=0
\]

when

\[
f(\chi)>F(g).
\]

Hence every fixed observer packet sees only finitely many ramification levels and retains a finite lower bound.

The failure is global uniformity over the union of all test levels.

## Conductor filtration

Define the source filtration

\[
\boxed{
E^{(F)}
=
\{
g:
m_{g,\chi}=0
\text{ whenever }
\sum_{v\in S_f}
f(\chi_v)\log q_v>F
\}.
}
\]

On `E^(F)`, the negative Tate multiplier satisfies

\[
\boxed{
A_{S,-}
\preceq
(F+C_S)I.
}
\]

Therefore the common Plancherel edge Gram

\[
C_L
=LI-A_{S,-}
\]

is positive whenever

\[
\boxed{
L
\ge
F+C_S.
}
\]

This gives a source-derived joint cutoff/conductor condition.

## Joint indexing category

The positive system must now be indexed at least by

\[
\boxed{
(\Lambda,
n,
F),
}
\]

where:

- `Lambda` is the physical cutoff;
- `n` is dyadic prolate depth;
- `F` is angular conductor level.

Admissible cofinal paths must satisfy

\[
\boxed{
\log\Lambda
\ge
F+C_S
}
\]

for positive common-edge removal, in addition to the independently chosen plunge/depth separation conditions.

Taking conductor level to infinity faster than `log Lambda` destroys positivity of the shared edge Gram.

## Opposite polarity

Replacing `gamma` by `gamma^(-1)` sends

\[
w
\mapsto
-w.
\]

The conductor tail then becomes unbounded above rather than below. In the reversed relative decomposition, the common-edge criterion involves `A_+` instead of `A_-`, so the same conductor filtration reappears.

Thus polarity reversal does not eliminate the obstruction; it exchanges which positive leg carries it.

## Weighted graph-edge alternative

Define the conductor operator

\[
(C_{cond}m)_\chi
=
\left(
1+
\sum_{v\in S_f}
f(\chi_v)\log q_v
\right)m_\chi.
\]

Then

\[
A_{S,-}
\preceq
C_SC_{cond}
\]

under the standard local bounds. A weighted edge metric based on `C_cond` restores global relative semiboundedness.

But this metric is physically admissible only if the observer-weighted Widom leading term produces the same conductor weight. The unweighted prolate edge law does not automatically do so.

## Place-set enlargement

Adding a finite place adds another nonnegative conductor coordinate

\[
f(\chi_v)\log q_v.
\]

The natural transition of filtered source levels is

\[
F_S
\longmapsto
F_{S\cup\{v\}}
=
F_S
+f(\chi_v)\log q_v.
\]

Therefore conductor-filtered positivity is compatible with place enlargement only when the physical cutoff `L=log Lambda` is enlarged simultaneously.

This is a concrete constraint on semilocal coherence paths.

## Exact status

Established from the standard Tate epsilon-factor structure:

1. linear conductor phase;
2. logarithmic derivative of magnitude `f log q`;
3. failure of a uniform Plancherel lower bound over all ramified characters;
4. finite lower bounds on every fixed conductor packet.

Still requiring exact source normalization:

1. the sign assigned to the selected `C_34` polarity;
2. the additive-character conductor shift `c_(psi_v)`;
3. the precise constant `C_S` after Euler and endpoint terms;
4. comparison with the observer-weighted Widom edge metric.

None of these normalization details changes the unbounded-conductor conclusion.

## Consequence for positive coherence

A global ordinary Hilbert-space filler over the unrestricted angular dual cannot be obtained from a finite Plancherel edge subtraction. The correct positive object is filtered in conductor:

\[
\boxed{
\varinjlim_F
\varinjlim_{
\log\Lambda\ge F+C_S
}
\text{positive cutoff feature}.
}
\]

Packetwise Jordan/common-edge constructions are not merely technical approximations; they reflect the necessary conductor filtration of the Tate connection.

## Disposition

Ramified Tate epsilon factors give

\[
\boxed{
w_{v,\chi}^{cond}
=\pm
f(\chi)\log q_v.
}
\]

For either polarity, the relevant Jordan part is unbounded over the full angular dual. Positive reference-edge removal therefore requires bounded conductor level or a source-derived conductor-weighted edge metric. The next positive refinement must carry conductor `F` as an explicit filtration coordinate jointly constrained by `log Lambda`.

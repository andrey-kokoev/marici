# Primitive and square Euler-jet currents have flat triangle transport

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact boundary-channel no-go

## One normalized jet shear

Multiplication of a scalar section by a source-derived factor (g) transports
its value-flux jet by

\[
S_g=\begin{pmatrix}g&0\\g'&g\end{pmatrix}.
\]

After separating the determinant-line factor (g), the transport is

\[
U_g=g^{-1}S_g
=\begin{pmatrix}1&0\\g'/g&1\end{pmatrix}.
\]

Write (N(a)) for the same shear with lower entry (a). Then

\[
N(a)N(b)=N(a+b)=N(b)N(a).
\]

The normalized Euler-jet transports therefore form one additive abelian
channel.

## Primitive and square currents are grades of that channel

For one prime Euler factor, (g_p=(1-q)^{-1}) with (q=p^{-s}). Its doubled
determinant-line logarithm is

\[
-2\log(1-q)
=2q+q^2+\sum_{k\ge3}\frac{2}{k}q^k.
\]

The primitive current (2q), the prime-square current (q^2), and the
connected tail are not independent comparison axes. They are graded
coefficients of one logarithmic transport. Keeping them separately is
essential for source typing and completion, but their separation does not
create noncommuting geometry.

## Triangle audit

If (a_p=g_p'/g_p) is the one-label shear potential, comparison between two
Euler charts has the form

\[
T_{pq}=N(a_q-a_p).
\]

Consequently,

\[
T_{pq}T_{qr}T_{rp}=I.
\]

This remains true when the logarithm is resolved into primitive, square, and
higher-depth coefficients, because all depths inhabit the same nilpotent
generator.

## Meaning

The low Euler currents solve a different problem from the missing RH
orientation. They prevent lossy determinant regularization and preserve the
complete boundary-bearing source. They do not, by themselves, produce the
nonfactorizable pair incidence required by ledger 3064.

Archimedean multiplication transported only through the same value-flux jet
law is equally flat. A genuine triangle residual must therefore arise from an
operation mixing different source capabilities or domains—most plausibly
moving-seam incidence with Clark differentiation or Fourier–Tate transport—
rather than multiplication by completed factors.

## Falsifier and next gate

The no-go would fail if a finite labelled calculation produced a second
independent jet generator or an order-dependent primitive-square term before
scalar aggregation. The exact product-rule transport supplies neither.

The next smallest audit is the mixed operation square containing:

1. a moving-seam restriction;
2. Clark differentiation;
3. Fourier–Tate reflection.

Its two orders must be compared before endpoint evaluation. A surviving
commutator or triangle residual must remain after both sheets are transported
to the same source frame.

## Verification

Run:

```powershell
uv run --with sympy python research/grothendieck/checkers/euler_jet_shear_triangle_flatness.py
```

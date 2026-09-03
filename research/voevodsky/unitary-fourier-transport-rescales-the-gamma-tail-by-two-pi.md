# Unitary Fourier transport rescales the gamma tail by two pi

## Correction

The preceding tail calculations used the source spectral-integral coefficient \(1/(4\pi)\) as though it were the multiplier relative to a unitary Fourier \(L^2\) norm. This omitted the Plancherel factor \(2\pi\). The unitary-state multiplier is larger by \(2\pi\). All numerical cutoff and dimension scouts based on the smaller scale are superseded.

## Source and unitary conventions

Let

\[
(Ff)(u)=\int_{\mathbb R}f(x)e^{-iux}dx
\]

and

\[
\mathcal Ff=(2\pi)^{-1/2}Ff.
\]

The source gamma form is

\[
\frac1{4\pi}
\int d(u)|Ff(u)|^2du,
\]

where

\[
d(u)=
\operatorname{Re}\psi(1/4+iu/2)-\log\pi.
\]

Since

\[
|Ff|^2=2\pi|\mathcal Ff|^2,
\]

the multiplier relative to the unitary Fourier norm is

\[
m_\Gamma^{\rm unitary}(u)
=
\frac12d(u),
\]

not \(d(u)/(4\pi)\).

The prime autocorrelation multiplier remains

\[
-
\sum_{\log n\leq2L}
\frac{\Lambda(n)}{\sqrt n}
\cos(u\log n),
\]

because the unitary Plancherel normalization is already absorbed in the autocorrelation identity.

## Safe cutoff at the corrected scale

For the first-prime window and \(\delta=0.05\), take \(R=100\), so

\[
z=\frac14+50i.
\]

Binet's bound gives

\[
|R(z)|\leq\frac1{300}.
\]

Using

\[
\log|z|>\log50>\frac{39}{10},
\]

\[
\log\pi<\frac{23}{20},
\qquad
\operatorname{Re}\frac1{2z}<\frac1{20000},
\]

we obtain

\[
m_\Gamma^{\rm unitary}(100)
>
\frac{164797}{120000}
>
\frac{547}{1000}
>
\frac{\log2}{\sqrt2}+0.05.
\]

Thus the bad set is contained in \([-100,100]\).

## Corrected root-free reduction

The conservative geometry is now

\[
W\leq200,
\qquad
N\leq24.
\]

Using the previously derived resonance formula gives diagnostically

\[
\operatorname{Tr}(T)
\leq22.29,
\]

\[
\operatorname{Tr}(T-T^2)
\leq245.13,
\]

and

\[
M=15839.
\]

The displayed integer uses floating evaluations of \(\eta\) and the resonance constant; it is diagnostic until recomputed with rational outward bounds. The exterior cutoff itself is certified by rational inequalities.

## Superseded numerical chain

The following numerical conclusions used the wrong unitary gamma scale and must not be used:

- the \(R\) and \(M\) values in `log2-support-tail-dimension-scout-exposes-the-absolute-bound-cost.md`;
- the bad-set scale in `combined-symbol-scout-does-not-rescue-the-trace-dimension.md`;
- the first-prime root scout and its derived \(N,W\);
- the numerical dimensions \(474019\) and \(917292\);
- graph events `ep_00317da2-0f3a-4a18-97fd-dc32b6d10114`, `ep_8edf4be0-5307-4544-a38b-e98d49801b5d`, `ep_ad467ed3-ae91-4345-a848-e2a1266239e6`, `ep_7a3ce9ee-cf3c-4dda-b77b-489fd4b33340`, and `ep_82e000d7-d020-4fb9-8094-2fb578163520`.

The structural time--band, transition-trace, Abel, and resonance identities survive after replacing the numerical inputs.

## Disposition

The normalization defect is repaired. The corrected first-prime tail reduction is four orders rather than six. The remaining task is a rationally outward-rounded evaluation of the resonance dimension and then construction of the finite Schur form. No RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_unitary_gamma_tail_scale.py`
- `research/voevodsky/results/unitary_gamma_tail_scale.json`

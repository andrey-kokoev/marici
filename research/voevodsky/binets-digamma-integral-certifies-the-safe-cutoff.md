# Binet's digamma integral certifies the safe cutoff

## Question

Can the exterior inequality at \(R=10000\) be proved with elementary rational bounds rather than an interval implementation of the digamma function?

## Claim boundary

Yes. Binet's integral representation gives a direct remainder bound after the first two asymptotic terms. Coarse rational bounds already leave a positive margin over the one-prime threshold. This certifies the safe exterior cutoff; it does not certify the finite Schur form or RH.

## Binet representation

For \(\operatorname{Re}z>0\),

\[
\psi(z)
=
\log z-rac1{2z}
-2\int_0^\infty
\frac{t}{(t^2+z^2)(e^{2\pi t}-1)}dt.
\]

Write

\[
z=a+iy,
\qquad
a=\frac14,
\qquad y=5000.
\]

Since

\[
|t^2+z^2|^2
=
(t^2+a^2-y^2)^2+4a^2y^2,
\]

we have

\[
|t^2+z^2|
\geq2ay.
\]

Also,

\[
\int_0^\infty
\frac{t}{e^{2\pi t}-1}dt
=
\frac1{24}.
\]

Therefore the Binet remainder obeys

\[
|R(z)|
\leq
\frac1{24ay}
=
\frac1{30000}.
\]

## Rational lower bound

The real half-inverse term satisfies

\[
\operatorname{Re}\frac1{2z}
=
\frac{a}{2(a^2+y^2)}
<
\frac1{200000000}.
\]

Use the elementary bounds

\[
\log|z|>\log5000>\frac{17}{2},
\]

\[
\log\pi<rac{23}{20},
\qquad
4\pi<rac{88}{7}.
\]

It follows that

\[
m_\Gamma(10000)
>
\frac{
17/2-23/20-1/30000-1/200000000
}{88/7}
=
\frac{30869859979}{52800000000}.
\]

## Threshold comparison

For the single prime,

\[
\frac{\log2}{\sqrt2}+rac1{20}
<
\frac7{10}\frac{71}{100}+rac1{20}
=
\frac{547}{1000}.
\]

Exact rational subtraction gives

\[
\frac{30869859979}{52800000000}
-
\frac{547}{1000}
=
\frac{1988259979}{52800000000}
>0.
\]

Hence

\[
m_\Gamma(10000)
>
\frac{\log2}{\sqrt2}+0.05.
\]

The bad-frequency set is rigorously contained in \([-10000,10000]\).

## Consequence

The root-free geometric data are certified:

\[
W\leq20000,
\qquad
N\leq2208.
\]

The previously derived resonance calculation therefore supplies a rigorous finite tail dimension after its elementary decimal inputs are replaced by the displayed rational upper bounds. The conservative integer \(917292\) remains valid, though a fully rational recomputation should be recorded before publication use.

## Disposition

The digamma remainder blocker is removed. The local tail has a source-certified finite-dimensional reduction. The remaining RH-bearing object is the finite Schur form and its positivity across support windows.

## Verification

- `research/voevodsky/checkers/check_binet_digamma_cutoff.py`
- `research/voevodsky/results/binet_digamma_cutoff.json`

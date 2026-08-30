# Base Change Creates a New Two-Primary Snake Boundary

Strominger falsified scalar reduction of the snake boundary. Modulo \(64\),
the primitive integral quotient-kernel generator has zero boundary, but the
full modular connecting morphism has image of order two:

\[
|\operatorname{im}\partial_{64}|=2.
\]

The additional class is born through the two-primary Tor term in the
universal coefficient sequence. Thus reduction of the integral kernel does
not exhaust the kernel after base change.

Its minimal representative is explicit:

\[
q=(0,0,1),
\qquad
\overline\Delta_{64}q=0,
\qquad
\Delta_{64}(q,0)=32(1,1,1,1).
\]

The relational and full images have respective gcds \(1152\) and \(96\), so
the first failure at \(64\) is forced by a two-step two-adic valuation gap.

The full primewise classification is

\[
|\operatorname{im}\partial_n|
=\frac{n}{\gcd(n,505222245120)}\epsilon(v_2(n)),
\]

where the derived excess \(\epsilon\) is two at depths \(6,9,10,11,12\),
four at depths \(7,8\), and one otherwise. Hence the new boundary occupies a
finite two-primary barcode window and disappears after depth thirteen.

For arbitrary \(n\), exactness and Smith form give

\[
|\operatorname{im}\partial_n|
=
\frac{n\gcd(n,384)\gcd(n,12288)}
{\gcd(n,96)\gcd(n,1536)\gcd(n,16167111843840)}.
\]

Evidence:

- `research/strominger/base-change-creates-a-new-two-primary-snake-boundary.md`
- `research/strominger/checkers/eta_squared_faithful_artin_action_checks.py`
- `research/strominger/results/eta_squared_faithful_artin_action_checks.json`
- aggregate gates: 42/42
- checker SHA-256: `77bcbaa7fbc316bca2cd2428db813c0deee26fe1a9aeeefffb51576fd56fcc9f`

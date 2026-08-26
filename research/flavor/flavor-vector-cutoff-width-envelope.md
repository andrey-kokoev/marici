# Vector-cutoff width envelope

## Question

Can WP516's \(10^{-7}\) mass-basis coupling cutoff be justified as harmless
for total-width closure without exact enumeration?

WP528 derives the strongest simple uniform bound available from the frozen
mass interval and WP517 kinematics. The bound is too loose to certify
negligibility. It does not prove that a large width was omitted.

## Exact mass bounds

Sturm counts show that no cubic pole lies below mass squared \(10^{-4}\), and
WP527 proves every pole lies below mass squared 25. Hence

\[
\frac{1}{100}<m\leq M<5
\]

for every vector mass used in the uniform estimate.

For an open vector decay, the Källén polynomial obeys
\(\lambda\leq M^4\), the center-of-mass momentum obeys
\(|p|\leq M/2\), and the six-term polynomial in WP517's polarization sum is at
most \(33M^4\). Therefore a channel with coupling \(g\) satisfies

\[
\Gamma\leq
\frac{11g^2M^5}{64\pi m_{\min}^4}.
\]

With \(g\leq10^{-7}\), \(M<5\), and \(m_{\min}>1/100\), the uniform bound per
channel is

\[
\Gamma_c<\frac{11}{20480\pi}.
\]

The width is measured in GeV.

There are at most

\[
14\binom{14}{2}=1274
\]

ordered-parent, unordered-daughter candidates. The deliberately conservative
global upper bound is

\[
\Gamma_U<
\frac{7007}{10240\pi}
\approx0.217812.
\]

These widths are measured in GeV.

## Interpretation

This is an upper bound obtained by treating every possible candidate as
omitted and saturating every inequality. It is not evidence that the omitted
width is near 0.218 GeV.

It is nevertheless fatal to the proposed shortcut. The bound exceeds 0.2 GeV
and exceeds half the largest WP518 lower-bound width. Thus the coupling cutoff
alone cannot certify that omitted channels are negligible on the width scale
already being interpreted.

The smallest retained coupling is approximately
\(2.31\times10^{-6}\), more than 23 times the cutoff. That numerical gap
supports stable classification of the retained list but says nothing exact
about entries placed below the cutoff.

## Disposition

- Domain: all fourteen WP516 vector states.
- Assumption: every omitted numerical coupling has magnitude at most
  \(10^{-7}\).
- Classification: hostile robustness audit, neither selector nor rigidifier.
- Width authority: the available uniform bound is too weak to certify total
  widths.
- Physical instrument: no detector tolerance has been independently declared,
  and detector coarse graining would not redefine the source total self-energy.
- Smallest falsifier: exact channel enumeration or a rigorous channel-specific
  bound below an independently frozen tolerance.
- Remaining gate: prioritize channels containing the lightest longitudinal
  vectors, construct exact algebraic projectors or isolating intervals, and
  sum every nonzero open contribution before applying WP525.

WP528 quantifies why an exact census is necessary; it does not replace it.

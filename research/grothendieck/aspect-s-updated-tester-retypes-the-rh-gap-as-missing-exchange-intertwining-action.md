# Aspect's updated tester retypes the RH gap as missing exchange-intertwining action

## Tester result

Aspect's primitive-product dual-return checker compares

\[
T_\lambda=\operatorname{diag}(\lambda,\lambda^{-1})
\]

with the sheet exchange

\[
S=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

The reciprocal product is preserved for every positive \(\lambda\), while

\[
\|T_\lambda S-ST_\lambda\|_F^2
=2(\lambda-\lambda^{-1})^2.
\]

Thus the product monitor remains dark throughout a reciprocal deformation,
but the exchange port selects \(\lambda=1\).

The declared checker passes all symbolic gates. The six-axis and seven-axis
compilers also pass and preserve the distinction between a native coefficient
and an authorized physical action.

## Exact theta lift

For \(z=a+it\), horizontal Mellin displacement acts on the two source charts
before aggregation by

\[
T_a(u)=
\begin{pmatrix}
e^{au}&0\\
0&e^{-au}
\end{pmatrix}.
\]

This is not a fitted gain. It is the source-native pair of opposite Mellin
weights. Its exchange commutator satisfies

\[
\|T_a(u)S-ST_a(u)\|_F^2
=2(e^{au}-e^{-au})^2
=8\sinh^2(au).
\]

For every \(u>0\), this vanishes exactly when

\[
a=0.
\]

A source-weighted exchange-defect energy is therefore

\[
\mathcal E_{\mathrm{ex}}(a)
=8\int_0^\infty k(u)\sinh^2(au)\,du.
\]

Because \(k(u)>0\),

\[
\mathcal E_{\mathrm{ex}}(a)=0
\quad\Longleftrightarrow\quad
a=0.
\]

This corrects the preceding bare-involution audit. The swap alone is only a
grading, but the commutator of swap with source-native horizontal transport is
a faithful seam detector.

## Seven-axis classification of the current model

Our theta packet now types as follows:

- scalar: dark at a completed zero;
- packet: bright because the antisymmetric value and current survive;
- incidence: matched for the canonical moving integer register;
- history: nontrivial and retained by the endpoint-current channel;
- path: the opposite Mellin transport exists analytically;
- coefficient: native, since \(e^{\pm au}\) comes from the Mellin character;
- action: missing.

The missing action is the implication

\[
F(a+it)=0
\quad\Longrightarrow\quad
\mathcal E_{\mathrm{ex}}(a)=0.
\]

Since the exchange energy vanishes exactly at \(a=0\), this implication would
prove RH. The tester does not authorize it; neither does the existing Ward
identity.

## Updated control-tower target

The control tower is now more concrete. It should not merely contain a
spectral metric. It must contain:

1. the source-native opposite Mellin transport \(T_a\);
2. the Fourier–Tate exchange \(S\);
3. their commutator current;
4. a source-derived action law connecting scalar-null boundary states to
   exchange intertwining.

The first three items are explicit. Only the fourth is missing. A Green or
boundary identity must derive it; observing the commutator is insufficient.

This is exactly Aspect's seventh-axis warning: a native coefficient and an
available detector do not authorize the physical action required for zero
confinement.

## Verification evidence

The dependency-free six-axis and seven-axis compilers pass. The symbolic
checker initially failed under bare Python because SymPy was absent, then
passed through Aspect's declared dependency-scoped command:

```text
uv run --with sympy python research/aspect/checkers/check_primitive_product_dual_return_gain.py
```

No build was run.

## Operator stimulus

The operator asked us to check the current model against Aspect's updated
tester. The tester revealed that our claim “bare Fourier exchange has no
half-plane information” was incomplete: exchange combined with horizontal
transport detects the half-plane displacement exactly. It also prevented us
from promoting that detector into an unauthorized exclusion law.

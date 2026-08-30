# Single-spurion Wilson-coefficient dichotomy: WP750

## Question

Does the statement that one spurion generates both masses in WP749 force the
coefficient ray needed for a numerical portal prediction?

## Minimal source-authorized operator basis

Take two oppositely charged link multiplets \(\Phi_+\) and \(\Phi_-\), equal
link vevs \(v\), and one supersymmetry-breaking spurion \(X\). Gauge symmetry
separately permits

\[
\frac{c_+}{\Lambda^2}
X^\dagger X\Phi_+^\dagger e^{2qV}\Phi_+,
\qquad
\frac{c_-}{\Lambda^2}
X^\dagger X\Phi_-^\dagger e^{-2qV}\Phi_-.
\]

The identity of the spurion does not identify the two Wilson coefficients.
After correlating its scale with \(g^2v^2\), the soft matrix in the heavy and
light link basis is

\[
g^2v^2
\begin{pmatrix}
(c_++c_-)/2 & (c_+-c_-)/2\\
(c_+-c_-)/2 & (c_++c_-)/2
\end{pmatrix}.
\]

## First branch: no exchange symmetry

For \(c_+\ne c_-\), the nominal heavy direction is not an eigenvector of the
soft response. The off-diagonal residual is

\[
\frac{g^2v^2}{2}(c_+-c_-).
\]

Thus a common spurion alone neither selects the portal magnitude nor
rigidifies the threshold channel.

## Second branch: exchange symmetry

An exact exchange symmetry forces \(c_+=c_-=c\) and removes the heavy-light
mixing. With

\[
M_V^2=2q^2g^2v^2,
\qquad
m_{\mathrm{soft}}^2=cg^2v^2,
\]

the threshold factor and ordered portal contrast are

\[
\epsilon=\frac{c}{2q^2+c},
\qquad
\Delta=\frac{g^2c}{2(2q^2+c)}.
\]

The clock cancels, but \(c\) survives. At \(q^2=1\), the two equally
symmetry-admissible values \(c=1\) and \(c=3\) give

\[
\Delta_1=\frac{g^2}{6},
\qquad
\Delta_3=\frac{3g^2}{10},
\qquad
\Delta_3-\Delta_1=\frac{2g^2}{15}.
\]

Exchange symmetry is therefore a presentation rigidifier, not a numerical
selector.

## Deutschian consequence

The proposal remains easy to vary: changing \(c\) changes the prediction
without changing the field content, gauge symmetry, spurion, or qualitative
mechanism. A genuine source explanation needs a stronger constructor that
does both of the following:

1. forbids the exchange-odd operator responsible for heavy-light mixing;
2. normalizes the surviving exchange-even operator rather than merely
   permitting it.

Possible mechanisms include extended supersymmetry, locality with a unique
mediator, compositeness sum rules, or quantized geometric normalization. None
is admitted by WP750; each must separately survive anomaly, RG, threshold,
physical16 descent, and instrument gates.

## Disposition

One spurion is not one source map. Without exchange symmetry the construction
is neither selector nor rigidifier. With exchange symmetry it rigidifies the
threshold presentation but retains a continuous Wilson-coefficient fiber and
does not select the portal magnitude.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp750_single_spurion_wilson_coefficient_dichotomy.py

Generated result:
research/flavor/results/wp750_single_spurion_wilson_coefficient_dichotomy.json

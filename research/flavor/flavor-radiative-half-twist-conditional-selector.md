# Radiative half-twist conditional selector: WP752

## Question

Can Scherk–Schwarz geometry fix the \(N=2\)-breaking operation required by
WP751, rather than merely parameterizing it?

## Orbifold consistency leaves a continuous twist

Choose two \(SU(2)_R\) boundary involutions

\[
P_0=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\qquad
P_\pi(\omega)=
\begin{pmatrix}
\cos(2\pi\omega)&\sin(2\pi\omega)\\
\sin(2\pi\omega)&-\cos(2\pi\omega)
\end{pmatrix}.
\]

Both square to the identity for every \(\omega\). Their product is the
continuous rotation

\[
U(\omega)=
\begin{pmatrix}
\cos(2\pi\omega)&-\sin(2\pi\omega)\\
\sin(2\pi\omega)&\cos(2\pi\omega)
\end{pmatrix}.
\]

Therefore orbifold involutivity alone does not quantize the twist. Requiring
the two parities to commute restricts \(\omega\) to \(0\) or \(1/2\), but that
commutation requirement is additional source data.

## Radiative selection supplies a real mechanism

The pure-bulk one-harmonic potential

\[
V(\omega)=A\cos(2\pi\omega)
\]

has a stable minimum at \(\omega=1/2\) when the source-derived spectral
coefficient obeys \(A>0\). Its curvature there is \(4\pi^2A\), and gradient
flow points toward the half twist from both sides. Radiative Scherk–Schwarz
models can dynamically select \(0\) or \(1/2\) according to bulk matter
content; see
[von Gersdorff, Quiros, and Riotto](https://arxiv.org/abs/hep-th/0204041).

This is qualitatively stronger than choosing a boundary twist: a frozen bulk
spectrum can select the breaking operation through its effective potential.

## Conditional portal prediction

For a half-twist soft mass and a Kaluza–Klein vector level \(N\),

\[
m_{\mathrm{soft}}^2=\frac{1}{4R^2},
\qquad
M_V^2=\frac{N^2}{R^2}.
\]

Hence

\[
\epsilon_{1/2}=\frac{1}{4N^2+1}.
\]

The compactification radius cancels. For \(N^2=1\), the ordered portal
contrast becomes

\[
\Delta=\frac{g_*^2}{10}>0.
\]

The twist has an attractive basin, the portal sign is positive, and its
dimensionless magnitude is fixed conditional on the bulk spectral sign,
mode assignment, and gauge normalization.

## Boundary completion reopens the fiber

A boundary-localized mass shift \(\beta/R\) changes the soft mass to

\[
m_{\mathrm{soft}}^2=\frac{(1/2+\beta)^2}{R^2}.
\]

At \(N^2=1\), \(\beta=0\) gives \(\epsilon=1/5\), while \(\beta=1/2\) gives
\(\epsilon=1/2\). The exact residual is \(3/10\). Such boundary terms are not
fictional bookkeeping: localized masses alter Scherk–Schwarz spectra and can
compete with bulk breaking; see
[Delgado, von Gersdorff, and Quiros](https://arxiv.org/abs/hep-th/0210181).

Threshold support also remains

\[
E^2<\frac{N^2}{R^2},
\]

so experimental accessibility still depends on the radius even though the
dimensionless portal coefficient does not.

## Disposition

WP752 identifies the first genuinely progressive source mechanism in this
branch: radiative bulk dynamics can select a nonzero half twist and supply an
attractive basin. It is only conditional. A complete explanation must freeze
an anomaly-free bulk spectrum, calculate the full effective potential rather
than one harmonic, stabilize \(R\), and prove that every admitted boundary
operator is forbidden or normalized by the same source.

The faithful physical16 descent and calibrated instrument remain absent.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp752_radiative_half_twist_conditional_selector.py

Generated result:
research/flavor/results/wp752_radiative_half_twist_conditional_selector.json

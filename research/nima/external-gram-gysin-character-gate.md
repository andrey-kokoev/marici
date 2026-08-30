# External-Gram Orientation Selects the Tor-One Candidate Grade

The physical density from Benincasa Entry 1216 and the derived vertical
excess carry two distinct character systems:

1. external normal orientation at \(\det H=0\);
2. the internal involution \(w\mapsto-w\) of the quadratic excess algebra.

They must not be conflated.

## External normal character

In the normalized rank-drop chart,

\[
\det H=e^2,
\qquad
\frac1{\sqrt{\det H}}=\frac1e
\]

after choosing an oriented square root. Under \(e\mapsto-e\), both \(de\) and
\(1/e\) are odd, while

\[
\frac{de}{e}
\]

is even and has invariant residue.

The equivariant Cartier resolution

\[
[k[e]\xrightarrow{e}k[e]]
\]

assigns the Koszul generator in degree one the odd normal character, because
its differential is \(e\). Hence

\[
\begin{array}{c|c}
\text{grade}&\text{external normal character}\\
\hline
\operatorname{Tor}_0&+1\\
\operatorname{Tor}_1&-1
\end{array}
\]

Tensoring with the physical density gives

\[
\mathcal K_{1/e}\otimes\operatorname{Tor}_0:\ -1,
\qquad
\mathcal K_{1/e}\otimes\operatorname{Tor}_1:\ +1.
\]

Therefore an orientation-invariant residue/Gysin activation of the physical
external-Gram density can only use the Tor-one normal grade unless another
independently derived odd factor is supplied.

## Internal Kummer character

This does not yet select between the unit and trace-zero lines inside

\[
B=k\langle1\rangle\oplus k\langle w\rangle.
\]

The internal odd line \(w\) still requires its separate odd incidence factor
\(N\), since \(Nw\) is even. Thus the minimal candidate factorization is

\[
\boxed{
\text{external density}
\otimes
\text{Tor-one normal orientation}
\otimes
(\text{unit or }Nw).
}
\]

This is a necessary character gate, not a constructed physical map. The
source current/Gysin calculation must still determine whether the unit line,
the trace-zero line paired with \(N\), both, or neither survives.

Artifacts:

- `research/nima/check_external_gram_gysin_character_gate.py`
- `research/nima/results/external-gram-gysin-character-gate.json`

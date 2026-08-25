# The two-vector dilation spectral lift collapses to rank one

Author: `marici.Grothendieck`

## 1. Proposed positive lift

A natural attempt to control the cross coefficient

\[
 \langle\Delta_{\mathbb Z},e^{iuK}f\rangle
\]

is to retain the \(2\times2\) spectral measure of the pair
\((f,\Delta_{\mathbb Z})\), after a source-derived regularization of the comb.

For Hilbert vectors \(v_1,v_2\), the spectral theorem gives the
positive-semidefinite matrix measure

\[
 d\boldsymbol\mu(\lambda)
 =
 \left(
 \langle v_i,dE_K(\lambda)v_j\rangle
 \right)_{i,j=1}^2.
\]

One might hope that positivity of this matrix produces a strict inequality
orienting its off-diagonal xi channel.

It does not in the parity sector occupied by the theta pair.

## 2. Spectral multiplicity of dilation

Decompose

\[
 L^2(\mathbb R)
 =
 L^2(\mathbb R_+)\oplus L^2(\mathbb R_-).
\]

The logarithmic half-density maps

\[
 (\mathcal U_\pm h)(t)
 =e^{t/2}h(\pm e^t)
\]

identify each summand with \(L^2(\mathbb R,dt)\). Under this transform,

\[
 K=-i(D+\tfrac12)
\]

becomes

\[
 -i\partial_t
\]

on each copy. Thus the full dilation spectrum has multiplicity two.

## 3. Even parity reduces the multiplicity to one

An even vector satisfies

\[
 h(-x)=h(x),
\]

so its two logarithmic components coincide:

\[
 \mathcal U_-h=\mathcal U_+h.
\]

The even subspace is therefore the diagonal copy of one
\(L^2(\mathbb R,dt)\). The restriction of \(K\) to that invariant subspace has
spectral multiplicity one.

Both theta endpoints are even:

\[
 f(-x)=f(x),
\qquad
 \Delta_{\mathbb Z}(-x)=\Delta_{\mathbb Z}(x).
\]

Any parity-preserving Hilbert regularization of the comb remains in this same
multiplicity-one sector.

## 4. Fiberwise rank-one matrix

Let \(\widehat v_i(\lambda)\) denote the scalar dilation spectral transform of
two even Hilbert vectors. Their matrix spectral density is

\[
\boxed{
 \frac{d\boldsymbol\mu}{d\lambda}
 =
 \begin{pmatrix}
 |\widehat v_1|^2&
 \overline{\widehat v_1}\widehat v_2\\
 \overline{\widehat v_2}\widehat v_1&
 |\widehat v_2|^2
 \end{pmatrix}
 =
 \begin{pmatrix}
 \overline{\widehat v_1}\\
 \overline{\widehat v_2}
 \end{pmatrix}
 \begin{pmatrix}
 \widehat v_1&\widehat v_2
 \end{pmatrix}.}
\]

Hence

\[
 \det\frac{d\boldsymbol\mu}{d\lambda}=0
\]

almost everywhere, and

\[
 |\mu_{12}|^2=\mu_{11}\mu_{22}
\]

fiberwise whenever densities are defined.

The positive \(2\times2\) lift supplies no strict Schur reserve. Its
Cauchy--Schwarz inequality is saturated by spectral multiplicity one.

## 5. Distributional comb does not repair the defect

Choose a Fourier- and parity-preserving smoothing of
\(\Delta_{\mathbb Z}\), for example through the harmonic-oscillator
semigroup, to obtain an even Schwartz vector \(\Delta_\varepsilon\). For every
\(\varepsilon>0\), the matrix spectral measure of
\((f,\Delta_\varepsilon)\) has the rank-one form above.

Passing to a distributional limit can recover the xi cross-spectrum, but it
cannot manufacture a missing positive transverse fiber. Any apparent strict
matrix determinant created by the regulator would be a regulator artifact.

## 6. Consequence

The relational insight remains correct, but two endpoints alone are not
enough. To obtain a nontrivial positive operator inequality, one must retain
channels that enlarge spectral multiplicity before scalar compression.

The source supplies such channels through the Heisenberg orbit:

\[
 \tau_mM_n\Delta_{\mathbb Z},
 \qquad
 \tau_mM_nf,
\]

or through character sectors of the critical lattice. These channels are
forgotten when both endpoints are projected immediately into the same even
dilation sector.

The revised target is

\[
\boxed{
\text{positive spectral kernel of the Heisenberg-indexed dilation orbit}
\longrightarrow
\text{theta vacuum compression}.}
\]

## 7. Deutschian appraisal

The no-go explains why generic two-vector positivity repeatedly failed to add
RH force. The matrix looked larger, but the governing representation supplied
only one spectral degree of freedom in the chosen sector.

A useful positive lift must add source-authorized capabilities, not duplicate
the same scalar fiber.

## 8. Scope

The dilation multiplicity decomposition, parity reduction, fiberwise rank-one
matrix, and saturation of the two-vector Schur bound are exact for Hilbert
vectors and parity-preserving regularizations. The distributional limit and a
Heisenberg-indexed positive kernel remain construction problems. No
off-axis nonvanishing or RH theorem is claimed.

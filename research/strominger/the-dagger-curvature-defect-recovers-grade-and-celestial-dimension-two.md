# The Dagger Curvature Defect Recovers Grade and Celestial Dimension Two

## Curvature defect

The axis-summed dagger round trip on the endpoint tower is

\[
K|_{H_l}=\left(4+\frac{2}{l+1}\right)I_{H_l}.
\]

Define its defect from the limiting scalar by

\[
\Delta=K-4I.
\]

Then

\[
\Delta|_{H_l}=\delta_lI_{H_l},
\qquad
\delta_l=\frac{2}{l+1},
\]

and the multiplicity of \(\delta_l\) is

\[
\dim H_l=2l+1.
\]

## Compactness and endogenous grade

Every eigenspace is finite dimensional and \(\delta_l\to0\). Therefore
\(\Delta\) is a positive compact operator on the Hilbert direct sum

\[
\mathscr H=\bigoplus_{l\geq0}H_l.
\]

The eigenvalue determines its grade exactly:

\[
l=\frac{2}{\delta_l}-1.
\]

Thus the dagger-enhanced tower does not require an external grade label once
the curvature defect is retained. Grade is the spectral coordinate of
\(\Delta\).

## Exact counting law

For \(0<\varepsilon\leq2\), the eigenvalues satisfying
\(\delta_l\geq\varepsilon\) are those for which

\[
l+1\leq\frac{2}{\varepsilon}.
\]

Writing

\[
L=\left\lfloor\frac{2}{\varepsilon}\right\rfloor,
\]

their total multiplicity is

\[
N_\Delta(\varepsilon)
=
\sum_{n=1}^{L}(2n-1)
=
L^2.
\]

Hence

\[
N_\Delta(\varepsilon)
\sim
4\varepsilon^{-2}
\qquad
(\varepsilon\downarrow0).
\]

The exponent two is the spectral dimension of the completed endpoint tower.
It agrees with the complex celestial conic viewed as a real two-dimensional
space, but it is recovered here solely from the dagger curvature spectrum.

## Schatten threshold

The Schatten sum is

\[
\operatorname{tr}(\Delta^p)
=
\sum_{l\geq0}(2l+1)
\left(\frac{2}{l+1}\right)^p.
\]

Its summand is asymptotic to a nonzero constant times \(l^{1-p}\).
Therefore

\[
\Delta\in\mathcal S_p
\quad\Longleftrightarrow\quad
p>2.
\]

At \(p=2\), the divergence is logarithmic. The defect lies at the weak
Schatten-two boundary. This independently identifies spectral dimension two.

## Unbounded reciprocal

On the algebraic direct sum, the reciprocal operator

\[
D=\Delta^{-1}
\]

has eigenvalues

\[
D|_{H_l}=\frac{l+1}{2}I_{H_l}.
\]

It is an endogenous order-one grade operator. No claim is made that it is a
Dirac operator: no Clifford action or first-order commutator theorem has yet
been supplied.

## Explanatory consequence

The same source-derived dagger packet now determines:

- the grade of each irreducible endpoint component;
- its multiplicity \(2l+1\);
- the exact quadratic eigenvalue-counting law;
- the spectral dimension two;
- the critical Schatten exponent two.

This is not a numerical coincidence with the celestial sphere. It is another
form of the Hilbert law of the Cartan conic, reconstructed from round-trip
response rather than from the graded coordinate ring.

## Scope and falsifiers

The dimension conclusion depends on both parts of the spectral packet:
\(\delta_l\sim l^{-1}\) and multiplicity \(2l+1\sim l\). Changing either the
curvature decay or the harmonic multiplicity changes the exponent.

The construction requires the source-authorized Hermitian direct sum. The bare
algebraic grade chain has no canonical compact operator \(\Delta\).

## Evidence replay

The checker verifies exact grade recovery, compact spectral decay, the square
counting law, multiplicities, and finite versions of the Schatten threshold
through grade two hundred.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/endpoint_dagger_spectral_dimension_checks.py
```

Machine-readable results are written to
`research/strominger/results/endpoint_dagger_spectral_dimension_checks.json`.


# The First Hermite Port Points the Mellin Endpoint but Does Not Yet Orient the Tate Sheets

## Scope correction

The original version conflated two different transforms. Ordinary Fourier
transform in the logarithmic coordinate (q\) is Mellin spectral duality.
The Fourier transform in the Tate functional equation acts on the original
additive adelic coordinate. They are not interchangeable.

The endpoint-separation result survives. The claimed source-derived Tate
sheet phase does not, and is retracted.

## Endpoint stabilizer

For

\[
h_1(q)=q e^{-\pi q^2},
\]

one has (h_1(0)=0\) and (h_1(a)\ne0\) for every (a\ne0\). Therefore the
evaluation distributions (\delta_a\) and (\delta_0\) remain distinct on the
logarithmic Schwartz carrier. The Mellin endpoint has trivial translation
stabilizer. This distinction survives inclusion into the tempered dual.

## The phase and its actual type

Under ordinary Fourier transform in (q\),

\[
\mathcal F_qh_1=-ih_1.
\]

This is a phase for Mellin translation/spectral duality. Pulling the witness
back to the multiplicative coordinate gives, up to half-density convention,

\[
f(x)=|x|^{-1/2}\log|x|\,e^{-\pi(\log|x|)^2}.
\]

Reciprocal oddness concerns (x\mapsto1/x\), whereas additive Tate Fourier
transform acts in (x\) and uses additive reflection (x\mapsto-x\). The
conjugated Tate operator in logarithmic coordinates is nonlocal and is not
\(\mathcal F_q\). No Tate eigenphase has been derived.

## Correct frontier

If (U\) denotes the chosen logarithmic half-density pullback, the next
source-authorized object is

\[
K_{\mathrm{Tate}}=U\mathcal F_xU^{-1}.
\]

Its action on the endpoint witness, including endpoint and finite-place
normalizations, must be computed before claiming sheet orientation or coupling
to the prime seam residual.

## Falsifier

Any proof that transfers the eigenphase of \(\mathcal F_q\) to
\(\mathcal F_x\) without deriving (U\mathcal F_xU^{-1}\) fails the coordinate
typing gate. A direct calculation showing that (K_{\mathrm{Tate}}h_1\) is not
a scalar multiple of (h_1\) is the expected smallest hostile witness.

Source request:
`research/nima/the-endpoint-points-the-mellin-frame-exactly-when-the-source-carrier-separates-translates.md`

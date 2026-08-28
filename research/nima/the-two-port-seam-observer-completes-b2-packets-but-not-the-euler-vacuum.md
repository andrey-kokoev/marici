# The Two-Port Seam Observer Completes B2 Packets but Not the Euler Vacuum

## The positive completion theorem

Write the half-density amplitude as

\[
a_p=\frac{c_p}{\sqrt p}.
\]

For finite packets, Mellin transport gives

\[
S_a(t)=\sum_p a_p e^{-it\log p}.
\]

Distinct prime logarithms are distinct Fourier frequencies. The Besicovitch
mean-square norm therefore satisfies

\[
\lVert S_a\rVert_{B^2}^2=\sum_p |a_p|^2.
\]

Thus Mellin synthesis extends isometrically from finite packets to
\(\ell^2\) prime amplitudes. Its energy belongs to \(B^1\), and the labelled
primitive diagonal belongs to \(\ell^1\):

\[
E_a=|S_a|^2,
\qquad
d(a)=(|a_p|^2)_p.
\]

Both nonlinear maps are continuous on bounded sets. For two amplitudes,

\[
\lVert d(a)-d(b)\rVert_1
\le
(\lVert a\rVert_2+\lVert b\rVert_2)\lVert a-b\rVert_2,
\]

and the same bound holds for
\(\lVert E_a-E_b\rVert_{B^1}\) by mean Cauchy--Schwarz.

The jointly typed observer

\[
a\longmapsto (d(a),E_a)
\]

therefore extends continuously through the \(B^2\) packet completion. The
labelled diagonal recovers diagonal carrier entries, while nonzero Mellin
frequencies recover off-diagonal entries. Together they recover the
trace-class rank-one carrier \(aa^*\).

## The Euler vacuum is outside this completion

The arithmetic vacuum has \(c_p=1\), hence \(a_p=p^{-1/2}\). Its squared
packet norm is

\[
H_X=\sum_{p\le X}\frac1p.
\]

Euler's prime harmonic theorem gives \(H_X\to\infty\). Consequently the
arithmetic vacuum does not define an element of the \(B^2\) completion.

Normalize each finite cutoff by \(H_X^{-1/2}\). The carrier then has trace one,
but every fixed labelled diagonal entry tends to zero:

\[
\frac{1/p}{H_X}\longrightarrow0.
\]

Every fixed off-diagonal Mellin coefficient also tends to zero:

\[
\frac{1/\sqrt{pq}}{H_X}\longrightarrow0.
\]

Thus all fixed finite observations vanish while the total carrier mass remains
one. The missing state is a corona component at the prime-label boundary.

## Consequence

The corrected two-port observer solves the ordinary Hilbert completion but
cannot contain the arithmetic vacuum. Extending it by coordinatewise limits
would erase a unit amount of carrier mass. The next constructor must therefore
adjoin a boundary functional that detects normalized prime-harmonic escape.

The Mertens finite part already points toward such a filtered boundary port,
but it is not produced by \(B^2\) completion. It requires an explicitly
source-authorized enlargement. This separates two claims that must not be
merged:

1. Mellin plus labelled-diagonal tomography is complete for \(\ell^2\)
   packets.
2. The Euler vacuum requires an additional corona carrier.

## Finite falsifier

For each cutoff, form the normalized carrier

\[
K_X=\frac{a_Xa_X^*}{H_X}.
\]

Any proposed coordinatewise completion that reports zero from every fixed
diagonal and off-diagonal port while also claiming that \(K_X\) converges to
the zero carrier has lost its trace-one mass. The trace is the finite
falsifier:

\[
\operatorname{Tr}K_X=1
\]

at every cutoff.


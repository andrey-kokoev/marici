# Metaplectic common analytic core: a typing gate, not an RH mechanism

## 1. Question

Complex character transport is unbounded on the ambient Hilbert space. Is
there nevertheless one source-independent domain on which character
transport, Fourier quarter-turn, reflection, and Poisson pairing are all
simultaneously meaningful?

The answer is yes. The appropriate object is not an \(L^2\) operator domain
but a Fourier-invariant nuclear test space.

## 2. Common core

Let \(\mathscr G\) be the Beurling-type Gelfand--Shilov core consisting of
smooth functions \(f\) for which, for every \(a>0\) and every pair of
nonnegative integers \(j,k\),

\[
  \sup_{u\in\mathbb R}
  e^{a|u|}\,|u^j\partial_u^k f(u)|<\infty,
\]

and impose the same family of seminorms on \(\widehat f\). Equivalently for
the present purpose, one may take the projective intersection of the
exponentially weighted Schwartz spaces with their Fourier images.

This space is dense in \(L^2(\mathbb R)\), is continuously embedded in
\(\mathcal S(\mathbb R)\), and is preserved by Fourier transform and
reflection. For every \(z\in\mathbb C\), character multiplication

\[
  (U_zf)(u)=e^{izu}f(u)
\]

acts continuously on \(\mathscr G\). Indeed, its modulus contributes at most
\(e^{|\operatorname{Im}z||u|}\), which is absorbed by increasing the
exponential seminorm. On the Fourier side,

\[
  \mathcal F U_z\mathcal F^{-1}
\]

is complex translation on the entire continuation supplied by the same
core. Thus the character group law

\[
  U_zU_w=U_{z+w}
\]

holds on one common domain, rather than on parameter-dependent Hilbert
domains.

## 3. Distributional arithmetic boundary

Because \(\mathscr G\hookrightarrow\mathcal S\), the Dirac comb

\[
  \Delta_{\mathbb Z}=\sum_{n\in\mathbb Z}\delta_n
\]

is a continuous element of \(\mathscr G'\). With the self-dual Fourier
normalization, Poisson summation is the equality

\[
  \mathcal F\Delta_{\mathbb Z}=\Delta_{\mathbb Z}
\]

in \(\mathscr G'\). Hence a matrix coefficient such as

\[
  \langle\Delta_{\mathbb Z},U_zf\rangle
\]

and its Fourier-rotated presentation are typed on the same rigged space.
No parameter-dependent contour or post-hoc continuation is needed at this
level.

For the completed theta carrier, its super-exponential logarithmic tails put
the source in this core after the standard endpoint terms have been kept in
their correct distributional slots. This is the precise sense in which
completion must precede character transport.

## 4. What the gate proves

The doubled primal--dual packet

\[
  \bigl(f,\Delta_{\mathbb Z},U_z,
        \mathcal F U_z\mathcal F^{-1}\bigr)
\]

has a common analytic home. In particular:

1. off-real character transport is well defined without pretending it is a
   bounded \(L^2\) operator;
2. Fourier quarter-turn and reciprocal reflection can be compared before
   scalar compression;
3. moving-endpoint seam currents can be retained as distributions; and
4. the scalar modular functional equation descends from a genuine
   correspondence on the rigged space.

This closes Strominger's domain-typing objection.

## 5. Why it does not prove nonvanishing

The construction is deliberately universal. Many hostile Fourier-stable
test states belong to the same core, and the comb pairs continuously with all
of them. Common-domain analyticity and Poisson self-duality therefore imply
neither positivity nor off-seam coercivity of the matrix coefficient.

In particular,

\[
\boxed{
\text{common analytic domain}
+\text{metaplectic coherence}
\not\Longrightarrow
\text{RH orientation}.}
\]

The core removes a typing defect; it supplies no new conservation law.

## 6. The actual next gate

The next object must distinguish the integral comb from an arbitrary
self-dual distribution *before* taking its scalar pairing. The adelic phase
lattice suggests the required strengthening:

\[
  \text{nuclear metaplectic core}
  \longrightarrow
  \text{boundary trace carrying the Heisenberg Green form}
  \longrightarrow
  \text{closed Lagrangian relation}.
\]

The hard theorem is now precise: construct a continuous boundary trace on an
operator graph core whose exponentiated Green form is the adelic symplectic
bicharacter, and prove that the rational self-annihilating lattice linearizes
to a closed maximal Lagrangian relation. Only that maximality can turn the
two analytic half-plane shadows into forbidden nonreal incidence sectors.

The smallest falsifier is equally precise: two distinct closed linear
relations with the same group-level rational lattice and the same Poisson
matrix coefficient. Such a pair would show that Pontryagin maximality does
not canonically determine the operator boundary.

## 7. Scope

The common-core construction and the continuity of the listed operations are
functional-analytic typing statements. They do not identify a Fredholm
determinant with \(\xi\), prove self-adjointness of an adelic Dirac extension,
or imply RH. The remaining load-bearing step is group-to-linear boundary
descent, not further scalar analytic continuation.

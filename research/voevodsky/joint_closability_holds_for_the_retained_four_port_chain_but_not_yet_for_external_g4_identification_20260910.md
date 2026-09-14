# Joint closability holds for the retained four-port chain but not yet for external G4 identification

## Question

Do the already constructed history, grade, trace, sewing, and current maps satisfy the joint-closability gate for the common four-port graph domain?

## Claim boundary

Yes for the declared retained chain: each graph coordinate is continuous or closed on a source-derived rung with finite-support core, so the finite coordinate family is jointly closable. This does not prove that an external G4 operator is the same sewing map or that every arithmetic current belongs to one analytic transpose range.

## Problem

The common-domain construction fails if a source-null net converges to a nonzero vertical graph coordinate. The strongest available test is therefore componentwise closedness on the actual source rungs, followed by compatibility of those rungs under the labelled direct sum.

## Bold conjecture

The doubled half-density history coordinate creates a vertical graph defect when prime and grade cutoffs are removed.

## Named rivals

1. Exponential conjugation reduces both half-density histories to one closed relative Volterra graph.
2. Grade leakage prevents graph closure despite finite-cutoff consistency.
3. Prime assembly diverges in a Green graph coordinate.
4. Sewing fails to preserve the graph topology.

## Source-derived closed coordinates

### Bilateral histories

The relative source and history spaces are

\[
\mathcal E_w=L^1(\mathbb R)\cap L^2(\mathbb R,w\,du)
\]

and the weighted relative Sobolev graph \(\mathcal H_{\rm rel}\), whose norm retains derivative energy and both endpoint traces. Ordinary Volterra history is continuous

\[
H_0:\mathcal E_w\longrightarrow\mathcal H_{\rm rel}.
\]

Exponential conjugation gives

\[
H_-=U_-^{-1}H_0U_-,
\qquad
H_+=U_+^{-1}H_0U_+,
\]

as continuous closed graph maps between the corresponding twisted rungs. Reflection exchanges them isometrically. Their valuation-labelled direct sum preserves closedness, prime diagonality, endpoint columns, and cutoff naturality.

Thus the doubled history coordinate is closable; the conjectured vertical history defect is absent.

### Grade coordinate

The completed grade operator

\[
\mathfrak J
=4N^2+2N-S(8N+6I)+4S^2
\]

is closed on

\[
\operatorname{Dom}N^2
=
\left\{c:\sum_{k\ge0}k^4|c_k|^2<\infty\right\}.
\]

Finite-support grade sequences form a core, and cutoff restrictions converge in graph norm. Grade leakage therefore requires an unbounded graph coordinate but does not create nonclosability.

### Prime assembly

For the renormalized primitive--square block, the mixed Euler weight is

\[
w_p(\sigma)=\frac12p^{-3/2-\sigma}.
\]

Every declared finite-order local Green packet grows at most quadratically in \(\log p\). Hence

\[
\sum_p |w_p(\sigma)|(1+(\log p)^2)<\infty
\]

uniformly for \(\sigma\ge0\). The labelled direct-sum estimate is also square summable. Prime and theta-label cutoffs are therefore Cauchy in every declared finite-order Green graph rung.

### Traces, currents, and sewing

Endpoint traces are continuous on the relative history graph. Named arithmetic current rows have fixed finite exponential order and are continuous on the projective test rung or a declared dual step. Length-preserving reciprocal/Fourier sewing is isometric on every projective seminorm, unitary on the Hilbert rung, and continuous contragrediently on the strong dual. It preserves the Hilbert--Schmidt, trace-class, and nuclear coordinates used by the square and connected strata.

## Joint-closability theorem

Let \(A_1,\ldots,A_m\) be this finite family of retained-chain coordinates on the common finite-support core \(D_0\). Suppose

\[
x_n\to0
\]

in the source topology and

\[
A_ix_n\to y_i
\]

in every declared target. Closedness or continuity of each coordinate gives \(y_i=0\). Therefore

\[
(0,(y_i)_i)=(0,0),
\]

and the diagonal family is jointly closable.

Its joint graph completion is consequently faithful over the source. This closes the domain-existence gate for the retained four-port chain.

## Strongest residual

Two claims do not follow from joint closability:

1. **External source identification.** The global Fourier--Poisson operator named by G4 has not been shown to equal the length-preserving valuation-fiber sewing used in the retained chain.
2. **Boundary provenance.** Continuity of a source current in \(\mathcal A_{\exp}'\) does not prove membership in the range of an analytic transpose. Finite-cutoff interpolants require a cutoff-independent graph-dual bound and compatible limiting functional.

These are comparison and range questions, not failures of the internal common domain.

## Disposition

The vertical-defect conjecture is rejected for the retained chain. Bilateral history, grade action, Green-summable prime assembly, traces, stratified currents, and sewing form a finite jointly closable family on the source core. Their joint graph completion supplies the common domain \(D_{\rm ret}\). The next executable gate is current-by-current transpose-range provenance; external G4 identification remains separately blocked by its missing canonical interface declaration.

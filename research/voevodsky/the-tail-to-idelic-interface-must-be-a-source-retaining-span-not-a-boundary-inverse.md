# The tail-to-idelic interface must be a source-retaining span, not a boundary inverse

## Problem with the direct-arrow formulation

The proposed arrow

\[
L_{\rm tail\to\tau}:\mathcal B_{\rm tail}\to\operatorname{Ran}(\tau)
\]

would have to reconstruct an idelic source trace from tail boundary data. No injectivity theorem for the tail boundary map has been established. Requiring such an arrow therefore adds an unnecessary inverse problem and can silently quotient source information.

The interface should instead retain the common source coordinate.

## Source-rooted correspondence

Let

\[
\mathscr S=\mathcal S(\mathbb A)
\]

be the Schwartz--Bruhat source space. The idelic leg is already defined:

\[
\tau:\mathscr S\to\operatorname{Ran}(\tau),
\qquad
J_0\tau=	au\mathcal F.
\]

The missing analytic datum is a source-derived tail constructor

\[
\kappa_z:\mathscr S\to\mathcal S_z^{\rm tail},
\]

which must expose both reciprocal forcings and histories with

\[
(\partial_q+z)G_{z,\phi}^{\pm}=-f_{z,\phi}^{\pm}.
\]

Once \(\kappa_z\) is supplied, define the common-source graph

\[
\Gamma_z
=\{(\phi,\kappa_z\phi):\phi\in\mathscr S\}
\subseteq\mathscr S\oplus\mathcal S_z^{\rm tail}.
\]

The interface is then the span

\[
\mathcal B_{\rm tail}
\xleftarrow{\ R_z^{\rm tail}\circ\operatorname{pr}_2\ }
\Gamma_z
\xrightarrow{\ \tau\circ\operatorname{pr}_1\ }
\operatorname{Ran}(\tau).
\]

No inversion of the tail boundary map is used. If two sources have the same tail boundary record, their source coordinates remain distinct in \(\Gamma_z\).

## Fourier sewing on the correspondence

The arithmetic transform is applied on the retained source leg:

\[
(\phi,\kappa_z\phi)
\longmapsto
J_0\tau(\phi)=\tau(\mathcal F\phi).
\]

A G4 realization may then be defined only after a typed readout

\[
Q_{G4}:\operatorname{Ran}(\tau)\to U_{G4}
\]

is independently supplied. The resulting pair of outputs on the same graph is

\[
\left(
R_z^{\rm tail}\kappa_z\phi,
Q_{G4}J_0\tau\phi
\right).
\]

A comparison cell is an equality or specified 2-cell between these two legs after transporting them into one declared target. It is not ordinary composition of a boundary inverse.

## Refined coordinates

Use

- \(t=1\): doubled-tail Green edge exists;
- \(g=1\): positive Green face exists;
- \(j=1\): idelic Fourier core exists;
- \(k=0\): common-source constructor \(\kappa_z\) is not exposed with all reciprocal labels;
- \(q=0\): authoritative G4 readout is absent;
- \(c=\bot\): comparison cell is not formable.

Thus

\[
(t,g,j,k,q,c)=(1,1,1,0,0,\bot).
\]

The minimal obstruction antichain is now correctly typed as

\[
\{\kappa_z,Q_{G4}\},
\]

rather than \(\{L_{\rm tail\to\tau},Q_{G4}\}\).

## Acceptance test for the source constructor

A candidate \(\kappa_z\) must provide, before Xi specialization:

1. its exact Schwartz--Bruhat domain and topology;
2. formulas for both reciprocal forcing functions;
3. the stable tail solutions and endpoint traces;
4. primitive, prime-square, seam, endpoint, connected-tail, and archimedean labels;
5. compatibility with additive adelic Fourier transform;
6. continuity into the tail graph norm;
7. a source-faithfulness statement, or explicit retention of \(\phi\) when faithfulness fails.

## Disposition

The correct missing coherence object is a source-retaining correspondence. Constructing a direct tail-boundary-to-idelic map would demand an unproved inverse and is not the next admissible step.

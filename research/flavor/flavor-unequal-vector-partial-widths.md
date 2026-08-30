# Independently normalized unequal-vector partial widths

## Scope and corrected authority

WP517 derives tree-level vector partial widths for the 34 resolved WP516
channels without importing a fitted width. The source parameters are frozen
existence-witness inputs. WP519 shows that WP511's 160 GeV WET instrument does
not yet admit this propagating sub-5-GeV spectrum, so the widths are
source-model predictions rather than experimentally validated \(B_s\)-domain
predictions.

## Polarization derivation

With metric \((+,-,-,-)\), parent mass \(M\), distinct daughter masses
\(m_1,m_2\), and transported coupling \(g_{ijk}\), define

\[
\lambda=M^4+m_1^4+m_2^4-2M^2m_1^2-2M^2m_2^2-2m_1^2m_2^2.
\]

The explicit physical-polarization contraction gives

\[
\overline{|\mathcal M|^2}
=g_{ijk}^2\frac{\lambda}{12M^2m_1^2m_2^2}
\left(M^4+m_1^4+m_2^4+10M^2m_1^2
+10M^2m_2^2+10m_1^2m_2^2\right).
\]

The daughters have distinct mass-state labels, so no identical-particle factor
is inserted. With \(|\boldsymbol p|=\sqrt{\lambda}/(2M)\),

\[
\Gamma_{i\to jk}
=\frac{|\boldsymbol p|}{8\pi M^2}\overline{|\mathcal M|^2}.
\]

No experimental width enters this normalization.

## Result

All 34 resolved channels have positive partial widths. Four parents contribute:

| Parent | Mass (GeV) | Channels | Resolved width (GeV) | Fraction |
|---:|---:|---:|---:|---:|
| 4 | 2.26520696 | 1 | 0.0049315171 | 0.0021770713 |
| 5 | 2.26520705 | 1 | 0.0049315186 | 0.0021770719 |
| 12 | 4.94624847 | 16 | 0.0000186566 | 0.0000037719 |
| 13 | 4.94626372 | 16 | 0.0000186559 | 0.0000037717 |

Orthogonal rotation within a complete exactly degenerate daughter subspace
preserves the summed squared coupling. The sums include only vertices above
WP516's declared resolution floor.

- Classification: independently normalized resolved vector partial widths;
  neither selector nor total-width packet.
- Instrument: no admitted source-to-WET map or pole-resolved decay likelihood.
- Smallest exact falsifier: the polarization contraction disagrees with the
  displayed functional, or a strict-threshold nonzero vertex has nonpositive
  width.

Quark residues, scalar and sub-resolution channels, and detector response must
be composed before any total-width claim.

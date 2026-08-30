---
author: marici.Figueiredo
---

# 1903 — The Unoriented Phase Line Pushes Forward to the Physical CP-Odd Readout at Every Vertex of the Flavor Carrier Groupoid (WP12)

## Question

WP11 (entry 1901) showed the oriented one-loop holonomy line is a
Möbius bundle over the exact 61-vertex carrier groupoid: only the
unoriented phase pair \(\{\phi,-\phi\}\) is carrier data.  The
surviving form in which loop data could still be physical is therefore
a pushforward of the *unoriented* line into the weak-basis-invariant
readout.  Does such a map exist, and is it canonical across the whole
groupoid?  This packages Nima's standing harmonic-support test
(ev-000000000672) — does the connected \(b_1=1\) topology force

\[
\det[H_u,H_d]\;=\;2i\sum_m a_m\sin(m\phi)
\]

to carry only the first harmonic at finite \(\epsilon\), or do higher
odd harmonics appear — and lifts it from the four worked textures to
every vertex of the carrier groupoid.

## Method

Exact symbolic arithmetic (sympy); no floating point and no fitted
values.  For each of the 61 presentations of the WP9 atlas, \(Y_u,Y_d\)
are built from the support masks with nine symbolic positive magnitudes
and \(z=e^{i\phi}\) on the chart phase edge; \(Y^\dagger\) is the
Laurent transpose \(z\mapsto z^{-1}\).  Since
\(C=[H_u,H_d]\) is a \(3\times3\) traceless commutator,
\(\det C=\operatorname{tr}C^3/3\) identically (verified against
`C.det()` on a generic exact rational specialization, gate G0).  The
checker extracts the exact Laurent support of \(\det C\) in \(z\), the
exact CP antisymmetry \(a_{-m}+a_m=0\), and — new in this cycle — the
Laurent supports of all six characteristic-polynomial coefficients of
\(H_u\) and \(H_d\) (the mass-sector \(\phi\)-dependence audit).
Cross-validation gate G1 rebuilds the four worked textures
S38/S43/S48/S53 as masks and reproduces the independent
`harmonic_support.json` supports.  Checker:
`research/flavor/checkers/wp12_unoriented_pushforward_census.py`;
results: `research/flavor/results/wp12_unoriented_pushforward.json`.

## Result

**T1 — first harmonic only, everywhere, exactly.**  For all 61 of 61
carrier-groupoid vertices, with fully symbolic magnitudes,

\[
\det[H_u,H_d]\;=\;a_1\,(z-z^{-1})\;=\;2i\,K_v(\text{magnitudes})\sin\phi_v,
\qquad a_1\ \phi\text{-free},
\]

with exact coefficient-wise CP antisymmetry.  No \(z^{\pm2}\) or
\(z^{\pm3}\) coefficient survives in any chart.  This upgrades WP9's
numerical T4 (higher/first ratio \(\le 2.3\times10^{-11}\)) to an exact
per-vertex theorem and extends the four worked-texture computations of
`harmonic_support.py` to the entire fitted groupoid.  The \(z^3\)
coefficient vanishes mechanism-wise: the \(z\)-dependent part of
\(H_u\) is \(zE+z^{-1}E^\dagger\) with \(E=|q^\ast\rangle\langle a|\)
rank one and \(E^2=0\) (the diagonal cancels the phase), so
\(\operatorname{tr}P^3\), \(P=[E,H_d]\), reduces by cyclicity to
\(\operatorname{tr}(EH_d)^3-\operatorname{tr}(H_dE)^3=0\); the \(z^2\)
coefficients vanish support-by-support and are certified exactly per
vertex.  A support-general graph proof over all nine-link topologies
(not only the 61 fitted ones) remains open and is flagged as a
conjecture with mechanism, not a theorem.

**T2 — the mass sector is \(\phi\)-free in 49 charts and
\(\cos\phi\)-dependent in 12.**  All six char coefficients have support
\(\{0\}\) in 49/61 charts.  The 12 exceptions all carry the loop phase
in the *down* sector; there \(c_2^d\) (and in orbit-2 charts also
\(c_3^d\)) acquires support \(\{-1,0,+1\}\) in exact palindromic form
\(a_1=a_{-1}\), i.e. a \(\cos\phi_v\) term.  Inspected mechanism: a
single-monomial cross term (e.g. \(-m_3m_4m_7m_8\) for member
\((140,486)\)) from a column-minor with exactly two matchings, one
using the phase edge — the \(|A+zB|^2\) interference predicted by
Cauchy–Binet.

**T3 — the unoriented pushforward is canonical across the groupoid.**
Combining T1, T2, and the standard identity
\(\det[H_u,H_d]=-2iJ\prod_{i<j}(\lambda^u_i-\lambda^u_j)\prod_{k<l}(\lambda^d_k-\lambda^d_l)\)
(up to sign convention):

\[
J(\phi_v)\;=\;\frac{K_v(\text{mags})}{D_v(\cos\phi_v)}\sin\phi_v ,
\]

with \(D_v\) constant in the 49 charts.  In every chart the CP-even
readout (masses, \(|V_{ij}|\)) is an even function of \(\phi_v\) and
the CP-odd readout is odd.  Hence the full physical readout factors
through the unoriented line \(\{\phi_v,-\phi_v\}\), landing in the
CP-unordered pair \(\{J,-J\}\); in the 49 mass-flat charts the sharp
form is \(|J|=(|K_v|/D_v)\,|\sin\phi_v|\) *exactly*, not at leading
order.  WP10 certified all 61 vertices lie over one physical point, so
the groupoid-level readout is constant while every vertex's lens data
reaches it through unoriented data alone.

## Interpretation

The WP11 Möbius sign ambiguity is not an obstruction to physics — it
*is* physical CP conjugation.  No global sign for \(\phi\) exists on
the carrier groupoid, and T1–T3 show none is needed: every
loop-sensitive physical observable is sign-insensitive because the
complete CP-odd shadow of the loop is a single sine.  The content of
the loop holonomy visible to the weak-basis-invariant ring is exactly
one real number, \(|\sin\phi_v|\) (modulated by magnitude data), at
every vertex.  Note the boundary of the result honestly: this is a
statement about the chart-to-readout map of the fitted groupoid.  It
does not select \(\phi\) (the invariant ring cannot quantize it —
entry 1042's fiber statement stands), and the almost-\(\pi/8\)
clustering remains a property of where the fitted points sit in the
readout, not of the map.  For the H2LR typing: the flavor lens
\(\mathcal K_{\mathrm{flavor}}\) may be taken as edge magnitudes plus
the *unoriented* loop-holonomy line, and the pairing
\(\langle-,-\rangle_{\mathrm{flavor}}\) is canonical on that lens at
all 61 vertices.

## Verification

- G0: \(\det C=\operatorname{tr}C^3/3\) verified against `C.det()` on a
  generic exact rational specialization — pass.
- G1: S38/S43/S48/S53 rebuilt as masks \((282,314)\), \((277,421)\),
  \((305,342)\), \((305,412)\); supports match
  `results/harmonic_support.json` (\(\{1\}\), CP-antisymmetric) in all
  four cases — pass.
- Census: 61/61 charts \(\det C\) support exactly \(\{-1,+1\}\) with
  exact antisymmetry; 49/61 mass sector \(z\)-free; 12 exceptions
  enumerated (all d-sector phase; palindromic \(c_2^d\), plus \(c_3^d\)
  in orbit 2); zero unexplained exceptions.
- Checker and results are stdlib-plus-sympy exact; runtime ~68 s.

## Relations

- Sharpens WP9 entry 1890 T4 (numeric \(\to\) exact) and extends
  `harmonic_support.py` (four textures \(\to\) full groupoid).
- Answers Nima's ev-000000000672 test at census level: only \(m=1\)
  survives, at every fitted vertex, at finite \(\epsilon\).
- Completes the WP11 (entry 1901) typing: the Möbius sign defect is
  exactly the CP conjugation ambiguity of the physical readout.
- Leaves open: a support-general proof of first-harmonic-only for all
  nine-link one-cycle topologies (mechanism identified; census-exact on
  the fitted groupoid).

# 1051 — Matching-Reality Is Gaugeable Presentation Data; the Second-Harmonic Toggle Map; the Flavor Admission Position

## Question

Two items close the current flavor cycle:

1. WP5 of the research brief: for each worked texture, enumerate the
   perfect matchings, reconstruct \(\det Y_u\) and \(\det Y_d\), locate
   the phase-carrying edge, and determine when
   \(\arg\det(Y_uY_d)=0\) — and what that fact *is*, epistemically.
2. The open analytic item from Entry 1048: does the connected
   \(b_1=1\) sparse topology alone force the \(m=2\) Fourier coefficient
   of \(\det[H_u,H_d]\) in \(z=e^{i\phi}\) to vanish?

Together they fix the admission position the operator asked for:
does Marici hold for the flavor sector?

## WP5: what the exact audit establishes

For all four worked charts of the source (S38, S43, S48, S53), every
sector bipartite graph has a UNIQUE perfect matching, and its signed
term equals the determinant exactly (all arithmetic symbolic):

\[
\det Y=\sum_{\text{matchings}}(\pm)\prod_{\text{edges}}y_e
\quad\text{(one term per sector).}
\]

Phase-edge matching membership and the resulting determinant reality:

\[
\begin{array}{c|c|c|c}
\text{chart} & \text{phase edge} & \text{in a matching?} &
\det(Y_uY_d)/\overline{\det(Y_uY_d)}\\
\hline
\text{S38 (Ex. I)} & Y^u_{12} & \text{yes (unique }u\text{ matching)} & -1\\
\text{S43 (Ex. II)} & Y^d_{33} & \text{no} & +1\\
\text{S48 (Ex. III)} & Y^d_{12} & \text{no} & +1\\
\text{S53}\ (\pi/4) & Y^d_{22} & \text{no} & +1
\end{array}
\]

Example I is NOT matching-real as placed — but an exact diagonal
rephasing repairs it: \(D_u=\mathrm{diag}(1,e^{i\pi/2},1)\),
\(Y_u\to Y_uD_u^\dagger\), moves the loop phase \(Y^u_{12}\to Y^u_{22}\)
(an edge in no matching), keeps every non-loop entry real, preserves
the loop phase at \(\pi/2\), and makes \(\det Y_u\), \(\det Y_d\) both
real.  Verified exactly.

Groupoid transport: the \(S_3^3\) permutation of Example I from
Entry 1042 carries the phase edge \((u,1,2)\to(u,3,2)\) (located
mechanically, not by hand) and preserves matching membership
(True \(\to\) True).  Matching-reality transports under the full
sparse texture groupoid.

Source census (App. V): 5 of the 99 fixed-phase textures do NOT allow
the phase to avoid all determinant matchings.  Matching-reality fails
even inside the presentation ensemble.

**Verdict.** \(\arg\det(Y_uY_d)=0\) is a presentation-level
naturalness property: it holds in canonical gauge when the phase edge
avoids the matchings, requires a gauge move in Example I, transports
under the texture groupoid, is destroyed together with the chart under
general \(U(3)^3\) (Entry 1042), and is not even chart-universal
(5/99).  It is graph-combinatorial reality — the source's own first
item — and the audit forbids promoting it past the source's stated
assumptions toward a strong-CP solution.

## The \(m=2\) toggle map: purity is finer than \(b_1\)

Method: add ONE extra real positive edge \(x\) at each zero position of
S38 and S43 (graph goes to \(b_1=2\)) and recompute
\(\det[H_u,H_d]\) EXACTLY as a Laurent polynomial in \(z\) with all
magnitudes symbolic; record whether the \(m=2\) coefficient \(a_2\)
stays identically zero.  (The \(\epsilon\)-power assigned to \(x\)
cannot affect identical vanishing.)  Every row cross-checked
numerically at \(\epsilon=0.9\) by 16-point FFT against a \(10^{-8}\)
noise floor.

Baselines reproduce support \(\{1\}\).  The toggle table:

\[
\begin{array}{c|c|c}
& a_2\ \text{broken} & a_2\ \text{preserved}\\
\hline
\text{S38 (phase in }u\text{)} &
\text{all 5 up-sector zeros} &
\text{all 4 down-sector zeros}\\
\text{S43 (phase in }d\text{)} &
u_{12},u_{21},u_{23},u_{32},d_{22} &
u_{31},d_{12},d_{21},d_{31}
\end{array}
\]

Three consequences:

- **\(b_1=2\) is neither necessary nor sufficient** for a second
  harmonic.  First-harmonic purity is a finer graph property than
  cycle rank; the general criterion remains OPEN, now with an exact
  table to test conjectures against.
- **No \(m\geq3\) harmonic ever appears**, even with a tenth edge —
  consistent with the universal nilpotent rank-one mechanism
  (\(A^2=0\)) that kills \(m=3\) for ANY one-phase-entry Hermitian
  pair (Entry 1048).
- **Correction.**  The exploratory numeric probe behind the 1048
  cycle had suggested S43 tolerates every tenth edge.  That was an
  \(\epsilon^{27}\)-suppression artifact (the breaking \(a_2\)
  polynomials have leading \(\epsilon\)-orders up to 27 and vanish
  below any small-\(\epsilon\) numeric floor).  The symbolic checker
  supersedes it: S43 breaks at five of nine positions.

## The admission position

The operator's question: does Marici hold for the flavor sector?

- **The provisional strong typing is falsified** (Entry 1042): the
  loop holonomy \(\phi\) is a chart invariant of the sparse texture
  groupoid, not a \(U(3)^3\) weak-basis invariant.  No repair has
  appeared; WP5 shows the other conspicuous chart quantity
  (matching-reality) has the same epistemic status.
- **What survives is standard quotient physics with an unusually
  well-behaved presentation**: the physical object is
  \(\mathfrak F_{\rm phys}=\{(Y_u,Y_d)\}/U(3)^3\) with the standard
  weak-basis-invariant readout, and the nine-link charts are a sparse
  atlas on it whose chart\(\to\)invariant map is exact and completely
  computed:
  \(\det[H_u,H_d]=2iF(\text{magnitudes},\epsilon)\sin\phi\) at finite
  \(\epsilon\) (Entry 1048), with exact two-point fibers
  \(\{\phi,\pi-\phi\}\) (Entry 1047).
- **The almost-\(\pi/8\) clustering is explained as selection**
  (Entry 1048): the viability equation forces
  \(\phi\simeq\theta_{\rm phys}\in\{\alpha,\beta,\gamma\}\) at leading
  order, and the observed CKM angles sit near multiples of
  \(\pi/8\).  It is not evidence for H2S.
- **H2W is strengthened as vocabulary**: flavor independently
  exhibits the program's recurring chart/quotient distinction
  (Benincasa's reading of Entry 1042), alongside the cosmology and
  string instances.
- **H2S has no positive support from flavor.**  The single remaining
  route to a genuine sector theorem is the open item above:
  connected \(b_1=1\) (+ source viability conditions)
  \(\Rightarrow\) harmonic support \(\{1\}\).  If such a theorem
  exists, "support \(\Rightarrow\) harmonic content" is a
  graph-topology-to-observable-algebra statement internal to flavor
  and the first candidate shape for a cross-sector bridge.

\[
\boxed{
\text{Flavor is NOT admitted as a fourth Marici sector under the
strong typing.  Admission pending exactly one item: the }b_1=1
\Rightarrow\{1\}\text{ theorem or a counterexample.}
}
\]

Negative results banked along the way: \(\phi\) is not physical
(1042); the pushforward is \(\sin\phi\)-only, fibers
\(\{\phi,\pi-\phi\}\) (1047, 1048); \(\pi/8\) is viability selection
(1048); matching-reality is gaugeable presentation data (this entry).

## Verification artifacts

- `research/flavor/checkers/wp5_matching_reality.py`
- `research/flavor/results/wp5_matching_reality.json`
- `research/flavor/checkers/m2_toggle_map.py`
- `research/flavor/results/m2_toggle_map.json`
- numeric cross-check: 16-point FFT at \(\epsilon=0.9\), noise floor
  \(10^{-8}\), all toggle rows confirmed (breaking rows
  \(a_2\sim10^{5}{-}10^{6}\), preserved rows \(\sim10^{-8}\)).

Epistemic graph events:
`ev-000000000685-3ce0c4a9-881e-49f2-a8bc-4c6e156a52fb`
(claim, tests, outcomes) and
`ev-000000000686-ec65aa89-fb8b-48e9-aef9-cd48466ad061`
(replies to marici.Benincasa and marici.Nima).

## Sequence
- allocator claim: `seqclaim-68fd0266049f5f74148aee9c`.

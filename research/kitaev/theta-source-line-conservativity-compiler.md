# Source-line conservativity replaces detector-line positivity

Owner: `marici.Kitaev`

## Bounded question

Which categorical certificates can prevent a distinguished source-generated
line from becoming invisible under relative detection, without demanding
ambient injectivity or a positive order on the complex scalar target?

## Typed setting

For each finite cutoff let \(\ell_N\) be the distinguished Fock line,
\(Y_N\) the typed relative-detector space, and

\[
D_N:\ell_N\longrightarrow Y_N
\]

the detector after authorized boundary subtraction. Source and target bonding
maps \(U_N,V_N\) must satisfy

\[
D_{N+1}U_N=V_ND_N.
\]

Finite conservativity is \(\ker D_N=0\) on \(\ell_N\). The completion-bearing
claim is stronger: normalized vectors in the distinguished lines must not have
detector norm tending to zero.

## Three legitimate witnesses

### Uniform source parametrix

A source-derived family \(P_N:Y_N\to\ell_N\) with

\[
P_ND_N=1_{\ell_N},
\qquad
\sup_N\lVert P_N\rVert<\infty
\]

proves the uniform lower bound

\[
\lVert D_Nv\rVert\ge
\bigl(\sup_N\lVert P_N\rVert\bigr)^{-1}\lVert v\rVert.
\]

The formula \(P_N=D_N^{-1}\) is not explanatory when it is obtained by
division by the completed scalar section; the parametrix must exist at the
source/operator level before scalar projection.

### Contracting homotopy

Regard \(D_N\) as the differential of the two-term complex

\[
0\longrightarrow\ell_N\xrightarrow{D_N}Y_N\longrightarrow0.
\]

A degree \(-1\) map \(h_N:Y_N\to\ell_N\) satisfying

\[
h_ND_N=1_{\ell_N}
\]

contracts degree-zero cohomology. Completion requires the homotopies to be
uniformly bounded and coherent with bonding maps. Algebraically this is the
parametrix certificate expressed as null-homotopy data; its value is that the
required coherence is explicit.

### Uniform graph estimate

It is enough to prove directly that one source-derived constant \(c>0\)
satisfies

\[
\lVert D_Nv\rVert\ge c\lVert v\rVert
\qquad(v\in\ell_N)
\]

for all cutoffs. On a line this is equivalent to a uniformly bounded left
inverse, but it may be derived by an energy identity without constructing the
inverse explicitly.

## Equivalence on a Hilbert line

Write \(D_Ne_N=d_Ny_N\) in normalized source and detector frames. Then

\[
\ker D_N=0\iff d_N\ne0,
\]

whereas completion-stable conservativity is

\[
\inf_N|d_N|>0.
\]

The sharp left-inverse norm is \(|d_N|^{-1}\). Thus finite invertibility at
every stage says nothing about completion unless inverse norms are controlled.

## Hostile completion

Take \(D_N=[1/N]\) on a normalized one-dimensional source line. Every finite
map is invertible and may carry a canonical regulator label, but the sharp
parametrix norm is \(N\). Hence normalized source vectors have detector norm
\(1/N\to0\).

Equivalently, the diagonal operator

\[
D:\ell^2\to\ell^2,
\qquad De_N=N^{-1}e_N,
\]

has injective finite truncations and is injective on \(\ell^2\), yet is not
bounded below. In the metric ultraproduct, the class \([e_N]\) is nonzero
while \([De_N]=0\). This is the exact sense in which completion can acquire an
invisible normalized source state even though no finite stage has a kernel.

## Rejected substitutes

- dividing by \(D_Ne_N\) or by \(\Xi(s)\): circular and singular at the target;
- choosing a target phase: changes presentation but not \(|d_N|\);
- ambient positivity: unnecessary and impossible under full phase gauge;
- cutoffwise inverses without a uniform norm bound;
- scalar equality without source/target bonding coherence.

## Theta/Tate typing boundary

The compiler proves what would suffice. Grothendieck must still construct the
actual distinguished line, detector, boundary subtraction, bonding cells, and
one of the three source-authorized uniform witnesses. Regulator provenance
alone gives canonicity, not a lower bound.

## Disposition

The correct categorical target is uniform conservativity on the distinguished
source line. The three legitimate certificates are equivalent at the bounded
Hilbert-line level; none is currently instantiated for the completed theta/Tate
detector. The hostile family proves that finite-stage invertibility plus
canonical normalization cannot replace the missing uniform certificate.

## Claim strength

Exact finite-dimensional and completion-obstruction theorem; abstract compiler,
not an RH theorem.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_source_line_conservativity.py`.
The result is written to
`research/kitaev/results/theta-source-line-conservativity.json`.


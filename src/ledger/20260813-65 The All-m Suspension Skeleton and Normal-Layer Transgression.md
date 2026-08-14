# The All-\(m\) Suspension Skeleton and Normal-Layer Transgression

## Record

Date: 2026-08-13

Status: exact integral theorem for the abstract carrier \(K_{2,m}\), followed by
a conditional scalar-normal-geometry hypothesis. Only the \(m=3\) carrier is
currently derived from the scalar polarity atlas.

Entry 64 proved that the two six-point scalar polarity tripods glue to
\(K_{2,3}\), and that their Mayer--Vietoris boundary sends the QTDS contact
difference to the marked-theta Ward circuit. The cellular part of that result
is not special to three roads.

For every \(m\geq2\), let

\[
R_m=\{0,\ldots,m-1\}
\]

be a discrete road set and let \(S^0=\{+,-\}\) be a two-element polarity set.
Then

\[
K_{2,m}
=
S^0*R_m
=
\operatorname{Cone}_+(R_m)\cup_{R_m}\operatorname{Cone}_-(R_m).
\]

The reduced road divisor lattice suspends canonically and integrally to the
entire circuit lattice:

\[
\boxed{
\Gamma_m:
\widetilde H_0(R_m;\mathbb Z)
\xrightarrow{\ \sim\ }
H_1(K_{2,m};\mathbb Z).}
\]

The theorem supplies the universal carrier that a higher-point scalar
polarity atlas would have to realize. It does not assert that such an atlas
exists.

## Integral suspension theorem

Orient every edge of \(K_{2,m}\) from its polarity core to its road endpoint
and denote it by \(e_{\varepsilon i}\). Identify

\[
\widetilde H_0(R_m;\mathbb Z)
=
A_{m-1}
=
\left\{
(c_0,\ldots,c_{m-1})\in\mathbb Z^m:
\sum_i c_i=0
\right\}.
\]

Define

\[
\boxed{
\Gamma_m(c)
=
\sum_{i=0}^{m-1}
c_i\bigl(e_{+i}-e_{-i}\bigr).}
\]

Since

\[
\partial(e_{+i}-e_{-i})=E_--E_+,
\]

one has

\[
\partial\Gamma_m(c)
=
\left(\sum_i c_i\right)(E_--E_+)
=
0.
\]

Conversely, let \(z\) be an integral cycle in \(K_{2,m}\). The incidence
condition at road \(i\) says that the coefficients of \(e_{+i}\) and
\(e_{-i}\) are opposite. The incidence condition at either core says that the
plus-core coefficients sum to zero. Hence there is a unique \(c\in A_{m-1}\)
such that \(z=\Gamma_m(c)\).

Projection to the plus-core edge coefficients is therefore an integral inverse
to \(\Gamma_m\). In particular, the map is not merely a rational rank
comparison: its image is saturated and it is the Mayer--Vietoris connecting
isomorphism for the union of the two contractible cones.

Equivalently,

\[
\boxed{
H_1(K_{2,m};\mathbb Z)
\cong
A_{m-1}.}
\]

## Symmetry type

The decomposition \(K_{2,m}=S^0*R_m\) carries the natural action of

\[
S_2\times S_m.
\]

Road permutations act on \(A_{m-1}\) by the standard root-lattice
representation. Exchanging the two polarity cores reverses every suspended
cycle. Thus the equivariant form of the theorem is

\[
\boxed{
H_1(K_{2,m};\mathbb Z)
\cong
\operatorname{sgn}_{S_2}\boxtimes A_{m-1}.}
\]

This is the all-\(m\) carrier signature of the six-point phenomenon: a
polarity-even reduced channel divisor becomes a polarity-odd Ward circuit
after suspension.

The suspension itself is natural for maps of road sets. If
\(f:R_m\to R_n\), then

\[
(S^0*f)_*\Gamma_m
=
\Gamma_n\widetilde f_*.
\]

Consequently, once a physical Cut is typed as a map of the marked polarity
covers and their coefficient systems, the carrier-level Cut square is forced
to commute. The current gap is precisely the construction of that typed
physical map.

At \(m=2\),

\[
K_{2,2}=C_4
\]

has the larger automorphism group \(D_4\). The subgroup preserving the declared
polarity/road bipartition is \(S_2\times S_2\) of index two. The extra
automorphisms show that the unmarked graph does not remember which factor was
the scalar polarity and which was the road set. Markings or coefficients are
therefore essential even in the smallest example.

## Composition with the road-polygon resolution

Choose a cyclic order on the roads and let \(C_m\) be the oriented road
polygon. Write \(t_i\) for the edge from road \(i+1\) to road \(i\). Its
boundary is

\[
B(t_i)=e_i-e_{i+1}.
\]

Entries 61--63 identify the exact cellular sequence

\[
0
\longrightarrow
H_1(C_m;\mathbb Z)
\longrightarrow
C_1(C_m;\mathbb Z)
\xrightarrow{\ B\ }
A_{m-1}
\longrightarrow
0.
\]

Composing with suspension gives another saturated exact sequence,

\[
\boxed{
0
\longrightarrow
H_1(C_m;\mathbb Z)
\longrightarrow
C_1(C_m;\mathbb Z)
\xrightarrow{\ \Gamma_m B\ }
H_1(K_{2,m};\mathbb Z)
\longrightarrow
0.}
\]

Each adjacent road tag maps to the individually supported four-circuit

\[
\Gamma_m B(t_i)
=
e_{+i}-e_{-i}-e_{+,i+1}+e_{-,i+1}.
\]

The sole relation is

\[
t_0+\cdots+t_{m-1},
\]

the fundamental cycle of \(C_m\). This is the all-\(m\) form of the
three-tag Ward resolution.

There are two different symmetry statements here:

1. \(\Gamma_m\) is \(S_2\times S_m\)-equivariant;
2. the adjacent-tag presentation chooses a cyclic order and is naturally only
   dihedrally equivariant.

The loss from \(S_m\) to \(D_m\) belongs to the planar road presentation, not
to the suspension theorem.

## One source, two constructions

The reduced divisor

\[
c\in A_{m-1}
\]

now has two structurally different uses.

The first is a local resolution problem:

\[
B(j)=c.
\]

Its invariant solution is the integral flow torsor

\[
\operatorname{Flow}_{C_m}(c),
\]

while the inverse Laplacian chooses a rational zero-circulation representative.

The second is a global descent operation:

\[
c\longmapsto \Gamma_m(c).
\]

This map is canonical, integral, and requires no section. The correct picture
is therefore a fork rather than an operator and its inverse:

\[
\boxed{
\begin{array}{ccccc}
&&c\in A_{m-1}&&\\
&\swarrow&&\searrow&\\
\operatorname{Flow}_{C_m}(c)
&&&&
\Gamma_m(c)\in H_1(K_{2,m}).
\end{array}}
\]

The left branch asks for a primitive of a divergence. Its ambiguity is
harmonic flow on the road polygon. The right branch turns the same overlap
datum into a global cycle by gluing two local cones. Confusing these branches
is what made the inverse Laplacian look more fundamental than it is.

At \(m=3\), scalar geometry supplies both branches. The two QTDS polarity
tripods contain local primitives \(\eta_6^\pm\) with the same boundary \(c\),
and

\[
\eta_6^+-\eta_6^-
\longmapsto
\Gamma_3(c).
\]

Thus the Ward circuit is not the chosen scalar current. It is the obstruction
to identifying the two scalar currents across the polarity cover.

## Normal-layer transgression hypothesis

The exact theorem suggests an additional theory-producing operation on the
scalar master. Let \(\mathcal U=\{U_+,U_-\}\) be a scalar-derived polarity
cover, let its overlap carry a coefficient system \(\mathcal E\), and suppose
a normal extraction produces a reduced overlap class

\[
c\in
\widetilde H_0(U_+\cap U_-;\mathcal E).
\]

The Mayer--Vietoris connecting map produces

\[
\delta_{\mathrm{MV}}(c)
\in
H_1(U_+\cup U_-;\mathcal E).
\]

The proposed operation is

\[
\boxed{
\operatorname{Trans}_{\mathcal U,\mathcal E}
=
\delta_{\mathrm{MV}},}
\]

or, for a larger atlas, the corresponding class in the total
Cech/derived-descent complex.

This changes the candidate master principle. A derived physical sector need
not be the output of one globally defined operator on an amplitude. It may be
a descent class measuring the incompatibility of locally valid scalar-derived
dictionaries:

\[
\text{normal data on overlaps}
\longrightarrow
\text{local primitives}
\longrightarrow
\text{global transgression class}.
\]

The six-point carrier theorem is the first exact instance of this pattern.
Calling the resulting class a physical Yang--Mills class still requires the
first-normal-jet and gauge-cohomological coefficient map.

## Relation to the emerging operation algebra

The tentative scalar operation list should therefore be widened from unary
operations

\[
\operatorname{gr}_R,\quad
J^1_F,\quad
H_{\rm gauge},\quad
I_{\rm scalar}^{-1},\quad
\operatorname{HarmSchur}_\lambda,\quad
\operatorname{Mod}
\]

to a derived descent calculus containing

\[
\check C(\mathcal U;\mathcal E),
\qquad
\delta_{\rm MV},
\qquad
\operatorname{Tot},
\qquad
\operatorname{hofib}.
\]

This is not evidence for a strict operator algebra on final amplitudes. It is
evidence for a homotopy-coherent dictionary between self-factorizing carriers.
Unary operations describe local normal models; descent data determine whether
those local models assemble into a global physical sector.

The representation identity

\[
H_1(K_{2,m})
\cong
\operatorname{sgn}_{S_2}\boxtimes A_{m-1}
\]

is especially useful because it predicts the symmetry type of the missing
physical coefficient carrier before its formula is known.

## Precise next falsifier

The first new case is \(m=4\). One must not begin by freely drawing
\(K_{2,4}\). Instead, derive or disprove the following data inside scalar
normal geometry:

1. two canonical polarity carriers \(U_+^{\rm sc}\) and \(U_-^{\rm sc}\);
2. four common channel strata whose contracted incidence is \(R_4\);
3. a scalar normal source in \(A_3=\widetilde H_0(R_4)\);
4. local primitives on the two carriers with equal boundary;
5. a physical first-jet/Ward coefficient map transforming as
   \(\operatorname{sgn}_{S_2}\boxtimes A_3\);
6. a marked Cut whose induced map commutes with the suspension square;
7. an oriented image for the polygon relation generator.

Failure of items 1 or 2 means that the all-\(m\) graph is only a formal
completion of the six-point carrier. Failure of items 5 or 6 means that the
Mayer--Vietoris class exists topologically but is not the physical Ward sector.

The executable next test is a marked-road comparison between \(m=4\) and
\(m=3\). It should retain the nonsplit four-tag resolution rather than choose
the rational \(1/4\) Green section.

## Reproducible certificate

Run:

```text
rustc --edition=2021 -O research/nima/check_k2m_suspension.rs -o "$env:TEMP\\marici-k2m-suspension.exe"
& "$env:TEMP\\marici-k2m-suspension.exe"
```

The certificate proves the integral inverse to \(\Gamma_m\), saturation,
\(S_2\times S_m\) covariance, the adjacent-road four-circuit formula, and the
dihedral tag relations. It audits the finite combinatorics for
\(2\leq m\leq12\).

## Internal dependencies

- Entries 21 and 64: the scalar-derived \(m=3\) polarity carrier.
- Entries 61--63: the all-\(m\) road resolution, Green section, and flow
  torsor.
- `research/nima/check_k2m_suspension.rs`: exact all-\(m\) certificate.

## Forward update

Entries 67--68 execute and refine the proposed \(m=4\) falsifier. The
identification \(m=n/2\) fails, and even the provisional global \(K_{2,8}\)
requires collapsing disconnected rank-one fibers. The canonical octagon
rank-zero/rank-one skeleton is two disjoint stars, while every marked
factorization boundary recovers \(K_{2,3}\). The abstract suspension theorem
survives as a local model; higher scalar realizations must be extracted from
the full regional-polarity core diagram or its homotopy colimit.
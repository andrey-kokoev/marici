# Magnetic 24-by-3 numerical upper bracket

The frozen complement supplies a reproducible construction upper bracket for
the worst three-port deletion condition number:

\[
\kappa_{\mathrm{worst}}\le 238.40834228941753
\]

at float64 resolution. Its columns are Parseval to defect
\(5.87\times10^{-16}\), and all 2024 three-row submatrices are numerically
invertible. The worst triple is the zero-based row set \((8,11,18)\), with

\[
\sigma_{\min}=0.004194484095636396.
\]

This is deliberately separate from the exact lower-bound theorem

\[
\kappa_{\mathrm{worst}}>
[1012(2+\varphi)]^{1/6}\approx3.925926752.
\]

The wide interval is honest: the lower endpoint is a universal symbolic
obstruction, while the upper endpoint is one nonoptimal numerical
construction.

## Exact existence certificate

Interpret every stored decimal entry as a rational number and call the
resulting matrix \(B\). Its Gram matrix satisfies the exact rational bound

\[
\delta=\|B^TB-I\|_2
\le\|B^TB-I\|_\infty<10^{-14}.
\]

Form its exact real polar factor

\[
Q=B(B^TB)^{-1/2}.
\]

Then \(Q^TQ=I\), and spectral calculus gives \(\|Q-B\|_2\le\delta\).
For each three-row restriction \(T\), exact rational arithmetic verifies

\[
\sigma_{\min}(B_T)
\ge\frac{2|\det B_T|}{\|B_T\|_F^2}
>\frac1{673}+10^{-14}.
\]

Weyl perturbation therefore proves

\[
\sigma_{\min}(Q_T)>\frac1{673}
\quad\hbox{for all }|T|=3,
\]

and hence constructs an exact Parseval complement with

\[
\kappa_{\mathrm{worst}}<673.
\]

The polar entries are generally algebraic rather than rational. The stronger
float64 estimate \(238.41\) is not promoted to a rigorous bound by this
argument.

The determinant estimate is intentionally elementary but wasteful. A sharper
exact test retains the full singular spectrum. For every rational three-row
block \(B_T\), exact arithmetic verifies all three leading principal minors
of

\[
B_TB_T^T-
\left(\frac1{261}+10^{-14}\right)^2I
\]

are positive. Sylvester's criterion therefore gives

\[
\sigma_{\min}(B_T)>\frac1{261}+10^{-14}.
\]

The same polar perturbation bound removes at most \(10^{-14}\), proving the
sharper exact result

\[
\sigma_{\min}(Q_T)>\frac1{261},
\qquad
\kappa_{\mathrm{worst}}(Q)<261.
\]

The smallest verified third leading principal minor is approximately
\(3.82\times10^{-10}\). Thus the exact upper bound lies within about
\(0.14\%\) of the float64 estimate, without promoting that estimate itself.

Exact rational bisection can retain essentially the entire margin. Repeating
the same Sylvester test at the threshold

\[
\frac1{238.4083423}+10^{-14}
\]

leaves every principal minor positive. The active block is again
\((8,11,18)\). Therefore the algebraic polar frame rigorously satisfies

\[
\kappa_{\mathrm{worst}}(Q)<238.4083423.
\]

The hostile neighboring certificate request at \(238.4083422894\) is rejected
because the active block's third Sylvester minor becomes negative. Failure of
this sufficient certificate does not disprove that tighter proposition. The
proved upper bound concerns the constructed frame and does not show that it
minimizes the 24-port design problem.

## Invariant generalized-pencil certificate

The perturbative polar estimate is still only a proof chart. The polar frame
itself admits an exact rational test before taking any square root. Put
\(G=B^TB\). For every row triple \(T\),

\[
\sigma_{\min}\bigl(B_TG^{-1/2}\bigr)>\tau
\quad\Longleftrightarrow\quad
B_T^TB_T-\tau^2G>0.
\]

Both matrices in the pencil have rational entries, so Sylvester's criterion
is exact. Testing all 2024 triples proves

\[
238.4083422894
\le\kappa_{\mathrm{worst}}(Q)
<238.4083422895.
\]

The active triple is \((8,11,18)\) at both endpoints. In particular, the
stronger claim that failed the perturbative certificate is admitted by the
invariant pencil. That earlier failure was a boundary of the chosen proof
chart, not a loss of rank or a counterexample in the underlying frame.

## What the optimization separated

Determinant repulsion first produced condition number about \(408.29\).
Optimizing the triple singular-value floor improved it to about \(260.64\)
without a comparable improvement in the minimum absolute determinant. Thus
minor volume and recovery shape are distinct design variables. Full spark
certifies algebraic recovery; it does not certify useful numerical recovery.

The extended optimization is also not monotone in the true floor: its three
successive condition brackets were approximately \(263.32\), \(265.62\), and
\(260.64\). The optimized smooth inverse-power objective is only a surrogate.
At the final stage, five distinct triples lie within about \(8.9\%\) of the
worst floor. That spreading active set is evidence for minimax balancing, but
it is not a stationarity or optimality certificate.

A later search on the full \(24\)-by-\(3\) Stiefel manifold repaired the
coordinate restriction in that first search. Every proposed tangent move was
polar-retracted and accepted only after replaying all 2024 triples. It reduced
the condition number to approximately \(243.5018551\). Eight triples then lay
within \(0.37\%\) of the floor. This disproves local minimaxity of the earlier
packet, but the improved packet still has one exact active triple and is not
claimed locally or globally optimal.

A second, smaller-scale Stiefel search reduced the bracket further to about
\(243.1082230\). The first three triples are equal within
\(4.6\times10^{-7}\) relative, while six lie within \(2.2\times10^{-5}\).
This is a substantially sharper active-set balance, but exact equality and a
Clarke or KKT stationarity certificate remain open.

The expanded Clarke audit still falsifies stationarity. The closest convex
combination of sixteen near-active Stiefel gradients has norm approximately
\(0.03683\), and its pairing with every constituent gradient is positive.
Normalizing that combination therefore gives a common first-order ascent
direction. A polar-retracted step of size \(3.48\times10^{-7}\), accepted only
after replaying every triple, improves the global floor to approximately
\(0.00419450\), or condition number \(238.40763\). The new floor triple is
\((11,16,20)\).

This proves that the frozen frame is neither locally stationary nor globally
optimal. It does not prove that the escaped frame is optimal, and it does not
exactify that escaped frame; those remain separate constructors.

## Why the active set keeps growing

The real Stiefel manifold of 24-by-3 Parseval complements has tangent
dimension

\[
24\cdot3-\frac{3(3+1)}2=66.
\]

At a regular local maximum of the minimum singular-value objective, Clarke
stationarity requires the origin to lie in the convex hull of the active
Riemannian gradients. Carathéodory's theorem then guarantees that some
stationarity certificate uses at most 67 active gradients. This is an upper
bound on certificate support, not a claim that 67 active triples are
necessary.

The exploratory active-width sequence continued to improve as the hull grew:
approximately \(242.22\) at width 8, \(240.67\) at width 12, \(238.41\) at
width 16, \(235.59\) at width 20, \(234.81\) at width 24, and \(233.46\) at
width 28. The width-28 endpoint separated a cluster of 30 triples from the
31st by a gap of about \(3.09\%\).

The exact 30-gradient convex-hull audit gives strictly positive weight to
every member of that cluster, with smallest weight about \(0.00234\). Thus it
is a coherent oriented face rather than a face padded by irrelevant
constraints. Its closest-hull residual is nevertheless about \(0.01511\), so
the origin remains outside. A common-ascent polar step of approximately
\(9.09\times10^{-4}\) improves the exploratory condition number further to
about \(232.73\). These wider endpoints remain discovery evidence rather than
the exactified contract matrix.

There is a useful invariant interpretation. If \(g_i\) are the active
Riemannian gradients and \(\bar g=\sum_iw_i g_i\) is the closest point of
their convex hull to the origin, strict positivity of every \(w_i\) puts
\(\bar g\) in the relative interior. The simplex KKT equations then give

\[
\langle g_i,\bar g\rangle=\|\bar g\|^2
\]

for every active gradient. Hence \(\bar g/\|\bar g\|\) raises every member of
the 30-face at one common first-order rate. The face is transported as a
coherent packet until a previously inactive constraint collides with it.
Stationarity is exactly the singular limit \(\bar g=0\); before that limit,
the convex projection itself is the canonical repair direction.

The 30-face is not a classical block design. Its 3-uniform support hypergraph
is connected and uses all 24 ports, but vertex degrees range from 1 to 6, only
six pairs repeat, and its 24-by-30 incidence matrix has full row rank. Even
after weighting blocks by the positive closest-hull coefficients, port loads
range from approximately \(0.00388\) to \(0.4163\), rather than becoming
uniform around their mean \(1/8\).

Thus the balance is tensorial, not incidence-only. The relevant active object
is the projected singular-vector tensor

\[
P_{T_B}\!\left(E_S^*u_Sv_S^T\right),
\]

not the indicator of the triple \(S\). A purely combinatorial block design
forgets the orientations and anisotropies that permit tangent-gradient
cancellation.

An abstract hostile fixture makes the information loss exact. Give two
records the same repeated support \(\{0,1,2\}\). If their oriented tensors are
\((1,0)\) and \((-1,0)\), their convex hull contains the origin. If the
tensors are instead \((1,0)\) and \((1,0)\), its distance from the origin is
one. The incidence bytes are identical while the stationarity answers differ.
Therefore no incidence-only classifier can decide tangent cancellation.

This fixture proves a typing requirement, not that either two-vector packet
is realized by the current magnetic frame. Realizability by singular-vector
gradients is a separate source-side constraint.

The tensor constructor is itself stratified. If the least singular value is
simple, its singular vectors obey the simultaneous sign gauge

\[
(u,v)\sim(-u,-v),
\]

and \(uv^T\) is gauge invariant. It is therefore a canonical rank-one
cotangent record. If the least singular value has multiplicity \(r>1\), no
preferred rank-one record exists. The spectral subdifferential is

\[
\left\{UHV^T:H\succeq0,\ \operatorname{tr}H=1\right\}.
\]

Choosing one direction on that stratum requires selector authority not
provided by the matrix. The compiler must retain the whole convex
subdifferential unless such a selector is supplied. The current active minima
are numerically simple; this repeated-value rule is a boundary type.

For any three-row matrix \(T\), with singular values
\(s_1\ge s_2\ge s_3\),

\[
|\det T|=s_1s_2s_3,
\qquad
s_1s_2\le\frac{s_1^2+s_2^2}{2}
\le\frac{\|T\|_F^2}{2}.
\]

Consequently,

\[
\frac{2|\det T|}{\|T\|_F^2}
\le\sigma_{\min}(T)
\le|\det T|^{1/3}.
\]

The normalized shape factor

\[
\chi(T)=\frac{\sigma_{\min}(T)}{|\det T|^{1/3}}
\]

ranges from approximately \(0.04275\) to \(0.89012\) in the frozen packet.
The worst shape occurs at rows \((0,13,20)\), not at the worst recovery rows.
Its two large singular values are close while its normal singular direction
collapses. This is an almost rank-two isotropic sheet, and it nearly saturates
the determinant lower estimate: the slack ratio is approximately
\(1.0001209\).

## Hostile gates

The replay rejects three nearby but invalid inferences:

- duplicating a row creates a singular triple;
- globally scaling the matrix destroys the Parseval contract;
- changing the authority flag cannot turn a numerical frame into executable
  physical observation ports.

The packet constructs an exact algebraic polar frame and certifies its stated
condition interval. It does not prove optimality, and it supplies no source
authority for physical realization. Wider active-set endpoints remain
floating-point discovery evidence until separately frozen and exactified.

## The canonical robust object is a projector

The exact complement \(Q\) canonically determines

\[
P=I_{24}-QQ^T,
\]

an orthogonal projector of rank 21. A 24-by-21 Parseval analysis matrix is a
factorization

\[
A^TA=I_{21},\qquad AA^T=P.
\]

It is not canonical: \(A\) and \(AO\) determine the same projector for every
\(O\in O(21)\). Thus the optimized robust design is intrinsically a
Grassmannian point, while a coefficient matrix is one orthonormal chart.

Relating that chart to the 21 low-harmonic magnetic modes requires a
source-derived comparison isometry. Realizing its 24 rows as executable
observation ports requires a further physical constructor. Neither follows
from the projector's support, rank, or conditioning.

The projector also carries a leverage profile

\[
P_{ii}=1-\|q_i\|^2.
\]

For the frozen design these values range from approximately \(0.82122\) to
\(0.90872\), with maximum deviation \(0.05378\) from the equal-leverage value
\(21/24=7/8\). Hence the design does not lie on the equal-normalization
stratum. If a physical instrument requires equally normalized ports, that is
an additional source constraint and the optimization must be repeated on the
equal-diagonal projector manifold. Row rescaling is not an innocent repair:
it generally changes Parseval tightness and the deletion objective.

The constraint is geometrically substantial. The ambient complement
Grassmannian has dimension

\[
\dim\mathrm{Gr}(3,24)=3(24-3)=63.
\]

Fixing all 24 diagonal projector entries gives only 23 independent equations,
because their sum is the fixed rank. Hence the regular equal-diagonal stratum
has dimension

\[
63-(24-1)=40.
\]

Thus equal normalization removes 23 genuine design directions. This dimension
formula applies on the regular stratum; it does not assert that every
equal-diagonal projector is a smooth point of the diagonal map.

Equal leverage is also characterized by one-erasure minimaxity. Deleting row
\(i\) leaves lower frame bound \(1-P_{ii}=\|q_i\|^2\). Since

\[
\sum_iP_{ii}=21,
\]

some leverage is at least \(7/8\). Therefore every 24-by-21 Parseval frame
satisfies

\[
\kappa_{\text{worst one erasure}}\ge\sqrt8,
\]

with equality exactly on the equal-leverage stratum. The frozen
three-erasure-oriented design instead has worst one-erasure condition about
\(3.30986\), attained at row 9, which is about \(17.0\%\) above \(\sqrt8\).
Thus robustness is indexed by a fault profile: optimizing three simultaneous
erasures can sacrifice minimax performance for one erasure.

An exact Pareto hostile shows that the objectives are genuinely incomparable.
Let

\[
Q_{\mathrm{stack}}=\frac1{\sqrt8}
\begin{pmatrix}I_3\\I_3\\ \vdots\\I_3\end{pmatrix}
\]

with eight identity blocks. This complement is Parseval and every row has
squared norm \(1/8\), so it attains the one-erasure optimum \(\sqrt8\).
However, rows \((0,3,6)\) are identical and their three-row block has rank
one. Its worst three-erasure condition is therefore infinite.

The stacked fixture is better for one erasure and worse for three; the frozen
design is worse for one and finite for three. Selecting between them requires
a typed fault objective or distribution, not a scalar word such as
"robustness."

For the frozen algebraic polar frame, exact rational generalized-eigenvalue
tests give the cardinality profile

\[
3.3098598106\le\kappa_1<3.3098598107,
\]

\[
26.7230985167\le\kappa_2<26.7230985168,
\]

\[
238.4083422894\le\kappa_3<238.4083422895.
\]

The controlling deletion supports are respectively \((9)\), \((17,22)\),
and \((8,11,18)\). Increasing fault cardinality therefore changes the active
geometric locus; it does not merely rescale one fixed weak port set.

The profile terminates sharply after three erasures. Once \(s\ge4\), the
retained analysis matrix has at most 20 rows for a 21-dimensional signal
space, so it cannot be injective. Therefore

\[
\kappa_s=\infty\qquad(s\ge4).
\]

This is the dimensional content of distance four: three erasures can be
corrected when every complementary three-minor is nonzero, while four
erasures force rank loss independently of the chosen frame geometry.

These condition numbers assume that erased-port locations are known. They do
not locate unknown corruptions. Distance four supplies the algebraic budget

\[
2e+s<4,
\]

so one unknown error, or one unknown error together with one known erasure,
is uniquely decodable in exact arithmetic. Error localization is a discrete
decoder capability; the \(\kappa_s\) profile is a continuous stability bound
after the erasure set is given. Neither capability implies the other.

For one unknown error, location \(i\) produces a syndrome on the projective
line \(\operatorname{span}(q_i)\subset\mathbb{RP}^2\). Exact decoding needs
distinct lines; stable localization depends on their minimum projective
angle. The frozen frame's worst pair is \((0,23)\), with angle approximately
\(9.428^\circ\). Exact rational inner-product tests certify

\[
6.10465590
\le\frac1{\sin\theta_{\min}}
<6.10465591.
\]

This syndrome-line condition is neither \(\kappa_1\) nor \(\kappa_2\). It
becomes a physical noise bound only after a syndrome noise model and decision
rule are authorized.

For one unknown error together with one known erasure, the erased coordinate
contributes an unknown nuisance amplitude along its syndrome vector \(q_j\).
The relevant localization problem therefore lives in the quotient

\[
\mathbb R^3/\operatorname{span}(q_j).
\]

Enumerating every erased row and every remaining candidate pair with exact
rational inner products finds the worst quotient geometry at erased row
\(j=7\) and candidate error rows \((2,23)\), using zero-based indices. The
projective angle is approximately \(0.892115814^\circ\), and the exact
inverse-sine condition factor satisfies

\[
64.22719311
\leq
\frac{1}{\sin\theta_{\min}^{(1,1)}}
<
64.22719312.
\]

Thus all quotient syndrome lines remain distinct, as required by the
distance-four budget \(2e+s<4\) for \((e,s)=(1,1)\), but their worst local
separation is much poorer than in the un-erased one-error problem. This proves
exact mixed decodability for the frozen algebraic frame; it does not promote
that statement to stable localization or to a physical noise guarantee.

The local Sommerfeld normal form separates this conditional collision from an
ordinary small-volume event. Let \(K_{rs}=\langle q_r,q_s\rangle\). An exact
Schur-complement identity gives

\[
\sin^2\theta_{a,b\mid j}
=
\frac{
\det K_{\{j,a,b\}}\,K_{jj}
}{
\det K_{\{j,a\}}\,\det K_{\{j,b\}}
}.
\]

For \((j,a,b)=(7,2,23)\), the raw determinant of the corresponding three
pre-polar rows is approximately \(8.7338948987\times10^{-4}\). It ranks only
41st-smallest among the 2024 triples, rather than first. The projector Gram
determinant is approximately \(7.6280920101\times10^{-7}\), while the two
pair determinants are approximately \(0.01966279960\) and \(0.02110221931\).
The instability is therefore conditional: the three-way volume is small
relative to two individually robust pair areas.

Numerically, a near-left-null relation is

\[
-0.35063721q_7+q_2+0.96529111q_{23}\simeq0.
\]

Erasing row 7 discards almost exactly the component that distinguishes rows 2
and 23. This explains the quotient amplification for the frozen frame, but it
does not yet explain why the magnetic source should force this relation. That
requires tracing the relation through the source constructor or showing that
it persists under every authorized deformation.

An ambient deformation audit rules out a stronger rigidity claim. On the
Stiefel manifold of 24-by-3 Parseval frames, the tangent gradient norm of the
logarithmic quotient separation is approximately \(476.7598\); the collision
is not stationary. Moreover, a cone-corrected combination with the previously
audited common triple-floor ascent direction gives a small polar-retracted
step that changes

\[
64.2271931\longrightarrow64.2270641
\]

for the mixed condition factor and simultaneously changes

\[
238.4083423\longrightarrow238.4081340
\]

for the worst three-erasure condition factor. Thus the frozen point is not
Pareto-rigid relative to the audited ambient tangent constraints. This remains
an exploratory frame deformation: no source-derived magnetic constructor has
authorized the direction, and the single finite step is not a global Pareto
theorem.

The joint direction is not an analysis-chart rotation. Its vertical component
along the right \(O(3)\) gauge has norm approximately
\(1.9\times10^{-11}\), while its horizontal component has unit norm. For the
rank-21 projector \(P=I-QQ^T\), the induced tangent is

\[
\dot P=-(DQ^T+QD^T),
\qquad
\|\dot P\|_F=\sqrt2.
\]

The escape therefore changes the invariant Grassmannian point rather than
only its complement coordinates.

This also locates the present authority boundary. The magnetic low block is
already source-defined as

\[
\mathcal H_{2,M}\oplus\mathcal H_{3,M}\oplus\mathcal H_{4,M}
\simeq\mathbb R^{21},
\]

with a normalized harmonic basis and 21 authorized coefficient observations.
The missing constructor is not the magnetic source map. It is the redundant
port encoder

\[
E:\mathbb R^{21}\longrightarrow\mathbb R^{24},
\qquad EE^T=P,
\]

realizing the optimized rank-21 projector as 24 executable linear
aggregations. The projector fixes all deletion conditioning invariants, but an
\(O(21)\) choice remains when identifying its image with the labelled harmonic
basis. The candidate supplies neither that isometry nor an exact 24-by-21
coefficient packet with instrument authority. An optimizer seed supplies
neither. The smallest adequate constructor must provide the encoder isometry,
exact coefficients, harmonic-label coherence, coefficient-realization
authority, and instrument-execution authority.

The mathematical encoder existence gap can be closed without selecting a
fitted physical instrument. The rational matrix

\[
P=I-B(B^TB)^{-1}B^T
\]

is an exact rank-21 projector. Every complementary three-row minor is
nonzero, so the chart \(J=\{0,\ldots,20\}\), omitting rows \(21,22,23\), is
invertible. Therefore

\[
E=P_{[:,J]}\bigl(P_{[J,J]}\bigr)^{-1/2}
\]

is a deterministic exact real-algebraic 24-by-21 Parseval encoder satisfying
\(EE^T=P\). Float64 replay gives a chart eigenvalue floor of approximately
\(0.02764\), Parseval defect \(1.4\times10^{-14}\), and projector reproduction
defect \(1.4\times10^{-14}\). What remains missing is a materialized exact
coefficient record plus coefficient-realization and instrument-execution
authority; algebraic construction alone does not supply either capability.

The coefficient record can itself be exact without expanding 504 algebraic
entries. The contract now carries a typed expression DAG whose nodes construct
\(G=B^TB\), the rational projector \(P\), the selected chart \(C=P_{[:,J]}\),
its positive-definite Gram block \(H=P_{[J,J]}\), the unique principal
inverse square root \(R=H^{-1/2}\), and finally \(E=CR\). The equations

\[
E^TE=I_{21},\qquad EE^T=P,\qquad RHR=I_{21},\qquad R>0
\]

uniquely type its value. This closes machine-readable mathematical
materialization while deliberately leaving coefficient realization and
instrument execution unauthorized.

The exact packet also induces a source-neutral realization acceptance test.
If an implemented encoder \(\widetilde E\) satisfies

\[
\|\widetilde E-E\|_2\le10^{-4},
\]

then every three-row restriction changes by operator norm at most \(10^{-4}\).
Using the exact nominal condition endpoint and Weyl's inequality gives

\[
\sigma_{\min}(\widetilde E_{S^c})
>
\frac1{238.4083422895}-10^{-4}>0
\]

for every three-port deletion set \(S\), and hence

\[
\kappa_{\mathrm{worst}}(\widetilde E)<244.2310134.
\]

This specifies a sufficient coefficient-realization tolerance. It does not
assert that an instrument has been measured against the specification, and it
does not define a physical noise model.

For unconstrained coefficient error, the exact worst-case acceptance radius
can be characterized rather than merely bounded. Let \(\mathcal F\) be the
union, over all three-port deletion sets, of matrices whose retained block has
rank below 21. Then

\[
\operatorname{dist}_2(E,\mathcal F)
=
\min_{|S|=3}\sigma_{\min}(E_{S^c}).
\]

Weyl's inequality proves the lower bound. Conversely, for an active deletion
set, subtracting the smallest singular value times its left-right singular
dyad on the retained rows produces a full-matrix perturbation of exactly that
norm and kills the singular direction. The certified radius satisfies

\[
0.0041944840956349457
<
\operatorname{dist}_2(E,\mathcal F)
<
0.0041944840956367052.
\]

At the active deletion set \((8,11,18)\), the hostile rank-one perturbation
drops the retained rank to 20. The conservative \(10^{-4}\) specification uses
about 2.38 percent of this sharp unconstrained radius. The theorem permits
arbitrary coefficient perturbations; it neither preserves Parseval structure
nor supplies a physical noise interpretation.

## Hostile DPC compilation

The physical pipeline is currently typed as mathematically completed but
operationally unclosed:

\[
\mathcal H_{2:4,M}
\longrightarrow\mathbb R^{21}
\longrightarrow\mathbb R^{24}
\dashrightarrow\text{implemented coefficients}
\dashrightarrow\text{physical records}.
\]

The first three objects and arrows are source or mathematically authorized.
The dashed arrows require coefficient-realization and instrument-execution
authority. The compiler separately types known erasure, unknown additive
error, mixed error-erasure, coefficient drift, correlated port loss, and
harmonic-label confusion; none may borrow a theorem proved for another fault
action.

Eight hostile fixtures reject distinct forms of laundering:

1. an exact expression DAG promoted to realized coefficients;
2. algebraic existence promoted to execution;
3. a realization bound asserted without calibration;
4. an erasure theorem applied to unknown corruption;
5. independent deletion tolerance promoted to correlated-fault authority;
6. the sharp mathematical radius promoted to a physical noise tolerance;
7. a dense coefficient formula promoted to a local detector architecture;
8. a three-modes-per-port architecture promoted to three-erasure tolerance.

The last fixture matters even after exact coefficient materialization. A
global linear functional is mathematically executable as a finite sum, but a
local detector may not have access to all 21 harmonic coefficients. No
detector-support architecture is currently declared. Physical closure
therefore requires five independent payloads: coefficient-realization
authority, instrument-execution authority, a calibration witness, a
source-derived fault grammar, and a detector-support architecture.
Each field has a distinct deletion witness. This establishes minimality only
relative to the declared physical-realization DPC grammar, not absolute
minimality across every possible physical constructor language.

The detector-support frontier already has a source-neutral combinatorial
obstruction. Let the bipartite support graph join a harmonic coordinate to a
port whenever that port has a nonzero coefficient on the coordinate. To retain
rank after every three-port deletion, every nonempty coordinate set \(T\) must
satisfy the robust Hall condition

\[
|N(T)|\ge |T|+3.
\]

Taking \(|T|=1\) shows that each of the 21 harmonic coordinates must feed at
least four ports. Hence every admissible architecture has at least 84
mode-port incidences. With only 24 ports, at least one port must couple to at
least four modes. An architecture in which every port accesses at most three
modes has at most 72 incidences and is impossible, independently of coefficient
values. Robust Hall support is only necessary: satisfying it does not prevent
algebraic cancellations or by itself construct a full-spark encoder.

The incidence lower bound is nevertheless attainable. Give harmonic
coordinate \(c\) support on the four consecutive ports
\(c,c+1,c+2,c+3\). This interval graph has exactly 84 incidences and maximum
port width four. A deterministic integer coefficient assignment recorded in
the contract was tested against all 2024 three-port deletion patterns. Every
retained determinant is nonzero modulo the prime \(1000000007\), which proves
that every corresponding integer determinant is nonzero. Thus width four is
sufficient for exact three-erasure recovery for at least one coefficient
choice.

This sparse fixture is not Parseval and has no certified uniform conditioning.
Whitening its columns would generally mix harmonic coordinates and destroy the
width-four support. The result therefore separates two design problems:
minimal locality for exact distinction preservation, and dense tight-frame
optimization for quantitative stability.

For the recorded integer fixture, column normalization preserves support and
rank but yields full condition approximately \(38.54\) and worst three-port
deletion condition approximately \(7.79\times10^6\), at deletion set
\((13,20,21)\). Exact recoverability is therefore an extremely weak stability
certificate here.

The interval support pattern also has an exact Parseval obstruction. Columns
\(c\) and \(c+3\) overlap in exactly one port. Full-spark support requires both
coefficients on that overlap to be nonzero, so the columns cannot be
orthogonal. Principal column whitening makes all 504 entries numerically
nonzero in this fixture. This obstruction concerns the consecutive interval
pattern; it does not prove that every width-four support graph forbids a
Parseval realization.

Single overlaps are not the only obstruction. A second 84-incidence graph
uses two common ports together with the edges of a path on the remaining 22
ports. Every set of \(t\) path edges touches at least \(t+1\) vertices, so the
common core raises the union to at least \(t+3\) ports. It therefore satisfies
the same robust Hall law, and a deterministic integer coefficient assignment
again has all 2024 retained determinants nonzero modulo \(1000000007\).

This graph has no column pair intersecting in exactly one port. Its normalized
worst deletion condition improves to approximately \(2.13\times10^5\), still
far from the dense candidate's \(238.41\). Parsevality nevertheless remains
impossible for the support pattern: choose three disjoint path edges. Their
columns have disjoint private support and meet only on the two common ports.
Orthogonality would require their three nonzero common-core restrictions to be
pairwise orthogonal in \(\mathbb R^2\). This is impossible. Thus eliminating
single overlaps is necessary for this search but not sufficient.

## Operational metric authority

Ordinary Euclidean condition numbers do not yet authorize a physical ranking
of the dense and sparse architectures. A typed operational metric requires a
signal norm \(G\), port-noise covariance \(\Sigma\), fault weight \(\pi(S)\),
detector coupling cost, decoder resource class, and spatial locality geometry.
For retained port set \(R\), the corresponding information operator is

\[
G^{-1/2}E_R^T\Sigma_R^{-1}E_RG^{-1/2}.
\]

Its minimum eigenvalue is invariantly meaningful only after \(G\) and
\(\Sigma\) have source authority. The current packet authorizes neither the
harmonic Euclidean norm as physical energy nor independent isotropic port
noise. It also does not authorize uniform weighting of all deletion triples.

Four additional hostile fixtures reject those assumptions and reject the claim
that digital inverse-Gram preconditioning erases analog noise amplification.
Preconditioning may change reconstruction coordinates, but it cannot restore
signal-to-noise information already suppressed by the measurement map. The
DPC comparison frontier therefore includes an operational-metric authority
grant alongside realization, calibration, fault, and detector-support grants.

Metric selection must precede encoder selection. Otherwise every full-rank
candidate can be declared tight after the fact by choosing

\[
G=E^TE.
\]

That maneuver erases the comparison rather than explaining it. The compiler
therefore requires one source-declared metric shared by all candidates and
rejects candidate-fitted whitening. Under an invertible harmonic-coordinate
change \(x'=Sx\), the covariant transformation

\[
E'=ES^{-1},
\qquad
G'=S^{-T}GS^{-1}
\]

preserves the generalized information spectrum. Ordinary condition number
need not be preserved. The checker replays this covariance explicitly on the
sparse tree-core fixture.

The source artifacts do provide one canonical benchmark and one important
obstruction. Orthonormal spherical harmonics give the static low block its
mathematical angular \(L^2\) coefficient metric. Bondi news energy instead
acts on histories. For

\[
C(u,\Omega)=\sum_i c_i f_i(u)Y_i(\Omega),
\]

angular orthogonality gives

\[
\|N\|^2
=
\sum_i |c_i|^2\int |f_i'(u)|^2du.
\]

The weights depend on the temporal profiles and vanish for stationary modes.
Indeed, the entire 21-dimensional time-independent low block has zero news
energy. News energy is therefore a positive-semidefinite history seminorm, not
an invertible norm on the static coefficient packet. An invertible physical
metric would require a declared temporal-profile class with a positive weight
floor or an additional boundary/soft norm. Neither is currently authorized.

## Static distinction authority

Zero news energy does not make the 21 static coefficients observationally
null. In the declared weak radiative phase space, complete local shear tests
and the low-harmonic coefficient ports separate every pair of low-block
states. The exact-form gauge quotient removes exact one-form presentations,
not nonzero coexact magnetic modes. Conservation restricts source charges at
\(l=0,1\), and antipodal matching transports the \(l=2,3,4\) coefficients by
an invertible map. None of those arrows erases the low block.

The first relevant nonfaithful arrow is the grade-three readout itself. Its
21-dimensional kernel cannot be promoted to blindness of every observable.
Likewise, a no-magnetic endpoint policy may exclude static endpoint records,
but it is additional boundary authority and does not exclude returning
low-mode histories. Time-resolved shear or news ports detect those histories.

Accordingly the 21 inputs have contextual distinction authority before an
optional endpoint or observable-algebra quotient. Four hostile fixtures reject
promotion of grade-three blindness to universal nullity, zero energy to gauge,
endpoint exclusion to history exclusion, and invertible antipodal matching to
an aliasing sum.

## Interface-selection authority

The grade-three operator is an authorized mathematical constructor: it is the
paired magnetic fourth-order incidence port, continuous on the declared
functional scales and Fredholm on every Sobolev level. No source artifact,
however, identifies it as an unavoidable physical observer interface.

Direct low-harmonic coefficients, complete local shear tests, and some lower
derivative grades already detect the missing modes. The packet declares no
observer class, accessible field region, derivative-grade restriction,
angular-integration constraint, endpoint/history access rule, or comparative
cost that removes those alternatives. Therefore a kernel in the selected
grade-three channel does not establish universal need for a repair.

The 21-port augmentation is mathematically minimal once that interface is
selected. The 24-port construction is a conditional fault-tolerant bypass
design. Neither rank minimality nor mathematical bypass authority proves that
the redundant instrument is physically optimal or executable. Four hostile
fixtures enforce these distinctions, and interface-selection authority is now
an explicit member of the DPC completion frontier.

## Programme disposition

The encoder-optimization lane is conditionally closed pending new authority,
not pending a better numerical frame. The intrinsic results remain in force:
the completed magnetic low block has dimension 21, grade three loses exactly
that block, direct low-harmonic ports restore faithfulness, and the modes are
contextually distinguishable before optional endpoint reduction. The exact
encoder, decoder, realization-radius, and sparse-support theorems also remain
valid as conditional mathematics.

What is suspended is physical promotion. A new condition-number record alone
does not reopen the lane. Reopening requires a source-derived grade-three
interface selection, a physical fault grammar, and an operational metric. This
disposition prevents an optional coding construction from displacing the
intrinsic magnetic kernel and boundary-observable questions.

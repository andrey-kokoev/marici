# Connected vertex source frontier for Deutschean completion

Status: bounded successor packet. The predecessor
`deutschean-primitive-cumulant-completion-explanation.md` is frozen as the
programme background. This packet owns only the live connected-decoration
problem.

## Bounded question

For the oriented inverse response, write

\[
v=z\exp W(s,v),
\qquad s=q-4.
\]

Can the coefficients of the connected vertex source \(W\) be derived from
the Gamma carrier as nonnegative local decoration weights at every grade?

This is the remaining coefficient-side theorem. If

\[
W\in w\mathbb Q_{\geq0}[s][[w]],
\]

then Lagrange inversion places \(v\) in the oriented positive cone, and the
relative-curvature formula transports that cone to the margin. Continuous
Borel--Laplace control remains a separate theorem.

## Exact bounded evidence

The parameterized checker reconstructs the response through normal grade 60,
forms the unique implicit constructor, and logarithmically extracts \(W\)
through vertex grade 30. It finds no negative coefficient.

The first subleading connected-source diagonal is

\[
[s^{n-1}w^n]W=1
\]

for every reconstructed \(n\geq3\). It is not proved by the Cayley face.
Indeed, under the highest-shape scaling \(w=T/s\),

\[
W(s,T/s)
=T+\frac{H_1(T)}s+O(s^{-2}),
\]

where the Cayley theorem fixes only the leading term \(T\). The reconstructed
first correction is

\[
H_1(T)=2T+\frac{11}{4}T^2+\frac{T^3}{1-T}.
\]

Thus the constant diagonal belongs to the one-loop or first subleading
saddle sector and still requires a source derivation. The earlier statement
that the Cayley theorem proved this diagonal is withdrawn.

The next diagonal has a stronger finite-difference law. For every tested
\(4\leq n\leq30\),

\[
[s^{n-2}w^n]W
=\frac{5n^3+10n^2+175n-198}{48}.
\]

Equivalently, its third forward difference is the constant \(5/8\). The
formula is reconstructed from \(n=4,5,6,7\) and verified on the 23 withheld
grades \(8\leq n\leq30\). It is therefore a sharp bounded theorem, not yet an
all-orders source derivation.

The same test extends by decoration deficit. Put

\[
c_{n,d}=[s^{n-1-d}w^n]W.
\]

For every \(0\leq d\leq5\), exact reconstruction gives

\[
\deg_n c_{n,d}=3d,
\qquad n\geq d+3.
\]

The polynomial for deficit \(d\) is reconstructed from \(3d+1\) consecutive
grades and tested on every remaining grade through 30. At \(d=5\), seven
grades remain withheld and all agree. The first nontrivial cases are

\[
c_{n,1}
=\frac{5n^3+10n^2+175n-198}{48},
\]

\[
c_{n,2}
=\frac{
4n^6+28n^5+580n^4-795n^3+8356n^2-30283n+22680
}{1440}.
\]

This is evidence for a triangular finite-width transport in subleading
decoration order: each additional order raises the placement degree by three,
and its stable law begins after one further initialization grade. It is not
yet the transport theorem because interpolation does not identify the
source-local state or transition map.

The natural placement basis is positive. For every tested deficit,

\[
c_{n,d}
=\sum_{k=0}^{3d}A_{d,k}
\binom{n-d-3}{k},
\qquad A_{d,k}>0.
\]

For example,

\[
c_{n,1}
=\frac{491}{24}
+\frac{95}{8}\binom{n-4}{1}
+\frac{85}{24}\binom{n-4}{2}
+\frac58\binom{n-4}{3}.
\]

Thus positivity is not produced by cancellation among monomials in \(n\).
Each stable deficit sector is a positive weighted sum of finite
attachment-choice spaces. The Newton coefficients \(A_{d,k}\) are candidate
local decoration weights. The source derivation must identify the underlying
attachments; their positivity alone does not confer source authority.

## Propagator form of the deficit transport

The Newton basis is the natural saddle basis. Set \(m=n-d-3\) and form the
stable deficit generating function

\[
G_d(T)=\sum_{m\geq0}c_{m+d+3,d}T^m.
\]

The positive Newton expansion is equivalent to

\[
G_d(T)
=\sum_{k=0}^{3d}\frac{A_{d,k}}{(1-T)^{k+1}},
\qquad A_{d,k}>0.
\]

The denominator is not fitted notation. In the highest-shape source saddle,
the quadratic fluctuation operator has inverse

\[
\frac1{1-T},
\]

because the saddle equation is \(T=ze^T\). Hence each Newton basis element
is a power of the source-derived saddle propagator. The observed degree-
\(3d\) law says that indexed subleading order \(d+1\) reorganizes into no
more than \(3d+1\) propagator powers after its initialization terms are
separated.

This resembles the generic one-dimensional connected saddle expansion, in
which each additional asymptotic order introduces finitely many Gaussian
propagators. It is not yet derived from that expansion: the unusually low
first-correction pole order shows that source-specific cancellations and the
inverse-response transform matter. Logarithmic connectedization and implicit
reversion must be carried through explicitly before the \(3d+1\) bound is a
theorem.

This explains the finite width and the choice of basis, but one sign theorem
is still missing. Ordinary saddle diagrams can carry alternating symmetry and
derivative signs. The source theorem must show that after the oriented
normal-coordinate reversal and the fixed-section Ward factor, all connected
weights collected into \(A_{d,k}\) are nonnegative. The exact positive values
for \(d\leq5\) are evidence for that cancellation-free reorganization, not a
proof of it.

## Interpretation

Decoration deficit zero contains exactly one connected primitive type per
grade. Deficit one has cubic multiplicity. A cubic law is consistent with one
marked local defect carrying three independent placement statistics on a
rooted source tree. This is a proposed combinatorial interpretation, not yet
an identification: the source constructor must produce the marking and its
weight before this language is promoted.

The next derivation should expand the highest-shape Gamma saddle one order
beyond the Cayley face. It must first recover
\(H_1(T)=2T+11T^2/4+T^3/(1-T)\). The following order must yield the displayed
cubic diagonal. Repeating by powers of \(q^{-1}\) should then produce a
triangular recurrence by subleading decoration order.

## Exact source saddle before expansion

The required expansion has a particularly small source presentation.  Put

\[
t=-\frac zq,
\qquad x=qy.
\]

After combining the carrier with the Gamma density, the exponent and
amplitude separate exactly as

\[
Z_q(-z/q)
=\text{(normalization)}
\int_0^\infty e^{qf(y,z)}a(y,z,q)\,dy,
\]

\[
f(y,z)=\log y+\frac{e^{-zy}-1}{z},
\qquad
a(y,z,q)=e^{-9zy/4}
\left(1+\frac{3z e^{zy}}{2q}\right).
\]

This identity retains the two pieces that a bare Cayley argument discards:
the source amplitude \(e^{-9zy/4}\) and its explicit \(q^{-1}\) correction.
They are therefore the first possible origin of the connected correction
\(H_1\).

The saddle equation is

\[
\partial_y f=0
\quad\Longleftrightarrow\quad
y=e^{zy}.
\]

Writing \(T=zy\) gives \(T=ze^T\), while the normalized quadratic operator is

\[
-y^2\partial_y^2f=1-T.
\]

Hence \((1-T)^{-1}\) is source-derived before any coefficient fitting.  The
next gate is now exact and local: perform the connected Laplace expansion of
this displayed pair \((f,a)\), apply the fixed-\(t\) adjacent-grade response,
and only then carry out implicit reversion.  Success means recovering
\(H_1\) from the amplitude and Gaussian fluctuation terms separately.  A
failure at that gate would show that the observed propagator law is a
coordinate shadow rather than a constructor theorem.

The first connected Laplace coefficient can already be evaluated exactly.
Let \(h=1-T\). The explicit amplitude correction, amplitude curvature,
mixed amplitude--cubic term, quartic vertex, and paired cubic vertices give

\[
\frac{3T}{2}
+\frac{81T^2}{32h}
-\frac{9T(2-T^2)}{8h^2}
+\frac{T^3-6}{8h^2}
+\frac{5(2-T^2)^2}{24h^3}.
\]

They collapse to

\[
\frac{T^4-66T^3+53T^2-8}{96(T-1)^3}.
\]

The \(-1/(12q)\) Stirling term from the Gamma normalization then yields the
normalized one-loop coefficient

\[
S_2(T)=
\frac{T(T^3-74T^2+77T-24)}{96(T-1)^3}.
\]

Two structural facts are exact: \(S_2(0)=0\), as required by zero-source
normalization, and no propagator power above three occurs. This is the first
source-side explanation of the observed three-units-per-order width. It is
not yet the diagonal theorem: the fixed-\(t\) adjacent-grade difference and
implicit reversion can still cancel, raise, or reorient these terms.

At the first response order that remaining transport can be done in closed
form. Let

\[
\mathcal E=z\partial_z=\frac{T}{1-T}\partial_T.
\]

The saddle action and determinant--amplitude term are

\[
S_0=1+T+T^{-1}-e^T/T,
\qquad
S_1=-\frac54T-\frac12\log(1-T).
\]

Fixed-\(t\) differentiation gives

\[
A_0=S_0+\mathcal E S_0=T,
\qquad
1+\mathcal E A_0=\frac1{1-T}.
\]

The identity term here is part of the source definition of the normalized
adjacent response \(qd=1+q(\partial_q\ell_q-\partial_q\ell_{q-1})\); it is not
a normalization fitted after the saddle calculation.

Expanding the adjacent grade at
\(q-1\) and \(z(1-q^{-1})\), the next coefficient of \(qd\) is

\[
Q_1=-\frac{T^2(7T^2-19T+8)}{4(T-1)^4}.
\]

Consequently the scaled response \(V=qv\) has

\[
V=T+q^{-1}V_1+O(q^{-2}),
\qquad
V_1=-\frac{T^2(7T^2-19T+8)}{4(T-1)^2}.
\]

Finally one must convert from \(q\) to \(s=q-4\) and from \(V\) to the
implicit connected coordinate. That conversion gives

\[
H_1(T)=\left(T^{-1}-1\right)V_1+4T
=2T+\frac{11}{4}T^2+\frac{T^3}{1-T}.
\]

Thus the first subleading connected-source diagonal is now source-derived.
In particular, the coefficient of \(T^n\) in \(H_1\) is one for every
\(n\geq3\), proving

\[
[s^{n-1}w^n]W=1
\qquad(n\geq3)
\]

at all grades. The correction recorded above is therefore resolved: Cayley
supplies the leading face, while the determinant--amplitude response supplies
the first connected diagonal.

## Hard-to-vary test

There is a natural two-parameter hostile family that preserves the phase and
therefore preserves the Cayley saddle:

\[
F_{b,c}(t,x)
=\left(e^{tx}-ct\right)e^{btx}
\exp\left[-\frac{e^{tx}-1-tx}{t}\right].
\]

Repeating the first-response transport without specializing \(b\) or \(c\)
gives

\[
H_1^{(b,c)}(T)
=\left(\frac92-2b\right)T
+\left(b+\frac32\right)T^2
+\frac{T^3}{1-T}.
\]

This separates initialization from continuation. The dressing exponent
\(b\) changes only the grade-one and grade-two weights. The explicit atom
\(c\) does not occur at this order; it first enters the next Laplace
coefficient. Neither can vary the infinite unit tail while the source phase
is held fixed.

The answer to the first hard-to-vary question is therefore stronger than
expected: the repeatable attachment is the tree-saddle Jacobian itself. The
tail

\[
\frac{T^3}{1-T}
\]

is universal throughout the phase-preserving family, whereas the two finite
initialization weights remember the dressing. To destroy the unit tower one
must alter the primitive exponential phase, not merely its finite amplitude
decoration. The next hostile family should consequently deform
\(e^{tx}-1-tx\) while preserving zero-source normalization and test which
phase deformations retain a one-step continuation law.

The first phase-normal deformation can also be evaluated. Add
\(\kappa(tx)^2\) inside the primitive numerator. It preserves zero-source
normalization but changes the saddle map to

\[
z=Te^{-T}-2\kappa T^2.
\]

At fixed leading connected coordinate, the first variation of \(H_1\) is

\[
-\frac{Te^T}{T-1}
\left(
2bT^4+T^4+2bT^3+10T^3-10bT^2-9T^2
+2bT-22T+4b+26
\right).
\]

This is not confined to initialization: it has infinitely many nonzero tail
coefficients. At the physical value \(b=5/4\), its \(T^3\) and \(T^4\)
coefficients are respectively \(17\) and \(41/12\). Thus the phase-normal
direction genuinely changes continuation, while the amplitude blade changes
only finite initialization data. In Clifford language, the response is flat
along the amplitude blade but curved in its phase-normal direction.

The quadratic fixture is the first value of a general linearized phase
operator. For a normalized primitive perturbation \(g(T)=O(T^2)\), direct
differentiation gives

\[
\delta_gH_1
=-\frac{Te^T}{2(T-1)}\mathcal L_b[g],
\]

where

\[
\begin{aligned}
\mathcal L_b[g]={}&(T-T^2)g^{(4)}\\
&+(2bT^3+T^3-4bT^2+4T^2+2bT-14T+11)g^{(3)}\\
&+(4bT^3+2T^3-6bT^2+13T^2-2bT-37T+4b+26)g''\\
&+(2bT^3+T^3-2bT^2+8T^2-4bT-22T+4b+15)g'.
\end{aligned}
\]

The monomial symbols are individually nonzero. At the physical value
\(b=5/4\), a perturbation \(a_2T^2\) contributes \(31a_2T\) at its first
response grade. For \(m\geq3\), a monomial \(a_mT^m\) contributes

\[
\frac{m(m-1)(m-2)(m+8)}2a_mT^{m-2}.
\]

Every displayed multiplier is nonzero, but this does not imply injectivity.
The \(T^2\) and \(T^3\) inputs both reach response grade one: their endpoint
observations collide. Solving the resulting recurrence reveals a
one-parameter formal kernel. With primitive normalization its beginning is

\[
g_{\mathrm{null}}(T)
=33T^2-31T^3+\frac{273}{16}T^4-\frac{731}{104}T^5
+\frac{61429}{24960}T^6-\cdots.
\]

The checker solves this null jet through \(T^9\) and verifies zero response
through grade seven. Thus the phase normal is curved but not faithfully
observed by \(H_1\) alone. There is a distinguished phase-gauge direction
whose effect first disappears through a genuine integral circuit
\((33,-31)\), then propagates by a rational recurrence.

This correction is structurally important. The first connected response is
one observation port, not the whole source. Faithful reconstruction requires
either the next connected saddle response or an independent phase-sensitive
port. The next gate is to test whether the null jet survives in \(H_2\); if it
does not, the pair \((H_1,H_2)\) is the minimal jointly faithful phase
instrument.

The dimension of this kernel is itself source-controlled. Put \(h=g'\) in
\(\mathcal L_{5/4}[g]=0\). At \(T=0\) the regular-singular leading terms are

\[
Th'''+11h''
\]

plus terms of lower derivative order.

For \(h\sim T^\rho\), the indicial polynomial is

\[
\rho(\rho-1)(\rho+9).
\]

The root \(\rho=0\) corresponds to an unauthorized linear primitive term,
which changes the zero-source base law. The root \(\rho=-9\) is singular.
Only \(\rho=1\) lies in the normalized analytic class \(g=O(T^2)\).
Consequently the formal kernel is exactly one-dimensional, rather than an
accidental bounded nullspace. Its primitive jet above is the canonical
coordinate of that phase-gauge line.

## Falsifiers

The route fails if any of the following occurs:

- a coefficient of \(W\) is negative;
- a fixed decoration-deficit diagonal has no finite source recurrence;
- the saddle correction disagrees with the reconstructed cubic diagonal;
- positivity holds only after implicit reversion and has no connected
  Gamma-atom interpretation.

The last failure is especially important: canonical reversion alone is an
explanation-inert coordinate change.

## Verification

The checker
`research/strominger/checkers/deutschean_connected_vertex_diagonals.py`
reads the order-30 hostile result and verifies the exact diagonal laws,
including the withheld-grade test. Its result is
`research/strominger/results/deutschean_connected_vertex_diagonals.json`.

The independent checker
`research/strominger/checkers/deutschean_source_saddle_one_loop.py` derives
the five one-loop terms and verifies their collapse, Gamma normalization,
zero-source value, and cubic propagator bound. Its result is
`research/strominger/results/deutschean_source_saddle_one_loop.json`.

## Second connected port

The next adjacent-grade expansion initially appeared to disagree with the
exact coefficients. The residual was a spurious quadratic Taylor term. The
leading connected map is exactly \(W_0(T)=T\), so \(W_0''=0\); removing that
term gives

\[
H_2(T)=
\frac{T^2(146T^5-425T^4+248T^3+536T^2-866T+391)}
{48(T-1)^4}.
\]

Its beginning is

\[
H_2(T)=
\frac{391}{48}T^2+
\frac{349}{24}T^3+
\frac{491}{24}T^4+
\frac{97}{3}T^5+
\frac{191}{4}T^6+\cdots,
\]

which agrees with the independently reconstructed connected source. For
every \(n\geq4\), partial fractions give

\[
[T^n]H_2
=\frac{5n^3+10n^2+175n-198}{48}.
\]

Thus the deficit-one cubic diagonal is now an all-grades saddle theorem. The
fourth-order pole at \(T=1\) explains the cubic placement law directly. The
remaining categorical test is separate: linearize this second port under the
primitive-phase deformation and evaluate it on \(g_{\mathrm{null}}\).

That test is already decisive at the first available grade. Retaining the
variation of the deformed leading-coordinate curvature gives

\[
D H_2(g_{\mathrm{null}})
=-\frac{1065}{2}T^2+O(T^3).
\]

The coefficient is stable when the truncation is raised by one grade. Hence
the canonical \(H_1\)-null line is not a source equivalence: it is detected by
the second connected port. Within the normalized primitive-phase tangent
space, \((H_1,H_2)\) is therefore jointly faithful because \(H_1\) has exactly
that one-dimensional kernel and \(H_2\) is nonzero on its generator.

The bounded checker
`research/strominger/checkers/deutschean_h2_phase_null_probe.py` verifies the
undeformed leading \(T^2\) coefficient before testing the null jet. Higher
baseline coefficients are verified by the independent all-grades checker,
not by this deliberately short variation jet. Its result is
`research/strominger/results/deutschean_h2_phase_null_probe.json`.

The same pair also separates the two finite amplitude directions. In the
phase-preserving family,

\[
\partial_bH_1=T(T-2),
\qquad
\partial_cH_1=0,
\qquad
\partial_cH_2=T^2(3-2T).
\]

The corresponding two-port amplitude Jacobian has determinant

\[
-T^3(T-2)(2T-3),
\]

which is a nonzero formal series. Thus \(H_1\) observes the dressing exponent,
while \(H_2\) supplies the missing explicit-atom port. This proves faithfulness
on the two-dimensional amplitude tangent plane. It does not yet exclude a
mixed phase--amplitude cancellation; that requires the joint block kernel,
not separate restrictions to the phase and amplitude summands.

An earlier mixed-block computation omitted the deformation of the explicit
amplitude atom. Under phase deformation the saddle map changes, so that term
is \(cze^T/q\), not \(cT/q\). The old rank-two matrix and its vector
\((1/99,3/2,1)\) are therefore withdrawn. The deterministic retirement check
is `research/strominger/checkers/deutschean_h2_mixed_block_rank.py`, with
result `research/strominger/results/deutschean_h2_mixed_block_rank.json`.

The formerly proposed circuit still has a useful closed form:

\[
g_{\mathrm{mix}}(T)
=\frac23\left[1-(1+T)e^{-T}\right],
\qquad
\delta b=\frac32,
\qquad
\delta c=1.
\]

Substitution into the untruncated saddle transport gives

\[
D H_1(g_{\mathrm{mix}},\delta b,\delta c)=0,
\qquad
D H_2(g_{\mathrm{mix}},\delta b,\delta c)=2T^2(T^2-2).
\]

Thus it is an exact \(H_1\) alias but not a joint \((H_1,H_2)\) alias. The
second port already detects the direction at grade two.

The corrected joint statement is stronger. Write a normalized analytic phase
jet as

\[
g(T)=\sum_{m\geq2}a_mT^m
\]

and include the two amplitude tangents \(\delta b,\delta c\). The coefficients
of \(DH_1\) at grades one through four together with those of \(DH_2\) at
grades two through four give a square linear system on

\[
(a_2,a_3,a_4,a_5,a_6,\delta b,\delta c).
\]

Its exact determinant is

\[
-205301174400.
\]

Therefore every joint-kernel element has these seven coordinates equal to
zero. For each \(m\geq7\), the next unused \(H_1\) coefficient determines
\(a_m\) with multiplier

\[
\frac{m(m-1)(m-2)(m+8)}2,
\]

which never vanishes. Induction forces the entire phase tail to zero. Hence
\((H_1,H_2)\) is jointly faithful on the full normalized analytic
primitive-phase tangent space plus both amplitude tangents. The exact initial
block checker is
`research/strominger/checkers/deutschean_h1_h2_mixed_faithfulness.py`, with
result
`research/strominger/results/deutschean_h1_h2_mixed_faithfulness.json`.

This tangent theorem upgrades to formal local faithfulness without assuming a
Banach inverse theorem. Let \(X(\epsilon)\) and \(Y(\epsilon)\) be normalized
source arcs through the physical source in the separated \(\epsilon\)-adic
completion, and suppose their two readouts agree. If the arcs differ, let
\(r\) be their first unequal order and write

\[
X(\epsilon)-Y(\epsilon)=\epsilon^r v+O(\epsilon^{r+1}).
\]

Because all lower orders agree, the coefficient of \(\epsilon^r\) in the
readout difference is exactly

\[
D(H_1,H_2)_{X_0}v.
\]

The joint tangent theorem forces \(v=0\), contradicting the definition of
\(r\). Thus equal \((H_1,H_2)\) readout arcs have identical formal source
arcs. This is a first-difference theorem, not a global inverse theorem. It
does not identify distant finite sources, control convergence, or distinguish
smooth arcs whose difference is flat at \(\epsilon=0\).

The compiler check and its hostile zero-differential example are in
`research/strominger/checkers/deutschean_formal_arc_faithfulness.py`, with
result
`research/strominger/results/deutschean_formal_arc_faithfulness.json`.

The direct Banach upgrade fails in the naive same-radius analytic coefficient
norm. For the monomial phase perturbation \(g_m(T)=T^m\), the principal H1
response contains

\[
\lambda_mT^{m-2},
\qquad
\lambda_m=\frac{m(m-1)(m-2)(m+8)}2.
\]

If \(\|T^m\|_R=R^m\), the operator-norm ratio has the lower bound

\[
\frac{\lambda_mR^{m-2}}{R^m}=\frac{\lambda_m}{R^2},
\]

which diverges quartically. Hence the ordinary analytic coefficient space is
not the correct common domain and codomain for an inverse-function argument.

Two honest repairs are visible. Passing from radius \(R\) to a smaller radius
\(r\) replaces the ratio by

\[
\frac{\lambda_m}{R^2}\left(\frac rR\right)^{m-2},
\]

which is bounded for \(r<R\). Alternatively, at fixed radius the target can
carry the principal graph weight \(R^m/\lambda_m\) at response grade \(m-2\).
Neither repair is yet a completed analytic theorem: the lower-order triangular
terms and nonlinear saddle substitutions must be bounded in the same chosen
scale. The hostile checker is
`research/strominger/checkers/deutschean_analytic_norm_hostile.py`, with result
`research/strominger/results/deutschean_analytic_norm_hostile.json`.

The fixed-radius repair has a natural source space. For

\[
g(T)=\sum_{m\geq2}a_mT^m,
\]

define

\[
\|g\|_{X_R}=\sum_{m\geq2}|a_m|(1+m)^4R^m.
\]

The weight is submultiplicative because

\[
1+i+j\leq(1+i)(1+j).
\]

Thus \(X_R\) is a weighted Wiener algebra. For \(m\geq3\), the principal
multiplier obeys the coarse uniform comparison

\[
\frac9{256}(1+m)^4
\leq \lambda_m
\leq \frac{11}{6}(1+m)^4.
\]

Consequently the shifted principal H1 operator is bounded above and below
between \(X_R\) and the ordinary readout Wiener space, up to the fixed factor
\(R^{-2}\). Its inverse is bounded in the opposite direction. The base saddle
denominators are also controlled for \(0<R<1\):

\[
\|(1-T)^{-1}\|_R=\frac1{1-R},
\qquad
\|e^{\pm T}\|_R=e^R.
\]

This identifies the appropriate analytic constructor. The remaining linear
gate is quantitative: split the H1 differential into its shifted diagonal and
strict triangular remainder, then find \(R>0\) for which the conjugated
remainder has norm below one. The finite seven-coordinate determinant handles
the initial block; a Neumann estimate would handle the tail. Only after that
bound may the analytic inverse theorem be invoked. The constructor checker is
`research/strominger/checkers/deutschean_weighted_wiener_constructor.py`, with
result
`research/strominger/results/deutschean_weighted_wiener_constructor.json`.

The tail gate closes with a deliberately coarse explicit radius. For a
monomial \(T^m\), factor the response as

\[
D H_1[T^m]
=T^{m-2}\frac{e^T}{2(1-T)}Q_m(T),
\]

where

\[
\begin{aligned}
Q_m(T)={}&m(m-1)(m-2)(m+8)\\
&-\frac{m(m-1)(2m^2+13m-96)}2T\\
&-\frac{m(2m^2+73m-115)}2T^2\\
&+\frac{m(7m^2-10m-51)}2T^3\\
&+\frac{m(14m-3)}2T^4+\frac{7m}{2}T^5.
\end{aligned}
\]

Dividing each coefficient by \((1+m)^4\), coarse absolute bounds are

\[
44, 109, 95, 34, \frac{17}{2}, \frac72.
\]

Use \(e^R\leq(1-R)^{-1}\) and the lower diagonal comparison
\(\lambda_m\geq9(1+m)^4/256\). At

\[
R=\frac1{10000},
\]

the conjugated strict-tail norm is bounded above by the exact rational number
recorded by the checker, approximately \(0.28018<1\). The tail is therefore
invertible by a Neumann series. Combined with the finite initial determinant,
the full differential of \((H_1,H_2)\) is a bounded isomorphism between the
weighted Wiener source space with two amplitude coordinates and the typed
readout space.

All source operations in the saddle formulas are analytic on a sufficiently
small neighborhood: the weighted Wiener space is a Banach algebra, and the
base reciprocal factors remain invertible for \(R<1\). The analytic inverse
function theorem now applies. Hence there is a convergent neighborhood of the
physical source in which \((H_1,H_2)\) is faithful and supplies analytic local
coordinates. The radius above controls the series variable; the neighborhood
size in source norm is existential and not yet optimized.

The exact tail certificate is
`research/strominger/checkers/deutschean_tail_neumann_bound.py`, with result
`research/strominger/results/deutschean_tail_neumann_bound.json`.

The algebraically extended positive quadratic family develops a fold on the
full interval \(0<T<1\). Set

\[
g(T)=T^2,
\qquad
z_k(T)=Te^{-T}-2kT^2.
\]

The saddle coordinate develops a caustic when

\[
z_k'(T)=e^{-T}(1-T)-4kT=0.
\]

Equivalently,

\[
k=\kappa(T)=\frac{e^{-T}(1-T)}{4T}.
\]

On \(0<T<1\), this function is positive and strictly decreasing because

\[
\frac{d}{dT}\log\kappa(T)
=-1-\frac1{1-T}-\frac1T<0.
\]

It runs from infinity to zero. Therefore every \(k>0\), however small,
creates a unique caustic somewhere in the unit interval. At that point

\[
z_k(T)=\frac{Te^{-T}(1+T)}2>0,
\]

so the failure is specifically \(z_k'=0\), equivalently the vanishing of the
normalized Hessian \(h=Tz_k'/z_k\), rather than collapse of the source
coordinate itself.

This is not a global readout collision. Within the extended family, the saddle
chart fails before global comparison can continue through it. The contour
audit below shows that this positive family is not admitted by the original
real Gamma cycle. The exact checker is
`research/strominger/checkers/deutschean_quadratic_phase_caustic.py`, with
result
`research/strominger/results/deutschean_quadratic_phase_caustic.json`.

The caustic is a simple fold, not a higher degeneration. On its critical
locus,

\[
z_k''(T)
=\frac{e^{-T}}T\left(T^2-T-1\right).
\]

The two roots of the polynomial factor are

\[
\frac{1-\sqrt5}{2},
\qquad
\frac{1+\sqrt5}{2},
\]

both outside \((0,1)\). Hence \(z_k''(T)<0\) throughout the physical caustic
locus. Locally,

\[
z-z_c
=\frac12z_k''(T_c)(T-T_c)^2+O((T-T_c)^3).
\]

The inverse saddle coordinate is therefore two-sheeted with square-root
branching. The Gaussian expansion fails because its Hessian vanishes, while
the next normal coefficient remains nonzero. This identifies the required
replacement type: any continuation of the original Gamma integral across the
fold must use a source-derived uniform fold, ordinarily an Airy constructor,
rather than either Gaussian branch separately.

The fold theorem does not yet authorize that Airy completion. Its contour,
normalization, and relation to \((H_1,H_2)\) must be derived from the original
integral. The exact classification checker is
`research/strominger/checkers/deutschean_quadratic_phase_fold.py`, with result
`research/strominger/results/deutschean_quadratic_phase_fold.json`.

The algebraically deformed Gamma phase fixes the local Airy normal form. For
the quadratic deformation it is

\[
f_k(y,z)
=\log y+\frac{e^{-zy}-1}{z}+kzy^2.
\]

At a caustic labelled by \(T_c\), the critical data are

\[
z_c=\frac{T_ce^{-T_c}(1+T_c)}2,
\qquad
y_c=\frac{2e^{T_c}}{1+T_c}.
\]

Direct differentiation gives

\[
f_y=f_{yy}=0,
\]

\[
A_c:=f_{yyy}
=\frac{e^{-3T_c}(1+T_c)^2(1+T_c-T_c^2)}4>0,
\]

and the transverse unfolding coefficient is unusually simple:

\[
B_c:=\partial_zf_y=\frac1{T_c}.
\]

Thus the local exponent has the source-derived form

\[
q(f-f_c)
=q\left(\frac{A_c}{6}(y-y_c)^3
+B_c(z-z_c)(y-y_c)+\cdots\right).
\]

With

\[
u=\left(\frac{qA_c}{2}\right)^{1/3}(y-y_c),
\]

the Airy argument is

\[
\xi
=-q^{2/3}(z-z_c)B_c\left(\frac2{A_c}\right)^{1/3}.
\]

The transition window therefore has width \(z-z_c=O(q^{-2/3})\), and a
compatible fold integral would carry \(q^{-1/3}\) scaling. These exponents and
normalization factors come from the algebraic phase formula, rather than from
a fitted catastrophe model. They do not by themselves authorize a contour.

What remains untyped is global: the positive-real contour must be transported
to steepest-descent cycles to determine the authorized Airy combination and
its Stokes multipliers. The exact local-data checker is
`research/strominger/checkers/deutschean_source_airy_fold_data.py`, with result
`research/strominger/results/deutschean_source_airy_fold_data.json`.

The original positive-real Gamma contour rejects the real fold family. The
large-\(y\) logarithm of the base integrand is

\[
qf_k(y,z)-\frac94zy.
\]

Its quadratic asymptotic coefficient is

\[
\lim_{y\to\infty}
\frac{qf_k(y,z)-9zy/4}{y^2}
=qkz.
\]

The second amplitude atom changes only the linear exponential rate, so it
cannot cancel this quadratic growth. For \(z,q>0\), the original contour is
therefore convergent in the quadratic direction only for \(k\leq0\). But the
interior real caustic requires

\[
k=\frac{e^{-T}(1-T)}{4T}>0.
\]

The two domains are disjoint. The fold and its Airy data are algebraically
describable but not constructible in the original real-contour source sector.
They become admissible only after an independently authorized contour
rotation, analytic continuation, or source amplitude with sufficient
quadratic decay. The exact contour audit is
`research/strominger/checkers/deutschean_quadratic_phase_contour_admissibility.py`,
with result
`research/strominger/results/deutschean_quadratic_phase_contour_admissibility.json`.

The admissible sign contains a different, genuine catastrophe beyond
\(T=1\). Write \(k=-\alpha\) with \(\alpha>0\). Then

\[
z_\alpha(T)=Te^{-T}+2\alpha T^2
\]

and a fold occurs for \(T>1\) when

\[
\alpha=\psi(T)=\frac{e^{-T}(T-1)}{4T}.
\]

The fold profile has a unique maximum because

\[
\psi'(T)
=-\frac{e^{-T}(T^2-T-1)}{4T^2}.
\]

Its critical point is the golden ratio

\[
\varphi=\frac{1+\sqrt5}{2},
\qquad
\alpha_*=rac{e^{-\varphi}}{4\varphi^2}.
\]

For \(0<\alpha<\alpha_*\), two folds occur beyond \(T=1\). At
\(\alpha=\alpha_*\), they merge. The saddle map then satisfies

\[
z_\alpha'=z_\alpha''=0,
\qquad
z_\alpha'''=e^{-\varphi}(3-\varphi)>0.
\]

This is a cusp of the saddle map. The phase classification is exact. At the
critical source,

\[
f_y=f_{yy}=f_{yyy}=0,
\qquad
f_{yyyy}\neq0.
\]

Moreover, the two controls \((z,\alpha)\) unfold the linear and quadratic
normal terms with determinant

\[
-2\varphi^2e^{-\varphi}\neq0.
\]

Thus the admissible negative quadratic sector contains a genuine two-control
quartic cusp. Its uniform local model is Pearcey-type, with amplitude scaling
\(q^{-1/4}\), one control scale \(q^{-1/2}\), and the other \(q^{-3/4}\) after
the source-derived linear recombination of \((z-z_c,\alpha-\alpha_*)\).

Unlike the positive quadratic Airy fold, this cusp lies inside the original
real-contour convergence domain. The remaining missing constructor is its
global positive-real Pearcey cycle and the induced continuation of the
connected readout ports. The exact cusp checker is
`research/strominger/checkers/deutschean_admissible_quadratic_cusp.py`, with
result
`research/strominger/results/deutschean_admissible_quadratic_cusp.json`.

At the admissible cusp the original integration cycle already selects the
uniform contour. The phase tends to minus infinity at both ends of the
positive-real \(y\)-axis, and the critical point lies in its interior. Put

\[
C_c=-f_{yyyy}(y_c,z_c,\alpha_*)>0
\]

and define

\[
u=\left(\frac{qC_c}{6}\right)^{1/4}(y-y_c).
\]

The positive-real contour maps locally to the real \(u\)-axis, and the
quartic term becomes \(-u^4/4\). If

\[
\ell=\delta f_y,
\qquad
a=\delta f_{yy}
\]

are the two source-derived control covectors, then

\[
Y=q^{3/4}\left(\frac6{C_c}\right)^{1/4}\ell,
\qquad
X=q^{1/2}\left(\frac6{C_c}\right)^{1/2}a.
\]

The leading uniform integral is therefore the real Pearcey-type cycle

\[
\int_{-\infty}^{\infty}
\exp\left(-\frac{u^4}{4}+\frac{Xu^2}{2}+Yu\right)du,
\]

multiplied by the positive source amplitude at the cusp and the Jacobian

\[
\left(\frac6{qC_c}\right)^{1/4}.
\]

No fitted Stokes choice is needed for the leading uniform model: the original
positive-real Gamma contour fixes the real Pearcey cycle. Stokes jumps arise
only if this fixed cycle is decomposed into separate saddle thimbles. The
remaining task is to compute uniform correction terms and define connected
readout ports that remain finite through the cusp. The exact cycle checker is
`research/strominger/checkers/deutschean_real_pearcey_cycle.py`, with result
`research/strominger/results/deutschean_real_pearcey_cycle.json`.

The uniform correction tower closes on three finite observation ports. Define

\[
P(X,Y)=\int_{-\infty}^{\infty}
e^{-u^4/4+Xu^2/2+Yu}\,du
\]

and moments

\[
M_n=\int_{-\infty}^{\infty}
u^n e^{-u^4/4+Xu^2/2+Yu}\,du.
\]

Integration by parts gives

\[
M_{n+3}=XM_{n+1}+YM_n+nM_{n-1}.
\]

Therefore every polynomial correction reduces to the three-port basis

\[
P,
\qquad
\partial_YP,
\qquad
\partial_Y^2P.
\]

Equivalently, the uniform carrier satisfies

\[
\partial_Y^3P=X\partial_YP+YP,
\qquad
\partial_XP=\frac12\partial_Y^2P.
\]

This replaces the divergent tower of separate Gaussian propagators by a
finite rank-three module that remains regular at the cusp. At \(X=Y=0\),

\[
P=\frac{\Gamma(1/4)}{\sqrt2},
\qquad
\partial_YP=0,
\qquad
\partial_Y^2P=\sqrt2\,\Gamma(3/4).
\]

Hence the connected mean vanishes by parity, while the connected variance is

\[
2\frac{\Gamma(3/4)}{\Gamma(1/4)}>0.
\]

The three ports are the natural finite replacement for singular Gaussian
readouts at the cusp. What remains is a matching theorem: away from the cusp,
their saddle asymptotics must reproduce the previously normalized \(H_1,H_2\)
ports and their source amplitude corrections. The exact closure checker is
`research/strominger/checkers/deutschean_pearcey_port_closure.py`, with result
`research/strominger/results/deutschean_pearcey_port_closure.json`.

The three ports match the ordinary saddle geometry on both sides of the cusp.
At \(Y=0\), the Pearcey exponent has stationary equation

\[
-u(u^2-X)=0.
\]

For \(X=-A\) with \(A\to\infty\), only \(u=0\) is real and maximal. Gaussian
rescaling gives

\[
P(-A,0)\sim\sqrt{\frac{2\pi}{A}},
\qquad
\frac{\partial_YP}{P}=0,
\qquad
\frac{\partial_Y^2P}{P}\sim\frac1A.
\]

For \(X=A\to\infty\), the two maxima are \(u_\pm=\pm\sqrt A\), each with
action \(A^2/4\) and Hessian \(-2A\). Thus

\[
P(A,0)\sim2\sqrt{\frac\pi A}e^{A^2/4}.
\]

A nonzero \(Y\) biases their actions by \(2Y\sqrt A\). At leading order the
branch-weight ratio is

\[
\frac{w_+}{w_-}=e^{2Y\sqrt A},
\]

and the normalized ports reconstruct

\[
\frac{\partial_YP}{P}
\sim\sqrt A\tanh(Y\sqrt A),
\qquad
\frac{\partial_Y^2P}{P}\sim A.
\]

Hence the rank-three uniform fiber retains both saddle branches and their
relative weight. Selecting one Gaussian saddle is an asymptotic quotient of
the Pearcey carrier, not additional source data. The remaining normalization
gate is narrower: include the full Gamma amplitude and adjacent-grade
operator, then verify that the one-branch expansion reproduces the existing
\(H_1,H_2\) formulas coefficient by coefficient. The exact leading matching
checker is
`research/strominger/checkers/deutschean_pearcey_gaussian_matching.py`, with
result
`research/strominger/results/deutschean_pearcey_gaussian_matching.json`.

The one-branch overlap reproduces the Gaussian propagator with exact uniform
corrections. Put \(X=-A\), \(Y=0\), and rescale \(u=v/\sqrt A\). Then

\[
P(-A,0)
=\frac1{\sqrt A}\int_{-\infty}^{\infty}
e^{-v^2/2}e^{-v^4/(4A^2)}\,dv.
\]

Expanding the quartic factor and using Gaussian moments gives

\[
P(-A,0)
\sim\sqrt{\frac{2\pi}{A}}
\left(
1-\frac{3}{4A^2}+\frac{105}{32A^4}
-\frac{3465}{128A^6}+\cdots
\right).
\]

The normalized second port becomes

\[
\frac{\partial_Y^2P}{P}
\sim\frac1A
\left(1-\frac3{A^2}+\frac{24}{A^4}+\cdots\right).
\]

Thus the ordinary Gaussian inverse Hessian \(A^{-1}\) is the leading face of
the finite Pearcey variance port, and its divergent higher propagator powers
are reorganized into a regular overlap expansion. Every coefficient is fixed
by the same real cycle through Gaussian moments; no matching constant is free.

This closes the universal part of the overlap. The remaining source-specific
calculation must expand the Gamma amplitude and adjacent-grade operator in the
same normal coordinate. The exact overlap checker is
`research/strominger/checkers/deutschean_pearcey_one_branch_overlap.py`, with
result
`research/strominger/results/deutschean_pearcey_one_branch_overlap.json`.

At the exact cusp, the first source-specific uniform correction has a parity
selection rule. After the quartic rescaling, the amplitude derivative and
the fifth phase derivative enter at relative order \(q^{-1/4}\), but both
multiply odd Pearcey moments and integrate to zero on the real cycle. The
first surviving correction is relative order \(q^{-1/2}\). It combines the
second amplitude derivative, the sixth phase derivative, and the square and
mixed products of the fifth derivative. Using

\[
M_6=3M_2,
\qquad
M_{10}=21M_2,
\]

the entire term reduces to the single variance port. The explicit \(q^{-1}\)
Gamma amplitude atom enters only two uniform orders later. The exact source
derivatives and correction coefficient are recorded by
`research/strominger/checkers/deutschean_cusp_first_uniform_correction.py`,
with result
`research/strominger/results/deutschean_cusp_first_uniform_correction.json`.

The fixed-\(t\) adjacent step also closes on the variance port. Since
\(z_{q-1}=z_q-z_q/q\), its leading shifts at the cusp are

\[
\Delta Y=y_1q^{-1/4},
\qquad
\Delta X=x_1q^{-1/2},
\]

where \(y_1,x_1\) are fixed explicitly by the source covectors
\(\partial_zf_y\) and \(\partial_zf_{yy}\). Acting on the uniform carrier gives

\[
e^{\Delta X\partial_X+\Delta Y\partial_Y}P.
\]

At the cusp, \(P_Y=0\), so the relative \(q^{-1/4}\) term vanishes. Using
\(P_X=P_{YY}/2\), the first surviving translation is

\[
\frac{x_1+y_1^2}{2}\,q^{-1/2}P_{YY}.
\]

Thus both the intrinsic uniform correction and the adjacent-grade translation
first appear at relative order \(q^{-1/2}\), and both occupy the same variance
port. The exact translation checker is
`research/strominger/checkers/deutschean_cusp_adjacent_translation.py`, with
result
`research/strominger/results/deutschean_cusp_adjacent_translation.json`.

Projectivizing the three linear ports produces exactly two connected ports:

\[
\mu=\frac{P_Y}{P},
\qquad
\nu=\frac{P_{YY}}P.
\]

The complete logarithmic adjacent response does not identify these cusp ports
with the legacy names \(H_1,H_2\).  Logarithmization sends the first relative
cusp correction to a nonzero term \(Cq^{-1/2}\nu\).  On a Puiseux monomial the
source-normalized adjacent operator acts as

\[
q\left(\partial_q q^{-1/2}-\partial_q(q-1)^{-1/2}\right)
=\frac34q^{-3/2}+O(q^{-5/2}).
\]

The identity in \(qd=1+q(\partial_q\ell_q-\partial_q\ell_{q-1})\) changes only
the grade-zero term.  It cannot remove this residual.  Both the intrinsic
uniform coefficient and the fixed-\(t\) translation coefficient are positive,
so their variance-port contributions cannot cancel.  The first complete cusp
residual is therefore

\[
\frac34(C_{\mathrm{intrinsic}}+C_{\mathrm{translation}})
q^{-3/2}\nu.
\]

This is an exact typing result: \(H_1\) and \(H_2\) occupy the integer slots
\(q^{-1}\) and \(q^{-2}\), whereas the quartic cusp creates a half-integral
Puiseux coset.  A Gaussian overlap chart may compare their coordinates away
from the cusp, but it does not supply source authority to rename \(\nu\) as
either \(H_1\) or \(H_2\).  The exact residual checker is
`research/strominger/checkers/deutschean_cusp_qd_normalization_residual.py`,
with result
`research/strominger/results/deutschean_cusp_qd_normalization_residual.json`.

The half-integral residual nevertheless has a canonical transition into the
Gaussian integer filtration.  In the overlap scaling put
\(A=\kappa q^{1/2}\).  On the one-saddle face,

\[
\nu\sim A^{-1}(1-3A^{-2}+24A^{-4}+\cdots),
\]

and therefore

\[
\frac34Cq^{-3/2}\nu
\sim\frac{3C}{4\kappa}q^{-2}+O(q^{-3}).
\]

The cusp residual first lands in the \(H_2\) filtration slot and has no
\(q^{-1}\) component there.  On the symmetric two-saddle face,
\(\nu\sim A\), so instead

\[
\frac34Cq^{-3/2}\nu
\sim\frac{3C\kappa}{4}q^{-1}.
\]

Thus one uniform variance port projects to different legacy orders on the two
faces: \(H_2\)-order for one saddle and \(H_1\)-order for two saddles.  This is
filtration compatibility, not equality of source-normalized coefficients.
Coefficient equality still requires the full amplitude and branch packet on
the chosen face.  The exact transition checker is
`research/strominger/checkers/deutschean_cusp_gaussian_filtration_transition.py`,
with result
`research/strominger/results/deutschean_cusp_gaussian_filtration_transition.json`.

Coefficient equality with the legacy \(H_1,H_2\) is not merely unproved; it is
ill-typed without an additional source morphism.  The quartic cusp belongs to
the deformed phase with \(\alpha=\alpha_*>0\).  On the saddle, quadratic
degeneracy is controlled by

\[
\frac{(T-1)e^{-T}}T-4\alpha.
\]

At the legacy specialization \(\alpha=0\), its only positive zero is \(T=1\).
There the cubic phase derivative equals \(e^{-3}\), so the legacy source has a
simple fold rather than a quartic cusp.  Forgetting \(\alpha\) therefore does
not preserve the singularity stratum, phase, or uniform carrier.

Consequently the branch-sensitive overlap is the strongest currently typed
adapter: it preserves filtration order but not source identity.  Promoting it
to coefficient equality would require a source-derived morphism preserving
phase, amplitude, contour, cusp stratum, and \(qd\) normalization.  No such
constructor is presently supplied.  One may instead derive new
\(H_1,H_2\)-analogues inside the full \(\alpha\)-family.  The exact no-go
checker is
`research/strominger/checkers/deutschean_cusp_legacy_source_adapter_no_go.py`,
with result
`research/strominger/results/deutschean_cusp_legacy_source_adapter_no_go.json`.

The first connected response can instead be derived inside the admissible
\(\alpha\)-family.  Its saddle map and normalized Hessian are

\[
z_\alpha(T)=Te^{-T}+2\alpha T^2,
\qquad
h_\alpha=\frac{4T\alpha e^T-T+1}{2T\alpha e^T+1},
\]

and fixed-\(t\) transport is

\[
\mathcal E_\alpha
=\frac{z_\alpha}{\partial_Tz_\alpha}\partial_T.
\]

Applying the same source-defined logarithm, \(qd\) identity, \(q\)-to-\(s\)
conversion, and implicit reversion gives an exact deformed first response
\(K_{1,\alpha}(T)\).  Its full rational-exponential expression is recorded in
the machine result.  It obeys

\[
K_{1,0}(T)=\frac{T(7T^2-3T-8)}{4(T-1)}=H_1(T).
\]

At \((T,\alpha)=(\varphi,\alpha_*)\), however, it has a simple pole:

\[
K_{1,\alpha_*}(\varphi+x)
=\frac{c_*}{x}+O(1),
\]

where

\[
c_*=-\frac{15(1+\sqrt5)(2+\sqrt5)(\sqrt5+3)}
{2(15+7\sqrt5)(\sqrt5+5)}\ne0.
\]

This supplies the source-specific relation that the legacy comparison could
not: the finite Pearcey variance port is the uniform completion of the
deformed Gaussian first-response coordinate at its simple pole.  It is not a
literal continuation of the finite legacy coefficient.  The exact checker is
`research/strominger/checkers/deutschean_deformed_first_connected_response.py`,
with result
`research/strominger/results/deutschean_deformed_first_connected_response.json`.

The second connected response also closes internally.  The deformed one-loop
coefficient is obtained directly from the five source terms

\[
\frac{3Ze^T}{2},\qquad
\frac{a''}{2aC},\qquad
\frac{a'f'''}{2aC^2},\qquad
\frac{f''''}{8C^2},\qquad
\frac{5(f''')^2}{24C^3},
\]

with \(Z=z_\alpha(T)\), \(C=-f''\), followed by the fixed Stirling correction
\(-1/12\).  Applying the second adjacent shift, logarithmic cumulant
subtraction, \(q\)-to-\(s\) conversion, and second implicit reversion produces
an exact \(K_{2,\alpha}(T)\), recorded in the machine result.  It satisfies

\[
K_{2,0}(T)=H_2(T)
\]

coefficient for coefficient.  At the admissible quartic cusp its leading
singularity is

\[
K_{2,\alpha_*}(\varphi+x)
=-\left(\frac76+\frac{21\sqrt5}{40}\right)x^{-5}+O(x^{-4}).
\]

Thus the first two deformed Gaussian ports have pole orders one and five,
while the rank-three Pearcey module remains finite.  The uniform carrier is
therefore completing a growing singular response hierarchy, not repairing a
single isolated coordinate.  No general pole-order law is yet asserted.  The
exact checker is
`research/strominger/checkers/deutschean_deformed_second_connected_response.py`,
with result
`research/strominger/results/deutschean_deformed_second_connected_response.json`.

The first two exact denominators separate the singular mechanism into two
source factors:

\[
F=4T\alpha e^T-T+1,
\qquad
G=2T^2\alpha e^T+2T\alpha e^T+2\alpha e^T-1.
\]

The first is the Hessian or caustic factor.  The second is the implicit
reversion factor, since

\[
\partial_TV_0=-\frac{G}{(2T\alpha e^T+1)^2}.
\]

At the cusp, \(F\) has order two and \(G\) has order one.  Grades one and two
fit the source-operator recurrence

\[
\operatorname{den}(K_n)\sim F^{3n-2}G^{2n-1},
\qquad
\operatorname{ord}_{\rm cusp}N_n=4n-2.
\]

If the increments continue without a new cancellation, then

\[
p_n=2(3n-2)+(2n-1)-(4n-2)=4n-3,
\qquad p_{n+1}=p_n+4.
\]

This reproduces \(p_1=1\) and \(p_2=5\) and predicts \(p_3=9\), with
denominator \(F^7G^5\) and numerator zero order ten.  The statement is a sharp
recurrence conjecture, not yet an all-grade theorem: an explicit \(K_3\)
calculation or a proof of the operator increments must rule out an additional
grade-three cancellation.  The exact valuation checker is
`research/strominger/checkers/deutschean_deformed_response_pole_recurrence.py`,
with result
`research/strominger/results/deutschean_deformed_response_pole_recurrence.json`.

The four-unit increment has an independent source explanation in connected
quartic diagrams.  For a standard Gaussian \(X\), the pure quartic sector is

\[
\log\mathbb E e^{\lambda X^4}
=\sum_{n\ge1}\frac{\kappa_n(X^4)}{n!}\lambda^n.
\]

Its first connected cumulants are

\[
\kappa_1=3,
\qquad
\kappa_2=96,
\qquad
\kappa_3=9504,
\]

so the corresponding logarithmic coefficients after the \(4!\) vertex
normalization are \(1/8,1/12,11/96\).  Each new quartic vertex supplies two
Gaussian propagators.  Since the Hessian has cusp order two, every new loop
order adds four poles.  In particular the leading pure-quartic pieces at the
next orders are

\[
\frac{(f'''')^2}{12C^4},
\qquad
\frac{11(f'''')^3}{96C^6}.
\]

This derives the increment at the source-loop level rather than fitting it to
\(K_1,K_2\).  The remaining grade-three gate is noncancellation after cubic
vertices, amplitude insertions, adjacent transport, and implicit reversion.
The bounded exact cumulant checker is
`research/strominger/checkers/deutschean_quartic_loop_pole_increment.py`, with
result
`research/strominger/results/deutschean_quartic_loop_pole_increment.json`.

The bidirectional constructor calculus has a prospective Deutschean test.  The
fixture is frozen with forward map \((X,Y)\mapsto\nu(X,Y)\), target claim
two-control local faithfulness, and declared pullback requirements

\[
\{\text{even variance port},\text{ odd mean port}\}.
\]

Only the variance port is supplied, so the backward compiler predicts the
typed residual `odd_mean_port` before evaluating the forward hostile.  The
semantic map then independently confirms the prediction: the real Pearcey
cycle makes \(P\) and \(\nu=P_{YY}/P\) even in \(Y\), hence

\[
\nu(X,Y)=\nu(X,-Y).
\]

The missing port \(\mu=P_Y/P\) is odd and separates this collision.  At the
cusp the variance-only Jacobian has rank one, while the \((\mu,\nu)\) Jacobian
has nonzero determinant.  Thus semantic pullback predicts the minimal
extension before the hostile is computed; no post-hoc rule adjustment is
needed.  The frozen contract and checker are
`research/strominger/contracts/deutschean-pearcey-prospective-pullback.v1.json`
and
`research/strominger/checkers/deutschean_pearcey_prospective_pullback.py`.

A second prospective fixture produces a domain residual rather than a missing
port.  Freeze the complete nonlinear map

\[
(X,Y)\longmapsto(\mu,\nu)
\]

and ask for an executable inverse on an arbitrary pair of real record values.
The declared semantic pullback requires the strict moment domain
\(\nu>\mu^2\).  This is source-derived because

\[
\partial_Y\mu=\nu-\mu^2=\operatorname{Var}(u)>0
\]

for the positive full-support real Pearcey measure.  Before evaluating the
hostile, the compiler therefore predicts
`strict_moment_domain_nu_gt_mu_squared` as its residual.  The frozen hostile
record \((\mu,\nu)=(1,1)\) then has zero variance and no finite real-Pearcey
source preimage.  The minimal repair restricts the target schema; it does not
add a port or fabricate a source state.  The contract and checker are
`research/strominger/contracts/deutschean-pearcey-moment-domain-pullback.v1.json`
and
`research/strominger/checkers/deutschean_pearcey_moment_domain_pullback.py`.

Closing the moment cone produces a genuinely different residual.  Along

\[
X=-A,
\qquad
Y=Am,
\qquad
A\to\infty,
\]

the positive Pearcey measure concentrates at \(u=m\), and

\[
(\mu,\nu)\longrightarrow(m,m^2).
\]

For \(m=1\), the stationary point satisfies

\[
u_A^3+Au_A-A=0,
\qquad
0<1-u_A=\frac{u_A^3}{A}<\frac1A,
\]

while the local curvature \(A+3u_A^2\) diverges.  The limiting record
\((1,1)\) is therefore the Dirac state \(\delta_1\).  It lies in the weak-*
completion of the measure family but has no finite-control preimage.

The prospective compiler accordingly predicts
`weak_star_dirac_boundary_constructor` before the concentration hostile.  The
minimal extension adjoins \(\delta_m\) as an atomic weak-* boundary state; it
must not be retyped as an ordinary finite control or flat scalar base change.
The frozen contract and checker are
`research/strominger/contracts/deutschean-pearcey-weak-star-completion-pullback.v1.json`
and
`research/strominger/checkers/deutschean_pearcey_weak_star_completion_pullback.py`.

The Pearcey relations close their derivatives polynomially:

\[
\partial_Y\mu=\nu-\mu^2,
\qquad
\partial_Y\nu=X\mu+Y-\mu\nu,
\]

\[
\partial_X\mu=\frac{X\mu+Y-\mu\nu}{2},
\qquad
\partial_X\nu=\frac{1+Y\mu+X\nu-\nu^2}{2}.
\]

At the cusp, \(\mu=0\) and

\[
\nu_0=2\frac{\Gamma(3/4)}{\Gamma(1/4)}.
\]

The control Jacobian is

\[
\begin{pmatrix}
0&\nu_0\\
(1-\nu_0^2)/2&0
\end{pmatrix}.
\]

It is invertible. Indeed, integration by parts gives
\(\mathbb E[u^4]=1\), while strict Cauchy--Schwarz gives
\(0<\mathbb E[u^2]^2<1\); hence \(0<\nu_0<1\). Therefore \((\mu,\nu)\)
locally reconstructs both uniform controls \((X,Y)\) through the cusp.

These are the natural completed connected readouts: two finite nonlinear
coordinates obtained from the rank-three linear carrier. The exact checker is
`research/strominger/checkers/deutschean_connected_pearcey_ports.py`, with
result
`research/strominger/results/deutschean_connected_pearcey_ports.json`.

There is also a source-side clue. For

\[
P(T)=e^{-T}-1+T,
\]

the phase component is

\[
g_{\mathrm{mix}}=\frac23(T\partial_T-1)P.
\]

Thus it is the Euler-rescaling direction of the primitive phase, accompanied
by definite amplitude shifts. This resemblance does not make it a source
equivalence: the second connected port distinguishes it. The exact checker is
`research/strominger/checkers/deutschean_closed_mixed_circuit.py`, with result
`research/strominger/results/deutschean_closed_mixed_circuit.json`.

The Euler clue does not by itself lift to a carrier symmetry. Write
\(u=tx\),

\[
P(u)=e^u-1-u,
\qquad
F=(e^u-ct)e^{bu}e^{-P(u)/t}.
\]

Compare the mixed parameter deformation with the coordinate dilation

\[
\frac23(t\partial_t+u\partial_u)F,
\]

which is \(2t\partial_tF/3\) at fixed \(x\). Their difference is

\[
-tu\,e^{5u/4}e^{-P(u)/t}.
\]

The prefactor \(e^u-3t/2\) cancels, leaving one nonzero source atom. Therefore
the mixed circuit is not the bare Euler reparametrization of the full carrier.
It can become a genuine source equivalence only if this residual atom is
independently shown to be boundary-exact or removed by an authorized carrier
transformation. Otherwise a higher connected port may detect it. The exact
comparison checker is
`research/strominger/checkers/deutschean_mixed_circuit_carrier_residual.py`,
with result
`research/strominger/results/deutschean_mixed_circuit_carrier_residual.json`.

The residual has a precise source type:

\[
-tu\,e^{5u/4}e^{-P/t}=\partial_b\partial_cF.
\]

It is the mixed curvature of the two amplitude constructors. After restoring
\(u=tx\), its first term is

\[
-t^2x+O(t^3).
\]

Normalized Gamma integration sends this term to

\[
-qt^2,
\]

which is nonzero for positive grade. Therefore the residual cannot be a total
\(x\)-derivative with vanishing endpoint contribution under the existing
Gamma boundary contract. Removing it would require a new nonzero boundary
current, not an integration-by-parts identity already present in the source.
This source residual agrees with the corrected port calculation: \(H_2\)
already detects it. No third-port calculation is needed for this falsifier.

The source hostile is recorded separately under the ignored manifest
`.ai/tmp/strominger-connected-vertex-order30-run.json`; its generated result
remains temporary because it is a parameterized falsification run rather than
the default durable checker output.

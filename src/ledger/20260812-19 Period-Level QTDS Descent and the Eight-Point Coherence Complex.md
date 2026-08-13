# Period-Level QTDS Descent and the Eight-Point Coherence Complex

## Record

Date: 2026-08-12

Status: the all-orders QTDS family gives a representation-independent, period-level pointed lift
of the scalar-derived half-class, and its tree residues are factorization compatible. A canonical
local polarity flow is constructed in the six-point flip complex. The eight-point presentation
complex and its first higher-coherence cells are identified exactly. No augmentation into the
scalar specialized twisted-chain complex has yet been constructed.

## Upgraded verdict

> **Period-level pointed QTDS descent.** For every even multiplicity and every alternating lift
> of a cyclic order, the QTDS quartic-tree sum evaluates to the corresponding scalar rank-jump
> period. The complete family descends through the Parke--Taylor quotient and, through the perfect
> scalar pairing, reconstructs
> \[
> \mathsf J_n=[(\operatorname{Pf}'A_n)^2].
> \]
> Trees containing a physical channel are in product bijection with lower-point trees, so residues
> factorize before the final sum over channels.

This is stronger than matching one color ordering. It is weaker than a chain-level
strictification, which still requires a scalar-normal twisted primitive for the polarity
comparison and coherent fillers for its higher flip relations.

## Complete periods and factorization

For an alternating cyclic lift \((\alpha,\varepsilon)\), define

\[
q_{n,\alpha,\varepsilon}
=
\sum_{Q\in\operatorname{Quad}_n(\alpha)}
\frac{N^\varepsilon_Q}{\prod_{D\in Q}X_D}[Q].
\]

The QTDS tree theorem and scalar associated-grade theorem give, up to the declared
quartic-coupling sign,

\[
\operatorname{Ev}_{\alpha,\varepsilon}(q_{n,\alpha,\varepsilon})
=
A_n^{\rm QTDS}(\alpha,\varepsilon)
=
a_{R,n}(\alpha).
\]

Entry 14 proves that the right side annihilates the Parke--Taylor relation ideal. Hence the
complete QTDS family defines

\[
a_n^{\rm QTDS}\in(H_n^-)^*,
\qquad
\mathsf J_n^{\rm QTDS}
=(I_n^\flat)^{-1}a_n^{\rm QTDS}
=\mathsf J_n.
\]

At six points the exact audit evaluates both polarity families on all six elements of an
independent Parke--Taylor basis. Inverting the \(6\times6\) biadjoint pairing produces the scalar
grade coordinates and predicts every additional audited ordering.

For an allowed channel \(D\),

\[
\{Q\in\operatorname{Quad}_n:D\in Q\}
\simeq
\operatorname{Quad}_{L}\times\operatorname{Quad}_{R}.
\]

Cutting \(1/X_D\) therefore gives

\[
\operatorname*{Res}_{X_D=0}q_{n,\alpha,\varepsilon}
=
q_{L,\alpha_L,\varepsilon_L}
\otimes
q_{R,\alpha_R,\varepsilon_R}.
\]

The audit verifies the product count and exact residue for both polarities at six and eight
points. At a nested eight-point \(3|3\), \(5|3\) corner, the simultaneous residue equals the
product of three four-point periods. This proves evaluated presentation-level cut coherence, not
the existence of its chain-level two-cell.

## Why the interval is not enough

The endpoint comparison has the interval coalgebra

\[
dh=q_+-q_-,
\qquad
\Delta q_\pm=q_\pm\otimes q_\pm,
\]

\[
\Delta h=q_-\otimes h+h\otimes q_+.
\]

It is strictly coassociative, but freely adjoining \(h\) is a formal cylinder. Non-vacuity
requires:

1. a local \(h\) in the QTDS presentation complex;
2. an image in a declared scalar specialized complex;
3. Alexander--Whitney residue compatibility;
4. a composition-stable augmentation kernel.

## Six points: canonical local flow

The three hexagon quadrangulations form a flip triangle. Write

\[
q_{6,\pm}
=
\sum_{i=1}^{3}\frac{N_i^\pm}{X_i}[Q_i].
\]

Both polarity choices have the same four-point residue on the \(Q_i\) pole, so

\[
X_i\mid N_i^+-N_i^-.
\]

Set

\[
c_i=\frac{N_i^+-N_i^-}{X_i}.
\]

Equality of total sums gives \(c_1+c_2+c_3=0\). The inverse triangle Laplacian supplies a
basepoint-free local flow:

\[
H_{ij}=\frac{c_i-c_j}{3},
\qquad
\sum_{j\ne i}H_{ij}=c_i.
\]

Thus

\[
\partial h_6=q_{6,+}-q_{6,-}.
\]

A one-step rotation exchanges polarities and sends \(c,h_6\) to \(-c,-h_6\). The exact descent
audit checks the contact residues, sum-zero identity, local flow, and rotation law. This is a real
homotopy in the quadrangulation presentation complex, but not yet in scalar twisted chains.

## Eight points: first higher-coherence complex

The eight admissible octagon diagonals form the cubic Möbius ladder \(M_8\), the
\(2\)-divisible type-\(A_2\) compatibility graph. Its twelve edges are the twelve
quadrangulations. The full flip graph is the line graph

\[
\Gamma_8=L(M_8),
\qquad
|V|=12,
\quad
|E|=24,
\quad
\deg Q=4.
\]

Its explicit medial cellulation has

\[
8\text{ triangles},
\qquad
4\text{ squares},
\qquad
1\text{ octagon}.
\]

Every edge lies on two faces and every vertex link is a four-cycle. The complex is a closed
connected surface with

\[
\chi=12-24+13=1,
\]

hence a projective-plane cellulation. Exact boundary matrices give

\[
(b_0,b_1,b_2)_{\mathbb Q}=(1,0,0),
\qquad
(b_0,b_1,b_2)_{\mathbb F_2}=(1,1,1).
\]

Rational coefficients erase a genuine \(\mathbb Z_2\) sector. Polarity transport must retain
integral, sign-local-system, or mod-two information until this sector is resolved.

Each triangle consists of the three quadrangulations containing a fixed physical channel.
Factorization prescribes

\[
\operatorname*{Res}_{X_D=0}h_8
=
q_{L,-}\otimes h_R
+
h_L\otimes q_{R,+}.
\]

The four squares are the first local higher-coherence tests; the octagon tests global cyclic
holonomy. Equality of summed amplitudes tests none of these fillers.

## Local eight-point equation and Jordan obstruction

A local flip homotopy has the form

\[
h_8
=
\sum_{Q\sim Q'}
\frac{H_{QQ'}}{\prod_{D\in Q\cap Q'}X_D}[Q,Q'].
\]

At every quadrangulation it must solve

\[
N_Q^+-N_Q^-
=
\sum_{Q'\sim Q}
\sigma_{QQ'}X_{Q\setminus Q'}H_{QQ'}.
\]

This forbids nonlocal repair poles. Its residues on the eight channel triangles are fixed by
\(h_6\), its square circulations need local fillers, and its octagonal holonomy must obey the
one-step rotation/deck law.

The predicted unstripped square curvature is the Jordan defect

\[
\mathfrak D(x,y)=Q_{Q_xy}-Q_xQ_yQ_x.
\]

The exact audit locates this defect inside the complex. Label the Möbius-ladder cycle by
\(d_0,\ldots,d_7\), its outer edges by

\[
A_i=(d_i,d_{i+1}),
\]

and its four matching edges by

\[
B_i=(d_i,d_{i+4}).
\]

Then the factorization triangles, squares, and octagon can be written

\[
T_i=(A_{i-1},A_i,B_{i\bmod4}),
\]

\[
S_i=(A_i,B_{i+1},A_{i+4},B_i),
\qquad i=0,\ldots,3,
\]

\[
O=(A_0,A_1,\ldots,A_7).
\]

Root the seven input slots as

\[
(x,y,x,z,x,y,x).
\]

With the convention \(Q_xy=T^+(x,y,x)\), the two nonadjacent matching
quadrangulations \(B_0\) and \(B_2\) carry

\[
B_0:
\quad
T^+(T^+(x,y,x),z,T^+(x,y,x))
=
Q_{Q_xy}z,
\]

\[
B_2:
\quad
T^+(x,T^-(y,T^+(x,z,x),y),x)
=
Q_xQ_yQ_xz.
\]

There are exactly four shortest three-flip paths from \(B_0\) to \(B_2\). Thus the Jordan
fundamental formula is an exact endpoint-coherence problem in this presentation complex, not a
post hoc resemblance.

This does **not** yet prove that one square curvature equals \(\mathfrak D\). The cell complex
alone supplies paths but no Jordan-valued edge transport \(H_{QQ'}\). The distribution of the
endpoint defect among the four squares and the octagonal holonomy depends on that coefficient
system. Locality, triangle residues, and cyclic covariance must determine it before the stronger
claim is meaningful.

This underdetermination is quantitative. Orient the three edges of the \(i\)-th factorization
triangle as

\[
a_i:A_{i-1}\to A_i,
\qquad
b_i:A_i\to B_{i\bmod4},
\qquad
c_i:B_{i\bmod4}\to A_{i-1}.
\]

Writing their local coefficients as \(A_i/X_{d_i}\), \(B_i/X_{d_i}\), and \(C_i/X_{d_i}\), the
twelve vertex-divergence equations are

\[
\delta_{A_j}
=
\frac{A_j-B_j}{X_{d_j}}
+
\frac{C_{j+1}-A_{j+1}}{X_{d_{j+1}}},
\]

\[
\delta_{B_k}
=
\frac{B_k-C_k}{X_{d_k}}
+
\frac{B_{k+4}-C_{k+4}}{X_{d_{k+4}}}.
\]

The incidence matrix has rank \(11\). Once the total polarity difference vanishes, the solution
space for 24 edge coefficients has dimension

\[
24-11=13,
\]

exactly the number of two-cells. Thus vertex data and summed-amplitude equality cannot choose the
homotopy; the eight triangle, four square, and one octagonal fillings are precisely the missing
coherence data.

There is also a concrete negative result for the naive square proposal. Rooting the twelve
quadrangulations and decorating them by the polarized special Jordan triple product

\[
[x\,y\,z]=xyz+zyx
\]

gives canonical vertex bracketings. But the alternating sum of the four vertex bracketings around
a square is nonzero in the free associative envelope even though the Jordan fundamental formula
holds identically there. Therefore

\[
\boxed{\text{naive square vertex sum}\ne\text{Jordan defect}.}
\]

A valid square curvature requires degree-one edge syzygies specifying which polarized Jordan
identity is transported across each flip. At the stripped ordered level, a generic Jordan pair
also supplies \(xyz+zyx\), whereas QTDS selects an oriented word such as \(xyz\). An oriented
splitting or associative-envelope datum is therefore required in addition to the metric Jordan
pair.

The next finite calculation is to decorate the twelve quadrangulations by a generic metric
quadratic pair, solve the 24 edge equations with the eight triangle constraints, and compute the
four square curvatures and the residual octagonal holonomy. Equality of square curvature with
\(\mathfrak D\) would identify the Jordan identity as the first extension obstruction. A surviving
octagonal class would show that Jordan closure is necessary but insufficient.

## Correct scalar-geometric target

Three spaces must not be conflated:

1. scalar parameter geometry \(B_n\), containing the rank stratum \(R_n\);
2. worldsheet geometry \(\overline{\mathcal M}_{0,n}\);
3. the alternating presentation groupoid \(\widetilde{\mathcal B}_n\).

A proposed chain model starts with

\[
\mathscr K_n\in
D_c^b(B_n\times\overline{\mathcal M}_{0,n})
\]

and selects a normal-order and monodromy summand of Verdier specialization:

\[
\mathscr K_n^R
=
e_{m,\lambda}\operatorname{Sp}_{R_n}(\mathscr K_n).
\]

This must not be called a vanishing-cycle object without a normal-slice calculation. For a
hypersurface \(f\),

\[
i^*\mathscr K_n
\longrightarrow
\psi_f\mathscr K_n
\longrightarrow
\phi_f\mathscr K_n
\xrightarrow{+1}.
\]

The NLSM grade is a vanishing sector only if it dies in the persistent scalar piece. In greater
codimension, specialization or a \(V\)-filtration summand is the safe typing.

An actual augmentation would be

\[
a_n:\mathcal Q_n[n-3]\longrightarrow p^*\mathscr K_n^R,
\]

with

\[
a_n(q_\pm)=\omega_{n,\pm},
\qquad
a_n(h)=\eta_n,
\]

\[
\nabla\eta_n
=
\omega_{n,+}-T_\gamma\omega_{n,-},
\]

and

\[
\operatorname{Res}_D\eta_n
=
\omega_{L,-}\boxtimes\eta_R
+
\eta_L\boxtimes\omega_{R,+}.
\]

Here \(T_\gamma\) is actual local-system transport. The period family lands first in the dual
scalar object, so a chain-level half-object lift additionally requires a chain-level perfect
pairing

\[
I^\flat:\mathscr K_n^R\xrightarrow{\sim}\mathbb D\mathscr K_n^R.
\]

Perfectness only on cohomology yields exactly the pointed cohomological lift proved here.

At six points, non-vacuity requires a normal-link one-chain realizing \(h_6\) and forms

\[
\nabla\eta_6=\omega_{6,+}-\omega_{6,-}.
\]

At eight points, every square or octagonal boundary gives

\[
\Theta_F=\sum_{e\subset\partial F}\epsilon(e,F)\eta_e,
\]

and requires a factorization-local filler \(\nabla\xi_F=\Theta_F\). The obstruction must be
computed with the normal filtration, microsupport, and residue locality fixed; an unrestricted
acyclic enlargement would make it tautological.

## Jordan provenance boundary

Microlocal monodromy is linear and does not itself produce a metric quadratic Jordan pair.
Jordan data remains a coefficient system or rank-stratum modulus unless unstripped scalar normal
correspondences construct a canonical \(3\)-graded Lie algebra

\[
\mathfrak g=\mathfrak g_{-1}\oplus\mathfrak g_0\oplus\mathfrak g_1.
\]

Only then could

\[
\{x,y,z\}=[[x,y],z],
\qquad
Q_x(y)=\frac12\{x,y,x\}
\]

derive Jordan coherence from Jacobi rather than supply it externally.

At the operadic level the missing object can be stated as a coefficient-system map

\[
\Phi:
C_\bullet(\mathfrak M_8;\mathbb Z_\eta)
\longrightarrow
\mathcal C_J
\]

assigning vertex contractions to quadrangulations, Jordan syzygies to flips, factorization
homotopies to triangles, polarized fundamental-identity coherences to squares, and cyclic descent
to the octagon. Equivalently, one needs a declared cofibrant or \(JP_\infty\) resolution, not only
an algebra over the degree-zero Jordan-pair identities.

## Reproducible audits

- python research/nima/check_qtds_lift.py checks complete-period reconstruction, cut products,
  nested residues, and the rectangular Jordan identity.
- python research/nima/check_qtds_descent.py checks the six-point local flip flow and the exact
  eight-point projective-plane cell complex, homology, and placement of the Jordan fundamental
  formula at two explicit quadrangulation vertices.

Both scripts use standard-library exact arithmetic.

## Sources and provenance boundary

- [Cao, Han, and Zhu, *NLSM amplitudes from a quartic two-derivative theory*](https://arxiv.org/html/2607.27345v1)
  supplies the QTDS grammar, tree equivalence, generalized-cut statement, and polarity caveats.
- [Fomin and Reading, *Generalized cluster complexes and Coxeter combinatorics*](https://arxiv.org/abs/math/0505085)
  supplies the generalized cluster-complex setting. The explicit \(M_8\), line-graph,
  projective-plane cellulation, and homology audit are Marici calculations.
- [Maxim and Schürmann, *Constructible sheaf complexes in complex geometry and applications*](https://arxiv.org/abs/2105.13069)
  supplies standard constructible, nearby-cycle, vanishing-cycle, and stratified-Morse context.
- [Treumann, *Exit paths and constructible stacks*](https://arxiv.org/abs/0708.0659)
  supplies exit-path constructible descent, not the cross-multiplicity factorization maps here.

## Decision

Promote the complete QTDS period family and its residues to a **cohomology-level pointed
factorization lift of \(\mathsf J\)**.

Do not yet call it a Jordan strictification. The remaining primary frontier is:

1. realize the six-point triangle flow as a scalar-normal twisted primitive;
2. solve the eight-point local edge equations with factorization-triangle data;
3. identify square curvature with the Jordan defect or falsify it;
4. test residual octagonal and \(\mathbb Z_2\) holonomy;
5. only then seek an all-arity coherence theorem.

Entry 20 sharpens this frontier. It proves that the summed scalar amplitude underdetermines the
triangle flow, but the scalar cubic-cell grade does not: its parity-core decomposition gives the
exact six-point QTDS contact redistribution and canonically labels the eight-point factorization
triangles and square faces.

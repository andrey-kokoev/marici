# Theta cubic bilinear companion

Status: live two-copy successor packet.

## 1. The logarithmic denominator cancels

Let

\[
 W(u)=\frac{V'(u)}u=-\frac{\Phi'(u)}{u\Phi(u)},
 \qquad V=-\log\Phi.
\]

Define the antisymmetric bilinear source kernel

\[
\boxed{
 \mathscr B(u,v)
 =\frac{\Phi(u)\Phi'(v)}v
  -\frac{\Phi'(u)\Phi(v)}u.
}                                                       \tag{1}
\]

Then

\[
\boxed{
 \Phi(u)\Phi(v)[W(u)-W(v)]=\mathscr B(u,v).
}                                                       \tag{2}
\]

Thus the two-copy separation integrand contains no logarithm and no quotient
of theta sums.  The source densities cancel the nonlinear denominators
exactly.

Since \(W\) is strictly increasing with \(R=u^2\),

\[
 (u^2-v^2)\mathscr B(u,v)>0
 \qquad(u\ne v).                                      \tag{3}
\]

## 2. Fixed product companion kernel

Use the ordered product-ratio chart

\[
 u=\sqrt p\,e^s,
 \qquad
 v=\sqrt p\,e^{-s},
 \qquad p>0, s\ge0,                                  \tag{4}
\]

whose Jacobian is \(du\,dv=dp\,ds\).  Define

\[
\boxed{
 k(p)
 =2p\int_0^\infty
  \sinh(2s)\,
  \mathscr B(\sqrt p e^s,\sqrt p e^{-s})\,ds.
}                                                       \tag{5}
\]

Equation (3) gives

\[
 k(p)>0.                                               \tag{6}
\]

Crucially, \(k\) is independent of the tilt index.

Let

\[
 K_t=\int_0^\infty p^{2t}k(p)\,dp.                    \tag{7}
\]

The exact covariance reserve is

\[
\boxed{
 C_t=\frac{K_t}{Z_t^2}.
}                                                       \tag{8}
\]

Hence the inverse separation length is

\[
\boxed{
 L_t
 =\sqrt{2t+1}\,\frac{Z_t}{\sqrt{K_t}}.
}                                                       \tag{9}
\]

The entire cubic gate becomes

\[
\boxed{
 \left|
  \sqrt{2t+3}\frac{Z_{t+1}}{\sqrt{K_{t+1}}}
  -\sqrt{2t+1}\frac{Z_t}{\sqrt{K_t}}
 \right|\le1.
}                                                       \tag{10}
\]

This is a paired moment theorem for two fixed positive source objects:

\[
 \Phi(u)\,du,
 \qquad
 k(p)\,dp.                                             \tag{11}
\]

No hierarchy is raised when \(t\) advances; both sides undergo ordinary
monomial size bias.

## 3. Quadratic theta-label expansion

Write the completed source as

\[
 \Phi=\sum_{n\ge1}\phi_n.
\]

Then the companion kernel expands bilinearly:

\[
\boxed{
 \mathscr B(u,v)
 =\sum_{n,m\ge1}
 \left[
  \frac{\phi_n(u)\phi_m'(v)}v
  -\frac{\phi_n'(u)\phi_m(v)}u
 \right].
}                                                       \tag{12}
\]

Consequently

\[
 k(p)=\sum_{n,m\ge1}k_{n,m}(p),                       \tag{13}
\]

where every \(k_{n,m}\) is obtained from the same product-ratio integral.
Individual label-pair kernels need not be positive; positivity is a property
of the completed quadratic packet.  This distinction preserves the known
primitive curvature defect and its cross-label repair.

The benefit is closure: label activation, modular reflection, and adjacent
tilt all act on one fixed quadratic label matrix.  No derivative of a
logarithm of an infinite label sum remains.

## 4. Faithful adjacent transport

Let \(P_t\) be the probability law

\[
 dP_t(p)=K_t^{-1}p^{2t}k(p)\,dp.                       \tag{14}
\]

Then

\[
 \frac{K_{t+1}}{K_t}=\mathbb E_{P_t}(p^2),            \tag{15}
\]

while

\[
 \frac{Z_{t+1}}{Z_t}=\mathbb E_{Q_t}(u^2)=A_t.        \tag{16}
\]

Therefore

\[
\boxed{
 \frac{L_{t+1}}{L_t}
 =\sqrt{\frac{2t+3}{2t+1}}
  \frac{A_t}{\sqrt{\mathbb E_{P_t}(p^2)}}.
}                                                       \tag{17}
\]

This recovers the earlier separation-law formula, but now the separation law
is explicitly the moment family of a fixed bilinear source companion.

## 5. Hard-to-vary explanation target

The candidate mechanism is:

\[
\boxed{
 \text{completed theta source }\Phi
 \longmapsto
 \text{positive bilinear companion }k
 \longmapsto
 \text{coherent paired moment lengths }L_t.
}                                                       \tag{18}
\]

The missing theorem is not positivity of either moment sequence separately.
It is the relative moment inequality (10).  The unit bound asserts that the
ordinary theta scale and its curvature-weighted product companion remain
coherent under the same monomial tilt.

This route avoids both previously diagnosed hierarchy shifts:

- heat differentiation introduced \(C_{t+2}\);
- Stein size bias introduced a higher tail primitive;
- bilinearization leaves the companion kernel fixed.

## 6. Immediate label-combinatorics attack

The next calculation should preserve the matrix \((k_{n,m})\) and ask:

1. which diagonal label packets carry the primitive hostile curvature;
2. which off-diagonal packets repair them;
3. whether modular reflection pairs the signed packets into positive blocks;
4. whether each completed block has a moment-length increment in the common
   unit interval;
5. whether block addition preserves that interval through a source-derived
   correspondence rather than a generic convexity claim.

The sharp local falsifier is a completed modular block whose contribution
forces the paired length difference outside one.  If individual blocks fail
but the total succeeds, the cross-block coherence—not blockwise positivity—is
the theorem that must be explained.

## 7. Explicit label-score matrix

Up to one common positive constant, the theta labels on the positive chamber
are

\[
 \phi_n(u)
 =n^2e^{5u/2}(2n^2x-3)e^{-n^2x},
 \qquad x=\pi e^{2u}.                                  \tag{19}
\]

Their logarithmic derivatives are

\[
\boxed{
 \lambda_n(u)
 :=\frac{\phi_n'(u)}{\phi_n(u)}
 =\frac52+\frac{4n^2x}{2n^2x-3}-2n^2x.
}                                                       \tag{20}
\]

Therefore the ordered label-pair entry is

\[
\boxed{
 \mathscr B_{n,m}(u,v)
 =\phi_n(u)\phi_m(v)
  \left(\frac{\lambda_m(v)}v-\frac{\lambda_n(u)}u\right).
}                                                       \tag{21}
\]

The completed kernel is the sum of this score matrix.  The diagonal entries
measure within-label curvature; the off-diagonal entries transport score
between different arithmetic scales.

No sign is assigned entrywise.  In particular, the primitive diagonal
inherits the known curvature transition.  Positivity emerges only after the
full source packet is assembled.

At \(u=0\), individual quotients \(\lambda_n(u)/u\) are singular, whereas
the completed quotient is regular because modular evenness gives

\[
 \Phi'(0)=0.                                           \tag{22}
\]

Thus any finite label blocking must retain the exact cancellation required
at the seam.  Termwise score bounds that discard this cancellation are not
faithful near \(u=0\).

## 8. Polarization identifies the true repair channel

For two source packets \(F,G\), define

\[
 \mathscr B[F,G](u,v)
 =\frac{F(u)G'(v)}v-\frac{F'(u)G(v)}u.                 \tag{23}
\]

Then

\[
\boxed{
 \mathscr B[F+G,F+G]
 =\mathscr B[F,F]+\mathscr B[G,G]
  +\mathscr B[F,G]+\mathscr B[G,F].
}                                                       \tag{24}
\]

The last two terms are the exact cross-label repair.  They are forced by
source addition before the curvature readout; they are not fitted after a
diagonal block fails.

For the primitive/tail split

\[
 \Phi=\phi_1+T,
\]

the positive completed companion is therefore

\[
\boxed{
 \mathscr B[\Phi,\Phi]
 =\mathscr B[\phi_1,\phi_1]
  +\mathscr B[T,T]
  +\mathscr B[\phi_1,T]
  +\mathscr B[T,\phi_1].
}                                                       \tag{25}
\]

This is the faithful algebraic meaning of “labels repair primitive
curvature.”  A proof should orient the polarized pair, not attempt to make
each diagonal term positive.

## 9. Finite label blocks fail the modular seam gate

The tempting smallest test would use \(F=\phi_1+\phi_2\).  That packet has
four companion-matrix entries, but it is not a completed modular source.  In
general,

\[
 (\phi_1+\phi_2)'(0)\ne0,                              \tag{26}
\]

whereas regularity of the physical score quotient requires

\[
 \sum_{n\ge1}\phi_n'(0)=\Phi'(0)=0.                   \tag{27}
\]

A standalone two-label moment-length theorem would therefore test a source
that violates the seam condition.  The earlier two-label degree-two packet
used this pair only as a local analytic core; the full tail was retained and
separately proved absorbable.

## 10. Seam-closed block criterion

For a label packet \(F_S=\sum_{n\in S}\phi_n\), admissibility of its score
companion near the modular seam requires at minimum

\[
\boxed{
 F_S'(0)=0.
}                                                       \tag{28}
\]

If this fails, the individual \(1/u\) score terms are coordinate-singular
and must be combined with the complementary packet before interpretation.
Source blocks are selected by seam incidence, not by label count.

The next combinatorial question is:

\[
\boxed{
 \text{Does the theta label matrix admit any proper, source-derived,
 seam-closed block decomposition?}
}                                                       \tag{29}
\]

If no such decomposition exists, cross-label coherence is irreducibly global
at the seam.  Tail absorption must then be treated as an estimate inside the
one completed object, not addition of an independently physical block.

## 11. Prime divisibility supplies a Boolean route family

Benincasa's Boolean score theorem transfers to theta labels through the exact
prime-scale recursion.  Fix a finite set of primes \(P\).  For each label
\(n\), define its divisibility signature

\[
 \sigma_P(n)=\{p\in P:p\mid n\}.                       \tag{30}
\]

Let

\[
 v_S(u)=\sum_{\sigma_P(n)=S}\phi_n(u)
 \qquad(S\subseteq P)                                 \tag{31}
\]

be the exact-signature packets, and define the divisibility-route packets

\[
 M_T(u)=\sum_{S\supseteq T}v_S(u).                     \tag{32}
\]

If \(d_T=\prod_{p\in T}p\), the theta scale law gives

\[
\boxed{
 M_T(u)
 =\sum_{d_T\mid n}\phi_n(u)
 =d_T^{-1/2}\Phi(u+\log d_T).
}                                                       \tag{33}
\]

Thus every Boolean route is source-derived: it is a translated copy of the
same undecomposed theta source, not a fitted deletion observable.

Möbius inversion reconstructs every exact signature:

\[
\boxed{
 v_S
 =\sum_{T\supseteq S}(-1)^{|T|-|S|}M_T.
}                                                       \tag{34}
\]

Hence the complete finite prime-divisibility tower is jointly faithful on the
label packet modulo the chosen finite signature resolution.

## 12. Product Möbius inversion reconstructs the companion matrix

Because \(\mathscr B[-,-]\) is bilinear,

\[
 \mathscr B[M_T,M_U]
 =\sum_{S\supseteq T}\sum_{R\supseteq U}
  \mathscr B[v_S,v_R].                                 \tag{35}
\]

This is the Boolean zeta transform on the product lattice
\(2^P\times2^P\).  Double Möbius inversion gives

\[
\boxed{
 \mathscr B[v_S,v_R]
 =\sum_{T\supseteq S}\sum_{U\supseteq R}
  (-1)^{|T|-|S|+|U|-|R|}
  \mathscr B[M_T,M_U].
}                                                       \tag{36}
\]

Therefore the complete mixed prime-score tower is jointly faithful on the
quadratic coefficient packet.  The off-diagonal repair channels are, in
principle, reconstructible from source-generated translated theta routes.

This is the first exact combinatorial closure of the bilinear companion:

\[
\boxed{
 \text{prime-scale routes}
 \xrightarrow{\text{mixed bilinear scores}}
 \text{Boolean zeta data}
 \xrightarrow{\text{Möbius inversion}}
 \text{divisibility-resolved companion matrix}.
}                                                       \tag{37}
\]

## 13. Faithfulness is not positivity or physical decomposition

The theorem has a strict scope boundary.  For nonempty \(T\),

\[
 M_T(u)=d_T^{-1/2}\Phi(u+\log d_T)
\]

is generally not even about \(u=0\), so it need not satisfy the physical seam
condition \(M_T'(0)=0\).  The Boolean tower reconstructs labelled
coefficients; it does not make every route an independently physical source.

Likewise, mixed score correlators contain all divisibility sectors compatible
with their route indices.  Möbius inversion must be performed before assigning
an exact-signature interpretation.  This is the theta analogue of Nima's
contact-normal warning: a raw contextual score includes background deletion
sectors.

The durable conclusion is

\[
\boxed{
 \text{joint coefficient faithfulness}
 \ne
 \text{seam-closed block positivity}.
}                                                       \tag{38}
\]

What the Boolean theorem supplies is the missing faithful coordinate system
for the quadratic label matrix.  The remaining RH-relevant problem is to
show that the physical recombination selected by the modular seam orients its
paired moments according to (10).

## 14. The modular seam obstruction is finite rank

Fix the finite divisibility resolution and write

\[
 a_S=v_S(0),
 \qquad
 b_S=v_S'(0).                                         \tag{39}
\]

Near the seam,

\[
 v_S(u)=a_S+b_Su+O(u^2).
\]

For fixed \(u>0\) and \(v\downarrow0\), the polarized companion has residue

\[
\boxed{
 \mathscr B[v_S,v_R](u,v)
 =\frac{v_S(u)b_R}{v}+O(1).
}                                                       \tag{40}
\]

Thus the entire singular residue matrix factors through the single
coefficient vector

\[
 b=(b_R)_{R\subseteq P}.                               \tag{41}
\]

It has rank at most one.  At the opposite boundary \(u\downarrow0\), the
residue factors through the same vector in the other index:

\[
\boxed{
 \mathscr B[v_S,v_R](u,v)
 =-\frac{b_Sv_R(v)}u+O(1).
}                                                       \tag{42}
\]

Therefore the combined two-boundary obstruction has rank at most two.

## 15. Physical recombination annihilates the residue

The physical source is the all-signature recombination

\[
 \Phi=\sum_{S\subseteq P}v_S.
\]

Modular evenness gives

\[
\boxed{
 \sum_{S\subseteq P}b_S=\Phi'(0)=0.
}                                                       \tag{43}
\]

Consequently contraction of either companion index with the physical
all-ones coefficient vector annihilates the corresponding seam residue.
The full physical companion is regular even though its divisibility-resolved
entries need not be.

This identifies the exact typed sewing map:

\[
\boxed{
 \text{divisibility coefficient packet}
 \xrightarrow{\langle\mathbf1,-\rangle}
 \text{physical completed source},
 \qquad
 \langle\mathbf1,b\rangle=0.
}                                                       \tag{44}
\]

The cancellation is source-derived and finite rank.  It is not positivity:
the regular finite part of the matrix still has to satisfy the paired moment
orientation.

## 16. Möbius reconstruction of the seam vector

The Boolean routes determine the residue vector exactly.  From (33),

\[
 M_T'(0)=d_T^{-1/2}\Phi'(\log d_T).                    \tag{45}
\]

Applying Möbius inversion gives

\[
\boxed{
 b_S
 =\sum_{T\supseteq S}(-1)^{|T|-|S|}
  d_T^{-1/2}\Phi'(\log d_T).
}                                                       \tag{46}
\]

Hence both the full quadratic coefficient matrix and its complete seam
residue are jointly reconstructible from mixed prime-scale routes.

This is the precise analogue of the finite-rank defect architectures found
in the prime-two and Green-identity lanes, with a crucial distinction:

\[
\boxed{
 \text{here the finite-rank seam term is exactly annihilated by physical
 completion; it is not a positive repair of the remaining bulk.}
}                                                       \tag{47}
\]

The next invariant object is therefore the regularized companion obtained
after quotienting the rank-two seam residue.  Cubic positivity must be proved
for that regularized physical packet, not for its singular contextual
coordinates separately.

## 17. Canonical seam-compatible coefficient hyperplane

Let \(\mathcal C_P=\mathbb R^{2^P}\) be the divisibility coefficient space.
The seam derivative defines the covector

\[
 b^*(c)=\sum_{S\subseteq P}c_Sb_S.                    \tag{48}
\]

Define

\[
\boxed{
 \mathcal C_P^{\mathrm{seam}}=\ker b^*.
}                                                       \tag{49}
\]

For \(c\in\mathcal C_P\), the corresponding packet

\[
 F_c=\sum_Sc_Sv_S
\]

satisfies

\[
 F_c'(0)=b^*(c).                                       \tag{50}
\]

Hence \(F_c'(0)=0\) exactly when \(c\in\mathcal C_P^{\mathrm{seam}}\).
The polarized companion is regular at both boundaries on

\[
 \mathcal C_P^{\mathrm{seam}}\times
 \mathcal C_P^{\mathrm{seam}}.                        \tag{51}
\]

The physical coefficient vector

\[
 \mathbf1=(1)_{S\subseteq P}
\]

lies in this hyperplane by (43).

Thus no counterterm or choice of complement is required.  The canonical
operation is restriction to the kernel of the source-derived seam covector.
If \(b\ne0\), this loses exactly one contextual coefficient direction at
each boundary while retaining the physical ray.

The remaining positivity problem has three distinct levels:

1. Boolean mixed scores reconstruct the full contextual coefficient matrix;
2. the seam covector selects its regular codimension-one domain;
3. the physical all-ones ray inside that domain supplies the completed scalar
   companion entering the cubic gate.

Faithfulness holds at level one, regularity is imposed at level two, and RH
orientation is asked only at level three.  None implies the next.

## 18. Boolean signatures forget prime-power valuation

The Boolean packet records only whether \(p\mid n\).  Even after every prime
is included, it distinguishes \(\operatorname{rad}(n)\), not the full label
\(n\).  Thus Boolean faithfulness is exact only at squarefree divisibility
resolution.

The theta scale law supplies the missing refinement.  For a finite prime set
\(P\) and multi-index

\[
 \alpha=(\alpha_p)_{p\in P}\in\mathbb N^P,
 \qquad
 d_\alpha=\prod_{p\in P}p^{\alpha_p},                 \tag{52}
\]

define the valuation-tail route

\[
 M_\alpha(u)
 =\sum_{v_p(n)\ge\alpha_p\ \forall p\in P}\phi_n(u).
                                                               \tag{53}
\]

The same label transport gives

\[
\boxed{
 M_\alpha(u)
 =d_\alpha^{-1/2}\Phi(u+\log d_\alpha).
}                                                       \tag{54}
\]

Thus every node of the product-of-chains poset \(\mathbb N^P\) is again a
source-derived translated theta route.

## 19. Product finite differences recover exact valuations

Let \(v_\alpha^{(P)}\) collect labels with

\[
 v_p(n)=\alpha_p
 \qquad(p\in P),                                      \tag{55}
\]

while leaving primes outside \(P\) unresolved.  Möbius inversion on the
product of chains reduces to one forward difference in each coordinate:

\[
\boxed{
 v_\alpha^{(P)}
 =\sum_{\epsilon\in\{0,1\}^P}
  (-1)^{|\epsilon|}M_{\alpha+\epsilon}.
}                                                       \tag{56}
\]

For one prime this is simply

\[
 v_j^{(p)}=M_j-M_{j+1}.                                \tag{57}
\]

The quadratic companion is recovered by double finite difference:

\[
\boxed{
 \mathscr B[v_\alpha^{(P)},v_\beta^{(P)}]
 =\sum_{\epsilon,\delta\in\{0,1\}^P}
  (-1)^{|\epsilon|+|\delta|}
  \mathscr B[M_{\alpha+\epsilon},M_{\beta+\delta}].
}                                                       \tag{58}
\]

This upgrades Boolean faithfulness to valuation faithfulness at every finite
prime resolution.  As \(P\) increases through the primes, the exact integer
label is separated in the directed limit.

For finite-dimensional coefficient charts, also choose valuation caps
\(N_p\).  The cells \(0,\ldots,N_p-1\) record exact valuations and the final
overflow cell records \(v_p(n)\ge N_p\).  Formula (56) applies to interior
cells, while the overflow packet is \(M_{N_p}\).  These capped product charts
retain the full source and form a directed system as primes and caps are
added.  This avoids treating an infinite all-ones vector as an algebraic
finite-support coefficient.

## 20. Seam data commute with valuation refinement

Define

\[
 b_\alpha^{(P)}=(v_\alpha^{(P)})'(0).                  \tag{59}
\]

Equation (56) and the scale routes give

\[
\boxed{
 b_\alpha^{(P)}
 =\sum_{\epsilon\in\{0,1\}^P}
  (-1)^{|\epsilon|}
  d_{\alpha+\epsilon}^{-1/2}
  \Phi'(\log d_{\alpha+\epsilon}).
}                                                       \tag{60}
\]

If a coarse valuation cell is refined by adding a prime or increasing the
retained valuation depth, its packet is the sum of its children.  Therefore
its seam coefficient is also the sum of the child coefficients:

\[
\boxed{
 b_{\mathrm{coarse}}=\sum_{\mathrm{child}}b_{\mathrm{child}}.
}                                                       \tag{61}
\]

Let \(J\) be the coefficient pullback that assigns the coarse coefficient to
every child.  Then

\[
 (b_{\mathrm{fine}})^*J=b_{\mathrm{coarse}}^*.        \tag{62}
\]

Consequently

\[
\boxed{
 J\bigl(\mathcal C_{\mathrm{coarse}}^{\mathrm{seam}}\bigr)
 \subseteq
 \mathcal C_{\mathrm{fine}}^{\mathrm{seam}}.
}                                                       \tag{63}
\]

The physical all-ones vector is preserved by \(J\), and bilinearity gives
the same physical companion before and after refinement.

Thus the seam-compatible coefficient spaces form a coherent directed system:

\[
\boxed{
 \text{valuation refinement}
 \longrightarrow
 \text{coefficient pullback}
 \longrightarrow
 \text{seam-kernel preservation}
 \longrightarrow
 \text{invariant physical ray}.
}                                                       \tag{64}
\]

This removes dependence on a chosen finite prime census.  Finite Boolean
charts are faithful contextual coordinates at their declared resolution;
the product-of-chains refinement recovers prime powers; and the physical
scalar packet is compatible across the entire system.

## 21. What this construction proves—and does not

The coefficient architecture is now complete at the algebraic level:

1. translated theta routes generate the incidence-algebra observations;
2. finite differences recover valuation-labelled source packets;
3. double differences recover every quadratic companion channel;
4. the seam covector is reconstructed and preserved under refinement;
5. the physical ray is independent of the chosen chart.

This proves contextual faithfulness and coherence of the arithmetic
coefficient system.  It does not prove the scalar moment inequality (10).
The remaining theorem is genuinely an orientation statement on the invariant
physical ray, not missing label information.

## 22. Pull--push correspondence and the fiber norm

Let

\[
 q:\mathcal I_{\mathrm{fine}}\longrightarrow
   \mathcal I_{\mathrm{coarse}}                       \tag{65}
\]

be the map from a capped refined valuation chart to its coarse cells.  Define
coefficient pullback and packet pushforward by

\[
 (q^*c)_i=c_{q(i)},
 \qquad
 (q_!v)_a=\sum_{i\in q^{-1}(a)}v_i.                   \tag{66}
\]

Their composite on coarse coefficients is the exact fiber norm:

\[
\boxed{
 q_!q^*
 =\operatorname{diag}
  \bigl(|q^{-1}(a)|\bigr)_{a\in\mathcal I_{\mathrm{coarse}}}.
}                                                       \tag{67}
\]

For uniform refinement this is \(|\ker q|I\); for capped valuation charts the
fiber size may depend on the overflow cell, so the diagonal form is the
faithful statement.

The seam covectors transform covariantly:

\[
 b_{\mathrm{coarse}}=q_!b_{\mathrm{fine}},
 \qquad
 b_{\mathrm{fine}}^*q^*=b_{\mathrm{coarse}}^*.        \tag{68}
\]

Hence pullback preserves the seam kernel, as already seen in (63).

Let \(\mathbf B_{\mathrm{fine}}(u,v)\) be the matrix of polarized companion
entries.  Coarse packet aggregation gives

\[
\boxed{
 \mathbf B_{\mathrm{coarse}}
 =q_!\mathbf B_{\mathrm{fine}}q_!^{\mathsf T}.
}                                                       \tag{69}
\]

Since

\[
 q_!^{\mathsf T}\mathbf1_{\mathrm{coarse}}
 =q^*\mathbf1_{\mathrm{coarse}}
 =\mathbf1_{\mathrm{fine}},                            \tag{70}
\]

the physical scalar is refinement invariant:

\[
\boxed{
 \mathbf1_{\mathrm{coarse}}^{\mathsf T}
 \mathbf B_{\mathrm{coarse}}
 \mathbf1_{\mathrm{coarse}}
 =
 \mathbf1_{\mathrm{fine}}^{\mathsf T}
 \mathbf B_{\mathrm{fine}}
 \mathbf1_{\mathrm{fine}}.
}                                                       \tag{71}
\]

Thus the valuation charts form a finite correspondence/Mackey system at each
capped stage:

\[
\boxed{
 \text{pullback duplicates coefficients},
 \quad
 \text{pushforward aggregates packets},
 \quad
 \text{pull--push produces the fiber norm},
 \quad
 \text{physical readout is covariant}.
}                                                       \tag{72}
\]

This is an algebraic theorem about the coefficient--companion packet.  It
does not provide the unavailable physical relative-chain pushforward, nor
does it orient the scalar cubic moment inequality.  It establishes that the
arithmetic refinement coordinates themselves are canonical and coherent.

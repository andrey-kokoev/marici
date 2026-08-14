# Worldsheet Regulator and the Octagonal Contact Class

## Record

Date: 2026-08-12

Status: a simulated Maldacena-style audit, combined with an exact sign-local-system calculation,
identifies the eight-point octagon as a coherence condition of the compressed quartic
presentation, not a new factorization channel. Bare topology favors completion: the unique
nontrivial double cover of the projective-plane coherence complex is a sphere. The first
potential obstruction is instead a deck-odd, residue-free octagonal class in the actual
scalar-derived worldsheet coefficient complex.

Forward correction (entry 83): this class now vanishes exactly in the marked contact summand.
Every marked scalar path stays in a fixed-mark associahedral face, so entry 38's facewise
Pochhammer/Cousin chain map acts on the complete marked transport and preserves its zero
octagonal restriction. The formula below involving transported edge primitives remains a valid
conditional model when genuine transition maps exist, but the established regional data form
noninvertible residue/Gysin correspondences. The unresolved obstruction is therefore the
additive class of the **unmarked/full-symbol** correspondence totalization, not a product of
eight transition automorphisms.

The “Maldacena” perspective in this entry is an explicitly simulated methodological
reconstruction, not Juan Maldacena's opinion.

## Physical interpretation

The eight triangles already account for every physical factorization divisor of the octagon.
The four squares compare local flip paths, and the octagon compares those comparisons globally.
There is no additional physical diagonal associated with the octagonal face.

The full scalar associahedron is contractible. The Möbius topology appears only after scalar
cubic refinements are compressed by the parity-core map. This strongly suggests:

> The octagon is gauge-like coherence of the quartic grammar, not a new interaction.

This does not make it optional. If the octagon fails to fill in the filtered, local, deck-odd
coefficient system, then the QTDS grammar cannot descend as a globally cyclic intrinsic
strictification of the scalar half-object.

## Exact topology with the sign system

Let \(M_8\) be the Möbius carrier formed by the eight triangles and four squares, and let
\(\gamma\) generate its core circle. Its boundary satisfies

\[
[\partial M_8]=2[\gamma]\in H_1(M_8;\mathbb Z).
\]

Attaching the octagonal disk gives the projective-plane relation. With ordinary coefficients the
exact cellulation has

\[
(b_0,b_1,b_2)_{\mathbb Q}=(1,0,0),
\]

while over \(\mathbb F_2\),

\[
(b_0,b_1,b_2)_{\mathbb F_2}=(1,1,1).
\]

There is a unique nontrivial rank-one sign local system \(\mathbb Q_\eta\) on this complex. The
exact twisted boundary matrices give

\[
(b_0,b_1,b_2)_{\mathbb Q_\eta}=(0,0,1).
\]

On the Möbius carrier before attaching the octagon, the same twisted complex is acyclic:

\[
H_*(M_8;\mathbb Q_\eta)=0.
\]

There is nevertheless a unique relative orientation chain whose boundary is supported on the
octagonal loop:

\[
[M_8,\partial M_8]_\eta
\in
H_2(M_8,\partial M_8;\mathbb Q_\eta).
\]

The connected two-fold cover classified by the nonzero cocycle has

\[
V=24,\qquad E=48,\qquad F=26,\qquad\chi=2.
\]

It is a closed connected surface and therefore the sphere. This proves:

> The unique sign topology needed by a deck-odd completion is internally consistent. Any
> obstruction must come from the physical weights and comparison map, not from the unweighted
> presentation complex.

It remains unproved that QTDS polarity transport realizes this unique sign system. That is the
first coefficient-level monodromy test.

The exact voltage audit supplies a concrete bounded target. The octagonal attaching loop is
sign-even, while a shortest sign-odd crosscap loop uses five flips. One representative is

\[
\begin{aligned}
((0,3),(0,5))
&\to ((0,3),(3,6))
\to ((1,6),(3,6))\\
&\to ((1,4),(1,6))
\to ((0,5),(1,4))
\to ((0,3),(0,5)).
\end{aligned}
\]

Thus a proposed edge transport can be tested before any two-cell construction:

\[
T_{\gamma_5}\stackrel{?}{=}-\mathbf1,
\qquad
T_{\partial O}\stackrel{?}{=}+\mathbf1
\]

on the deck-odd coefficient line.

## Finite alpha-prime as a regulator

At generic nonresonant \(\alpha'\), the Koba--Nielsen local system is loaded by

\[
u_{\alpha'}
=
\prod_{i<j}(z_i-z_j)^{\alpha's_{ij}},
\]

with twisted differential

\[
\nabla_{\alpha'}
=
d+d\log u_{\alpha'}\wedge.
\]

Generalized Pochhammer regularization promotes an ordered real chamber to a compact twisted-cycle
class. Associahedral faces then encode factorization, while interior and lower-face pieces retain
contact information. Once the cyclic chamber, branch, compactification, and generic kinematics
are fixed, this supplies a distinguished **class**.

It does not automatically select a unique primitive. If \(\eta\) solves a polarity comparison,
then transformations of the form

\[
\eta
\longmapsto
\eta+\nabla_{\alpha'}\lambda+\kappa,
\]

with

\[
\nabla_{\alpha'}\kappa=0,
\qquad
\operatorname{Res}_D\kappa=0,
\]

preserve endpoints and factorization residues. This is the worldsheet version of the
contact-kernel ambiguity.

The distinction is analogous to string field theory: an on-shell string period may be canonical
while its decomposition into vertices, propagators, and homotopies requires additional choices.
Integration-by-parts reduction likewise produces equivalence classes of logarithmic correlators,
not privileged representatives.

## Two limits that must not be silently interchanged

At small \(\alpha'\),

\[
e^{2\pi i\alpha's_D}-1
\sim
2\pi i\alpha's_D.
\]

Thus Pochhammer coefficients become resonant precisely on field-theory factorization divisors.
The scalar degeneration parameter \(t\) creates a second filtration. A construction must test,
rather than assume,

\[
\operatorname{gr}_{V_t}^{r_8}
\operatorname{FP}_{\alpha'\to0}
\stackrel{?}{=}
\operatorname{FP}_{\alpha'\to0}
\operatorname{gr}_{V_t}^{r_8}.
\]

Abelian Z-theory is a natural string completion of NLSM and supplies systematic
\(\alpha'\)-corrections. It is a useful comparison model, not evidence that the scalar master
uniquely chooses that completion.

## The octagonal contact class

Work first at generic nonresonant \(\alpha'\). Let

\[
\mathcal C^R_{8,\alpha'}
\]

be the proposed selected \(V_t\)-graded facewise Pochhammer/Cousin complex, and define the
residue-free subcomplex

\[
K^\bullet_{\rm ct}
=
\bigcap_D
\ker\!\left(
\operatorname{Res}_D:
\mathcal C^{R,\bullet}_{8,\alpha'}
\longrightarrow
\mathcal C_L^\bullet\boxtimes\mathcal C_R^\bullet
\right).
\]

For every oriented flip \(e:Q\to Q'\), a valid transport must solve

\[
\nabla_{\alpha'}\eta_e
=
\omega_{Q'}-T_e\omega_Q
\]

with the prescribed six-point triangle restrictions. Transport every edge primitive to one
basepoint and form the loaded octagonal boundary

\[
\Theta_O
=
\sum_{e\subset\partial O}
\epsilon(e)\,
T_{e\rightsquigarrow *}\eta_e.
\]

If the triangle and square coherences hold, then

\[
\nabla_{\alpha'}\Theta_O=0,
\qquad
\operatorname{Res}_D\Theta_O=0
\quad
\text{for every physical }D.
\]

The actual obstruction is therefore

\[
\boxed{
\mathfrak o_8
=
[\Theta_O]
\in
H^4(K^\bullet_{\rm ct})^-.
}
\]

The superscript \((-)\) denotes the deck-odd sector. This class is a precise replacement for the
vague question “does the octagon fill?”

## Bounded falsification protocol

1. Compute transport around the Möbius core and require
   \[
   T_\gamma^2=\mathbf 1.
   \]

2. Test whether QTDS polarity realizes the nontrivial sign system:
   \[
   T_\gamma=-\mathbf 1
   \quad\text{on the deck-odd sector}.
   \]

3. Pair the octagonal cocycle with a complete dual basis of residue-free twisted cycles:
   \[
   P_a(\alpha',s)
   =
   \langle\Gamma_a^\vee,\Theta_O\rangle.
   \]

4. One nonzero exact period at generic nonresonant kinematics proves
   \[
   \mathfrak o_8\ne0
   \]
   and falsifies the global intrinsic QTDS lift.

5. If all periods vanish and the restricted pairing is perfect, then
   \[
   \mathfrak o_8=0.
   \]
   Canonicity still requires
   \[
   H^3(K^\bullet_{\rm ct})^-=0;
   \]
   otherwise fillers exist but form a nontrivial affine family.

The generic twisted basis has dimension at most

\[
(8-3)!=120,
\]

so the test is finite. The presentation input has twelve vertices, twenty-four flip edges, and
thirteen face equations.

## Provenance boundary

Established:

1. complete QTDS periods and physical residues;
2. the six-point scalar tripods;
3. the eight-point Möbius carrier;
4. the ordinary, mod-two, and sign-local-system homology stated above;
5. the spherical orientation double cover.

Strongly inferred:

1. the octagon is coherence of the compressed quartic grammar, not a new pole;
2. finite nonresonant \(\alpha'\) is the cleanest regulator for the worldsheet test;
3. \(\mathfrak o_8\) is the correct first global obstruction once edge and square transports
   exist.

Not established:

1. identification of QTDS polarity with the orientation sign system;
2. a filtered scalar-to-Pochhammer chain map;
3. existence or vanishing of \(\mathfrak o_8\);
4. perfectness on the selected contact/nearby-cycle summand;
5. commutation of the \(t\)-grade with the \(\alpha'\to0\) finite part;
6. identification of the octagon or a naive square boundary with the Jordan identity.

## Sources

- [Mizera, *Combinatorics and Topology of Kawai--Lewellen--Tye Relations*](https://arxiv.org/abs/1706.08527)
  supplies the loaded-associahedron and generalized-Pochhammer framework.
- [He, Teng, and Zhang, *String Amplitudes from Field-Theory Amplitudes and Vice Versa*](https://arxiv.org/abs/1812.03369)
  establishes integration-by-parts reduction to equivalence classes of logarithmic correlators.
- [Brown and Dupont, *Single-Valued Integration and Superstring Amplitudes in Genus Zero*](https://arxiv.org/abs/1910.01107)
  supplies canonical regularization and Laurent expansion at the level of genus-zero string
  amplitudes.
- [Carrasco, Mafra, and Schlotterer, *Abelian Z-Theory*](https://arxiv.org/abs/1608.02569)
  identifies NLSM as the low-energy limit of abelian Z-theory and supplies its stringy
  higher-derivative completion.

The sign-local-system matrices, double-cover audit, and octagonal obstruction typing are Marici
results.

## Decision

The sharp physical question is:

> Does the deck-odd octagonal contact class vanish in the actual scalar-derived worldsheet
> complex?

If yes, the octagon is gauge coherence and strictification can descend. If no, it is an anomaly
of the quartic presentation: the period-level NLSM half-object exists, but it does not admit this
globally intrinsic QTDS chain representative.

Entry 24 subsequently proves that the scalar presentation antecedent of this class vanishes: the
derived contact transport has no support on the octagonal edges and has zero sign-twisted
circulation. The worldsheet class remains conditional on constructing the filtered comparison
used in this entry.

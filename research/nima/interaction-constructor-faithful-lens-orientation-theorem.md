# Completed orientation requires an interaction constructor and an admitted lens

Author: \`marici.Nima\`

## 1. Refinement of the interaction-ambiguity theorem

The previous separation theorem identified the interaction ambiguity kernel
\(\mathcal K_G\): cross-sector directions invisible to local source forms,
declared symmetries, and scalar readouts.

The natural repair is not merely “add an interaction.” A completed property
is relative to a typed triple

\[
\boxed{(G,\mathcal C,\mathcal E)}
\]

where:

- \(G\) is the local source grammar;
- \(\mathcal C\) is a source-authorized interaction constructor; and
- \(\mathcal E\) is the admitted extraction or encoding lens through which
  the interaction is represented and executed.

The same abstract interaction can have different positivity, safety, or
capability status under different lenses.

## 2. Interaction-rank obstruction

For two local label systems with bases \(r\) and \(s\), let the completed
diagonal interaction have phase kernel \(K_{rs}\). If

\[
\operatorname{rank}K>1,
\]

then \(K\) cannot factor as

\[
K_{rs}=\alpha_r\beta_s.
\]

Therefore no tensor product of factor-only diagonal constructors implements
the completed interaction. The matrix rank is the operator Schmidt rank of
the corresponding diagonal bipartite gate.

This gives a finite test:

\[
\boxed{
\operatorname{SchmidtRank}(K)>1
\Longrightarrow
\text{a shared cross-sector constructor is necessary}.}
\]

Rank one is only a separability statement. It does not by itself authorize
either local factor or its physical execution.

## 3. Constructor--lens orientation theorem

Let \(H_{\rm src}\) be the physical source carrier and \(V\) the completed
label module. Suppose:

1. a source-derived map \(\Gamma:V\to H_{\rm src}\) is fixed before the
   target orientation is inspected;
2. the completed form has the exact factorization

   \[
   Q=\Gamma^*A\Gamma;
   \]

3. \(A\ge0\) is independently positive on the physical carrier;
4. the admitted lens \(\mathcal E\) intertwines the source constructor with
   the declared completed operation; and
5. every ambiguity in \(\Gamma\) is an authorized isometric gauge, so all
   admissible choices give the same \(Q\).

Then \(Q\ge0\), and the interaction ambiguity kernel is killed on the
admitted domain.

The proof is immediate:

\[
\langle v,Qv\rangle
=\langle\Gamma v,A\Gamma v\rangle\ge0.
\]

The substantive content lies in the five source conditions, especially the
existence and lens compatibility of \(\Gamma\). Defining \(\Gamma\) from a
desired positive \(Q\) is a circular Cholesky factorization, not an
explanation.

## 4. Kitaev's exact finite interaction

For Wilson residue labels \(r,s\in\mathbb Z/4\), product-sector quarter
evolution contains

\[
K_{rs}=i^{rs}.
\]

The full coefficient matrix has rank four. On the \(D(S_3)\) dimension-two
by dimension-three supports it has rank three. On the even supports
\(\{0,2\}\times\{0,2\}\), it is the all-ones matrix and has rank one.

Thus generic product sectors require a shared interaction constructor, while
the even-support collapse is the exceptional separable restriction.

In the native ququart lens, \(K\) is generalized \(CZ_4\), a Clifford
operation. Under the binary encoding

\[
r=2a+b,\qquad s=2c+d,
\]

it becomes

\[
\boxed{
K=CS(b,d)\,CZ(a,d)\,CZ(b,c).}
\]

The controlled-\(S\) factor is non-Clifford in the frozen binary stabilizer
architecture. Hence:

\[
\boxed{
\text{one source interaction}
\not\Rightarrow
\text{one lens-independent capability class}.}
\]

The constructor is known; coherent Wilson-residue extraction and an admitted
implementation in the selected lens remain separate authorities.

## 5. Arithmetic consequence

In the theta/prime problem, positive Fock grammar supplies the local edge
energies. A successful RH reopening would need a source-derived
\(\Gamma_Y\) and independently positive \(A_Y\) such that

\[
\sum_{N\le Y}
\frac{\Lambda(N)}{\sqrt N}(I-S_N)^*(I-S_N)+C_Y
=\Gamma_Y^*A_Y\Gamma_Y
\]

on one common form domain, compatibly as \(Y\) varies.

No such constructor--lens factorization is currently known. Factoring the
already completed Weil/Pick form after assuming its positivity would be
circular. The interaction-constructor theorem therefore sharpens, but does
not reopen, the RH block.

## 6. Strominger consequence

The shared linearizer is an interaction constructor: it supplies ordering
that disconnected local capabilities cannot generate. Quorum replication is
an encoding lens for that constructor. Its faithfulness is indexed by the
fault grammar:

\[
\forall Q_1,Q_2,F,\qquad
(Q_1\cap Q_2)\setminus F\ne\varnothing.
\]

Changing from crash to Byzantine faults changes whether the lens faithfully
represents a single non-equivocating linear resource. The abstract
linearizer objective remains the same; the implementation theorem does not
transport across the lens change.

## 7. Benincasa consequence

For the reported

\[
R_7\oplus B_1\oplus M_3
\]

typing, analytic dressing with \(F(0)\ne0\) gives a triangular projection on
the original label tower and therefore a faithful lens on \(R_7\).
Pure cubic and higher jets lie outside that scoped lens. They enlarge
coefficient/readout data without acquiring Carrier-incidence authority.

This is the same rule: an intertwining lens transfers only the typed domain
on which its faithfulness was proved.

## 8. Hostile cases

A claimed orientation certificate fails if:

1. the interaction kernel has rank \(>1\) but only factor-local constructors
   are supplied;
2. a shared constructor exists abstractly but is unavailable in the admitted
   encoding lens;
3. extraction into the interaction labels is not source-derived;
4. the factorization is chosen after inspecting the desired orientation;
5. different non-gauge factorizations yield different completed forms; or
6. a proof on one fault, coefficient, or encoding lens is transported to
   another without reproof.

## 9. Durable refinement

\[
\boxed{
\text{completed orientation authority}
=
\text{source grammar}
+\text{shared interaction constructor}
+\text{faithful admitted lens}
+\text{independent positive carrier law}.}
\]

The interaction Schmidt rank diagnoses when the shared constructor is
unavoidable. It does not manufacture that constructor or authorize a lens.

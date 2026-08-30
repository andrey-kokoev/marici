# Source grammar does not determine completed interaction positivity

Author: \`marici.Nima\`

## 1. Cross-sector problem

Several Marici sectors now exhibit the same separation:

1. a source grammar determines admissible generators, their types, and their
   local signs;
2. coherent transport determines how those generators compose;
3. completion introduces interactions among sectors; and
4. positivity, safety, or physical orientation of the completed object
   requires information not contained in the local grammar alone.

The purpose of this packet is to state that separation as a finite theorem,
identify the missing datum, and give a reusable falsifier.

## 2. Typed setup

Let

\[
\mathcal V=\bigoplus_{i=1}^r\mathcal V_i
\]

be a labelled source module. A **source grammar** \(G\) fixes:

- the typed summands \(\mathcal V_i\);
- positive local forms \(q_i\ge0\);
- admitted constructors and composition laws;
- support and typing rules; and
- source symmetries.

A completed interaction is a Hermitian form \(Q\) on \(\mathcal V\) whose
diagonal restrictions are the prescribed local forms:

\[
P_iQP_i=q_i.
\]

The grammar may also fix a compressed readout \(R(Q)\), such as trace,
dimension, rank, scalar functional equation, or quorum count.

Define the **interaction ambiguity kernel**

\[
\boxed{
\mathcal K_G=
\left\{
K=K^*:
P_iKP_i=0\ \forall i,\quad
R(K)=0,\quad
K\text{ preserves the declared source symmetries}
\right\}.}
\]

Its elements change only completed interactions. They leave every local
source sector and declared scalar readout unchanged.

## 3. Separation theorem

**Theorem (grammar--orientation separation).** Suppose \(Q\) is one
completion admitted by \(G\). If there is a \(K\in\mathcal K_G\) and a vector
\(v\in\mathcal V\) such that

\[
\langle v,(Q+K)v\rangle<0,
\]

while \(Q+K\) remains admitted by all non-orientation clauses of \(G\), then
completed positivity is not a consequence of the source grammar.

More strongly, if two admitted completions \(Q_+\) and \(Q_-\) agree on all
local restrictions and compressed readouts but have different inertia, no
proof using only those common data can authorize the orientation of either
completion.

**Proof.** Every premise visible to the grammar and readout has the same
value on \(Q_+\) and \(Q_-\). A conclusion assigning the same positivity
verdict to both is false for one of them. Therefore any correct orientation
proof must use additional data that distinguish their interaction classes.
\(\square\)

## 4. Smallest finite falsifier

Take two one-dimensional positive source sectors and reciprocal exchange

\[
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Consider

\[
Q_+=
\begin{pmatrix}1&0\\0&1\end{pmatrix},
\qquad
Q_-=
\begin{pmatrix}1&2\\2&1\end{pmatrix}.
\]

Both:

- restrict to the same positive local form \(1\) on each sector;
- have trace \(2\);
- are invariant under \(J\); and
- preserve the same two-sector grammar.

But

\[
\operatorname{spec}(Q_+)=\{1,1\},
\qquad
\operatorname{spec}(Q_-)=\{3,-1\}.
\]

The interaction perturbation

\[
K=Q_--Q_+
=\begin{pmatrix}0&2\\2&0\end{pmatrix}
\in\mathcal K_G
\]

is therefore the smallest source-local falsifier. The negative witness is
\(v=(1,-1)\).

This example retains reciprocal symmetry and the scalar trace. The failure
cannot be blamed on negative local generators or asymmetric completion.

## 5. What suffices to transmit positivity

Source grammar *can* determine completed positivity when it includes one of
the following additional mechanisms.

### 5.1 Completely positive completion

There is a source-derived map

\[
\mathfrak C:\prod_i q_i\longmapsto Q
\]

that is completely positive and fixes every interaction block. Positivity
then follows functorially rather than from a fitted scalar readout.

### 5.2 Independent interaction domination

Writing

\[
Q=D+K,\qquad D=\bigoplus_iq_i\ge0,
\]

the source supplies a precompression inequality such as

\[
\left\|D^{-1/2}KD^{-1/2}\right\|\le1
\]

on the supported domain, or a monotone form law controlling the interaction
remainder.

### 5.3 Authorized quotient

The ambiguity kernel is proved to be exactly a source-authorized gauge
radical, and the quotient form is positive with zero residual ambiguity.

Without one of these mechanisms, positivity is an extra assertion about
completion.

## 6. Arithmetic instance

Positive Fock grammar supplies one positive primitive at \(p\), Adams
transport gives

\[
\Lambda(p^k)=\log p>0,
\]

and the determinant-line logarithm excludes squarefree connected atoms.
These facts determine the prime-power support and edge signs.

At cutoff \(Y\), completion is

\[
Q_Y=
\sum_{N\le Y}
\frac{\Lambda(N)}{\sqrt N}(I-S_N)^*(I-S_N)
+C_Y,
\]

where

\[
C_Y=Q_{\rm endpoint+\Gamma}^{(Y)}-2A_YI.
\]

Fock grammar does not orient \(C_Y\). The stopped-packet \(N=8\) matrix and
the Hermite Poisson hostile pair show that universal transport, reciprocal
symmetry, and chart positivity do not supply the missing domination law.

Here \(\mathcal K_G\) is the space of completion/counterterm changes invisible
to the positive prime grammar and admitted scalar symmetries. An RH-bearing
advance requires an independent preprojection inequality for this
interaction class.

## 7. Kitaev instance

Quantum dimension is a scalar compression of the Wilson character row.
The two typed dimension-six sectors in \(D(S_4\times D_4)\) have equal
dimension but different quarter packets:

\[
(282,0,180,0),
\qquad
(242,0,220,0).
\]

The full residue packet, not dimension, is the compositional invariant. Its
product is residue convolution in
\(\mathbb N[(\mathbb Z/4,\cdot)]\).

This is the non-Hermitian analogue of the theorem: scalar grammar does not
determine the completed interaction packet. Kitaev's replacement semiring
works because it retains exactly the interaction data discarded by
dimension.

## 8. Strominger instance

Quorum geometry fixes the minimum overlap

\[
I_{\min}=\max(0,2q-n).
\]

The same \(n=3,q=2\) geometry is safe under durable crash
non-equivocation and unsafe under one Byzantine fault. The interaction datum
is the admissible fault family:

\[
\forall Q_1,Q_2,\forall F\in\mathcal F,\qquad
(Q_1\cap Q_2)\setminus F\ne\varnothing.
\]

Replica counts and local signatures do not determine completed safety. The
fault hypergraph is the missing cross-sector interaction grammar. Once it is
source-authorized, the safety predicate is exact.

## 9. Benincasa instance

The current lower-point typing is

\[
R_7\oplus B_1\oplus M_3.
\]

The zero-background/conformal-mass projection retains \(R_7\), and analytic
dressing with \(F(0)\ne0\) is triangular on the original label tower.
Additional cubic and higher jets are coefficient/readout enlargement, not
new Carrier incidence.

This prevents a common completion error: interpreting directions introduced
by a coefficient completion as new primitive source sectors. The grammar
determines the Carrier; the completed response space may be larger without
changing that incidence authority.

This instance is presently supported by Benincasa's admitted message at
epistemic sequence 3396; a consolidated artifact was not located during this
audit.

## 10. Cross-sector prediction protocol

For any proposed explanation:

1. decompose the source into typed local sectors;
2. record exactly what the grammar fixes;
3. construct the completed interaction object before scalar compression;
4. compute \(\mathcal K_G\);
5. search for the smallest \(K\in\mathcal K_G\) that changes inertia, safety,
   capability, or physical incidence;
6. if one exists, reject grammar-only orientation;
7. if none exists, exhibit the completely positive completion, domination
   inequality, or authorized quotient that kills the kernel.

The decisive finite question is therefore

\[
\boxed{
\text{what source-derived operation fixes or dominates the interaction
ambiguity kernel?}}
\]

## 11. Durable cross-sector law

\[
\boxed{
\begin{array}{c}
\text{source grammar determines constructibility and local signs},\\
\text{coherent transport determines admissible composition},\\
\text{completed orientation requires control of interaction ambiguity}.
\end{array}}
\]

Local positivity is not incomplete global positivity. It is a different
typed theorem.

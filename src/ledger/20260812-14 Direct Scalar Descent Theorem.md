# Direct Scalar Descent Theorem

## Record

Date: 2026-08-12

Status: all-multiplicity theorem at generic formal massless tree kinematics. The scalar
associated grade descends through the full Parke--Taylor relation ideal. Boundary resonance and
the surface-function lift remain separate questions.

## Verdict

The missing scalar-provenance step in entry 11 can be proved without identifying the answer as
NLSM and without inserting the CHY representative.

Let

\[
a_n(\alpha)=\operatorname{gr}_R A_{{\rm scalar},n}(\alpha)
\]

for even (n), and set (a_n=0) for odd (n). The alternating scalar construction supplies
the following data directly:

1. cyclic symmetry;
2. homogeneity of Mandelstam degree one;
3. only simple allowed planar poles;
4. scalar boundary factorization
   \[
   \operatorname*{Res}_{P^2=0}a_n=a_La_R;
   \]
5. an Adler zero when any external momentum is soft.

These properties imply the photon-decoupling identity and the fundamental BCJ relation at every
even multiplicity. A general field-theory theorem then says that cyclic symmetry and the
fundamental BCJ relation generate the full KK and general BCJ relations. Consequently,

\[
\boxed{a_n(\ker q_n)=0,}
\]

where (q_n) sends cyclic words to Parke--Taylor twisted-cohomology classes. Thus the inverse
pairing construction

\[
\mathsf J_n=(I_n^\flat)^{-1}a_n
\]

is representation independent at all multiplicities.

Combined with the period-separation theorem of entry 11, this gives

\[
\boxed{
\mathsf J_n=[(\operatorname{Pf}'A_n)^2].
}
\]

## Formal kinematic setting

Work first on the Gram-free massless Mandelstam vector space

\[
V_n=
\left\{
s_{ij}=s_{ji},\quad s_{ii}=0,\quad
\sum_j s_{ij}=0
\right\}.
\]

Its dimension is

\[
\dim V_n=\frac{n(n-3)}2.
\]

The soft subspace for leg (i) is

\[
W_i=\{s\in V_n:s_{ij}=0\text{ for every }j\}
\simeq V_{n-1}.
\]

An identity on this formal space specializes to any fixed spacetime dimension. Working here
avoids accidental Gram relations during the contact-term argument.

For four distinct labels define the alternating four-cycle (C_{abcd}\in V_n) by

\[
(ab,bc,cd,da)=(+1,-1,+1,-1)
\]

and all other edge coordinates zero. One explicit basis of (V_n) is

\[
\left\{C_{123k},C_{12k3}:4\leq k\leq n\right\}
\cup
\left\{C_{12k\ell}:4\leq k<\ell\leq n\right\}.
\]

Its cardinality is

\[
2(n-3)+\binom{n-3}{2}=\frac{n(n-3)}2,
\]

and independence follows directly in edge coordinates.

## Two soft-contact lemmas

### Linear lemma

Let (L\in V_n^*). If

\[
L|_{W_i}=0
\qquad\text{for every }i,
\]

then (L=0) for (n\geq5).

Every basis four-cycle omits at least one external label and therefore belongs to the
corresponding (W_i). Hence (L) vanishes on a basis.

### Quadratic lemma

Let (Q\in\operatorname{Sym}^2(V_n^*)). For even (n\geq6), if

\[
Q|_{W_i}=0
\qquad\text{for every }i,
\]

then (Q=0).

Polarize (Q) to a symmetric bilinear form (b). The soft condition gives

\[
b(W_i,W_i)=0.
\]

It is enough to test (b) on pairs of alternating four-cycles. If their supports omit a common
label, both cycles lie in one (W_i), so their pairing vanishes.

For even (n\geq10), the union of two four-cycle supports contains at most eight labels and
there is automatically a common omitted label. At (n=8), the only extra case has disjoint
supports. Choosing a label (t) from the second support and using

\[
C_{abcd}=C_{abct}+C_{atcd}
\]

reduces it to pairs whose support union has size seven.

At (n=6), support unions of size at most five are immediate. Union-six cases reduce by the
same split unless the two labels unique to each cycle are adjacent in both cyclic orders. The
remaining permutation orbit is represented by the following exact identity in
\(\operatorname{Sym}^2V_6\):

\[
\begin{aligned}
C_{1342}\odot C_{1562}
={}&C_{1243}\odot C_{1235}
+C_{1243}\odot C_{1263}
-C_{1243}\odot C_{1236}\\
&-C_{1253}\odot C_{1245}
+C_{1245}\odot C_{1256}
-C_{1345}\odot C_{1356}.
\end{aligned}
\]

Every pair on the right omits a common label. Thus (b=0), and therefore (Q=0).

These lemmas are the only uniqueness input below. No general NLSM uniqueness theorem is used.

## Photon decoupling from scalar residues

Choose leg (1) and define

\[
D_n=
a_n(1,2,\ldots,n)
+\sum_{i=2}^{n-1}
a_n(2,\ldots,i,1,i+1,\ldots,n).
\]

The insertion-residue combinatorics is local on a cut polygon. On any allowed channel, retain
only the insertion positions for which that channel is planar. Cutting the polygon maps these
positions bijectively to all positions of leg (1) on one lower-point factor. The other factor
is fixed. Therefore every residue has the form

\[
\operatorname*{Res}D_n=a_LD_m
\]

or the same expression with left and right exchanged.

Assume lower even multiplicities vanish. Then (D_n) has no residues. Since every (a_n) has
only simple physical poles, (D_n) is a local homogeneous polynomial of Mandelstam degree one.
Every term has the scalar-derived Adler zero, so

\[
D_n|_{W_i}=0
\]

for every leg. The linear contact lemma gives (D_n=0).

The base case is

\[
D_4=s_{13}+s_{23}+s_{12}=0.
\]

Thus photon decoupling holds for all even (n).

## Fundamental BCJ from scalar residues

For the same distinguished leg define

\[
x_i=\sum_{j=2}^{i}s_{1j}
\]

and

\[
B_n=
\sum_{i=2}^{n-1}
x_i\,
a_n(2,\ldots,i,1,i+1,\ldots,n).
\]

There are two channel types relative to the reference cut between (n) and (2).

### Non-wrapping channel

For a consecutive block (P=[a,b]), collapse it to an internal label (I). The identity

\[
s_{1I}=\sum_{j=a}^{b}s_{1j}
\]

turns the residue bracket exactly into the lower-point fundamental combination. Hence

\[
\operatorname*{Res}_{P^2=0}B_n=a_LB_m
\]

up to exchanging the two factors.

### Wrapping channel

Let

\[
P=[a,\ldots,n]\cup[2,\ldots,b].
\]

The allowed insertion slots are (i=b,\ldots,a-1). Write

\[
z_i=\sum_{j=b+1}^{i}s_{1j},
\qquad
x_i=x_b+z_i.
\]

The (z_i) terms form the lower fundamental BCJ combination, while the constant (x_b)
multiplies the lower photon-decoupling sum. Thus

\[
\operatorname*{Res}_{P^2=0}B_n
=
a_L(B_m+x_bD_m)
\]

up to exchanging factors.

Simultaneous induction on (D_m) and (B_m) kills every residue. Therefore (B_n) is a local
homogeneous polynomial of Mandelstam degree two. It has an Adler zero for each leg: for legs
other than (1), each amplitude term vanishes; when leg (1) is soft, every (x_i) vanishes.
The quadratic contact lemma gives (B_n=0) for even (n\geq6).

At four points,

\[
a_4(2,1,3,4)=s_{23},
\qquad
a_4(2,3,1,4)=s_{12},
\]

and (s_{12}+s_{13}=-s_{23}), so

\[
B_4=s_{12}s_{23}-s_{23}s_{12}=0.
\]

Relabeling gives every fundamental BCJ relation.

## Closure of the full Parke--Taylor ideal

The remaining step is algebraic rather than dynamical. At generic field-theory kinematics,
cyclic symmetry together with the relabeled fundamental BCJ relations is a set of primary
relations: it generates the general KK relations and all general BCJ relations. In particular,
reflection and photon decoupling are included in the generated ideal.

Our scalar family has cyclic symmetry intrinsically: a cyclic step exchanges the two polygon
colours and sends (delta\mapsto-\delta), while the extracted even grade is unchanged. The proof
above supplies the other primary relation. Hence the scalar covector kills every relation among
Parke--Taylor classes, and

\[
a_n\in(H_n^-)^*.
\]

This is exactly the descent criterion of entry 11.

## Consequences and limits

Established now at generic genus-zero kinematics:

- the scalar grade is a representation-independent covector;
- inverse scalar/BAS pairing produces a unique half-class (mathsf J_n);
- its complete set of periods identifies it with
  ([({\rm Pf}'A_n)^2]);
- the low-point basis-change checks in entry 12 are audits of a theorem rather than the only
  evidence for it.

Not supplied by this proof:

- naive inversion at a resonant physical pole; use the nearby-cycle channel quotient of entry 13;
- the scalar-to-surface comparison (chi_\Sigma);
- a canonical cut-kernel primitive (omega_\Sigma);
- Jordan/QTDS strictification directly on the half-class;
- modular completion.

## Sources checked

- [NLSM inside Tr(Phi cubed)](https://arxiv.org/abs/2401.05483) for the scalar-derived pole
  structure, factorization, homogeneity, and Adler zero.
- [On Primary Relations at Tree-level in String Theory and Field Theory](https://arxiv.org/abs/1109.0685)
  for the theorem that cyclic symmetry and fundamental BCJ generate general field-theory KK and
  BCJ relations.
- [Amplitude Relations in Non-linear Sigma Model](https://arxiv.org/abs/1311.1133) for the
  independent application of the same primary-relation closure to even-point amplitudes.

## Decision

Close the direct scalar-descent gap at tree level. The next Nima question is no longer whether
(mathsf J) exists as a representation-independent normal symbol. It is whether the Jordan
strictification acts intrinsically on that half-symbol. The surface/Cut-Equation naturality test
remains with Frost, and the resonant six-point pairing block remains with YM.

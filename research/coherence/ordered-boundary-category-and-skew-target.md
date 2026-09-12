# Finite categorical skeleton for ordered boundary–Pfaffian theory

## Status

This specifies the ordinary categorical skeleton that must exist before any higher enhancement. It is intentionally ordered monoidal, not symmetric monoidal: arbitrary permutations do not preserve half-line order. Orientation-changing relabellings belong to a separate signed action.

## Source category

Define \(\mathbf{OrdInt}^{\mathrm{met},\pm}\).

### Objects

An object is a finite ordered metric configuration

\[
X=(a_0<\cdots<a_{n-1};\,\epsilon_X),
\]

where \(a_i\in\mathbb R_+\) are distinct and \(\epsilon_X\) is an orientation of the labelled frame. The empty configuration is admitted.

Equivalently, a nonempty object is encoded by its first position and positive gap word

\[
(a_0;d_0,\ldots,d_{n-2}),
\qquad d_i=a_{i+1}-a_i>0.
\]

### Monoidal product

If every point of \(X\) precedes every point of \(Y\), ordered concatenation is

\[
X\star_gY,
\]

where \(g>0\) is the separating gap. The product is strictly associative when the complete gap word is retained:

\[
(X\star_gY)\star_hZ
=
X\star_g(Y\star_hZ).
\]

The empty word is the unit. This is a nonsymmetric metric monoidal operation.

### Generating morphisms

1. **Orientation-preserving relabelling** of the supplied labels.
2. **Orientation reversal**
   \[
   \mathrm{rev}:X\to X^{\mathrm{op}}.
   \]
3. **Even cut/sewing** at a gap following an even number of points.
4. **Odd cut/sewing**, exposing one odd state on each side.
5. **Pair insertion** into a selected polarized gap.
6. **Metric translation** by a common positive displacement when the half-line endpoint remains admitted.
7. **Graph refinement** adding signed-log evaluation coordinates required by a declared transport word.

### Relations

The finite source relations are:

- associativity and empty-unit laws for ordered concatenation;
- \(\mathrm{rev}^2=1\);
- Koszul sign under labelled frame permutation;
- strict factorization at even cuts;
- odd--odd sewing through the cross-gap kernel;
- pair insertion multiplier \(z\) between pairs and \(z^{-1}\) inside a pair;
- functorial inclusion of trace-depth fibers \(\Gamma_k^+\to\Gamma_{k+1}^+\).

No relation identifies arbitrary subdivisions or arbitrary permutations.

## Target category

Define \(\mathbf{SkBdry}_{\mathbb Z_2}\).

### Objects

An object is a tuple

\[
\mathbb K=(C,F,L_{\rm in},L_{\rm out},q_{\rm in},q_{\rm out},\lambda,\pi),
\]

where:

- \(C\) is a finite based perfect complex;
- \(F:C\to C^\vee[1]\) is skew self-dual;
- \(L_{\rm in},L_{\rm out}\) are boundary lines;
- \(q_{\rm in}:H(C)\to L_{\rm in}\) and \(q_{\rm out}:H(C)\to L_{\rm out}\) are boundary charges;
- \(\lambda\) is the Pfaffian determinant line with its based trivialization;
- \(\pi\in\mathbb Z_2\) is homological parity.

The basis and Pfaffian trivialization are retained because forgetting them erases metric torsion.

### Morphisms

Morphisms are based chain maps preserving the skew form and boundary charges. A weak morphism may preserve them through a specified chain homotopy and determinant-line comparison; weak morphisms belong to the later enriched category, not this strict skeleton.

### Composition

Boundary sewing is a relative contraction

\[
\mathbb K_X\odot_g\mathbb K_Y.
\]

On odd residual lines its scalar component is

\[
q_{\rm out}(X)\,e^{-tg}\,q_{\rm in}(Y).
\]

Parity adds modulo two. Pfaffian lines tensor.

## Finite functor

For an ordered configuration \(X\), let \(M_X\) be its antisymmetric chain kernel and define

\[
\mathcal A_1(X)
=
\left(
\mathbb K_{M_X},
q_{\rm in},q_{\rm out},
\operatorname{PfLine}(M_X),
|X|\bmod2
\right).
\]

Its minimal model is

\[
\bigoplus_rH(e^{-td_{2r}})
\oplus
\mathbb K^{|X|\bmod2}.
\]

The functor sends:

- even objects to Pfaffian torsion amplitudes;
- odd objects to bicharged residual lines;
- even cuts to tensor multiplication;
- odd cuts to boundary contraction;
- reversal to dualization and orientation sign.

## Complete odd--odd sewing square

For contiguous odd configurations \(X,Y\), require the diagram

\[
\begin{array}{ccc}
\mathcal A_1(X)\odot_g\mathcal A_1(Y)
&\xrightarrow{\text{charge contraction}}&
q_{\rm out}(X)e^{-tg}q_{\rm in}(Y)\\
\downarrow\text{microscopic sewing}&&\downarrow=\\
\mathcal A_1(X\star_gY)
&\xrightarrow{\operatorname{Pf}}&
\operatorname{Pf}(M_{X\star_gY})
\end{array}
\]

and the established rank-one block identity gives

\[
\operatorname{Pf}(M_{X\star_gY})
=u_X^TB_{XY}u_Y
=q_{\rm out}(X)e^{-tg}q_{\rm in}(Y).
\]

Thus this square commutes strictly.

## Boundary of the skeleton

The strict category does not yet identify different elimination orders, graph refinements, or weakly equivalent boundary presentations. Those comparisons must become 2-cells in the enhancement. The next exact task is to construct the comparison between two elimination orders and determine whether its space of choices is contractible.

---
authors:
  - marici.Nima
date: 2026-08-18
---
# 738 — The Global Principal Cell Restricts Vertexwise Across Resolved Corners

## Identity gate from Entry 737

Entry 736 writes a local augmented source as

\[
K_{L_1,i}\oplus \mathbbm 1_{\rm principal},
\]

but that local notation alone does not say whether the principal summand is
shared between the corners incident to one divisor.  The answer is fixed by
the global source complex of Entry 511, before taking indicial kernels.

There the principal cell is one module \(P\) in

\[
D_{-1}(f,p)=
\bigl(d(f)+Kp,\;\widehat H(f)+Ep\bigr).
\]

It is the conormal cell of the single principal equation \(K=0\).  Pullback
to a resolved divisor \(D_i\), followed by restriction to either incident
corner, therefore gives the two restrictions of the same vertex section
\(p_i\).  Restriction does not replace \(P|_{D_i}\) by an independent direct
sum indexed by incidence germs.

Hence the principal cells in the resolved Čech object are vertex-labelled:

\[
P|_{D_1}\oplus P|_{D_2}\oplus P|_{D_3},
\]

not six unrelated cells \(p_{i,ij}\).  The incidence-local alternative in
Entry 737 would require a further functor

\[
P|_{D_i}\longmapsto
\bigoplus_{j\ne i} P|_{D_i\cap E_{ij}},
\]

together with independent generators before the Čech differential.  No such
operation occurs in Entries 511, 729–736, or in the blowup restriction maps.
Introducing it would change the source complex.

## Horizontal consequence

With orientations \(1\to2\), \(1\to3\), and \(2\to3\), the rational
principal-line map is therefore the vertex-shared matrix from Entry 737:

\[
\delta_{\rm pr}=
\begin{pmatrix}
0&1&0\\
0&0&1\\
0&-1&1
\end{pmatrix}.
\]

It has rank two.  Its horizontal cokernel is the canonical line detected by

\[
\lambda(x_{12},x_{13},x_{23})=x_{12}-x_{13}+x_{23}.
\]

Thus the incidence-local immediate-vanishing branch is closed for the
already declared labelled principal-gradient complex.

## Deliberate limit

This establishes only the \(E_1\)-page horizontal shadow.  The principal
cell has an internal differential through \((K,E)\), and the exceptional
targets have their own indicial differentials.  Therefore

\[
\boxed{
\dim\operatorname{coker}(\delta_{\rm pr})=1
\quad\not\Rightarrow\quad
\dim\mathbb H(\operatorname{Tot})=1.
}
\]

The class represented by \(\lambda\) survives only if the exact local
principal columns of Entry 736 extend to chain maps whose total differential
neither hits nor kills it.

## Evidence

- Entry 511's global principal module \(P\) and its differential;
- Entries 735–736's source-labelled corner maps;
- Entry 737's two possible horizontal matrices;
- allocator claim `seqclaim-73370218b12ca891767a6b8e`;
- epistemic event `ev-000000000351-6d3a0fcc-1662-42e5-95a4-da9f72911f0e`.

## Next falsifier

Export the internal degree and differential of \(P|_{D_i}\) and of the three
principal target lines.  Assemble the smallest rational invariant bicomplex
containing these terms and compute whether \(\lambda\) survives its total
differential.  Homogeneous resonance directions remain present in the full
local complexes even though their first-corner columns vanish.

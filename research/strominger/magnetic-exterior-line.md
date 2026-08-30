# Magnetic rank is a transported exterior-power section

Companion to `checkers/magnetic_exterior_line_checks.py` (6/6, exit 0) and
`results/magnetic_exterior_line.json`.

Let (M_{g,q,k}) be a component matrix with (r) source columns.  Its
coordinate-free rank detector is the top column exterior power

\[
s_{g,q,k}=\bigwedge^r M_{g,q,k}.
\]

After choosing the monomial target basis, the coordinates of this section are
the maximal minors (\Delta_I).  Cauchy-Binet gives the integral invariant

\[
\boxed{
\|s_{g,q,k}\|^2
=\det(M_{g,q,k}^{T}M_{g,q,k})
=\sum_{|I|=r}\Delta_I^2.
}
\]

Because the entries are integral, this quantity vanishes if and only if every
Plucker coordinate vanishes.  Hence it distinguishes the invariant events:

\[
\begin{array}{c|c}
\Delta_{I_0}=0,\ \Delta_{I_1}\ne0&s\ne0:\ \text{chart boundary}\\
\Delta_I=0\ \text{for every }I&s=0:\ \text{transport failure}
\end{array}
\]

The checker verifies the Cauchy-Binet identity by explicit exact coordinate
enumeration on a regular component.  At each of the seven known even chart
onsets

\[
(g,q,k)=(2r,4r+8,r+4),\qquad1\le r\le7,
\]

the preferred coordinate is zero but the uniform neighboring coordinate
obtained by (1\mapsto3) is nonzero.  Therefore (s_{g,q,k}\ne0).

At the genuine fibers

\[
(g,q,k)=(2,1,0),\qquad(2,7,3),
\]

the Gram determinant is exactly zero and the column nullity is exactly one.
Changing either grade or the nearby component label restores a positive Gram
determinant in the tested transverse fibers.

Thus the primitive exceptional circuits are degeneration fibers of the
exterior section.  They are not attached to the zeros of a preferred
coordinate; they appear only where the complete Plucker vector vanishes.

## Transport formulation

Cutoff extension should be regarded as a morphism of determinant lines

\[
L_k=\bigwedge^{r_k}\operatorname{im}M_{g,q,k}
\longrightarrow
L_{k+1}=\bigwedge^{r_{k+1}}\operatorname{im}M_{g,q,k+1}.
\]

The previously computed scalar determinant factors are local expressions for
this morphism after choosing a chart.  A singular local expression is harmless
when another trivialization survives.  A genuine residue is the cokernel fiber
where the invariant line map loses rank.

## Scope

The exterior criterion is an exact linear-algebra theorem.  Its application
here is exact on the seven chart onsets, the two exceptional fibers, and four
nearby transverse fibers.  An unbounded magnetic theorem still requires a
symbolic atlas or a direct proof that this exterior section is nowhere zero
outside the two exceptional loci.

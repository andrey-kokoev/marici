# The two-adjoint vacuum supplies a reference but leaves the portal ratio free

Work package: WP618  
Owner: marici.Figueiredo

## Bounded question

Does the admitted source-free WP438 two-adjoint vacuum repair WP617 by
selecting the centered charge geometry, or does it only provide a relational
reference in which a free portal coefficient can be fitted?

## Source-derived reference

Use the normalized WP438 representative

\[
A=\operatorname{diag}(1,-1,0),
\qquad
D=\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\end{pmatrix}.
\]

Its quadratic composite defines

\[
H=
\frac32\left[
A^2+D^2-\frac13\operatorname{Tr}(A^2+D^2)I
\right]
=
\operatorname{diag}(1,1,-2).
\]

This is not an imported flavor axis. It is constructed from the prepared
two-adjoint packet and is the primitive generator of its residual stabilizer.
It commutes with both \(A\) and \(D\).

Both \(A\) and \(H\) are written in primitive integral cocharacter
normalization. This freezes their relative coordinate convention before
introducing \(r\); an arbitrary rescaling of either basis generator is not
silently counted as a different physical portal.

The smallest charge-lens family using that reference is

\[
X(r)=H+rA
=
\operatorname{diag}(1+r,1-r,-2).
\]

The parameter \(r\) is the relative portal normalization between two
source-derived directions. Algebraic availability of both directions does not
fix that normalization.

## Exact target and hostile points

At

\[
r=\frac35,
\]

the lens is

\[
X\left(\frac35\right)
=
\frac25\operatorname{diag}(4,1,-5),
\]

which lies on the centered WP614 target ray. Its three absolute gaps have
ratio

\[
1:2:3.
\]

But the same frozen \(A,D,H\) source packet also admits, for example,

\[
r=1,
\]

whose gap ratio is

\[
1:1:2.
\]

More generally, the signed gaps are

\[
2r,\qquad 3-r,\qquad 3+r.
\]

Thus the source-free two-adjoint vacuum constructs a continuous family of
inequivalent charge geometries. The observed relation selects \(r=3/5\) from
that family; the vacuum does not.

## Probe factorization

If \(X(r)\) is the Higgs direction for a family-vector sector, the three
positive-root mass squares are proportional to

\[
(2r)^2,\qquad(3-r)^2,\qquad(3+r)^2.
\]

At the target ratio their normalized values are \(1:4:9\). A resolved
three-pole spectrum therefore measures \(|r|\) and directly falsifies the
target portal geometry when the ratios disagree.

That ordinary spectrum has a kernel:

\[
X\longmapsto-X
\]

leaves every mass square unchanged. A sign-sensitive record requires the
source-derived reference port \(H\). The coherent pairing

\[
\operatorname{Tr}(XH)=6
\]

changes sign when \(X\) is reversed while \(H\) is retained.

This is explicitly a new relational experiment over the stabilizer groupoid
of the jointly prepared \(A,D,H\) packet. It does not recover an absolute sign
of the original unreferenced mass experiment.

## Disposition

The WP438 vacuum supplies:

- a source-derived relational carrier;
- an orientation reference;
- a presentation rigidifier once \(r\) is declared;
- no numerical charge-gap selector.

The smallest exact falsifier of selection is the pair \(r=3/5\) and \(r=1\):
the same source vacuum supports both while their gap geometries differ.

A complete physical instrument must resolve all three family-root vector
masses and a coherent \(H\)-referenced interference channel, demonstrate that
both records arise from the same prepared two-adjoint vacuum, and control any
additional Higgs contributions. Selection authority requires a symmetry,
representation multiplicity, or source-vacuum equation deriving \(r=3/5\)
before inspecting flavor data.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp618_two_adjoint_relational_charge_lens.py

The generated result is
`research/flavor/results/wp618_two_adjoint_relational_charge_lens.json`.

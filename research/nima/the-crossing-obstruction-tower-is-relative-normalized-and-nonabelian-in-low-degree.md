# The crossing obstruction tower is relative, normalized, and nonabelian in low degree

## Record

The spectral coherence tower is a relative cubical theory. Let \(B=B_-\cup B_+\) be the two contour-admissible bulk complexes and let \(W\) be the crossing wall. The relevant object is the pair
\[
(B,W),
\]
not an absolute bulk cube. The finite crossing determinant is a wall transgression relating the two bulk determinant systems.

Normalization requires every identity edge and every degenerate cube to carry unit transport or unit residual. This removes artifacts caused solely by inserting identities, repeated parameters, or degenerate cutoff steps.

## Degree one: transport

Each oriented edge \(e:x\to y\) carries an intertwiner
\[
g_e:\mathcal F_x\longrightarrow\mathcal F_y,
\qquad
g_{\bar e}=g_e^{-1},
\]
where \(\mathcal F\) is the defect fiber, determinant fiber, or their exact coupled object. Identity edges have \(g_{\mathrm{id}}=I\).

This is nonabelian data. It cannot initially be replaced by logarithms or additive one-cochains.

## Degree two: ordered face defect

Choose a base vertex \(v_f\) and oriented boundary
\[
\partial f=e_4e_3e_2e_1.
\]
The face residual is the ordered product
\[
\Omega_f=g_{e_4}g_{e_3}g_{e_2}g_{e_1}
\in\operatorname{Aut}(\mathcal F_{v_f}).
\]
Changing the base path conjugates \(\Omega_f\). Hence the invariant datum is its transported conjugacy class unless a source-authorized trivialization has been fixed.

For a cube with a common base vertex \(v\), each face residual must first be transported to \(v\):
\[
\widetilde\Omega_f
=
h_f^{-1}\Omega_f h_f,
\]
where \(h_f\) is the selected base-path transport. Only these conjugated residuals can enter a common boundary product.

## Degree three: cubical Bianchi obstruction

The cube obstruction is the oriented, ordered product of its six transported face defects:
\[
\mathfrak B_3(C)
=
\overrightarrow{\prod_{f\subset\partial C}}
\widetilde\Omega_f^{\epsilon(f)}.
\]
This is a nonabelian Bianchi or associator obstruction. Its order is fixed by an explicit shelling of the oriented boundary. Merely multiplying determinants or scalar phases of the faces discards commutators.

If every face residual is identity, then \(\mathfrak B_3=I\). If face residuals lie in a common center, the product may be interpreted abelianly. Before either condition, ordinary additive coboundary notation is unauthorized.

## Relative wall transgression

The wall supplies clutching maps \(\kappa\) between restrictions of the minus and plus bulk systems. For a wall cell \(\sigma\), define the relative residual by comparing:

1. transport in \(B_-\), followed by clutching;
2. clutching first, followed by transport in \(B_+\);

with the finite crossing determinant factor inserted. Symbolically,
\[
\tau_W(\sigma)
=
\kappa_{\partial_1\sigma}\,g^-_\sigma
\bigl(g^+_\sigma\kappa_{\partial_0\sigma}\bigr)^{-1}.
\]
Thus the crossing determinant is a transgression cochain on \(W\), not an independent absolute class in either bulk.

## Degree four: relative anomaly

Transport every side-cube obstruction and wall-prism residual to one base object. Their oriented boundary product defines
\[
\mathfrak A_4(B,W).
\]
There are three outcomes:

- \(\mathfrak A_4=I\): relative coherence closes.
- \(\mathfrak A_4\ne I\) but is central: it descends to a relative determinant-gerbe/anomaly class.
- \(\mathfrak A_4\) is noncentral: no higher abelian class is defined; the tower stops as incoherent.

The central anomaly is therefore available only after the nonabelian lower-stage transport has been performed and shown to centralize at the final gate.

## Mandatory hostile

Let \(A,B\in\mathrm{GL}_2(\mathbb C)\) fail to commute. Assign four transported face defects
\[
\widetilde\Omega_1=A,\quad
\widetilde\Omega_2=B,\quad
\widetilde\Omega_3=A^{-1},\quad
\widetilde\Omega_4=B^{-1},
\]
and unit defects to the remaining faces. Every determinant multiplies to one:
\[
\prod_i\det\widetilde\Omega_i=1.
\]
But the ordered boundary product is the commutator
\[
ABA^{-1}B^{-1},
\]
which need not be identity. Therefore scalar face phases can report perfect cancellation while the actual cube remains incoherent.

A concrete unipotent pair,
\[
A=
\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
B=
\begin{pmatrix}1&0\\1&1\end{pmatrix},
\]
has determinant one in every factor and a nontrivial commutator. Any checker that only multiplies scalar determinants necessarily misses this defect.

## Typed RH gate

The categorical RH gate on the admitted source-generated component must verify, in order:

1. normalized source-authorized edge intertwiners;
2. identity of nonabelian ordered face residuals;
3. identity of transported degree-three Bianchi residuals;
4. natural relative transgression of the finite crossing determinant;
5. identity of the degree-four relative residual, or an explicitly classified central anomaly outside the claimed RH component.

No later scalar calculation may repair failure at an earlier nonabelian gate.

## Next constructor

Turn the tower into a finite checker contract. Its input must include oriented cells, source and target fibers, edge matrices, base paths, shelling order, wall clutching matrices, and crossing determinant factors. The checker should reject dimension mismatches, absent base-path conjugations, nonunit degenerate cells, and any attempt to scalarize before centrality has been established.

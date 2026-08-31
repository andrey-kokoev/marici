# The grade-six Adams-seam diamond is the first source-extracted cell complex

## Source extraction verdict

The full Adams-seam parameter complex cannot yet be frozen without invention. The current records source-authorize:

- moving-seam Hilbert fibers \(E_a\);
- unitary transport \(T_{b\leftarrow a}=R_b^{-1}R_a\);
- prime-power scales \(a_{p,k}=k\log p\);
- Euler half-density weights
  \[
  w_{p,k}=\frac1k p^{-k/2};
  \]
- positive Adams ratios
  \[
  \rho_r(p,k)=\frac1r p^{-(r-1)k/2};
  \]
- exact geometric and scalar cocycle laws.

They do not yet source-authorize:

- type-fiber maps \(A_{r;p,k}\);
- endpoint attachment;
- archimedean attachment;
- a complete global sewing object.

Therefore the maximal frozen object is a geometric-plus-coefficient subcomplex. The first full typed complex remains a constructor slot.

## The first source-derived finite inventory

Fix a prime \(p\) and the grade set
\[
K=\{1,2,3,6\}.
\]
Define vertices
\[
v_k=(p,k,E_{k\log p},L_{p,k}),
\]
where \(L_{p,k}\) is the one-dimensional Euler coefficient line.

The four authorized geometric-plus-coefficient edges are
\[
e_2:v_1\to v_2,
\qquad
e_3:v_1\to v_3,
\]
\[
f_3:v_2\to v_6,
\qquad
f_2:v_3\to v_6.
\]

Their transport operators are
\[
\Psi^{gc}_{r;p,k}
=
M_{\rho_r(p,k)}\otimes T_{rk\log p\leftarrow k\log p}.
\]

The superscript \(gc\) means geometric plus coefficient. It excludes the missing type-fiber map.

## Source-derived 2-cell

The moving-seam cocycle gives
\[
T_{6\log p\leftarrow2\log p}
T_{2\log p\leftarrow\log p}
=
T_{6\log p\leftarrow\log p},
\]
and
\[
T_{6\log p\leftarrow3\log p}
T_{3\log p\leftarrow\log p}
=
T_{6\log p\leftarrow\log p}.
\]

The coefficient cocycle gives
\[
\rho_3(p,2)\rho_2(p,1)
=
\rho_2(p,3)\rho_3(p,1)
=
\rho_6(p,1).
\]

Therefore the geometric-coefficient paths agree:
\[
\Psi^{gc}_{3;p,2}\Psi^{gc}_{2;p,1}
=
\Psi^{gc}_{2;p,3}\Psi^{gc}_{3;p,1}.
\]

This supplies one source-derived square cell
\[
\sigma_{2,3;p}.
\]

## Cellular chain complex

Orient edges as above and order
\[
C_0=\mathbb Z\langle v_1,v_2,v_3,v_6\rangle,
\]
\[
C_1=\mathbb Z\langle e_2,e_3,f_3,f_2\rangle,
\qquad
C_2=\mathbb Z\langle\sigma\rangle.
\]

The boundary map \(\partial_1:C_1\to C_0\) has columns
\[
\partial_1e_2=v_2-v_1,
\]
\[
\partial_1e_3=v_3-v_1,
\]
\[
\partial_1f_3=v_6-v_2,
\]
\[
\partial_1f_2=v_6-v_3.
\]

In the ordered bases,
\[
[\partial_1]
=
\begin{pmatrix}
-1&-1&0&0\\
1&0&-1&0\\
0&1&0&-1\\
0&0&1&1
\end{pmatrix}.
\]

Choose the square orientation
\[
\partial_2\sigma=e_2+f_3-f_2-e_3.
\]
Then
\[
[\partial_2]
=
\begin{pmatrix}
1\\
-1\\
1\\
-1
\end{pmatrix}.
\]

Direct substitution gives
\[
\partial_1\partial_2=0.
\]

## Additive topology

The 1-skeleton is connected with four vertices and four edges, so
\[
b_1^{\mathrm{graph}}=4-4+1=1.
\]
Its unique cycle is the grade-six diamond.

The 2-cell spans that cycle, hence
\[
H_1(K_{p,6}^{gc};\mathbb Z)=0.
\]

Thus no abelian Wilson coordinate survives in the geometric-coefficient diamond.

## Ordered topology

Choose the spanning tree
\[
\{e_2,e_3,f_3\}.
\]
The non-tree edge \(f_2\) generates the based loop
\[
\gamma=f_2e_3(e_2f_3)^{-1}
\]
up to composition convention.

The square relation imposes
\[
f_3e_2=f_2e_3.
\]
Therefore
\[
\pi_1(K_{p,6}^{gc})=1.
\]

The ordered geometric-coefficient holonomy is exactly the identity.

## The typed lift is supplied by source grade reindexing

A full edge is
\[
\Psi_{r;p,k}
=
M_{\rho_r(p,k)}
\otimes T_{r;k}
\otimes S_r,
\]

where the source map is

\[
S_re_{p,k}=e_{p,rk}.
\]

The successor packet
`source-grade-reindexing-fills-the-typed-grade-six-adams-diamond.md` proves
that \(S_r\) is continuous on the projective exponential completion and
intertwines the weighted analytic incidence. It satisfies

\[
S_3S_2=S_2S_3=S_6.
\]

Thus the geometric, coefficient, and type-fibre boundary words are all filled.
The former spurious logical cycle does not survive on the retained labelled
source.

## Primitive, square, and connected vertex typing

The four vertices cross operator classes:

- \(v_1\): primitive;
- \(v_2\): square;
- \(v_3,v_6\): connected.

Therefore the missing type maps cannot be replaced by identities. Doing so would collapse distinct operator-ideal classes and falsely fill the typed square.

The grade-six diamond is high information because it compares two paths crossing these classes in different orders.

## Endpoint and archimedean cells

The local recollement record source-authorizes the shape of endpoint and Fourier boundary operations, including the two-port observer plane
\[
\operatorname{span}\{\epsilon_p,\mu_p\}
\]
and the dihedral relation
\[
BA_p(a)B=A_p(a)^{-1}.
\]

But this does not yet attach endpoint or archimedean cells to the grade-six Adams-seam diamond. The global restricted-product sewing object remains open.

Therefore no endpoint or archimedean 2-cell is included in the frozen inventory.

## Reciprocal sewing status

Fourier–Poisson transport is natural inside each moving cut bundle:
\[
F_bT_{b\leftarrow a}=T_{b\leftarrow a}F_a.
\]
This gives geometric sewing naturality, but not the completed reciprocal-sheet attachment required by the RH constructor.

The frozen complex records this as an available operator relation, not as a global reciprocal cycle.

## First topological falsifier

Delete or mistype \(\sigma\). Then
\[
H_1\cong\mathbb Z,
\qquad
\pi_1\cong\mathbb Z,
\]
and a spurious grade-six Wilson cycle survives despite exact source cocycles.

This is the requested missing-cell hostile.

## First coefficient-sensitive falsifier

Keep the additive boundary relation but attach type maps for which
\[
\Omega
=
(A_{2;p,3}A_{3;p,1})^{-1}
A_{3;p,2}A_{2;p,1}
\neq I.
\]
The abelian cell complex still has
\[
H_1=0,
\]
while the ordered type holonomy is \(\Omega\).

This is the requested case where the abelian cycle vanishes but ordered commutator/path holonomy remains nontrivial.

## Frozen packet

The first source-extracted packet contains:

- four typed geometric-coefficient vertices;
- four authorized edges;
- one source-derived square;
- explicit \(\partial_1,\partial_2\);
- verified \(\partial_1\partial_2=0\);
- \(H_1=0\);
- trivial geometric-coefficient \(\pi_1\);
- one spanning-tree choice;
- identity ordered geometric-coefficient holonomy;
- a declared missing type-fiber square;
- endpoint, archimedean, and global reciprocal attachments marked absent.

## Next source obligation

Construct
\[
A_{2;p,1},
A_{3;p,1},
A_{3;p,2},
A_{2;p,3}
\]
from source data and test the grade-six square.

Only after that cell is filled may the parameter complex be enlarged with endpoint, archimedean, and reciprocal sewing cells. This prevents topology from being invented around formal constructor slots.

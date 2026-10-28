# Persistent shared-seam compatibility is an observability condition

Date: 2026-10-22. Recorded and independently checked by `marici.Strominger`.

## Question and claim boundary

When do independently updated local coefficient triples remain compatible on one shared oriented edge? This note records the conversation's conditional pairing theorem using the [documented two-triangle source](../nima/two-triangles-shared-edge-half-phase.md), without assigning P/E identities. The operator's question whether established mathematics already solves the problem redirected the investigation to linear gluing and observability; that question is search provenance, not evidence.

SCC obligation: route/readout compatibility on a fixed five-coordinate real cochain carrier, with specified local linear endomorphisms. The local-to-global operation exists only on the invariant compatibility subspace. Composition index denotes repeated applications, not physical time.

## Source and gluing

Retain triangles \(T_1=(AB,BC,CA)\) and \(T_2=(BA,AD,DB)\). There are four vertices, five undirected edge supports and six directed edge occurrences, grouped into two triangle occurrences. Declare \(BA=-AB\) for coefficient readings, not as an identification of occurrences.

For \(x=(a,b,c,d,e)\), set

\[
R_1x=(a,b,c),\qquad R_2x=(-a,d,e),\qquad h=(1,0,0).
\]

The global coefficient space is the fiber product

\[
V=\{(y_1,y_2)\in\mathbb R^3\oplus\mathbb R^3:h(y_1+y_2)=0\}\cong\mathbb R^5.
\]

A product of local linear operations descends precisely when it preserves this kernel. For a fixed common local operator \(T\), define the mismatch and its successive seam readings by

\[
z=R_1x+R_2x=(0,b+d,c+e),\qquad m_n=hT^nz.
\]

## Theorem and proof

For any linear \(T:\mathbb R^3\to\mathbb R^3\), the maximal persistently compatible global subspace is

\[
V_T=(R_1+R_2)^{-1}(N_T),\qquad
N_T=\bigcap_{n\ge0}\ker(hT^n)=\ker\mathcal O_T,
\qquad
\mathcal O_T=\begin{pmatrix}h\\hT\\hT^2\end{pmatrix}.
\]

The first equality is the seam equation at every composition index. Cayley-Hamilton expresses every higher power as a linear combination of \(I,T,T^2\), proving the finite-to-all-indices implication. This is the standard unobservable-subspace/observability-rank criterion, applied to a mismatch rather than to a physical dynamical state. Necessity and sufficiency are linear identities; no sampling or limit is involved.

The source operators are

\[
C(a,b,c)=(b,c,a),\qquad
S=\frac13\begin{pmatrix}2&2&-1\\-1&2&2\\2&-1&2\end{pmatrix},\qquad S^2=C.
\]

Here \(\mathcal O_C=I_3\), and

\[
\mathcal O_S=\begin{pmatrix}1&0&0\\2/3&2/3&-1/3\\0&1&0\end{pmatrix},
\qquad \det\mathcal O_S=1/3.
\]

Both pairs \((T,h)\) are observable. Therefore

\[
V_C=V_S=K(\mathbb R^3),\qquad
K(a,b,c)=(a,b,c,-b,-c),\qquad R_2K=-R_1K=-I_3.
\]

This is the maximal set, not merely a convenient chosen subspace: any persistently gluable input has zero mismatch. Conversely, \(T^nR_2K=-T^nR_1K\) guarantees compatibility for every index. The glued operation is \(Kv\mapsto KTv\); it is not the serial embedded operation.

For \(T=I\), \(N_I=\ker h\) has dimension two, and \(V_I=\mathbb R^5\). Thus geometry alone does not force opposition of the complete triples.

| Operator | Observability rank | Unobservable dimension | Compatible global dimension |
| --- | --- | --- | --- |
| \(C\) | 3 | 0 | 3 |
| \(S\) | 3 | 0 | 3 |
| \(I\) | 1 | 2 | 5 |

## Reference exchange and protocols

Define

\[
J(a,b,c,d,e)=(-a,d,e,b,c).
\]

Then \(J^2=I\), \(R_1J=R_2\), \(R_2J=R_1\), and \(JK(v)=K(-v)\). Exchange is defined on all \(V\); persistent synchronization is not its prerequisite.

For the source's serial embeddings

\[
T_i=I_5+R_i^T(T-I_3)R_i,
\]

orthogonality of \(J\) gives \(JT_1J=T_2\) and \(J(T_2T_1)J=T_1T_2\). For both \(C\) and \(S\), the fixed-frame difference \(T_2T_1-T_1T_2\) has rank two. Conjugacy under a transported reference is not commutation in a fixed reference.

The circulation functionals are \(L=a+b+c\), \(R=-a+d+e\), and \(O=L+R=b+c+d+e\). Seam cancellation is an incidence identity. On \(K\), \(R=-L\), \(O=0\), and synchronized \(C,S\) preserve each local circulation. Serial operations preserve their own triangle's circulation but need not preserve the other or \(O\). Both triangle occurrences survive all these distinctions.

## Falsifiers and disposition

- Universal simultaneous gluing is false: \(x=(0,1,0,0,0)\) has initial mismatch reading zero, but the first \(C\) and \(S\) readings are respectively \(1\) and \(2/3\).
- Geometry-forced synchronization is false: identity updates leave the same nonzero mismatch invisible at every index.
- Zero outer circulation is insufficient: \(x=(0,1,-1,0,0)\) has \(O=0\), but its first cyclic seam mismatch is \(1\).
- Serial substitution is false: \(C_2C_1K(0,1,0)=(1,0,0,0,-1)\), outside \(K(\mathbb R^3)\).

Surviving claim: persistent simultaneous gluing for the specified observable operators forces opposite local coefficient triples. It does not select simultaneous rather than serial processing, supply a reconciliation of conflicting independent proposals, identify triangle occurrences, establish particle identities or counts, or bind this seam to the cube or quadrangulation orientation cover. Those separate interpretation branches remain deferred. The [revision-scoped polarity-cover audit](polarity-flip-cover-source-audit.md) records why the inspected orientation and normal-sign cocycles do not establish source polarity flip transport; it does not alter this local theorem.

## Verification and references

Run the dependency-free exact checker:

```sh
python research/strominger/checkers/check_shared_seam_observability.py
```

Receipt: [shared-seam-observability.json](results/shared-seam-observability.json). It records exact observability matrices, global constraint ranks, exchange identities, hostile residuals, and source/checker SHA-256 digests. The checker imports source arithmetic without running the source's artifact-writing main routine. No formal proof assistant or browser verification is claimed.

- [Source packet](../nima/two-triangles-shared-edge-half-phase.md), especially the simultaneous-update and synchronized-protocol sections.
- [Source checker](../nima/checkers/check_two_triangle_half_phase.py).
- Standard terminology: Eduardo D. Sontag, *Mathematical Control Theory: Deterministic Finite Dimensional Systems*, 2nd ed., Springer, 1998, linear observability; DOI [10.1007/978-1-4612-0577-7](https://doi.org/10.1007/978-1-4612-0577-7). The complete finite-dimensional proof needed here is given above; this citation is not a claim of a newly audited theorem number.
- Public summary: [ledger entry 4330](/research/ledger/20261022-4330-persistent-shared-seam-compatibility-is-an-observability-condition/).
- [Persistent-seam P/E conjecture](persistent-seam-pe-conjecture.md): subsequent working interpretation and open source-protocol selection, linked into the current nets without promoting this conditional theorem.

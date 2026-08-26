# Hypergraph reference faults are systematic-code distance

## Bounded question

What replaces augmented minimum cut when one comparison record may test the
parity of more than two command replicas?

## Frozen algebraic model

Let \(V_0=V\setminus A\) be the unanchored command coordinates and let

\[
H:\mathbf F_2^{V_0}\longrightarrow\mathbf F_2^M
\]

be the source-labelled comparison matrix. Row \(j\) records the parity of its
incident unanchored commands; anchored command values are frozen to zero in the
error calculation. A command fault \(x\) and comparison-record fault \(e\)
produce residual

\[
r=Hx+e.
\]

An invisible nonzero joint fault therefore has \(e=Hx\). With unit costs its
minimum weight is

\[
d(H)=\min_{x\ne0}\bigl(\operatorname{wt}(x)+\operatorname{wt}(Hx)\bigr).
\]

Equivalently, \(d(H)\) is the minimum distance of the systematic binary code
with encoder

\[
G_H:x\longmapsto(x,Hx).
\]

Positive coordinate costs give the corresponding weighted systematic-code
distance.

## Detection and correction theorem

The syndrome map on joint faults is \(R(x,e)=Hx+e\). Two fault patterns have
the same residual exactly when their difference lies in

\[
\ker R=\{(x,Hx):x\in\mathbf F_2^{V_0}\}.
\]

Consequently all joint faults of weight below \(d(H)\) are detected, and all
joint faults of weight at most \(t\) are uniquely correctable exactly when

\[
d(H)\ge 2t+1.
\]

This is the same kernel-distance mechanism as the graph controller, but the
distance is no longer generally a graph cut.

## Exact boundary of the min-cut compiler

For an ordinary comparison edge \(\{u,v\}\), the row output is one exactly
when the edge crosses the command-flip set. Thus graph incidence turns
\(\operatorname{wt}(Hx)\) into cut size and recovers the augmented-mincut
theorem.

For higher-arity parity rows, the set function

\[
S\longmapsto\operatorname{wt}(H1_S)
\]

need not be submodular. A single ternary row on \(\{1,2,3\}\) gives, for
\(S=\{1,2\}\) and \(T=\{2,3\}\),

\[
f(S)+f(T)=0<2=f(S\cap T)+f(S\cup T).
\]

Every nonnegative graph cut function is submodular. Therefore no ordinary
nonnegative-capacity augmented graph can represent this parity objective on
all subsets. This is a structural obstruction, not a failed search for the
right graph.

## Degree-like data are not faithful

Use three free vertices and the three distinct typed checks

\[
\{1,2\},\qquad \{1,2,3\},\qquad \{3,a\},
\]

where \(a\) is anchored. After restricting to free coordinates,

\[
H=
\begin{pmatrix}
1&1&0\\
1&1&1\\
0&0&1
\end{pmatrix}.
\]

Every column has weight two, so the singleton estimate is three. Yet
\(x=(1,1,0)\) has \(Hx=0\), hence \(d(H)=2\). The checks are distinct at the
source level; the cancellation is not produced by duplicated rows.

## Carrier geometry versus coefficient lens

The labelled incidence relation between commands and comparison ports is
Carrier geometry. Turning incidence into parity uses the classical
\(\mathbf F_2\) coefficient lens. The systematic encoder, kernel distance,
and Hamming decoder are classical coding structure. None of these alone gives
Pauli commutation or a quantum stabilizer code. That further step requires a
symplectic coefficient lens and the independently derived commutation maps.

## Exact audit

The checker exhausts every binary comparison matrix with up to three command
coordinates and three output rows. It verifies the kernel description, the
systematic rank, minimum distance, and the one-fault correction criterion by
direct collision enumeration. It separately requires both hostile witnesses:
the typed three-check degree failure and the ternary-row submodularity failure.

## Claim boundary

This is a finite classical algebraic theorem. It does not provide an efficient
decoder for arbitrary matrices, a stochastic threshold, a quantum stabilizer
Hamiltonian, a physical comparison port, correlated-noise correction, or an
ordinary graph-cut representation for higher-arity parity checks.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
9/10. The frozen alternatives were survival of augmented cuts and transition
to systematic-code distance. The discriminants were exact submodularity and
correction tests; the main confound was accidental use of duplicate checks.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Ordinary cuts were eliminated for general ternary parity by a strict
submodularity residual. The systematic-code branch produced the exact kernel,
distance, and correction theorem. The typed hostile matrix uses distinct
checks. Efficient decoding and quantum symplectic lifting remain open.

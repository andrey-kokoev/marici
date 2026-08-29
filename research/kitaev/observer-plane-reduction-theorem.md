# Observer-plane reduction theorem

## Question

When an observation plane in the SCC lattice selects a source-authorized family of constructors and observations, what mathematical object represents the operational reality visible from that plane, and what quantitative vector measures its viewing strength?

## Claim boundary

The theorem below is finite-dimensional and linear after a source carrier, inner product, constructor closure, output calibration, and common authority frame have been frozen. It identifies behavioral indistinguishability with the radical of an observability Gramian and proves monotonic refinement under compatible probe addition.

It does not make the 405 SCC profiles into operational domains. It does not identify domains from eigenvalues alone. It does not equate an effect map with a physical instrument, certify apparatus access, or establish a cutoff-independent completion bound. Integral, finite-labelled, and noncommutative coefficient realizations require their typed Smith, partition, or blockwise replacements.

## Disposition

### Frozen packet

Let (X) be a finite-dimensional real or complex inner-product space. An observation plane (P) supplies:

- a source-authorized constructor family \(\mathcal A_P\subseteq\operatorname{End}(X)\), closed under admitted finite composition;
- a calibrated observation family \(\mathcal O_P\), with each \(O:X\to Y_O\) linear;
- fixed inner products on (X) and every output space;
- a declared common frame for every joint comparison.

The constructor-closed behavioral map is

\[
B_Px=(O\alpha x)_{(O,\alpha)\in\mathcal O_P\times\mathcal A_P}.
\]

Its observability Gramian and viewing-strength vector are

\[
W_P=B_P^*B_P,
\qquad
\mathbf v(P)=\operatorname{spec}_{\downarrow}(W_P).
\]

### Observer-plane reduction theorem

For the frozen packet:

1. (W_P) is positive semidefinite.
2. Behavioral indistinguishability is exactly its kernel:
   \[
   B_Px=0\iff x\in\ker W_P.
   \]
3. The semidefinite form
   \[
   g_P(u,v)=\langle u,W_Pv\rangle
   \]
   has radical \(\ker W_P\) and descends to a positive-definite form on
   \[
   X_P=X/\ker W_P.
   \]
4. If (Q) adds compatible calibrated observations in the same source frame, then
   \[
   W_Q-W_P\succeq0,
   \qquad
   \ker W_Q\subseteq\ker W_P.
   \]
5. For compatible packets transported into a common frame by (T_i),
   \[
   W_{\mathrm{joint}}=\sum_iT_i^*W_iT_i,
   \qquad
   \ker W_{\mathrm{joint}}=\bigcap_i\ker(T_i^*W_iT_i).
   \]
6. Faithfulness is \(\ker W_P=0\), equivalently \(\lambda_{\min}(W_P)>0\).
7. A cutoff family is completion-stable only when its frozen normalization admits a uniform lower bound
   \[
   \inf_N\lambda_{\min}(W_{P,N})>0.
   \]

The proof is immediate from

\[
\langle x,W_Px\rangle=\|B_Px\|^2
\]

and from adding positive semidefinite transported summands. The content is primarily typing: constructor closure, calibration, source module, and common-frame authority must be fixed before the equations are meaningful.

### Operational-domain object

The reduced carrier alone is not a complete domain identity. The operational object is

\[
\mathsf{Reality}(P)=
\bigl(X_P,\bar g_P,\bar{\mathcal A}_P,\bar{\mathcal O}_P\bigr),
\]

provided the admitted constructors descend to (X_P). Two planes define the same operational domain only through a verified equivalence intertwining the reduced carrier, constructor action, observations, metric or typed replacement, and completion topology.

Equal spectra do not imply such an equivalence. Isospectral Gramians may have differently placed eigenspaces, inequivalent constructor actions, or different loop holonomy.

### Toric rank ladder

On the marked two-dimensional primal logical quotient of the finite toric code, normalize the two logical coordinates orthonormally. Local syndrome is zero on this quotient:

\[
W_{\mathrm{syndrome}}=
\begin{pmatrix}0&0\\0&0\end{pmatrix}.
\]

Adding one marked noncontractible loop probe gives

\[
W_{\mathrm{one\ loop}}=
\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

Adding an independent second loop probe gives

\[
W_{\mathrm{two\ loops}}=
\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]

Thus the visible logical quotient grows through ranks (0,1,2). The marked frame and normalization are part of the packet; the unmarked torus does not canonically order these coordinates.

### Coefficient-aware replacements

- Hilbert-linear packets use the ordered Gramian spectrum.
- Integral-linear packets retain rank and Smith invariant factors; arbitrary real rescaling is not admitted.
- Finite-labelled packets use the observer partition or ordered fiber-size profile.
- Noncommutative packets use blockwise Gramians together with commutant and inter-block coherence data.

These are coefficient-lens realizations of one Carrier pattern: an observation family defines an indistinguishability congruence, and the reduced object retains the action that descends through it.

### Instrument boundary

The Gramian records present output distinguishability. A physical instrument additionally contains conditional future-state maps. Two instruments may have the same (W_P) and different backaction. Predictive operational equivalence must therefore compare both the record map and the conditional transition family.

### Falsifiers

The proposed use of the theorem fails when any of the following occurs:

1. An alleged invisible vector has \(B_Px\ne0\).
2. A declared joint Gramian adds terms without an authorized common-frame transport.
3. Numerical eigenvalues are compared after unrecorded detector or source rescaling.
4. A constructor does not preserve \(\ker W_P\), so it does not descend to the proposed operational quotient.
5. Two packets are called equivalent only because their spectra agree.
6. Present effects agree while conditional future-state maps differ.
7. Every finite Gramian is positive but its smallest eigenvalue tends to zero.
8. A non-Hilbert coefficient packet is forced into an eigenvalue spectrum that erases its integral, labelled, or block structure.

### Immediate programme use

The 405-cell SCC classifier supplies the coarse base profile. The observer atlas supplies (W_P) or its typed replacement over occupied profiles. The 28-cell reconciler lattice supplies transports and higher common-frame checks. Operational domains are then derived from verified equivalences of the reduced action-observation objects, while rank loss, undefined joins, holonomy, and uniform-margin collapse label distinct domain walls.

Companion model: `public/experiments/typed-reconciler-cube/observer-atlas.toml`.

Primary finite evidence: `research/kitaev/toric-code-selection-readout-decoding.md`, `research/kitaev/milestone-s3-central-readout-algebra.md`, and `research/kitaev/milestone-s3-endpoint-control-span.md`.

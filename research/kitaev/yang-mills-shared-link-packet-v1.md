# Iteration 2 — shared-link recoupling and the spectral packet dictionary

## Question, conjecture and disposition

Do two source plaquettes compose as independent gapped atoms, or does the shared gauge link change the excitation data that the packet must retain?

The independent-atom conjecture fails. The product of two fundamental loop characters splits into shared-link spin-zero and spin-one channels with different electric energies. Its mean energy is the naive sum, but it is not an eigenstate. Retaining that mean alone loses subsequent Hamiltonian action.

Constructed: `spectral-packet-dictionary` on the explicit seven-link SU(2) source, with gauge-compatible evaluation, core operations and a covariant derivative detector. The written electric gap theorem and the exact differential controls support this scope. The full `finite-gauge-source` gate remains open: no coupled four-dimensional Wilson family or its Euclidean reflection-positive transfer construction is claimed.

Contract: [shared-link packet](contracts/yang-mills-shared-link-packet.v1.json). All source choices are independent of a desired mass or counting constant.

## Actual source and physical packet map

The vertices are 0,...,5 and edges are

    U0:0->1, U1:1->2, U2:2->3, U3:3->0,
    U4:1->4, U5:4->5, U6:5->0.

The two plaquettes share U0. Put A=U1 U2 U3, B=U4 U5 U6 and Wp=U0 A, Wq=U0 B. Both loop orientations are explicitly chosen to use the shared edge in the same direction; reversing the second loop does not change its SU(2) fundamental character.

Use normalized product Haar measure and the actual vertex gauge action Ue mapping to g_source Ue g_target inverse. The physical Hilbert space is the gauge-invariant closed subspace of L2(SU(2)^7). A spanning-tree gauge leaves two loop holonomies under simultaneous conjugation. This space is not the tensor product of two separate conjugacy-class spaces: simultaneous relative loop orientation also matters.

A source packet retains the edge order, representation labels and actual index contractions of a finite gauge-invariant matrix-coefficient polynomial. Evaluation sends it to its smooth invariant function. Exact zero evaluations are quotiented; Hilbert completion uses Haar norm. The gauge-averaged Peter–Weyl polynomial core is dense by compact-group harmonic analysis and bounded gauge averaging. No finite spin cutoff is assumed in this density statement.

The actual primitive operations are quaternion/matrix multiplication, contraction, gauge action, invariant link differentiation, multiplication by the plaquette potential and rational/complex linear combination. Their evaluation squares commute by those operations' definitions. A different retained derivation with the same smooth evaluation has identical derivatives and multiplication results. Witness details not consumed by this declared interface are therefore quotiented, not arbitrarily assigned energy.

## Electric generator and covariant detector

Supply H0=kappa times the sum of seven positive link Casimirs. On the core, the associated derivative packet D obeys q0(psi)=kappa times the squared L2 norm of D psi. Its target carries an edge and Lie-algebra index. Under a vertex gauge change these indices rotate by the appropriate adjoint orthogonal action, so the norm is invariant. Individual derivative components are not scalar gauge-invariant observables; the packet is covariant, not a falsely scalar quotient map.

Spin networks diagonalize H0, with eigenvalue kappa times the sum of j_e(j_e+1). A nontrivial-representation support of a gauge-invariant spin network cannot have a degree-one vertex: one nontrivial irreducible representation has no invariant vector. Thus a nonempty support has a cycle. This graph has girth four, so it uses at least four nontrivial edges, each with Casimir at least 3/4. Therefore

\[
q_0(\psi)\ge3\kappa\|(I-P_0)\psi\|^2.
\]

The character on either single plaquette attains equality. The constant is the unique electric vacuum; finite spin-network sums are a form core. This proves the all-spin electric gap 3 kappa on this graph, not merely on the sampled functions. Standard spin-network completeness, compact-group Laplacians and closure are imported mathematics, not new proof-assistant results.

The self-adjoint closure of H0 exists by its complete nonnegative spin-network spectral description. The bounded real magnetic multiplication below preserves its operator/form domains. Its semigroup is a well-defined continuation on the physical Hilbert space. This is a mathematical Hamiltonian-source interface; it is not yet physical spacetime reconstruction or a four-dimensional reflection-positive lattice-action family.

## The shared-link hostile: correct mean, wrong continuation

Let

\[
F=\operatorname{Tr}(U_0A)\operatorname{Tr}(U_0B),\qquad
F_0=\tfrac12\operatorname{Tr}(AB^{-1}),\qquad F_1=F-F_0.
\]

Haar averaging the shared link gives F0. Its shared representation is spin zero; the orthogonal remainder has spin one, since one half tensor one half equals zero plus one. All six outer edges retain spin one half. Thus

\[
H_0F_0=\tfrac92\kappa F_0,\qquad
H_0F_1=\tfrac{13}2\kappa F_1.
\]

With normalized product Haar,

\[
\|F\|^2=1,\qquad \|F_0\|^2=\tfrac14,
\qquad\|F_1\|^2=\tfrac34,\qquad \langle F_0,F_1\rangle=0.
\]

The identities follow from normalized fundamental-character orthogonality and the shared-link Haar projection. The checker independently regresses the quadratic Haar moments with the eight signed coordinate quaternions, whose second moments are exactly those of the unit three-sphere. The polynomial degree in each integrated outer holonomy is at most two; no general Haar cubature claim is made.

Consequently the mean energy is 6 kappa, exactly the sum of two separate 3 kappa loop energies, but

\[
\|(H_0-6\kappa)F\|^2=\tfrac34\kappa^2\ne0.
\]

This is a source-derived equal-mean/different-continuation hostile. Merely adding the two atom energies would miss the two shared-link channels. At U0 equal to a pure imaginary unit quaternion and all other links identity, F evaluates to zero whereas H0F evaluates to minus 2 kappa, giving an exact pointwise rejection of the proposed eigen-equation.

The checker computes the seven-link differential operator directly, not from the claimed channel energies: for each edge and each quaternion unit, vary the link by exp(t e_i/2), keep its exact second Taylor jet, evaluate the actual traces, and take minus the second derivative. Here t is a group-deformation coordinate, not physical time. Eight fixtures verify the channel equations; six independent vertex-gauge transformations per fixture preserve all evaluated functions.

## Magnetic extension and the detector's vacuum mismatch

For nonnegative lambda add lambda times Vp+Vq, with Vp=1-Tr(Wp)/2 and likewise for q. Each potential lies in [0,2]. The operator is a bounded nonnegative perturbation. Compact resolvent and min–max give

\[
E_1\ge3\kappa,\qquad E_0\le2\lambda,
\qquad E_1-E_0\ge3\kappa-2\lambda.
\]

This sufficient estimate is weaker than the single-plaquette one; its extensivity is a limitation of this argument, not evidence that the true gap decreases with graph size.

The constant electric state is again not a magnetic vacuum:

\[
H_\lambda1=2\lambda-\tfrac\lambda2
\bigl(\operatorname{Tr}W_p+\operatorname{Tr}W_q\bigr).
\]

The two characters are orthogonal normalized functions, so the orthogonal residual has squared norm lambda squared over two.

A sharper typing consequence follows. The raw electric derivative D kills only constants on the connected configuration space. A magnetic ground state at positive lambda is nonconstant, so D Omega_lambda is nonzero. A proposed inequality

\[
q_{H_\lambda-E_0}(\psi)\ge\epsilon\|D\psi\|^2,
\qquad\epsilon>0,
\]

fails already at psi=Omega_lambda. Hence the dictionary supplies a legitimate covariant detector and energy-form interpretation, but not the magnetic-vacuum-faithful detector required by the later gap route. This blocks a concrete proposed map, not every possible detector.

## Strongest test, survivor and next operation

Rivals: independent plaquette tensor factors; a mean-energy-only packet; an unchanged electric vacuum; raw derivatives used unchanged after vacuum subtraction.

The strongest explicit residual is the all-function eigenstate failure with norm squared 3 kappa squared over four. The vacuum residual and the ground-state detector mismatch locate a second failure independently of recoupling.

The surviving source structure is a gauge-invariant polynomial packet with the shared intertwiner channel retained, actual Casimir continuation and a covariant derivative norm. This is the bounded dictionary construction admitted by the net. It is not a higher-categorical universal identity theorem, a selected atomic particle, or a continuum gap.

Next executable test: construct the magnetic-ground-state-relative gradient and derive its weighted Poincare problem. Determine whether its constants can be bounded in terms of source parameters and graph size. The finite four-dimensional Wilson/transfer-family task remains separate; no spin-cutoff repetition can supply it.

## Reproduction

```text
python research/kitaev/checkers/check_yang_mills_shared_link_packet.py
```

Receipt: `research/kitaev/results/yang-mills-shared-link-packet-v1.json`. Verification combines exact rational quaternion/second-jet/degree-two moment controls with the written all-spin harmonic-analysis proof. Earlier owner sources and receipts are unchanged; no proof-assistant closure, external physical evidence or continuum claim is included.

# Base-preserving transport of the small-probe eigenstate

## Question and source

Can the normalized eigenstate and its local readouts be transported between the actual finite and thermodynamic vacuum measures, rather than inferred from convergent spectral scalars?

SCC obligation: attachment transport and state-based readout comparison, using positive spectral filtering as the completion. Retain the actual spaces H=L2(nu), H_Lambda=L2(nu_Lambda), generators A,A_Lambda, normalized constant vacua and full gap m=kappa*c. Here kappa>0, 0<=R<9/64, c=1/2-3R and a=4/3. The mesh-word coefficient is C_R=max(2R/c,44 eta_R/7)<=18/5, with eta_R=R/2+(8R/9)/(1-8R/9). Parameters are Euclidean source semigroup parameters, not calibrated physical time.

Let real smooth gauge-invariant U have finite support K_U and ||U||_infinity<=delta<=m/8. The previous spectral packet constructs B_U=A+M_U, its rank-one projection Pi_U, lowest eigenvalue E(U), original-state overlap alpha_U>=8/9 and relative gap g_U>=m-2delta>=3m/4. Use these objects separately in every original Hilbert space. Multiplication by a local observable is retained as an operator before forming its pairing. Finite measures on X use their prescribed source Haar-exterior extension; finite spectral vectors depend only on their source links. This extension does not posit an infinite Haar vacuum density.

## Issue-boundary DPC

- **Problem:** neither scalar pressure convergence nor common pointwise filter coordinates identify normalized vectors or state-dependent local readouts.
- **Conjecture:** orthogonal spectral filtering is uniformly stable because the original preparation has a nonzero overlap. Compare fixed-parameter positive sandwich packets in their actual bases before completing the filter.
- **Named rivals:** copy Hilbert coordinates across measures; omit the squared-norm denominator; divide two independently uncontrolled small readouts; infer a pointwise or common-Hilbert eigenvector limit from local scalar convergence.
- **Risky consequences:** a positive normalized eigenvector in each original H, an exponentially controlled filter, a one-inverse-denominator spatial bound, and weak convergence of the auxiliary tilted probability states.
- **Strongest falsifiers:** identical constant filters in two gap1 reset sources give local readout discrepancy1/6 in their different original measures. Dropping the norm denominator in a norm-small two-state projection loses constant readout1 by1/257.
- **Disposition:** the written filter/sandwich argument constructs the eigenstate readout transport below. No cross-source isometry, pointwise eigenfunction transport, tilted dynamics, original magnetic-vacuum replacement or continuum/root closure follows.

## Positive vector completion within each fixed original space

Set q_T=exp(-T B_U)1 and h_T=q_T/||q_T||_H. The signed probe is positive-preserving after shifting V=U+delta>=0; in particular q_T>=exp(-delta T)>0 as an actual C(X) function at finite T. Decompose

\[
e^{TE(U)}q_T=\sqrt{\alpha_U}\,\psi_U+\eta_T,
\quad \psi_U=\Pi_U1/\sqrt{\alpha_U},
\quad \eta_T\perp\psi_U,
\quad \|\eta_T\|\le\sqrt{1-\alpha_U}\,e^{-g_UT}.
\]

This fixes the eigenvector phase by the original preparation. With r_T=||eta_T||/sqrt(alpha_U),

\[
r_T^2\le\tfrac18e^{-2g_UT},\qquad
\|h_T-\psi_U\|^2
=2\left(1-\frac1{\sqrt{1+r_T^2}}\right)\le r_T^2.
\]

Thus h_T converges in its OWN H norm, uniformly in source size; the closed positive cone implies psi_U>=0. It has norm1 and is gauge invariant because the original semigroup, probe and constant preparation are equivariant. This does not assert a common full-measure pointwise representative across different spaces.

Define the auxiliary normal probability measure dnu_U=psi_U^2 dnu, and analogously dnu_(Lambda,U)=psi_(Lambda,U)^2 dnu_Lambda. For any bounded real f with norm<=F, the state-effect pairing obeys

\[
|\nu_U(f)-\nu(h_T^2 f)|
\le2F\|h_T-\psi_U\|
\le F e^{-3mT/4}.
\]

Normalization here constructs the auxiliary eigenstate; it does not replace the original nu or normalize the original generating function Z_U to1. A constant shift of U changes E and Z but leaves these normalized filters and eigenstates unchanged.

## Based sandwich sewing before spatial comparison

For fixed T use V=U+delta and its positive contraction Q_V(T). The common factor exp(delta T) cancels from the normalized filter. In EACH original space, symmetry gives

\[
\nu(h_T^2 f)=\frac{N_T(f)}{D_T},\qquad
N_T(f)=\langle1,Q_V(T)M_fQ_V(T)1\rangle,
\quad D_T=Z_V(2T).
\]

The full packet retains the two probe segments, the middle multiplication, the original state, numerator and norm denominator. It has D_T>=exp(-4delta T) and |N_T(f)|<=F D_T. The latter inequality is essential: treating numerator and denominator as unrelated scalars wastes a second inverse denominator.

Let f be a real smooth gauge-invariant cylinder with support K_f, and put K=K_U union K_f, b=d(K,Lambda complement). Apply the mesh-word comparison to positive probe factors on both sides of f/F, then pass the already constructed strong product limit. The total gradient budget is2T M(U)+M(f)/F. Consequently

\[
|N_{\Lambda,T}(f)-N_T(f)|
\le C_R[2T M(U)F+M(f)]a^{-b},
\quad
|D_{\Lambda,T}-D_T|\le2C_RT M(U)a^{-b}.
\]

For F=0 the observable is zero and division by F is unnecessary. For F>0 the exact quotient estimate, using the actual positivity relation, is

\[
\left|\frac{N_{\Lambda,T}}{D_{\Lambda,T}}-\frac{N_T}{D_T}\right|
\le\frac{|N_{\Lambda,T}-N_T|+F|D_{\Lambda,T}-D_T|}{D_{\Lambda,T}}
\le C_Re^{4\delta T}[M(f)+4T M(U)F]a^{-b}.
\]

No finite vacuum is treated as a marginal or as an isometric coordinate copy of nu. Combining the two same-space filtering errors proves

\[
|\nu_{\Lambda,U}(f)-\nu_U(f)|
\le2F e^{-3mT/4}
+C_Re^{4\delta T}[M(f)+4T M(U)F]a^{-b}.
\]

Fix T, send the spatial buffer to infinity, then send T to infinity. This proves local readout convergence without interchanging an uncontrolled pair of limits.

Gauge invariance extends this conclusion to arbitrary smooth real cylinders: average f over the compact product of gauge groups at endpoints of its finitely many links. This leaves all state pairings unchanged, does not enlarge its link support, and does not increase sup norm or M(f), since left/right link actions are isometries. Smooth cylinders are uniformly dense in C(X). Probability normalization then extends the convergence to all continuous functions on the compact product X: nu_(Lambda,U) converges weakly to nu_U. This is not total-variation convergence or H-norm convergence between different bases.

## Rational joint budget and exact special cases

Take T=n/m, b>=4n and integer n>=1. Since exp(-3/4)<=4/7 and exp(1/2)<=2, the working norm ball gives the rational envelope

\[
|\nu_{\Lambda,U}(f)-\nu_U(f)|
\le2F(4/7)^n
+C_R\left[M(f)+\frac{4n}{m}M(U)F\right](81/128)^n.
\]

Both terms tend to0; the second has an explicitly retained linear n prefactor. The first n meeting a tolerance gives a sufficient diagonal buffer, not an optimal physical-volume claim. A whole-window planner uses m_lower=5kappa/64 and requires delta<=m_lower/8; the actual m is at least this lower bound. With kappa=1, delta=1/128, F=M(f)=M(U)=1 and tolerance1/1000, buffers140 over the whole window and112 at R=9/128 suffice under this rule.

At R=0 the fixed-T cross-source error is exactly0, hence the tilted local readouts agree once both supports are inside Lambda. A constant f is exact for every probability state. If U is constant (in particular U=0), psi_U=1 and the comparison reduces to the original-state budget C_R M(f)a^(-b), with no filtering cost. The derivative-zero criterion uses connectedness of the finite product SU2 support, not an assertion about arbitrary disconnected carriers.

## Finite controls and the next constructor

The checker replays the full pressure receipt and preregisters15 orthogonal-filter geometry packets,180 exact reversible two-state filtered readouts,81 positive-denominator quotient packets,192 rational transport budgets and the two falsifiers. These are finite analogues, not SU2 eigenfunctions or proof of the imported analytic estimates. Independent analytic review remains open.

The next executable issue is the source ground-state transform. Prove psi_U>0 almost everywhere, construct the canonical multiplication unitary from L2(nu_U) to its original L2(nu), and realize exp(sE)psi_U^(-1)Q_U(s)(psi_U f) as a conservative positive symmetric semigroup. Transport its local paired readouts through the based filters and preserve its relative spectral gap. This is not yet a Feller or smooth-drift assertion: psi_U is currently an L2 vector. The required positivity and operator arguments are executable from the bounded potential, original gap and current packet, without a new external authority.

Contract: `research/kitaev/contracts/yang-mills-probe-eigenstate.v1.json`.
Checker: `research/kitaev/checkers/check_yang_mills_probe_eigenstate.py`.
Receipt: `research/kitaev/results/yang-mills-probe-eigenstate-v1.json`.

# Iteration 4 — physical quotient descent without erasing mixed-loop states

## Question and disposition

Does the actual-vacuum detector descend to physical states without counting gauge directions, discarding relative loop orientation, or replacing the physical integration measure?

**Constructed:** `quotient-descent` for the finite SU(2) Hamiltonian/temporal heat-kernel family of iteration 3. The detector has a closed covariant horizontal target, an exact descended energy form and a correctly weighted quotient Hilbert norm. It is not a collection of scalar gauge-invariant derivative components. No free gauge action or smooth global gauge slice is assumed.

**Rejected:** reading only the individual elementary loop characters. An explicit nonzero physical state is invisible to that reader even on the seven-link graph. This is stronger than saying that different word histories might matter: it is a computed loss of physical Hilbert data.

[Contract](contracts/yang-mills-quotient-descent.v1.json). Source group, Hamiltonian, ground state and energy units are unchanged from iteration 3. That iteration's lack of volume-uniform constants remains unchanged.

## Quotient space, measure and nulls

Let M=SU(2)^E, K=SU(2)^vertices and pi:M->X=M/K. Compact-group averaging identifies the physical Hilbert space exactly with L2(X,mu_X), where mu_X=pi_*mu and mu is normalized product Haar. Pullback pi^* is unitary onto invariant functions. The orbit space includes stabilizer strata; it is not assumed to be a manifold or a free principal-bundle quotient.

The actual unique positive ground function Omega from iteration 3 is invariant, so it descends to omega on X. Put nu_X=omega squared mu_X. Multiplication by omega is the unitary from the weighted quotient space to the physical quotient space. Its constant vector goes to the actual magnetic vacuum.

A finite source packet is still evaluated as its smooth invariant matrix-coefficient polynomial. A packet-null evaluation vanishes everywhere: a continuous function zero Haar almost everywhere is zero because Haar has full support. Its differentiated evaluation therefore also vanishes. Exact alternative polynomial/contraction receipts with the same evaluation give the same detector. Gauge transforms give the same physical state, not a new excitation.

Passing to completion requires care. L2-Cauchy packets alone need not have Cauchy derivatives. Complete the packet core in the physical form norm and then use the closed operator below. No derivative bound or energy continuity is inferred from bare Hilbert convergence.

## The target is covariant and horizontal

Use left generators X_ea defined by U_e(t)=exp(t e_a/2)U_e, with e_a the three imaginary quaternion units. For a physical form vector define

\[
z_{ea}=D_\Omega\psi:=\Omega X_{ea}(\psi/\Omega).
\]

Writing z_e as a Lie-algebra vector, gauge invariance implies the exact equivariance law

\[
z_e(g\cdot U)=\operatorname{Ad}(g_{s(e)})z_e(U).
\]

It follows by moving exp(t e_a/2) past the source gauge matrix; the inverse adjoint on the generator becomes the adjoint on the gradient vector. The scalar norm is invariant, but the components generally change.

An infinitesimal gauge change at vertex v yields the pointwise vertical constraint

\[
\sum_{s(e)=v}z_e-
\sum_{t(e)=v}\operatorname{Ad}(U_e^{-1})z_e=0.
\]

The incoming sign and transport are necessary: right multiplication by exp(-t xi) becomes left multiplication by exp(-t Ad(U_e)xi). Thus the field annihilates every gauge-orbit tangent; it does not charge energy to a vertical gauge change.

Use as target the closed subspace of L2(M;Lie(SU2)^E) satisfying these equivariance and vertical constraints almost everywhere. Equivariance is the fixed space of a unitary compact-group representation; the vertical map is bounded pointwise and hence bounded on L2, so its kernel is closed. Norms descend by integration against mu_X. At nonfree strata, equivariance also requires invariance under the stabilizer; one need not invent constant-rank quotient fibers. Calling this a measurable covariant field space avoids an unjustified global vector-bundle claim.

Since Omega is smooth with a positive minimum on each fixed compact M, multiplication/division by Omega preserves H1. The inherited detector is closed, with physical H1 domain, and iteration 3's identity becomes

\[
q_{H-E_0}(\psi)=\kappa\|D_\Omega\psi\|^2
\]

on the entire quotient form domain. Its kernel is exactly the vacuum span: a function with zero gradient on connected M is constant after division by Omega. The smooth invariant polynomial core remains a form core after averaging. Compact-group elliptic theory and Sobolev closure are imported analytic inputs; these statements are not proof-assistant results.

Gauge symmetry also intertwines the physical semigroup and symmetric transfer steps with pi^*. This is the actual continuation compatibility: evaluation, source differential/multiplication operations and physical transfer agree on their specified domains. It is not a theorem transporting this norm between different spatial volumes.

## A nonzero mixed-loop sector hidden by elementary traces

In spanning-tree gauge the seven-link graph has two loop holonomies x=U0 A and y=U0 B under simultaneous conjugation. Choose

    (x,y)=(i,i) or (i,j).

Both have Tr x=Tr y=0. But Tr(xy) is -2 in the first case and 0 in the second. Simultaneous conjugation cannot change the relative axes' dot product. These are different physical quotient points with identical separate loop characters. Keeping every character of each loop separately does not fix the problem: SU(2) characters of one loop are polynomials in its fundamental trace.

Consider the actual invariant polynomial

\[
h(x,y)=\operatorname{Tr}(xy)-\tfrac12\operatorname{Tr}x\operatorname{Tr}y.
\]

Writing x=x0+x_vec and y=y0+y_vec gives h=-2 x_vec dot y_vec. Under product Haar the loop holonomies x,y are independent: conditional on the shared link, each three-link return path is independent Haar, and multiplying by that link preserves Haar. Conditional on x0,y0, their axes are independently uniform. Hence

\[
\mathbb E[h\mid\operatorname{Tr}x,\operatorname{Tr}y]=0,
\qquad \|h\|^2=4\sum_{a,b}
\mathbb E[x_ax_b]\mathbb E[y_ay_b]=\tfrac34.
\]

Thus h is orthogonal to the entire closed subspace of functions of individual loop traces, not just to a finite observable list. A normalized hidden physical state exists. This reader is not faithful on the quotient.

The trace identity gives h=F/2-2F0=F1/2-3F0/2 in iteration 2 notation. Therefore

\[
q_0(h)/\kappa=\tfrac{15}4,
\qquad q_0(h)/\|h\|^2=5\kappa.
\]

The exact covariant derivative detects it. This is a finite-source blindness counterexample, not a normalized low-energy family or evidence that the Yang–Mills gap closes. At positive magnetic coupling the norm/conditional-expectation statement here still concerns the Haar physical reader; no claim that the unknown ground-weighted conditional distribution stays product Haar is made.

## A second hostile: a flat gauge-fixed angle changes the vacuum projection

For one conjugacy angle theta in [0,pi], normalized SU(2) Haar pushes to (2/pi)sin(theta)^2 dtheta. It does not push to dtheta/pi. The fundamental character has squared norm 1 under Haar and 2 under the flat angle. For chi2=4cos(theta)^2-1 the means are respectively 0 and 1. Thus flat-angle substitution alters both excitation norms and the vacuum projection.

The class radial positive link Laplacian is

\[
-\tfrac14(\partial_\theta^2+2\cot\theta\,\partial_\theta),
\]

not the flat interval Laplacian. Four links on a single loop give the electric operator normalization used in iteration 1. The coupled graph has further shared-link structure; independent radial operators on separate traces do not recover its quotient operator. A gauge slice without its induced measure and differential form is not a valid source-to-physical map.

## Exact verification and what it does not prove

The checker differentiates actual quaternion trace packets at first order on all seven links. For a strictly positive invariant test function Omega_test=2+(Tr Wp+Tr Wq)/4, in [1,3], it checks the repaired quotient formula, adjoint covariance, invariant squared norm and all vertex vertical constraints under rational gauge transformations. **Omega_test is not claimed to be the magnetic ground state.** The test verifies the algebraic transformation law valid for any positive invariant weight; the actual-ground-state identity is the written analytic theorem inherited from iteration 3.

It also verifies the hidden state's Haar moments with exact degree-two quaternion cubature, the written recoupling energy via the direct second-jet Casimir checker, and the Haar-versus-flat angle moments. Gauge-transformed components are demonstrably unequal before adjoint transport, rejecting the scalar-target shortcut. These are exact finite controls, distinct from the all-domain quotient proof.

## Survivor, next operation and boundary

The surviving packet retains mixed-loop contractions, uses the pushforward Haar/ground measure, and maps to horizontal covariant fields. Its closed finite-graph energy identity and vacuum kernel descend correctly. It supplies no new physical degree of freedom from a gauge-null distinction.

The later `faithful-excitation-detection` gate is newly ready but stays open: its route needs one volume-compatible detector constant. The available 3 min(Omega squared)/max(Omega squared) is not that constant. Next investigate a local conditional Poincare/approximate-tensorization criterion and whether the actual ground-state measure satisfies it. Local plaquette potential alone does not justify treating Omega squared as a local Wilson Gibbs density.

`continuum-correlation-construction` remains separately ready and open. No continuum reconstruction, volume-uniform magnetic gap, atomic selection or parent discharge occurs in this turn.

Reproduce: `python research/kitaev/checkers/check_yang_mills_quotient_descent.py`.
Receipt: `research/kitaev/results/yang-mills-quotient-descent-v1.json`.

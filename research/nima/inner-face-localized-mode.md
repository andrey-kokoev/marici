# Inner-face excitation: a hidden contrast exists, but the current cycle does not bind it

## Source and trial preparation

Freshly inspected the exact twelve-triangle implementation and the prior full mean/fluctuation composition law. The existing geometric cycle is

    P_collective P_symmetry P_local = P_collective = u u^dagger/80.

Its twelve local complex eigenvectors v_i are retained in a 36-dimensional direct sum. Each has squared norm 20/3. The two cone cells meeting OAB correspond to the existing AB and BA triangle blocks, (F_ABC,A,B) and (F_ABD,B,A).

Prepare trial amplitudes +1 and -1 in those blocks, keeping their source-derived local eigenvectors and transport maps. This is a test input proposed by the hypothesis, not a claimed spontaneous birth. Also test the in-phase +1,+1 control. No new interaction Hamiltonian is introduced.

## Exact result

The opposite-phase contrast has squared norm 40/3 and passes local eigenmode selection unchanged. In the common transported frame its two amplitudes sum to zero. The symmetry average and full collective cycle therefore map its active readout to zero.

The in-phase control also passes local selection. Its collective output is u/6, with one sixth of its input squared norm, spread across all twelve blocks. It is not localized at OAB.

More generally, every eigenvector with nonzero eigenvalue of this rank-one projector lies in span(u). Because u occupies every triangle block, no nonzero cycle eigenmode can stay confined to the selected two blocks. This is a structural statement about the source cycle, not merely failure of the two trial vectors.

## Birth versus preparation

The established collective background satisfies P(u)=u. Also P(0)=0 and

    P(u+epsilon*d)=u

for the tested contrast d and every scalar epsilon, by linearity and P(d)=0. Exact rational perturbation controls agree. Thus this particular cycle neither creates the contrast from its background nor amplifies a supplied perturbation into a persistent localized active mode.

Zero active readout does not erase the full retained input. The exact decomposition x=Px+(I-P)x stores the contrast in the residual. Calling that retained residual an electron would nevertheless need a return/coupling law, a persistent independently detectable observable, and particle properties. Storage alone does not establish them.

## A concrete response lead, kept separate from the tested cycle

The prior same-slot composition law for residuals with unit reference is

    (b diamond a)_i=a_i+b_i+b_i*a_i.

Specializing its algebra to twelve scalar coefficients with uniform weights, the +1,-1 pair has zero first mean, but its self-composition has mean

    sum_i a_i^2/12=1/6.

Independent-context composition gives zero instead. This illustrates how the retained hidden contrast could be detected by a previously constructed nonlinear response operation without assigning a fitted correction coefficient.

This is NOT already the twelve-triangle cycle. The prior implementation's physical domain involved a different retained slot set; applying its general algebra here is an explicit trial specialization. It requires a source choice of same-slot incidence and an amplitude-to-response interpretation. The number 1/6 scales quadratically with the prepared amplitude and is neither an electron mass nor a universal coupling.

Accordingly, the next meaningful test is to inspect whether an existing operation on these actual retained triangle ports implements that composition or another feedback map. Substituting it after the projector failed would be a model change unless that source binding is supplied.

## Disposition

The proposed support carries a nontrivial hidden contrast. The current geometric cycle does not support an additional localized persistent excitation there: one phase combination is invisible and the other becomes the existing collective mode. This narrows the electron proposal to a retained-record response mechanism rather than establishing a new particle.

## Verification

`python research/nima/checkers/check_inner_face_localized_mode.py` passes with exact arithmetic in Q(i*sqrt(3)). Receipt: `results/inner-face-localized-mode.json`. Checks reconstruct the actual local and symmetry projectors, verify their collective product, test both interface preparations, perturbations, norm decomposition, and the separately labelled scalar composition control. No prior source law, viewer, geometry receipt or formal proof was changed.

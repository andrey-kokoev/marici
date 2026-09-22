# Cubic observer frames are coherent on the common visible source quotient

## Result

The original four-sector, private two-sector, and combined five-sector cubic measurements form a coherent system on their GENUINE source images. Their transitions are explicitly defined, invertible there, and satisfy every composition/cocycle identity. The original and recalibrated ideal observers are the same functional in these frames.

This does not identify arbitrary noisy data across frames. In fact the transition from the old four-sector image to the private image has norm of order exp(800pi A^2). Synthetic private data reconstructed from old noisy data therefore do not provide the noise advantage of measuring the private sector directly.

The theorem concerns one fixed cubic source corner and fixed spectral point. It does not yet establish frame coherence of every extension of the detector to the all-depth saturated observer tower.

## 1. Fixed source, three frames, and their common kernel

Fix the translated six-event packet, A and iy, as in `an-extra-existing-sector-gives-order-optimal-cubic-observer-noise.md`. Let V be its entire two-feature I^3 component. Its actual 270 disjoint-support basis products include v_0 and v_x, with all notation and physical weights unchanged.

Let K be the span of the other 268 products. It is a kernel of these FINITE LINEAR measurement maps, not a new source ideal or a congruence imposed on the attachment. Set

`C=V/K`, with coordinates `(a,b)=[a v_0+b v_x]`.

Write z_11,z_12,z_21,z_22 for the original actual two-feature response tensors, and z_d for the private A_1D_1 response tensor. Each is nonzero; the weak even copies and X_F>0 suffice, irrespective of possible residual zeros.

The three frame embeddings of C are

`E_4(a,b)=(a z_11,(a+b)z_12,a z_21,a z_22)`,

`E_p(a,b)=(a z_11,b z_d)`,

`E_5(a,b)=(E_4(a,b),b z_d)`.

They follow from the actual sector coefficients on ALL 270 source products. All three are injective and their source measurement kernels are exactly K. Let M_f=E_f(C), with its inherited response norm, for f in {4,p,5}.

These are observable states modulo K, not reconstruction of the full source V. No claim that K is stable under arbitrary source actions is needed or made.

## 2. Exact transitions and coherence

Define on genuine images

`T_(g<-f)=E_g E_f^(-1):M_f->M_g`.

The inverse here recovers only the two visible coefficients. At fixed A these are finite-dimensional bounded isomorphisms. They satisfy

`T_(f<-f)=identity`,

`T_(h<-g) T_(g<-f)=T_(h<-f)`.

Thus every route between these frames gives the same state. No ambient invertibility assumption has been used.

Let lambda_f be any of the existing IDEAL observer representatives in its frame. Their source restrictions are the common functional

`G(a,b)=a S_0+b S_x`,

with conjugation if retaining the first-slot convention. Consequently

`lambda_g T_(g<-f)=lambda_f` on M_f.

The original and recalibrated tests on the four-sector carrier are two extensions of the same G E_4^(-1), not different genuine-image frames. Their different ambient norms and different reactions to structured errors are compatible with this exact equality.

## 3. The transition costs are explicit, and large

Put n_ij=||z_ij||, d=||z_d||, B=n_12 and K_0=n_11+n_21+n_22. The inherited norms on C are

`N_4(a,b)=K_0|a|+B|a+b|`,

`N_p(a,b)=n_11|a|+d|b|`,

`N_5(a,b)=N_4(a,b)+d|b|`.

Weighted l1 column norms, using coordinates (a,a+b) for the old frame, give EXACTLY

`||T_(p<-4)||=max((n_11+d)/K_0,d/B)`,

`||T_(4<-p)||=max((K_0+B)/n_11,B/d)`.

The supplied response asymptotics imply K_0~n_11, while

`d/B=||O Psi(D_1)||/||O Psi(B_2)||
     ~3^(-(y+5/2)) exp(800pi A^2)`.

Hence old-to-private conversion has this large norm, whereas the reverse norm tends to one. The projection maps from M_5 to M_4 and M_p are contractions, as expected from their labelled sum norms.

The private observer's optimal norm order is exp(101pi A^2)A^(-2y-5). Paying for conversion from old data restores the old exp(901pi A^2) order. In particular exact frame coherence cannot manufacture the improved measurement precision from an old four-sector data protocol. Access to the additional existing private row remains essential.

## 4. Explicit ambient retractions, not ambient inverses

For clarity, coefficient recovery does not require a nonzero residual mean. Let h=||e_y||_(H_-gamma), and use the admitted norm-one weak-EVEN response test

`kappa_u(w)=sqrt(2(y+gamma)) integral exp(-(y+2gamma)u) w_even(u)du`.

It gives kappa_u(O Psi(F))=sqrt(2)h X_F. Therefore kappa_u tensor kappa_u on a sector F,G gives the known positive number D_FG=2h^2 X_F X_G.

An explicit bounded decoder R_4 on the ambient four-sector space is

`a=(kappa_u tensor kappa_u)(y_11)/D_11`,

`b=(kappa_u tensor kappa_u)(y_12)/D_12-a`.

For R_p use its two private sectors separately, dividing by D_11 and D_d. For R_5 use those same two coordinates inside the five-sector record. In every case R_f E_f=identity_C.

Set P_f=E_f R_f and define ambient transports

`T_hat_(g<-f)=E_g R_f`.

They obey the exact composition identity

`T_hat_(h<-g) T_hat_(g<-f)=T_hat_(h<-f)`.

But T_hat_(f<-f)=P_f, not the ambient identity, and the round trip equals this projection. Components outside the genuine image are discarded by this reconstruction device. It is not a change to the physical response or a declaration that projected noisy data are an actual source measurement.

The ambient extension depends on the chosen decoder. The intrinsic transition in section 2 does not. These explicit decoders also need not be optimal for noise.

## 5. Noise and calibration are transported separately

Suppose two measured frames approximate the same exact visible state c:

`||y_f-E_f(c)||<=epsilon_f`, `||y_g-E_g(c)||<=epsilon_g`.

For the ideal tests, agreement on the exact image gives

`|lambda_f(y_f)-lambda_g(y_g)|
 <=||lambda_f|| epsilon_f+||lambda_g|| epsilon_g`.

There is no equality assertion for arbitrary measured records. For example data supported only in old sector A_2B_2 are seen by the original test but not by its two-sector recalibration. Such an error vector need not belong to M_4.

The explicit reconstructed states satisfy

`||R_f y_f-R_g y_g||_1
 <=||R_f|| epsilon_f+||R_g|| epsilon_g`.

Converting old data synthetically incurs the reconstruction/transition constants; measuring private data directly has its own independent error budget. These are different protocols.

For a rationally calibrated test lambda_hat_f, write its exact-image defect as

`lambda_hat_f E_f=G+delta_f`,

where delta_f is a linear or conjugate-linear functional on C. Then the cross-frame discrepancy bound acquires |delta_f(c)-delta_g(c)|. If |a|<=M_0, |b|<=M_x and the two calibration-coordinate errors are bounded by e_0,e_x, the corresponding defect is at most e_0 M_0+e_x M_x. No uniform relative bound on cancellation-prone combinations follows.

On exact states these defects compose additively:

`(delta_h-delta_g)+(delta_g-delta_f)=delta_h-delta_f`.

This is bookkeeping for fixed calibration errors, not a claim that calibration makes the ideal scalar agreement exact. Voevodsky's Arb-certified private observer supplies concrete enclosures for these two coordinates at A=2.

Shared-template error is another separate model. Its cancellation for the original positive witness does not imply invariant evaluation by all off-image extensions. The frame theorem does not overwrite that advantage of the original observer.

## 6. Port and full-response presentations

The same construction includes the selected prepared-port presentations before rigged response substitution. Their actual tensors are nonzero and have the same two coefficient columns. Thus their genuine images have the same kernel K, and the port-to-response transition is exactly the admitted slotwise O tensor O map restricted to that image. Its inverse is only a finite-visible-state inverse at this fixed frame, not a global strong-port inverse.

The FULL balanced output may retain information about the other 268 source directions. Its genuine image is therefore not silently identified with the two-dimensional visible state. Since the old-sector projection factors through the full output, ker Y_full is contained in K. Consequently

`Y_full(V)/Y_full(K)`

is canonically isomorphic to V/K. This finite linear visible quotient provides a coherent comparison to the selected frames without asserting that the full measurement protocols contain the same information. The actual full output and all its labels remain unchanged.

## 7. Boundary for the all-depth observer tower

This theorem compares observers on the declared CUBIC source subspace. Equality there is stronger than equality on the positive witness but weaker than equality of arbitrary extensions to J_1/J_4.

The all-depth saturated tower uses functionals x->ell_r(a x b) on general filtered source inputs. Cubic-layer equality alone does not prove that two extensions coincide on all those inputs. It guarantees equality for contexts whose products lie in the homogeneous cubic subspace considered here; it does not justify promoting private-sector recalibration to an identical row of the entire saturated tower.

A full tower-frame theorem must track the lower-filtration discrepancies of the extensions and their source-action saturations. Neither a new source ideal nor an unproved observer descent is introduced to bypass that gate.

Likewise no change of spectral chart, arithmetic background or physical normalization is included in the present frame class. The cocycle is established for the concrete source/port/response frames at fixed parameters.

## Disposition and verification

Established: the common visible quotient, exact transitions, composition coherence, explicit finite-dimensional conditioning, coherent ambient retractions, and separate noise/calibration transport for the already constructed cubic frames.

`uv run --with sympy python research/nima/checkers/check_cubic_frame_coherence.py`

The checker verifies the actual source columns, decoder identities, all three-frame composition routes, projection round trips, norm formulas and calibration-defect composition. The infinite-dimensional response norms are supplied by the owning paired comparison; finite coordinate checks do not assert general inverse stability.

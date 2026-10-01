# Iteration 7: local conserved transition current and a necessary profile change

## Main result and scope

The global mode-matched unitary from iteration 6 is not automatically a local electromagnetic source. This iteration supplies a local transition-current construction and audits its one-photon radiation amplitude.

Two conclusions must be kept together:

1. The exact compact momentum top-hat cannot be the nonzero first-order radiation amplitude of a compact-spacetime transition current.
2. Explicit conserved local currents do produce alternative normalizable radiation profiles. They change the earlier engineered profile, and do not inherit its exact pi/2 transfer probability.

## Current constructed from the two-packet vector

For the same seed-plane vector v=a*u+b*w, use the already declared spacetime adapter to define

    d=(sqrt(3)*a,-b,0).

Supply a scalar spacetime envelope f and an antisymmetric polarization tensor

    M^{0i}=d_i f, M^{i0}=-d_i f, M^{ij}=0,
    j^mu=partial_nu M^{nu mu}.

Then

    j^0=-d.grad(f), j^i=d_i partial_t f,
    partial_mu j^mu=0.

Conservation follows identically from commuting derivatives and tensor antisymmetry. It is not imposed by projecting a previously nonconserved emission amplitude. The compensating charge density is essential: a checker control deleting it fails current conservation.

Complex d describes a transition matrix element, not a complex-valued physical charge observable. An operator-valued Hermitian current is obtained as

    j_hat^mu(x)=sigma_- j_ge^mu(x)+sigma_+ conjugate(j_ge^mu(x)).

The source operators here are fixed interaction-picture matrix labels. Their free evolution, gap modulation and actual source dynamics must be included consistently in a later dynamical model. They are not supplied by the algebraic conservation identity.

The local coupling density j_hat^mu(x) A_mu(x) is gauge invariant after integration by parts with vanishing boundary terms. This establishes a conserved local source form, not its apparatus realization or coupling strength.

## Fourier current and Ward check

With ftilde(k)=integral exp(i k.x)f(x) d^4x,

    jtilde^mu(k)=-i*ftilde(k)*J^mu(k),
    J(k)=(k_vec.d, omega*d).

The identity k.J=0 holds OFF SHELL. The checker verifies its complete quadratic basis certificate as well as mixed fixtures. Transforming M as an antisymmetric Lorentz tensor gives the corresponding vector transformation of J; the source envelope must also be transported, rather than re-declared isotropic in every frame.

The first-order outgoing amplitude is proportional to

    A_h(k)=epsilon_h(k)^*.J(k)*ftilde(k),

up to the common coupling/phase convention. Gauge shifts of epsilon leave it unchanged. Normalized helicity polarizations are used in the radiation norm; the code's inherited norm-six polarization representatives are divided by six at the intensity level.

## Why the exact top-hat fails the local compact-source gate

For a smooth current with compact spacetime support, its Fourier transform is entire: differentiation with respect to complex momentum is justified under the finite-support integral, with an exponential bound from that support.

Restrict to the nonsingular null ray k=(omega,0,0,omega), omega>0. A fixed transverse polarization then gives an analytic radiation amplitude along this ray. The proposed top-hat has a nonzero component inside omega in [1/2,1] and zero on an open interval outside. An analytic function vanishing on an open interval vanishes identically, contradicting the nonzero target.

Even continuity alone rules out the particular jump at the band edge. The checker audits that jump exactly at sequences approaching the boundary. It does NOT pretend finite samples prove Fourier analyticity; the exclusion is the analytic argument above.

More generally, smoothing a compact momentum bump does not evade analytic uniqueness for a compact-spacetime prescribed transition current. Radiationless nonzero currents are not excluded: the conclusion concerns a NONZERO radiation amplitude with exact compact momentum support, not the current itself.

This gate is for the stated Fourier/transition-current model, not a blanket assertion about arbitrary all-orders quantum scattering amplitudes or an apparatus with noncompact current tails.

## A genuinely compact smooth source alternative

Define

    b(s)=exp[-1/(1-s^2)] for |s|<1, and 0 otherwise,
    f(t,x)=b(t/tau) b(x_1/ell_1) b(x_2/ell_2) b(x_3/ell_3).

All boundary derivatives vanish, so f and its derived current are C-infinity and compactly supported. The implementation retains the exact exponential factor and rational derivative coefficients separately and checks support and conservation without transcendental rounding.

Its radiation profile is NOT a top-hat. It is nonetheless normalizable:

- compact smooth support implies rapid Fourier decay by repeated integration by parts;
- the dipole factor contributes one power of omega;
- the invariant measure contributes omega*domega/2;
- the norm integrand therefore behaves as omega^3*|ftilde|^2, integrable at infinity and at omega=0;
- choosing further integrations by parts gives finite energy moments of every finite order.

The norm is nonzero: ftilde(0)>0, continuity preserves nonzero envelope near zero, and a nonzero dipole radiates on an open set of transverse directions at small positive omega. The compact-bump normalization is a positive finite integral; no uncomputed numerical value is fabricated.

## Gaussian alternative with an exact radiation normalization

For an isotropic spatial Gaussian, rescale the source envelope so ftilde(0)=1:

    ftilde(k)=exp[-(tau^2 omega^2+ell^2 |k_vec|^2)/2].

This corresponds to the position-space Gaussian divided by (2*pi)^2*tau*ell^3 under the stated Fourier convention. The pointwise current sampler omits this common normalization factor; the analytic radiation formulas explicitly use the Fourier-normalized envelope.

On shell let a=tau^2+ell^2. Then

    sum_h |A_h(k)|^2
      =omega^2[|d|^2-|n.d|^2] exp(-a omega^2),
    N_source = sum_h integral dmu |A_h|^2
             = 2*pi*|d|^2/(3*a^2).

For unit widths and either circular seed candidate, |d|^2=6 and a=2, so

    N_source=pi,
    <omega>=3*sqrt(pi)/(4*sqrt(2)),
    <omega^2>=1.

Dividing the amplitude by sqrt(N_source) defines a normalized conditional one-photon radiation state. N_source is an amplitude norm with the overall coupling omitted, not an emission probability already set to one.

The Gaussian is rapidly localized but NOT compact in spacetime. It provides a closed-form comparison to the genuinely compact bump rather than passing off Gaussian tails as strict finite support.

## Locality changes the angular/helicity profile

Let e_h(n) be a normalized circular polarization about direction n. The angular intensity is

    |e_h(n)^*.d|^2
      = [|d|^2-|n.d|^2+i*h*n.(d cross conjugate(d))]/2.

For the g_plus dipole d=(sqrt(3),-i sqrt(3),0):

- along +z, only helicity -1 is emitted;
- along -z, only helicity +1 is emitted;
- along +x, both intensities are 3/2.

Thus the helicity identification at one momentum is not global helicity purity of this local electric-dipole wavepacket. Under the parity-even Gaussian envelope, integrated helicity probabilities are 1/2 and 1/2. This does not make the photon spin zero; helicity is correlated with momentum direction.

The angular norm is a degree-two polynomial. The checker verifies an exact six-axis spherical averaging rule on all its degree-zero/one/two monomials before using it to recover the integrated helicity intensities. This is not an approximate angular quadrature for the present formula.

## Photon number and probability are not yet inherited

A prescribed CLASSICAL current generates a coherent radiated field, not deterministic one-photon emission. Here a QUANTUM transition matrix element is specified, so the first-order source-changing term has a one-photon component. Its normalized conditional state is determined by A_h(k).

The interaction also needs a dynamical source model, a gap/time dependence and a coupling strength. Higher-order source/field processes have not been computed here. In particular, choosing a coupling so the first-order probability equals one is not a valid proof of deterministic emission. The exact global-control sin^2(theta) law from iteration 6 is not transferred to this local-current model.

## Verification

    python research/nima/checkers/check_photon_local_current.py

Fresh checks pass for current conservation, off-shell Ward identities, Lorentz tensor covariance, Hermitian transition completion, source support, gauge-invariant amplitudes, angular/helicity patterns and analytic Gaussian normalization. The source/packet chain through iteration 6 is rerun separately within the command; its previous checks remain scoped to their own models.

Implementation: `checkers/photon_local_current.py`.

Report: `results/photon-local-current.json`.

## Next executable iteration

Audit quantum source dynamics for this new local coupling, including photon-number contamination and the role of counter-rotating terms. Determine which one-excitation statements survive exactly and which require a controlled approximation. Keep the new conserved-current model separate from the engineered global-control model and include the source gap/time modulation rather than silently assuming it away.

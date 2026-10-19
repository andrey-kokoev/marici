# Exact two-port response with minimal retained conservative memory

## Scope

This construction concerns the existing principal autonomous two-rim contact model, not the latest strained pentachoron scattering model. Its core, ports and metric are reconstructed from `research/strominger/results/neutron-two-rim-contact-binding.json`. The continuum, kinetic, threshold, contact-strength and preparation choices remain supplied model inputs. No physical source selection, measured calibration or scattering-root admission follows.

The excluded unchanged coefficient-law bridge stays rejected. We construct the actual core response rather than fitting that coefficient law to the desired amplitudes.

## Metric and response

Let K be the raw 24-coordinate core operator, M its positive source metric and W its two raw rim columns. The source normalization is W^T M W=3I, so the physical normalized columns in whitened coordinates correspond to W/sqrt(3), not W.

At eta=2, ell=1, the contact-dressed raw core is

    D=K+(2/3) W W^T M.

Regenerate the five-dimensional port Krylov span, with basis B, metric G=B^T M B, left inverse L=G^-1 B^T M, d=LDB, k=LKB and w=LW. The complete state decomposes as

    chi=Bq+n chi,       n=I-BL.

Here n is the metric-orthogonal reducing projector on 19 retained dark directions. Neither their initial state nor their energy is reset or discarded. Ports cannot drive or read them in this fixed contact model; other source operations may act on them.

Define the normalized two-port resolvent response

    R(E)=(1/3) w^T G (EI-d)^-1 w,
    V_eff(E)=2I+4R(E).

The direct 2I contact diagonal and the dressed core diagonal must both be retained. This is a boundary response, not an S matrix, a detector gain, a stored-energy observable or an unconditional probability.

The exact even and odd normalized responses are

    r_even(E)=(3292 E - 2099)/(3292 E^2 - 11069 E + 4198),

    r_odd(E)=(10837264 E^2 - 35494344 E + 23644249)
             /(10837264 E^3 - 65023584 E^2 + 115350575 E - 53719961).

In the actual two-rim basis,

    R(E)=1/2 [[r_even+r_odd, r_even-r_odd],
              [r_even-r_odd, r_even+r_odd]].

There are two visible even poles and three visible odd poles, with no cancellations. The five-state requirement therefore comes from the actual response, not an arbitrary allocation of storage coordinates.

The checker proves equality with the full 24-coordinate resolvent at every resolvent energy by constructing X=(EI-d)^-1 w and verifying

    (EI-D) B X = W,
    (1/3) W^T M B X = R(E).

No energy sampling or 24-dimensional floating inverse replaces this identity. Apparent singularities at decoupled dark eigenvalues can be handled by continuation of the rational port response with zero incoming dark component; the formula is initially proved where the full inverse exists, not by pretending that dark eigenstates are absent.

## Conservative memory realization

The exact retained bright state satisfies

    i*hbar*q' = d q - (eta sqrt(ell)/sqrt(3)) w psi(0).

The boundary mismatch is

    sqrt(ell) psi(0) - w^T G q/sqrt(3).

Combined with the moving lead and retained contact diagonals, this is the same conservative contact form, now in source-addressed core coordinates. With zero boundary drive, the bright generator d conserves q^dagger G q and q^dagger G d q, including its contact diagonal. When driven by the lead it exchanges norm/energy through the contact. It is not separately closed under an arbitrary imposed boundary field.

Eliminating q gives the causal convolution

    q(t)=exp(-id(t-t0)/hbar)q(t0)
         +(i eta sqrt(ell)/(hbar sqrt(3)))
           integral[t0,t] exp(-id(t-s)/hbar)w psi(0,s) ds.

The initial-core term matters. Zero incoming bound/dark component is a preparation convention, not a universal reset rule. No capture probability is inferred from a resolvent pole or a localized level.

## Minimality and positivity

The bare bright core is positive semidefinite with one exact zero mode; the contact-dressed bright core is positive definite. The first checker run correctly failed an overly strong bare positive-definiteness assertion. All bare energy principal minors and all dressed positive pivots are now checked without deleting the zero mode. Contact uplift is conditional on the supplied interaction, not a derived physical mass gap.

The actual ports generate all five bright directions. Metric-self-adjointness makes the realization observable as well. More explicitly define moments

    mu_j=(1/3) w^T G d^j w.

The finite 10-by-10 block Hankel matrix H_ij=mu_(i+j), i,j=0,...,4, has exact rank five. Every finite linear realization of the same strictly proper matrix response factors this Hankel matrix through its memory state, so it needs at least five scalar complex state coordinates. The constructed five-state realization attains this bound.

This is a lower bound for a finite time-invariant linear input/output realization of this exact response. It is not a detector count, an information-storage capacity, the dimension of the whole scattering state or a statement about nonlinear/infinite-dimensional encodings.

For the positive metric, d is similar to a Hermitian operator. Its spectral residues in R(E) are positive semidefinite. Contact controllability makes every bright pole visible. Consequently, for z in the upper half plane,

    Im R(z) = -(Im z)/3 * w^dagger (zI-d)^(-dagger) G (zI-d)^-1 w <= 0.

The sign is tied to the convention (zI-d)^-1; changing the resolvent convention changes the sign. On real resolvent energies,

    R'(E)=-(1/3) w^T G (EI-d)^-2 w.

This is a passive/conservative response statement, not monotonic scattering probabilities. Threshold factors, lead matching and interference still enter the actual scattering calculation.

## Poles are not bound energies or physical species

The checker distinguishes the two parity branches and verifies no numerator/denominator cancellation. Together their visible poles reproduce the five-root bright characteristic polynomial. These are poles of the retained-core resolvent. Bound energies of the lead-coupled system solve the exterior-decay/contact condition and are different objects; no physical mass or particle identification is supplied.

High-energy normalization is E R(E) tending to I. Omitting the source factor 1/3 incorrectly gives 3I. This is a source-metric normalization control, not an independently calibrated physical gain.

## Verification and disposition

Checker: `research/nima/checkers/check_scattering_two_port_memory.py`.

Receipt: `research/nima/results/scattering-two-port-memory-v1.json`.

Run through structured-command using `uv run --with sympy python` and the checker path. The first successful execution passed 42 exact controls, exit 0: `structured_command_execution:e_12616_1791930399749006700_115`. Exact controls include source-receipt freshness, full/bright equality, source reconstruction, parity pole visibility, Hankel minimality, retained dark records, metric and port-frame covariance, and scope-preserving corruption rejection. The final report is rehashed on the final replay. The general time-domain, spectral positivity and minimality interpretations above are written arguments, not a new formal-kernel certificate.

The successor work contract `research/nima/contracts/scattering-core-bridge-work-net.v2.json` records only the conditional mathematical response construction. It retains the rejected coefficient candidate and the open native-contact source-law and broader-root obligations. Version 1 and its accepted research history are not rewritten. Formal outcomes stay unassigned; no stationary scattering solve or measurement work is performed.

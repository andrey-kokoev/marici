# Iteration 6: conditional source-field emission with a drive/work ledger

## The normalized packet now has a specified emission model

Let A_psi^dagger create the normalized continuum packet constructed in iteration 5. Supply a two-level source with states g,e, energy gap Omega>0, and lowering operator sigma_-. Declare the interaction-picture control

    V_I(t)=g(t)[zeta*sigma_- A_psi^dagger+conjugate(zeta)*sigma_+ A_psi],
    |zeta|=1, g(t) real.

The temporal envelope, phase, source gap and continuum form factor are INPUTS. The two-packet seed has not selected them.

Starting from an excited source and field vacuum,

    |e,0> -> cos(theta)|e,0>-i*zeta*sin(theta)|g,psi>,
    theta=integral g(t)dt.

This is exact in the interaction-picture one-excitation sector for the declared control. A pi/2 pulse gives complete source depletion and one photon. A partial pulse gives emission probability sin^2(theta), retaining the vacuum/no-emission branch with probability cos^2(theta).

This result is an emission process in a specified mathematical model, not a laboratory implementation or a source-derived local electromagnetic Hamiltonian.

## Why it is not the forbidden single-frequency substitution

The free Hamiltonian remains the full continuum operator

    H0=Omega*|e><e|+sum_h integral dmu(k) omega_k a_h^dagger(k)a_h(k).

To implement the stated V_I(t), the Schrödinger-picture coupling must contain

    g(t)*zeta*psi_h(k)*exp[-i(omega_k-Omega)t]*sigma_- a_h^dagger(k)+h.c.

The frequency-dependent control phase exactly cancels the free interaction-picture dressing. An unshaped stationary coupling does not do that. This is an explicitly engineered, mode-matched drive; it is not obtained by replacing the broadband packet with an autonomous oscillator of energy <omega>.

For a desired pulse area, one possible smooth envelope is

    g(t)=(theta/T)[1-cos(2*pi*t/T)], 0<=t<=T.

It vanishes at the endpoints and integrates to theta. This supplies a family of mathematical control envelopes, not an experimentally certified pulse.

## Outgoing free phase is retained

The displayed two-state rotation is in the interaction picture. At physical time T, the emitted Schrödinger-picture photon profile is

    exp(-i*omega_k*T)*psi_h(k),

and the un-emitted excited-source component has its phase exp(-i*Omega*T). The heralded record retains the outgoing continuum phase explicitly; it does not silently return an unevolved top-hat amplitude as the physical state at T.

If one wants exactly psi_h(k) at time T, an additional fixed precompensation exp(+i*omega_k*T) in the interaction-picture form factor achieves that. This is extra coherent drive data, not seed-derived timing.

The code retains affine frequency exponents exactly, without approximating continuum exponentials by rounded complex numbers.

## Source, field and no-emission records

The ordered interaction-picture basis is

    |g,0>, |e,0>, |g,psi>.

Its exact control unitary is

    U = [[1, 0, 0],
         [0, c, -i*conjugate(zeta)*s],
         [0, -i*zeta*s, c]],
    c=cos(theta), s=sin(theta).

It preserves total excitation number |e><e|+N_field. The ground source plus field vacuum is dark. Applying a full-transfer unitary twice reabsorbs the retained photon and re-excites the source; it does not generate another photon from an undepleted source.

An ideal field vacuum/one-packet readout gives the source instrument

    K0=|g><g|+c*|e><e|,
    K1=-i*zeta*s*|g><e|,
    K0^dagger K0+K1^dagger K1=I.

A zero-probability emission branch is rejected as a normalized heralded packet rather than being fabricated.

For an initially excited source, the unconditional field is the vacuum/one-packet mixture. For a coherent source superposition, vacuum/one-photon coherence can survive in the reduced field. The checker includes this control; it does not impose the diagonal mixture on arbitrary source inputs. Source density matrices returned by the interface are explicitly in the interaction picture.

## Work and the broadband obstruction

For an initially excited source and p=sin^2(theta), let mu=<omega> and sigma^2=Var(omega). Endpoint interaction energy is zero for the stated switched envelope. The free-energy change supplied by the external drive is

    <W>=p*(mu-Omega).

In a two-projective-energy-measurement work diagnostic,

    <W^2>=p*[sigma^2+(mu-Omega)^2],
    Var(W)=p*sigma^2+p*(1-p)*(mu-Omega)^2.

The no-emission event has W=0; the emission event has W=omega-Omega. For a coherent initial source, an actual initial energy measurement would destroy its energy coherence; the TPM diagnostic is not asserted to leave that unmeasured coherent-source experiment unchanged.

For the constructed profile, full transfer and Omega=1 give

    initial mean free energy = 1,
    final mean free energy = 49/54,
    mean external work = -5/54,
    work variance = 799/23328.

Negative mean work means the prescribed drive extracts net energy on average in this fixture. With a smaller gap it instead supplies positive net energy. These are model energy balances, not derived source scales.

Even setting Omega=mu only makes the MEAN work zero. The exact full-continuum obstruction remains

    ||[H0,V]|e,0>||^2 = integral dmu |psi(k)|^2(omega-Omega)^2
                       = sigma^2+(mu-Omega)^2 > 0,

where V is the unit-strength exchange generator. At the mean gap this is still 799/23328. An autonomous energy-conservation claim is therefore rejected.

The instantaneous control-power expectation is also checked:

    <partial_t V_S>=2*g(t)*sin(theta)*cos(theta)*(mu-Omega)

for the excited initial source. It agrees with the derivative of the free-energy expectation. The envelope-derivative term has zero expectation in this matched state. The compressed power matrix is used only for this expectation, not as a replacement for the full continuum free Hamiltonian.

## What is still not supplied

The global form factor psi_h(k) and its coherent frequency compensation have been programmed into the interaction. No proof yet identifies them with the radiation of a conserved, physically localized source current. The ideal compact momentum top-hat may require noncompact source support or approximation.

Source recoil, angular-momentum exchange and the drive's own quantum degrees of freedom are not closed here. In particular a fixed two-level source with no center-of-mass coordinate is not a proof of momentum conservation for source plus field alone. A real apparatus would need those external supports and calibration.

## Verification

    python research/nima/checkers/check_photon_source_emission.py

Fresh checks pass for the exact unitary, excitation conservation, source instrument, full and partial transfer, dark and coherent-source controls, reabsorption, heralding boundaries, continuum phase compensation, free output phase, work moments and instantaneous power. The run reruns the entire prior packet/Maxwell/Lorentz/Fock/wavepacket chain.

Implementation: `checkers/photon_source_emission.py`.

Report: `results/photon-source-emission.json`.

## Next executable iteration

Audit the mode-matched coupling against a conserved local source current. Determine whether the exact top-hat can arise from a finite-duration/spatially bounded current, and, if not, construct an admissible smooth alternative or a controlled approximation. Keep this source-realization question separate from the already verified global-control unitary.

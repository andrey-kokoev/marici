# Iteration 3: conditional Lorentz and gauge transport of the packet vector

## Result

The iteration-2 Maxwell adapter now extends beyond its fixed +z frame. `PhotonTransportLedger` retains the original six two-packet coefficients, supplied null momentum, polarization representative, cumulative Lorentz frame, and every Lorentz/gauge step.

For a real proper orthochronous Lorentz map Lambda,

    k' = Lambda k,
    epsilon' = Lambda epsilon,
    F' = Lambda F Lambda^T.

The inverse decoder applies the retained Lambda^-1 before the previous gauge-class decoder. Exact tests recover the original six coefficients after boosts, rotations, null rotations, gauge changes and their compositions.

This is a covariant realization INSIDE the supplied Maxwell/Lorentz model. It does not derive that model or a physical photon source from the packet endpoints.

## Example outside the original momentum direction

A supplied x boost with cosh(eta)=5/4 and sinh(eta)=3/4 sends

    (1,0,0,1) -> (5/4,3/4,0,1).

The result is future-directed and null. The transported polarizations remain transverse and obey the free Maxwell equation. A second origin energy scales the momentum consistently without changing the original packet coefficients.

The checker verifies both field-strength covariance and the operator identity

    M(Lambda k)=Lambda M(k) Lambda^-1,
    M(k)=k^2 I-k(eta k)^T.

The Hermitian transverse norm and the pairing with a correspondingly transported conserved current are unchanged. No charge or coupling normalization is added by these checks.

## Null little-group translations are gauge

For k0=(1,0,0,1), define r=(a^2+b^2)/2 and

    N(a,b) = [[1+r, a, b, -r],
              [a,   1, 0, -a],
              [b,   0, 1, -b],
              [r,   a, b, 1-r]].

This is a real proper orthochronous Lorentz map fixing k0. On the original transverse representative at k=E*k0,

    N(a,b) epsilon = epsilon + alpha*k,
    alpha=(a*epsilon_x+b*epsilon_y)/E.

It therefore preserves the field strength and acts trivially on the physical polarization quotient. Tests establish the translation composition and rotation-conjugation laws:

    N(a,b)N(c,d)=N(a+c,b+d),
    R_z(theta)N(a,b)R_z(theta)^-1
      =N(cos(theta)*a-sin(theta)*b,
         sin(theta)*a+cos(theta)*b).

Conjugating these stabilizers by an arbitrary tested frame Lambda gives the corresponding little-group action at Lambda k. The translation part is still gauge there. No extra physical polarization is created by its two parameters.

## Helicity phases in the moved frame

In the active-rotation convention U(R_theta)=exp(-i*h*theta), the inherited candidates still have

    g_plus -> h=-1,
    g_minus -> h=+1

under the DECLARED Maxwell vector action. The conjugated rotation Lambda R_z(theta) Lambda^-1 fixes Lambda k and multiplies the transported circular polarizations by their expected helicity phases.

A decoder using the co-transported frame recovers the original seed coordinates. A decoder using a fixed reference frame records the helicity phase instead. These are different coordinate questions, not conflicting results.

The finite C3 seed still does not uniquely select this continuous spin-one representation. The iteration-1 higher-helicity alias control remains in force.

## Momentum alone is insufficient frame data

Lambda and Lambda R_z(theta) send the original k to the same momentum. If the seed polarization is a linear superposition of the two helicities, holding its coefficients fixed while changing between those frames rotates its physical polarization: the field strengths differ, not merely their gauges.

The checker exhibits this case. Decoding with the wrong frame returns different seed coefficients despite identical momentum. Therefore the interface retains polarization frame information rather than inferring it from the momentum alone. This is not a unique global frame choice over all null momenta.

## Retained transport records

The interface provides:

- `start(seed, gauge)` for a registered conditional origin wave;
- `transport(wave, transformation)` for a validated Lorentz step;
- `regauge(wave, alpha)` for a retained change of gauge representative;
- `decode(wave)` for frame-aware gauge-class recovery;
- `deconstruct(wave)` and `history(wave)` for exact prior-record recovery.

Sequential transport and transport by the composed matrix agree in momentum, polarization and frame, but keep different operation histories. A Lorentz round trip returns the original numerical data without erasing its intermediate records.

Lorentz and gauge changes form a commuting square on numerical representatives when the same scalar gauge parameter is used; both routes remain recorded. Photon-number creation, packet execution and physical apparatus authority are not implied by this registration.

## Hostile controls

The implementation rejects improper, time-reversing, non-Lorentz and complex spacetime maps; malformed dimensions; invalid boost data; substituted or foreign transport records; and inexact gauge inputs. In particular, a complex rotation satisfying c^2+s^2=1 is still rejected by the real-spacetime gate.

Noncommuting transverse boosts retain their order. The same-momentum/wrong-frame control prevents a false inverse-decoding claim. Gauge-zero/pure-gauge wave rejection and the Maxwell adapter's previous scope gates remain active.

## Verification

    python research/nima/checkers/check_photon_lorentz_transport.py

Fresh exact tests pass for the seven primary transformation fixtures and their tested compositions, three seed polarizations, transported currents, little-group identities and provenance controls. The command also reruns iteration 2, iteration 1 and the preceding whole-seed closure.

Implementation: `checkers/photon_lorentz_transport.py`.

Report: `results/photon-lorentz-transport.json`.

## Next executable iteration

The packet now has a conditional covariant Maxwell polarization realization, but this is still a field-mode amplitude, not a state with exactly one photon. Construct a conditional creation-state map for the two helicity components, explicitly declaring the vacuum, bosonic/Fock algebra, mode normalization and momentum support. Test photon number, gauge independence and helicity phase transport without pretending these quantum structures were derived from the seed.

Source selection of the Maxwell/Lorentz/Fock model, electromagnetic source coupling and an executable physical preparation remain distinct open gates.

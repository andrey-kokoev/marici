# Complex response of the retained four-packet feedback cycle

## Question and result

Can the outer factor in 12(12²+3²) be derived as 12+i*eta from the already checked feedback cycle, without fitting eta to a measured mass?

The unchanged feedback operator has genuine complex rotation sectors. Their exact one-step phases are 60 and 120 degrees, with conjugate phases under reversal. However, a pure phase preserves amplitude: replacing a nominal outer response 12 by 12*exp(i*theta) leaves the magnitude of 153 times that response equal to 1836.

It does NOT give 12+i*eta with real part fixed at 12 and nonzero eta. That would require additional quadrature amplitude, a different allocation of record budget, or a different readout. None is selected by the existing cycle. The test derives phases, not a proton mass correction.

## Input kept fixed

Use U from `four-packet-record-feedback.md` without changing its twenty real coefficients, record exchange, preparation or rotation schedule. It satisfies U^T U=I and U^6=I. The prior three-cycle history limit is unchanged; statements about six steps below are operator identities, not extra retained trajectory advances.

The dimensions four and sixteen refer to the carrier and record bank. There is no established map assigning its modes to the twelve directed relationships in `proton-electron-shared-state-comparison-hypothesis.md`. In particular a coincidence of a spectral subspace dimension with twelve is not that assignment.

## Extract the complex structure instead of inserting i

Define real operators

    D = U-U^T,
    P = -D²/3.

Exact matrix calculation gives P²=P=P^T, rank P=8, D^T=-D and D²=-3P. Therefore

    K = D/sqrt(3)

is a complex structure on im P: K²=-I and K^T K=I there. On its complement K vanishes. K is not a new global scalar imaginary unit on the full Clifford algebra.

Let H=U+U^T and

    P_plus  = (P+HP)/2,
    P_minus = (P-HP)/2.

These are orthogonal rank-four projectors with sum P. Their restrictions obey

    U P_plus  = ( 1/2 I + sqrt(3)/2 K) P_plus,
    U P_minus = (-1/2 I + sqrt(3)/2 K) P_minus.

Thus the complex eigenvalues in these oriented sectors are

    exp(i*pi/3), exp(i*2*pi/3).

Their real conjugate partners give the corresponding negative phases on complexification. Replacing U by U^-1 while retaining the same K conjugates the readings. The remaining twelve real dimensions have eigenvalues +1 or -1, not an extra independently selected imaginary response.

These angles belong to rotations of coefficient modes of the supplied linear map. They do not establish physical 60-degree tetrahedral motions or proton spin.

## A concrete phase-sensitive readout

For a nonzero real vector v in either sector, define

    z(v) = <v,Uv>/||v||² + i <Kv,Uv>/||v||².

Then z(v)=1/2+i*sqrt(3)/2 on P_plus and z(v)=-1/2+i*sqrt(3)/2 on P_minus. In both sectors |z(v)|=1. The result is independent of rescaling v. This is a declared quadrature readout using the cycle-derived complex structure, not a derived physical mass observable.

All checks use exact rational matrices and the representation z=a+i*sqrt(3)*b with rational a,b; no approximate eigensolver or measured mass is used.

## Test the proposed outer factor

As a clearly conditional readout test, suppose twelve equal coherent channels share one of these phases. Their total response would be

    A_outer = 12 z.

For the 60-degree sector this is

    A_outer = 6+i*6*sqrt(3),
    153 A_outer = 918+i*918*sqrt(3).

For the 120-degree sector the real parts have opposite sign. In either case,

    |A_outer|=12,
    |153 A_outer|=1836.

Returning through six steps restores phase one. It does not accumulate an additional positive magnitude. A complex phase has been derived, but not an amplitude excess.

By contrast, for the proposed additive response,

    A_outer = 12+i*eta,
    |A_outer|²=144+eta².

If its magnitude remains twelve, eta must be zero. Keeping real part twelve while adding a nonzero imaginary component requires more outer-port squared amplitude than the starting value 144. A record bank could in principle supply that budget, but the relevant coupling, allocation, preparation and scale must be identified; the rotation angle alone does not supply it.

Dividing the phase response by its real part is not innocuous: forcing Re(A_outer)=12 in either of these sectors gives |A_outer|=24. This doubles the magnitude by a new gain choice rather than extracting a small phase correction.

## Counting, amplitudes and energy are different readouts

The previous 1836 construction counts positive-resource labelled comparison instances. A coherent amplitude sum is a different operation, and a squared-amplitude sum is different again. The uniform twelve-channel example above tests the conjecture but does not identify these three readings.

The full spectral trace of this U is zero, not twelve. Neither that trace nor the dimension of its real-mode subspace may be silently substituted for the outer relationship count. A source-authorized adapter to the twelve channels and a physical readout are still required.

The arbitrary seed amplitude is also not fixed by U. Both alpha*v and v have the same extracted phase, while their budgets differ by alpha². No unique eta or physical energy scale can be inferred from the eigenphase alone.

## Verification and disposition

    python research/nima/checkers/check_four_packet_complex_response.py

Fresh checks pass for the complex-structure identities, two projector ranks, both restricted operator laws, all nonzero projected basis witnesses, reversal conjugation, scale invariance, phase-only magnitude preservation, fixed-real-part controls and U^6=I. Result: `results/four-packet-complex-response.json`.

No observed proton/electron mass value or fitted coefficient is an input. No new dynamical law, retention truncation or graphical representation was introduced.

Follow-up: [twelve-channel-record-quadrature.md](twelve-channel-record-quadrature.md) constructs a conditional isometric common-plus-gradient adapter with eta=sqrt(12)*s and conserved readout budget. It derives record return but leaves the physical quadrature convention and seed unselected; conjugate reciprocity would forbid its nonzero common imaginary response.

Next substantive target: specify a source-derived coupling from the retained record bank to a phase-sensitive twelve-relationship response, including its conserved budget and physical readout. The current result prevents confusing a unit-modulus phase with an additive imaginary amplitude correction; it does not rule out such a correction from a separately derived coupling.

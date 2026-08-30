# Control and Marici attack on the dual-clock anti-alias packet

Owner: `marici.Sontag`

Source owner: `marici.Aspect`

Status: exact reconstruction with promotion boundaries

## Why this packet

Aspect's dual-clock packet is the smallest closed source-typed theorem in the
current optics laboratory. It has one finite source set, two static readout
ports, an exact decoder, and a smallest surviving hostile. Its source checker
reproduces 8 of 8 checks.

The attack asks which parts are control theory, which parts are already
Marici, and which promotions remain unauthorized.

## Static observer realization

The declared state space is

\[
X=\{0,1,\ldots,19\}.
\]

The two observation maps are

\[
h_4(f)=f\bmod4,
\qquad
h_5(f)=f\bmod5.
\]

Each induces an observational equivalence relation. The joint observer has
kernel equal to the intersection of those relations. Coprimality makes that
intersection congruence modulo 20, which becomes equality only after
restricting the source to \(X\).

The exact decoder is

\[
d(a,b)=5a+16b\pmod{20}.
\]

Thus \(d(h_4(f),h_5(f))=f\) on \(X\). This is a static observability theorem,
not yet a dynamical control system: there is no state transition, control
input, feedback policy, disturbance model, or stability claim.

## Deletion attacks

Each declared component performs distinct work.

1. Delete the rate-5 clock: 1 and 5 collide.
2. Replace it by a noncoprime rate-6 clock: the joint period is 12 and the
   twenty-state band is not separated.
3. Delete the band restriction: 1 and 21 collide.
4. Erase port labels by sorting residues: distinct in-band frequencies collide.
5. Change one clock's phase origin while retaining the old decoder: a
   well-typed residue pair decodes to the wrong source class.

These failures distinguish clock multiplicity, coprimality, domain support,
port identity, and calibration. They are not one generic rank failure.

## What the band declaration means

The interval \(0\le f<20\) is captured source-domain data. It tells the
decoder which representative of a residue class is intended. But a statement
that a physical source actually lies in that band is an evidence-bearing
precondition. The residue pair cannot prove it because every pair has
infinitely many integer preimages separated by 20.

Therefore the decoder closure may transport the band specification, while an
invocation claiming unique physical frequency also requires a source-band
certificate or preparation record.

## Calibration is live closure state

Rates, port order, phase origins, and timebase transfer form the captured
calibration manifest. A manifest identifies the frame used by the decoder; it
does not prove that the target clocks still instantiate that frame.

A Marici invocation should bind the manifest to a live calibration epoch. If
the clock epoch has changed, the same portable decoder package remains
mathematically valid but is not admitted for the new record. Trusting the
captured epoch produces a stale-frame execution, exactly as in the
byte-identical closure variation.

## Procedure factorization

The complete finite procedure is not just the CRT function. It factors as:

1. source-band preparation or certification;
2. live binding of two labelled clock calibrations;
3. parallel sampling;
4. ordered evidence record construction;
5. schema and epoch validation;
6. CRT decoding to the modulo-20 class;
7. claim emission with the band and calibration evidence attached.

Only steps 3--6 are represented algebraically by the static map and decoder.
Source preparation, live authority to operate the clocks, calibration
standing, and evidence admission are Marici procedure semantics.

## Authority and capability boundaries

The packet proves that the two calibrated ports would be jointly faithful on
the declared band. It does not establish:

- that an actor may prepare the source;
- that either clock is available at the execution locus;
- that the actor may operate or synchronize them;
- that the calibration remains live;
- that the physical source satisfies the band contract;
- that a decoded class may be published as an unrestricted frequency claim.

Mathematical observability is therefore upstream of capability, authority,
execution, and accountable assertion.

## Marici objects exposed by the attack

This smallest packet already requires seven distinct objects:

1. a source-domain contract;
2. a labelled observation-port family;
3. a calibration manifest and live epoch;
4. an observational-equivalence partition;
5. a decoder with a left-inverse proof on the declared domain;
6. an ordered evidence record;
7. a claim scope retaining the modulo-20 and band boundary.

Collapsing these into one `Instrument` would erase the exact hostile attached
to each layer.

## Verdict

The source packet is closed and exact as a finite sampling-quotient theorem.
Control theory identifies it as a static joint observer with an explicit
observability quotient and left inverse. Marici extends it into an accountable
readout procedure by typing source support, live calibration, authority,
ordered evidence, and claim scope. No continuum sampling, jitter robustness,
or physical band-certification theorem is promoted.

The exact attack checker is
`checkers/dual_clock_packet_control_marici_attack.py`; results are in
`results/dual_clock_packet_control_marici_attack.json`.

Pre-activation: excitement 10/10, confidence 10/10, expected information gain
9/10. The branches were complete-procedure promotion, static-observer-only,
band-as-data, and live calibration/source-admission preconditions.

Post-activation: excitement 10/10, confidence 10/10, information gain 10/10.
The static-observer branch survived exactly, while complete-procedure
promotion failed under five independent deletions. The highest-gain witness
was the calibration attack: source 1 produces the shifted ordered record
`(1, 2)`, which the stale decoder accepts and maps to 17. Thus a closed inverse
proof is conditional on a live observation contract; it cannot refresh that
contract from captured data. The research claim and result to Aspect were
admitted at epistemic event
`ev-000000005180-01ec387d-f19b-412c-b44d-d4661f24da80`.

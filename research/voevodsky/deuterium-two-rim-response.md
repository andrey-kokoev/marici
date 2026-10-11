# Deuterium: two source-rim maps and a binding-sign test

## Joint attachment, not another bridge contact

Active SCC obligation: attachment transport before binding readout. The source belt has lower-rim triangle indices (1,7,13) and upper-rim indices (4,10,16). These triangles carry the three actual boundary edges of each rim. They are different from the cross-face bridge contacts tested previously.

On the aligned six-amplitude belt sector the joint trace is

    T(a)=(a_1,a_4).

It is the mean retained mode coefficient around each rim. The source norm pairing is diag(3*n), retaining all three sectors. This supplies the belt side of both coefficient interfaces; the geometric match to a proton face or an electron face does not determine their coefficient adapters.

The electron's retained boundary-cell state has two spinor components. Mapping it to this scalar trace requires a typed channel or covariant pairing. No spinor is replaced silently by one scalar amplitude.

## Exact harmonic extension and joint compatibility

For prescribed lower and upper coefficients b, minimizing the source energy over the four other amplitudes gives a unique extension E b. The checker verifies

    T E=I,
    (M K E)_interior=0.

For every original aligned state a, retain the full decomposition

    a=E T a+r, T r=0.

The residual has four coordinates; it is not discarded. Its energy is orthogonal to the extension energy. Thus the two rim values and this residual reconstruct the state exactly.

The joint effective energy is

    c*|b_lower-b_upper|^2,
    c=1499960093/591106225 approximately 2.537547448430.

The factor of three in the aligned metric is included. This is the source-side rim stiffness, not a binding constant selected from an isotope mass.

The equal-rim and opposite-rim frequency responses access the face-even and face-odd blocks respectively. Their exact rational resolvents are retained in `deuterium_two_rim.json`; replacing the belt by two independent terminal bits would lose those modes and their response memory.

## Binding-sign result

Equal rim amplitudes attain zero compatibility energy. Opposite unit amplitudes cost 4c. The gluing energy is nonnegative and cannot lower the composite below a breakup threshold consisting only of zero constituent constraint energies.

This rules out interpreting the successful face/rim match itself as attractive nuclear binding. A common-vacuum interacting law may define a different breakup threshold, but that must be calculated in the same system with its exterior resources retained. The existing open-flux model has not yet been extended to the typed proton–belt–electron attachments.

## Mass readout: reuse the existing constructor

Nima's `hydrogen-mass-readout.md` already supplies the exact invariant-mass and radiation/recoil constructor. Its deuterium extension retains the complete tuple

    (m_p,m_n,m_e,B_nuclear,B_electronic),

with

    M_deuteron=m_p+m_n-B_nuclear,
    M_atom=M_deuteron+m_e-B_electronic.

An effective one-photon threshold channel verifies exact four-momentum conservation and mass shells. It is a kinematic test of supplied bindings, not a derivation of a two-stage capture process. Nuclear controls 0, 1 MeV and 2.2 MeV are deliberately illustrative; the last is not an observed deuteron binding input. The old hydrogen electronic binding is used only as a readout control, not as a deuterium prediction.

The atom's mass depends on the supplied binding while the closed atom-plus-radiation system preserves the initial invariant mass. Both binding inputs remain separate from the derived nonnegative rim stiffness.

## Reproduction

    python research/voevodsky/checkers/check_deuterium_two_rim.py
    python research/voevodsky/checkers/check_deuterium_mass_readout.py
    python research/aspect/scc/scc.py check voevodsky-deuterium-rim-response

Packets:

- `research/voevodsky/results/deuterium_two_rim.json`: actual rim indices, joint trace, minimum-energy extension, retained residual, both response channels and source hashes.
- `research/voevodsky/results/deuterium_mass_readout.json`: full-source recovery, mass-shell and recoil/radiation controls.
- `research/voevodsky/scc-models/deuterium-rim-response.json`: typed attachment obligation and missing proton/spinor coupling.

Next construction: a particle-sector-preserving interaction between the typed external constituent ports and these two rim traces, with its breakup energy calculated in the common vacuum. Positive matching penalties alone have failed the binding test.

# Equal nonzero transport with different actual photon cuts

## Question and result

Can the extra degree-six scale-null cut direction occur as a difference between two actual real sources, despite being excluded from the zero-transport fibre?

[Contract](contracts/photon-equal-transport-v1.json) · [checker](checkers/check_photon_equal_transport_v1.py) · [tests](checkers/test_photon_equal_transport_v1.py) · [receipt](results/photon-equal-transport-v1.json).

**Yes.** An exact rational source curve has the same nonzero six-coordinate degree-six common-log transport everywhere and different full degree-six cuts. Both explicit witness sources retain all three nonzero quartic contacts and are not common-sign partners. This disproves recovery of generic degree-six cut data from degree-six transport alone in the imported model. It does not disprove recovery after adding lower-degree cut data.

This is a mathematical counterexample in fixed amplitude frames and normalized units of the real parity-even eight-contact Born domain at quadratic two-photon order. No actual matching value, preparation, native dynamics, full physical IR inventory or UV completion is selected. Polynomial identities certify the entire family; exact samples supplement rather than replace that certificate.

## 1. A genuine constant-transport curve

For any real v let

    d=7+30*v^2,
    p=14*v/d, q=(7-30*v^2)/d,
    X(v)=(1,0,p,q,0,-7*p^2/16,-5*p^2/56,-5*p*q/84)

in source order (g2,f2,g3,f3,h3,g4,g4prime,f4). The denominator is strictly positive for all real v, and

    q^2+(30/7)*p^2=1.

The quartic contacts vary as explicitly retained coordinates, not as assumed vanishing nuisance parameters or physically selected matching relations. The common-log transport in order (G6,G6prime,G6doubleprime,F6,F6prime,H6) is exactly

    T(X(v))=(-1/960,1/960,0,0,0,0).

Thus it is nonzero and independent of v. Multiplying the source coordinates by d^2 and the monomials by d^2 gives polynomial numerators. The checker verifies all twelve source-factorization identities, all six constant-transport identities, and all seven cut-response identities coefficientwise. This is a genuine entire real parameter curve in the source domain, not a Jacobian null vector that might fail to integrate.

## 2. Cut response along the curve

In the established response order (D0,D2,O0,O2,M2,M3,H), with H the positive logarithmic single-minus coefficient,

    R(X(v))=(1/1152,1/5760,0,0,0,0,0)
              +(p^2/4032)*(-3,-3,0,0,5,1,0).

The second vector is exactly the linear transport-null cut direction. Since p^2 varies, so does the cut. The zero-fibre theorem remains valid: no individual nonzero cut in this family has zero transport; differences of factorizable vectors need not themselves be factorizable.

Choose v=1 and v=2. The actual rational sources are

    X1=(1,0,14/37,-23/37,0,-343/5476,-35/2738,115/8214),
    X2=(1,0,28/127,-113/127,0,-343/16129,-70/16129,565/48387).

All three quartic contacts are nonzero in each source. Their leading g2 is the same positive mathematical coordinate, so they cannot be related by simultaneous sign reversal. Their full cut response difference is

    R(X2)-R(X1)=[-24857/1059868848]*(-3,-3,0,0,5,1,0).

In particular their forward D cut coefficients differ by 24857/176644808, already enough to distinguish them. The full angular polynomials are also compared directly using the independently projected cut inventory, not just the seven-coordinate calibration.

These are formal source values in fixed units, not physically measured couplings. No same-scope UV constraints have been admitted to select or exclude them.

## 3. Lower-order data and the remaining inverse question

The degree-four cut data agree because (g2,f2)=(1,0) throughout. But the calibrated degree-four/five data contain g2*g3=p and g2*f3+10*f2*g3=q, which vary. The witness pair therefore has **different degree-five data**. It does not establish failure of a joint inverse using those earlier cuts together with degree-six scale transport.

Next test whether that joint data reconstructs the missing degree-six cut coordinate and hence recovers the previously classified source fibres. Retain zero-leading and cancellation strata and every independent quartic input. A positive result must provide exact charts and image conditions; a negative result needs a genuine same-joint-data/different-cut source witness. Neither follows from the zero-fibre theorem or the present counterexample alone.

## Controls and scope

There are 36 exact rational parameter controls in addition to the coefficient-polynomial identities. Eight tests, scoped SCC and a fresh headless receipt check factorization, nonzero constant transport, distinct cuts, nonzero quartic inputs, non-sign-equivalence and the lower-data limitation. General curve identities are documented algebra, not proof-assistant formalization. All eighteen finite local matching directions remain free; the eight-source curve is not a selection of those higher local coefficients.

C1–C12 dispositions, zero/not-renewed C12 budget and the high-energy pause remain unchanged. Native preparation, physical matching and UV gates are unearned. See [frontier v3](photon-eft-frontier-v3.md).

```text
python -S research/nima/checkers/check_photon_equal_transport_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_equal_transport_v1.py
```

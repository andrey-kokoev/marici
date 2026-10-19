# Joint lower cuts and degree-six transport recover the full cut

## Question and result

Does the loss from degree-six transport alone persist after adjoining the complete degree-four/five cuts?

[Contract](contracts/photon-joint-transport-v1.json) · [checker](checkers/check_photon_joint_transport_v1.py) · [tests](checkers/test_photon_joint_transport_v1.py) · [receipt](results/photon-joint-transport-v1.json).

**No:** the joint data reconstruct every full degree-six cut response on the actual real eight-contact source domain. Their real image and source fibres are therefore exactly equivalent to those of the already classified joint degree-four/five/six cuts. This includes zero-leading and cancellation strata, irrational source branches and the wholly unseen quartic contacts when the leading pair vanishes.

The theorem is pointwise/exact within the imported real parity-even on-shell photon contact ansatz and quadratic two-photon order. It is not a stability theorem, numerical matching, native dynamics or UV completion. All eighteen finite local matching coefficients remain free.

## 1. Data and the missing coordinate

Write the complete calibrated lower data as

    J=(a,b,c,u,v,w,z)
      =(g2^2,f2^2,g2*f2,g2*g3,f2*f3,g2*f3+10*f2*g3,h3*(6*g2+f2)).

Let B=(G,Gp,Gpp,F,Fp,Hb) denote the six common-log transport coefficients in the established G6,G6prime,G6doubleprime,F6,F6prime,H6 normalization. These are formal mathematical data, not measured couplings or finite matching values. Use the previously proved lower-data real image conditions before choosing a leading chart.

The transport map loses only M3=g3^2/4032. This coordinate is recovered by distinct exact charts:

    if a>0:       g3^2=u^2/a;
    if a=0,b>0:   g3^2=w^2/(100*b).

These remain valid on the single-minus cancellation loci; they do not divide by 6*g2+f2 or 10*g3+f3.

If a=b=0, the valid lower data are all zero and degree-six data reduce to the cubic square. First calculate

    O2=(Fp-12*F)/18.

On precisely this zero-leading stratum, O2=h3^2/480 and

    Gpp+2*O2=-(5/336)*g3^2.

Consequently g3^2=-(336/5)*(Gpp+2*O2). The checker verifies that last identity coefficientwise on the entire six-monomial cubic-square block. It is not extended to nonzero leading sources with independent quartic interference. A negative recovered square or inconsistent remaining data is rejected by the source-image conditions below, not reinterpreted as a complex source.

## 2. Full angular response reconstruction

Set m3=g3^2/4032 and calculate

    m2=5*m3-Gpp/2,
    d2=(Gp-4*m2+2*m3)/6,
    d0=-G-d2-m2-m3,
    o2=(Fp-12*F)/18,
    o0=-4*F-o2,
    h=Hb/3.

Then the complete physical cut polynomials are

    D=d0*P0+d2*P2,
    O=o0*P0+o2*P2,
    M=m2*d22^2+m3*d22^3,
    single-minus=-h*alpha*(1-alpha).

The minus sign in the final section follows the fixed logarithmic/right-cut convention. The six transport rows augmented by the M3 row give an invertible seven-by-seven map; its inverse is checked on every coordinate basis vector. Thus the whole angular response is determined, not merely a fitted set of forward coefficients.

Conversely the original cut data determine B by their fixed linear transport map. Together these maps give a bijection of the two **realizable joint data images**, preserving the actual source preimage of every datum. No physical sign or source is chosen by this change of data coordinates.

## 3. Necessary and sufficient real image conditions and fibres

The construction is a complete image test, not an assertion that arbitrary thirteen real numbers are physical data:

1. Require seven lower coordinates and six transport coordinates, and impose the complete degree-four/five real Gram/factorization conditions from the [lower-cut charts](photon-joint-cut-fibres-v1.md).
2. Use the appropriate chart above to reconstruct M3 and all four angular cut sections.
3. On a nonzero leading pair, apply the exact overdetermined residual solve and square/linear conditions of the [nonzero-leading classifier](photon-joint-degree6-fibres-v1.md). This retains unknown g4,g4prime,f4 and all polynomial rows.
4. On zero leading pair, impose the full [cubic-square image conditions](photon-zero-leading-fibres-v1.md), including the cubic Gram, h3 square, linear/square relation and whole polynomial consistency. All three quartic contacts remain free.

Necessity follows from the response identities. For sufficiency these conditions construct exactly the earlier real source fibres for the reconstructed cut, whose transport is the supplied B by the augmented inverse identity. They therefore furnish actual sources for the joint data. This is a constructive real-algebra argument, not proof-assistant formalization.

The source fibres are unchanged: nonzero leading data give two common-sign sources except double cancellation with nonzero h3, which gives four. At h3=0 the relative-sign branches merge. Zero leading data have two or four cubic branches each carrying a quartic R3, or a single quartic R3 at zero cubic with antipodal common sign and a fixed origin. Irrational leading roots and independent irrational h3 branches are retained algebraically. None of these fibre statements licenses selecting actual matching values.

## 4. Controls and the next boundary

There are 414 exact source controls: 352 g2-nonzero, two f2-only and 60 zero-leading sources, including both cancellations, pure h3 and pure quartic cases. Three algebraic controls retain sqrt(2) leading roots, h3=+/-sqrt(2) on double cancellation, and a mixed sqrt(7) pair with normalized h3 square 2/7. Six incomplete/incompatible data controls are rejected. Eight tests, scoped SCC and a fresh headless receipt accompany these identity controls; no fresh full-suite or physical-evidence claim is made.

The [equal-transport counterexample](photon-equal-transport-v1.md) does not survive the added lower data: its two lower inputs reconstruct their respective different cuts. The transport-only counterexample and the present joint-data theorem are consistent.

Next examine **stability near the zero-leading boundary**, explicitly tracking quartic nuisance size. Ratios u^2/a or w^2/b in an exact chart do not imply a uniformly stable readout. Separate any unbounded-source counterexample from conclusions under an admitted finite source bound; do not silently assume such a bound from EFT terminology. Actual preparation, finite matching, native dynamics and UV/dispersive hypotheses remain unearned. C1–C12 and the zero/not-renewed C12 budget are unchanged. See [frontier v3](photon-eft-frontier-v3.md).

```text
python -S research/nima/checkers/check_photon_joint_transport_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_joint_transport_v1.py
```

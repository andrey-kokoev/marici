# Subthreshold photon unitarity cuts on the Bose carrier

[Contract](contracts/photon-unitarity-cut.v1.json) · [checker](check_photon_unitarity_cut.py) · [receipt](results/photon-unitarity-cut.v1.json)

## 1. Scope and optical normalization

The [crossed leading tensor](CROSSED-FOUR-PHOTON.md) produced the real scalar photon partial waves A_minus=R+C and A_plus=-C below the charged threshold, with C(s)=integral_0^1 R(-s*x)dx. It did not supply their next absorptive terms. Here derive the **pure order-g2^4 photon-intermediate coefficient**, using 0<s<4, m=1 and b=epsilon2^2.

This is not every order-lambda^4 term in the two-coupling theory. Independent g3 contributions, additional interactions and their multiparticle cuts remain separate. In particular the cubic photon vertex can have other photon-number consequences; it is not set equal to g2 or declared absent. In the restricted scalar interaction, two insertions supply four external photons, so the only subthreshold intermediate amplitude needed for this coefficient is the photon pair. All Fock sectors remain in the carrier; none is deleted. Extra channels at the same order would add positive terms with the leading photon amplitude held fixed, converting the stated equality to a lower bound.

For each normalized Bose partial-wave carrier write

    S=I+i*T,
    T=(b/2)*A+b^2*B+... .

Below the massive-pair threshold A is real Hermitian. The exact optical identity 2*Im T=T^dagger*T fixes

    Im B=A^dagger*A/8.

This is the absorptive coefficient forced by unitarity, not an exact S matrix. Real order-b^2 subtraction data, crossed cuts and all-orders dynamics remain unconstructed. No incident polarization average or population over J,M is selected.

## 2. Retain all helicities, then impose Bose symmetry

In the ordered pair labels (++ , -- , +- , -+), the preceding tensor gives

    A(s,z)=(1/2)*[[R(s), -(R(s)+R(t)+R(u)), 0, 0],
                 [-(R(s)+R(t)+R(u)), R(s), 0, 0],
                 [0, 0, R(u), R(t)],
                 [0, 0, R(t), R(u)]],
    t=-s*(1-z)/2, u=-s*(1+z)/2.

The equal/opposite-helicity blocks decouple at this leading order because a three-plus/one-minus all-outgoing configuration cannot pair into two nonzero pseudoscalar vertices. This is derived from all sixteen assignments, not assumed from the displayed scalar block.

The four ordered labels are **not four independent Bose states**. Equal helicities permit even J only. For mixed helicities J>=2, the normalized physical combination is (|+->+(-1)^J|-+>)/sqrt(2). Thus the carrier dimensions per M are:

- J=0: the two scalar parity channels;
- J=1: none;
- even J>=2: two equal-helicity parity channels and one mixed channel;
- odd J>=3: one mixed channel.

Use normalized angular measure and Wigner d projections. At J=2, d22=((1+z)/2)^2 and d2,-2=((1-z)/2)^2. Its ordered mixed block is [[D,D],[D,D]], but the physical Bose eigenvalue is **2D**. Its cut is therefore four times the square of a single ordered diagonal entry, before the common 1/8. At odd J the sign changes in the off-diagonal and in the Bose vector, with the same norm result. The forbidden combination is null; no second independent mixed state is added.

## 3. General-J moments and the first higher-J carrier

For a monomial R(s)=r_k*s^k, k>=2, define equal-helicity crossed moments E_kJ for even J and mixed moments H_kJ for J>=2. They vanish for k<J. Otherwise

    E_kJ=(-1)^(k+J)*(k!)^2/[(k-J)!*(k+J+1)!],
    H_kJ=(-1)^k*(k-2)!*(k+2)!/[(k-J)!*(k+J+1)!].

The integral representations are (-1)^k*integral_0^1 x^k*P_J(1-2*x)dx and (-1)^k*integral_0^1 x^(k+2)*P_(J-2)^(0,4)(2*x-1)dx. Rodrigues integration by parts gives the factorial forms. The mixed expression already includes the coherent Bose factor, not a single ordered entry. The checker compares independent polynomial expansions against 110 exact factorial moments.

For J=0 the eigenvalues are R+C and -C. For even J>=2 the leading carrier eigenvalues are E_J,-E_J,H_J; odd J>=3 has H_J alone. This diagonalization is scoped to the declared leading tensor, not every higher-order interaction. In particular,

    E_2=c0*s^2/30-c1*s^3/20+s^4/(105*pi)+...,
    H_2=c0*s^2/5-c1*s^3/6+s^4/(42*pi)+....

The full helicity sum gives Im B_J=diag(eigenvalues_squared)/8 in this basis. A nontrivial photon complement has mandatory absorptive terms even though the selected scalar parity sector does not leak into it. For J>=4, the first nonzero dispersive Taylor coefficient occurs at k=J; J=3 has a possible c1 term and otherwise starts at k=4.

## 4. Infrared regimes and certified cuts

For either scalar parity, and the J=2 carrier, the first IR power depends on the **unfixed** local subtraction data. The following entries multiply the listed common factor and s^q in Im B; the full Im T contribution is b^2 times this coefficient.

| subtraction regime | q | common factor | J0 minus | J0 plus | J2 minus / plus | J2 mixed |
|---|---:|---|---:|---:|---:|---:|
| c0 nonzero | 4 | c0^2 | 2/9 | 1/72 | 1/7200 | 1/200 |
| c0=0, c1 nonzero | 6 | c1^2 | 9/128 | 1/128 | 1/3200 | 1/288 |
| c0=c1=0 control | 8 | 1/pi^2 | 1/200 | 1/7200 | 1/88200 | 1/14112 |

The zero-subtraction choice is still only a control. Neither positivity nor this table selects c0,c1. In every regime the orthogonal scalar channel has a nonzero leading cut. At isolated energies a phase may vanish; strict positivity for every s and arbitrary subtraction data is not claimed.

The checker also encloses Im B at s=1,2 for all five waves in the zero-subtraction control. It bounds the full convergent leading-amplitude series, squares interval bounds and uses the preceding rational pi enclosure. These are ten exact implementation certificates, not physical rates. The zero-threshold location is that of a photon pair: although the leading massive-pair response was analytic at zero, photon-intermediate discontinuities arise at the next coupling order.

## 5. Right-cut IR logarithm, with a finite-window boundary

Suppose Im B(t)=kappa*t^q+... near zero, as in the table. Choose 0<mu<4 and retain only this leading monomial as an IR comparison density. A twice-subtracted **right-cut component** is

    B_IR(s)=(kappa*s^2/pi)*integral_0^mu t^(q-2)/(t-s)dt
      =(kappa/pi)*[sum_(p=2)^(q-1) s^p*mu^(q-p)/(q-p)
                    +s^q*(log(mu-s)-log(-s))].

Its right-cut nonanalytic term is -(kappa/pi)*s^q*log(-s). On the upper physical rim log(-s)=log(s)-i*pi, giving the positive Im B=kappa*s^q. Higher powers of the actual cut density give higher IR terms; the displayed finite-window function is not the entire cut spectrum. Regular terms depend on the window and subtraction data. The branch at the artificial endpoint mu belongs to this split representation, not a new physical threshold; matching the rest of the cut must remove that bookkeeping dependence. The checker verifies the integrand division exactly and encloses three spacelike monomial witnesses using rational log(2) bounds.

Subtractions at zero need care once a massless cut is present. For this leading density an n-times-subtracted integral at a fixed off-cut s behaves as t^(q-n) at its lower endpoint and exists only for n<=q. The q-th Taylor derivative itself is logarithmically singular for the right-cut component. Arbitrary extra subtractions at zero are not an IR cure. No UV growth or high-energy subtraction count is inferred from this subthreshold window.

**Do not call this the complete crossed infrared germ.** At this order photon cuts in crossed channels can also begin at zero. Their projections may add logarithms or alter cancellations in the total upper germ. Their coefficients must be derived, not guessed from one right cut or from pointwise phase exponentiation. We have fixed the positive physical photon cut, not all its dispersive completion. Likewise an order-b^2 cut cannot repair the older order-b fractional Cayley response in a fixed-s perturbative comparison. Nonuniform resummations or new same-order massless dynamics would be additional assumptions.

## 6. Executable successor and evidence limits

The [crossed photon IR-log audit](CROSSED-PHOTON-IR-LOGS.md) now crosses the leading-IR pure-g2^4 photon cuts in all three subtraction regimes. Both scalar parity real logs survive in these controls, with partial cancellations and sign changes; right-cut positivity is unchanged. This is a leading-IR kernel, not the full quartic spectrum. The [local counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) now supplies 3, 5 and 6 independent on-shell coefficients in the parity-even log-supported sectors at q=4,6,8, with beta=-h for log(nu); finite matching remains free. This is not a complete off-shell EFT basis or anomalous-dimension matrix. The [mixed photon IR-log audit](MIXED-PHOTON-IR-LOGS.md) now constructs the degree-five `c0*c1` cuts and their three local running coefficients. Its scalar real-log coefficients are 31/144 and 5/144 with `c0*c1` stripped; signed interference preserves positivity of the complete two-term square. The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected. The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence. The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded. The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds. The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free. The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected. Next construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. Do not identify a positive optical-theorem coefficient with a crossing-complete causal S matrix.

The projection, optical and dispersion arguments are documented mathematics, not machine-formalized proofs. Exact checks cover nine full helicity matrices, 110 general-J moments, coherent Bose norms, the three IR regimes, ten subthreshold cut boxes and 27 IR polynomial-division identities. Native preparation and local interacting dynamics remain unlicensed. C1-C12, exhausted C12 effort, high-energy pause and historical owner/hash warnings are unchanged; no physical rate or branching ratio is admitted.

```sh
python -S research/scattering/low-energy/check_photon_unitarity_cut.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_photon_unitarity_cut.py
```

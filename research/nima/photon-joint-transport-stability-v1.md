# Stability boundary of exact joint-data photon-cut reconstruction

## Question and result

Does the [exact joint-data reconstruction](photon-joint-transport-v1.md) remain continuous near zero leading coupling without controlling quartic nuisance contacts?

[Contract](contracts/photon-joint-transport-stability-v1.json) · [checker](checkers/check_photon_joint_transport_stability_v1.py) · [tests](checkers/test_photon_joint_transport_stability_v1.py) · [receipt](results/photon-joint-transport-stability-v1.json).

**Without a source bound, no:** there are actual-source data converging to a realizable zero-leading datum while their reconstructed cuts stay a fixed distance from its cut. All three quartic contacts diverge explicitly. **With stated bounds on g4 and g4prime,** an exact bias identity gives a quantitative continuity estimate at that boundary. These statements are compatible and do not imply that a bounded physical source class is unstable.

The scope remains the imported real parity-even eight-contact Born model, retained quadratic two-photon degree-six cut, fixed amplitude frames and normalized coefficient units. No actual source bound, physical matching, uniform EFT validity window, native dynamics or UV input is derived.

## 1. Exact discontinuity witness on the unbounded data image

Take the v=1 source from the [constant-transport curve](photon-equal-transport-v1.md):

    x=(1,0,p,q,0,K,L,M),
    p=14/37, q=-23/37,
    K=-343/5476, L=-35/2738, M=115/8214.

For epsilon>0 rescale

    X_epsilon=(epsilon,0,p,q,0,K/epsilon,L/epsilon,M/epsilon).

More generally rescaling the eight source coordinates by epsilon powers (1,1,0,0,0,-1,-1,-1) preserves all twelve degree-six source monomials: every retained product has total exponent zero. This is checked coefficientwise via all twelve pair exponents, not inferred from a few small epsilon values. Thus every X_epsilon has the same nonzero transport B*=(-1/960,1/960,0,0,0,0) and the same degree-six cut as x.

Its calibrated lower data are

    J_epsilon=(epsilon^2,0,0,epsilon*p,0,epsilon*q,0) -> 0.

The limiting joint datum (0,B*) is itself realizable, for example by Y=(0,0,0,1,0,0,0,0). Its cut response is R0=(1/1152,1/5760,0,0,0,0,0), while every X_epsilon has response R0+(p^2/4032)*(-3,-3,0,0,5,1,0).

Use max norms on the fixed thirteen joint-data coordinates and on the thirteen D/O/M/single-minus polynomial coefficients. For 0<epsilon<=23/37,

    joint data distance = (23/37)*epsilon,
    cut coefficient distance = 7/10952,
    required inverse amplification = 7/(6808*epsilon).

The reconstruction therefore is not continuous at this realizable datum on the full unbounded source image. The forward source-to-data and source-to-cut maps remain polynomial and continuous: the source sequence does not converge. Its maximum quartic contact magnitude is 343/(5476*epsilon), and **all three quartic contacts diverge**. Four exact epsilon controls verify these identities in addition to the universal rescaling argument.

This is not a bounded-source counterexample and establishes no common perturbative/low-energy validity window for the diverging family. Rescaling an interaction strength to repair such a physical window would also rescale the data and requires a separate analysis. No physical instability or measured uncertainty is inferred from these formal coefficient limits.

## 2. A universal missing-coordinate bias identity

For arbitrary supplied transport B=(G,Gp,Gpp,F,Fp,Hb), put

    O2hat=(Fp-12*F)/18,
    M3hat=-(Gpp+2*O2hat)/60.

Let Rhat(B) be the seven-coordinate augmented response inverse from the preceding packet with M3 replaced by M3hat. It is a linear surrogate, equal to the true response for realizable zero-leading data. Away from that stratum it need not be an actual-source cut and is not a substitute real-image classifier.

For **every** actual real eight-contact source, exact coefficientwise identities give

    b = M3-M3hat
      = -g2*g4/1680 + g2*g4prime/7200 - f2*g4prime/43200,
    R-Rhat(B)=b*(-3,-3,0,0,5,1,0).

The h3 square and all cubic terms cancel from this bias identity. No bound on f4 is needed for this particular missing coordinate; its contributions to the other response directions are already carried by B. This is not a statement that f4 is physically unobservable or globally harmless.

The response max norm of the line vector is five. Its D/O/M/H polynomial-coefficient max norm is eighteen. The checker derives the complete surrogate matrices and their exact ambient max-norm bounds:

    ||Rhat(B)-Rhat(B0)|| <= (61/18)*||B-B0||,
    ||Chat(B)-Chat(B0)|| <= (13/3)*||B-B0||.

These are linear-operator bounds, not claims of a physically minimax measurement prescription.

## 3. Conditional bounded-nuisance boundary estimate

**Assume explicitly**, without deriving a physical prior, that |g4|<=Kmax and |g4prime|<=Lmax. Then

    |b| <= E := |g2|*Kmax/1680
                 +|g2|*Lmax/7200+|f2|*Lmax/43200.

Let (0,B0) be any realizable zero-leading datum, with actual response R0 and cut coefficient vector C0. Since its bias vanishes,

    ||R-R0|| <= (61/18)*||B-B0||+5*E,
    ||C-C0|| <= (13/3)*||B-B0||+18*E.

The leading magnitudes are available from the exact lower data as |g2|=sqrt(a), |f2|=sqrt(b_lead). Therefore as joint data approach (0,B0), fixed finite Kmax,Lmax ensure E->0 and cut continuity at this boundary. This estimate remains valid regardless of the other contacts' sizes when the supplied transport data are used; it does not select their values.

The counterexample in section 1 has no fixed Kmax,Lmax, so E does not tend to zero and there is no contradiction. Neither an EFT label nor exact source-factorization charts license a finite native bound. Nor does this boundary estimate prove a global two-data noise modulus or a stable unique Born-source inverse; residual sign ambiguities remain.

## Controls and next test

The bias, rescaling and linear inverse identities supply the general algebra; norm and triangle inequalities supply the real bound. There are 576 bounded-nuisance source controls and two controls with large f4 in addition to the four degeneration controls. Eight tests, scoped SCC and fresh headless receipt accompany the packet. These are implementation controls; the documented stability arguments are not proof-assistant formalizations or independent physical evidence.

Next derive an explicit **two-data cut uncertainty modulus on a conditional finite source box**, using all lower degree-five coordinates rather than this boundary-only surrogate. Alternatively produce a sharp bounded-source obstruction to a proposed modulus. A source box is an assumption requiring separate native/UV licensing before physical use. All eighteen finite local matching coefficients remain free, C1–C12 and C12's exhausted budget remain unchanged, and physical preparation/matching/native/UV gates remain unearned. See [frontier v3](photon-eft-frontier-v3.md).

```text
python -S research/nima/checkers/check_photon_joint_transport_stability_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_joint_transport_stability_v1.py
```

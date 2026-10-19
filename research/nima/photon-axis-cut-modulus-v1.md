# Sharp half-power cut recovery on an exact leading-axis face

## Result and scope

[Contract](contracts/photon-axis-cut-modulus-v1.json) · [checker](checkers/check_photon_axis_cut_modulus_v1.py) · [tests](checkers/test_photon_axis_cut_modulus_v1.py) · [receipt](results/photon-axis-cut-modulus-v1.json).

On the **explicitly restricted face f2=0**, the conditional finite-box cut-reconstruction exponent improves from one-third to a sharp one-half. The theorem retains arbitrary h3 and all three quartic contacts, includes zero leading/cubic pairs, and does not require a leading-coupling lower bound. A bounded half-power obstruction also has a uniformly positive normalized factorization-discriminant margin.

This is a scoped answer, not the general margin-only theorem: fixing f2=0 is an additional exact structural assumption beyond source bounds or branch separation. Small or noisy f2 data cannot be projected to this face by convention. The imported real parity-even eight-contact photon model, retained quadratic two-photon order and normalized joint13/cut13 max norms are unchanged. No physical axis prior, box, noise model, matching, native dynamics or UV completion is licensed. All eighteen finite local matching directions remain free.

## 1. Explicit all-gap estimate

For sources X,Y with f2_X=f2_Y=0 and all eight contacts bounded in absolute value by M>=1, put delta=||D(X)-D(Y)|| in the established thirteen joint lower-cut/transport coordinates. Then

    ||C(X)-C(Y)|| <= omega_axis_M(delta),
    omega_axis_M(delta)=min((2713/3360)*M^2,
                            (35/3)*delta+(37/700)*M*sqrt(delta)).

At delta=0 this is zero by exact joint-data reconstruction. For 0<=delta<=1 it gives the uniform Holder-1/2 estimate

    cut gap <=[35/3+(37/700)*M]*sqrt(delta).

Rational square-root enclosures are computed at relative dyadic precision with no floating-point fit or fixed floor at zero. The constants are conservative; only the power exponent is claimed sharp on this face.

## 2. A transport-measured cubic radius

Write the six common-log coefficients as B=(G,Gp,Gpp,F,Fp,Hb). The linear combination

    I=Gp+2*Gpp+4*F-Fp/3

has, on f2=0, the exact source identity

    I=g3^2/224+f3^2/960.

All g2-by-quartic terms and the h3 square cancel. Thus h3 need not be deleted to obtain this radius. The coefficientwise identity on the full eight-contact model is

    I=g3^2/224+f3^2/960+f2*g4prime/240+f2*f4/35,

showing exactly why f2=0 cannot be replaced silently by a near-axis approximation. The transport-to-I gain in the max norm is 22/3.

Let w=1/224+1/960=37/6720. The weighted cubic vector z=(g3/sqrt(224),f3/sqrt(960)) has squared norm I, bounded by w*M^2. Its lower degree-five measured vector on this face is

    T=(g2*g3/sqrt(224),g2*f3/sqrt(960))=g2*z.

A pair of such vectors has measured gap at most sqrt(w)*delta.

## 3. Near/away proof, including the zero strata

Let r=max(|g2_X|,|g2_Y|). A simultaneous sign reversal of one entire source, which leaves all data/cuts unchanged, can make its nonzero leading coefficient positive for this proof; no physical Born sign is selected.

### Away from zero leading pair

If r>=2*sqrt(delta), the other leading magnitude is at least r/2: the measured g2^2 gap is at most delta<=r^2/4. For nonzero weighted cubic vectors, write z_i=sqrt(I_i)*e_i with unit direction e_i. Elementary normalization gives

    ||e_X-e_Y|| <=2*||T_X-T_Y||/max(||T_X||,||T_Y||).

The squared first-component difference consequently obeys

    |(z_X)_1^2-(z_Y)_1^2|
      <=|I_X-I_Y|+2*min(I_X,I_Y)*||e_X-e_Y||
      <=(22/3)*delta+(8*w)*M*delta/r.

When a cubic vector is zero, the angular term is zero and the same bound follows from the radius difference. Thus no cubic-radius lower bound is imposed. Since (z_i)_1^2=g3_i^2/224, the exact augmented response inverse and its fixed-M3 cut gain 13/3 yield

    cut gap <=(35/3)*delta+(37/840)*M*delta/r
             <=(35/3)*delta+(37/1680)*M*sqrt(delta).

Every other response component, including single-minus/h3 contributions, is retained in the measured transport term.

### Near zero leading pair

If r<=2*sqrt(delta), use the universal missing-coordinate bias from the preceding packets. On this face,

    b=-g2*g4/1680+g2*g4prime/7200,
    |b| <=(37/50400)*M*|g2|.

The two biases, the cut-line norm eighteen and the surrogate gain 13/3 give

    cut gap <=(13/3)*delta+(37/1400)*M*r
             <=(13/3)*delta+(37/700)*M*sqrt(delta).

This also covers r=0, arbitrary pure-h3 contacts and pure quartic sources. Combining the regimes proves the stated all-gap bound; the source-box diameter supplies the cap. The argument is documented real geometry and exact coefficient identities, not proof-assistant formalization.

## 4. Sharpness with an explicit positive branch-separation margin

The bounded pair X_r,Y_r in the [earlier box-modulus packet](photon-box-cut-modulus-v1.md) lies on f2=0 with equal nonzero degree-six transport. It has data gap/r^2->840/1369 and cut gap/r->161/202612, excluding every uniform exponent above one-half. Its unit-box bounds were certified for the whole parameter interval, not inferred from isolated small r values.

It also satisfies a positive normalized discriminant margin on both sources:

    |g2*f3-10*f2*g3| /
      [sqrt(g2^2+f2^2)*sqrt(g3^2+f3^2)]
      =|f3|/sqrt(g3^2+f3^2) >=23/37>1/2.

Indeed that family has q<=-23/37 and p^2+q^2<=1 for its parameter range. Thus the half-power theorem remains sharp even in the axis sub-sector with margin at least 1/2. This does not prove the half-power upper bound for general non-axis sources with the same positive margin; that broader question remains open.

For the axis-sector definition, zero leading or zero cubic pairs are included separately and no undefined normalized ratio is assigned to them. The upper estimate covers all such points. The positive-margin obstruction uses only nonzero pairs, so its margin is well-defined.

## 5. Controls and next question

There are 2187 exact radius-identity controls, 71 two-data face controls, three scaled nonzero-h3/unknown-quartic controls, and four bounded positive-margin sharpness pairs. Eight tests, scoped SCC and a fresh headless receipt accompany the algebraic certificates. A source with f2=10^(-12) is explicitly rejected by the face checker. These are implementation controls, not physical evidence or a native model-selection rule.

For a nonempty set of compatible sources on this exact face and box within a deterministic data tolerance epsilon, the cut diameter is at most omega_axis_M(2*epsilon). This is neither a probability guarantee nor permission to impose an exact axis prior on noisy data. Source-box, noise and face licensing remain independent unearned gates.

Next remove the exact leading-axis assumption and test a normalized discriminant margin alone on a fully stated source sector. Give a quantitative uniform rate or a bounded actual-source obstruction, with zero-stratum conventions and without choosing a physical factorization branch. The full-box one-third exponent remains sharp outside restricted sectors. C1–C12, C12's exhausted budget and the high-energy pause are unchanged. See [frontier v4](photon-eft-frontier-v4.md).

```text
python -S research/nima/checkers/check_photon_axis_cut_modulus_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_axis_cut_modulus_v1.py
```

# Joint photon-cut source fibres through degree six: nonzero leading pair

## Question and result

Once the complete degree-six cut is included, what remains ambiguous on the nonzero-leading stratum when all three quartic Born contacts remain unknown?

[Contract](contracts/photon-joint-degree6-fibres-v1.json) · [checker](checkers/check_photon_joint_degree6_fibres_v1.py) · [tests](checkers/test_photon_joint_degree6_fibres_v1.py) · [receipt](results/photon-joint-degree6-fibres-v1.json).

**Complete scoped classification:** all three quartic contacts are uniquely reconstructed on an oriented leading chart. Actual source fibres have two members related by the common Born sign, except on double cancellation with nonzero h3, where an additional independent relative h3 sign gives four members. At h3=0 those relative-sign branches merge. The previous continuous h3 ambiguity has become at most a discrete ambiguity, not an unconditional physical inverse.

The domain is real imported parity-even leading photon contacts with (g2,f2) nonzero and exact full coherent angular cut data. No source, physical sign, measured matching value or UV condition is selected. The zero-leading stratum is expressly outside this theorem.

## 1. Leading charts and complete degree-six data

Use the [degree-four/five image and fibre charts](photon-joint-cut-fibres-v1.md). They fix an oriented leading lift and g3,f3; h3 is either fixed or remains free on 6*g2+f2=0. They retain the two actual common-sign partners, not a physical sign convention.

For rational data the implementation writes every source as sqrt(d) times coefficients on that chart and divides the degree-six quadratic data by d. This exact encoding does not force sources to be rational. Write the normalized first five coefficients as (g,f,p,q,h), and unknown quartic contacts as (K,L,M)=(g4,g4prime,f4).

The [complete degree-six cut](photon-general-degree6-cut-v1.md) is the degree-three square plus 2-by-4 interference. Subtract the known degree-three-square contribution where h is already fixed. The remaining nuisance map is linear in (K,L,M). Its coefficients in the angular bases P0,P2 and d22^2 are

    D0 = g*K/16+g*L/96+7*f*M/24,
    D2 = f*M/210,
    O0 = 7*g*M/40+5*f*K/48+5*f*L/288,
    O2 = -f*L/1440,
    mixed2 = g*K/56-g*L/240.

These are coefficient identities, not forward values alone. If f!=0, D2 fixes M, O2 fixes L and O0 fixes K. If f=0,g!=0, O0 fixes M and (D0,mixed2) fix (K,L); that two-by-two determinant is -g^2/2240. Thus the nuisance map has rank three everywhere on the declared nonzero-leading stratum. All remaining polynomial rows must also match; fitting only three rows is insufficient for image membership.

Consequently, away from 6*g2+f2=0 the previous leading chart fixes h3 and the full degree-six data uniquely fix all three quartic contacts. The actual fibre has exactly two common-sign partners.

## 2. Leading cancellation: reconstruct the square before deciding its sign

On the leading cancellation chart, normalized g=1,f=-6 and the previous data leave h free. Subtract the degree-three square with h=0. The diagonal/helicity-preserving residual is the nuisance map plus t times the h3-square response, where t=h^2. The latter has coefficients D2=O2=mixed2=1/480 and no P0 component. This four-column augmented map has rank four.

One explicit elimination is

    M = -(40/693)*(O0+10*D0),
    t = 480*(D2+M/35),
    L = 240*O2-t/2,
    K = 56*(mixed2+L/240-t/480).

Check every remaining response row and require t>=0; a negative square is not a real source. Therefore unknown quartic contacts do not silently absorb the h3 square on this stratum.

Set S=10*p+q. The independent single-minus degree-six response is

    H(alpha)=-h*S*alpha*(1-alpha)/960.

- If S!=0, H fixes h with sign; require h^2=t. The fibre again has two common-sign members.
- If S=0, H must vanish. For t>0, both h=+sqrt(t) and h=-sqrt(t) survive, independently of the common Born sign: four actual source members, or two after the common-sign quotient.
- If S=0,t=0, the relative-sign branches coincide at h=0: two actual common-sign members.

All three quartic contacts remain fixed in each of these cases, since they depend only on t and the diagonal data. The exact algebraic t=2 control ensures that an irrational h is not rejected merely because the recorded cut data are rational.

These conditions plus the earlier degree-four/five image conditions and full response consistency are necessary and sufficient on realizable data in this domain. The implementation uses an exact overdetermined solve rather than numerical fitting; the algebra above proves the required ranks and exhausts all real sources. Executable tests are not a proof-assistant formalization of that real theorem.

## 3. Exceptional signs and conditioning remain physical-inference boundaries

The previous explicit pair with leading (1,-6), cubic (2,-20,+/-1), and quartic (1,-2,3) lies on the four-member case. Its two h3 signs are not global-sign partners. The equality includes the complete 2-by-4 interference, not an isolated square with nuisance parameters set to zero.

An exact inverse is not uniformly stable near double cancellation. Keep leading (1,-6), cubic diagonal coefficients p=1,q=-10+epsilon, quartic (1,-2,3), and compare h=+1 with h=-1. Their earlier cut data agree; their full degree-six coefficient separation in the fixed polynomial-coordinate max norm is |epsilon|/480, while h separation is two. The necessary inverse amplification is at least 960/|epsilon|. Exact epsilon=1/10,1/100,1/1000 controls retain this obstruction. The square-root branch at t=0 also cannot be treated as a globally regular signed inverse.

## Verification and next stratum

Controls retain 354 exact sources spanning ordinary, resolved leading-cancellation and double-cancellation cases; include g2=0 charts; verify quartet nuisance rank three; retain irrational square roots; reject incompatible higher mixed-wave data and negative h squares; and test the relative-sign conditioning sequence. All source couplings are photon EFT coefficients, not the earlier independent Dirac-current g3.

The **zero-leading** stratum remains unclassified here. It is not invalid data; it is a different inverse problem. There, degree-six data see the degree-three Born square and no quartic Born contact at all. Classify those fibres separately before extending an inverse across the rank change. Regular degree-six tensor/log/window completion, actual preparation/matching and native/UV inputs remain unearned. C1–C12 and C12's exhausted budget are unchanged.

```text
python -S research/nima/checkers/check_photon_joint_degree6_fibres_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_joint_degree6_fibres_v1.py
```

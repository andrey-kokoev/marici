# Zero-leading photon-cut source fibres through degree six

## Question and result

What does the joint cut data identify when g2=f2=0, where the nonzero-leading inverse is not defined?

[Contract](contracts/photon-zero-leading-fibres-v1.json) · [checker](checkers/check_photon_zero_leading_fibres_v1.py) · [tests](checkers/test_photon_zero_leading_fibres_v1.py) · [receipt](results/photon-zero-leading-fibres-v1.json).

**Complete scoped classification:** degree-six data identify the cubic Born triple up to common sign and a possible additional relative h3 sign. Every allowed cubic triple is accompanied by an entirely free quartic R3. If the cubic triple vanishes, the whole fibre is the quartic R3, with antipodal common-sign action and a fixed origin. The zero-leading case is not an extrapolation of an inverse that reconstructs quartic contacts.

This is a theorem in the imported real parity-even on-shell contact model and fixed coherent amplitude frames. It selects no physical sign, values, preparation, UV hypothesis or native dynamics. Rational/algebraic executable controls supplement the documented real-algebra proof, not a proof-assistant formalization.

## 1. Reduced data and necessary/sufficient image conditions

Degree-four/five data force the leading pair to vanish and are themselves zero. In the [complete degree-six cut](photon-general-degree6-cut-v1.md), all 2-by-4 terms then vanish regardless of the unknown quartic contacts. The remaining degree-three square determines calibrated coordinates

    Z(p,q,h)=(a,b,c,d,t)=(p^2,q^2,p*q,h^2,h*(10*p+q)),
    (p,q,h)=(g3,f3,h3).

This calibration is checked against the independently projected physical Bose matrices. In angular variable alpha=(1-z)/2, if D,O,M,H denote the cut polynomials, one extraction is

    a=-672*[alpha^3]M,
    d=80*[alpha^2]O,
    b=960*[alpha^2]D-12*d,
    c=96*(O(0)-d/480),
    t=-960*[alpha]H.

The remaining polynomial rows must also match the cubic-square image; five fitted coefficients are not an unrestricted new cut ansatz.

The complete real invariant conditions are

    a>=0, b>=0, d>=0, a*b=c^2,
    Delta=100*a+20*c+b,
    t^2=d*Delta.

Delta is nonnegative on the leading Gram locus: it equals (10*p+q)^2. Together with full polynomial consistency these conditions are necessary and sufficient. They are reality/factorization conditions on the data, not unearned UV bounds on EFT couplings or a declaration that every positive cut is a realizable source.

## 2. Cubic fibres and all quartic freedom

If a+b>0, the Gram pair (p,q) has two lifts differing by sign. On a>0 choose the mathematical p-positive chart

    p=sqrt(a), q=c/sqrt(a).

If a=0,b>0 use q=sqrt(b),p=0. This fixes an orientation only, not a physical Born sign.

- For Delta>0, h=t/(10*p+q) is fixed on that chart. Its square is d by the image condition. The actual cubic fibre contains two common-sign triples.
- For Delta=0, nonzero pair implies q=-10*p and t=0. If d>0, both h=+sqrt(d) and h=-sqrt(d) survive independently of the pair's sign: four cubic triples. If d=0, the relative-sign branches merge and there are two triples.
- If a=b=0,d>0, the only cubic triples are (0,0,+sqrt(d)) and (0,0,-sqrt(d)); t=0. A positive-h chart is just another mathematical orientation.
- If a=b=d=0, the cubic triple is exactly zero and all invariant data vanish.

Every cubic triple above is accompanied by arbitrary (g4,g4prime,f4) in R3. These contacts are **not identified** by these cut orders: neither the degree-three square nor vanished 2-by-4 interference contains them.

Consequently the actual eight-source fibre is two or four disjoint copies of R3 when the cubic source is nonzero. Common sign reversal exchanges components and negates the quartic triple, leaving one or two copies of R3 after the sign quotient. When the cubic triple is zero, there is only one R3 component; the sign acts antipodally within it, with the origin fixed. Calling that case a free two-sheet cover would lose its actual type.

These charts exhaust all real sources: the Gram determines the pair's two lifts, the square and linear relation determine precisely the h choices, and the cut is independent of the remaining three inputs. The separate [nonzero-leading result](photon-joint-degree6-fibres-v1.md) reconstructs the quartic contacts only on its different rank stratum.

## 3. Exact algebraic controls and same-data witnesses

The implementation retains sqrt(root_square) charts and, on pair cancellation, a separate h coefficient square. It does not discard rational cut data with irrational source lifts. Controls include a=7,b=28,c=14,d=63,t=252, and cancellation data a=7,b=700,c=-70,d=2,t=0, whose normalized h square is 2/7. These are exact, not floating-point fits.

There are 1048 exact source controls across ordinary pair, cancellation, pure-h and zero-cubic strata, with all quartic triples varied and shifted independently. Full angular-shape, Gram, nonnegative-square and linear/square incompatibilities are rejected.

In particular the sources

    (0,0,0,0,0,1,2,3), (0,0,0,0,0,4,5,6)

have identical zero cuts through degree six but different Born tensors: their forward Phi1 degree-four coefficient differs by three. Therefore zero data do not establish zero interaction, and no regularization may silently choose the quartic source to be zero. This is an imported mathematical counterexample, not an assertion that arbitrary such couplings admit a UV completion.

## Disposition and next constructor

Together with the nonzero-leading charts, this closes the actual real source-fibre classification for the declared eight-leading-coupling joint cut map through degree six. It does not select any actual source or the remaining higher-order local matching. C1–C12 dispositions, exhausted C12 budget and high-energy pause are unchanged.

Next construct the regular local tensor jet through degree six before lifting its generic cut to logarithmic/window form. Retain the independent single-minus coefficient and every forward-invisible term. The lower-degree inverse results do not supply those higher matching coefficients; physical/native/UV gates remain separate and unearned.

```text
python -S research/nima/checkers/check_photon_zero_leading_fibres_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_zero_leading_fibres_v1.py
```

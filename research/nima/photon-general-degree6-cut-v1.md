# Complete degree-six quadratic photon cut

## Question and result

What is the full degree-six two-photon cut when independent leading degree-four contacts are retained, rather than inferring higher-source recovery from the degree-three square alone?

[Contract](contracts/photon-general-degree6-cut-v1.json) · [checker](checkers/check_photon_general_degree6_cut_v1.py) · [tests](checkers/test_photon_general_degree6_cut_v1.py) · [receipt](results/photon-general-degree6-cut-v1.json).

The complete scoped inventory is constructed for eight real leading photon Born couplings g2,f2,g3,f3,h3,g4,g4prime,f4. It contains six 2-by-4 monomials and six symmetric 3-by-3 monomials. Both archived R-family sectors match with the unchanged normalization dictionary. A higher cut sees h3 squared, but an explicit h3-sign ambiguity survives through degree six even with nonzero quartic nuisance inputs.

This is a conditional imported on-shell parity-even contact-EFT two-photon elastic cut. It is not all physical IR contributions, a selected matching polynomial or native/UV dynamics.

## 1. Project the whole Born jet before squaring

The existing covariant local basis supplies all eight leading Born unit tensors. At s=1, alpha=(1-z)/2, the checker extracts bounded-degree helicity polynomials from five exact angle evaluations and checks a sixth unused angle. All physical scalar and mixed Bose waves are projected through J=4 and reconstructed as exact polynomials.

Besides the lower waves, use

    P4(1-2alpha)=1-20alpha+90alpha^2-140alpha^3+70alpha^4,
    d^4_22=(1-alpha)^2*(1-14alpha+28alpha^2).

The physical positive-parity block remains [[Phi1+Phi2,2Phi5],[2Phi5,2Phi3]], with off-diagonal sqrt(6)*b stored exactly. Single-minus Born h3 has only its previously normalized J=2 transition. Leading quartic Born Phi5 vanishes in the regular degree-four ansatz; that is not a rule setting h3 or higher matching coefficients to zero.

The unit f4 Born J=4 plus wave is 1/2520; the unit g4 mixed J=4 wave is 1/2016. Both are nonzero, even though degree-two/three waves have no J=4 component and thus these higher waves contribute zero to this cut coefficient. They are retained in the source, not deleted from the model.

## 2. Extract the complete homogeneous cut

For pi-stripped physical Born matrices F2,F3,F4, quadratic unitarity gives

    pi^2*Im F_loop,6 = (F2*F4+F4*F2+F3*F3)/2

when the Fd symbols on the right denote their pi-stripped coefficients. Both interference orderings and the half factor for a diagonal square are required. The checker reconstructs all independent helicity responses pi*Im(Phi1,Phi2,Phi3,Phi5)/s^6, with Phi4 supplied by the Bose-reflected mixed response.

Keep the twelve monomials

    g2*g4, g2*g4prime, g2*f4, f2*g4, f2*g4prime, f2*f4;
    g3^2, g3*f3, g3*h3, f3^2, f3*h3, h3^2.

Every response polynomial is recorded in the receipt. Their coefficient map has rank seven on the twelve monomial bookkeeping coordinates; these products arise from eight source couplings, not twelve freely selectable physical inputs. All source directions remain retained. The inventory is independently checked against coefficient extraction after squaring the complete graded Born-wave matrix, on all 256 signed unit-coupling choices and eight coordinate sources. A positive complete-wave square does not imply that its degree-six coefficient is PSD: signed 2-by-4 interference may be negative.

The R-family restrictions are checked only after constructing the general inventory:

- r1 squared: g3=r1/4,f3=-3*r1/4,h3=0;
- r0*r2: g2=r0/4,f2=-r0/4,g4=r2/4,g4prime=0,f4=-r2/8.

After stripping the relevant common strength/monomial, both agree exactly with the [archived degree-six sectors](../scattering/low-energy/DEGREE6-PHOTON-IR-LOGS.md) divided by 16. The f4 coefficient follows from s^4+t^4+u^4=S2^2/2, not a new fit. Leading quartic source coefficients are independent inputs here, not a particular loop-subtraction shift.

## 3. h3 effects and what the higher cut does not identify

The h3 square contributes

    pi*Im Phi1 / (h3^2*s^6)=P2(z)/480,
    pi*Im Phi2 / (h3^2*s^6)=P2(z)/480,
    pi*Im Phi3 / (h3^2*s^6)=x^2/480,    x=(1+z)/2.

Its physical block is positive; angular coefficients need not be pointwise positive. The single-minus degree-six section is

    pi*Im Phi5 = -h3*(10*g3+f3)*s^4*t*u/960.

There is no 2-by-4 contribution to this section because neither degree-two nor degree-four leading Born tensor has a single-minus transition. This does not predict finite analytic single-minus matching or higher-loop terms.

At leading g2=1,f2=-6, the three quartic nuisance-response columns have rank three; adding the h3-square response raises the rank to four. Thus the square is not erased by those three fixed-leading nuisance directions. This is a scoped linear witness, not a complete source-fibre classification.

Crucially, take the eight-source pair

    (1,-6,2,-20,+1,1,-2,3),
    (1,-6,2,-20,-1,1,-2,3).

Their joint degree-four/five data agree because 6*g2+f2=0. Their entire degree-six cuts also agree because 10*g3+f3=0 and h3 enters the remaining terms only through its square. The quartic nuisance inputs are nonzero and equal, not silently fixed away. These sources are not global sign partners and their Born Phi5 difference is 288/625 at the retained exact angle. Higher cut order therefore does **not** remove every h3 ambiguity.

## Boundary and next test

Algebraic/partial-wave derivations are documented and exact polynomial controls are executable; no proof-assistant formalization is claimed. All source directions and independent leading quartic contacts are retained. C1–C12 dispositions, exhausted C12 budget and the high-energy pause are unchanged. No physical coupling, source preparation, global spectral positivity or UV completion is selected.

Next extend the joint source-fibre analysis through degree six on the nonzero-leading stratum while retaining the unknown quartic contacts. Determine exactly when the extra h3-linear and h3-square data resolve the previous continuous fibre, and when the double-cancellation sign ambiguity remains. Do not use the twelve-monomial linear kernel as a substitute for actual coupling fibres, or drop nuisance inputs to claim an inverse. The separate regular degree-six tensor/log/window construction remains open.

```text
python -S research/nima/checkers/check_photon_general_degree6_cut_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_general_degree6_cut_v1.py
```

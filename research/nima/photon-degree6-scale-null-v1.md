# Actual real sources on the degree-six scale-null locus

## Question and result

Does the extra linear scale-null direction of the degree-six cut occur as a nonzero cut of an actual real eight-coupling Born source?

[Contract](contracts/photon-degree6-scale-null-v1.json) · [checker](checkers/check_photon_degree6_scale_null_v1.py) · [tests](checkers/test_photon_degree6_scale_null_v1.py) · [receipt](results/photon-degree6-scale-null-v1.json).

**Result: no.** On the declared real source domain, zero degree-six common-log transport is equivalent to zero degree-six cut. Their common source locus is exactly

    {(g,f,0,0,0,0,0,0)} union {(0,0,0,0,0,K,L,M)}.

These are a leading R2 and a quartic R3 meeting at the origin, not just the zero interaction. Nonzero cubic contacts necessarily leave at least one degree-six scale coefficient nonzero, even when all three quartic nuisance contacts are retained. This is an algebraic statement in the imported real parity-even quadratic two-photon model, not a UV bound, actual source selection or native-QFT result.

The theorem is about the **zero fibre only**. It does not prove that arbitrary equal nonzero transport data imply equal cuts; differences of two factorizable source vectors need not be factorizable source vectors.

## 1. Exact transport-null line before source factorization

Use [the generic log/window lift](photon-general-degree6-window-v1.md). In response coordinates

    R=(D0,D2,O0,O2,M2,M3,H),

where H=h3*(10*g3+f3)/960 is the logarithmic single-minus coefficient, the six transport equations have a one-dimensional kernel

    R=t*(-3,-3,0,0,5,1,0).

The checker verifies the six-by-seven matrix, its exact nullspace, and its composition with the independently projected twelve-monomial response matrix. For an actual source write

    (g,f,p,q,h,K,L,M)=(g2,f2,g3,f3,h3,g4,g4prime,f4).

Then t=M3=p^2/4032. Hence transport zero requires

    E0=D0+3*M3=0, E2=D2+3*M3=0,
    EM=M2-5*M3=0, O0=O2=H=0.

The cubic square and 2-by-4 interference are both present. Individual homogeneous cut coefficients are not assumed positive.

## 2. Real-domain certificate excluding a nonzero cubic triple

The projected coefficient rows give exact polynomial identities

    g*L - (355/224)*p^2 - (25/64)*q^2 - (259/48)*h^2
      =40*E0-140*EM-2450*E2,
    f*L-3*h^2=-1440*O2,
    h*(10*p+q)=960*H.

These identities are checked coefficientwise in all twelve source products before imposing any zero equation.

### h=0

If f=0, E2=0 reduces to p^2/1344+q^2/5760=0, forcing p=q=0 over the reals. If f!=0, O2=0 forces L=0. The first identity then becomes

    (355/224)*p^2+(25/64)*q^2=0,

again forcing p=q=0. No sign assumption on g or f is used.

### h!=0

H=0 forces q=-10*p. O2=0 gives f*L=3*h^2, so f is nonzero. Put u=p^2/h^2>=0 and a=g/f. The first identity forces

    a=259/144+(3035/224)*u>0.

The remaining null equations imply

    g*K/h^2=-(5/12)*u+(7/10)*a-7/60,
    f*M/h^2=-(365/96)*u-7/16.

Use source factorization to substitute g*M/h^2=a*(f*M/h^2) and f*K/h^2=(g*K/h^2)/a into O0. Then

    a*O0/h^2 = a/8-49*a^2/640-7/576
                -u*(511*a^2/768+25/576+5*a/48).

Inserting the positive affine expression for a gives a cubic polynomial in u with coefficients

    (-464569/13271040,
     -492857215/111476736,
     -1186505935/24772608,
     -672419425/5505024).

Every coefficient is strictly negative. Therefore this polynomial is negative for every u>=0, contradicting O0=0. The checker derives it independently from the actual O0 response row, verifies the earlier residual equations after substitution, and checks the displayed polynomial identity exactly. This excludes the whole h!=0 branch, not just a sampled range or rational points. General real-algebra reasoning is documented here; it is not a proof-assistant formalization.

## 3. Remaining quartic contacts and complete null locus

Thus p=q=h=0. The transport-null line then has t=0, so the entire degree-six cut vanishes.

For a nonzero leading pair, the remaining quartic map is injective. If f!=0, D2=f*M/210, O2=-f*L/1440 and then O0=5*f*K/48 successively force M=L=K=0. If f=0,g!=0, O0 fixes M; the D0/M2 two-by-two determinant is -g^2/2240, fixing K=L=0. If g=f=0, every quartic triple remains entirely free. These are exactly the two source components stated above, and both plainly give zero transport and cut.

For example (1,2,0,0,0,0,0,0) and (0,0,0,0,0,1,2,3) each have zero **degree-six** transport and cut but nonzero forward Born Phi1 value one in the formal unit-energy control. The leading source can have lower-degree cuts; the pure quartic source can first contribute beyond this cut order. Neither is a declaration of a UV-realizable physical source or zero total running.

## Controls and next question

The coefficient identities and strict-negative polynomial certify the universal real statement. Additionally, 6561 exact source points in {-1,0,1}^8 check transport-zero, cut-zero and the complete locus equivalence; exactly 35 lie on the null locus. The inherited nonzero linear null-cut vector is retained as a bookkeeping control, not mislabeled an actual source. Eight unit tests, scoped SCC and a fresh headless receipt accompany the packet; these are implementation controls, not independent physical evidence.

Next test **nonzero equal transport fibres**: exhibit two actual real sources with equal degree-six transport but different cuts, or prove they cannot occur on a precisely stated domain. This is not settled by the zero-fibre theorem or a Jacobian nullspace alone. All finite matching, actual preparation, native dynamics and UV gates remain unearned. C1–C12 and C12's exhausted budget are unchanged. See [frontier v3](photon-eft-frontier-v3.md).

```text
python -S research/nima/checkers/check_photon_degree6_scale_null_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_degree6_scale_null_v1.py
```

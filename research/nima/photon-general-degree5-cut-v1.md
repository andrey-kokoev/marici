# General degree-two/degree-three photon Born interference

## Question and bounded result

What changes when the R-family ties are removed and photon EFT g2,f2,g3,f3,h3 are independent?

[Contract](contracts/photon-general-degree5-cut-v1.json) · [checker](checkers/check_photon_general_degree5_cut_v1.py) · [tests](checkers/test_photon_general_degree5_cut_v1.py) · [receipt](results/photon-general-degree5-cut-v1.json).

**Result:** the general quadratic degree-five two-photon elastic cut in the declared real parity-even contact stratum has six bilinear source coordinates but only four independent cut responses. A single-minus loop section is generally nonzero. The special R-family zero is therefore not a general absence theorem. All source directions are retained; a rank-four readout does not license identifying the couplings or choosing physical values.

## 1. Fix the physical matrix before projection

The frozen [primary excerpt](sources/photon-scattering-2024-excerpts.tex), original lines 419-471, explicitly gives the physical positive-parity even-J block

    F_J = [[Phi1_J+Phi2_J, 2*Phi5_J],
           [2*Phi5_J,      2*Phi3_J]],

with S=I+iF, plus the separate negative-parity scalar Phi1_J-Phi2_J and odd-J mixed scalar 2*Phi3_J. The checker verifies those source anchors. No normalization is fitted to the restricted family.

Start from the covariant local tensors, one unit coefficient at a time. At s=1 and alpha=(1-z)/2 the five Born helicity polynomials are recovered by unisolvent interpolation and checked at an unused fifth angle. Their degree bound is known from the explicit local jet. The scalar and mixed projections use the already checked Legendre/d22 conventions.

For the new transition, d^2_02=sqrt(6)*alpha*(1-alpha). The finite spin-two Wigner formula gives sqrt(96)/4=sqrt(6), with positive sign; its squared norm is 6*integral alpha^2*(1-alpha)^2=1/5. Since physical F02=2*Phi5,

    pi*F02_Born = sqrt(6)*integral alpha*(1-alpha)*Phi5 /8
                =sqrt(6)*h3/240.

Exact reconstruction of Phi5=h3*alpha*(1-alpha) exhausts this Born wave. Radicals are retained symbolically: a block [[a,sqrt(6)*b],[sqrt(6)*b,d]] is stored as the rational triple (a,b,d), not approximated numerically.

## 2. Complete finite Born waves and the matrix product

With pi factors stripped, the independent degree-two waves are

    J0: plus=g2/16+5*f2/48, minus=g2/16-5*f2/48;
    J2 positive block: a=f2/240, b=0, d=g2/40;
       negative scalar=-f2/240; J3 mixed=0.

The degree-three waves are

    J0: plus=g3/16+f3/96, minus=g3/16-f3/96;
    J2 positive block: a=-f3/480, b=h3/240, d=-g3/48;
       negative scalar=f3/480; J3 mixed=-g3/336.

These are obtained from the tensor projections. Exact polynomial reconstruction checks no Born wave was silently dropped. In particular the h3 off-diagonal block is not replaced by independent scalar probabilities.

For two real physical blocks A,B, the interference is (AB+BA)/2 from 2*Im F_loop=F_Born^dagger*F_Born. In rational block coordinates,

    diagonal00 = a_A*a_B+6*b_A*b_B,
    diagonal22 = d_A*d_B+6*b_A*b_B,
    offdiag/sqrt(6) = (a_A*b_B+b_A*d_B+a_B*b_A+b_B*d_A)/2.

Both orderings matter. In the degree-two/three product b_A=0, but b_B=h3/240 creates the single-minus response through the sum of the degree-two diagonal entries. It cannot be obtained by squaring only diagonal waves.

## 3. General right cut

Let x=(1+z)/2=1-alpha. In invariant amplitude units, the degree-five coefficients are

    pi*Im Phi1 = s^5*[g2*g3/16+f2*f3*(17-z^2)/960],
    pi*Im Phi2 = s^5*[g2*f3/96+5*f2*g3/48],
    pi*Im Phi3 = -s^5*g2*g3*x^2/48,
    pi*Im Phi4 = -s^5*g2*g3*(1-x)^2/48,
    pi*Im Phi5 = s^5*h3*(6*g2+f2)*alpha*(1-alpha)/480
                =h3*(6*g2+f2)*s^3*t*u/480.

All couplings here are amplitude-normalized photon EFT coefficients, not the earlier independent Dirac-current g3. No common strength or coupling monomial is double inserted. These formulas describe the leading quadratic four-photon-contact interference two-photon cut, not a complete physical IR inventory or all-orders amplitude.

Substituting g2=lambda*r0/4, f2=-lambda*r0/4, g3=lambda*r1/4, f3=-3*lambda*r1/4, h3=0 reproduces the independently checked R-family D/O/M polynomials exactly, with no rescaling. Its Phi5 vanishes because of the chosen leading h3=0, not because the channel is forbidden. Using Phi5 rather than 2*Phi5 in the physical matrix halves the induced response and fails the source convention.

## 4. Source/readout kernel and interference positivity

Keep bilinear source order

    (g2*g3,g2*f3,g2*h3,f2*g3,f2*f3,f2*h3).

Exact row reduction of all output polynomial coefficients gives rank four, with kernel

    (0,-10,0,1,0,0),
    (0,0,-1/6,0,0,1).

Only g2*f3+10*f2*g3 and 6*g2*h3+f2*h3 occur in their respective responses. These are kernel relations in the linear bookkeeping space of six monomials, not six independently selectable physical couplings: the monomials arise from an outer product of two and three source coefficients. Nothing is discarded from the Born source or identified as native merely because this readout is nonfaithful. For example f2=-6*g2 can cancel the single-minus interference with nonzero h3; this is an algebraic control, not selected matching or an admitted UV solution.

Interference can be indefinite. The f2-by-h3 J2 product has negative determinant in the physical block. Nevertheless the square of every real complete Born block is positive semidefinite: its determinant is (a*d-6*b^2)^2. The checker retains that identity and 243 exact complete-wave controls. This does not construct the degree-six cut inventory or make the isolated degree-five coefficient positive.

## Boundary and next constructor

The scoped general Born-interference inventory is complete; the six source monomials and their two-dimensional readout kernel remain retained. Algebraic/partial-wave arguments are documented, not machine-formalized proofs. The result supplies neither a generic crossed logarithmic/window tensor nor finite physical matching, native preparation or UV assumptions. Existing C1–C12 dispositions and C12's exhausted budget are unchanged.

Next lift these six-coordinate cuts into the twelve-generator regular degree-five log/window framework, including the induced Phi5 section. Verify all channel coefficients and the associated h5 scale direction, exact R-family restriction and two-variable generated remainder. Do not erase the kernel or infer zero single-minus running from the restricted family.

```text
python -S research/nima/checkers/check_photon_general_degree5_cut_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_general_degree5_cut_v1.py
```

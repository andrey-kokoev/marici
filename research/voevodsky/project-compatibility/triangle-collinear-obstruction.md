# Collinear collision obstruction to extending the regular-patch limit

## Scope

Freshly re-read the current transverse-density contract. Work in its candidate real reduced-family representative, with a,b>0 and the literal normalization. Take E=0 FIRST, then examine w=rho^2 down to0. This is an iterated-limit diagnosis, not the joint E,w asymptotic of the physical period.

The lengths are r=sqrt(x^2+w), s=sqrt((x-a)^2+w), t=sqrt((x+b)^2+w). Exclude x=-b,0,a, where this Taylor chart fails. The remaining source rational factor A0 is exactly the six-term expression documented in `triangle-transverse-density.md`.

## Vanishing denominators and leading coefficients

For a nonzero real u, sqrt(u^2+w)=|u|+w/(2|u|)+O(w^2). Applying this to every source denominator yields:

| x interval | Vanishing denominators | A0 leading term |
| --- | --- | --- |
| x<-b | none | finite positive |
| -b<x<0 | q3, q31 | (b+x)/(b(a+b)) * w^(-2) |
| 0<x<a | q3, q23 | (a-x)/(a(a+b)) * w^(-2) |
| x>a | none | finite positive |

Here q3=s+t-a-b, q23=r+s-a, q31=r+t-b. The cut-edge denominators r,s,t are nonzero on these open intervals.

Proof on0<x<a: r=x, s=a-x, t=x+b at w0. Then q1=2a, q2=2t, q3=w(a+b)/(2st)+O(w^2), and q23=wa/(2rs)+O(w^2). The leading bracket in A0 is

    (1/r+1/s)/q23 = 2/w + O(1).

Dividing by q1*q2*q3 gives s/[a(a+b)] * w^(-2). All other terms are lower order and all terms are positive, so cancellation cannot remove the leading term.

On-b<x<0 instead q1=2s, q2=2b, q31=wb/(2rt)+O(w^2), and the leading bracket is (1/r+1/t)/q31=2/w+O(1). This gives t/[b(a+b)] * w^(-2). Outside[-b,a] the strict nonzero denominator values give order0. These expansions are uniform on compact subintervals excluding the three endpoints.

## The actual local integrability gate

The coordinate map R=x^2+w, S=(x-a)^2+w has Jacobian determinant2a. Thus dR dS=2a dx dw and F=4a^2w. The limiting density from the regular-patch calculation is therefore proportional to

    w^epsilon A0(x,w) dx dw.

On either interior interval it has a nonzero leading coefficient times w^(epsilon-2). At fixed generic regulator and a nonzero local normalization, its absolute integral near w0 exists precisely when Re(epsilon)>1. In particular it is not absolutely integrable near epsilon0.

The earlier Re(epsilon)>-1/2 bound only controlled the transverse z endpoints on a compact F>0 patch. It cannot justify extending that limit through F=0. This is a concrete source-denominator obstruction, not just the absence of a supplied theorem.

The normalization C(d) may itself vanish or become singular at exceptional regulator values. No conclusion here substitutes epsilon=0 before integration, removes the regulator, or rules out analytically regularized boundary objects. Absolute integrability failure is not nonexistence of a regularized period.

## What remains open

The calculation does NOT establish that the finite-E period diverges, identify its E residue, or justify exchanging E→0 with w integration. The transition region w comparable to E may alter the result. The joint neighborhoods of x=-b,0,a and all unbounded ends remain untreated. The intended physical continuation and normalization are still awaiting owner evidence.

Next local task: derive the joint E,w scaling on a compact interior x interval, retaining z and the actual denominators. It must bridge the w much larger than E overlap with this w^(-2) result, rather than integrating the limiting singular density without control.

## Verification

`python research/voevodsky/project-compatibility/check_triangle_collinear.py` passes54 exact Fraction leading-jet fixtures spanning both interior intervals and both exterior intervals for multiple a,b values. `triangle-collinear.json` records fixtures and stable source hashes. These are arithmetic checks; the general interval proof is the Taylor/positivity calculation above, not exhaustive machine verification or a formalized analytic theorem.

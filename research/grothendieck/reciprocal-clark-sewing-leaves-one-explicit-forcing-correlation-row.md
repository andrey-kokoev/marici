# Reciprocal Clark sewing leaves one explicit forcing-correlation row

## Computation

Applying the recorded Clark codiagonal to the actual smooth zeroth/first-moment source ports gives an exact polarized identity. The first-moment forcing contributions cancel. The remaining forcing row is a single correlation of Phi with the difference of the two reciprocal first-moment tails.

This calculation uses the existing local mixed Green identity on its actual source vectors. No derivative-delta incidence is inserted.

## 1. Tail conventions

Let Phi be the real source forcing on [0,infinity), and put f_0(x)=Phi(x), f_1(x)=x Phi(x). For sigma in {+1,-1}, define

G_(sigma,j)(z;x)=integral_x^infinity exp(sigma i z(t-x)) f_j(t) dt.

Then (partial_x+sigma i z)G_(sigma,j)=-f_j. Assume the source decay needed for these tails, their L2 pairings and their endpoint values on the spectral region considered. Completed theta decay supplies the intended source setting; all exchanges below can also first be made on finite integrations and passed under corresponding integrable bounds.

Write h_(sigma,j)(z)=G_(sigma,j)(z;0). The recorded oriented resolvent entries are M_(sigma,j)=sigma i h_(sigma,j). Use the order (+,0),(-,0),(+,1),(-,1).

The fixed Clark matrix S maps M to (E,E_star). Set

N(w,z)=conjugate(E(w))E(z)-conjugate(E_star(w))E_star(z).

## 2. Exact coefficient matrix

With J=diag(1,-1) and D=diag(i,-i,i,-i),

N(w,z)=h(w)* C h(z),

C=D* S* J S D
 = (1/2) [[0,0,-1,1], [0,0,-1,1], [-1,-1,0,0], [1,1,0,0]].

The corresponding matrix S* J S has inertia (one positive, one negative, two zero). These signs specify the sewn form before any source restriction.

Let a,b run over the four channels; write sigma_a and j_a for their signs and moments. Define the actual cross-tail Gram entries

T_ab(w,z)=<G_a(w),G_b(z)>,

with inner product conjugate-linear in the first slot.

## 3. Applying the local Green identity

Integration by parts in each nonzero matrix entry gives

conjugate(h_a(w))h_b(z)
 = i(sigma_b z-sigma_a conjugate(w)) T_ab(w,z)
   +<f_(j_a),G_b(z)>+<G_a(w),f_(j_b)>.

Consequently

N(w,z)=B(w,z)+R(w,z),

B(w,z)=sum_ab C_ab i(sigma_b z-sigma_a conjugate(w)) T_ab(w,z).

This includes both same-orientation and cross-orientation tail pairings. Replacing it by two independent positive diagonal Grams would discard entries of the actual attachment.

## 4. The surviving source row

The two rows of C associated with f_1 sum to zero. The two associated with f_0 sum to (0,0,-1,1). Thus

R(w,z)=<Phi,G_(-,1)(z)-G_(+,1)(z)>
       +<G_(-,1)(w)-G_(+,1)(w),Phi>.

All first-moment forcing terms have canceled in the sewn identity. This formula is the exact remaining mixed source term.

It has a one-variable correlation representation. Define

A(d)=integral_0^infinity (x+d) Phi(x)Phi(x+d) dx, d>=0.

Changing variables t=x+d yields

R(w,z)=2i integral_0^infinity A(d)
       [sin(conjugate(w)d)-sin(zd)] dd.

Thus the arithmetic source enters through a specified weighted theta autocorrelation. Any comparison with the existing arithmetic Green current must account for this row together with B.

## 5. Divided-difference form and diagonal limits

With the declared kernel normalization K=N/[-i(z-conjugate(w))],

K(w,z)=B(w,z)/[-i(z-conjugate(w))]
 +2 integral_0^infinity A(d)
   [sin(zd)-sin(conjugate(w)d)]/[z-conjugate(w)] dd.

Normalization factors such as 2 pi can be restored when comparing with a particular de Branges convention; the convention above fixes every sign in this packet.

For real z=w=x, R(x,x)=0. Its divided-difference contribution nevertheless has the finite limit

K_R(x,x)=2 integral_0^infinity d A(d) cos(xd) dd.

This limit matters: real-axis cancellation of the numerator does not remove the boundary kernel contribution.

For z=w=iy, y>0,

R(iy,iy)=4 integral_0^infinity A(d)sinh(yd)dd.

If Phi is nonnegative and nonzero on an interval, this is strictly positive. At general complex pairs the row is nonzero and requires the complete polarized calculation. No positive-kernel theorem for this row alone is asserted.

## 6. Relation to the actual closure problem

The source forcing, reciprocal tails, endpoint maps, and fixed Clark interconnection now give a complete scalar polarized attachment identity on their admitted domain. The surviving mixed term is explicitly R, and the bulk contribution is the displayed cross-tail sum B.

The next equality to test against the independent arithmetic Green realization is therefore its pullback against B+R on the same source. A proof of positivity would concern the resulting full divided-difference kernel. The local conservative charts already provide the entries used here; their reciprocal sum retains the cross terms and weighted autocorrelation just computed.

This calculation advances the shared attachment comparison to an actual source formula. It leaves the independent prime-resolved pullback and its positive-domain comparison open.

## Verification

`uv run --with sympy --with mpmath python research/grothendieck/checkers/check_clark_polarized_forcing_sewing.py`

Passed:
- exact rational/complex calculation of C and the signed inertia;
- exact cancellation of the f_1 forcing rows;
- all nonzero local mixed Green entries for a Gaussian smooth source;
- the full sewn identity and its reduced forcing row;
- a nonzero off-real reservoir value and zero real diagonal numerator.

Numerical regressions use 40-digit arithmetic and a Gaussian source; they do not constitute numerical tests of completed-zeta positivity. The identities above apply analytically to the admitted real theta source under the stated convergence hypotheses.

Sources:
- `research/nima/one-sided-mixed-green-block-is-closed-by-the-forcing-reservoir.md`
- `research/voevodsky/the-completed-clark-pair-is-a-fixed-codiagonal-sewing-of-four-oriented-resolvent-cross-entries.md`
- `research/voevodsky/the-full-line-translation-resolvent-realizes-the-one-sided-theta-transform-as-an-exact-source-to-endpoint-cross-entry.md`

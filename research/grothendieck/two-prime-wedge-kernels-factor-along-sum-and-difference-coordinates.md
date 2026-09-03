# Two-prime wedge kernels factor along sum and difference coordinates

## Setup

Let `A=log2`, `B=log3`, and put

`S=(A+B)/2`, `D=(B-A)/2`.

For spectral variables `u,v`, define the parity wedges

`W_+=cos(Su)cos(Dv)-cos(Sv)cos(Du)`,

`W_-=sin(Su)sin(Dv)-sin(Sv)sin(Du)`.

The completed Turan kernels are `Q_+=W_+^2` and `Q_-=W_-^2`.

## Prime-coordinate factorization

Set

`P(u,v)=sin(A(u+v)/2) sin(B(u-v)/2)`,

`R(u,v)=sin(B(u+v)/2) sin(A(u-v)/2)`.

Trigonometric addition gives the exact identities

`W_+=-(P+R)`,

`W_-=-(P-R)`.

Therefore

`Q_+=(P+R)^2`,

`Q_-=(P-R)^2`,

and

`Q_++Q_-=2(P^2+R^2)`,

`Q_+-Q_-=4PR`.

## Interpretation

The two parity channels are the symmetric and antisymmetric combinations of two crossed prime-coordinate products:

- the `A` character on `u+v` paired with the `B` character on `u-v`;
- the same assignment with `A` and `B` exchanged.

This is an exact two-prime factorization of the wedge kernels. It is not edge-correlation composition and not route holonomy. The mixed quantity `PR` controls the difference between parity determinants, while `P^2+R^2` controls their sum.

## Consequence for the double Weil functional

Writing `L=mu_t tensor mu_t`,

`N_++N_-=4 L(P^2+R^2)`,

`N_+-N_-=8 L(PR)`.

Thus simultaneous rectangle positivity is equivalent to

`L(P^2+R^2)>=2 abs(L(PR))`.

The pointwise inequality `P^2+R^2>=2 abs(PR)` has exactly this form, but it cannot be integrated against the unresolved signed tensor Weil distribution. It nevertheless isolates the sole comparison that a source-side argument must preserve.

## Revised arithmetic target

Instead of deriving two unrelated Turan inequalities, seek a completed source estimate that proves tensor-Weil domination of the crossed term:

`2 abs(L(PR)) <= L(P^2+R^2)`.

This target retains both prime coordinates symmetrically and packages endpoint, gamma, prime, and mixed contributions before enclosure. A source proof still requires a positivity-preserving property of `L` on this restricted three-dimensional span; full positivity of the Weil distribution need not be assumed syntactically, though proving the restriction may remain equally difficult.

## Disposition

The first rectangle now has an exact non-tautological prime-coordinate factorization. The surviving question is whether the completed arithmetic source controls the crossed tensor pairing on the span of `P` and `R`.

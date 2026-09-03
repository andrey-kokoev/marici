# Completed Turan numerators are double-Weil wedge functionals

## Question

Can the cancellation in the mixed-prime parity determinants be performed algebraically before splitting the explicit formula into endpoint, archimedean, and prime sectors?

## Distributional formulation

Let `mu_t` denote the completed even Weil distribution weighted by the centered spectral Gaussian, so formally

`K_t(a)=integral cos(a u) dmu_t(u)`.

No positivity of `mu_t` is assumed. Put

`S=(A+B)/2`,

`D=(B-A)/2`,

where `A=log2` and `B=log3`. Define parity vectors

`X(u)=(cos(Su),cos(Du))`,

`U(u)=(sin(Su),sin(Du))`.

The unnormalized parity blocks are exactly

`G_+=2 integral X(u)X(u)^T dmu_t(u)`,

`G_-=2 integral U(u)U(u)^T dmu_t(u)`.

## Exact determinant identity

For any finite signed measure, and by distributional continuation whenever the pairings exist,

`det G_+ = 2 double_integral det(X(u),X(v))^2 dmu_t(u)dmu_t(v)`,

`det G_- = 2 double_integral det(U(u),U(v))^2 dmu_t(u)dmu_t(v)`.

The diagonal `u=v` vanishes automatically. For an atomic measure this is exactly the Cauchy--Binet wedge sum; finite signed approximations extend the identity algebraically.

The square kernels are pointwise nonnegative:

`Q_+(u,v)=[cos(Su)cos(Dv)-cos(Sv)cos(Du)]^2`,

`Q_-(u,v)=[sin(Su)sin(Dv)-sin(Sv)sin(Du)]^2`.

## What this accomplishes

This identity performs every determinant polarization and endpoint--gamma--prime cancellation before numerical enclosure. Instead of bounding six large signed sector pieces whose residual is `1e-23` of their scale, one evaluates the completed tensor functional

`2 (mu_t tensor mu_t)(Q_+)`,

`2 (mu_t tensor mu_t)(Q_-)`.

It also identifies the exact radical: a channel vanishes when its parity vectors are collinear on the support seen by the completed distribution.

## What it does not accomplish

Pointwise positivity of `Q_+` and `Q_-` does not imply positivity under `mu_t tensor mu_t`, because source-side positivity of `mu_t` is equivalent to the unresolved Weil criterion. The identity is an algebraic preconditioning, not a proof of RH.

Applying the one-variable explicit formula twice will generate endpoint, gamma, and prime-prime contributions in a paired order different from naive determinant polarization. A useful arithmetic advance requires that this paired formula expose cancellations or monotonicity unavailable in the six-sector expansion.

## Revised executable target

Derive the iterated explicit formula for `Q_+` and `Q_-` with common cutoffs. Test whether the prime-prime term admits a diagonal/off-diagonal decomposition whose diagonal is nonnegative and whose off-diagonal part is controlled by the completed archimedean terms. If no such structure appears, record the exact signed residual rather than reverting to independent sector bounds.

## Disposition

The first mixed-prime problem is now reduced to two completed double-Weil square functionals. This is the narrowest algebraic form found that preserves all source terms and removes the observed catastrophic sector polarization before evaluation.

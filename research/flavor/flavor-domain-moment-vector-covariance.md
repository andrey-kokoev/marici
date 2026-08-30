# WP968 — Vector contextual-covariance certificate

Owner: `marici.Figueiredo`.

## Question

What preparation certificate is sufficient for simultaneous estimation of the two
route moments when joint slots are not assumed exchangeable or independent?

## Claim boundary

Let each admitted slot return (X_iin{-1,0,1}), and define the feature
vector

[
phi(X_i)=(X_i,X_i^2)^T.
]

The physical route weights are reconstructed from the feature mean
(m=(m_1,m_2)^T) by

[
p=A m+c,qquad
A=egin{pmatrix}1/2&1/2\\0&-1\\-1/2&1/2end{pmatrix},
qquad c=(0,1,0)^T.
]

For an arbitrary jointly prepared (N)-slot packet, write
(Gamma_{ij}=operatorname{Cov}(phi(X_i),phi(X_j))). The exact covariance of
the empirical feature mean is

[
K_N=rac1{N^2}sum_{i,j=1}^NGamma_{ij},
]

and the exact reconstructed-weight covariance is

[
operatorname{Cov}(widehat p)=A K_N A^T.
]

Thus neither marginal calibration nor a scalar sign covariance certifies the
two-moment instrument. The source-authorized object must bound the full
two-feature contextual covariance (K_N), or a stronger independently
calibrated block covariance from which it follows.

A sufficient matrix certificate is

[
K_Npreceq rac{kappa}{N}I_2.
]

It implies

[
mathbb E|widehat p-p|_2^2
=operatorname{tr}(A K_N A^T)
leq rac{2kappa}{N},
]

because (operatorname{tr}(A^TA)=2). Markov's inequality then gives

[
Pr(|widehat p-p|_1geqeta)
leq rac{6kappa}{Neta^2}.
]

The factor (6) uses (|v|_1^2leq3|v|_2^2). Hence
(Ngeq6kappa/(deltaeta^2)) is sufficient for failure probability at most
(delta).

This is a conditional readout theorem, not a selector. It neither reduces the
admissible flavor family nor privileges a chart. Its first physical gate is a
source-defined joint preparation/reset construction whose calibrated feature
covariance satisfies the matrix inequality over the admitted domain.

## Smallest exact hostile packet

Take two slots with one shared latent route (Z), uniform on
({-1,0,1}), and set (X_1=X_2=Z). Every slot has the correct uniform
marginal. Nevertheless the empirical moments reconstruct the point mass at
(Z), while the target route law is uniform. The total-variation error is
(2/3) for every outcome.

The failure is not in moment inversion. It is the joint preparation arrow:
(Gamma_{12}=Gamma_{11}), so (K_2=Gamma_{11}) rather than
(Gamma_{11}/2). The support feature (X^2) also carries a common mode, which
a sign-only covariance certificate does not control.

## Domain, quotient, instrument, and falsifiers

- State domain: jointly prepared finite packets of labelled route outcomes
  (X_iin{-1,0,1}).
- Faithful quotient coordinate: route weights recovered by the two moments;
  any flavor application remains conditional on the established
  `physical16` route typing.
- Probe family: the source-authorized feature pair ((X,X^2)) in every
  admitted slot.
- Contextual partition: two joint preparations are equivalent exactly when
  they induce the same feature-mean law for the authorized finite packet.
- Instrument: absent until slot construction, reset, feature calibration, and
  a domain-uniform upper certificate for (K_N) are physically supplied.
- Exact falsifiers: the shared-route two-slot packet; violation of
  (K_Npreceq(kappa/N)I_2); or collapse of the smallest certified matrix
  margin under uncertainty/completion.

## Disposition

The scalar exchangeable certificate of WP967 is a one-feature special case.
For the actual two-moment route reconstruction, the largest justified
certificate is matrix-valued. It repairs finite-confidence readout only when
the source preparation supplies the covariance bound; it is neither a selector
nor a presentation rigidifier.

# The endpoint jump is the complete first-order seam obstruction

## Question

After the two one-sided tail problems are uniquely solved, what exactly
obstructs their gluing into one bilateral first-order distribution?

## Piecewise bilateral carrier

Let (G_+,G_-\in H^1(\mathbb R_+)). Form the oriented bilateral function

\[
G(q)=
\begin{cases}
G_+(q),&q>0,\\
G_-(-q),&q<0.
\end{cases}
\]

Write the endpoint jump as

\[
[G]_0=G_+(0)-G_-(0).
\]

Its distributional derivative is

\[
\partial_qG
=
\mathbf 1_{q>0}G_+'(q)
-\mathbf 1_{q<0}G_-'(-q)
+[G]_0\delta_0.
\]

The sign on the negative side is forced by the oriented coordinate.

## Exact sewing theorem

The following conditions are equivalent:

1. (G\in H^1_{\mathrm{loc}}(\mathbb R));
2. the distributional derivative has no seam delta;
3. the endpoint traces agree;
4. ([G]_0=0).

Therefore the endpoint jump is the complete singular obstruction for a
first-order bilateral gluing.

If the one-sided forcing maps and endpoints are already frozen, each half is
unique. Equal endpoint traces then determine a unique bilateral sewn tail.

## Application to the theta tail and seam atoms

Grothendieck's source-derived atoms obey

\[
g_r(0)=h_r(0)=\Phi(r).
\]

Their common trace makes the endpoint jump vanish identically, label by
label and hence for every finite linear packet. This closes the singular
first-order seam gate before arithmetic aggregation.

The opposed inward normal derivatives

\[
g_r'(0)=\Phi'(r),
\qquad
h_r'(0)=-\Phi'(r)
\]

do not create a delta in the first derivative. They are oriented
normal-current data. They become a separate defect only when the completed
identity differentiates again, forms a Green boundary current, or imposes an
additional derivative matching law.

## What remains after trace sewing

Once the common endpoint equality is used, none of the following can be
called an unspecified first-order seam ambiguity:

- the primitive Clark seam line;
- the normal derivative current;
- the arithmetic aggregation map;
- a mixed Green polarization;
- failure of a uniform completion estimate.

Each is a typed downstream object. It must be tested in its own target
space.

## Relation to the alternating polarization

Trace sewing removes the distributional jump but retains the complete
bilateral tail. It therefore does not imply that the mixed or alternating
Green relation descends to the common scalar trace. The compact-support
kernel witnesses survive inside the continuous sewn carrier whenever they
are admitted by the common forcing incidence.

Thus two statements coexist without tension:

1. endpoint equality is sufficient for first-order bilateral gluing;
2. endpoint equality is insufficient for reconstructing cross-tail energy.

The first is a sewing theorem. The second is a relational descent theorem.

## Falsifier certificate

    {
      "code": "first_order_seam_jump",
      "plus_endpoint": "p_plus",
      "minus_endpoint": "p_minus",
      "delta_coefficient": "p_plus - p_minus",
      "sewn_H1_local": false
    }

When the coefficient is zero, any claimed residual first-order delta is a
sign, orientation, or typing error.

## Disposition

The source-derived common trace closes the complete singular first-order
seam obstruction. The surviving frontier is the normal/current layer,
arithmetic aggregation, and relational Green descent.

## Claim boundary

This theorem classifies first distributional derivatives of scalar or
finite-vector half-line graph carriers. It does not prove second-order normal
matching, positivity of a Green boundary form, Fourier--Tate covariance, or
completion-stable observability.

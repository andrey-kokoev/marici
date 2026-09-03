# Nontrivial positive-norm torsors have unbounded return

## Question

Can the full unresolved absolute-lift torsor be bounded uniformly below unit return norm without selecting a lift or proving norm descent?

## Affine growth

Let the absolute lifts of one relative class be

\[
\mathcal L_q=c_0+V,
\]

where \(V=\ker\pi\), and let \(Q\ge0\) be the quadratic form defining the physical normalized coupling norm. Along one torsor direction \(v\in V\),

\[
Q(c_0+tv)
=Q(c_0)+2tQ(c_0,v)+t^2Q(v).
\]

If \(Q(v)>0\), this quantity is unbounded as \(|t|\) grows. Therefore no unrestricted affine torsor containing a positive-norm direction admits a finite uniform norm bound, much less a bound below one.

## Exact descent criterion

For a positive semidefinite form, \(Q(v)=0\) implies \(Q(v,x)=0\) for every \(x\). Hence \(Q\) is constant on all fibers of \(\pi\) exactly when

\[
V\subseteq\operatorname{rad}(Q).
\]

If \(Q\) is positive definite on the declared absolute support, its radical is zero. A nontrivial rank-seven lift torsor then cannot be invisible to the norm and coercivity cannot descend through the relative quotient.

Thus the previously proposed “uniformly bound the full torsor” alternative is viable only if source admissibility cuts the affine fiber to a bounded subset. For the unrestricted torsor it is impossible unless every direction is radical.

## Hostile family

With Euclidean \(Q\), base lift \(c_0=(3/5,0)\), and torsor direction \(v=(0,1)\), the squared norms at \(t=0,1,2\) are

\[
\frac9{25},
\qquad
\frac{34}{25},
\qquad
\frac{109}{25}.
\]

The same relative class moves from strict to superunit return. With semidefinite \(Q=\operatorname{diag}(1,0)\), the same direction is radical and all three norms equal \(9/25\); only in this second case does the norm descend.

## Joint-form gate

Testing pair or triple restrictions cannot replace the full descent theorem. Voevodsky's four-sector counterexample has every pair and triple restriction positive while the full joint Gram form has a negative collective eigenvalue. The radical and coercivity tests must therefore be made on the complete physical joint form or follow from a source-derived all-size theorem.

## Verification

`research/aspect/checkers/check_torsor_norm_descent.py` verifies affine norm growth, threshold crossing, radical constancy, and absence of nonzero radical for a positive-definite form using exact rationals.

## Disposition

The q_G12 branch now has a binary gate. Either source admissibility selects or bounds an absolute lift, or the complete physical form must be semidefinite with the entire rank-seven torsor in its radical. If the form is positive definite and the torsor remains unrestricted, coercivity descent is impossible.

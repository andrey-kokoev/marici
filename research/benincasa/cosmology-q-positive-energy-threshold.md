# The algebraic quartic has one nonsoft positive-energy crossing

> **Scope.** This is a real-locus theorem, not a singular-support theorem.
> Ledger Entries 181, 183, and 212 prove that the resolved physical pair and
> source cycle extend across a generic such crossing with trivial monodromy
> and variation. Entry 718 confirms that the lower second-normal mechanism
> does not reopen that verdict.

Let

\[
s=X_1+X_2,
\qquad
p=X_1X_2,
\qquad
E=X_1+X_2+X_3,
\]

with \(X_1,X_2>0\) and \(X_3\ge0\).  The source quartic is

\[
\mathcal Q(E)
=-16p^2-8pE^2+8sE^3-5E^4.
\]

At the soft endpoint \(E=s\), exact factorization gives

\[
\boxed{
\mathcal Q(s)
=(s^2-4p)(3s^2+4p)
=(X_1-X_2)^2(3s^2+4p).
}
\]

Hence \(\mathcal Q(s)>0\) for unequal positive \(X_1,X_2\), whereas
\(\mathcal Q(E)\to-\infty\) as \(E\to+\infty\).

Differentiate:

\[
\mathcal Q'(E)
=-4E\,g(E),
\qquad
g(E)=5E^2-6sE+4p.
\]

On \(E\ge s\),

\[
g(s)=4p-s^2=-(X_1-X_2)^2<0,
\]

and

\[
g'(E)=10E-6s\ge4s>0.
\]

Thus \(g\) crosses zero exactly once.  The quartic first increases from its
positive soft-endpoint value, then decreases strictly to \(-\infty\).
Consequently:

\[
\boxed{
X_1\ne X_2
\Longrightarrow
\exists!\ E_Q>s\text{ with }\mathcal Q(E_Q)=0.
}
\]

Equivalently, every positive unequal \((X_1,X_2)\) ray contains exactly one
nonsoft positive \(X_3=E_Q-s\) quartic crossing.

If \(X_1=X_2\), then \(\mathcal Q(s)=g(s)=0\), while \(g(E)>0\) for
\(E>s\).  The quartic decreases immediately and has no additional positive
root.  The crossing then collapses onto soft support.

## Consequence for the Q search

The two-prime transport census proves that the labelled source transports do
not lose cohomological rank at generic \(\mathcal Q=0\).  The theorem above
shows simultaneously that \(\mathcal Q=0\) is reached in the real positive
energy chamber.  This does **not** make it a physical threshold: the frozen
raw Landau/log-discriminant census has no generic \(\mathcal Q\) component.
The prior simultaneous-resolution theorem already answers the generic
crossing comparison:

\[
\boxed{
T_{\mathcal Q}=1,
\qquad N_{\mathcal Q}=0,
\qquad \operatorname{Var}_{\mathcal Q}(\Gamma_{\rm phys})=0.
}
\]

This supports neither a new Carrier wall nor a raw transport singularity. The
canonical cycle is locally constant across a generic crossing, and the word
“threshold” is inadmissible. The zero is a real crossing of an apparent
algebraic letter, not a physical singularity.

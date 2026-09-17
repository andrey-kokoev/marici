# The L=0.75 fourth jet defeats sectorwise tail budgeting

After directed certification of value through third-derivative jump tails, the remaining triangle-budget reserve is

$$
2.5211505334213682793\times 10^{-10}.
$$

A 256-bit Arb computation of the fourth-derivative jump component, using five Legendre antiderivatives and modes from 1000 through 49999 followed by a Bernstein tail bound, gives

$$
\|T_4\|
\leq
4.047879133690114\times 10^{-10}.
$$

Thus

$$
\|T_4\|
>
2.521150533421369\times 10^{-10}.
$$

This rejects completion by independent absolute bounds on successive jet sectors. It does not reject positivity of the full tail because the decomposition

$$
r_{\rm tail}=T_0+T_1+T_2+T_3+T_4+r_{C^5}+r_\gamma+r_{\rm endpoint}
$$

is not orthogonal. Cross terms can cancel, and the completed source requires precisely such coupled cancellation.

The next valid test must assemble the full interval tail vector, or an interval Gram matrix retaining its cross terms, before taking the norm. Adding component norms by the triangle inequality is now quantitatively too expensive.

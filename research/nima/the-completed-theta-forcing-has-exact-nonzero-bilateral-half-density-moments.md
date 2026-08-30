# The completed theta forcing has exact nonzero bilateral half-density moments

The base-source qualification left open in event 10304 is already settled by
the completed bilateral theta Green identity.

Let

[
h(u)=rac12 e^{u/2}artheta(e^{2u}),
qquad
Phi=left(partial_u^2-rac14ight)h.
]

Modularity makes (h) even, and the two source Wronskian traces satisfy

[
M_-(Phi)=int_{mathbb R}e^{-u/2}Phi(u),du=rac12,
qquad
M_+(Phi)=int_{mathbb R}e^{u/2}Phi(u),du=rac12.
]

Thus the admitted completed theta precursor has neither half-density channel
dark:

[
(M_-^0,M_+^0)=left(rac12,rac12ight).
]

This is not inferred from parity alone. The value and normalization follow
from the endpoint Wronskian jumps of the source precursor (h).

## Prime transport

For (L=log p), the primitive Euler half-density (p^{-1/2}) followed by
Mellin transport gives

[
p^{-1/2}T_L=operatorname{diag}(1,p^{-1}).
]

Applied to the exact theta trace column, this gives

[
v_p^{+}
=
rac12
egin{pmatrix}
1\
p^{-1}
end{pmatrix}.
]

The reciprocal chart gives

[
v_p^{-}
=
rac12
egin{pmatrix}
p^{-1}\
1
end{pmatrix}.
]

Hence the full reciprocal two-chart matrix is

[
V_p
=
rac12
egin{pmatrix}
1&p^{-1}\
p^{-1}&1
end{pmatrix}.
]

Its determinant and singular values are

[
det V_p=rac14(1-p^{-2})>0,
]

[
sigma_pm(V_p)=rac12(1pm p^{-1}).
]

Therefore

[
sigma_{min}(V_p)
=
rac12(1-p^{-1})
ge
rac14.
]

The reciprocal doubled theta-signal packet is consequently an exact,
uniformly faithful rank-two local wall observer at every prime.

## Relation to the derivative companion

The independently source-derived odd precursor (Phi') has exact column

[
left(M_-(Phi'),M_+(Phi')ight)
=
left(rac14,-rac14ight).
]

It provides the parity-diagonal description of the same local two-dimensional
trace capacity. The reciprocal translated pair above instead exhibits that
capacity in the two comoving prime charts. These descriptions must be related
by an authorized comparison cell; equality of their spans is not by itself
that cell.

## What this closes

This closes the base-moment and finite local-frame questions:

- both source half-density moments exist;
- both equal (1/2);
- reciprocal prime transport produces rank two;
- the local lower frame bound is at least (1/4).

It does not yet construct the incidence map from the doubled passive signal
port into the theta history pair, nor prove graph closure or primewise
assembly. The earliest remaining constructor is therefore narrower:

[
	ext{doubled signal port}
longrightarrow
	ext{reciprocal translated theta trace pair}.
]

That arrow must intertwine prime labels, reflection, Mellin transport, and the
source Wronskian normalization. No boundary-pencil or coercivity claim follows.

## Source locators

- `research/nima/twisted-theta-histories-give-exact-normalized-completion-trace-columns.md`
- `research/nima/the-bilateral-theta-derivative-supplies-the-missing-reciprocal-trace-direction.md`
- `research/nima/mellin-half-density-transport-exactly-preserves-the-bilateral-trace-frame.md`
- `research/nima/euler-half-density-plus-mellin-transport-forces-the-local-wall-square-coefficient-pair.md`

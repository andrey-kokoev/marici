# The zero-section sum exactly equals the reciprocal Euler odd derivative

## Gradewise zero-section response

For one prime (p), let the grade-(k) Fock coefficient be

[
a_{p,k}=rac1k p^{-k/2}.
]

The signed zero-section position pairing contributes

[
2a_{p,k}k(log p)
=
2(log p)p^{-k/2}
]

when the position test is normalized to one at (klog p).

Summing over all positive grades gives

[
J_p^{mathrm{zero}}
=
2(log p)sum_{kge1}p^{-k/2}
=
rac{2(log p)p^{-1/2}}{1-p^{-1/2}}.
]

## Exact Euler identity

The reciprocal Euler ratio satisfies

[
left.partial_zloggamma_p(z)ight|_{z=0}
=
rac{2(log p)p^{-1/2}}{1-p^{-1/2}}.
]

Therefore

[
J_p^{mathrm{zero}}
=
left.partial_zloggamma_p(z)ight|_{z=0}.
]

This is an exact source-level linking identity between the sheet-oriented
zero-section current and the odd reciprocal Euler response. No fitted
normalization remains once the signed-position convention is frozen.

With the endpoint-Gram convention,

[
h_p
=
rac12J_p^{mathrm{zero}}
=
rac12left.partial_zloggamma_p(z)ight|_{z=0}.
]

## Granularity correction

The two-endpoint Adams cell contains only grades (1) and (2). Its truncated
zero-section current is

[
J_p^{(1,2)}
=
2(log p)
left(
p^{-1/2}+p^{-1}
ight).
]

Hence its intrinsic odd coordinate is

[
h_p^{(1,2)}
=
(log p)
left(
p^{-1/2}+p^{-1}
ight).
]

The full Euler odd coordinate is

[
h_p^{(infty)}
=
rac{(log p)p^{-1/2}}{1-p^{-1/2}}.
]

Their difference is the connected higher-grade tail:

[
h_p^{(ge3)}
=
(log p)
rac{p^{-3/2}}{1-p^{-1/2}}.
]

Thus inserting (h_p^{(infty)}) directly into a (2	imes2) primitive--square
Gram silently imports every grade (kge3).

## Two legitimate constructions

### Strict two-endpoint cell

Use (h_p^{(1,2)}) in the primitive--square Gram and retain the connected tail
as a separate feature channel.

### Completed local Euler cell

Enlarge the coefficient space to include all Fock grades, form the full odd
current there, and only then compress to a primitive--square effective block
through a source-authorized Schur or pushforward map.

These constructions can agree only after proving that the eliminated tail
induces exactly the difference (h_p^{(ge3)}).

## Positivity test at correct granularity

For the strict two-endpoint Gram, the positivity condition is

[
left(h_p^{(1,2)}ight)^2
le
a_pb_p-x_p^2.
]

The full (h_p^{(infty)}) must instead be tested against the determinant of
the enlarged completed local cell or its authorized effective Schur
complement. Testing it against the bare (2	imes2) even plane is mistyped.

## Wronskian gate

The arithmetic linking is now exact:

[
	ext{zero-section current}
=
	ext{odd Euler derivative}.
]

The remaining three-way theorem is only the analytic leg:

[
J_p^{mathrm{Wr}}
=
J_p^{mathrm{zero}}
]

after polarization on the relative Green domain and with the same sign frame.

## Consequence

One of the three desired calibrations is closed algebraically. The frontier is
no longer to compare three unrelated odd quantities. It is:

1. choose strict or completed local granularity;
2. retain the connected odd tail accordingly;
3. prove the polarized Wronskian represents the already identified
   zero-section/Euler current.

This prevents a correct all-grade arithmetic current from being attached to
the wrong finite Gram.

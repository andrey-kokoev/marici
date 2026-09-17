# Operator face registry for the eight-axis positive cube

The eight axes give

$$
\binom{8}{2}=28
$$

generic square types and

$$
28\cdot2^6=1792
$$

square instances.

| Face | Status | Operator decoration |
|---|---|---|
| $$H\times V$$ | strict | transverse Beck--Chevalley |
| $$H\times D$$ | strict | dagger naturality of rooted substitution |
| $$H\times q$$ | canonical | Fourier transports rooted convolution to chart product |
| $$H\times L$$ | strict | convolution associativity |
| $$H\times C$$ | strict | multiplicativity of forward realization |
| $$H\times O$$ | strict | multiplicativity of endpoint observation |
| $$H\times R$$ | strict | completion continuity of rooted substitution |
| $$V\times D$$ | strict | dagger naturality of marked cuts |
| $$V\times q$$ | canonical | Fourier transport of Laurent cut multipliers |
| $$V\times L$$ | strict | commuting admitted cut and degree multipliers |
| $$V\times C$$ | strict | realization of marked cut branches |
| $$V\times O$$ | strict | endpoint transport of cut labels |
| $$V\times R$$ | strict | Laurent completion continuity of cuts |
| $$D\times q$$ | strict | source reflection and chart successor |
| $$D\times L$$ | strict | left/right successor dagger exchange |
| $$D\times C$$ | strict | contragredient realization square |
| $$D\times O$$ | strict | endpoint swap-conjugation |
| $$D\times R$$ | strict | dagger on graph completion |
| $$q\times L$$ | canonical | Fourier convolution-to-multiplication successor |
| $$q\times C$$ | historical gate | native chart-to-realization intertwiner |
| $$q\times O$$ | strict | retained observation under chart transport |
| $$q\times R$$ | lax | cutoff leakage |
| $$L\times C$$ | strict | Mellin realization of degree successor |
| $$L\times O$$ | strict | endpoint multiplier naturality |
| $$L\times R$$ | strict | closed multiplier extension |
| $$C\times O$$ | strict | observation through realization |
| $$C\times R$$ | strict | realization through completion |
| $$O\times R$$ | strict | observation through completion |

The status count is:

$$
23\text{ strict},
\qquad
3\text{ canonical},
\qquad
1\text{ lax},
\qquad
1\text{ historical gate}.
$$

The lax coefficient is

$$
A_X=P_X\mathcal F(I-P_X).
$$

Every cubical 3-face inherits exactly three entries from this table. There are

$$
\binom{8}{3}2^5=1792
$$

such 3-face instances.

The canonical retained model now has a decoration on every square type. The historical native model requires the chart-to-realization map on

$$
q\times C.
$$

The next residue test compares the three square decorations around each generic 3-face and records the corresponding modification or obstruction.

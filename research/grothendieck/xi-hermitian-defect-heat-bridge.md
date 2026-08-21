# Hermitian heat bridge for the RH reflection defect

For the normal zero operator `Z e_rho=(rho-1/2)e_rho`, let

```
X=Re Z=(Z+Z*)/2.
```

Define the Hermitian defect heat trace

```
Theta_H(t)=Tr[X^2 exp(-t Z*Z)]
          =sum_rho (Re(rho)-1/2)^2
             exp(-t|rho-1/2|^2),       t>0.            (1)
```

Every summand is nonnegative. The critical-strip bound and zero counting
make the trace finite for every `t>0`. Functional calculus gives

```
H_Xi = Tr[X^2(I+Z*Z)^(-1)]
     = integral_0^infinity e^(-t) Theta_H(t) dt.        (2)
```

Consequently the following are equivalent:

```
RH;
X=0;
Theta_H(t)=0 for every t>0;
Theta_H(t_0)=0 for one t_0>0;
H_Xi=0.                                                (3)
```

The one-time equivalence follows because (1) is a sum of nonnegative terms.

## Hostile quartet

For a simple off-line quartet with horizontal displacement
`a=beta-1/2` and height `T`,

```
Theta_H^quartet(t)=4a^2 exp[-t(a^2+T^2)],              (4)
```

whose Laplace integral with `e^(-t)` is

```
4a^2/[1+a^2+T^2].                                     (5)
```

Thus the heat bridge retains the smallest off-line falsifier exactly.

## Difference from the existing spectral heat trace

The earlier RH-conditional heat trace uses squared real ordinates. Away
from RH, a holomorphic continuation involves `Z^2`, whereas (1) uses the
positive operator `Z*Z`. These are categorically different:

```
exp(-tZ^2)      holomorphic but not positive off line;
exp(-tZ*Z)      positive but Hermitian/nonholomorphic.                 (6)
```

An ordinary one-variable explicit formula naturally accesses holomorphic
functions of `Z`. The desired source identity must instead construct the
adjoint and the paired heat semigroup, or equivalently the conjugation-graph
correspondence. Calling the holomorphic heat kernel “the same” is a
falsifiable category error.

## Source-side target

Construct an arithmetic Hilbert space and a normal operator `Z_src` such
that a trace identity identifies

```
Tr[(Re Z_src)^2 exp(-t Z_src*Z_src)]
```

with (1), then derive its vanishing without assuming RH. Even a source-side
upper bound tending to zero for one fixed `t` would suffice. No such
construction is claimed here.


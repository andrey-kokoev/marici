# Functional-completion extension diagram

```text
finite point packets (strict LF)
        |                         \
        | TV completion           \ weak-* completion
        v                           v
countably atomic l1 measures     finite Radon measures
        | no pure smooth low        | contains smooth flux densities
        | harmonic                   v
        |                    hard source channels
        |                 T_uu (electric), coexact T_uA (magnetic)
        |                           |
        +---------------------------+----------------------+
                                                            v
                                      shear C in H^s(L^2) + H^s(L^-2)
                                                            |
                                            parity/helicity decomposition
                                                            |
                                                            v
                         A_3=(bar-eth eth^3, eth bar-eth^3)
                              /                         \
                             /                           \
            kernel: l=2,3,4 (21/sector)       transported l>=5 output
                             |                  target l=4 cokernel (9)
                             v
                    P_low: 21-port repair
                             |
                             v
                 (A_3 C, P_low C) is faithful

local scalar chart only:
    p^4-q^4 = 0 -> four ridge families
                    |
                    +-- cutoff creates source
                    +-- no compactly supported distributional solution
                    +-- no nonzero planar L2 solution
                    +-- no authority to replace the paired global operator
```

The two completion arrows are different constructors. Total-variation
completion preserves atomic source type and does not create the smooth low
kernel. Weak-* completion admits smooth flux densities and therefore admits
the global `l=2,3,4` kernel. Enlarging scalar coefficients alone does neither.

The first nonfaithful arrow is the grade-three readout, not hard transport.
The low projector is consequently attached before that quotient. Endpoint
memory is a separate port: it can remove a permanent magnetic endpoint record,
but it does not observe a returning pulse.

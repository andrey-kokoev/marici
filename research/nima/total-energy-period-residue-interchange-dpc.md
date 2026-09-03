# Total-energy period-residue interchange

## Problem

After withdrawing every amplitude interpretation, the surviving claim says the explicit simple total-energy pole yields a computable twisted-period residue.

## Bold conjecture

The explicit `1/E` factor in the frozen three-site integrand supplies a computable residue of the integrated twisted period at `E=0`.

## Named rivals

1. formal rational residue automatically commutes with the period integral;
2. only the integrand residue exists, while the relative chain may pinch or change at `E=0`;
3. the generic oriented chain specializes, but endpoint terms obstruct residue/integration interchange.

## Risky consequences

The source must provide a relative-chain specialization to `E=0`, endpoint trivialization there, and an interchange theorem identifying residue of the period with period of the residue.

## Strongest falsification attempt and residual

`research/benincasa/cyclic_q_assembly_certificate.md` freezes the explicit denominator `q_G=E`, the rational integrand, and one common oriented chain at generic source parameters. It does not construct:

- specialization of that relative chain to `E=0`;
- endpoint trivialization at the total-energy divisor;
- a residue/integration interchange map.

Execution `structured_command_execution:e_32940_1788309397602869800_4` verifies the missing arrow census. Therefore the explicit pole supplies a formal rational-integrand residue but not a computable twisted-period residue. The bold period-level conjecture is falsified.

## Disposition and residual conjecture

The surviving object is only

\[
\operatorname{Res}^{\rm formal}_{E=0}(\text{rational integrand}).
\]

Promotion to a period requires source-derived relative-chain specialization and residue/integration interchange. Reopening requires those maps; neither amplitude language nor generic-chain orientation supplies them.

## Evidence

- `research/nima/checkers/check_total_energy_period_residue_interchange.py`
- `research/benincasa/cyclic_q_assembly_certificate.md`
- `research/nima/total-energy-amplitude-proportionality-typing-dpc.md`

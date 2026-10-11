"""Quarantined entrypoint: the former matrix narrative was not a valid checker.

Use TickRetainedStructure.agda for the full fixed-source Bool classification,
and check_tick_interpretation_nonuniqueness.py for the explicitly declared
stochastic interpretation class. Neither selects physical unitary dynamics.
The original source and receipt are hash-preserved under quarantine/.
"""
import sys


def main():
    print(
        'QUARANTINED: check_tick_selects_generator.py contained false matrix '
        'claims and unconditional success reporting. No verification performed. '
        'See research/nima/tick-evidence-repair-20261007.md and '
        'research/nima/source-to-generator-audit.md.',
        file=sys.stderr,
    )
    return 2


if __name__ == '__main__':
    raise SystemExit(main())

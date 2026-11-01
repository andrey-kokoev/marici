"""Replay the period-cover rival and native integer-lift boundary operation."""
from pathlib import Path
import json
import subprocess

if __name__ == '__main__':
    results = []
    for name in ['check_su32_five_period_cover.mjs', 'check_su32_native_window_operation.mjs']:
        done = subprocess.run(
            ['node', 'research/strominger/checkers/' + name],
            cwd=Path(__file__).resolve().parents[3], capture_output=True,
            text=True, encoding='utf-8',
        )
        if done.returncode:
            print(done.stdout)
            print(done.stderr)
            raise SystemExit(done.returncode)
        result = json.loads(done.stdout)
        assert result['passed'] is True
        results.append(result)
    print(json.dumps({
        'passed': True,
        'conclusion': results[1]['conclusion'],
        'nativeOperation': results[1],
        'finiteCoverRival': results[0],
    }, indent=2))

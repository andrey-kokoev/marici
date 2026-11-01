"""SCC evidence preflight; does not run Node or certify physical compatibility."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[3]
p = root / 'research/strominger/results/cellulation-dot-422-compatibility.json'
report = json.loads(p.read_text(encoding='utf-8'))
assert report['status'] == 'unresolved' and report['checksPassed'] is True
for source in report['sources']:
    assert hashlib.sha256((root / source['path']).read_bytes()).hexdigest() == source['sha256'], source['path']
assert report['strict']['complete'] is False
assert report['strict']['completedCells'] == 0
assert report['strict']['dot422Colour'] is None
for result in report['results']:
    assert {c['colour'] for c in result['dot422Claims']} == {0xff3030, 0xffffff}
    assert result['sourceCompatible'] is False
assert any(b.get('point') == '3,3,2' and b.get('requiredColour') == 0xff3030 and b.get('observedColour') == 0xffffff for b in report['strict']['blockers'])
print(json.dumps({'classification': 'blocked', 'checks_passed': True,
                  'obligation': 'route/coherencer compatibility before readout descent',
                  'residual': report['residual'], 'evidence': str(p.relative_to(root))}))

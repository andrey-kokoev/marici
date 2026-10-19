"""Refresh the registry from existing inventory; do not refresh collection copies."""
import json
from collect import HOME, registry


if __name__ == '__main__':
    inventory = json.loads((HOME / 'inventory.json').read_text(encoding='utf-8'))
    selected = {entry['source']: entry['reason'] for entry in inventory['files']}
    (HOME / 'registry.json').write_text(json.dumps(registry(selected), indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('Programme registry refreshed; collection snapshots and inventory unchanged.')

from pathlib import Path
import tarfile
root = Path(__file__).resolve().parents[3]
base = root / 'research/sources/nima/papers/six-point-nmhv'
for arxiv_id in ('0907.5418','1008.2958'):
    target = base / arxiv_id
    target.mkdir(parents=True, exist_ok=True)
    with tarfile.open(base / f'{arxiv_id}.eprint', 'r:*') as archive:
        members = [m for m in archive.getmembers() if m.isfile() and not Path(m.name).is_absolute() and '..' not in Path(m.name).parts]
        archive.extractall(target, members=members, filter='data')
    print(arxiv_id, len(members))

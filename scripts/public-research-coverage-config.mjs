import fs from 'node:fs/promises'
import path from 'node:path'
import { createHash } from 'node:crypto'

export const coveragePointerPath = 'config/public-research-coverage.current.json'
export const canonicalCoverageJSON = value => JSON.stringify(value, null, 2) + '\n'
const digest = value => createHash('sha256').update(canonicalCoverageJSON(value)).digest('hex')

export async function loadPublicResearchCoverage(base) {
  const pointer = JSON.parse(await fs.readFile(path.join(base, coveragePointerPath), 'utf8'))
  if (pointer.schema !== 'marici.public-research-coverage-pointer.v1' || !Array.isArray(pointer.history) || !pointer.history.length || pointer.history_hash_basis !== 'SHA-256 of UTF-8 JSON.stringify(snapshot, null, 2) plus LF') throw Error('Invalid coverage current pointer or missing history')
  const refs = [pointer, ...pointer.history]
  const seen = new Set()
  const versions = []
  for (const ref of refs) {
    const match = /^config\/public-research-coverage\.v([1-9][0-9]*)\.json$/.exec(ref.config ?? '')
    if (!match || ref.snapshot_id !== 'public-research-frontier-v' + match[1] || seen.has(ref.snapshot_id)) throw Error('Unsafe, mismatched or duplicate coverage snapshot reference')
    seen.add(ref.snapshot_id)
    versions.push(Number(match[1]))
  }
  if (versions.slice(1).some(version => version >= versions[0])) throw Error('Coverage current pointer must select a successor of historical snapshots')
  const snapshots = []
  for (const [index, ref] of refs.entries()) {
    const contract = JSON.parse(await fs.readFile(path.join(base, ref.config), 'utf8'))
    if (contract.schema !== 'marici.public-research-coverage.v1' || contract.snapshot_id !== ref.snapshot_id || contract.scientific_dispositions_modified !== false) throw Error('Invalid or overstated coverage snapshot')
    if (index && (!/^[a-f0-9]{64}$/.test(ref.sha256 ?? '') || digest(contract) !== ref.sha256)) throw Error('Historical coverage snapshot changed: ' + ref.config)
    snapshots.push({ config: ref.config, snapshot_id: ref.snapshot_id, sha256: digest(contract), contract })
  }
  return { pointer, contract: snapshots[0].contract, snapshots }
}

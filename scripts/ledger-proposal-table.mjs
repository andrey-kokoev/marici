import fs from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const ledgerRoot = path.join(root, 'src', 'ledger')
const graphLedgerRoot = path.join(root, '.narada', 'epistemic', 'ledger')
const ledgerFilenamePattern = /(?:^|\/)(\d{8})-(\d+)[ _-](.+)\.md$/i

function parseDate(value, optionName) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) {
    throw new Error(`${optionName} must be YYYY-MM-DD`)
  }
  const date = new Date(`${value}T00:00:00.000Z`)
  if (Number.isNaN(date.valueOf()) || date.toISOString().slice(0, 10) !== value) {
    throw new Error(`${optionName} is not a valid calendar date`)
  }
  return value
}

async function walkMarkdown(directory, relative = '') {
  const files = []
  for (const entry of await fs.readdir(path.join(directory, relative), { withFileTypes: true })) {
    const child = path.posix.join(relative, entry.name)
    if (entry.isDirectory()) files.push(...await walkMarkdown(directory, child))
    else if (entry.isFile() && entry.name.toLowerCase().endsWith('.md')) files.push(child)
  }
  return files
}

function dateRange(startDate, endDate) {
  const dates = []
  for (let time = Date.parse(`${startDate}T00:00:00.000Z`); time <= Date.parse(`${endDate}T00:00:00.000Z`); time += 86_400_000) {
    dates.push(new Date(time).toISOString().slice(0, 10))
  }
  return dates
}

/** Count dated ledger Markdown files and admitted graph proposals by UTC date. */
export async function buildLedgerProposalTable({
  startDate = '2026-08-10',
  endDate = new Date().toISOString().slice(0, 10),
} = {}) {
  parseDate(startDate, 'startDate')
  parseDate(endDate, 'endDate')
  if (startDate > endDate) throw new Error('startDate must not be after endDate')

  const markdownCounts = new Map()
  for (const relative of await walkMarkdown(ledgerRoot)) {
    const match = relative.replaceAll('\\', '/').match(ledgerFilenamePattern)
    if (!match) continue
    const date = `${match[1].slice(0, 4)}-${match[1].slice(4, 6)}-${match[1].slice(6, 8)}`
    if (date >= startDate && date <= endDate) markdownCounts.set(date, (markdownCounts.get(date) ?? 0) + 1)
  }

  const proposalIdsByDate = new Map()
  const eventFiles = (await fs.readdir(graphLedgerRoot)).filter(name => /^ev-\d{12}-[0-9a-f-]+\.json$/i.test(name)).sort()
  for (const name of eventFiles) {
    const event = JSON.parse(await fs.readFile(path.join(graphLedgerRoot, name), 'utf8'))
    if (event.event_kind !== 'proposal_admitted' || !event.proposal_id || !event.occurred_at) continue
    const date = new Date(event.occurred_at).toISOString().slice(0, 10)
    if (date < startDate || date > endDate) continue
    if (!proposalIdsByDate.has(date)) proposalIdsByDate.set(date, new Set())
    proposalIdsByDate.get(date).add(event.proposal_id)
  }

  const rows = dateRange(startDate, endDate).map(date => ({
    date,
    ledgerMarkdownFiles: markdownCounts.get(date) ?? 0,
    admittedProposals: proposalIdsByDate.get(date)?.size ?? 0,
  }))
  rows.push({
    date: 'Total',
    ledgerMarkdownFiles: rows.reduce((sum, row) => sum + row.ledgerMarkdownFiles, 0),
    admittedProposals: rows.reduce((sum, row) => sum + row.admittedProposals, 0),
  })
  return rows
}

export function formatLedgerProposalTable(rows) {
  return [
    '| Date | Ledger MD files | Admitted proposals |',
    '|---|---:|---:|',
    ...rows.map(row => `| ${row.date} | ${row.ledgerMarkdownFiles.toLocaleString('en-US')} | ${row.admittedProposals.toLocaleString('en-US')} |`),
  ].join('\n')
}

async function main() {
  const args = process.argv.slice(2)
  let startDate = '2026-08-10'
  let endDate = new Date().toISOString().slice(0, 10)
  for (let index = 0; index < args.length; index++) {
    if (args[index] === '--from' && args[index + 1]) startDate = args[++index]
    else if (args[index] === '--to' && args[index + 1]) endDate = args[++index]
    else throw new Error(`Usage: node scripts/ledger-proposal-table.mjs [--from YYYY-MM-DD] [--to YYYY-MM-DD]`)
  }
  console.log(formatLedgerProposalTable(await buildLedgerProposalTable({ startDate, endDate })))
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch(error => {
    console.error(error.message)
    process.exitCode = 1
  })
}

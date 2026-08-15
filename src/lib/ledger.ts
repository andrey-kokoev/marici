import { getCollection } from 'astro:content'
import type { CollectionEntry } from 'astro:content'

export type LedgerEntry = CollectionEntry<'ledger'>

export interface LedgerMeta {
  dateKey: string
  entry: number
  title: string
  description: string
  publishedAt: Date
  slug: string
  kind: string
}

export interface LedgerRecord {
  entry: LedgerEntry
  meta: LedgerMeta
}

function stripMarkdown(value: string): string {
  return value
    .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .replace(/[*_>#]/g, '')
    .replace(/\s+/g, ' ')
    .trim()
}

function firstParagraph(body: string, fallback: string): string {
  const candidate = body
    .split(/\r?\n\s*\r?\n/)
    .map((block) => block.trim())
    .find((block) => block && !/^#{1,6}\s/.test(block) && !/^[-*_]{3,}$/.test(block) && block !== '---' && !(/^\u0060{3}/.test(block)))
  const text = stripMarkdown(candidate ?? '')
  if (!text) return fallback
  if (text.length <= 280) return text
  return text.slice(0, 277).replace(/\s+\S*$/, '') + '…'
}

function dateFromKey(dateKey: string): Date {
  const year = Number(dateKey.slice(0, 4))
  const month = Number(dateKey.slice(4, 6))
  const day = Number(dateKey.slice(6, 8))
  return new Date(Date.UTC(year, month - 1, day))
}

function kindFor(title: string, body: string): string {
  const haystack = (title + ' ' + body).toLowerCase()
  if (/falsif|no-go|obstruction|gap|boundary/.test(haystack)) return 'boundary'
  if (/result|calibr|test|audit|search/.test(haystack)) return 'result'
  return 'research'
}

function toRecord(entry: LedgerEntry): LedgerRecord | null {
  const id = entry.id.replace(/\.(?:md|mdx)$/i, '').replace(/\\/g, '/')
  const match = id.match(/(?:^|\/)(\d{8})-(\d+)[ _-](.+)$/)
  if (!match) return null

  const [, dateKey, entryNumber, filenameTitle] = match
  const title = entry.body.match(/^#\s+(.+)$/m)?.[1]?.trim() || filenameTitle
  const slug = (dateKey + '-' + entryNumber + '-' + filenameTitle).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')

  return {
    entry,
    meta: {
      dateKey,
      entry: Number(entryNumber),
      title,
      description: firstParagraph(entry.body, title),
      publishedAt: dateFromKey(dateKey),
      slug,
      kind: kindFor(title, entry.body),
    },
  }
}

export async function getPublishedLedger(includeDrafts = import.meta.env.DEV): Promise<LedgerRecord[]> {
  const entries = await getCollection('ledger', ({ data }) => includeDrafts || !data.draft)
  return entries
    .map(toRecord)
    .filter((record): record is LedgerRecord => record !== null)
    .sort((a, b) => a.meta.entry - b.meta.entry || a.meta.slug.localeCompare(b.meta.slug))
}

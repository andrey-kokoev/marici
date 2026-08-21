import { defineCollection } from 'astro:content'
import { z } from 'astro/zod'
import { readdir, readFile } from 'node:fs/promises'
import { join, relative } from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

async function collectMarkdownFiles(directory: string): Promise<string[]> {
  const files: string[] = []
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name)
    if (entry.isDirectory()) {
      files.push(...(await collectMarkdownFiles(path)))
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      files.push(path)
    }
  }
  return files.sort()
}

function ledgerLoader() {
  return {
    name: 'marici-ledger-loader',
    async load({ config, entryTypes, generateDigest, parseData, store }) {
      const baseDirectory = fileURLToPath(new URL('./src/ledger/', config.root))
      const entryType = entryTypes.get('.md')
      if (!entryType) throw new Error('Markdown entry type is unavailable')

      store.clear()
      for (const filePath of await collectMarkdownFiles(baseDirectory)) {
        const fileUrl = pathToFileURL(filePath)
        const contents = await readFile(filePath, 'utf-8')
        const { body, data } = await entryType.getEntryInfo({ contents, fileUrl })
        const id = relative(baseDirectory, filePath)
          .replace(/\\/g, '/')
          .replace(/\.md$/i, '')
        const parsedData = await parseData({ id, data, filePath })
        store.set({
          id,
          data: parsedData,
          body,
          filePath: relative(fileURLToPath(config.root), filePath).replace(/\\/g, '/'),
          digest: generateDigest(contents),
        })
      }
    },
  }
}

const ledger = defineCollection({
  loader: ledgerLoader(),
  schema: z.object({
    draft: z.boolean().optional(),
    author: z.enum(['marici.Nima', 'marici.Benincasa', 'marici.Strominger', 'marici.Figueiredo', 'marici.Grothendieck']).optional(),
    authors: z.array(z.enum(['marici.Nima', 'marici.Benincasa', 'marici.Strominger', 'marici.Figueiredo', 'marici.Grothendieck'])).min(1).optional(),
  }).passthrough(),
})

export const collections = { ledger }

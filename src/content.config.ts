import { defineCollection } from 'astro:content'
import { glob } from 'astro/loaders'
import { z } from 'astro/zod'

const ledger = defineCollection({
  loader: glob({
    base: './src/ledger',
    pattern: '**/*.md',
  }),
  schema: z.object({
    draft: z.boolean().optional(),
    author: z.enum(['marici.Nima', 'marici.Benincasa']).optional(),
    authors: z.array(z.enum(['marici.Nima', 'marici.Benincasa'])).min(1).optional(),
  }).passthrough(),
})

export const collections = { ledger }

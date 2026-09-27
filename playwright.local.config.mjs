import { defineConfig } from '@playwright/test'

export default defineConfig({
  testDir: './tests',
  outputDir: '.ai/tmp/playwright-local',
  use: {
    baseURL: 'http://localhost:4321',
    viewport: { width: 1440, height: 1000 },
  },
  webServer: {
    command: 'pnpm run dev -- --host 127.0.0.1 --port 4321',
    port: 4321,
    reuseExistingServer: true,
  },
})

param([string]$CacheRoot, [string]$Through)

$ErrorActionPreference = 'Stop'

function Invoke-HeadlessRzk([string]$Exe, [string]$Arguments, [string]$WorkingDirectory) {
  $psi = [System.Diagnostics.ProcessStartInfo]::new()
  $psi.FileName = $Exe
  $psi.Arguments = $Arguments
  $psi.WorkingDirectory = $WorkingDirectory
  $psi.UseShellExecute = $false
  $psi.CreateNoWindow = $true
  $psi.RedirectStandardOutput = $true
  $psi.RedirectStandardError = $true
  $process = [System.Diagnostics.Process]::new()
  $process.StartInfo = $psi
  if (-not $process.Start()) { throw 'Failed to start Rzk' }
  $stdout = $process.StandardOutput.ReadToEnd()
  $stderr = $process.StandardError.ReadToEnd()
  $process.WaitForExit()
  [PSCustomObject]@{ ExitCode = $process.ExitCode; Stdout = $stdout; Stderr = $stderr }
}

$commit = '52a441cc4aaa03f3fe94ee94f70bb2874e26a6a2'
$archiveSha256 = 'b396523107ce51d24fb8e248c6f8409f2e1efd402854843791356d29a07566a8'
$url = "https://github.com/rzk-lang/sHoTT/archive/$commit.tar.gz"
if ([string]::IsNullOrWhiteSpace($CacheRoot)) {
  $localAppData = [Environment]::GetFolderPath('LocalApplicationData')
  if ([string]::IsNullOrWhiteSpace($localAppData)) { $localAppData = [System.IO.Path]::GetTempPath() }
  $CacheRoot = Join-Path $localAppData 'Narada/cache/rzk-shott'
}
$cacheRoot = $CacheRoot
$cacheDir = Join-Path $cacheRoot "$commit-$archiveSha256"
$project = Join-Path $cacheDir 'project'
$manifestPath = Join-Path $cacheDir 'complete.json'
$lockPath = Join-Path $cacheRoot "$commit-$archiveSha256.lock"
New-Item -ItemType Directory -Path $cacheRoot -Force | Out-Null
$lock = [System.IO.File]::Open($lockPath, 'OpenOrCreate', 'ReadWrite', 'None')
$clock = [System.Diagnostics.Stopwatch]::StartNew()
$cacheStatus = 'warm'

try {
  $cacheValid = $false
  if ((Test-Path $manifestPath) -and (Test-Path (Join-Path $project 'rzk.yaml'))) {
    try {
      $manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json
      $cacheValid = $manifest.commit -eq $commit -and
        $manifest.archive_sha256 -eq $archiveSha256 -and
        $manifest.schema -eq 'marici.rzk-shott-cache.v1'
    } catch { $cacheValid = $false }
  }

  if (-not $cacheValid) {
    $cacheStatus = 'cold'
    if (Test-Path $cacheDir) { Remove-Item -Recurse -Force $cacheDir }
    $build = Join-Path $cacheRoot "$commit-$archiveSha256.build-$PID"
    if (Test-Path $build) { Remove-Item -Recurse -Force $build }
    $extract = Join-Path $build 'source'
    $archive = Join-Path $build 'shott.tar.gz'
    New-Item -ItemType Directory -Path $extract -Force | Out-Null
    Invoke-WebRequest -Uri $url -OutFile $archive
    $actual = (Get-FileHash -Algorithm SHA256 $archive).Hash.ToLowerInvariant()
    if ($actual -ne $archiveSha256) { throw "archive digest mismatch: $actual" }
    $archiveStream = [System.IO.File]::OpenRead($archive)
    $gzipStream = [System.IO.Compression.GZipStream]::new($archiveStream, [System.IO.Compression.CompressionMode]::Decompress)
    try { [System.Formats.Tar.TarFile]::ExtractToDirectory($gzipStream, $extract, $true) }
    finally { $gzipStream.Dispose(); $archiveStream.Dispose() }
    $extractedProject = Get-ChildItem -Directory $extract | Select-Object -First 1
    New-Item -ItemType Directory -Path $cacheDir -Force | Out-Null
    Move-Item $extractedProject.FullName $project
    New-Item -ItemType Directory -Path (Join-Path $project 'src/marici') -Force | Out-Null
    Add-Content (Join-Path $project 'rzk.yaml') "`n  - src/marici/**/*.rzk.md"
    [ordered]@{
      schema = 'marici.rzk-shott-cache.v1'
      commit = $commit
      archive_sha256 = $archiveSha256
      prepared_at = [DateTimeOffset]::UtcNow.ToString('o')
    } | ConvertTo-Json | Set-Content -Encoding utf8 $manifestPath
    Remove-Item -Recurse -Force $build
  }
  $prepareMs = $clock.ElapsedMilliseconds

  $staged = Join-Path $project 'src/marici'
  Remove-Item (Join-Path $staged '*.rzk.md') -Force -ErrorAction SilentlyContinue
  $sourceFiles = @(Get-ChildItem (Join-Path $PSScriptRoot '*.rzk.md') | Sort-Object Name)
  $scope = 'full'
  if (-not [string]::IsNullOrWhiteSpace($Through)) {
    $throughName = [System.IO.Path]::GetFileName($Through)
    $index = [Array]::FindIndex($sourceFiles, [Predicate[object]]{ param($file) $file.Name -eq $throughName })
    if ($index -lt 0) { throw "Rzk prefix endpoint not found: $Through" }
    $sourceFiles = @($sourceFiles[0..$index])
    $scope = "prefix:$throughName"
  }
  Copy-Item $sourceFiles.FullName $staged
  $stageMs = $clock.ElapsedMilliseconds - $prepareMs

  $rzkCommand = Get-Command rzk -ErrorAction SilentlyContinue
  $rzkExecutable = if ($null -ne $rzkCommand) { $rzkCommand.Source } else { Join-Path $HOME '.local/bin/rzk.exe' }
  if (-not (Test-Path $rzkExecutable)) { throw 'Rzk executable not found' }
  $versionResult = Invoke-HeadlessRzk $rzkExecutable 'version' $project
  if ($versionResult.ExitCode -ne 0) { throw "Rzk version failed: $($versionResult.Stderr)" }
  if ($versionResult.Stdout.Trim() -ne '0.11.3') { throw "Rzk version mismatch: $($versionResult.Stdout.Trim())" }

  $typecheckStart = $clock.ElapsedMilliseconds
  $outputDir = Join-Path ([System.IO.Path]::GetTempPath()) "marici-rzk-output-$PID"
  New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
  $typecheckStdout = Join-Path $outputDir 'stdout.txt'
  $typecheckStderr = Join-Path $outputDir 'stderr.txt'
  try {
    $typecheck = Start-Process -FilePath $rzkExecutable -ArgumentList 'typecheck' -WorkingDirectory $project -NoNewWindow -Wait -PassThru -RedirectStandardOutput $typecheckStdout -RedirectStandardError $typecheckStderr
    $typecheckMs = $clock.ElapsedMilliseconds - $typecheckStart
    if ($typecheck.ExitCode -ne 0) {
      Get-Content $typecheckStdout -ErrorAction SilentlyContinue | Select-Object -Last 40 | ForEach-Object { Write-Output $_ }
      Get-Content $typecheckStderr -ErrorAction SilentlyContinue | Select-Object -Last 40 | ForEach-Object { Write-Output $_ }
      throw "Rzk failed: $($typecheck.ExitCode)"
    }
  } finally {
    Remove-Item -Recurse -Force $outputDir -ErrorAction SilentlyContinue
  }
  Write-Output "MARICI_FACTN_RZK_CHECK_OK scope=$scope files=$($sourceFiles.Count) cache=$cacheStatus prepare_ms=$prepareMs stage_ms=$stageMs typecheck_ms=$typecheckMs archive_sha256=$archiveSha256"
} finally {
  $lock.Dispose()
}

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
$work = Join-Path ([System.IO.Path]::GetTempPath()) "marici-factn-rzk-check-$commit-$PID"
$archive = Join-Path $work 'shott.tar.gz'
$extract = Join-Path $work 'source'
if (Test-Path $work) { Remove-Item -Recurse -Force $work }
New-Item -ItemType Directory -Path $extract -Force | Out-Null
Invoke-WebRequest -Uri $url -OutFile $archive
$actual = (Get-FileHash -Algorithm SHA256 $archive).Hash.ToLowerInvariant()
if ($actual -ne $archiveSha256) { throw "archive digest mismatch: $actual" }
$archiveStream = [System.IO.File]::OpenRead($archive)
$gzipStream = [System.IO.Compression.GZipStream]::new($archiveStream,[System.IO.Compression.CompressionMode]::Decompress)
try { [System.Formats.Tar.TarFile]::ExtractToDirectory($gzipStream,$extract,$true) }
finally { $gzipStream.Dispose(); $archiveStream.Dispose() }
$project = Get-ChildItem -Directory $extract | Select-Object -First 1
$staged = Join-Path $project.FullName 'src/marici'
New-Item -ItemType Directory -Path $staged -Force | Out-Null
Copy-Item (Join-Path $PSScriptRoot '*.rzk.md') $staged
Add-Content (Join-Path $project.FullName 'rzk.yaml') "`n  - src/marici/**/*.rzk.md"
$rzkCommand = Get-Command rzk -ErrorAction SilentlyContinue
$rzkExecutable = if ($null -ne $rzkCommand) { $rzkCommand.Source } else { Join-Path $HOME '.local/bin/rzk.exe' }
if (-not (Test-Path $rzkExecutable)) { throw 'Rzk executable not found' }
$versionResult = Invoke-HeadlessRzk $rzkExecutable 'version' $project.FullName
if ($versionResult.ExitCode -ne 0) { throw "Rzk version failed: $($versionResult.Stderr)" }
if ($versionResult.Stdout.Trim() -ne '0.11.3') { throw "Rzk version mismatch: $($versionResult.Stdout.Trim())" }
$typecheckStdout = Join-Path $work 'rzk-typecheck-stdout.txt'
$typecheckStderr = Join-Path $work 'rzk-typecheck-stderr.txt'
$typecheck = Start-Process -FilePath $rzkExecutable -ArgumentList 'typecheck' -WorkingDirectory $project.FullName -NoNewWindow -Wait -PassThru -RedirectStandardOutput $typecheckStdout -RedirectStandardError $typecheckStderr
if ($typecheck.ExitCode -ne 0) {
  Get-Content $typecheckStdout -ErrorAction SilentlyContinue | Select-Object -Last 40 | ForEach-Object { Write-Output $_ }
  Get-Content $typecheckStderr -ErrorAction SilentlyContinue | Select-Object -Last 40 | ForEach-Object { Write-Output $_ }
  throw "Rzk failed: $($typecheck.ExitCode)"
}
Write-Output "MARICI_FACTN_RZK_CHECK_OK archive_sha256=$actual"

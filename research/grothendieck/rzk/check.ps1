$ErrorActionPreference = 'Stop'

$commit = '52a441cc4aaa03f3fe94ee94f70bb2874e26a6a2'
$archiveSha256 = 'b396523107ce51d24fb8e248c6f8409f2e1efd402854843791356d29a07566a8'
$url = "https://github.com/rzk-lang/sHoTT/archive/$commit.tar.gz"
$work = Join-Path ([System.IO.Path]::GetTempPath()) "marici-rzk-check-$commit"
$archive = Join-Path $work 'shott.tar.gz'
$extract = Join-Path $work 'source'

if (Test-Path $work) {
    Remove-Item -Recurse -Force $work
}
New-Item -ItemType Directory -Path $extract -Force | Out-Null

Invoke-WebRequest -Uri $url -OutFile $archive
$actualArchiveSha256 = (Get-FileHash -Algorithm SHA256 $archive).Hash.ToLowerInvariant()
if ($actualArchiveSha256 -ne $archiveSha256) {
    throw "sHoTT archive digest mismatch: expected $archiveSha256, got $actualArchiveSha256"
}

$archiveStream = [System.IO.File]::OpenRead($archive)
$gzipStream = [System.IO.Compression.GZipStream]::new(
    $archiveStream,
    [System.IO.Compression.CompressionMode]::Decompress)
try {
    [System.Formats.Tar.TarFile]::ExtractToDirectory($gzipStream, $extract, $true)
}
finally {
    $gzipStream.Dispose()
    $archiveStream.Dispose()
}

$project = Get-ChildItem -Directory $extract | Select-Object -First 1
if ($null -eq $project) {
    throw 'sHoTT archive contained no project directory'
}

$mariciSource = Join-Path $PSScriptRoot 'src'
$stagedSource = Join-Path $project.FullName 'src/marici'
New-Item -ItemType Directory -Path $stagedSource -Force | Out-Null
Copy-Item (Join-Path $mariciSource '*.rzk.md') $stagedSource
Add-Content (Join-Path $project.FullName 'rzk.yaml') "`n  - src/marici/**/*.rzk.md"

$rzkCommand = Get-Command rzk -ErrorAction SilentlyContinue
$rzkExecutable = if ($null -ne $rzkCommand) {
    $rzkCommand.Source
}
else {
    Join-Path $HOME '.local/bin/rzk.exe'
}
if (-not (Test-Path $rzkExecutable)) {
    throw "Rzk executable not found on PATH or at $rzkExecutable"
}
$rzkVersion = & $rzkExecutable version
if ($null -eq $rzkVersion) {
    throw 'rzk version returned no output'
}
if ($rzkVersion.Trim() -ne '0.11.3') {
    throw "expected Rzk 0.11.3, got $rzkVersion"
}

Push-Location $project.FullName
try {
    $typecheckOutput = @(& $rzkExecutable typecheck 2>&1)
    $typecheckExitCode = $LASTEXITCODE
    if ($typecheckExitCode -ne 0) {
        $failureTail = $typecheckOutput | Select-Object -Last 25
        $failureTail | ForEach-Object { Write-Output $_ }
        throw "rzk typecheck failed with exit code $typecheckExitCode; showing last $($failureTail.Count) lines"
    }
}
finally {
    Pop-Location
}

Write-Output "MARICI_RZK_CHECK_OK rzk=$($rzkVersion.Trim()) shott=$commit archive_sha256=$actualArchiveSha256 modules=$((Get-ChildItem (Join-Path $mariciSource '*.rzk.md')).Count)"

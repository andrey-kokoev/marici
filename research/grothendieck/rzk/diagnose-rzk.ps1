$ErrorActionPreference = 'Stop'
Write-Output ("RZK_ENV home={0} userprofile={1}" -f $HOME, $env:USERPROFILE)
$command = Get-Command rzk -ErrorAction SilentlyContinue
$candidates = @(
    if ($null -ne $command) { $command.Source },
    (Join-Path $env:USERPROFILE '.cargo/bin/rzk.exe'),
    (Join-Path $env:USERPROFILE '.local/bin/rzk.exe'),
    (Join-Path $HOME '.cargo/bin/rzk.exe'),
    (Join-Path $HOME '.local/bin/rzk.exe')
) | Where-Object { $_ } | Select-Object -Unique
foreach ($candidate in $candidates) {
    Write-Output ("RZK_CANDIDATE path={0} exists={1}" -f $candidate, (Test-Path $candidate))
    if (Test-Path $candidate) {
        $output = & $candidate version 2>&1
        $exitCode = $LASTEXITCODE
        Write-Output ("RZK_VERSION path={0} code={1} lines={2}" -f $candidate, $exitCode, @($output).Count)
        $output | ForEach-Object { Write-Output ("RZK_VERSION_OUTPUT {0}" -f $_) }
        if ($exitCode -eq 0 -and @($output).Count -gt 0) { exit 0 }
    }
}
Write-Output 'RZK_EXECUTABLE_NOT_LIVE'
exit 3

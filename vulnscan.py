import subprocess

def run_nmap_command(args, description):
    print(f"\n--- {description} ---")
    result = subprocess.run(
        args,
        capture_output=True,
        text=True
    )
    print(result.stdout)

def scan_ports(target):
    # Basic scan
    run_nmap_command(["nmap", "-Pn", target], "Basic Scan")
    # Service/version detection
    run_nmap_command(["nmap", "-sV", target], "Service/Version Detection")
    # OS detection
    run_nmap_command(["nmap", "-O", target], "OS Detection")
    # Top 10 ports
    run_nmap_command(["nmap", "--top-ports", "10", target], "Top 10 Ports Scan")
    # Vulnerability scan (NSE vuln category)
    run_nmap_command(["nmap", "--script", "vuln", target], "Vulnerability Scan")
    # SMB vulnerabilities
    run_nmap_command(["nmap", "--script", "smb-vuln*", target], "SMB Vulnerability Scan")
    # HTTP vulnerabilities
    run_nmap_command(["nmap", "--script", "http-vuln*", target], "HTTP Vulnerability Scan")
    # Heartbleed vulnerability
    run_nmap_command(["nmap", "--script", "ssl-heartbleed", target], "SSL Heartbleed Vulnerability Scan")

if __name__ == "__main__":
    target_host = "ns1.dns-parking.com"
    scan_ports(target_host)
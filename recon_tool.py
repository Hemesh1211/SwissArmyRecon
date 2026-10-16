import socket
import requests
import dns.resolver
import argparse
import threading
from colorama import Fore, Style, init

init(autoreset=True)

SUBDOMAINS = ['www', 'dev', 'staging', 'vpn', 'mail', 'api', 'admin', 'test']
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 8080]
open_ports_found = []

def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"{Fore.BLUE}[INFO] Target {target} resolved to {ip}")
        return ip
    except socket.gaierror:
        print(f"{Fore.RED}[ERROR] Could not resolve hostname.")
        return None

def run_dns_enum(target):
    print(f"\n{Fore.CYAN}--- Phase 1: DNS Enumeration ---")
    for sub in SUBDOMAINS:
        domain = f"{sub}.{target}"
        try:
            dns.resolver.resolve(domain, 'A')
            print(f"{Fore.GREEN}[+] Found: {domain}")
        except:
            pass

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        s.send(b'GET / HTTP/1.1\r\n\r\n')
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner if banner else "No banner"
    except:
        return "Unable to grab banner"

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((ip, port)) == 0:
            banner = grab_banner(ip, port)
            print(f"{Fore.GREEN}[+] Port {port} OPEN | Service: {banner}")
            open_ports_found.append(port)
        s.close()
    except:
        pass

def run_port_scan(ip):
    print(f"\n{Fore.CYAN}--- Phase 2: Port Scanning ---")
    threads = []
    for port in COMMON_PORTS:
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def run_http_audit(target):
    print(f"\n{Fore.CYAN}--- Phase 3: HTTP Header Analysis ---")
    if 80 not in open_ports_found and 443 not in open_ports_found:
        print(f"{Fore.YELLOW}[!] No web ports found.")
        return
    try:
        response = requests.get(f"http://{target}", timeout=5)
        security_checks = {"X-Frame-Options": "Clickjacking", "Content-Security-Policy": "XSS"}
        for header, reason in security_checks.items():
            if header in response.headers:
                print(f"{Fore.GREEN}[+] {header} present.")
            else:
                print(f"{Fore.RED}[-] {header} MISSING -> {reason}")
    except:
        print(f"{Fore.RED}[ERROR] Connection failed.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", required=True)
    args = parser.parse_args()
    target_ip = resolve_target(args.target)
    if target_ip:
        run_dns_enum(args.target)
        run_port_scan(target_ip)
        run_http_audit(args.target)

if __name__ == "__main__":
    main()

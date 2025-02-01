import asyncio
import argparse
import socket
import random
import json
import csv
import aiohttp
from tqdm import tqdm
from colorama import Fore, Style, init
import pyfiglet
from flask import Flask, render_template_string, jsonify

# Initialize colorama for colored output
init(autoreset=True)

# Configuration Constants
PORT_SCAN_TIMEOUT = 6  # Timeout in seconds for each port scan
SUBDOMAIN_API = "https://crt.sh/?q={}&output=json"  # crt.sh for subdomain enumeration

app = Flask(__name__)
scan_results = []

def print_banner():
    """Prints a stylish banner at startup."""
    banner = pyfiglet.figlet_format("Subsaurus Rex", font="slant")
    print(Fore.CYAN + banner)
    print(f"{Fore.YELLOW}🔍 Caselka's Multi-Host Async Dino Scanner with Subdomains & Web Dashboard")
    print(f"{Fore.GREEN}🚀 Developed for efficient and stealthy dino scanning!\n{Style.RESET_ALL}")

async def grab_banner(reader, writer):
    """Attempts to grab the banner from an open port."""
    try:
        writer.write(b"\r\n")
        await writer.drain()
        banner = await reader.read(1024)  # Read up to 1024 bytes
        return banner.decode(errors="ignore").strip() if banner else "Unknown Service"
    except:
        return "Unknown Service"

async def scan_port(host, port, semaphore, stealth_mode):
    """Asynchronously scans a port with timeout and grabs service banner if open."""
    async with semaphore:
        try:
            async with asyncio.timeout(PORT_SCAN_TIMEOUT):
                reader, writer = await asyncio.open_connection(host, port)
                
                service = await grab_banner(reader, writer)

                writer.close()
                await writer.wait_closed()
                return {"host": host, "port": port, "service": service}
        except (asyncio.TimeoutError, OSError):
            return None  # Port is closed or timed out
        
        finally:
            if stealth_mode:
                delay = random.uniform(0.5, 3.0)
                await asyncio.sleep(delay)

async def scan_ports(host, start_port, end_port, max_concurrent_tasks, stealth_mode):
    """Scans multiple ports asynchronously while respecting timeout and stealth mode."""
    semaphore = asyncio.Semaphore(max_concurrent_tasks)
    tasks = [scan_port(host, port, semaphore, stealth_mode) for port in range(start_port, end_port + 1)]

    results = []
    for f in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc=f"🔎 Scanning {host}", unit="port"):
        scan_result = await f
        if scan_result:
            results.append(scan_result)

    return results

async def find_subdomains(domain):
    """Finds subdomains using crt.sh API."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(SUBDOMAIN_API.format(domain)) as response:
                if response.status == 200:
                    data = await response.json()
                    subdomains = {entry["name_value"] for entry in data}
                    return list(subdomains)
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to fetch subdomains: {e}{Style.RESET_ALL}")
        return []

def save_results_to_json(results, filename="scan_results.json"):
    """Saves scan results to a JSON file."""
    with open(filename, "w") as json_file:
        json.dump(results, json_file, indent=4)
    print(f"\n📁 Results saved to {Fore.YELLOW}{filename}{Style.RESET_ALL}")

def save_results_to_csv(results, filename="scan_results.csv"):
    """Saves scan results to a CSV file."""
    with open(filename, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["host", "port", "service"])
        writer.writeheader()
        writer.writerows(results)
    print(f"\n📁 Results saved to {Fore.YELLOW}{filename}{Style.RESET_ALL}")

### **🔥 Web Dashboard with Restored HTML**
@app.route("/")
def dashboard():
    """Web dashboard to display scan results."""
    return render_template_string("""
    {{ html_content | safe }}
    """, html_content=open("dashboard.html").read(), results=scan_results)

@app.route("/api/scan-results")
def get_scan_results():
    """API endpoint to return scan results as JSON."""
    return jsonify({"results": scan_results}), 200

@app.route("/learning")
def learning_page():
    """Learning Resources Page."""
    return render_template_string("""
    <html>
    <head><title>Learning Resources</title></head>
    <body>
        <h1>Learning Resources</h1>
        <p>Here are some useful links for learning more about cybersecurity:</p>
        <ul>
            <li><a href="https://owasp.org/www-project-top-ten/">OWASP Top 10</a></li>
            <li><a href="https://nmap.org/book/man.html">Nmap Documentation</a></li>
            <li><a href="https://portswigger.net/web-security">PortSwigger Web Security Academy</a></li>
        </ul>
        <a href="/">Back to Scanner</a>
    </body>
    </html>
    """), 200

def run_web_dashboard():
    """Runs Flask Web Server."""
    print("\n🌍 Web Dashboard running at http://127.0.0.1:5000/")
    app.run(debug=True, use_reloader=False)

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="Advanced Asynchronous Port Scanner")
    parser.add_argument("hosts", type=str, nargs="+", help="Target hosts to scan (supports multiple)")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")
    parser.add_argument("--concurrency", type=int, default=500, help="Number of concurrent scans (default: 500)")
    parser.add_argument("--stealth", action="store_true", help="Enable stealth mode (randomized delays to avoid detection)")
    parser.add_argument("--subdomains", action="store_true", help="Find and scan subdomains of each host")
    parser.add_argument("--json", action="store_true", help="Save results as JSON")
    parser.add_argument("--csv", action="store_true", help="Save results as CSV")
    parser.add_argument("--web", action="store_true", help="Launch a web dashboard to display results")

    args = parser.parse_args()

    global scan_results
    scan_results = []

    for host in args.hosts:
        print(f"\n🔍 Scanning {Fore.CYAN}{host}{Style.RESET_ALL} from port {args.start_port} to {args.end_port}...\n")

        open_ports = asyncio.run(scan_ports(host, args.start_port, args.end_port, args.concurrency, args.stealth))
        scan_results.extend(open_ports)

        if args.subdomains:
            subdomains = asyncio.run(find_subdomains(host))
            print(f"\n🔎 Found {len(subdomains)} subdomains for {host}: {subdomains}\n")

            for subdomain in subdomains:
                subdomain_results = asyncio.run(scan_ports(subdomain, args.start_port, args.end_port, args.concurrency, args.stealth))
                scan_results.extend(subdomain_results)

    if args.web:
        run_web_dashboard()
    elif scan_results:
        if args.json:
            save_results_to_json(scan_results)
        if args.csv:
            save_results_to_csv(scan_results)

if __name__ == "__main__":
    main()

import time
import dns.resolver

# The DNS servers you want to test
servers = {
    "Your Current": None, # Uses your system/Teltonika default
    "Cloudflare": "1.1.1.1",
    "Google": "8.8.8.8",
    "AdGuard (Ads)": "94.140.14.14",
    "Quad9 (Secure)": "9.9.9.9"
}

domain = "google.com"

def test_dns(name, ip):
    resolver = dns.resolver.Resolver()
    if ip:
        resolver.nameservers = [ip]
    
    start = time.perf_counter()
    # Add this line to your script's loop
    
    try:
        resolver.resolve(domain, "A")
        end = time.perf_counter()
        return round((end - start) * 1000, 2)
    except Exception as e:
        return "Fail"

print(f"Benchmarking DNS response for {domain}...")
print(f"Current DNS Server: {dns.resolver.Resolver().nameservers}")
for name, ip in servers.items():
    result = test_dns(name, ip)
    print(f"{name:15}: {result} ms")

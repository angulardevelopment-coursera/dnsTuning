## dnsTuning: Solving the LTE DNS Bottleneck

# The Problem
While setting up a remote workshop using a Teltonika RUT360 (LTE Gateway), I encountered significant network "stuttering." Benchmarking revealed that DNS resolution times were spiking as high as 2000ms.
The root cause was Carrier-Grade NAT (CGNAT) DNS Injection. The mobile provider was forcing non-functional DNS resolvers into the stack, causing Windows to hang while waiting for timeouts.
# The Solution
This tool is a Python-based utility designed to benchmark multiple DNS providers simultaneously. It identifies "Ghost" DNS entries and verifies if virtual network layers (like Tailscale) are successfully shielding the OS from high-latency carrier resolvers.
# Key Features
•	Multi-Provider Benchmarking: Compares system defaults against industry leaders (Cloudflare, Google, Quad9, AdGuard).
•	Resolver Transparency: Identifies exactly which IPs are responding (crucial for spotting "injected" ISP resolvers).
•	Performance Metrics: Measures raw response time in milliseconds to pinpoint bottlenecks.
•	Tailscale Integration Check: Verifies that the 100.100.100.100 virtual resolver is properly prioritized.
# Getting Started
Bash
# Clone the repository
git clone https://github.com/your-username/dnsTuning.git

# Install dependencies
pip install dnspython

# Run the benchmark
python dnsCheck.py
# Case Study: Results

Provider	Before Tuning	After Tuning
System Default	2049.48 ms	94.88 ms
Quad9 (Secure)	250.00 ms	27.01 ms

Optimization Note: The 95% reduction in latency was achieved by forcing a Global Nameserver override in Tailscale, bypassing the LTE carrier's faulty injection.



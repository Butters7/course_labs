<div align="center">
<h1><a id="intro">Лабораторная работа №6</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Давыдов Е.А.-8b9aff" alt="Contributor Badge"></a></div>

- [x] 1. Необходимо установить `Docker Engine` для Linux

```
bttrs@bttrs:~/Riski/course_labs/labs/lab06$ docker pull docker/docker-bench-security
Using default tag: latest
latest: Pulling from docker/docker-bench-security
378ed37ea5ff: Pull complete 
cd784148e348: Pull complete 
48fe0d48816d: Pull complete 
164e5e0f48c5: Pull complete 
Digest: sha256:ddbdf4f86af4405da4a8a7b7cc62bb63bfeb75e85bf22d2ece70c204d7cfabb8
Status: Downloaded newer image for docker/docker-bench-security:latest
docker.io/docker/docker-bench-security:latest
```

- [x] 2. Проверьте работу `докера` и сделать скрипт audit.sh исполняемым

```
bttrs@bttrs:~/Riski/course_labs/labs/lab06$ sudo systemctl status docker
[sudo] password for bttrs: 
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2025-12-21 17:46:17 MSK; 3h 45min ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 835 (dockerd)
      Tasks: 13
     Memory: 61.1M
        CPU: 1min 14.026s
     CGroup: /system.slice/docker.service
             └─835 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

bttrs@bttrs:~/Riski/course_labs/labs/lab06$ ls -lh audit.sh 
-rwxrwxr-x 1 bttrs bttrs 9,5K дек 14 21:56 audit.sh
```

- [x] 3. Развернуть уязвимое приложение как отдельные стенды

```
bttrs@bttrs:~/Riski/course_labs/labs/lab06$ docker compose up -d
WARN[0000] /home/bttrs/Riski/course_labs/labs/lab06/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] up 33/34
 ✔ Image nginx:alpine Pulled                                                                                                                                                                            26.2s 
 ✔ Image postgres:16-alpine Pulled                                                                                                                                                                      45.3s 
 ✔ Image python:3.11-alpine Pulled                                                                                                                                                                      25.8s 
 ✔ Network lab06_default Created                                                                                                                                                                         3.2s 
 ✔ Container insecure-db Created                                                                                                                                                                         1.0s 
 ✔ Container vulnerable-app Created                                                                                                                                                                      0.4s 
 ✔ Container vulnerable-nginx Created                                                                                                                                                                    0.2s 
bttrs@bttrs:~/Riski/course_labs/labs/lab06$ docker compose -f vulnerable-app.yml up -d
WARN[0000] /home/bttrs/Riski/course_labs/labs/lab06/vulnerable-app.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] up 12/12
 ✔ Image alpine:latest Pulled                                                                                                                                                                           11.1s 
[+] up 15/15nx:latest Pulled                                                                                                                                                                            17.4s 
 ✔ Image alpine:latest Pulled                                                                                                                                                                           11.1s 
 ✔ Image nginx:latest Pulled                                                                                                                                                                            17.4s 
 ✔ Container debug-shell Created                                                                                                                                                                         0.7s 
 ✔ Container vulnerable-nginx Recreated                                                                                                                                                                  0.9s 
 ! debug-shell Published ports are discarded when using host network mode
```

- [x] 4. Запустите скрипт из `venv` и проанализируйте то, что вывело на терминале и что вывело при конвертировании

```
(venv) bttrs@bttrs:~/Riski/course_labs/labs/lab06$ ./audit.sh
Starting Docker CIS & Image Security Audit
==========================================
Detected platform: Linux
Using docker-bench-security image: docker/docker-bench-security:latest
Reports will be saved to: ./audit_reports/

Running Trivy scan for docker/docker-bench-security:latest...
2025-12-21T22:04:09+03:00       INFO    [vuln] Vulnerability scanning is enabled
2025-12-21T22:04:09+03:00       INFO    [secret] Secret scanning is enabled
2025-12-21T22:04:09+03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-21T22:04:09+03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-21T22:04:09+03:00       INFO    Detected OS     family="alpine" version="3.8.2"
2025-12-21T22:04:09+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.8" repository="3.8" pkg_num=25
2025-12-21T22:04:09+03:00       INFO    Number of language-specific files       num=0
2025-12-21T22:04:09+03:00       WARN    This OS version is no longer supported by the distribution      family="alpine" version="3.8.2"
2025-12-21T22:04:09+03:00       WARN    The vulnerability detection may be insufficient because security updates are not provided
Saved to: ./audit_reports/json/docker-bench-security-trivy.json

Scanning lab images for vulnerabilities...

=== Trivy scan for nginx:alpine ===
2025-12-21T22:04:09+03:00       INFO    [vuln] Vulnerability scanning is enabled
2025-12-21T22:04:09+03:00       INFO    [secret] Secret scanning is enabled
2025-12-21T22:04:09+03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-21T22:04:09+03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-21T22:04:09+03:00       INFO    Detected OS     family="alpine" version="3.23.2"
2025-12-21T22:04:09+03:00       WARN    This OS version is not on the EOL list  family="alpine" version="3.23"
2025-12-21T22:04:09+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.23" repository="3.23" pkg_num=71
2025-12-21T22:04:09+03:00       INFO    Number of language-specific files       num=0
Saved to: ./audit_reports/json/nginx-alpine-trivy.json

=== Trivy scan for python:3.11-alpine ===
2025-12-21T22:04:09+03:00       INFO    [vuln] Vulnerability scanning is enabled
2025-12-21T22:04:09+03:00       INFO    [secret] Secret scanning is enabled
2025-12-21T22:04:09+03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-21T22:04:09+03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-21T22:04:09+03:00       INFO    Detected OS     family="alpine" version="3.23.2"
2025-12-21T22:04:09+03:00       WARN    This OS version is not on the EOL list  family="alpine" version="3.23"
2025-12-21T22:04:09+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.23" repository="3.23" pkg_num=38
2025-12-21T22:04:09+03:00       INFO    Number of language-specific files       num=1
2025-12-21T22:04:09+03:00       INFO    [python-pkg] Detecting vulnerabilities...
Saved to: ./audit_reports/json/python-3.11-alpine-trivy.json

=== Trivy scan for postgres:16-alpine ===
2025-12-21T22:04:09+03:00       INFO    [vuln] Vulnerability scanning is enabled
2025-12-21T22:04:09+03:00       INFO    [secret] Secret scanning is enabled
2025-12-21T22:04:09+03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-21T22:04:09+03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-21T22:04:09+03:00       INFO    Detected OS     family="alpine" version="3.23.2"
2025-12-21T22:04:09+03:00       WARN    This OS version is not on the EOL list  family="alpine" version="3.23"
2025-12-21T22:04:09+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.23" repository="3.23" pkg_num=45
2025-12-21T22:04:09+03:00       INFO    Number of language-specific files       num=1
2025-12-21T22:04:09+03:00       INFO    [gobinary] Detecting vulnerabilities...
2025-12-21T22:04:09+03:00       WARN    Using severities from other vendors for some vulnerabilities. Read https://trivy.dev/docs/v0.68/guide/scanner/vulnerability#severity-selection for details.
Saved to: ./audit_reports/json/postgres-16-alpine-trivy.json

Linux host detected – running CIS Docker Benchmark

Running Docker Bench Security (CIS host audit)

# --------------------------------------------------------------------------------------------
# Docker Bench for Security v1.6.0
#
# Docker, Inc. (c) 2015-2025
#
# Checks for dozens of common best-practices around deploying Docker containers in production.
# Based on the CIS Docker Benchmark 1.6.0.
# --------------------------------------------------------------------------------------------

Initializing 2025-12-21T22:04:10+03:00


Section A - Check results
WARNING: This output is designed for human readability. For machine-readable output, please use --format.
error: no such object: 13.1MB
error: no such object: 203MB
error: no such object: 69.2MB
error: no such object: 208MB
error: no such object: 211MB
error: no such object: 238MB
error: no such object: 203MB
error: no such object: 208MB
error: no such object: 211MB
error: no such object: 82MB
error: no such object: 228MB
error: no such object: 395MB
error: no such object: 84.4MB
error: no such object: 119MB

[INFO] 1 - Host Configuration
[INFO] 1.1 - Linux Hosts Specific Configuration
[WARN] 1.1.1 - Ensure a separate partition for containers has been created (Automated)
[INFO] 1.1.2 - Ensure only trusted users are allowed to control Docker daemon (Automated)
[INFO]       * Users: bttrs
[WARN] 1.1.3 - Ensure auditing is configured for the Docker daemon (Automated)
[WARN] 1.1.4 - Ensure auditing is configured for Docker files and directories -/run/containerd (Automated)
[WARN] 1.1.5 - Ensure auditing is configured for Docker files and directories - /var/lib/docker (Automated)
[WARN] 1.1.6 - Ensure auditing is configured for Docker files and directories - /etc/docker (Automated)
[WARN] 1.1.7 - Ensure auditing is configured for Docker files and directories - docker.service (Automated)
[INFO] 1.1.8 - Ensure auditing is configured for Docker files and directories - containerd.sock (Automated)
[INFO]        * File not found
[WARN] 1.1.9 - Ensure auditing is configured for Docker files and directories - docker.socket (Automated)
[WARN] 1.1.10 - Ensure auditing is configured for Docker files and directories - /etc/default/docker (Automated)
[WARN] 1.1.11 - Ensure auditing is configured for Dockerfiles and directories - /etc/docker/daemon.json (Automated)
[WARN] 1.1.12 - 1.1.12 Ensure auditing is configured for Dockerfiles and directories - /etc/containerd/config.toml (Automated)
[INFO] 1.1.13 - Ensure auditing is configured for Docker files and directories - /etc/sysconfig/docker (Automated)
[INFO]        * File not found
[WARN] 1.1.14 - Ensure auditing is configured for Docker files and directories - /usr/bin/containerd (Automated)
[INFO] 1.1.15 - Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim (Automated)
[INFO]         * File not found
[INFO] 1.1.16 - Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim-runc-v1 (Automated)
[INFO]         * File not found
[WARN] 1.1.17 - Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim-runc-v2 (Automated)
[WARN] 1.1.18 - Ensure auditing is configured for Docker files and directories - /usr/bin/runc (Automated)
[INFO] 1.2 - General Configuration
[NOTE] 1.2.1 - Ensure the container host has been Hardened (Manual)
[PASS] 1.2.2 - Ensure that the version of Docker is up to date (Manual)
[INFO]        * Using 29.1.3 which is current
[INFO]        * Check with your operating system vendor for support and security maintenance for Docker

[INFO] 2 - Docker daemon configuration
[NOTE] 2.1 - Run the Docker daemon as a non-root user, if possible (Manual)
[WARN] 2.2 - Ensure network traffic is restricted between containers on the default bridge (Scored)
[PASS] 2.3 - Ensure the logging level is set to 'info' (Scored)
[PASS] 2.4 - Ensure Docker is allowed to make changes to iptables (Scored)
[PASS] 2.5 - Ensure insecure registries are not used (Scored)
[PASS] 2.6 - Ensure aufs storage driver is not used (Scored)
[INFO] 2.7 - Ensure TLS authentication for Docker daemon is configured (Scored)
[INFO]      * Docker daemon not listening on TCP
[INFO] 2.8 - Ensure the default ulimit is configured appropriately (Manual)
[INFO]      * Default ulimit doesn't appear to be set
[WARN] 2.9 - Enable user namespace support (Scored)
[PASS] 2.10 - Ensure the default cgroup usage has been confirmed (Scored)
[PASS] 2.11 - Ensure base device size is not changed until needed (Scored)
[WARN] 2.12 - Ensure that authorization for Docker client commands is enabled (Scored)
[WARN] 2.13 - Ensure centralized and remote logging is configured (Scored)
[WARN] 2.14 - Ensure containers are restricted from acquiring new privileges (Scored)
[WARN] 2.15 - Ensure live restore is enabled (Scored)
[WARN] 2.16 - Ensure Userland Proxy is Disabled (Scored)
[INFO] 2.17 - Ensure that a daemon-wide custom seccomp profile is applied if appropriate (Manual)
[INFO] Ensure that experimental features are not implemented in production (Scored) (Deprecated)

[INFO] 3 - Docker daemon configuration files
[PASS] 3.1 - Ensure that the docker.service file ownership is set to root:root (Automated)
[PASS] 3.2 - Ensure that docker.service file permissions are appropriately set (Automated)
[PASS] 3.3 - Ensure that docker.socket file ownership is set to root:root (Automated)
[PASS] 3.4 - Ensure that docker.socket file permissions are set to 644 or more restrictive (Automated)
[PASS] 3.5 - Ensure that the /etc/docker directory ownership is set to root:root (Automated)
[PASS] 3.6 - Ensure that /etc/docker directory permissions are set to 755 or more restrictively (Automated)
[INFO] 3.7 - Ensure that registry certificate file ownership is set to root:root (Automated)
[INFO]      * Directory not found
[INFO] 3.8 - Ensure that registry certificate file permissions are set to 444 or more restrictively (Automated)
[INFO]      * Directory not found
[INFO] 3.9 - Ensure that TLS CA certificate file ownership is set to root:root (Automated)
[INFO]      * No TLS CA certificate found
[INFO] 3.10 - Ensure that TLS CA certificate file permissions are set to 444 or more restrictively (Automated)
[INFO]       * No TLS CA certificate found
[INFO] 3.11 - Ensure that Docker server certificate file ownership is set to root:root (Automated)
[INFO]       * No TLS Server certificate found
[INFO] 3.12 - Ensure that the Docker server certificate file permissions are set to 444 or more restrictively (Automated)
[INFO]       * No TLS Server certificate found
[INFO] 3.13 - Ensure that the Docker server certificate key file ownership is set to root:root (Automated)
[INFO]       * No TLS Key found
[INFO] 3.14 - Ensure that the Docker server certificate key file permissions are set to 400 (Automated)
[INFO]       * No TLS Key found
[PASS] 3.15 - Ensure that the Docker socket file ownership is set to root:docker (Automated)
[PASS] 3.16 - Ensure that the Docker socket file permissions are set to 660 or more restrictively (Automated)
[PASS] 3.17 - Ensure that the daemon.json file ownership is set to root:root (Automated)
[PASS] 3.18 - Ensure that daemon.json file permissions are set to 644 or more restrictive (Automated)
[PASS] 3.19 - Ensure that the /etc/default/docker file ownership is set to root:root (Automated)
[PASS] 3.20 - Ensure that the /etc/default/docker file permissions are set to 644 or more restrictively (Automated)
[INFO] 3.21 - Ensure that the /etc/sysconfig/docker file permissions are set to 644 or more restrictively (Automated)
[INFO]       * File not found
[INFO] 3.22 - Ensure that the /etc/sysconfig/docker file ownership is set to root:root (Automated)
[INFO]       * File not found
[PASS] 3.23 - Ensure that the Containerd socket file ownership is set to root:root (Automated)
[PASS] 3.24 - Ensure that the Containerd socket file permissions are set to 660 or more restrictively (Automated)

[INFO] 4 - Container Images and Build File
[PASS] 4.1 - Ensure that a user for the container has been created (Automated)
[NOTE] 4.2 - Ensure that containers use only trusted base images (Manual)
[NOTE] 4.3 - Ensure that unnecessary packages are not installed in the container (Manual)
[NOTE] 4.4 - Ensure images are scanned and rebuilt to include security patches (Manual)
[WARN] 4.5 - Ensure Content trust for Docker is Enabled (Automated)
[WARN] 4.6 - Ensure that HEALTHCHECK instructions have been added to container images (Automated)
[WARN]      * No Healthcheck found: [helloapp-client:latest]
[WARN]      * No Healthcheck found: [helloapp-server:latest]
[WARN]      * No Healthcheck found: [lab05-server:latest]
[WARN]      * No Healthcheck found: [lab05-client:latest]
[WARN]      * No Healthcheck found: [helloapp:latest]
[WARN]      * No Healthcheck found: [butters192/hello-appsec-world:latest]
[WARN]      * No Healthcheck found: [hellow-appsec-world:latest]
[WARN]      * No Healthcheck found: [nginx:alpine]
[WARN]      * No Healthcheck found: [python:3.11-alpine]
[WARN]      * No Healthcheck found: [postgres:16-alpine]
[WARN]      * No Healthcheck found: [alpine:latest]
[WARN]      * No Healthcheck found: [nginx:latest]
[WARN]      * No Healthcheck found: [ubuntu:latest]
[INFO] 4.7 - Ensure update instructions are not used alone in the Dockerfile (Manual)
[INFO]      * Update instruction found: [helloapp-client:latest]
[INFO]      * Update instruction found: [helloapp-server:latest]
[INFO]      * Update instruction found: [lab05-server:latest]
[INFO]      * Update instruction found: [lab05-client:latest]
[INFO]      * Update instruction found: [helloapp:latest]
[INFO]      * Update instruction found: [butters192/hello-appsec-world:latest]
[INFO]      * Update instruction found: [hellow-appsec-world:latest]
[NOTE] 4.8 - Ensure setuid and setgid permissions are removed (Manual)
[INFO] 4.9 - Ensure that COPY is used instead of ADD in Dockerfiles (Manual)
[INFO]      * ADD in image history: [ubuntu:latest]
[NOTE] 4.10 - Ensure secrets are not stored in Dockerfiles (Manual)
[NOTE] 4.11 - Ensure only verified packages are installed (Manual)
[NOTE] 4.12 - Ensure all signed artifacts are validated (Manual)

[INFO] 5 - Container Runtime
[PASS] 5.1 - Ensure swarm mode is not Enabled, if not needed (Automated)
[WARN] 5.2 - Ensure that, if applicable, an AppArmor Profile is enabled (Automated)
[WARN]      * No AppArmorProfile Found: vulnerable-web
[PASS] 5.3 - Ensure that, if applicable, SELinux security options are set (Automated)
[WARN] 5.4 - Ensure that Linux kernel capabilities are restricted within containers (Automated)
[WARN]      * Capabilities added: CapAdd=[ALL] to vulnerable-web
[WARN] 5.5 - Ensure that privileged containers are not used (Automated)
[WARN]      * Container running in Privileged mode: vulnerable-web
[WARN] 5.6 - Ensure sensitive host system directories are not mounted on containers (Automated)
[WARN]      * Sensitive directory / mounted in: vulnerable-web
[PASS] 5.7 - Ensure sshd is not run within containers (Automated)
[PASS] 5.8 - Ensure privileged ports are not mapped within containers (Automated)
[PASS] 5.9 - Ensure that only needed ports are open on the container (Manual)
[WARN] 5.10 - Ensure that the host's network namespace is not shared (Automated)
[WARN]      * Container running with networking mode 'host': vulnerable-web
[WARN] 5.11 - Ensure that the memory usage for containers is limited (Automated)
[WARN]       * Container running without memory restrictions: vulnerable-web
[WARN] 5.12 - Ensure that CPU priority is set appropriately on containers (Automated)
[WARN]       * Container running without CPU restrictions: vulnerable-web
[WARN] 5.13 - Ensure that the container's root filesystem is mounted as read only (Automated)
[WARN]       * Container running with root FS mounted R/W: vulnerable-web
[PASS] 5.14 - Ensure that incoming container traffic is bound to a specific host interface (Automated)
[PASS] 5.15 - Ensure that the 'on-failure' container restart policy is set to '5' (Automated)
[WARN] 5.16 - Ensure that the host's process namespace is not shared (Automated)
[WARN]       * Host PID namespace being shared with: vulnerable-web
[PASS] 5.17 - Ensure that the host's IPC namespace is not shared (Automated)
[PASS] 5.18 - Ensure that host devices are not directly exposed to containers (Manual)
[INFO] 5.19 - Ensure that the default ulimit is overwritten at runtime if needed (Manual)
[INFO]       * Container no default ulimit override: vulnerable-web
[PASS] 5.20 - Ensure mount propagation mode is not set to shared (Automated)
[PASS] 5.21 - Ensure that the host's UTS namespace is not shared (Automated)
[WARN] 5.22 - Ensure the default seccomp profile is not Disabled (Automated)
[WARN]       * Default seccomp profile disabled: vulnerable-web
[NOTE] 5.23 - Ensure that docker exec commands are not used with the privileged option (Automated)
[NOTE] 5.24 - Ensure that docker exec commands are not used with the user=root option (Manual)
[PASS] 5.25 - Ensure that cgroup usage is confirmed (Automated)
[WARN] 5.26 - Ensure that the container is restricted from acquiring additional privileges (Automated)
[WARN]       * Privileges not restricted: vulnerable-web
[WARN] 5.27 - Ensure that container health is checked at runtime (Automated)
[WARN]       * Health check not set: vulnerable-web
[INFO] 5.28 - Ensure that Docker commands always make use of the latest version of their image (Manual)
[WARN] 5.29 - Ensure that the PIDs cgroup limit is used (Automated)
[WARN]       * PIDs limit not set: vulnerable-web
[PASS] 5.30 - Ensure that Docker's default bridge 'docker0' is not used (Manual)
[PASS] 5.31 - Ensure that the host's user namespaces are not shared (Automated)
[WARN] 5.32 - Ensure that the Docker socket is not mounted inside any containers (Automated)
[WARN]       * Docker socket shared: vulnerable-web

[INFO] 6 - Docker Security Operations
[INFO] 6.1 - Ensure that image sprawl is avoided (Manual)
[INFO]      * There are currently: 14 images
[INFO]      * Only 4 out of 14 are in use
[INFO] 6.2 - Ensure that container sprawl is avoided (Manual)
[INFO]      * There are currently a total of 4 containers, with 1 of them currently running

[INFO] 7 - Docker Swarm Configuration
[PASS] 7.1 - Ensure that the minimum number of manager nodes have been created in a swarm (Automated) (Swarm mode not enabled)
[PASS] 7.2 - Ensure that swarm services are bound to a specific host interface (Automated) (Swarm mode not enabled)
[PASS] 7.3 - Ensure that all Docker swarm overlay networks are encrypted (Automated)
[PASS] 7.4 - Ensure that Docker's secret management commands are used for managing secrets in a swarm cluster (Manual) (Swarm mode not enabled)
[PASS] 7.5 - Ensure that swarm manager is run in auto-lock mode (Automated) (Swarm mode not enabled)
[PASS] 7.6 - Ensure that the swarm manager auto-lock key is rotated periodically (Manual) (Swarm mode not enabled)
[PASS] 7.7 - Ensure that node certificates are rotated as appropriate (Manual) (Swarm mode not enabled)
[PASS] 7.8 - Ensure that CA certificates are rotated as appropriate (Manual) (Swarm mode not enabled)
[PASS] 7.9 - Ensure that management plane traffic is separated from data plane traffic (Manual) (Swarm mode not enabled)


Section C - Score

[INFO] Checks: 117
[INFO] Score: 1


CIS audit output saved to: /home/bttrs/Riski/course_labs/labs/lab06/audit_reports/text/docker-bench-security-cis.txt

Converting Trivy JSON reports to XLSX/ODT formats...
✓ Saved to XLSX: ./audit_reports/xlsx/python-3.11-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/python-3.11-alpine-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/postgres-16-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/postgres-16-alpine-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/nginx-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/nginx-alpine-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/docker-bench-security-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/docker-bench-security-trivy.odt

==========================================
Audit complete!
Reports directory structure:
   ./audit_reports/
   ├── json/          (Trivy JSON outputs)
   ├── text/          (CIS audit text outputs)
   ├── xlsx/          (Excel spreadsheets)
   └── odt/           (OpenDocument Text files)

For CIS Docker Benchmark details, see:
https://www.cisecurity.org/benchmark/docker
```

- [x] 5. Проведите анализ уязвимостей, опишите их причину возникновения

### Результаты CIS Docker Benchmark (из docker-bench-security)

| CIS Check | Описание | Контейнер |
|-----------|----------|-----------|
| 5.2 | No AppArmorProfile Found | vulnerable-web |
| 5.4 | Capabilities added: CapAdd=[ALL] | vulnerable-web |
| 5.5 | Container running in Privileged mode | vulnerable-web |
| 5.6 | Sensitive directory / mounted | vulnerable-web |
| 5.10 | Container running with networking mode 'host' | vulnerable-web |
| 5.11 | Container running without memory restrictions | vulnerable-web |
| 5.12 | Container running without CPU restrictions | vulnerable-web |
| 5.13 | Container running with root FS mounted R/W | vulnerable-web |
| 5.16 | Host PID namespace being shared | vulnerable-web |
| 5.22 | Default seccomp profile disabled | vulnerable-web |
| 5.26 | Privileges not restricted | vulnerable-web |
| 5.27 | Health check not set | vulnerable-web |
| 5.29 | PIDs limit not set | vulnerable-web |
| 5.32 | Docker socket shared | vulnerable-web |

### Результаты Trivy (сканирование образов)

| Образ | CRITICAL | HIGH | MEDIUM | Всего |
|-------|----------|------|--------|-------|
| docker-bench-security (Alpine 3.8.2) | 3 | 0 | 0 | 3 |
| nginx:alpine | 0 | 0 | 0 | 0 |
| python:3.11-alpine | 0 | 0 | 1 | 1 |
| postgres:16-alpine | 0 | 2 | 10 | 12 |

**Критические CVE в docker-bench-security:**

- CVE-2019-9893 (CRITICAL) — libseccomp
- CVE-2019-14697 (CRITICAL) — musl, musl-utils

**CVE в postgres:16-alpine:**

- CVE-2025-58183 (HIGH) — stdlib
- CVE-2025-61729 (HIGH) — stdlib
- CVE-2025-47912 (MEDIUM) — stdlib
- + 9 других MEDIUM в stdlib

**CVE в python:3.11-alpine:**

- CVE-2025-8869 (MEDIUM) — pip

---

- [x] 6. Опишите влияния уязвимостей, их сценарий атаки

### Влияние уязвимостей (на основе CIS WARN из скрипта)

**CIS 5.5 + 5.6**:

```
[WARN] 5.5 - Container running in Privileged mode: vulnerable-web
[WARN] 5.6 - Sensitive directory / mounted in: vulnerable-web
```

Сценарий: запись SSH ключа → `echo "ssh-rsa ..." > /hostroot/root/.ssh/authorized_keys` → root на хосте.

**CIS 5.32**:

```
[WARN] 5.32 - Docker socket shared: vulnerable-web
```

Сценарий: из контейнера `docker run --privileged -v /:/mnt alpine chroot /mnt` → полный контроль.

**CIS 5.10 + 5.16**:

```
[WARN] 5.10 - Container running with networking mode 'host': vulnerable-web
[WARN] 5.16 - Host PID namespace being shared with: vulnerable-web
```

Сценарий: `tcpdump -i any` → перехват трафика; `kill -9 <host_pid>` → DoS.

**CIS 5.4 + 5.22**:

```
[WARN] 5.4 - Capabilities added: CapAdd=[ALL] to vulnerable-web
[WARN] 5.22 - Default seccomp profile disabled: vulnerable-web
```

Сценарий: CAP_SYS_ADMIN → mount namespace escape; CAP_NET_RAW → ARP spoofing.

**CIS 5.11 + 5.12 + 5.29**:

```
[WARN] 5.11 - Container running without memory restrictions: vulnerable-web
[WARN] 5.12 - Container running without CPU restrictions: vulnerable-web
[WARN] 5.29 - PIDs limit not set: vulnerable-web
```

Сценарий: fork bomb → `:(){ :|:& };:` → DoS хоста.

---

- [x] 7. Оцените риски ИБ и предложите меры для их снижения

### Оценка рисков (на основе CIS WARN из скрипта)

| CIS Check | Риск | Уровень | Мера снижения |
|-----------|------|---------|---------------|
| 5.5 Privileged mode | Container Escape | Критический | Убрать `privileged: true` |
| 5.6 Sensitive dir mounted | Data Leakage | Критический | Убрать монтирование `/` |
| 5.32 Docker socket shared | Full Host Takeover | Критический | Убрать монтирование docker.sock |
| 5.4 CapAdd=[ALL] | Privilege Escalation | Высокий | `cap_drop: ALL` + минимум |
| 5.22 Seccomp disabled | Syscall Abuse | Высокий | Использовать default seccomp |
| 5.2 No AppArmor | MAC Bypass | Средний | Включить AppArmor профиль |
| 5.10 Network host | Network Sniffing | Высокий | Использовать bridge network |
| 5.16 PID host | Process Manipulation | Средний | Убрать `pid: host` |
| 5.11/5.12/5.29 No limits | DoS | Средний | Добавить mem_limit, cpus, pids_limit |
| 5.27 No healthcheck | Availability | Низкий | Добавить HEALTHCHECK |

### Меры снижения рисков (что исправить в vulnerable-app.yml)

```yaml
# БЫЛО (уязвимо):
privileged: true
network_mode: host
pid: host
cap_add:
  - ALL
security_opt:
  - apparmor:unconfined
  - seccomp:unconfined
volumes:
  - /:/hostroot:rw
  - /var/run/docker.sock:/var/run/docker.sock

# СТАЛО (безопасно):
user: "101:101"
read_only: true
security_opt:
  - no-new-privileges:true
cap_drop:
  - ALL
cap_add:
  - NET_BIND_SERVICE
mem_limit: 256m
cpus: 0.5
pids_limit: 100
networks:
  - internal
healthcheck:
  test: ["CMD", "wget", "-q", "--spider", "http://localhost/"]
  interval: 30s
```

---

- [x] 8. Сделайте анализ уязвимостей из сгенерированных файлов .odt, .xslx и опишите их в отчете

### Анализ сгенерированных отчётов

Скрипт `audit.sh` сгенерировал отчёты в форматах JSON, XLSX и ODT:

```
✓ Saved to XLSX: ./audit_reports/xlsx/python-3.11-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/python-3.11-alpine-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/postgres-16-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/postgres-16-alpine-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/nginx-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/nginx-alpine-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/docker-bench-security-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/docker-bench-security-trivy.odt
```

### Содержимое отчётов (из JSON)

**docker-bench-security-trivy.json** (Alpine 3.8.2):

| CVE | Severity | Package |
|-----|----------|---------|
| CVE-2019-9893 | CRITICAL | libseccomp |
| CVE-2019-14697 | CRITICAL | musl |
| CVE-2019-14697 | CRITICAL | musl-utils |

Причина: образ использует устаревший Alpine 3.8.2 (строка 88 вывода: `This OS version is no longer supported`).

**nginx-alpine-trivy.json** (Alpine 3.23.2):

Уязвимостей не обнаружено — образ актуальный.

**python-3.11-alpine-trivy.json** (Alpine 3.23.2):

| CVE | Severity | Package |
|-----|----------|---------|
| CVE-2025-8869 | MEDIUM | pip |

**postgres-16-alpine-trivy.json** (Alpine 3.23.2):

| CVE | Severity | Package |
|-----|----------|---------|
| CVE-2025-58183 | HIGH | stdlib |
| CVE-2025-61729 | HIGH | stdlib |
| CVE-2025-47912 | MEDIUM | stdlib |
| CVE-2025-58185 | MEDIUM | stdlib |
| CVE-2025-58186 | MEDIUM | stdlib |
| + 7 других | MEDIUM | stdlib |

Причина: Go бинарники внутри образа (строка 127 вывода: `Using severities from other vendors`).

### Рекомендации (на основе CIS WARN из секций 1-4)

| CIS Check | Рекомендация |
|-----------|--------------|
| 1.1.3-1.1.18 | Настроить auditd для Docker файлов |
| 2.2 | Ограничить трафик на default bridge |
| 2.9 | Включить user namespaces |
| 2.14 | `--security-opt=no-new-privileges` по умолчанию |
| 4.5 | `export DOCKER_CONTENT_TRUST=1` |
| 4.6 | Добавить HEALTHCHECK во все образы |

- [x] 9. Подготовьте отчет `gist`.

- [x] 10. Почистите кеш от `venv` и остановите уязвимостей приложение, почистите контейнера

```
bttrs@bttrs:~/Riski/course_labs/labs/lab06$ docker compose -f vulnerable-app.yml down
WARN[0000] /home/bttrs/Riski/course_labs/labs/lab06/vulnerable-app.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] down 0/2
 ⠼ Container debug-shell    Removing                                                                                                                                                                     0.5s 
 ⠼ Container vulnerable-web Removing                                                                                                                                                                     0.5s 
bttrs@bttrs:~/Riski/course_labs/labs/lab06$ docker system prune -f
Deleted Containers:
e6284768b25214306d4e58b67d4f27e116ab7e51b97f335453d6dd7a35598e22
b76e09087db25134af1d63930aa18de3631254b74a79037f8f324ffa23b6ec06

Deleted Networks:
lab06_default

Deleted Images:
untagged: sha256:0d41c675ed556444b513069dae11e9012bfab363697bcdae0a3faa31af4f4249

Deleted build cache objects:
xz3qebg47o7hhh0g7ioh3mr58
zp7mo0zccyu6rjf21lp372ar7
dyfjff6dmjgd2a1mj4knkcfip
z31ijsicuos3crszy3orsu8wy
j1kwcemw6gwhaghnhqi5ww6qn
3v0nrt2q6iavg1rbrf5ea8pp8
gvnr71j3zf8mj83kv66369dfe
z579nhir4o3a08z4ax01ghrru
02hsuloe5zy2kn1m0iytxr8gw
maheqbp90b43ca28k69qqklva
p9oni51drh5a8j8fwcu17xq0v
q01k707mayh4uzrw572eaeq4q
9ut3n3zue9gnsybrsda1oqy19
hx2ktwpu5bmrporoumkph7rem
5ga1vn0vj2znpo4tbrpshbuv6
xs7s0vqwhh50rfvwpi44hu10q
50t5nd54b9czjlo4rjcudzrcy
igleyej74if3cvsrb0dbm9paa
a25c4nv1lue6j4v88y0fczq5y
y24bexl6yt3ht8f4955ud2s6q
0omswifs0qtbsvebf3ktxaocd
jq06r8fzalwky572lbbpzlj1y
uh7axsod7wyilxe8gn7k46m77
ecq5b0t7iwh632c3cybjigwd0
fo3h6l2m87rpjn0j4fuu72t8y
q8gqz3h74s4p7z91zpz1yeg1m
8gwsv317olmgzfgwn1d2jjznv
egzosinh6xc6b9f039zp3jbdg
ljuh3snu59w9hub68b3byfa4k
t806polu9hrqxa67cfxa3tjk5
im9v16f477v5orm4qeqcdmzpm
68pyv3m5d49pgm2gvw3giytdm
jgmgtmdme7cw2w3xd6dqmvwqo
xfa6q0fdvxwwvg36vx1jzvvnm
vdn83vq92go9sbmluhc0737j2
tb7yo3c95qxh3k3nc9gnpeuee
m70tzfzfcjshta2eocn2r0xyu
ez757nvrlp1zcyz9lm1cun4hz

Total reclaimed space: 286.5MB
bttrs@bttrs:~/Riski/course_labs/labs/lab06$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bttrs@bttrs:~/Riski/course_labs/labs/lab06$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

---

Copyright (c) 2025 Egor Davydov

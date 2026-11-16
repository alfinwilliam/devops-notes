---
title: "Scenario walk-throughs"
status: draft
form: guide
commands: none
---

# Scenario walk-throughs

> **Status: AI draft, 2026-11-16.** Not yet verified by me. Worked answers built from the linked pages; the commands are shown, not run for this page.

## In one line

For every "what would you do if..." question: ask one clarifying question, mitigate user impact first, then narrow down layer by layer with one command per step, say what a good and bad result look like, and finish with the fix and how you would stop it recurring.

## How to use these

Each scenario starts with **the question to ask first**, then numbered steps. In an interview, say the steps out loud with the command and what you are looking for; you rarely need to reach the end before the interviewer moves on ([How to answer technical questions](how-to-answer.md), [The debugging walk](../start/debugging-walk.md)).

## 1. "The site is slow"

**Ask first:** for everyone or some users, since when, and did anything change (deploy, traffic, config)?

1. Confirm and measure from outside: `curl -w '%{time_namelookup} %{time_connect} %{time_appconnect} %{time_starttransfer} %{time_total}\n' -o /dev/null -s https://app.example.com/` splits DNS, TCP, TLS and server time ([curl -v line by line](../networking/curl-v-annotated.md)).
2. Check the dashboards for the four golden signals: latency percentiles, traffic, errors, saturation ([Signals and methods](../observability/signals-and-methods.md)).
3. If server time dominates, find which hop is slow: load balancer target response time, then app latency, then database ([Tracing](../observability/tracing.md)).
4. Check saturation on the app hosts or pods: `kubectl top pods`, CPU throttling, memory, connection pools ([Requests, limits and QoS](../kubernetes/resources-and-qos.md)).
5. Check the database: `pg_stat_activity` for long or blocked queries ([PostgreSQL for operators](../data/postgres-for-operators.md)).
6. Mitigate: roll back a recent deploy, scale out, or shed non-critical load. Then find the root cause and add the alert that would have caught it earlier.

## 2. "A pod is in CrashLoopBackOff"

**Ask first:** is it a new deploy or a pod that was running before?

1. `kubectl get pod <pod> -o wide` and `kubectl describe pod <pod>`: last state, exit code, reason, events.
2. Exit code: `137` with reason `OOMKilled` means the memory limit; `1` or another app code means the app failed; `127` means command not found.
3. `kubectl logs <pod> --previous` for the crashed container's output.
4. Check configuration: missing ConfigMap or Secret keys, wrong environment variables, wrong command or arguments.
5. Check probes: an aggressive liveness probe kills a slow-starting app ([Probes and graceful shutdown](../kubernetes/probes-and-graceful-shutdown.md)).
6. Check dependencies the app needs at startup (database, DNS).
7. Fix the cause; if it came with a deploy, roll back first: `kubectl rollout undo deployment/<name>` ([Pods](../kubernetes/pods.md), [Troubleshooting playbook](../kubernetes/troubleshooting.md)).

## 3. "I can't SSH to a server"

**Ask first:** what exactly happens: timeout, connection refused, or permission denied?

1. **Timeout** means packets are dropped: check the route, security group and NACL for port 22 from your IP, and that the instance has a public IP or that you are on the VPN ([VPC troubleshooting](../aws-core/vpc-troubleshooting.md)).
2. `nc -vz <host> 22`: open, refused or timed out.
3. **Connection refused** means the host answered but nothing listens: `sshd` stopped, or listening on another port.
4. **Permission denied (publickey)**: wrong key, wrong user (`ubuntu`, `ec2-user`), key permissions too open, or the key not in `authorized_keys`. `ssh -v` shows which keys were offered ([SSH](../linux/ssh.md)).
5. If the instance is up but unreachable, use Session Manager or the serial console instead of SSH ([Systems Manager](../aws-services/systems-manager.md)).
6. If status checks fail, see [EC2](../aws-services/ec2.md): system check means AWS side (stop and start moves the host), instance check means inside the OS (disk full, bad fstab, kernel).

## 4. "The disk is full"

**Ask first:** which file system, and is it filling right now?

1. `df -h` to find the file system; `df -i` in case inodes, not bytes, are exhausted.
2. `sudo du -xh --max-depth=1 / | sort -h | tail` and drill down ([Disks and filesystems](../linux/disks-and-filesystems.md)).
3. Usual suspects: logs (`/var/log`, `journalctl --disk-usage`), container images and layers, core dumps, old releases.
4. If `df` says full but `du` cannot find it: a deleted file still held open. `sudo lsof +L1` lists them; restart the process (or truncate through `/proc/<pid>/fd/<n>`).
5. Free space safely: `journalctl --vacuum-size=500M`, rotate logs, `docker system prune` (check first what it removes).
6. Prevent: log rotation and retention, an alert at 80 percent, and a bigger or separate volume for data ([Logs](../linux/logs.md)).

## 5. "The deploy succeeded but users see errors"

**Ask first:** which errors, for which users, and did they start exactly at the deploy?

1. Compare error rate and latency before and after the deploy time on the dashboards.
2. Check which version serves the errors: some pods, all pods, one zone? `kubectl get pods -l app=<name> -o wide` and their image tags.
3. Read the app logs of new pods for the failing requests.
4. Check what "succeeded" meant: did readiness probes test the real dependencies, or only that the process started?
5. Mitigate: roll back (`kubectl rollout undo`, Argo CD revert, or redeploy the previous image) ([Promotion and rollback](../gitops/promotion-and-rollback.md)).
6. Then: a canary step, better readiness checks, and alerting on error rate during rollout ([Deployment strategies](../cicd/deployment-strategies.md)).

## 6. "5xx spike after a release"

**Ask first:** which code: 502, 503 or 504?

1. **502**: upstream crashed or closed the connection: app crashes, wrong target port, or keep-alive timeout on the app shorter than the load balancer's.
2. **503**: no healthy targets: readiness failing, all pods restarting, or the Service has no endpoints (`kubectl get endpointslices -l kubernetes.io/service-name=<svc>`).
3. **504**: upstream too slow: new code path slower, database slower, timeout too short ([HTTP](../networking/http.md)).
4. Correlate with the release: only new pods? Load balancer metrics by target group.
5. Roll back if impact is real, then debug on the old version's stable baseline ([ALB and NLB](../aws-core/load-balancers.md)).

## 7. "A pod can't reach the database"

**Ask first:** has it ever worked from this pod or namespace?

1. From the pod (or an ephemeral debug container): `nslookup db.internal.example.com` for DNS ([Services and DNS](../kubernetes/services-and-dns.md)).
2. `nc -vz <db-host> 5432`: timeout (network policy or security group), refused (nothing listening), open (then it is credentials or TLS).
3. Kubernetes NetworkPolicy: is egress from this namespace allowed to the database? ([Pod networking and NetworkPolicy](../kubernetes/pod-networking-and-network-policy.md))
4. AWS side: the database security group allows the source (node security group, or the pod's security group with security groups for pods) ([VPC CNI](../eks/vpc-cni.md)).
5. Route tables and NACLs between the subnets.
6. If open: check credentials, `sslmode`, and the database's own logs for rejected connections.

## 8. "terraform plan wants to destroy production resources"

**Ask first:** what changed: code, provider version, state, or the real infrastructure?

1. Do not apply. Find each resource marked `must be replaced` or `will be destroyed`, and the attribute flagged `# forces replacement` ([Reading a plan](../iac/reading-a-plan.md)).
2. A rename or move in code: add a `moved` block instead of destroy and create ([Import, moved and drift](../iac/import-and-drift.md)).
3. A `count` index shift: switch to `for_each` with stable keys ([Terraform language](../iac/language.md)).
4. Wrong workspace, backend or variables file: check `terraform workspace show` and the backend config.
5. Drift (someone changed it by hand): decide to adopt the change in code or let Terraform revert it.
6. Provider upgrade changed a default: pin the version, read the changelog.
7. Prevent: `prevent_destroy` on critical resources, plan review in CI, and policy checks on destroys ([Testing and CI](../iac/testing-and-ci.md)).

## 9. "A certificate expired"

**Ask first:** which certificate: the public site, an internal service, or a client certificate?

1. Confirm: `openssl s_client -connect app.example.com:443 -servername app.example.com </dev/null | openssl x509 -noout -dates -subject -issuer` ([TLS and certificates](../networking/tls.md)).
2. Find where it is served from: load balancer (ACM), ingress (cert-manager Secret), the app itself.
3. Renew or reissue; for ACM, check why automatic renewal failed (DNS validation record removed) ([Route 53 and ACM](../aws-core/route53-and-acm.md)).
4. Deploy it and confirm the new expiry date from outside.
5. Check intermediates: a renewed leaf served without its chain fails on some clients.
6. Prevent: alert on days-to-expiry for every endpoint, and automate renewal.

## 10. "A node is NotReady"

**Ask first:** one node or many, and since when?

1. `kubectl describe node <node>`: conditions (`Ready`, `MemoryPressure`, `DiskPressure`, `PIDPressure`) and the last heartbeat.
2. Many nodes at once suggests the control plane, network or a shared dependency; one node suggests that machine.
3. On the node (SSH or Session Manager): `systemctl status kubelet`, `journalctl -u kubelet --since '15 min ago'`, `systemctl status containerd` ([systemd and services](../linux/systemd.md)).
4. Check disk and memory: `df -h`, `free -m`, OOM messages in `dmesg` ([Memory and the OOM killer](../linux/memory-and-oom.md)).
5. Check the network path to the API server, and the CNI pods on that node ([Architecture](../kubernetes/architecture.md)).
6. Mitigate: cordon and drain if pods are stuck; with managed node groups or Karpenter, replacing the node is often faster than repairing it ([Disruptions and PDBs](../kubernetes/disruptions-and-pdbs.md)).

## After every scenario

Say the follow-up: what alert would have caught it sooner, what change prevents it, and what you would write in the incident review ([Incident response](../operations/incident-response.md)).

---
title: "Question index"
status: draft
form: guide
commands: none
---

# Question index

> **Status: generated.** Built by `tools/build-question-index.py` from every page's interview questions. Do not edit by hand.

## In one line

Every interview question in these notes, 1024 of them across 165 pages, grouped by section. Answer from memory, then open the page and compare with the hidden answer.

## How to drill with this page

1. Pick one section and set a timer.
2. Answer each question aloud or on paper before opening anything.
3. Open the page, expand the answer, and score yourself: 2 for every point, 1 for some, 0 for none or wrong.
4. A section passes at 70%. Anything scored 0 goes on your list for the next loop.

## Start here


**[One request, end to end](../start/request-path.md)**

1. Describe everything that happens when a user opens `https://shop.example.com` served from EKS.
2. Where does TLS usually terminate in this design, and what are the implications?
3. The site returns `503` from the load balancer after a deploy. Walk through your diagnosis.
4. How does traffic reach a pod with no public address?
5. Some users see an old version of the site after a DNS change. Which hop, and why?
6. A request fails only for large file uploads. Which hops would you suspect?

**[The debugging walk](../start/debugging-walk.md)**

1. A user says "the website is down". Walk me through how you diagnose it.
2. What is the difference between "connection refused" and "connection timed out", and what does each tell you to check?
3. Why should you run checks from the failing component rather than from your laptop?
4. `ping` to a server fails but the website works. What do you conclude?
5. A health check passes but users get errors. How can that be?
6. You get a `504` from the load balancer. Where in the walk are you, and what next?

## Linux


**[Shell and filesystem basics](../linux/shell-and-filesystem.md)**

1. What happens between typing `ls -l` and seeing its output?
2. Why is `cd` a shell builtin and not a program in `/usr/bin`?
3. What is an inode, and what does a directory actually contain?
4. What is the difference between a hard link and a symbolic link?
5. A script works when you run it, but fails in cron with `command not found`. Why?
6. `rm -rf $DIR/*` deleted far more than intended. What went wrong?
7. Two versions of `terraform` are installed and the wrong one runs. How do you find out why?

**[Users, groups and permissions](../linux/permissions.md)**

1. Explain the output `-rwxr-x--- 1 app deploy deploy.sh`. Who can do what?
2. How does Linux decide which permission set applies to a process?
3. What do `r`, `w` and `x` mean on a directory?
4. What are umask, setuid and the sticky bit?
5. A colleague fixed "permission denied" with `chmod -R 777`. What do you say?
6. You added `ci` to the `docker` group, but `docker ps` still says permission denied. Why?
7. An application running as `app` cannot read `/opt/sample-app/config/app.yaml`, yet the file is mode `644`. What do you check?

**[Processes and signals](../linux/processes-and-signals.md)**

1. What is the difference between a program and a process?
2. What is the difference between SIGTERM and SIGKILL?
3. A container exits with code 137. What does that tell you, and what do you check?
4. What is a zombie process, and how do you get rid of one?
5. What do exit codes 126, 127 and 130 mean?
6. Why does `docker stop` take 10 seconds for some containers, and how do you fix it?
7. A server has load average 30 but CPU is mostly idle. What is going on?

**[Streams, pipes and redirection](../linux/streams-and-redirection.md)**

1. What are stdin, stdout and stderr, and why does stderr exist?
2. What is the difference between `cmd > file 2>&1` and `cmd 2>&1 > file`?
3. What does a pipe do, and does the second command wait for the first to finish?
4. What is `set -o pipefail` for?
5. A cron job's log shows nothing on nights it failed. What do you change?
6. A colleague runs `sort data.txt > data.txt` and the file is now empty. Why?

**[Text tools: grep, sed, awk, find](../linux/text-tools.md)**

1. How do you find the 5 IP addresses that made the most requests in an access log?
2. Why does `uniq` need sorted input?
3. When would you use `awk` instead of `cut`?
4. How do you show 3 lines of context around every "Exception" in a log, case-insensitively?
5. How do you replace a value in a config file safely with `sed`?
6. A disk is filling with old logs. How do you find and delete logs older than 14 days under `/var/log/app` safely?
7. Using only the access log, how would you work out whether a spike of 502s came from one client or from everyone?

**[Boot, systemd and services](../linux/systemd.md)**

1. What is systemd, and what is a unit?
2. What is the difference between `After=` and `Requires=`?
3. You edited a unit file and restarted the service, but nothing changed. Why?
4. A service keeps restarting. Walk me through your investigation.
5. How do you change a setting of a packaged service without your change being lost on upgrade?
6. What happens when you run `systemctl stop` on a service?
7. When would you choose supervisord over systemd?

**[Logs](../linux/logs.md)**

1. Where do logs go on a modern Linux server?
2. How do you see only errors from one service in the last hour?
3. What is the difference between `copytruncate` and rotating with a reopen signal?
4. You are paged at 3 a.m. for a failing service. How do you read its logs efficiently?
5. After logrotate ran, the application's log file is empty but the application is clearly busy. Why?
6. Why are structured logs better than free-text logs?

**[Disks and filesystems](../linux/disks-and-filesystems.md)**

1. Walk through what it takes to use a new disk on a Linux server.
2. What is the difference between `df` and `du`?
3. A disk shows 100% in `df`, but `du` finds only half of that. What is happening and how do you fix it?
4. "No space left on device", but `df -h` shows 40% free. What do you check?
5. You enlarged a cloud volume from 50 GB to 100 GB, but the server still shows 50 GB. Why?
6. What is the safe way to clear a huge log file that a running service is writing to?
7. Why should `/etc/fstab` use UUIDs, and what does `nofail` do?

**[Memory and the OOM killer](../linux/memory-and-oom.md)**

1. `free -h` shows 200 MiB free on a 16 GiB server. Is that a problem?
2. What is the difference between VSZ and RSS?
3. What does the OOM killer do, and how does it choose?
4. A container was OOM-killed, but the host had 8 GiB free. How?
5. How would you confirm that a process was OOM-killed on a plain Linux server?
6. A Java service in a 2 GiB container sets `-Xmx2g` and keeps getting OOM-killed. What is wrong?
7. Should a production server use swap?

**[Performance triage](../linux/performance-triage.md)**

1. What does load average mean on Linux, and how do you judge whether 8 is high?
2. What is the USE method?
3. In `vmstat`, what do `r`, `b`, `wa` and `st` tell you?
4. A server's load is 20 on 4 CPUs, but CPU is 80% idle. What is happening and what do you run?
5. A containerised service has high latency but its CPU use never reaches its limit. What could it be?
6. When would you use `strace`, and what is the risk?
7. Users say a web app is slow. Walk me through your first five minutes on the server.

**[SSH](../linux/ssh.md)**

1. What happens when you run `ssh user@host`?
2. What are `known_hosts` and `authorized_keys`, and on which side does each live?
3. Why is `ProxyJump` safer than agent forwarding?
4. You get `Permission denied (publickey)` with a key you know is correct. What do you check?
5. SSH warns that the remote host identification has changed. What do you do?
6. How do you reach a database in a private subnet from your laptop?
7. How would you harden SSH on a public server?

**[Packages and updates](../linux/packages-and-updates.md)**

1. What is the difference between `apt update` and `apt upgrade`?
2. How do you find which package installed a given file, and what files a package installed?
3. How do you stop one package from being upgraded?
4. You patched OpenSSL on a server, but a scanner still reports the vulnerability. Why?
5. How do you add a third-party repository safely?
6. Should production servers patch themselves automatically?

**[Bash scripting](../linux/bash-scripting.md)**

1. What does `set -euo pipefail` do, line by line?
2. Why should you quote variables, and what goes wrong if you do not?
3. What is `trap` used for in scripts?
4. How do you read a file line by line correctly in bash?
5. A script runs fine by hand but fails in cron. What do you check?
6. How do you debug a bash script that does the wrong thing?
7. Write the outline of a script that deploys only if a health check passes, and rolls back otherwise.

**[Cron and timers](../linux/cron-and-timers.md)**

1. Explain `30 2 * * 1-5`.
2. Why does a script that works in your shell fail under cron?
3. How do you stop a cron job from overlapping with itself?
4. What does a systemd timer give you that cron does not?
5. Where would you look to see whether a cron job ran last night?
6. A daily cleanup must run at 23:00 India time, but the server uses UTC. What do you write?

**[jq and yq](../linux/jq-and-yq.md)**

1. How do you list the names of all pods that are not Running, using `kubectl` and `jq`?
2. What do `-r`, `-c` and `--arg` do in jq?
3. How do you give a default when a field might be missing?
4. Why use yq instead of sed to change an image tag in a manifest?
5. A script runs `jq ".items[] | select(.name == \"$NAME\")"` and breaks for some values. Why, and what is the fix?
6. How would you see which resources a Terraform plan will destroy, from a script?

## Networking


**[Layers and encapsulation](../networking/layers.md)**

1. What happens at L2, L3, L4 and L7? Give one example protocol and one device for each.
2. What is encapsulation?
3. What is the difference between a MAC address and an IP address?
4. What does ARP do, and does a host ARP for a destination on another subnet?
5. What is the difference between an L4 and an L7 load balancer?
6. A service cannot reach a database. How do you use the layers to narrow it down?
7. Small API responses work through a VPN, but large downloads hang. What layer and what cause?

**[IP addresses and subnetting](../networking/ip-and-subnetting.md)**

1. How many addresses are in a `/24`, a `/20` and a `/28`?
2. What does `/16` mean in `10.0.0.0/16`?
3. What are the private IPv4 ranges, and why do they need NAT to reach the internet?
4. Split `10.0.0.0/16` into 6 equal subnets. What prefix and what ranges?
5. Does `10.0.1.0/24` overlap with `10.0.0.0/20`? How do you tell quickly?
6. Two teams want to peer their VPCs, but both used `10.0.0.0/16`. What are the options?
7. A Kubernetes cluster on AWS stops scheduling pods with IP allocation errors. How is that a subnetting problem?

**[Routing and NAT](../networking/routing-and-nat.md)**

1. What is a default route, and when is it used?
2. Explain longest prefix match with an example.
3. What is NAT and why do private networks need it?
4. What is the difference between SNAT and DNAT?
5. Instances in a private subnet suddenly cannot reach the internet. What do you check?
6. How does traceroute work?
7. A request reaches the server, but the client times out waiting for the reply. What could cause that at the routing level?

**[TCP and UDP](../networking/tcp-and-udp.md)**

1. Walk me through the TCP three-way handshake.
2. What is the difference between TCP and UDP? Give a use for each.
3. What is the difference between "connection refused" and "connection timed out"?
4. What is TIME-WAIT, and should thousands of them worry you?
5. What is an ephemeral port?
6. A service cannot connect to a database on port 5432. `nc` times out. Walk through your next steps.
7. Connections from an application pool fail with resets after the system has been quiet for a while. Why?

**[DNS](../networking/dns.md)**

1. What does DNS do, and what does a user see when it fails?
2. What is the difference between a recursive resolver and an authoritative server?
3. What is the difference between an A record and a CNAME, and why can the top of a zone not be a CNAME?
4. What is a TTL, and what does "DNS propagation" really mean?
5. Walk me through what `dig +trace www.example.com` does.
6. You changed an A record ten minutes ago. Some users still reach the old server. Why, and how do you confirm it?
7. `curl` says "Could not resolve host" on one server, but the same name resolves on your laptop. What do you check, in order?
8. `dig` returns the correct address, but the application still connects to the wrong one. What could explain it?

**[HTTP](../networking/http.md)**

1. What is the difference between a `401` and a `403`?
2. What do `502`, `503` and `504` each mean, and who usually sends them?
3. What does idempotent mean, and why does it matter for retries?
4. What is the `Host` header for?
5. What does HTTP/2 change compared with HTTP/1.1?
6. After moving TLS termination to a load balancer, the site loops between redirects. Why?
7. Users report slowness. How would you use `curl` to find which part of a request is slow?

**[TLS and certificates](../networking/tls.md)**

1. What does TLS give you?
2. Explain the certificate chain of trust.
3. What is SNI and why is it needed?
4. A site works in Chrome but `curl` and a Java client fail with a certificate error. What is the likely cause?
5. What does "TLS termination at the load balancer" mean, and what are the trade-offs?
6. Why does forward secrecy matter?
7. How do you stop certificate expiry from causing outages?

**[Load balancers and proxies](../networking/load-balancers-and-proxies.md)**

1. What is the difference between an L4 and an L7 load balancer?
2. How do health checks work, and how can a bad one cause an outage?
3. What do `502`, `503` and `504` from a load balancer tell you?
4. What is connection draining, and why does it matter during deploys?
5. How does the application learn the real client address behind a proxy, and what is the risk?
6. Users get occasional `502`s under normal load, with no deploys. What would you check?
7. When would you choose sticky sessions, and what is the better alternative?

**[Firewalls and connection tracking](../networking/firewalls.md)**

1. What is the difference between a stateful and a stateless firewall?
2. What is the difference between DROP and REJECT?
3. Explain connection tracking and the ESTABLISHED state.
4. Which iptables chains does a packet pass through when it is routed through a host, for example a container's traffic?
5. You allowed port 443 inbound on a host, but HTTPS connections still time out. What do you check?
6. How do you change firewall rules on a remote server without locking yourself out?

**[Network tools on Linux](../networking/network-tools.md)**

1. Which tool do you use to see which ports a server is listening on, and which program owns each?
2. What is the difference between `ping`, `traceroute` and `mtr`?
3. How do you test whether a TCP port is reachable without the application's client?
4. How would you capture only the traffic to and from port 5432 on all interfaces, and save it?
5. A container image has no networking tools. How do you debug its network?
6. `traceroute` to a host shows `* * *` from hop 5 onwards, but the website loads. What does that mean?

**[curl -v, line by line](../networking/curl-v-annotated.md)**

1. In `curl -v` output, what do lines starting with `*`, `>` and `<` mean?
2. Walk me through the stages `curl -v https://example.com` shows.
3. The transcript stops at `Trying 203.0.113.10:443...` and eventually times out. What does that tell you?
4. How do you test a new server's certificate before DNS points at it?
5. `curl -v` shows `SSL certificate verify ok` and then `< HTTP/2 502`. Where is the problem?
6. What does `ALPN: server accepted h2` mean?

**[Nginx as a reverse proxy](../networking/nginx.md)**

1. How does Nginx decide which `server` and `location` handle a request?
2. What is the difference between `proxy_pass http://app;` and `proxy_pass http://app/;`?
3. A user gets a `502` from Nginx. Where do you look and what might you find?
4. What causes a `504` from Nginx, and how do you fix it properly?
5. What is the difference between `nginx -s reload` and a restart?
6. Why should a reverse proxy set `Host` and `X-Forwarded-For` headers?

## Git


**[How Git stores things](../git/how-git-stores-things.md)**

1. Does Git store diffs or snapshots? Explain.
2. What are blobs, trees and commits?
3. What is a branch, technically? What is HEAD?
4. What is the staging area for?
5. Why does rewriting history cause trouble for collaborators?
6. A large file was committed by mistake and deleted in the next commit. Is the repository smaller now?

**[Daily workflow](../git/daily-workflow.md)**

1. What is the difference between a fast-forward merge and a merge commit?
2. Merge or rebase: what is the difference and when would you use each?
3. How do you resolve a merge conflict?
4. What does `git stash` do, and when would you use it?
5. What is cherry-pick, and what is a typical use?
6. What is the difference between a lightweight and an annotated tag?

**[Undoing and recovering](../git/undo-and-recover.md)**

1. What is the difference between `git reset --soft`, `--mixed` and `--hard`?
2. What is the difference between `git reset` and `git revert`?
3. You ran `git reset --hard` and lost commits. How do you get them back?
4. A bad commit was merged to `main` and deployed. How do you undo it?
5. How would you find which of the last 200 commits introduced a bug?
6. What can Git not recover?

**[Remotes, pull requests and access](../git/remotes-and-collaboration.md)**

1. What is the difference between `git fetch` and `git pull`?
2. Why is a push rejected, and how do you fix it safely?
3. What does `--force-with-lease` protect against?
4. What would you put in branch protection for `main`?
5. How should a deployment server or CI job authenticate to Git?
6. Are Git hooks a good way to enforce that no secrets are committed?

**[Branching and release strategies](../git/branching-strategies.md)**

1. What is trunk-based development?
2. Compare GitFlow and trunk-based development.
3. What is a feature flag, and what problem does it solve?
4. How do you ship an urgent fix to production under trunk-based development, and under GitFlow?
5. What does semantic versioning mean by major, minor and patch?
6. Which strategy would you pick for a team deploying a web API many times a day, and what would you need in place?

## AWS identity and network


**[Accounts, regions and the CLI](../aws-core/accounts-regions-cli.md)**

1. What is the difference between a region and an Availability Zone?
2. How does the AWS CLI decide which credentials to use?
3. Why use many AWS accounts instead of one?
4. What should you do with the root user of an account?
5. Your script works on your laptop but runs against the wrong account in CI. What do you check?
6. What is the difference between `--query` and `--filters` in the CLI?

**[Organizations, SCPs and multi-account](../aws-core/organizations-and-scps.md)**

1. What is a service control policy, and does it grant permissions?
2. Who is affected by SCPs, and who is not?
3. How do SCPs combine across OUs?
4. Design an account structure for a company with two products, each with dev and prod.
5. How do you restrict an organisation to two regions without breaking global services?
6. An administrator in a member account gets `AccessDenied` for an action their policy allows. How do you investigate?

**[IAM policies and how they are evaluated](../aws-core/iam-policies.md)**

1. Explain how AWS evaluates whether a request is allowed.
2. What is the difference between an identity-based and a resource-based policy?
3. What is a permissions boundary, and when would you use one?
4. What does an explicit deny in an SCP mean for an account administrator?
5. A role can list a bucket but not read objects in it. Why?
6. How do you give a role in account A read access to an S3 bucket in account B?
7. Why is `"Effect": "Allow"` with `NotAction` risky?

**[IAM roles and STS](../aws-core/iam-roles-and-sts.md)**

1. What is the difference between an IAM user and an IAM role?
2. What is a trust policy, and how does it differ from a permissions policy?
3. What does `iam:PassRole` protect against?
4. How do temporary credentials from STS differ from access keys?
5. What is the confused deputy problem, and how does an external ID help?
6. An application on EC2 cannot get AWS credentials. What do you check?

**[Federation and SSO](../aws-core/federation-and-sso.md)**

1. What is federation in AWS, and why is it preferred over IAM users?
2. How does IAM Identity Center grant access to many accounts?
3. What is the difference between SAML and OIDC federation?
4. Why must a trust policy for a CI OIDC provider check the `sub` claim?
5. An engineer leaves. How do you make sure their AWS access is gone?
6. A pipeline can assume its AWS role from feature branches, but it should only work from `main`. What is wrong and how do you fix it?

**[Least privilege and AccessDenied](../aws-core/least-privilege-and-accessdenied.md)**

1. What is least privilege, and how do you apply it in practice on AWS?
2. Walk me through debugging an `AccessDenied` error.
3. Name some IAM permissions that allow privilege escalation.
4. How would you let developers create IAM roles for their applications without letting them escalate?
5. A role was tightened using 30 days of CloudTrail data and broke a month later. What went wrong?
6. An application can read an encrypted S3 object but not write one. Why?

**[VPC basics](../aws-core/vpc-basics.md)**

1. What makes a subnet public or private?
2. How many usable addresses does a `/24` subnet have in AWS, and why?
3. Draw a production VPC for a web application.
4. What is the difference between an internet gateway and a NAT gateway?
5. An instance in a private subnet cannot download packages. Walk through the checks.
6. Why plan VPC ranges across the whole organisation?

**[NAT, endpoints and PrivateLink](../aws-core/nat-endpoints-privatelink.md)**

1. Why do private subnets need a NAT gateway, and where does it live?
2. What is the difference between a gateway endpoint and an interface endpoint?
3. A NAT gateway was deleted by mistake. What do workloads see, and why?
4. How would you reduce a high NAT gateway bill?
5. What is PrivateLink, and how is it different from VPC peering?
6. How do you make sure an S3 bucket is only used from inside your VPC?

**[Peering, Transit Gateway and VPN](../aws-core/vpc-connectivity.md)**

1. What does "VPC peering is not transitive" mean?
2. When would you choose Transit Gateway over peering?
3. Explain association and propagation in Transit Gateway route tables.
4. What are the options for connecting an office to AWS, and how do they differ?
5. Two VPCs are peered and routes are added, but connections still time out. What do you check?
6. Two teams' VPCs overlap and they need one API between them. What do you do?

**[Security groups and NACLs](../aws-core/security-groups-and-nacls.md)**

1. What is the difference between a security group and a network ACL?
2. Why do NACLs need rules for ephemeral ports?
3. Why reference security groups instead of IP ranges?
4. How would you secure a three-tier application with security groups?
5. A client gets timeouts. You can see its requests in the server's access log. What is the likely cause?
6. How do you find security groups exposed to the internet?

**[ALB and NLB](../aws-core/load-balancers.md)**

1. When would you choose an ALB over an NLB, and the reverse?
2. What are listeners, rules and target groups?
3. An ALB returns `503`. What does it mean and what do you check?
4. How do you avoid dropping requests during a deploy behind an ALB?
5. Why might targets behind an ALB return intermittent `502`s?
6. What does Global Accelerator add on top of a regional load balancer?

**[Route 53 and ACM](../aws-core/route53-and-acm.md)**

1. What is an alias record, and how does it differ from a CNAME?
2. What is the difference between a public and a private hosted zone?
3. Name Route 53 routing policies and a use for each.
4. How does ACM validate and renew certificates?
5. Why does a CloudFront distribution not see a certificate you created in `ap-south-1`?
6. How would you migrate a domain to a new load balancer with a safe rollback?

**[CloudFront and WAF](../aws-core/cloudfront-and-waf.md)**

1. How does CloudFront decide whether to serve from cache?
2. How do you keep an S3 bucket private while serving it through CloudFront?
3. Why might a CDN make a site slower or more expensive?
4. What is a WAF, and how do you roll out new rules safely?
5. What does a rate-based rule protect against?
6. What is the difference between Shield Standard and Shield Advanced?

**[VPC troubleshooting](../aws-core/vpc-troubleshooting.md)**

1. An EC2 instance in a private subnet cannot reach the internet. Walk through your checks.
2. What do VPC Flow Logs record, and what do they not record?
3. Flow Logs show the request accepted at the server but the reply rejected. What is the cause?
4. What does Reachability Analyzer do?
5. Why does a timeout point to different causes than "connection refused" inside a VPC?
6. Two VPCs are peered, but an application in one cannot reach a database in the other. List the places to check.

## AWS services


**[EC2](../aws-services/ec2.md)**

1. What is the difference between stopping and terminating an instance?
2. Why use IMDSv2, and what does the hop limit do?
3. How do you get shell access without SSH keys?
4. When would you choose Graviton instances?
5. What do system and instance status check failures mean?
6. A T-family instance becomes slow every afternoon. Why?

**[Auto Scaling and AMIs](../aws-services/auto-scaling-and-amis.md)**

1. What is the difference between an AMI and a launch template?
2. EC2 vs load balancer health checks in an Auto Scaling group?
3. Which scaling policy would you choose and why?
4. How do you roll out a new AMI to a running group without downtime?
5. Golden images or bootstrapping?
6. An Auto Scaling group keeps replacing instances every few minutes. What do you check?

**[EBS](../aws-services/ebs.md)**

1. What is EBS and how is it different from instance store?
2. gp3 vs io2 vs st1?
3. How do you grow a volume without downtime?
4. How do snapshots work, and how are they used for DR?
5. Why can a pod's volume not follow it to another zone?
6. A database volume is slow. How do you investigate?

**[EFS](../aws-services/efs.md)**

1. When would you choose EFS over EBS?
2. What is a mount target and what does it need?
3. What is an EFS access point for?
4. An EFS mount hangs from a new node group. What do you check?
5. Elastic, Provisioned or Bursting throughput?
6. How do you reduce EFS storage cost?

**[S3](../aws-services/s3.md)**

1. What consistency does S3 provide today?
2. A user deleted an important file from a versioned bucket. How do you recover it?
3. How do you cut the S3 bill for a bucket that keeps growing?
4. How would you let browsers upload large files without passing them through your servers?
5. What does replication need, and what does it not do by default?
6. Why serve a static site through CloudFront instead of the S3 website endpoint?
7. What is a presigned URL, and what limits it?
8. Your Lambda, triggered by S3 uploads, is processing some files twice. Why, and what do you do?

**[S3 security](../aws-services/s3-security.md)**

1. Walk through how S3 decides whether a request is allowed.
2. A role in another account gets `AccessDenied` reading your bucket. What do you check?
3. SSE-S3 or SSE-KMS: which and why?
4. How do you make sure a bucket is never reached over plain HTTP?
5. How would you protect backups from deletion by ransomware or a compromised admin?
6. How do you find public or shared buckets across an account?
7. Governance mode versus compliance mode in Object Lock?
8. What is the difference between CloudTrail data events and S3 server access logs?

**[RDS and Aurora](../aws-services/rds-and-aurora.md)**

1. Multi-AZ versus read replica: what is each for?
2. Someone dropped a table at 14:05. How do you recover?
3. Explain Aurora's architecture and why failover is fast.
4. Lambda functions keep hitting "too many connections" on RDS. What do you do?
5. How does an app survive a database failover?
6. You changed `shared_buffers` and nothing happened. Why?
7. How would you do a major version upgrade with little downtime?

**[SQS, SNS and EventBridge](../aws-services/messaging.md)**

1. Queue, topic or event bus: when do you use which?
2. What is the visibility timeout, and what goes wrong if it is too short?
3. How do you make a consumer idempotent?
4. Explain the SNS to SQS fan-out pattern and why it is common.
5. Messages are landing in the DLQ. Walk me through it.
6. Standard or FIFO queue?
7. An EventBridge rule is not triggering its Lambda. What do you check?

**[KMS, Secrets Manager and Parameter Store](../aws-services/kms-and-secrets.md)**

1. Explain envelope encryption.
2. How do key policies and IAM policies interact?
3. Secrets Manager or Parameter Store?
4. What happens when a KMS key is rotated, and when it is deleted?
5. How does a rotated database password reach running applications without an outage?
6. A team wants to share an encrypted S3 bucket with another account. What must change on the KMS side?
7. How do you keep secrets out of logs and repositories?

**[CloudWatch](../aws-services/cloudwatch.md)**

1. What uniquely identifies a CloudWatch metric?
2. Why can't you see memory usage for an EC2 instance by default, and how do you fix it?
3. Explain alarm evaluation: period, evaluation periods, datapoints to alarm and missing data.
4. Your CloudWatch bill doubled. Where do you look?
5. How do you get application logs from CloudWatch into OpenSearch or S3?
6. What is the embedded metric format and when is it useful?
7. How would you alert on errors that only appear in logs?

**[CloudTrail, Athena and Config](../aws-services/cloudtrail-and-config.md)**

1. Someone deleted an S3 bucket last night. How do you find out who?
2. Management versus data events?
3. How do you protect CloudTrail logs from tampering?
4. How do you query months of CloudTrail logs efficiently?
5. What does AWS Config give you that CloudTrail does not?
6. You get `AccessDenied` in an app. How can CloudTrail help?
7. What would you alarm on from CloudTrail?

**[GuardDuty, Security Hub and Inspector](../aws-services/security-services.md)**

1. What is the difference between GuardDuty, Inspector and Security Hub?
2. GuardDuty reports an EC2 instance communicating with a known malicious IP. What do you do?
3. How do you prioritise 500 critical CVE findings?
4. When is it acceptable to suppress a finding?
5. How do you run these across 50 accounts?
6. Why might a CSPM control show failed even though the resource is fine?

**[Systems Manager](../aws-services/systems-manager.md)**

1. Why use Session Manager instead of SSH?
2. An instance does not appear in Systems Manager. How do you debug it?
3. How do you patch 500 instances safely?
4. How would you reach a private RDS database from your laptop without a bastion?
5. What are concurrency and error thresholds in Run Command for?
6. What is in an SSM document, and give examples.

**[ECR](../aws-services/ecr.md)**

1. Pods on EKS show `ImagePullBackOff` with an ECR image. What do you check?
2. How does CI push to ECR without long-lived keys?
3. Why turn on tag immutability, and what is the catch?
4. The ECR bill keeps growing. What do you do?
5. Why use a pull-through cache for public base images?

## Serverless and Fargate


**[Lambda](../serverless/lambda.md)**

1. Explain a Lambda cold start and how to reduce it.
2. What are reserved and provisioned concurrency?
3. Compare synchronous, asynchronous and event source mapping invocations.
4. How do you deploy a new Lambda version safely?
5. Why might more memory make a function cheaper?
6. A Lambda behind SQS keeps reprocessing the same messages and the queue grows. What do you check?

**[Lambda networking and permissions](../serverless/lambda-networking-and-permissions.md)**

1. What is the difference between a Lambda execution role and its resource-based policy?
2. A Lambda in a VPC times out calling S3. Why, and how do you fix it?
3. Does putting a Lambda in a public subnet give it internet access?
4. How should a Lambda function get a database password?
5. How do you let only one S3 bucket invoke a function?
6. When should a Lambda function be attached to a VPC?

**[API Gateway](../serverless/api-gateway.md)**

1. REST API or HTTP API?
2. What authorizer options are there?
3. A client gets "Missing Authentication Token". What is wrong?
4. A Lambda-backed API returns 502. What do you check?
5. How do you handle an operation that takes two minutes?
6. How do you protect an API from one noisy client?

**[ECS and Fargate](../serverless/ecs-and-fargate.md)**

1. Explain cluster, task definition, task and service.
2. What is the difference between the task execution role and the task role?
3. What does the awsvpc network mode change?
4. Fargate or EC2 launch type?
5. How do ECS rolling deployments and the circuit breaker work?
6. A new task revision never becomes healthy. How do you debug it?

**[Cognito](../serverless/cognito.md)**

1. What is the difference between a user pool and an identity pool?
2. Which tokens does a user pool issue, and what is each for?
3. How do you protect an API with Cognito?
4. How do you give admins extra rights?
5. Why use managed login instead of building your own sign-in form?

**[Step Functions](../serverless/step-functions.md)**

1. When would you use Step Functions instead of chaining Lambda functions?
2. Standard or Express workflows?
3. How do Retry and Catch work?
4. How do you wait for a human approval in a workflow?
5. What does the Map state do?

## Data stores


**[PostgreSQL for operators](../data/postgres-for-operators.md)**

1. The app reports "too many clients already". What do you do now and later?
2. New tables created by migrations are not readable by the app. Why?
3. `pg_dump` versus physical backups?
4. Queries are hanging. How do you find the cause?
5. What does `sslmode=prefer` really give you?
6. Session versus transaction pooling in PgBouncer?
7. How would you upgrade a major PostgreSQL version with little downtime?

**[Redis and caching patterns](../data/redis-and-caching.md)**

1. Explain cache-aside and its failure modes.
2. What is a cache stampede and how do you prevent it?
3. Which eviction policy for a pure cache, and which for sessions?
4. RDB versus AOF?
5. Redis or Valkey versus Memcached?
6. How does Redis Cluster split data, and what breaks?
7. After a database update, users still see the old price. Why?

## Containers


**[What a container is](../containers/what-is-a-container.md)**

1. What is a container, technically?
2. How is a container different from a virtual machine?
3. What are namespaces and cgroups, and which does what?
4. Why can a container ignore `docker stop` and get killed after 10 seconds?
5. What is copy-on-write in the container filesystem?
6. A container was OOM-killed although the host had plenty of free memory. Why?
7. Is running as root inside a container safe?

**[Images and Dockerfiles](../containers/images-and-dockerfiles.md)**

1. What is an image layer, and why does instruction order matter?
2. What is the difference between `CMD` and `ENTRYPOINT`?
3. What is a multi-stage build, and why use one?
4. Why should you not use the `latest` tag in production?
5. How can a secret end up in an image even after you delete it?
6. A container fails with `exec format error`. What happened?
7. How would you make a Dockerfile more secure?

**[Running and debugging containers](../containers/running-containers.md)**

1. A container keeps exiting right after it starts. How do you debug it?
2. What is the difference between a volume and a bind mount?
3. Why can two containers on the default bridge network not reach each other by name?
4. The app works inside the container but the published port refuses connections. Why?
5. How do you debug the network of a container whose image has no shell?
6. What do exit codes 125, 126, 127 and 137 mean for a container?

**[Registries and image security](../containers/registries-and-image-security.md)**

1. What is the difference between an image tag and an image digest?
2. How do you make sure every node runs exactly the same image?
3. What does an image scanner check, and what are its limits?
4. Your base image is distroless, yet the scan shows critical vulnerabilities. How is that possible?
5. Why rebuild images on a schedule, not only on code changes?
6. What should a CI pipeline do with image security?

**[Container runtimes](../containers/runtimes.md)**

1. What is the difference between Docker, containerd and runc?
2. What is the CRI?
3. Kubernetes removed dockershim. Do images built with Docker still run?
4. How do you debug containers on a Kubernetes node that has no Docker?
5. What is a containerd shim for?
6. What is the pause container in a pod?

**[Docker Compose](../containers/docker-compose.md)**

1. What is Docker Compose for?
2. Does `depends_on` make a service wait until its dependency is ready?
3. How do services in Compose find each other?
4. What is the difference between `docker compose down` and `down -v`?
5. Why not run production on Compose?

## Kubernetes


**[Architecture and the reconcile loop](../kubernetes/architecture.md)**

1. Name the control-plane components and what each does.
2. What runs on every worker node?
3. What is a reconcile loop?
4. Walk me through what happens when you apply a Deployment.
5. A node goes down. What does Kubernetes do, and what does it not do?
6. Why does every component talk only to the API server?

**[kubectl fluency](../kubernetes/kubectl.md)**

1. A pod is in `CrashLoopBackOff`. Which kubectl commands do you run, in order?
2. What is a kubeconfig context?
3. What is the difference between `kubectl apply` and `kubectl create`?
4. How do you preview a change before applying it?
5. How do you debug a container that has no shell?
6. Why should you be careful with `kubectl edit` and `kubectl scale` in production?

**[Pods](../kubernetes/pods.md)**

1. What is a pod, and why does Kubernetes not schedule containers directly?
2. What do containers in the same pod share?
3. What is the difference between an init container and a sidecar container?
4. What does `CrashLoopBackOff` mean?
5. Why should you not create pods directly in production?
6. A pod shows `1/2` ready. How do you find out which container is the problem?

**[Deployments and rollouts](../kubernetes/deployments-and-rollouts.md)**

1. How does a Deployment perform a rolling update?
2. What do `maxSurge` and `maxUnavailable` control?
3. What is the relationship between a Deployment, ReplicaSets and pods?
4. You deployed a bad image. What happens, and how do you recover?
5. Why is a readiness probe important for rolling updates?
6. When would you use the `Recreate` strategy?
7. You changed a ConfigMap, but the pods still use the old values. Why, and what do you do?

**[StatefulSets and DaemonSets](../kubernetes/statefulsets-and-daemonsets.md)**

1. When do you use a StatefulSet instead of a Deployment?
2. What is a headless Service, and why does a StatefulSet need one?
3. What happens to a StatefulSet's volumes when you scale down or delete a pod?
4. Does a StatefulSet replicate data or handle failover?
5. What is a DaemonSet, and what typically runs as one?
6. A StatefulSet's first pod is stuck `Pending`. What do you check?

**[Jobs and CronJobs](../kubernetes/jobs-and-cronjobs.md)**

1. When do you use a Job instead of a Deployment?
2. What do `completions`, `parallelism` and `backoffLimit` do?
3. What are the CronJob concurrency policies?
4. Why must CronJob work be idempotent?
5. A CronJob scheduled at 02:30 ran at 08:00. Why?
6. How do you test a CronJob without waiting for its schedule?
7. A Job with a mesh sidecar never completes. Why, and how do you fix it?

**[Labels, selectors and namespaces](../kubernetes/labels-selectors-namespaces.md)**

1. What is the difference between labels and annotations?
2. How does a Service know which pods to send traffic to?
3. Are namespaces a security boundary?
4. What do ResourceQuota and LimitRange do?
5. A Deployment shows `3/5` and no pods are failing. What do you check?
6. Why is an empty selector dangerous?

**[ConfigMaps and Secrets](../kubernetes/configmaps-and-secrets.md)**

1. What is the difference between a ConfigMap and a Secret?
2. Is a Kubernetes Secret secure? What makes it more secure?
3. You updated a ConfigMap, but the application still uses the old value. Why?
4. What does `CreateContainerConfigError` mean?
5. Why might someone who cannot `get secrets` still read one?
6. What are immutable ConfigMaps for?

**[Probes and graceful shutdown](../kubernetes/probes-and-graceful-shutdown.md)**

1. What is the difference between liveness, readiness and startup probes?
2. Why should a liveness probe not check the database?
3. What happens, in order, when a pod is deleted?
4. Users see errors during every rolling update. What do you check?
5. A slow-starting app keeps restarting with no errors in its logs. Why?
6. Why add a `preStop` sleep if the app already handles SIGTERM?

**[Requests, limits and QoS](../kubernetes/resources-and-qos.md)**

1. What is the difference between requests and limits?
2. What happens when a container exceeds its CPU limit, and its memory limit?
3. What are the QoS classes and how are they assigned?
4. A pod is `Pending` with `Insufficient memory`, but the nodes' memory usage is low. Why?
5. Should you set CPU limits?
6. How do you choose requests and limits for a new service?

**[Scheduling](../kubernetes/scheduling.md)**

1. How does the scheduler choose a node for a pod?
2. What is the difference between a taint and node affinity?
3. A pod is `Pending`. How do you find out why?
4. How do you spread replicas across availability zones?
5. What do the `NoSchedule`, `PreferNoSchedule` and `NoExecute` taint effects do?
6. What is preemption?

**[Services and DNS](../kubernetes/services-and-dns.md)**

1. What is a Kubernetes Service, and why do we need it?
2. Explain ClusterIP, NodePort, LoadBalancer and headless Services.
3. What is the difference between `port`, `targetPort` and `nodePort`?
4. A Service returns "connection refused". Walk through your checks.
5. How does DNS work for Services, and what is `ndots:5`?
6. Why might load not be balanced evenly across pods behind a Service?

**[Ingress and Gateway API](../kubernetes/ingress-and-gateway-api.md)**

1. What is the difference between an Ingress and an ingress controller?
2. Why is Gateway API replacing Ingress?
3. Name the main Gateway API objects and who typically owns each.
4. What happened to ingress-nginx, and what would you do about a cluster still using it?
5. An Ingress returns 503 for every request. How do you debug it?
6. How would you route 10% of traffic to a new version?
7. Why put TLS termination at the ingress layer, and what are the trade-offs?

**[Pod networking and NetworkPolicy](../kubernetes/pod-networking-and-network-policy.md)**

1. What is the Kubernetes network model?
2. What does a CNI plugin do?
3. Explain how NetworkPolicy evaluates traffic.
4. You applied a default-deny egress policy and the application broke completely. Why?
5. A NetworkPolicy seems to do nothing. What do you check?
6. How do you isolate namespaces from each other?

**[Storage](../kubernetes/storage.md)**

1. Explain PersistentVolume, PersistentVolumeClaim and StorageClass.
2. What are the access modes, and which work with EBS and EFS?
3. Why use `WaitForFirstConsumer`?
4. What does the reclaim policy control?
5. A pod with a PVC is stuck `ContainerCreating` with `Multi-Attach error`. What happened?
6. How do you grow a volume used by a StatefulSet?

**[Autoscaling](../kubernetes/autoscaling.md)**

1. How does the HPA decide how many replicas to run?
2. An HPA shows `<unknown>` for its target. What do you check?
3. Why does a CPU utilisation target depend on requests?
4. What are the differences between HPA, VPA and a node autoscaler?
5. Why is scale-down slower than scale-up by default?
6. A queue worker should scale on queue length, including down to zero. How?
7. Traffic spiked, the HPA scaled out, but users still saw errors for three minutes. Why, and what would you change?

**[Disruptions, drains and PDBs](../kubernetes/disruptions-and-pdbs.md)**

1. What is a PodDisruptionBudget, and what does it protect against?
2. What is the difference between voluntary and involuntary disruptions?
3. A `kubectl drain` hangs. What do you check?
4. What is wrong with `minAvailable: 1` on a single-replica Deployment?
5. What do cordon, drain and uncordon do?
6. How would you upgrade the nodes of a cluster without downtime?

**[RBAC and service accounts](../kubernetes/rbac-and-service-accounts.md)**

1. What is the difference between a Role and a ClusterRole, and a RoleBinding and a ClusterRoleBinding?
2. How does a pod authenticate to the API server?
3. How do you check whether a service account can delete pods?
4. Why is `create pods` a sensitive permission?
5. What is the difference between `Unauthorized` and `Forbidden`?
6. Design RBAC for a team that should manage its own namespace but nothing else.

**[Pod security](../kubernetes/pod-security.md)**

1. What are the three Pod Security Standards levels?
2. How do you apply Pod Security Admission to a namespace, and what are its modes?
3. A Deployment was applied successfully but has zero pods. The namespace enforces restricted. Why?
4. What do `runAsNonRoot`, `allowPrivilegeEscalation: false` and `capabilities.drop: ["ALL"]` each protect against?
5. What is `fsGroup` for?
6. A vendor's chart needs `privileged: true`. What do you do?

**[Finalizers and deletion](../kubernetes/finalizers-and-deletion.md)**

1. What is a finalizer, and what happens when you delete an object that has one?
2. A namespace has been `Terminating` for an hour. How do you investigate?
3. Explain background, foreground and orphan cascading deletion.
4. What is the risk of removing a finalizer by hand?
5. Why might a PVC stay in `Terminating`?
6. How do you replace a StatefulSet's spec field that cannot be changed, without restarting its pods?
7. You need to delete all resources labelled `app=old`. How do you do it safely?

**[CRDs, operators and admission webhooks](../kubernetes/crds-and-operators.md)**

1. What is the difference between a CRD and an operator?
2. Describe the order of admission control.
3. A webhook's pods crashed and now nobody can create pods. What happened, and how do you recover?
4. When would you use a ValidatingAdmissionPolicy instead of a webhook?
5. What is the status subresource of a custom resource for?
6. How does Istio get a sidecar into your pod?
7. You are about to uninstall an operator. What do you check first?

**[etcd, backups and cluster upgrades](../kubernetes/etcd-backups-and-upgrades.md)**

1. Why do etcd clusters have an odd number of members?
2. What happens to running pods if etcd loses quorum?
3. How do you back up and restore etcd?
4. What is the correct order for a Kubernetes upgrade?
5. How do you find out whether an upgrade will break any manifests?
6. On EKS you cannot reach etcd. How do you back up the cluster?
7. How long is a Kubernetes minor release supported?

**[Troubleshooting playbook](../kubernetes/troubleshooting.md)**

1. A pod is `Pending`. What do you check?
2. What is the difference between `ImagePullBackOff` and `CrashLoopBackOff`?
3. A pod restarts every few minutes with exit code 137. What could it be, and how do you tell?
4. Pods are Running and Ready, but the Service times out. Walk through it.
5. How do you debug a container whose image has no shell?
6. `kubectl logs` shows nothing useful for a crash-looping pod. What next?
7. A node shows `NotReady`. What happens to its pods, and what do you check?
8. A pod works in namespace `a` but calls to `web` fail after moving it to namespace `b`. Why?

## EKS


**[EKS architecture and node options](../eks/architecture.md)**

1. What does AWS manage in EKS, and what do you manage?
2. Compare managed node groups, Fargate and Karpenter.
3. What are the endpoint access options, and which would you choose for production?
4. How does kubectl authenticate to EKS?
5. What is the difference between the cluster IAM role and the node IAM role?
6. New nodes in private subnets never join the cluster. What do you check?
7. When would you choose EKS Auto Mode?

**[Cluster access, IRSA and Pod Identity](../eks/access-and-pod-identity.md)**

1. How do you give a new engineer read-only access to one namespace on EKS?
2. Explain how IRSA works end to end.
3. How does EKS Pod Identity differ from IRSA?
4. Why should application permissions not go on the node IAM role?
5. A pod gets AccessDenied calling S3. Walk through your debugging.
6. What is the risk of an IRSA trust policy without a `sub` condition?
7. You are migrating a cluster from `aws-auth` to access entries. What are the steps and risks?

**[Networking with the VPC CNI](../eks/vpc-cni.md)**

1. How does the VPC CNI give pods IP addresses?
2. Why can a node with free CPU and memory not run more pods?
3. What does prefix delegation change?
4. The cluster's subnets are running out of addresses. What are your options?
5. Why is pod traffic to the internet seen with the node's address?
6. When would you use security groups for pods?

**[AWS Load Balancer Controller](../eks/load-balancer-controller.md)**

1. What does the AWS Load Balancer Controller do?
2. Explain `target-type: ip` versus `instance`.
3. An Ingress was applied an hour ago and still has no address. What do you check?
4. How do you share one ALB between several Ingresses, and what is the risk?
5. Users see 502 errors for a few seconds on every deploy. How do you fix it?
6. What is a TargetGroupBinding for?

**[EBS and EFS CSI drivers](../eks/storage.md)**

1. When would you use EBS and when EFS on EKS?
2. Why does `WaitForFirstConsumer` matter for EBS?
3. A StatefulSet pod is stuck Pending with `volume node affinity conflict`. What happened?
4. An EFS mount times out. What do you check?
5. What is an EFS access point and why use one per application?
6. How do the CSI drivers get permission to create volumes?

**[Secrets from AWS into pods](../eks/secrets.md)**

1. Compare the External Secrets Operator and the Secrets Store CSI driver.
2. A secret was rotated in Secrets Manager. Will running pods see it?
3. How do pods authenticate to Secrets Manager on EKS?
4. Are Kubernetes Secrets encrypted on EKS?
5. Why commit an ExternalSecret instead of a Secret to Git?
6. An ExternalSecret shows a sync error after someone added a KMS key to the secret. What happened?

**[Node autoscaling: Cluster Autoscaler vs Karpenter](../eks/cluster-autoscaler-vs-karpenter.md)**

1. How does Cluster Autoscaler decide to add a node?
2. When does Cluster Autoscaler remove a node?
3. What is the main difference in how Karpenter adds capacity?
4. Pods are Pending but the autoscaler does nothing. How do you investigate?
5. Why run the autoscaler on a separate, fixed node group?
6. A team complains their pods restart every few hours since moving to Karpenter. What is happening and what do you change?

**[Karpenter in depth](../eks/karpenter.md)**

1. What are NodePool, EC2NodeClass and NodeClaim?
2. Walk through what happens when a pod is Pending in a Karpenter cluster.
3. Explain consolidation, drift and expiration.
4. How do you stop Karpenter from disrupting a running batch job?
5. How does Karpenter handle Spot interruptions?
6. Karpenter keeps logging that no instance type meets the pod's requirements. What do you check?
7. What protects production from Karpenter replacing too many nodes at once?

**[EKS upgrades](../eks/upgrades.md)**

1. What is the order of an EKS upgrade?
2. How do you find out whether workloads use APIs removed in the next version?
3. Can you roll back an EKS upgrade?
4. How does a managed node group update work, and what can make it fail?
5. How do Karpenter-managed nodes get upgraded?
6. When would you choose a blue-green cluster upgrade over in-place?
7. Why not stay on an old version with extended support?

## Helm


**[Charts, templates and values](../helm/charts-and-templates.md)**

1. What problem does Helm solve, and what is a chart?
2. What is the order of values precedence?
3. What is the difference between `include` and `template`?
4. How do you debug a chart that fails with a YAML parse error?
5. How would you make a value mandatory?
6. How do you stop a chart's replica count fighting an HPA?

**[Releases, hooks and debugging](../helm/releases-hooks-debugging.md)**

1. What is a Helm release, and where is its state stored?
2. How does `helm rollback` work, and what does it not undo?
3. A deploy fails with "another operation is in progress". What happened and how do you fix it?
4. How would you run a database migration with Helm?
5. What does `--rollback-on-failure` do (formerly `--atomic`)?
6. How do you see exactly what is deployed and with which values?

**[Kustomize, and Helm vs Kustomize](../helm/kustomize-vs-helm.md)**

1. What is the core idea of Kustomize?
2. Why do generated ConfigMaps have a hash suffix?
3. When would you choose Helm and when Kustomize?
4. Why is `labels` preferred over `commonLabels`?
5. A patch in the prod overlay does nothing. How do you debug it?
6. How do you change the image tag per environment with Kustomize?

## Service mesh


**[Why a mesh, and Istio architecture](../mesh/why-a-mesh.md)**

1. What problems does a service mesh solve?
2. Explain Istio's data plane and control plane.
3. What is xDS?
4. Sidecar mode or ambient mode?
5. What does a mesh cost you?
6. When would you not use a service mesh?

**[Sidecars and traffic flow](../mesh/sidecars-and-traffic-flow.md)**

1. How does a sidecar get into a pod?
2. How is traffic redirected into Envoy?
3. Why do Service port names matter in Istio?
4. What startup and shutdown problems do sidecars cause, and how are they solved?
5. Describe the path of a request between two meshed pods.
6. How would you reduce sidecar overhead in a large mesh?

**[Traffic management](../mesh/traffic-management.md)**

1. What do VirtualService and DestinationRule each do?
2. How do you run a canary with Istio?
3. What is outlier detection?
4. What are Istio's default retries and timeouts?
5. How do Istio resources map to Envoy configuration?
6. A canary at 10% receives no traffic. What do you check?

**[mTLS and authorization](../mesh/mesh-security.md)**

1. How does Istio identify workloads?
2. PERMISSIVE vs STRICT?
3. How are AuthorizationPolicies evaluated?
4. Does RequestAuthentication require a token?
5. What does mTLS not protect you from?
6. After switching a namespace to STRICT, a CronJob starts failing. Why?

**[Mesh troubleshooting](../mesh/mesh-troubleshooting.md)**

1. How do you start debugging a 503 in an Istio mesh?
2. What does `istioctl proxy-status` tell you?
3. What do the response flags UH, UF and NR mean?
4. How do you tell an application error from a mesh error?
5. What is `istioctl proxy-config` used for?
6. A VirtualService weight change has no effect. What do you check?

## Infrastructure as code


**[Terraform workflow](../iac/terraform-workflow.md)**

1. What happens during `terraform init`, `plan` and `apply`?
2. What is the difference between a resource and a data source?
3. How does Terraform decide the order of operations?
4. Why commit `.terraform.lock.hcl`?
5. Why save a plan in CI instead of running `apply` directly?
6. A colleague changed a security group in the console. What happens on the next plan?

**[Terraform state](../iac/state.md)**

1. Why does Terraform need state?
2. How do you set up remote state on AWS today?
3. What sensitive data can end up in state, and how do you protect it?
4. A pipeline was killed during apply and now the state is locked. What do you do?
5. How do you rename a resource without destroying it?
6. How would you split state for a company with several environments and teams?

**[Terraform language](../iac/language.md)**

1. What is the difference between `count` and `for_each`?
2. When would you use `create_before_destroy`?
3. What does `ignore_changes` do and what is the risk?
4. What does `cidrsubnet("10.0.0.0/16", 8, 3)` return?
5. Why might `for_each` fail with "known only after apply"?
6. Does `prevent_destroy` protect a resource if someone deletes its block?

**[Modules and environments](../iac/modules-and-environments.md)**

1. What is a Terraform module, and what is the root module?
2. How do you version modules, and why?
3. Directories per environment or workspaces? Defend a choice.
4. How do you move resources into a module without recreating them?
5. What makes a module well designed?
6. How would you roll out a risky change to a shared VPC module across ten accounts?

**[Reading a plan](../iac/reading-a-plan.md)**

1. What do `~`, `-/+` and `+/-` mean in a plan?
2. What does `# forces replacement` tell you, and why does it matter?
3. Why apply a saved plan file in CI?
4. When is `-target` acceptable?
5. How would you automatically block plans that delete databases?
6. A plan for a tags-only change wants to replace three NAT gateways. What do you do?

**[Import, moved and drift](../iac/import-and-drift.md)**

1. How do you bring an existing resource under Terraform?
2. You renamed a resource and the plan wants to destroy and recreate it. Fix it.
3. How do you stop managing a resource without deleting it?
4. How do you detect drift automatically?
5. Someone changed a security group in the console during an incident. What do you do?
6. What are the risks of `-generate-config-out`?

**[Testing and CI for Terraform](../iac/testing-and-ci.md)**

1. Describe a CI/CD pipeline for Terraform.
2. Why apply a saved plan, and what if it is stale?
3. What do TFLint, Trivy and Checkov each add over `terraform validate`?
4. What is `terraform test` and when would you use `command = plan`?
5. How do you make sure only reviewed code can change production?
6. A plan in CI shows changes nobody made in this pull request. What do you do?

**[Terragrunt](../iac/terragrunt.md)**

1. What problem does Terragrunt solve?
2. How do `include`, `remote_state` and `generate` work together?
3. What are `dependency` blocks and `mock_outputs` for?
4. How do you run Terragrunt across many units, and what changed recently?
5. When would you not use Terragrunt?
6. How do you promote a module change through environments with Terragrunt?

**[CloudFormation and CDK vs Terraform](../iac/cloudformation-vs-terraform.md)**

1. What is a CloudFormation change set, and how does it compare to a Terraform plan?
2. What happens when a CloudFormation update fails, compared with Terraform?
3. What does CDK add on top of CloudFormation?
4. When would you choose Terraform over CloudFormation?
5. How do you deploy the same infrastructure to many AWS accounts with each tool?

**[Ansible and configuration management](../iac/ansible.md)**

1. What is the difference between provisioning and configuration management?
2. What does "agentless" mean for Ansible?
3. What makes an Ansible task idempotent?
4. What are handlers for?
5. Where does Ansible fit in a Kubernetes and Terraform world?

## CI/CD


**[CI/CD concepts](../cicd/concepts.md)**

1. What is the difference between continuous delivery and continuous deployment?
2. What does "build once, promote the same artifact" mean, and why?
3. Describe the stages of a typical pipeline.
4. How do you keep a pipeline fast?
5. What metrics tell you whether delivery is healthy?
6. A deploy broke production even though all pipeline checks passed. What do you change?

**[Deployment strategies](../cicd/deployment-strategies.md)**

1. Compare rolling, blue-green and canary deployments.
2. How do you implement blue-green on Kubernetes?
3. What is a feature flag and how does it change deployment risk?
4. How do you change a database schema safely with zero-downtime deploys?
5. When would you roll forward instead of rolling back?
6. A canary at 5% shows the same error rate as the stable version, but users complain after full rollout. What went wrong?

**[GitHub Actions basics](../cicd/github-actions-basics.md)**

1. Explain workflow, job, step, action and runner.
2. How do jobs share data?
3. What is `GITHUB_TOKEN` and how do you limit it?
4. What does `concurrency` do in the Pages workflow?
5. Why are secrets not available to pull requests from forks?
6. A workflow did not run after a push. How do you find out why?

**[GitHub Actions in depth](../cicd/github-actions-in-depth.md)**

1. When would you use a reusable workflow versus a composite action?
2. How do you require approval before deploying to production?
3. Why pin actions to a commit SHA, and what does GitHub now recommend?
4. What is the risk of `pull_request_target`?
5. What are the risks of self-hosted runners?
6. A workflow fails only sometimes. How do you debug it?

**[Jenkins](../cicd/jenkins.md)**

1. Explain the controller and agent architecture.
2. Declarative vs scripted pipelines?
3. What is a shared library and why use one?
4. How do you use secrets safely in a Jenkinsfile?
5. How do you run Jenkins agents on Kubernetes?
6. Builds queue for a long time. What do you check?

**[Bitbucket Pipelines](../cicd/bitbucket-pipelines.md)**

1. Describe the structure of `bitbucket-pipelines.yml`.
2. What is the difference between caches and artifacts?
3. How do deployments and variables work together?
4. How do you deploy to AWS from Bitbucket without stored keys?
5. What is a pipe?

**[OIDC from pipelines to AWS](../cicd/oidc-to-aws.md)**

1. Why use OIDC instead of access keys in CI?
2. Walk through the OIDC flow from a GitHub Actions job to AWS.
3. Why must the trust policy pin `sub`?
4. A job fails with "Not authorized to perform sts:AssumeRoleWithWebIdentity". Debug it.
5. How does Bitbucket's OIDC differ from GitHub's?
6. How would you design roles for plan and deploy?

**[Pipeline security](../cicd/pipeline-security.md)**

1. Why is the CI/CD pipeline an attractive target?
2. What is poisoned pipeline execution?
3. How do you prevent script injection in GitHub Actions?
4. How should secrets be handled in pipelines?
5. What are SBOMs, provenance and signing for?
6. A popular third-party action was compromised yesterday. What do you do?

**[Quality and security gates](../cicd/quality-and-security-gates.md)**

1. What is the difference between SAST, SCA and DAST?
2. What is a SonarQube quality gate?
3. How do you decide whether a finding fails the build or only warns?
4. A critical CVE is reported in a base image used by 30 services. What do you do?
5. How do you keep security scanning from slowing delivery?
6. A secret was committed and pushed. What now?

**[Build tools: Maven, Gradle, npm](../cicd/build-tools.md)**

1. What happens when you run `mvn package`?
2. Why commit the Gradle wrapper?
3. What is the difference between `npm install` and `npm ci`?
4. How do you make builds faster in CI?
5. What is a SNAPSHOT version and why not deploy one to production?

**[Artifacts and registries](../cicd/artifacts-and-registries.md)**

1. What are hosted, proxy and group repositories?
2. Why put a proxy repository in front of public registries?
3. What does "immutable artifact" mean and why does it matter?
4. How do you promote an artifact from staging to production?
5. How are Helm charts stored in container registries?
6. What retention policy would you set for an image repository?

## GitOps and Argo CD


**[GitOps principles](../gitops/principles.md)**

1. What is GitOps?
2. Compare push-based CI/CD with pull-based GitOps.
3. Why separate the config repository from the application repository?
4. What does GitOps not solve by itself?
5. An engineer scaled a Deployment by hand during an incident; ten minutes later it went back. Why, and what should they have done?
6. How would you structure a config repository for three environments?

**[Argo CD architecture and Applications](../gitops/argocd-architecture.md)**

1. Describe Argo CD's main components.
2. What does an Application define?
3. What is the difference between sync status and health status?
4. What is an AppProject for?
5. How does a commit reach the cluster, and how fast?
6. An Application shows `Unknown` sync status with a comparison error. What do you check?

**[Sync, hooks and waves](../gitops/sync-hooks-waves.md)**

1. What is the difference between refresh, hard refresh and sync?
2. What do `prune` and `selfHeal` do, and what are their defaults?
3. How do you run a database migration before the new version starts?
4. What are sync waves?
5. An app is always OutOfSync on `spec.replicas`. Why, and how do you fix it?
6. How do Helm hooks behave under Argo CD?

**[App-of-apps and ApplicationSets](../gitops/app-of-apps-and-applicationsets.md)**

1. What is the app-of-apps pattern?
2. What is an ApplicationSet and what are generators?
3. When would you use app-of-apps and when ApplicationSets?
4. How can one ApplicationSet change cause an outage, and how do you prevent it?
5. How do you deploy an add-on to every production cluster?
6. How do you build preview environments per pull request with Argo CD?

**[Deletion, finalizers and safe cleanup](../gitops/deletion-and-finalizers.md)**

1. What happens when you delete an Argo CD Application?
2. How do you protect a PVC from being deleted with its Application?
3. How do you move resources from one Application to another without downtime?
4. How can a single change delete many applications in an app-of-apps or ApplicationSet setup?
5. An Application has been "deleting" for an hour. What do you check?
6. What does `Prune=confirm` do?

**[Promotion, rollback and troubleshooting](../gitops/promotion-and-rollback.md)**

1. How do you deploy a new version with GitOps?
2. How do you promote from staging to production?
3. How do you roll back, and why not with `argocd app rollback`?
4. An application is OutOfSync. Walk through your triage.
5. Production is Degraded right after a deploy. What do you do?
6. Someone changed a Deployment by hand and it keeps reverting. Explain.

## Observability


**[Signals and methods](../observability/signals-and-methods.md)**

1. What are metrics, logs and traces each best for?
2. Explain RED and USE.
3. What are the four golden signals?
4. What is cardinality and why does it matter?
5. What is the difference between monitoring and observability?
6. What would you monitor for a new web API before launch?

**[Prometheus](../observability/prometheus.md)**

1. How does Prometheus collect metrics, and why pull?
2. Explain counter, gauge, histogram and summary.
3. What is a time series in Prometheus?
4. What causes high cardinality and how do you fix it?
5. When should you use the Pushgateway?
6. What are kube-state-metrics and node_exporter for?

**[PromQL](../observability/promql.md)**

1. What is the difference between an instant vector and a range vector?
2. Explain `rate`, `irate` and `increase`.
3. Why must you take `rate()` before `sum()`?
4. Write a query for the error ratio of a service.
5. How do you compute p99 latency across all pods?
6. What are recording rules and how should they be named?

**[Prometheus on Kubernetes](../observability/prometheus-on-kubernetes.md)**

1. What does kube-prometheus-stack install?
2. What is a ServiceMonitor, and how does Prometheus find it?
3. You created a ServiceMonitor but the target never appears. What do you check?
4. ServiceMonitor or PodMonitor?
5. How do you add an alert rule for your application?

**[Alerting and Alertmanager](../observability/alerting.md)**

1. What do Prometheus and Alertmanager each do in alerting?
2. What do `for` and `keep_firing_for` do?
3. Explain grouping, inhibition and silences.
4. Why alert on symptoms rather than causes?
5. What should a good alert notification contain?
6. The on-call engineer gets 40 pages a week, mostly ignored. What do you do?

**[SLOs and error budgets](../observability/slos.md)**

1. What are SLI, SLO and SLA?
2. What is the error budget for 99.9% over 30 days?
3. What is a burn rate and why alert on it?
4. Why use multi-window burn-rate alerts?
5. How would you choose SLIs for an API?
6. The error budget is exhausted halfway through the month. What happens?

**[Grafana](../observability/grafana.md)**

1. What is a Grafana data source and why does it matter for queries?
2. How do variables make dashboards reusable?
3. How do you manage dashboards as code?
4. Grafana alerting or Alertmanager?
5. How would you lay out a service dashboard?

**[How Kubernetes logging works](../observability/kubernetes-logging.md)**

1. Where do container logs go in Kubernetes?
2. What does `kubectl logs` actually read?
3. How would you collect logs from every pod in a cluster?
4. When are logs lost?
5. What is the CRI log format?
6. Why prefer structured (JSON) logs?

**[Fluent Bit](../observability/fluent-bit.md)**

1. Describe the Fluent Bit pipeline.
2. How does Fluent Bit avoid re-reading or skipping logs after a restart?
3. What does the kubernetes filter do?
4. Memory vs filesystem buffering?
5. Logs went missing during a 10-minute OpenSearch outage. Why, and how do you prevent it?
6. How do you handle multiline stack traces?

**[OpenSearch](../observability/opensearch.md)**

1. Explain index, shard and replica.
2. What do green, yellow and red mean?
3. What is mapping explosion and how do you prevent it?
4. Writes suddenly fail with an index read-only error. Why?
5. How do you manage log index lifecycle?
6. Fluent Bit reports HTTP 429 from OpenSearch. What do you do?

**[Tracing and OpenTelemetry](../observability/tracing.md)**

1. What are a trace and a span?
2. How does context propagate between services?
3. Head vs tail sampling?
4. What does the OpenTelemetry Collector do?
5. With Istio installed, why might traces still be broken?

## Security


**[OAuth 2.0, OIDC and JWTs](../security/oauth-oidc-jwt.md)**

1. What is the difference between authentication and authorisation, and between OAuth and OIDC?
2. Walk through the authorization code flow with PKCE.
3. What is inside a JWT and how do you validate one?
4. When would you use the client credentials flow?
5. What is the difference between an ID token and an access token?
6. How do CI pipelines and pods use these ideas to reach AWS?

**[Secrets management](../security/secrets-management.md)**

1. Where should secrets never be stored?
2. Describe the secret lifecycle.
3. How do you manage secrets with GitOps?
4. Why can rotating a secret break an application, and how do you avoid it?
5. A developer pushed an AWS access key to GitHub. What do you do?
6. What is better than a well-managed long-lived secret?

**[Vulnerability and patch management](../security/vulnerability-and-patch-management.md)**

1. What are CVE, CVSS, EPSS and KEV?
2. How do you prioritise vulnerability findings?
3. How do you patch containers?
4. How do you patch a fleet of EC2 instances or EKS nodes safely?
5. What metrics show whether vulnerability management works?
6. A critical CVE is announced in a base image used everywhere. Walk through your response.

**[Hardening and benchmarks](../security/hardening-and-benchmarks.md)**

1. What does hardening mean, and how do you start?
2. What are CIS Benchmarks and how are they used?
3. List cloud posture basics you would check in a new AWS account.
4. How would you harden an EKS cluster?
5. Why prefer preventive controls over detective ones?
6. A scanner reports 400 benchmark failures across your accounts. How do you approach it?

**[Guardrails for AI agents in operations](../security/ai-agent-guardrails.md)**

1. Why is an AI agent with shell access a new kind of risk?
2. What is the difference between an instruction and a hook as a control?
3. How would you set up identities for an operations agent?
4. What should happen before an agent makes a change?
5. What are the limits of human approval?
6. What would you audit for agent activity?

## Operations


**[High availability and failure domains](../operations/high-availability.md)**

1. What failure domains do you design for, and how?
2. Compute the availability of two 99.9% components in series and in parallel.
3. Why add jitter to retries?
4. How do you make a Kubernetes workload survive the loss of a zone?
5. What is a circuit breaker?
6. Your service is 99.99% available but depends on a 99.9% database. What can you promise?

**[Backup and disaster recovery](../operations/backup-and-dr.md)**

1. What are RPO and RTO?
2. Describe the four DR strategies on AWS.
3. Why is replication not a backup?
4. If you run everything with GitOps, what still needs backing up?
5. How do you know your backups work?
6. Design backups for a production database with a 15-minute RPO.

**[Cost optimisation](../operations/cost-optimisation.md)**

1. How would you start reducing an AWS bill?
2. Compare On-Demand, Spot, Savings Plans and Reserved Instances.
3. Why can a Kubernetes cluster be expensive even when nodes look full?
4. How do NAT gateways become a large cost, and what do you do?
5. How do you keep costs under control without slowing teams?
6. What would you not cut to save money?

**[Incident response and postmortems](../operations/incident-response.md)**

1. Walk me through how you handle a production incident.
2. What does an incident commander do?
3. Why mitigate before finding the root cause?
4. What makes a postmortem blameless, and why does it matter?
5. What goes into a postmortem?
6. Tell me about an incident you handled. (How to structure the answer)

**[Change management](../operations/change-management.md)**

1. Why do changes cause most incidents, and what reduces the risk?
2. What do you do before making a risky production change?
3. What does "reversible steps first" mean?
4. How much review should a change get?
5. A change went wrong halfway through. What now?

**[Migration patterns](../operations/migration-patterns.md)**

1. What are rehost, replatform and refactor?
2. How would you move a stateful service from VMs to Kubernetes?
3. What is the strangler fig pattern?
4. How do you migrate a database with minimal downtime?
5. What does a good rollback plan for a migration contain?
6. When is a migration finished?

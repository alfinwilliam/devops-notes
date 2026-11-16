---
title: "X vs Y: rapid-fire differences"
status: draft
form: guide
commands: none
---

# X vs Y: rapid-fire differences

> **Status: AI draft, 2026-11-16.** Not yet verified by me. Summaries of the linked pages; each table links to the page that explains it properly.

## In one line

Interviewers love "what's the difference between X and Y?" because it tests whether you know both well enough to choose. Answer with the deciding difference first, then two or three supporting points, then when you would pick each. These tables are the short versions; the linked pages have the depth.

## Networking and AWS

### Security group vs NACL

| Aspect | Security group | Network ACL |
|---|---|---|
| Attached to | Network interface (instance, pod, endpoint) | Subnet |
| State | Stateful: return traffic allowed automatically | Stateless: return traffic needs its own rule (ephemeral ports) |
| Rules | Allow only; all rules evaluated | Allow and deny; numbered, first match wins |
| Typical use | Main control for every workload | Coarse subnet-wide blocks |

Home: [Security groups and NACLs](../aws-core/security-groups-and-nacls.md)

### ALB vs NLB

| Aspect | ALB | NLB |
|---|---|---|
| Layer | 7 (HTTP, HTTPS, gRPC) | 4 (TCP, UDP, TLS) |
| Routing | Host, path, header rules; redirects; auth | Port-based forwarding |
| Addresses | DNS name only | Static IP per zone (Elastic IPs possible) |
| Pick when | Web apps and APIs with routing needs | Non-HTTP, static IPs, extreme throughput, PrivateLink |

Home: [ALB and NLB](../aws-core/load-balancers.md)

### Internet gateway vs NAT gateway

| Aspect | Internet gateway | NAT gateway |
|---|---|---|
| Direction | Both ways, for resources with public IPs | Outbound only, for private subnets |
| Lives | Attached to the VPC | In a public subnet, one per zone for resilience |
| Cost | No hourly charge | Hourly plus per-GB processing |

Home: [NAT, endpoints and PrivateLink](../aws-core/nat-endpoints-privatelink.md)

### TCP vs UDP

| Aspect | TCP | UDP |
|---|---|---|
| Connection | Handshake, ordered, retransmits losses | No connection, no ordering, no retransmit |
| Overhead | Higher, congestion control | Lower |
| Used by | HTTP/1.1 and HTTP/2, SSH, databases | DNS queries, QUIC (HTTP/3), streaming, NTP |

Home: [TCP and UDP](../networking/tcp-and-udp.md)

### 502 vs 503 vs 504

| Code | Means | Usual cause behind a proxy or load balancer |
|---|---|---|
| 502 Bad Gateway | The upstream gave an invalid response or closed the connection | App crashed, wrong port, keep-alive timeout mismatch |
| 503 Service Unavailable | No healthy upstream, or deliberately shedding load | All targets unhealthy, no endpoints, maintenance |
| 504 Gateway Timeout | The upstream did not answer in time | Slow app or database, proxy timeout shorter than the work |

Home: [HTTP](../networking/http.md), [Load balancers and proxies](../networking/load-balancers-and-proxies.md)

### IAM role vs IAM user

| Aspect | IAM user | IAM role |
|---|---|---|
| Credentials | Long-term (password, access keys) | Temporary, from STS when assumed |
| Who | One person or system | Anyone allowed by its trust policy: services, users, other accounts, OIDC identities |
| Preferred for | Almost nothing today (break-glass at most) | Workloads, CI, people through SSO |

Home: [Roles and STS](../aws-core/iam-roles-and-sts.md)

### Identity policy vs resource policy

| Aspect | Identity policy | Resource policy |
|---|---|---|
| Attached to | User, group or role | The resource (bucket, key, queue, role trust) |
| Names a principal | No (the principal is whoever has it) | Yes, the `Principal` element |
| Cross-account | Needed on the caller's side | Needed on the resource's side; both must allow |

Home: [IAM policies and evaluation](../aws-core/iam-policies.md)

### EBS vs EFS vs S3

| Aspect | EBS | EFS | S3 |
|---|---|---|---|
| Kind | Block volume | NFS file system | Object store over HTTPS |
| Shared | One instance (Multi-Attach for some io volumes) | Many clients, many zones | Anyone with permissions |
| Scope | One zone | Region (or One Zone) | Region |
| Use | Boot disks, databases | Shared files, ReadWriteMany | Assets, backups, logs, data lakes |

Home: [EBS](../aws-services/ebs.md), [EFS](../aws-services/efs.md), [S3](../aws-services/s3.md)

### Multi-AZ vs read replica

| Aspect | Multi-AZ (DB instance) | Read replica |
|---|---|---|
| Purpose | Availability | Read scaling, reporting, DR copy |
| Replication | Synchronous | Asynchronous |
| Serves reads | No | Yes |
| Failover | Automatic | Manual promotion |

Home: [RDS and Aurora](../aws-services/rds-and-aurora.md)

### SQS vs SNS vs EventBridge

| Aspect | SQS | SNS | EventBridge |
|---|---|---|---|
| Model | Queue, consumers pull | Topic, pushes to subscribers | Bus, rules route by content |
| Fan-out | No (one consumer group) | Yes | Yes |
| Buffering | Yes, retention up to 14 days | No | Retries, archive and replay |

Home: [SQS, SNS and EventBridge](../aws-services/messaging.md)

### Secrets Manager vs Parameter Store

| Aspect | Secrets Manager | Parameter Store |
|---|---|---|
| Rotation | Built in | None |
| Cost | Per secret per month | Standard tier free |
| Use | Credentials that rotate | Configuration and simple secrets |

Home: [KMS, Secrets Manager and Parameter Store](../aws-services/kms-and-secrets.md)

### Terraform vs CloudFormation

| Aspect | Terraform | CloudFormation |
|---|---|---|
| Scope | Many providers (AWS, Kubernetes, GitHub...) | AWS only |
| State | A state file you store and lock | Managed by AWS in the stack |
| Preview | `terraform plan` | Change sets |
| Language | HCL | JSON or YAML (CDK generates it) |

Home: [CloudFormation and CDK vs Terraform](../iac/cloudformation-vs-terraform.md)

### count vs for_each

| Aspect | `count` | `for_each` |
|---|---|---|
| Addresses | By index: `aws_instance.web[0]` | By key: `aws_instance.web["api"]` |
| Removing a middle item | Shifts every later index: destroys and recreates | Only that key is destroyed |
| Use | N identical copies, or 0/1 toggles | Anything with a natural name |

Home: [Terraform language](../iac/language.md)

## Containers and Kubernetes

### CMD vs ENTRYPOINT

| Aspect | ENTRYPOINT | CMD |
|---|---|---|
| Role | The executable that always runs | Default arguments (or default command) |
| `docker run image args` | Args are appended to it | Args replace it |
| Override | `--entrypoint` | Any trailing arguments |

Use the exec form (`["app", "--port", "8080"]`) so the process gets signals directly. Home: [Images and Dockerfiles](../containers/images-and-dockerfiles.md)

### Docker vs containerd

| Aspect | Docker | containerd |
|---|---|---|
| What | A full developer toolchain: CLI, daemon, builds, Compose | A container runtime daemon: pull, unpack, run through runc |
| Kubernetes | Not used directly since dockershim was removed | Talks to the kubelet through CRI |
| Relation | Docker Engine uses containerd underneath | Images built by Docker run unchanged |

Home: [Runtimes](../containers/runtimes.md)

### Deployment vs StatefulSet vs DaemonSet

| Aspect | Deployment | StatefulSet | DaemonSet |
|---|---|---|---|
| Pods | Interchangeable, random names | Stable names (`db-0`), ordered start | One per node (or per selected node) |
| Storage | Shared or none | A volume per pod from a template | Usually host paths |
| Use | Stateless apps | Databases, quorum systems | Log shippers, CNI, node agents |

Home: [Deployments and rollouts](../kubernetes/deployments-and-rollouts.md), [StatefulSets and DaemonSets](../kubernetes/statefulsets-and-daemonsets.md)

### Readiness vs liveness vs startup probe

| Probe | On failure | Use for |
|---|---|---|
| Readiness | Pod removed from Service endpoints; not restarted | "Can I take traffic right now?" |
| Liveness | Container restarted | "Am I stuck beyond recovery?" |
| Startup | Other probes wait; restart if it never passes | Slow-starting apps |

Home: [Probes and graceful shutdown](../kubernetes/probes-and-graceful-shutdown.md)

### ConfigMap vs Secret

| Aspect | ConfigMap | Secret |
|---|---|---|
| Content | Non-sensitive configuration | Credentials, keys, tokens |
| Storage | Plain text | Base64 in the API; encrypted at rest only if the cluster enables it |
| Access | Usually broad read | Restrict with RBAC; avoid listing in logs |

Home: [ConfigMaps and Secrets](../kubernetes/configmaps-and-secrets.md)

### Requests vs limits

| Aspect | Requests | Limits |
|---|---|---|
| Used by | The scheduler, and CPU share under contention | The kernel, at runtime |
| CPU over it | Fine if spare CPU exists | Throttled |
| Memory over it | Possible eviction under node pressure | OOM-killed |

Home: [Requests, limits and QoS](../kubernetes/resources-and-qos.md)

### ClusterIP vs NodePort vs LoadBalancer

| Type | Reachable from | Notes |
|---|---|---|
| ClusterIP | Inside the cluster | Default; a virtual IP and DNS name |
| NodePort | Any node's IP on a high port | Adds to ClusterIP; rarely used directly |
| LoadBalancer | Outside, through a cloud load balancer | Adds to NodePort or targets pod IPs directly |

Home: [Services and DNS](../kubernetes/services-and-dns.md)

### Cluster Autoscaler vs Karpenter

| Aspect | Cluster Autoscaler | Karpenter |
|---|---|---|
| Scales | Existing node groups (Auto Scaling groups) | Launches instances directly from NodePools |
| Instance choice | Fixed per node group | Picks types to fit pending pods |
| Scale-down | Removes underused nodes | Consolidates: replaces nodes with cheaper or fewer ones |

Home: [Cluster Autoscaler vs Karpenter](../eks/cluster-autoscaler-vs-karpenter.md)

### Helm vs Kustomize

| Aspect | Helm | Kustomize |
|---|---|---|
| Approach | Templates plus values | Plain YAML plus overlays and patches |
| Extras | Packaging, versions, release history, rollback, hooks | Built into `kubectl -k`; nothing installed in the cluster |
| Pick when | Distributing or consuming packaged apps | Your own manifests with small per-environment changes |

Home: [Kustomize, and Helm vs Kustomize](../helm/kustomize-vs-helm.md)

## Delivery and operations

### Blue/green vs canary vs rolling

| Strategy | How | Rollback | Cost |
|---|---|---|---|
| Rolling | Replace pods a few at a time | Roll forward or back gradually | No extra capacity |
| Blue/green | Full new copy, switch traffic at once | Switch back instantly | Double capacity during the switch |
| Canary | Small share of traffic to the new version, increase while metrics hold | Send traffic back to the old version | Needs traffic splitting and good metrics |

Home: [Deployment strategies](../cicd/deployment-strategies.md)

### git merge vs git rebase

| Aspect | Merge | Rebase |
|---|---|---|
| History | Keeps both lines plus a merge commit | Rewrites your commits on top of the target: linear |
| Safe on shared branches | Yes | No: rewritten commits break others' copies |
| Use | Integrating shared branches | Tidying your own branch before a pull request |

Home: [Daily workflow](../git/daily-workflow.md)

### git reset vs git revert

| Aspect | `git reset` | `git revert` |
|---|---|---|
| Does | Moves the branch pointer back (optionally discarding changes) | Adds a new commit that undoes an old one |
| History | Rewritten | Preserved |
| Use | Local, unpushed work | Anything already pushed |

Home: [Undoing and recovering](../git/undo-and-recover.md)

### git fetch vs git pull

| Aspect | `git fetch` | `git pull` |
|---|---|---|
| Does | Downloads remote commits into remote-tracking branches | Fetch, then merge (or rebase) into your branch |
| Changes your branch | No | Yes |

Home: [Remotes, pull requests and access](../git/remotes-and-collaboration.md)

### SIGTERM vs SIGKILL

| Aspect | SIGTERM (15) | SIGKILL (9) |
|---|---|---|
| Can be caught | Yes: the app can finish work and exit cleanly | No: the kernel ends the process |
| Sent by | `kill`, Kubernetes at pod shutdown | `kill -9`, after the grace period, the OOM killer |

Home: [Processes and signals](../linux/processes-and-signals.md)

### Hard link vs symbolic link

| Aspect | Hard link | Symbolic link |
|---|---|---|
| Points to | The same inode | A path |
| Across file systems | No | Yes |
| Target deleted | Data stays while any link remains | Link dangles |

Home: [Shell and filesystem](../linux/shell-and-filesystem.md)

### Metrics vs logs vs traces

| Signal | Answers | Strength | Cost driver |
|---|---|---|---|
| Metrics | Is something wrong, how much? | Cheap, fast to alert on | Label cardinality |
| Logs | What exactly happened? | Full detail per event | Volume |
| Traces | Where did the time go across services? | Request path and latency per hop | Sampling rate |

Home: [Signals and methods](../observability/signals-and-methods.md)

## How to practise

Cover the right-hand columns and say the differences aloud, then check. If you can also say *when you would pick each*, you are ready for the follow-up ([How to answer technical questions](how-to-answer.md)).

---
title: "Glossary"
status: draft
form: guide
commands: none
---

# Glossary

> **Status: AI draft, 2026-11-16.** Not yet verified by me. Short definitions only; each term links to the page that explains it. Pages still marked "not written yet" list what they will cover.

## In one line

One line per term, in plain words, with a link to the one page where the term is explained properly. Use it to decode a word in an interview question, then follow the link for the real answer.

## A to C

| Term | In plain words | Explained in |
|---|---|---|
| Admission control | Code the API server runs on every create or update, which may change or reject the request | [CRDs, operators and admission webhooks](../kubernetes/crds-and-operators.md) |
| ALB | AWS's layer-7 (HTTP) load balancer | [ALB and NLB](../aws-core/load-balancers.md) |
| AMI | A machine image that EC2 instances boot from | [Auto Scaling and AMIs](../aws-services/auto-scaling-and-amis.md) |
| Argo CD | A GitOps controller that keeps a cluster in sync with Git | [Argo CD architecture](../gitops/argocd-architecture.md) |
| ARP | How a host finds the hardware (MAC) address for an IP on the same network | [Layers and encapsulation](../networking/layers.md) |
| Assume role | Exchanging your identity for an IAM role's temporary credentials through STS | [IAM roles and STS](../aws-core/iam-roles-and-sts.md) |
| Availability zone | One or more data centres in a region, isolated from the others | [Accounts, regions and the CLI](../aws-core/accounts-regions-cli.md) |
| Blue-green | Run the new version beside the old, then switch all traffic at once | [Deployment strategies](../cicd/deployment-strategies.md) |
| Canary | Send a small share of traffic to the new version first | [Deployment strategies](../cicd/deployment-strategies.md) |
| Capabilities (Linux) | Root's powers split into separate privileges that can be dropped | [Pod security](../kubernetes/pod-security.md) |
| cgroup | Kernel feature that limits and counts a group of processes' CPU and memory | [What a container is](../containers/what-is-a-container.md) |
| CIDR | Notation for an address range, such as `10.0.0.0/16` | [IP addresses and subnetting](../networking/ip-and-subnetting.md) |
| ClusterIP | A Service's stable virtual address inside the cluster | [Services and DNS](../kubernetes/services-and-dns.md) |
| CNI | The plugin interface that gives pods their network | [Pod networking and NetworkPolicy](../kubernetes/pod-networking-and-network-policy.md) |
| Conntrack | The kernel's table of tracked connections, used by NAT and stateful firewalls | [Firewalls and connection tracking](../networking/firewalls.md) |
| Container runtime | The software that actually starts containers, such as containerd or runc | [Runtimes](../containers/runtimes.md) |
| CoreDNS | The cluster's DNS server | [Services and DNS](../kubernetes/services-and-dns.md) |
| CRD | A custom object type added to the Kubernetes API | [CRDs, operators and admission webhooks](../kubernetes/crds-and-operators.md) |
| CronJob | Runs a Job on a schedule | [Jobs and CronJobs](../kubernetes/jobs-and-cronjobs.md) |

## D to H

| Term | In plain words | Explained in |
|---|---|---|
| DaemonSet | Runs one pod on every (or every matching) node | [StatefulSets and DaemonSets](../kubernetes/statefulsets-and-daemonsets.md) |
| Deployment | Keeps a number of identical pods running and rolls out changes | [Deployments and rollouts](../kubernetes/deployments-and-rollouts.md) |
| Drift | Real infrastructure differs from what the code or Git says | [Import, moved and drift](../iac/import-and-drift.md) |
| EBS | Block storage volumes for EC2 | [EBS](../aws-services/ebs.md) |
| EFS | Shared network file system for many instances or pods | [EFS](../aws-services/efs.md) |
| EKS | AWS's managed Kubernetes control plane | [EKS architecture and node options](../eks/architecture.md) |
| Encapsulation | Each network layer wrapping the one above in its own header | [Layers and encapsulation](../networking/layers.md) |
| EndpointSlice | The list of ready pod addresses behind a Service | [Services and DNS](../kubernetes/services-and-dns.md) |
| etcd | The key-value store that holds all Kubernetes state | [etcd, backups and cluster upgrades](../kubernetes/etcd-backups-and-upgrades.md) |
| Eviction | The kubelet or API removing a pod to free resources or drain a node | [Disruptions and PDBs](../kubernetes/disruptions-and-pdbs.md) |
| Federation | Signing in to AWS with an outside identity provider | [Federation and SSO](../aws-core/federation-and-sso.md) |
| Finalizer | A marker that holds an object after delete until cleanup is done | [Finalizers and deletion](../kubernetes/finalizers-and-deletion.md) |
| Fluent Bit | A light agent that collects and forwards logs | [Fluent Bit](../observability/fluent-bit.md) |
| Gateway API | The successor to Ingress for routing traffic into a cluster | [Ingress and Gateway API](../kubernetes/ingress-and-gateway-api.md) |
| GitOps | Git holds the desired state and a controller applies it | [GitOps principles](../gitops/principles.md) |
| Graceful shutdown | Finishing in-flight work after SIGTERM before exiting | [Probes and graceful shutdown](../kubernetes/probes-and-graceful-shutdown.md) |
| Helm chart | A package of templated Kubernetes manifests with values | [Charts, templates and values](../helm/charts-and-templates.md) |
| HPA | Changes the number of pods from a metric | [Autoscaling](../kubernetes/autoscaling.md) |
| HTTP status codes | Three-digit result of an HTTP request: 2xx success, 4xx client, 5xx server | [HTTP](../networking/http.md) |

## I to N

| Term | In plain words | Explained in |
|---|---|---|
| IAM policy | A JSON document that allows or denies actions on resources | [IAM policies and how they are evaluated](../aws-core/iam-policies.md) |
| Idempotent | Running it twice has the same effect as running it once | [Terraform workflow](../iac/terraform-workflow.md) |
| Image | The read-only filesystem layers and settings a container starts from | [Images and Dockerfiles](../containers/images-and-dockerfiles.md) |
| Ingress | Kubernetes object with host and path rules for HTTP into the cluster | [Ingress and Gateway API](../kubernetes/ingress-and-gateway-api.md) |
| Inode | The file's metadata record on disk; a name points to it | [Disks and filesystems](../linux/disks-and-filesystems.md) |
| IRSA, Pod Identity | Ways for a pod's service account to get AWS credentials | [Cluster access, IRSA and Pod Identity](../eks/access-and-pod-identity.md) |
| Istio | A service mesh: sidecar or node proxies that handle traffic between services | [Why a mesh](../mesh/why-a-mesh.md) |
| Job | Runs pods until a task completes | [Jobs and CronJobs](../kubernetes/jobs-and-cronjobs.md) |
| JWT | A signed token carrying claims, used by OIDC and service accounts | [OAuth 2.0, OIDC and JWTs](../security/oauth-oidc-jwt.md) |
| Karpenter | Launches right-sized nodes for pending pods | [Karpenter in depth](../eks/karpenter.md) |
| kind | Kubernetes in Docker, a local test cluster | [Architecture and the reconcile loop](../kubernetes/architecture.md) |
| kubelet | The node agent that starts pods and reports their status | [Architecture and the reconcile loop](../kubernetes/architecture.md) |
| Label, selector | Key-value tags on objects, and the queries that pick objects by them | [Labels, selectors and namespaces](../kubernetes/labels-selectors-namespaces.md) |
| Least privilege | Grant only the permissions a task needs | [Least privilege and AccessDenied](../aws-core/least-privilege-and-accessdenied.md) |
| Liveness probe | A check whose failure restarts the container | [Probes and graceful shutdown](../kubernetes/probes-and-graceful-shutdown.md) |
| Load average | Runnable plus waiting-on-disk tasks, averaged over time | [Performance triage](../linux/performance-triage.md) |
| mTLS | TLS where both sides present certificates | [mTLS and authorization](../mesh/mesh-security.md) |
| Namespace (Kubernetes) | A named group of objects for access, quotas and names | [Labels, selectors and namespaces](../kubernetes/labels-selectors-namespaces.md) |
| Namespace (Linux) | A kernel feature that gives processes their own view of PIDs, network or mounts | [What a container is](../containers/what-is-a-container.md) |
| NACL | A stateless subnet-level firewall in a VPC | [Security groups and NACLs](../aws-core/security-groups-and-nacls.md) |
| NAT | Rewriting addresses so private hosts can share public ones | [Routing and NAT](../networking/routing-and-nat.md) |
| NetworkPolicy | Kubernetes firewall rules between pods | [Pod networking and NetworkPolicy](../kubernetes/pod-networking-and-network-policy.md) |
| NLB | AWS's layer-4 (TCP, UDP, TLS) load balancer | [ALB and NLB](../aws-core/load-balancers.md) |

## O to R

| Term | In plain words | Explained in |
|---|---|---|
| Observability | Being able to explain a system's behaviour from its metrics, logs and traces | [Signals and methods](../observability/signals-and-methods.md) |
| OIDC | An identity layer on OAuth 2.0; also how pipelines get cloud credentials without keys | [OIDC from pipelines to AWS](../cicd/oidc-to-aws.md) |
| OOM killer | The kernel killing a process to free memory | [Memory and the OOM killer](../linux/memory-and-oom.md) |
| Operator | A controller that manages an application through custom resources | [CRDs, operators and admission webhooks](../kubernetes/crds-and-operators.md) |
| PDB | PodDisruptionBudget: how many pods may be down during voluntary disruptions | [Disruptions and PDBs](../kubernetes/disruptions-and-pdbs.md) |
| Pod | One or more containers sharing a network address and volumes | [Pods](../kubernetes/pods.md) |
| Pod Security Admission | Built-in check that enforces privileged, baseline or restricted pods per namespace | [Pod security](../kubernetes/pod-security.md) |
| PrivateLink, VPC endpoint | Reaching AWS services or other VPCs privately, without the internet | [NAT, endpoints and PrivateLink](../aws-core/nat-endpoints-privatelink.md) |
| PromQL | Prometheus's query language | [PromQL](../observability/promql.md) |
| PVC, PV | A claim for storage, and the volume that satisfies it | [Storage](../kubernetes/storage.md) |
| QoS class | Guaranteed, Burstable or BestEffort, from requests and limits | [Requests, limits and QoS](../kubernetes/resources-and-qos.md) |
| Quorum | The majority of members that must agree before a write counts | [etcd, backups and cluster upgrades](../kubernetes/etcd-backups-and-upgrades.md) |
| RBAC | Roles listing allowed verbs, bound to users or service accounts | [RBAC and service accounts](../kubernetes/rbac-and-service-accounts.md) |
| Readiness probe | A check whose failure removes the pod from Service endpoints | [Probes and graceful shutdown](../kubernetes/probes-and-graceful-shutdown.md) |
| Rebase | Replaying commits on top of another branch | [Daily workflow](../git/daily-workflow.md) |
| Reconcile loop | A controller repeatedly making reality match the desired state | [Architecture and the reconcile loop](../kubernetes/architecture.md) |
| Reflog | Git's local record of where branches pointed, used to recover lost commits | [Undoing and recovering](../git/undo-and-recover.md) |
| Requests, limits | What a container is guaranteed, and the most it may use | [Requests, limits and QoS](../kubernetes/resources-and-qos.md) |
| Resolver | The DNS server that looks names up on a client's behalf | [DNS](../networking/dns.md) |
| Reverse proxy | A server that receives client requests and forwards them to backends | [Load balancers and proxies](../networking/load-balancers-and-proxies.md) |
| Route table | Rules that decide where packets for each destination go | [Routing and NAT](../networking/routing-and-nat.md) |

## S to Z

| Term | In plain words | Explained in |
|---|---|---|
| SBOM | A list of the components inside a build or image | [Registries and image security](../containers/registries-and-image-security.md) |
| SCP | An Organizations policy that caps what accounts can do | [Organizations, SCPs and multi-account](../aws-core/organizations-and-scps.md) |
| Security group | A stateful firewall attached to network interfaces in a VPC | [Security groups and NACLs](../aws-core/security-groups-and-nacls.md) |
| Service (Kubernetes) | A stable name and address in front of a changing set of pods | [Services and DNS](../kubernetes/services-and-dns.md) |
| Service account | An in-cluster identity that pods run as | [RBAC and service accounts](../kubernetes/rbac-and-service-accounts.md) |
| Sidecar | A helper container running beside the main one in a pod | [Sidecars and traffic flow](../mesh/sidecars-and-traffic-flow.md) |
| SIGTERM, SIGKILL | The polite stop signal, and the one that cannot be caught | [Processes and signals](../linux/processes-and-signals.md) |
| SLI, SLO, error budget | What you measure, the target for it, and how much failure the target allows | [SLOs](../observability/slos.md) |
| SNI | The hostname a TLS client sends so the server picks the right certificate | [TLS and certificates](../networking/tls.md) |
| StatefulSet | Pods with stable names and their own volumes | [StatefulSets and DaemonSets](../kubernetes/statefulsets-and-daemonsets.md) |
| STS | AWS service that issues temporary credentials | [IAM roles and STS](../aws-core/iam-roles-and-sts.md) |
| Subnet | A slice of a network's address range; in AWS, tied to one zone | [VPC basics](../aws-core/vpc-basics.md) |
| systemd unit | A service, timer or other object that systemd manages | [systemd and services](../linux/systemd.md) |
| Taint, toleration | A node repelling pods, and a pod accepting that | [Scheduling](../kubernetes/scheduling.md) |
| TCP handshake | SYN, SYN-ACK, ACK: how a TCP connection opens | [TCP and UDP](../networking/tcp-and-udp.md) |
| Terraform state | Terraform's record of which real resources it manages | [State](../iac/state.md) |
| TLS | Encryption and server identity for connections | [TLS and certificates](../networking/tls.md) |
| Trace, span | One request's path across services, and one step of it | [Tracing](../observability/tracing.md) |
| Transit Gateway | A hub that connects many VPCs and networks | [Peering, Transit Gateway and VPN](../aws-core/vpc-connectivity.md) |
| TTL | How long a DNS answer may be cached | [DNS](../networking/dns.md) |
| VPA | Changes pods' CPU and memory requests from observed usage | [Autoscaling](../kubernetes/autoscaling.md) |
| VPC | A private network in AWS | [VPC basics](../aws-core/vpc-basics.md) |
| WAF | Rules that filter HTTP requests before they reach an application | [CloudFront and WAF](../aws-core/cloudfront-and-waf.md) |
| Webhook (admission) | An HTTPS service the API server calls to check or change objects | [CRDs, operators and admission webhooks](../kubernetes/crds-and-operators.md) |
| Zombie process | A finished process whose parent has not collected its exit status | [Processes and signals](../linux/processes-and-signals.md) |

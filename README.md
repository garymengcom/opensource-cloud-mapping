# opensource-cloud-mapping
A comprehensive mapping of open-source software to cloud-managed services across AWS, Azure, and GCP.


## Container Orchestration

| Service                    | Open Source                                                   | AWS                                                          | Azure                                                         | GCP                                                        |
|----------------------------|-------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------|
| **Container Orchestration** | [Kubernetes](https://kubernetes.io/), [k3s](https://k3s.io/) | [Amazon EKS](https://aws.amazon.com/eks/)                   | [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/products/kubernetes-service/) | [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/) |
| **Container Runtime**       | [containerd](https://containerd.io/), [CRI-O](https://cri-o.io/) | [AWS Bottlerocket](https://aws.amazon.com/bottlerocket/)     | [Azure Container Instances](https://azure.microsoft.com/en-us/products/container-instances/) | [GKE Autopilot](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) |
| **Container Registry**      | [Harbor](https://goharbor.io/), [Docker Registry](https://docs.docker.com/registry/) | [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) | [Azure Container Registry (ACR)](https://azure.microsoft.com/en-us/products/container-registry/) | [Google Artifact Registry](https://cloud.google.com/artifact-registry/) |
| **Serverless Containers**   | [Knative](https://knative.dev/), [OpenFaaS](https://www.openfaas.com/) | [AWS Fargate](https://aws.amazon.com/fargate/)               | [Azure Container Apps](https://azure.microsoft.com/en-us/products/container-apps/) | [Cloud Run](https://cloud.google.com/run/) |
| **Service Discovery**       | [Consul](https://www.consul.io/), [CoreDNS](https://coredns.io/) | [AWS Cloud Map](https://aws.amazon.com/cloud-map/)           | [Azure DNS Private Resolver](https://learn.microsoft.com/en-us/azure/dns/private-resolver-overview) | [Cloud DNS](https://cloud.google.com/dns/) |
| **Container Networking (CNI)** | [Cilium](https://cilium.io/), [Calico](https://www.tigera.io/project-calico/) | [AWS VPC CNI](https://docs.aws.amazon.com/eks/latest/userguide/pod-networking.html) | [Azure CNI](https://learn.microsoft.com/en-us/azure/aks/concepts-network) | [GKE Native CNI](https://cloud.google.com/kubernetes-engine/docs/concepts/cni-advanced-networking) |
| **Container Security**      | [Trivy](https://aquasecurity.github.io/trivy/), [Anchore](https://anchore.com/) | [Amazon Inspector](https://aws.amazon.com/inspector/)       | [Microsoft Defender for Containers](https://azure.microsoft.com/en-us/products/defender-for-cloud/) | [GCP Security Command Center](https://cloud.google.com/security-command-center/) |
| **Container Observability** | [Prometheus](https://prometheus.io/), [Grafana](https://grafana.com/) | [Amazon Managed Prometheus](https://aws.amazon.com/prometheus/) | [Azure Monitor for Containers](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/) | [Google Cloud Operations Suite](https://cloud.google.com/products/operations) |



## Data Storage

| Service             | Open Source                                                              | AWS                                              | Azure                                                        | GCP                                          |
|--------------------|------------------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------------------|----------------------------------------------|
| **Object Storage** | [Minio](https://min.io/)                                             | [Amazon S3](https://aws.amazon.com/s3/)         | [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs/) | [Google Cloud Storage](https://cloud.google.com/storage/) |
| **File Storage**   | [Ceph](https://ceph.io/), [GlusterFS](https://www.gluster.org/)      | [Amazon EFS](https://aws.amazon.com/efs/)       | [Azure Files](https://azure.microsoft.com/en-us/products/storage/files/) | [Filestore](https://cloud.google.com/filestore/) |
| **Distributed Storage** | [SeaweedFS](https://github.com/seaweedfs/seaweedfs), [HDFS](https://hadoop.apache.org/) | [Amazon FSx](https://aws.amazon.com/fsx/)       | [Azure NetApp Files](https://azure.microsoft.com/en-us/products/netapp/) | [Google Filestore](https://cloud.google.com/filestore) |
| **Block Storage**  | [Ceph RBD](https://docs.ceph.com/en/latest/rbd/)                     | [Amazon EBS](https://aws.amazon.com/ebs/)       | [Azure Managed Disks](https://azure.microsoft.com/en-us/products/storage/disks/) | [Persistent Disk](https://cloud.google.com/persistent-disk/) |
| **SQL Database**   | [PostgreSQL](https://www.postgresql.org/), [MySQL](https://www.mysql.com/) | [Amazon RDS](https://aws.amazon.com/rds/)       | [Azure Database for PostgreSQL](https://azure.microsoft.com/en-us/products/postgresql/), [Azure Database for MySQL](https://azure.microsoft.com/en-us/products/mysql/) | [Cloud SQL](https://cloud.google.com/sql/) |
| **Enterprise SQL** | [MariaDB](https://mariadb.org/), [CockroachDB](https://www.cockroachlabs.com/) | [Amazon RDS for MariaDB](https://aws.amazon.com/rds/mariadb/) | [Azure Database for MariaDB](https://azure.microsoft.com/en-us/products/mariadb/) | [Cloud SQL for MariaDB](https://cloud.google.com/sql/docs/mariadb/) |
| **Scalable SQL**   | [Vitess](https://vitess.io/), [TiDB](https://pingcap.com/)           | [Amazon Aurora](https://aws.amazon.com/rds/aurora/) | [Azure SQL Hyperscale](https://azure.microsoft.com/en-us/products/sql-database/) | [Spanner](https://cloud.google.com/spanner/) |
| **Key-Value Store** | [Redis](https://redis.io/), [Dragonfly](https://www.dragonflydb.io/) | [ElastiCache for Redis](https://aws.amazon.com/elasticache/redis/) | [Azure Cache for Redis](https://azure.microsoft.com/en-us/products/cache/) | [Cloud Memorystore](https://cloud.google.com/memorystore/docs/redis/) |
| **Document Store** | [MongoDB](https://www.mongodb.com/), [CouchDB](https://couchdb.apache.org/) | [Amazon DocumentDB](https://aws.amazon.com/documentdb/) | [Azure Cosmos DB](https://azure.microsoft.com/en-us/products/cosmos-db/) | [Firestore](https://cloud.google.com/firestore/) |
| **Columnar Store** | [Apache Cassandra](https://cassandra.apache.org/), [ScyllaDB](https://www.scylladb.com/) | [Amazon Keyspaces](https://aws.amazon.com/keyspaces/) | [Azure Cosmos DB (Cassandra API)](https://azure.microsoft.com/en-us/products/cosmos-db/) | [Bigtable](https://cloud.google.com/bigtable/) |
| **Graph Database** | [Neo4j](https://neo4j.com/), [JanusGraph](https://janusgraph.org/)   | [Amazon Neptune](https://aws.amazon.com/neptune/) | [Azure Cosmos DB (Gremlin API)](https://azure.microsoft.com/en-us/products/cosmos-db/) | [Graph DB](https://cloud.google.com/graph-db/) |
| **Data Warehouse** | [ClickHouse](https://clickhouse.com/), [Apache Druid](https://druid.apache.org/) | [Amazon Redshift](https://aws.amazon.com/redshift/) | [Azure Synapse Analytics](https://azure.microsoft.com/en-us/products/synapse-analytics/) | [BigQuery](https://cloud.google.com/bigquery/) |
| **Presto-based Query Engine** | [Presto](https://prestodb.io/), [Trino](https://trino.io/) | [Amazon Athena](https://aws.amazon.com/athena/) | [Azure Data Explorer](https://azure.microsoft.com/en-us/products/data-explorer/) | [BigQuery](https://cloud.google.com/bigquery/) |


## Networking

| Service               | Open Source                                                             | AWS                                                  | Azure                                                       | GCP                                                 |
|----------------------|-----------------------------------------------------------------------|------------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------|
| **Load Balancing**   | [HAProxy](http://www.haproxy.org/), [NGINX](https://nginx.org/)      | [Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/) | [Azure Load Balancer](https://azure.microsoft.com/en-us/products/load-balancer/) | [Cloud Load Balancing](https://cloud.google.com/load-balancing/) |
| **Reverse Proxy**    | [Traefik](https://traefik.io/), [Caddy](https://caddyserver.com/)   | [AWS ALB](https://aws.amazon.com/elasticloadbalancing/) | [Azure Application Gateway](https://azure.microsoft.com/en-us/products/application-gateway/) | [Cloud Load Balancer](https://cloud.google.com/load-balancing/) |
| **API Gateway**      | [Kong](https://konghq.com/), [Tyk](https://tyk.io/)                 | [Amazon API Gateway](https://aws.amazon.com/api-gateway/) | [Azure API Management](https://azure.microsoft.com/en-us/products/api-management/) | [Cloud Endpoints](https://cloud.google.com/endpoints/) |
| **Service Mesh**     | [Istio](https://istio.io/), [Linkerd](https://linkerd.io/)          | [AWS App Mesh](https://aws.amazon.com/app-mesh/) | [Azure Service Mesh](https://azure.microsoft.com/en-us/blog/announcing-the-public-preview-of-azure-service-mesh/) | [Anthos Service Mesh](https://cloud.google.com/anthos/service-mesh) |
| **DNS Management**   | [CoreDNS](https://coredns.io/), [Bind9](https://www.isc.org/bind/)  | [Amazon Route 53](https://aws.amazon.com/route53/)  | [Azure DNS](https://azure.microsoft.com/en-us/products/dns/) | [Cloud DNS](https://cloud.google.com/dns/) |
| **Networking Overlay** | [Calico](https://www.tigera.io/project-calico/), [Cilium](https://cilium.io/) | [AWS VPC Networking](https://aws.amazon.com/vpc/) | [Azure Virtual Network](https://azure.microsoft.com/en-us/products/virtual-network/) | [VPC Networking](https://cloud.google.com/vpc/) |
| **Web Application Firewall (WAF)** | [ModSecurity](https://owasp.org/www-project-modsecurity-core-rule-set/) | [AWS WAF](https://aws.amazon.com/waf/) | [Azure Web Application Firewall](https://azure.microsoft.com/en-us/services/web-application-firewall/) | [Cloud Armor](https://cloud.google.com/armor/) |
| **DDoS Protection**  | [FastNetMon](https://fastnetmon.com/), [CrowdSec](https://www.crowdsec.net/) | [AWS Shield](https://aws.amazon.com/shield/) | [Azure DDoS Protection](https://azure.microsoft.com/en-us/products/ddos-protection/) | [Cloud Armor](https://cloud.google.com/armor/) |
| **VPN & Secure Networking** | [WireGuard](https://www.wireguard.com/), [OpenVPN](https://openvpn.net/) | [AWS Client VPN](https://aws.amazon.com/vpn/) | [Azure VPN Gateway](https://azure.microsoft.com/en-us/products/vpn-gateway/) | [Cloud VPN](https://cloud.google.com/network-connectivity/docs/vpn/) |
| **Private Connectivity** | [Tinc](https://www.tinc-vpn.org/), [ZeroTier](https://www.zerotier.com/) | [AWS Direct Connect](https://aws.amazon.com/directconnect/) | [Azure ExpressRoute](https://azure.microsoft.com/en-us/products/expressroute/) | [Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/) |


## CI/CD (Continuous Integration / Continuous Deployment)

| Service                 | Open Source                                                           | AWS                                                        | Azure                                                   | GCP                                                          |
|-------------------------|---------------------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------------|
| **CI/CD Pipelines**     | [Jenkins](https://www.jenkins.io/), [Tekton](https://tekton.dev/) | [AWS CodePipeline](https://aws.amazon.com/codepipeline/)   | [Azure DevOps Pipelines](https://azure.microsoft.com/en-us/products/devops/pipelines/) | [Cloud Build](https://cloud.google.com/cloud-build) |
| **CI/CD Automation**    | [GitLab CI/CD](https://docs.gitlab.com/ee/ci/), [ArgoCD](https://argo-cd.readthedocs.io/en/stable/) | [AWS CodeBuild](https://aws.amazon.com/codebuild/) | [Azure DevOps Pipelines](https://azure.microsoft.com/en-us/products/devops/pipelines/) | [Cloud Build](https://cloud.google.com/cloud-build) |
| **Git Repositories**    | [Gitea](https://gitea.io/), [GitLab](https://about.gitlab.com/)   | [AWS CodeCommit](https://aws.amazon.com/codecommit/)      | [Azure Repos](https://azure.microsoft.com/en-us/products/devops/repos/) | [Cloud Source Repositories](https://cloud.google.com/source-repositories) |
| **Artifact Management** | [JFrog Artifactory](https://jfrog.com/artifactory/), [Nexus](https://www.sonatype.com/products/nexus-repository) | [AWS CodeArtifact](https://aws.amazon.com/codeartifact/) | [Azure Artifacts](https://azure.microsoft.com/en-us/products/devops/artifacts/) | [Artifact Registry](https://cloud.google.com/artifact-registry) |
| **Configuration Management** | [Ansible](https://www.ansible.com/), [Puppet](https://puppet.com/) | [AWS Systems Manager](https://aws.amazon.com/systems-manager/) | [Azure Automation](https://azure.microsoft.com/en-us/products/automation/) | [Cloud Deployment Manager](https://cloud.google.com/deployment-manager) |
| **Infrastructure as Code** | [Terraform](https://www.terraform.io/), [Pulumi](https://www.pulumi.com/) | [AWS CloudFormation](https://aws.amazon.com/cloudformation/) | [Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/) | [Google Cloud Deployment Manager](https://cloud.google.com/deployment-manager) |
| **Secrets Management**  | [Vault](https://www.vaultproject.io/), [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets) | [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) | [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/) | [Secret Manager](https://cloud.google.com/secret-manager) |
| **Policy as Code**      | [Open Policy Agent (OPA)](https://www.openpolicyagent.org/)      | [AWS IAM Policies](https://aws.amazon.com/iam/)           | [Azure Policy](https://azure.microsoft.com/en-us/products/governance/) | [Google Cloud IAM Policies](https://cloud.google.com/iam/docs/policies) |
| **Progressive Delivery** | [Flagger](https://flagger.app/), [Argo Rollouts](https://argoproj.github.io/argo-rollouts/) | [AWS AppConfig](https://aws.amazon.com/appconfig/) | [Azure Feature Flags](https://learn.microsoft.com/en-us/azure/azure-app-configuration/feature-management-overview) | [Google Cloud Feature Flags](https://cloud.google.com/feature-flagging/) |


## DevOps Tooling

| Service                | Open Source                                                    | AWS                                                            | Azure                                                         | GCP                                                         |
|------------------------|--------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| **Infrastructure as Code (IaC)** | [Terraform](https://www.terraform.io/), [Pulumi](https://www.pulumi.com/) | [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  | [Azure Resource Manager (ARM)](https://learn.microsoft.com/en-us/azure/azure-resource-manager/) | [Google Deployment Manager](https://cloud.google.com/deployment-manager) |
| **Configuration Management** | [Ansible](https://www.ansible.com/), [Puppet](https://puppet.com/) | [AWS Systems Manager](https://aws.amazon.com/systems-manager/) | [Azure Automation](https://azure.microsoft.com/en-us/products/automation/) | [Google Cloud Deployment Manager](https://cloud.google.com/deployment-manager) |
| **Logging & Monitoring** | [Prometheus](https://prometheus.io/), [Grafana](https://grafana.com/) | [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)       | [Azure Monitor](https://azure.microsoft.com/en-us/products/monitor/) | [Google Cloud Operations Suite](https://cloud.google.com/products/operations) |
| **Service Mesh**       | [Istio](https://istio.io/), [Linkerd](https://linkerd.io/) | [AWS App Mesh](https://aws.amazon.com/app-mesh/)               | [Azure Service Mesh](https://azure.microsoft.com/en-us/products/service-fabric/) | [Anthos Service Mesh](https://cloud.google.com/service-mesh) |
| **API Gateway**        | [Kong](https://konghq.com/), [Traefik](https://traefik.io/) | [Amazon API Gateway](https://aws.amazon.com/api-gateway/)     | [Azure API Management](https://azure.microsoft.com/en-us/products/api-management/) | [Google Cloud API Gateway](https://cloud.google.com/api-gateway) |
| **Error Tracking**     | [Sentry](https://sentry.io/), [OpenTelemetry](https://opentelemetry.io/) | [AWS X-Ray](https://aws.amazon.com/xray/)                     | [Azure Monitor Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview) | [Google Cloud Trace](https://cloud.google.com/trace) |



## Monitoring

| Service            | Open Source                                                        | AWS                                               | Azure                                                   | GCP                                         |
|--------------------|------------------------------------------------------------------|---------------------------------------------------|---------------------------------------------------------|---------------------------------------------|
| **Metrics Monitoring** | [Prometheus](https://prometheus.io/), [VictoriaMetrics](https://victoriametrics.com/) | [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) | [Azure Monitor](https://azure.microsoft.com/en-us/products/monitor/) | [Cloud Monitoring](https://cloud.google.com/monitoring/) |
| **Log Management** | [ELK Stack (Elasticsearch, Logstash, Kibana)](https://www.elastic.co/), [Fluentd](https://www.fluentd.org/), [Loki](https://grafana.com/oss/loki/) | [Amazon OpenSearch](https://aws.amazon.com/opensearch-service/) | [Azure Monitor Logs](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/logs-data-platform) | [Cloud Logging](https://cloud.google.com/logging/) |
| **Distributed Tracing** | [Jaeger](https://www.jaegertracing.io/), [Zipkin](https://zipkin.io/) | [AWS X-Ray](https://aws.amazon.com/xray/) | [Azure Application Insights](https://azure.microsoft.com/en-us/products/monitor/) | [Cloud Trace](https://cloud.google.com/trace/) |
| **APM (Application Performance Monitoring)** | [OpenTelemetry](https://opentelemetry.io/), [Pyroscope](https://pyroscope.io/) | [AWS X-Ray](https://aws.amazon.com/xray/) | [Azure Monitor Application Insights](https://azure.microsoft.com/en-us/products/monitor/) | [Cloud Trace + Profiler](https://cloud.google.com/profiler) |
| **Infrastructure Monitoring** | [Zabbix](https://www.zabbix.com/), [Nagios](https://www.nagios.org/) | [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) | [Azure Monitor](https://azure.microsoft.com/en-us/products/monitor/) | [Cloud Monitoring](https://cloud.google.com/monitoring/) |
| **Event Monitoring & Alerting** | [Grafana](https://grafana.com/), [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) | [Amazon Managed Grafana](https://aws.amazon.com/grafana/) | [Azure Monitor Alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview) | [Cloud Monitoring Alerting](https://cloud.google.com/monitoring/alerts/) |

## Security

| Service                | Open Source                                                      | AWS                                                               | Azure                                                                  | GCP                                                                    |
|------------------------|----------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| **Identity & Access Management (IAM)** | [Keycloak](https://www.keycloak.org/), [Auth0 OSS](https://github.com/auth0) | [AWS IAM](https://aws.amazon.com/iam/)                           | [Azure Active Directory (AAD)](https://azure.microsoft.com/en-us/products/active-directory/) | [Google Cloud IAM](https://cloud.google.com/iam/) |
| **Secrets Management** | [Vault](https://www.vaultproject.io/), [Bitwarden](https://bitwarden.com/) | [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)   | [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/) | [Google Secret Manager](https://cloud.google.com/secret-manager) |
| **Certificate Management** | [Certbot](https://certbot.eff.org/), [CFSSL](https://github.com/cloudflare/cfssl) | [AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/) | [Azure App Service Certificates](https://azure.microsoft.com/en-us/products/app-service/certificates/) | [Google Certificate Manager](https://cloud.google.com/certificate-manager/) |
| **Web Application Firewall (WAF)** | [ModSecurity](https://modsecurity.org/), [Naxsi](https://github.com/nbs-system/naxsi) | [AWS WAF](https://aws.amazon.com/waf/)                           | [Azure WAF](https://azure.microsoft.com/en-us/products/web-application-firewall/) | [Google Cloud Armor](https://cloud.google.com/armor) |
| **DDoS Protection**    | [FastNetMon](https://fastnetmon.com/), [Mitigation Services](https://github.com/topics/ddos-mitigation) | [AWS Shield](https://aws.amazon.com/shield/)                     | [Azure DDoS Protection](https://azure.microsoft.com/en-us/products/ddos-protection/) | [Google Cloud Armor](https://cloud.google.com/armor) |
| **SIEM (Security Information & Event Management)** | [Wazuh](https://wazuh.com/), [OSSEC](https://www.ossec.net/) | [AWS Security Hub](https://aws.amazon.com/security-hub/) | [Microsoft Sentinel](https://azure.microsoft.com/en-us/products/microsoft-sentinel/) | [Google Chronicle](https://cloud.google.com/chronicle) |
| **Endpoint Security** | [Falco](https://falco.org/), [OSQuery](https://osquery.io/) | [AWS GuardDuty](https://aws.amazon.com/guardduty/) | [Microsoft Defender for Endpoint](https://www.microsoft.com/en-us/security/business/threat-protection/microsoft-defender-endpoint) | [Security Command Center](https://cloud.google.com/security-command-center/) |

## Big Data & Analytics

| Service                     | Open Source                                                  | AWS                                                            | Azure                                                         | GCP                                                           |
|-----------------------------|------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| **Big Data Processing**     | [Apache Spark](https://spark.apache.org/), [Flink](https://flink.apache.org/) | [AWS EMR](https://aws.amazon.com/emr/)                        | [Azure Synapse Analytics](https://azure.microsoft.com/en-us/products/synapse-analytics/) | [Google Dataproc](https://cloud.google.com/dataproc) |
| **Data Warehouse**          | [ClickHouse](https://clickhouse.com/), [Apache Druid](https://druid.apache.org/) | [Amazon Redshift](https://aws.amazon.com/redshift/)          | [Azure Synapse Analytics](https://azure.microsoft.com/en-us/products/synapse-analytics/) | [BigQuery](https://cloud.google.com/bigquery) |
| **Message Queues & Streaming** | [Kafka](https://kafka.apache.org/), [Pulsar](https://pulsar.apache.org/) | [Amazon MSK](https://aws.amazon.com/msk/)                     | [Azure Event Hubs](https://azure.microsoft.com/en-us/products/event-hubs/) | [Google Pub/Sub](https://cloud.google.com/pubsub) |
| **Search & Indexing**       | [Elasticsearch](https://www.elastic.co/), [Solr](https://solr.apache.org/) | [Amazon OpenSearch](https://aws.amazon.com/opensearch-service/) | [Azure Cognitive Search](https://azure.microsoft.com/en-us/products/search/) | [Google Cloud Search](https://cloud.google.com/search/) |
| **ETL & Data Integration**  | [Apache NiFi](https://nifi.apache.org/), [Airbyte](https://airbyte.com/) | [AWS Glue](https://aws.amazon.com/glue/)                      | [Azure Data Factory](https://azure.microsoft.com/en-us/products/data-factory/) | [Google Dataflow](https://cloud.google.com/dataflow) |
| **Graph Databases**         | [Neo4j](https://neo4j.com/), [ArangoDB](https://www.arangodb.com/) | [Amazon Neptune](https://aws.amazon.com/neptune/)            | [Azure Cosmos DB (Graph)](https://azure.microsoft.com/en-us/products/cosmos-db/) | [Google Cloud Graph Engine](https://cloud.google.com/databases/) |
| **Time-Series Databases**   | [InfluxDB](https://www.influxdata.com/), [TimescaleDB](https://www.timescale.com/) | [Amazon Timestream](https://aws.amazon.com/timestream/)       | [Azure Time Series Insights](https://azure.microsoft.com/en-us/products/time-series-insights/) | [Google Cloud Bigtable](https://cloud.google.com/bigtable) |



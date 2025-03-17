# opensource-cloud-mapping
A comprehensive mapping of open-source software to cloud-managed services across AWS, Azure, and GCP.

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





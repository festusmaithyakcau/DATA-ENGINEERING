# DATA ENGINEERING
# LEARNING DATA ENGINEERING AND ML FROM SCRATCH 

In most organizations, a data engineer is the primary role responsible for integrating, transforming, and consolidating data from various structured and unstructured data systems into structures that are suitable for building analytics solutions. A data engineer also helps ensure that data pipelines and data stores are high-performing, efficient, organized, and reliable, given a specific set of business requirements and constraints.

# Types of data
There are three primary types of data that a data engineer will work with:

1. **Structured**
Structured data primarily comes from table-based source systems such as a relational database or from a flat file such as a comma-separated (CSV) file. The primary element of a structured file is that the rows and columns are aligned consistently throughout the file.

2. **Semi-Structured**

Semi-structured data is data such as JavaScript object notation (JSON) files, which may require flattening prior to loading into your source system. When flattened, this data doesn't have to fit neatly into a table structure.

3. **Unstructured**

Unstructured data includes data stored as key-value pairs that don't adhere to standard relational models and Other types of unstructured data that are commonly used include portable data format (PDF), word processor documents, and images.


# Important data engineering concepts

**Operational and analytical data**

<img src= "https://learn.microsoft.com/en-us/training/wwl-data-ai/introduction-to-data-engineering-azure/media/4-operational-analytical-data.png">

<i>Operational data <i>is usually transactional data that is generated and stored by applications, often in a relational or non-relational database. <i>Analytical data<i> is data that has been optimized for analysis and reporting, often in a data warehouse.

One of the core responsibilities of a data engineer is to design, implement, and manage solutions that integrate operational and analytical data sources or extract operational data from multiple systems, transform it into appropriate structures for analytics, and load it into an analytical data store (usually referred to as ETL solutions).

**Streaming data**

<img src="https://learn.microsoft.com/en-us/training/wwl-data-ai/introduction-to-data-engineering-azure/media/4-stream-data.png">

Streaming data refers to perpetual sources of data that generate data values in real time, often relating to specific events. Common sources of streaming data include Internet-of-things (IoT) devices and social media feeds.

Data engineers often need to implement solutions that capture real-time streams of data and ingest them into analytical data systems, often combining the real-time data with other application data that is processed in batches.

**Data pipelines**

<img src= "https://learn.microsoft.com/en-us/training/wwl-data-ai/introduction-to-data-engineering-azure/media/4-data-pipeline.png">

Data pipelines are used to orchestrate activities that transfer and transform data. Pipelines are the primary way in which data engineers implement repeatable extract, transform, and load (ETL) solutions that can be triggered based on a schedule or in response to events.

**Data lakes**

<img src= "https://learn.microsoft.com/en-us/training/wwl-data-ai/introduction-to-data-engineering-azure/media/4-data-lake.png">

A data lake is a storage repository that holds large amounts of data in native, raw formats. Data lake stores are optimized for scaling to massive volumes (terabytes or petabytes) of data. The data typically comes from multiple heterogeneous sources and may be structured, semi-structured, or unstructured.

The idea with a data lake is to store everything in its original, untransformed state. This approach differs from a traditional data warehouse, which transforms and processes the data at the time of ingestion.

**Data warehouses**

<img src= "https://learn.microsoft.com/en-us/training/wwl-data-ai/introduction-to-data-engineering-azure/media/4-data-warehouse.png">

A data warehouse is a centralized repository of integrated data from one or more disparate sources. Data warehouses store current and historical data in relational tables that are organized into a schema that optimizes performance for analytical queries.

Data engineers are responsible for designing and implementing relational data warehouses, and managing regular data loads into tables.

**Apache Spark**

<img src = "https://learn.microsoft.com/en-us/training/wwl-data-ai/introduction-to-data-engineering-azure/media/4-apache-spark.png">

Apache Spark is a parallel processing framework that takes advantage of in-memory processing and a distributed file storage. It's a common open-source software (OSS) tool for big data scenarios.

Data engineers need to be proficient with Spark, using notebooks and other code artifacts to process data in a data lake and prepare it for modeling and analysis.




## DATA LAKE STORAGE - Case Study (Azure Data Lake Storage Gen2) 

<img src = "https://learn.microsoft.com/en-us/training/data-ai-cert/introduction-to-azure-data-lake-storage/media/azure-data-lake-gen-2.png">



Benefits
Data Lake Storage is designed to deal with this variety and volume of data at an exabyte scale while securely handling hundreds of gigabytes of throughput. With this, you can use Data Lake Storage Gen2 as the basis for both real-time and batch solutions.

Hadoop compatible access
A benefit of Data Lake Storage is that you can treat the data as if it's stored in a Hadoop Distributed File System (HDFS). With this feature, you can store the data in one place and access it through compute technologies including Azure Databricks, Azure HDInsight, and Azure Synapse Analytics without moving the data between environments. The data engineer also has the ability to use storage mechanisms such as the parquet format, which is highly compressed and performs well across multiple platforms using an internal columnar storage.

Security
Data Lake Storage supports access control lists (ACLs) and Portable Operating System Interface (POSIX) permissions that don't inherit the permissions of the parent directory. In fact, you can set permissions at a directory level or file level for the data stored within the data lake, providing a much more secure storage system. This security is configurable through technologies such as Hive and Spark or utilities such as Azure Storage Explorer, which runs on Windows, macOS, and Linux. All data that is stored is encrypted at rest by using either Microsoft or customer-managed keys.

Performance
Azure Data Lake Storage organizes the stored data into a hierarchy of directories and subdirectories, much like a file system, for easier navigation. As a result, data processing requires less computational resources, reducing both the time and cost.

Data redundancy
Data Lake Storage takes advantage of the Azure Blob replication models that provide data redundancy in a single data center with locally redundant storage (LRS), or to a secondary region by using the Geo-redundant storage (GRS) option. This feature ensures that your data is always available and protected if catastrophe strikes.




## Author :black_nib:

* Festus Maithya [festusmaithyakcau](https://github.com/festusmaithyakcau)

## Acknowledgements :pray:

All work contained in this project was completed as part of the curriculum for the Bachelors Degree in Software Development at KCA UNIVERSITY.For more information, visit
[this link](https://www.kcau.ac.ke/).

<p align="center">
  <img src="https://imgs.search.brave.com/MTbtOFwZkcm_5kD492on7rnZtOFLek3Z3kLxhZT_UDw/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/ZWR1b3BpbmlvbnMu/Y29tL3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDIyLzA0L0tDQS11/bml2ZXJzaXR5LWxv/Z28ucG5n" alt="KCA UNIVERSITY">
</p>





import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import ReadFromBigQuery
from apache_beam.io.gcp.gcsfilesystem import GCSFileSystem

# Define pipeline options here
options = PipelineOptions(
    runner='DataflowRunner',  # Specify the runner (e.g., DataflowRunner, DirectRunner)
    project='your-gcp-project-id',  # Replace with your GCP project ID
    region='your-gcp-region',  # Replace with your desired GCP region
    temp_location='gs://your-bucket/temp',  # Replace with your Cloud Storage bucket for temporary files
    job_name='ecg-preprocessing-pipeline'  # Give your pipeline a descriptive name
)

# Function to preprocess a single example
def preprocess_ecg(element):
    # This function defines your preprocessing logic
    # e.g.,
    # element['ecg_data'] = normalize_ecg(element['ecg_data'])
    # element['features'] = extract_features(element['ecg_data'])
    return element

# Create the pipeline
with beam.Pipeline(options=options) as pipeline:
    # Read data from BigQuery
    data = (
        pipeline
        | 'ReadFromBigQuery' >> ReadFromBigQuery(table='health_monitoring_system.ecg_data')
    )

    # Preprocess and feature engineering
    processed_data = (
        data 
        | 'PreprocessECG' >> beam.Map(preprocess_ecg)
    )

    # Write preprocessed data to Cloud Storage in TFRecord format
    processed_data | 'WriteToTFRecord' >> beam.io.tfrecordio.WriteToTFRecord(
        file_path_prefix='gs://health_monitoring_system/preprocessed_data/ecg',
        # Additional TFRecord options (e.g., compression) can also be used if need be
    )

    # (Optional) Delete processed data from BigQuery
    # Lets say we wanna delete Specific Rows from BigQuer (within the Dataflow pipeline)

# Assuming that you have a way to identify processed data (e.g., using a flag or timestamp) in the pipeline, you can delete the processed data from BigQuery:
#processed_data_ids = processed_data | 'GetProcessedIDs' >> beam.Map(lambda x: x['id'])  # Extract IDs

# Construct a BigQuery delete query like this one which I commented out after testing

'''

delete_query = f"""
    DELETE FROM `health_monitoring_system.ecg_data`
    WHERE id IN UNNEST(@processed_ids)
"""

# Execute the delete query using a BigQuery client
client = bigquery.Client()
job_config = bigquery.QueryJobConfig(
    query_parameters=[
        bigquery.ArrayQueryParameter("processed_ids", "INT64", processed_data_ids)
    ]
)
client.query(delete_query, job_config=job_config)

'''
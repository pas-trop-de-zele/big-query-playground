from google.cloud import bigquery
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './service_account.json'

client = bigquery.Client()
bucket_name = 'bigquer_export_41421'
project = "big-query-playground-411020"
dataset_id = "NYHousing"

destination_uri = "gs://{}/{}".format(bucket_name, "nyhousing1-*.csv.gz")
dataset_ref = bigquery.DatasetReference(project, dataset_id)
table_ref = dataset_ref.table("NYHousingTable")
job_config = bigquery.job.ExtractJobConfig()
job_config.compression = bigquery.Compression.GZIP

extract_job = client.extract_table(
    table_ref,
    destination_uri,
    # Location must match that of the source table.
    location="US",
    job_config=job_config,
)  # API request
extract_job.result()  # Waits for job to complete.

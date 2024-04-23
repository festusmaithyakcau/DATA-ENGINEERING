from django.shortcuts import render
from .models import Patient
from google.cloud import bigquery  # Import BigQuery client library from google-cloud-bigquery package

# Importing model.py functions and classes

def patient_dashboard(request, patient_id):
    # Fetch patient data
    patient = Patient.objects.get(pk=patient_id)

    # Connect to BigQuery
    client = bigquery.Client()

    # Construct and run a BigQuery query to get latest prediction and recommendation for the patient
    query_job = client.query("""
        SELECT prediction, recommendation
        FROM `health_monitoring_system.predictions`  # Replace with your actual table and dataset names in BigQuery
        WHERE patient_id = @patient_id
        ORDER BY timestamp DESC
        LIMIT 1
    """, job_config=bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("patient_id", "INT64", patient_id)
        ]
    ))
    results = query_job.result()

    # Extract prediction and recommendation from the query results
    if results.total_rows > 0:
        prediction, recommendation = results[0]
    else:
        prediction, recommendation = None, None

    # Render the dashboard template with data
    return render(request, 'dashboard.html', {
        'heart_rate': patient.heart_rate,  # Actually this a sample statistic for the patient
        # Other patient statistics can be added here
        'prediction': prediction,
        'recommendation': recommendation
    })
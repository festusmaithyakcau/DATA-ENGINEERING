"""
Now that we've connected to data, we need to save it into the lakehouse. You can either save as a file or load as a Delta table.

Write to a file
Lakehouses support structured, semi-structured, and unstructured files. Load as a parquet file or Delta table to take advantage of the Spark engine.
"""
# Write DataFrame to Parquet file format
parquet_output_path = "your_folder/your_file_name"
df.write.mode("overwrite").parquet(parquet_output_path)
print(f"DataFrame has been written to Parquet file: {parquet_output_path}")

# Write DataFrame to Delta table
delta_table_name = "your_delta_table_name"
df.write.format("delta").mode("overwrite").saveAsTable(delta_table_name)
print(f"DataFrame has been written to Delta table: {delta_table_name}")

import com.google.cloud.bigquery.BigQuery;
import com.google.cloud.bigquery.BigQueryOptions;
import com.google.cloud.bigquery.InsertAllRequest;
import com.google.cloud.bigquery.TableId;
import org.apache.kafka.clients.consumer.*;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.time.Duration;
import java.util.*;

public class ECGConsumer {
    public static void main(String[] args) {
        // Kafka consumer configuration
        Properties props = new Properties();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ConsumerConfig.GROUP_ID_CONFIG, "ecg-consumer-group");
        // We can add other consumer properties here if need be

        // Our GCP BigQuery client Initialization
        BigQuery bigquery = BigQueryOptions.getDefaultInstance().getService();
        TableId tableId = TableId.of("health_monitoring_system", "ecg_data");

        try (KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props)) {
            consumer.subscribe(Collections.singletonList("ecg-topic"));

            while (true) {
                ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
                List<Map<String, Object>> rows = new ArrayList<>();

                for (ConsumerRecord<String, String> record : records) {
                    // Parse and process ECG data from record.value() here

                    // Create BigQuery row
                    Map<String, Object> row = new HashMap<>();
                    row.put("timestamp", System.currentTimeMillis());
                    row.put("ecg_data", processedData);
                    // We can also add other relevant fields here
                    rows.add(row);
                }

                // Inserting rows into BigQuery
                InsertAllRequest.Builder requestBuilder = InsertAllRequest.newBuilder(tableId);
                rows.forEach(requestBuilder::addRow);
                bigquery.insertAll(requestBuilder.build());

                consumer.commitSync();
            }
        }
    }
}
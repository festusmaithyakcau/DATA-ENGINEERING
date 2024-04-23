import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Enumeration;

import gnu.io.CommPortIdentifier;
import gnu.io.SerialPort;

import java.util.Properties;

public class ECGProducer {

    public static void main(String[] args) {
        // Kafka producer configuration
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");  // Replace with your Kafka broker address
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        // Add other producer properties as needed

        // Create the Kafka producer
        KafkaProducer<String, String> producer = new KafkaProducer<>(props);
        // Read ECG data from serial port
        String ecgData = "";
try {
    // Find the serial port (adjust port name as needed)
    Enumeration portEnum = CommPortIdentifier.getPortIdentifiers();
    String portName = "COM3"; // Replace with your actual port name (e.g., /dev/ttyUSB0 during testing) 
    while (portEnum.hasMoreElements()) {
        CommPortIdentifier currPortId = (CommPortIdentifier) portEnum.nextElement();
        if (currPortId.getName().equals(portName)) {
            // Opening the serial port
            SerialPort serialPort = (SerialPort) currPortId.open(this.getClass().getName(), 2000);
            serialPort.setSerialPortParams(9600, SerialPort.DATABITS_8, SerialPort.STOPBITS_1, SerialPort.PARITY_NONE);

            // Reading data from the serial port
            BufferedReader reader = new BufferedReader(new InputStreamReader(serialPort.getInputStream()));
            ecgData = reader.readLine(); 

            // Close the reader and serial port
            reader.close();
            serialPort.close();
            break;
        }
    }

} catch (Exception e) {
    e.printStackTrace();
        }
        finally {
            producer.close();
        }
    }
}


 

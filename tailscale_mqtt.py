import paho.mqtt.client as mqtt
import subprocess
import logging

# MQTT Configuration
MQTT_BROKER = "homeserver"
MQTT_PORT = 1883
MQTT_TOPIC = "system/tailscale"


# Logging
# logging.basicConfig(level=logging.INFO)
print("Program Starting...Ready to Listen to MQTT")

# Commands allowed
ALLOWED_COMMANDS = {
    "tailscale up": ["tailscale", "up"],
    "tailscale down": ["tailscale", "down"]
}


def execute_command(command):
    if command not in ALLOWED_COMMANDS:
        # logging.warning(f"Rejected command: {command}")
        print(f"Rejected command: {command}")
        return

    try:
        # logging.info(f"Executing: {command}")

        result = subprocess.run(
            ALLOWED_COMMANDS[command],
            capture_output=True,
            text=True
        )

        # logging.info(f"Return code: {result.returncode}")
        # logging.info(f"STDOUT: {result.stdout}")
        # logging.error(f"STDERR: {result.stderr}")
        print(f"Executing: {command}")
    except Exception as e:
        logging.error(f"Execution failed: {e}")


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        # logging.info("Connected to MQTT broker")
        print("Connected to MQTT broker")
        client.subscribe(MQTT_TOPIC)
        # logging.info(f"Subscribed to {MQTT_TOPIC}")
        print(f"Subscribed to {MQTT_TOPIC}")
    else:
        # logging.error(f"Connection failed with code {rc}")
        print(f"Connection failed with code {rc}")


def on_message(client, userdata, msg):
    payload = msg.payload.decode().strip().lower()

    # logging.info(f"Received MQTT message on {msg.topic}: {payload}")
    print(f"Received MQTT message on {msg.topic}: {payload}")

    execute_command(payload)


client = mqtt.Client()

# Uncomment if using MQTT auth
# client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)

client.loop_forever()
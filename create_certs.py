import os
import ssl
import subprocess

# Generate the CA certificate and private key
ca_cert_file = "ca.crt"
ca_key_file = "ca.key"
os.system(f"openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout {ca_key_file} -out {ca_cert_file} -days 365 -subj '/CN=MyCA'")

# Generate the server certificate and private key for App1
app1_cert_file = "app1.crt"
app1_key_file = "app1.key"
os.system(f"openssl req -newkey rsa:2048 -nodes -keyout {app1_key_file} -out app1.csr -subj '/CN=app1'")
os.system(f"openssl x509 -req -in app1.csr -CA {ca_cert_file} -CAkey {ca_key_file} -CAcreateserial -out {app1_cert_file} -days 365 -sha256")

# Generate the server certificate and private key for App2
app2_cert_file = "app2.crt"
app2_key_file = "app2.key"
os.system(f"openssl req -newkey rsa:2048 -nodes -keyout {app2_key_file} -out app2.csr -subj '/CN=app2'")
os.system(f"openssl x509 -req -in app2.csr -CA {ca_cert_file} -CAkey {ca_key_file} -CAcreateserial -out {app2_cert_file} -days 365 -sha256")

# Clean up the intermediate files
os.remove("app1.csr")
os.remove("app2.csr")

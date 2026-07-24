from ec2_metadata import ec2_metadata
import boto3

data = 'Instance ID: ' + ec2_metadata.instance_id + '\n' + 'Public IPv4: ' + ec2_metadata.public_ipv4 + '\n' + 'Private IPv4: ' + ec2_metadata.private_ipv4 + '\n' + 'Security Groups: ' + ' '.join(ec2_metadata.security_groups) + '\n'


with open("/etc/os-release", "r") as file:
    for line in file:
        if line.startswith("NAME="):
            data += '\n' + "OS Name: " + line.split("NAME=")[1].strip('"\n')
        if line.startswith("VERSION="):
            data += '\n' + "OS Version: " + line.split("VERSION=")[1].strip('"\n')

data += "\nUsers:\n"

with open("/etc/passwd", "r") as file:
    for line in file:
        if "nologin" in line or "false" in line:
            pass
        else:
            data += "\nUsername: " + line.split(":")[0]

print(data)
# SAVE TO FILE
with open("meta.txt", "w") as file:
    file.write(data)


# UPLOADD

s3 = boto3.client('s3')
s3.upload_file("meta.txt", "applicant-task", "instance-136")

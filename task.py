from ec2_metadata import ec2_metadata

data = 'Instance ID: ' + ec2_metadata.instance_id + '\n' + 'Public IPv4: ' + ec2_metadata.public_ipv4 + '\n' + 'Private IPv4: ' + ec2_metadata.private_ipv4 + '\n' + 'Security Groups: ' + ' '.join(ec2_metadata.security_groups) + '\n'


with open("/etc/os-release", "r") as file:
    for line in file:
        if line.startswith("NAME="):
            data += '\n' + "Name: " + line.split("NAME=")[1].strip('"\n')
        if line.startswith("VERSION="):
            data += '\n' + "Version: " + line.split("VERSION=")[1].strip('"\n')


print(data)

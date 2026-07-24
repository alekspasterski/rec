from ec2_metadata import ec2_metadata

data = 'Instance ID: ' + ec2_metadata.instance_id + '\n' + 'Public IPv4: ' + ec2_metadata.public_ipv4 + '\n' + 'Private IPv4: ' + ec2_metadata.private_ipv4 + '\n' + 'Security Groups: ' + ' '.join(ec2_metadata.security_groups) + '\n'

print(data)

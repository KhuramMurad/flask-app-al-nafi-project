# Output the VPC ID
output "vpc_id" {
  description = "The ID of the created VPC"
  value       = aws_vpc.project_vpc.id
}

# Output the IDs of public subnets
output "public_subnet_ids" {
  description = "The IDs of the public subnets"
  value       = [aws_subnet.public_subnet_1.id, aws_subnet.public_subnet_2.id]
}

# Output the IDs of private subnets
output "private_subnet_ids" {
  description = "The IDs of the private subnets"
  value       = [aws_subnet.private_subnet_1.id, aws_subnet.private_subnet_2.id]
}

# Output the IDs of NAT Gateways
output "nat_gateway_ids" {
  description = "The IDs of the NAT Gateways"
  value       = [aws_nat_gateway.nat_gateway_1.id, aws_nat_gateway.nat_gateway_2.id]
}

# Output the Elastic IPs of NAT Gateways
output "nat_gateway_eip" {
  description = "The Elastic IPs of the NAT Gateways"
  value       = [aws_eip.nat_1.public_ip, aws_eip.nat_2.public_ip]
}

# Output the IDs of public route tables
output "public_route_table_id" {
  description = "The ID of the public route table"
  value       = aws_route_table.public_rt.id
}

# Output the IDs of private route tables
output "private_route_table_ids" {
  description = "The IDs of the private route tables"
  value       = [aws_route_table.private_rt_1.id, aws_route_table.private_rt_2.id]
}


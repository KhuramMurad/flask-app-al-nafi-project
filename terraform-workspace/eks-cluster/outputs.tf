output "cluster_id" {
  description = "EKS cluster ID"
  value       = module.eks.cluster_id
}

output "cluster_endpoint" {
  description = "EKS cluster endpoint"
  value       = module.eks.cluster_endpoint
}

output "node_group_role_arn" {
  description = "IAM role ARN for worker nodes"
  value       = module.node_group.node_role_arn
}


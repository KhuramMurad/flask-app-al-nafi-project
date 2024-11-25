variable "cluster_name" {
  description = "Name of the EKS Cluster"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID for the cluster"
  type        = string
}

variable "private_subnets" {
  description = "Private subnets for the cluster"
  type        = list(string)
}

variable "node_instance_type" {
  description = "Instance type for worker nodes"
  type        = string
  default     = "t2.micro"
}

variable "desired_capacity" {
  description = "Desired number of worker nodes"
  type        = number
  default     = 1
}

variable "min_size" {
  description = "Minimum number of worker nodes"
  type        = number
  default     = 1
}

variable "max_size" {
  description = "Maximum number of worker nodes"
  type        = number
  default     = 2
}

variable "environment" {
  description = "Environment (e.g., dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "project" {
  description = "Project Name"
  type        = string
  default     = "multi-cloud-infra"
}


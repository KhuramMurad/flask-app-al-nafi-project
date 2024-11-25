variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "Name of the EKS Cluster"
  type        = string
  default     = "flask-web-app-cluster"
}

variable "vpc_id" {
  description = "VPC ID for the cluster"
  type        = string
  default     = "vpc-01d778b0a1f1ace6d"  # Your VPC ID
}

variable "private_subnets" {
  description = "Private subnets for the cluster"
  type        = list(string)
  default     = [
    "subnet-013d0c984efb24c9f",  # Private Subnet 1
    "subnet-09b2b939b71e09360"   # Private Subnet 2
  ]
}

variable "public_subnets" {
  description = "Public subnets for the cluster (optional for node groups)"
  type        = list(string)
  default     = [
    "subnet-065b486a4756659bd",  # Public Subnet 1
    "subnet-099e35e39aedc816d"   # Public Subnet 2
  ]
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

variable "kubernetes_version" {
  description = "Kubernetes version for the EKS cluster"
  type        = string
  default     = "1.27"
}


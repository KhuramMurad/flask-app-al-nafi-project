module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "20.29.0"
  cluster_name    = var.cluster_name
  cluster_version = "1.27"

  vpc_id     = var.vpc_id
  subnet_ids = var.private_subnets

  # Enable creation of the cluster IAM role
  create_eks = true

  # Tags for the cluster
  tags = {
    Environment = var.environment
    Project     = var.project
  }
}

module "node_group" {
  source          = "terraform-aws-modules/eks/aws//modules/eks-managed-node-group"
  version         = "20.29.0"

  cluster_name = module.eks.cluster_id
  subnet_ids   = var.private_subnets

  node_group_defaults = {
    ami_type             = "AL2_x86_64"
    disk_size            = 20
    instance_types       = [var.node_instance_type]
    capacity_type        = "ON_DEMAND"
    desired_capacity     = var.desired_capacity
    min_size             = var.min_size
    max_size             = var.max_size
    enable_monitoring    = true
    enable_auto_scaling  = true
    auto_scaling_metrics = true
  }

  tags = {
    Environment = var.environment
    Project     = var.project
  }
}


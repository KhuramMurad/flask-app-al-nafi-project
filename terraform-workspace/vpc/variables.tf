# Variables for the VPC
variable "vpc_cidr" {
  description = "The CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

# Variables for Public Subnets
variable "public_subnet_1_cidr" {
  description = "CIDR block for the first public subnet"
  type        = string
  default     = "10.0.1.0/24"
}

variable "public_subnet_2_cidr" {
  description = "CIDR block for the second public subnet"
  type        = string
  default     = "10.0.2.0/24"
}

# Variables for Private Subnets
variable "private_subnet_1_cidr" {
  description = "CIDR block for the first private subnet"
  type        = string
  default     = "10.0.3.0/24"
}

variable "private_subnet_2_cidr" {
  description = "CIDR block for the second private subnet"
  type        = string
  default     = "10.0.4.0/24"
}

# Variables for Availability Zones
variable "availability_zone_1" {
  description = "The first availability zone"
  type        = string
  default     = "us-east-1a"
}

variable "availability_zone_2" {
  description = "The second availability zone"
  type        = string
  default     = "us-east-1b"
}


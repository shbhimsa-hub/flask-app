variable "aws_region" {
  default = "eu-central-1"
}

variable "cluster_name" {
  default = "flask-cluster"
}

variable "docker_image" {
  description = "Docker Hub image to deploy"
  default     = "shbhimsa/flask-template:latest"
}

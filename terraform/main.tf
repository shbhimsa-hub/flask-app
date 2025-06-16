provider "aws" {
  region = var.aws_region
}

resource "aws_ecs_cluster" "main" {
  name = var.cluster_name
}

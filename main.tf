terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.0.0"
    }
  }
}

provider "google" {
  credentials = var.keyfile_location
}

module "kubernetes" {
  source = "./modules/kubernetes-k8s-agents-machine-data-extraction"

  master_sa_email             = var.master_sa_email
  master_sa_scopes            = var.master_sa_scopes
  master_preemptible          = var.master_preemptible
  master_additional_disk_type = var.master_additional_disk_type
  worker_sa_email             = var.worker_sa_email
  worker_sa_scopes            = var.worker_sa_scopes
  worker_preemptible          = var.worker_preemptible

  ssh_whitelist        = var.ssh_whitelist
  api_server_whitelist = var.api_server_whitelist
  nodeport_whitelist   = var.nodeport_whitelist
}
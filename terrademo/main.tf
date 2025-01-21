terraform {
  required_providers {
    google = {
        source = "hashicorp/google"
        version = "5.6.0"
    }
  }
}

provider "google" {
    project = "carbide-crowbar-448318-b0"
    region = "EU"
  }

resource "google_storage_bucket" "demo-bucket" {
  name          = "carbide-crowbar-448318-b0-terra-bucket"  
  location      = "EU"                       
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

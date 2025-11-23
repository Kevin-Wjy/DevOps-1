provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "dev" {
  metadata {
    name = "dev"
  }
}

resource "kubernetes_deployment" "myapp" {
  metadata {
    name      = "myapp"
    namespace = kubernetes_namespace.dev.metadata[0].name
  }
  spec {
    replicas = 2
    selector {
      match_labels = {
        app = "myapp"
      }
    }
    template {
      metadata {
        labels = {
          app = "myapp"
        }
      }
      spec {
        container {
          name  = "myapp"
          image = "ghcr.io/${var.owner}/myapp:latest"
          port {
            container_port = 8000
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "myapp" {
  metadata {
    name      = "myapp-service"
    namespace = kubernetes_namespace.dev.metadata[0].name
  }
  spec {
    selector = {
      app = "myapp"
    }
    port {
      port        = 80
      target_port = 8000
    }
    type = "ClusterIP"
  }
}

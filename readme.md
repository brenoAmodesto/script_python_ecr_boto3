## Verificação de Uso de Tags do ECR em Clusters EKS

## --

## Descrição 
Este repositório contém um script em Python que coleta tags de imagens armazenadas no Elastic Container Registry (ECR) da AWS e verifica se essas tags estão sendo utilizadas em clusters Elastic Kubernetes Service (EKS). Esse script é útil para identificar imagens que não estão em uso e potencialmente otimizar o uso do armazenamento no ECR.

# Pré-requisitos
    Python 3.7+ instalado.
    Credenciais AWS configuradas com permissões para acessar o ECR e os clusters EKS.
    Bibliotecas necessárias (definidas no arquivo requirements.txt).  
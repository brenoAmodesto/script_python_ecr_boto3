import boto3

def verificar_tags_ecr(region_name='region', tags_file='file'):
    # Carrega a lista de tags do arquivo
    with open(tags_file, 'r') as f:
        tags_para_verificar = set(line.strip() for line in f)
    
    # Inicializa o cliente ECR
    ecr_client = boto3.client('ecr', region_name=region_name)

    # Conjuntos para armazenar tags encontradas e não encontradas
    tags_existentes = set()
    tags_nao_existentes = tags_para_verificar.copy()

    # Lista todos os repositórios no ECR
    repositories = ecr_client.describe_repositories()['repositories']
    
    for repo in repositories:
        repo_name = repo['repositoryName']
        
        # Lista todas as imagens do repositório
        images = ecr_client.list_images(repositoryName=repo_name)['imageIds']
        
        # Para cada imagem, verifica a tag
        for image in images:
            image_tag = image.get('imageTag')
            if image_tag:
                full_tag = f"{repo_name}:{image_tag}"
                
                # Verifica se a tag está na lista para verificar
                if full_tag in tags_para_verificar:
                    tags_existentes.add(full_tag)
                    tags_nao_existentes.discard(full_tag)
    
    # Salva os resultados em arquivos
    with open('tags_existentes.txt', 'w') as existentes_file:
        for tag in sorted(tags_existentes):
            existentes_file.write(f"{tag}\n")
    
    with open('tags_nao_existentes.txt', 'w') as nao_existentes_file:
        for tag in sorted(tags_nao_existentes):
            nao_existentes_file.write(f"{tag}\n")
    
    print("Processo completo! Verifique 'tags_existentes.txt' e 'tags_nao_existentes.txt'.")

# Executa a função
if __name__ == "__main__":
    verificar_tags_ecr()

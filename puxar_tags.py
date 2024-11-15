import boto3

def salvar_tags_ecr_em_arquivo(region_name='region', output_file='base.txt'):
    # Inicializa o cliente ECR
    ecr_client = boto3.client('ecr', region_name=region_name)

    # Abre o arquivo para salvar as tags
    with open(output_file, 'w') as file:
        # Lista todos os repositórios no ECR
        repositories = ecr_client.describe_repositories()['repositories']
        
        for repo in repositories:
            repo_name = repo['repositoryName']
            print(f"Verificando repositório: {repo_name}")

            # Paginação para lidar com múltiplas imagens no repositório
            paginator = ecr_client.get_paginator('list_images')
            for page in paginator.paginate(repositoryName=repo_name):
                images = page['imageIds']
                
                # Itera sobre cada imagem e salva a tag
                for image in images:
                    image_tag = image.get('imageTag')
                    if image_tag:  # Ignora imagens sem tag
                        full_tag = f"{repo_name}:{image_tag}"
                        file.write(full_tag + '\n')
    
    print(f"Processo completo! Todas as tags foram salvas em '{output_file}'.")

# Executa a função
if __name__ == "__main__":
    salvar_tags_ecr_em_arquivo()

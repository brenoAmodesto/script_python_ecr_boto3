def comparar_tags(base_tags_file='file', tags_ecr_file='base.txt'):
    # Carrega as tags da base para um conjunto
    with open(base_tags_file, 'r') as base_file:
        tags_base = set(line.strip() for line in base_file)
    
    # Inicializa os conjuntos para as tags usadas e não usadas
    tags_usadas = set()
    tags_nao_usadas = set()

    # Verifica cada tag no arquivo ECR
    with open(tags_ecr_file, 'r') as ecr_file:
        for line in ecr_file:
            tag = line.strip()
            if tag in tags_base:
                tags_usadas.add(tag)
            else:
                tags_nao_usadas.add(tag)
    
    # Salva as tags usadas e não usadas em arquivos separados
    with open('tags_usadas.txt', 'w') as usadas_file:
        for tag in sorted(tags_usadas):
            usadas_file.write(f"{tag}\n")
    
    with open('tags_nao_usadas.txt', 'w') as nao_usadas_file:
        for tag in sorted(tags_nao_usadas):
            nao_usadas_file.write(f"{tag}\n")
    
    print("Processo completo! Verifique 'tags_usadas.txt' e 'tags_nao_usadas.txt'.")

# Executa a função
if __name__ == "__main__":
    comparar_tags()

def process_tags_file(input_file='file', output_file='file'):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Remove a URL base, mantendo apenas o formato <repositório>:<tag>
            cleaned_line = line.strip().split('/')[-1]  # Pega a última parte após a última barra
            outfile.write(cleaned_line + '\n')

    print(f"Arquivo processado. As tags limpas foram salvas em '{output_file}'.")

# Executa a função
if __name__ == "__main__":
    process_tags_file()

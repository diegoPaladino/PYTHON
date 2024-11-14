import os

# Caminho para a unidade (pode ser alterado para outra unidade se necessário)
drive_path = "C:\\"
# Tamanho mínimo do arquivo em MB para ser listado (atualmente configurado para 500 MB)
min_size_mb = 500
min_size_bytes = min_size_mb * 1024 * 1024

# Nome do arquivo para salvar a lista de arquivos grandes (ajustado para a área de trabalho)
output_file = os.path.expanduser("~/Desktop/arquivos_grandes.txt")

# Função para converter o tamanho em bytes para MB
def format_size(size):
    return f"{size / (1024 * 1024):.2f} MB"

with open(output_file, "w") as f:
    for root, dirs, files in os.walk(drive_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                if file_size >= min_size_bytes:
                    f.write(f"{file_path} - {format_size(file_size)}\n")
                    print(f"{file_path} - {format_size(file_size)}")
            except (PermissionError, FileNotFoundError):
                # Ignora arquivos que não podem ser acessados
                pass

print(f"\nA lista de arquivos grandes foi salva em {output_file}")

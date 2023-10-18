import threading
import numpy as np
import cv2

# Função para calcular Gx
def calculate_Gx(I, Gx, M, N):
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            value = (I[i + 1, j - 1] + I[i + 1, j] + I[i + 1, j + 1]) - (I[i - 1, j - 1] + I[i - 1, j] + I[i - 1, j + 1])
            Gx[i, j] = np.clip(value, 0, 255)  # Saturação

# Função para calcular Gy
def calculate_Gy(I, Gy, M, N):
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            value = (I[i - 1, j + 1] + I[i, j + 1] + I[i + 1, j + 1]) - (I[i - 1, j - 1] + I[i, j - 1] + I[i + 1, j - 1])
            Gy[i, j] = np.clip(value, 0, 255) 

# Função principal
def main():
    # Carregar a imagem em nível de cinza
    image = cv2.imread("coins.png", cv2.IMREAD_GRAYSCALE)
    M, N = image.shape

    # Criar arrays para Gx e Gy
    Gx = np.zeros((M, N), dtype=np.uint8)
    Gy = np.zeros((M, N), dtype=np.uint8)

    # Criar threads para calcular Gx e Gy
    thread_Gx = threading.Thread(target=calculate_Gx, args=(image, Gx, M, N))
    thread_Gy = threading.Thread(target=calculate_Gy, args=(image, Gy, M, N))

    # Iniciar as threads
    thread_Gx.start()
    thread_Gy.start()

    # Aguardar as threads terminarem
    thread_Gx.join()
    thread_Gy.join()

    # Calcular a imagem de saída G
    G = Gx + Gy
    G = np.clip(G, 0, 255).astype(np.uint8)  # Saturação

    # Salvar a imagem de saída
    cv2.imwrite("imagem_saida.png", G)

if __name__ == "__main__":
    main()
    
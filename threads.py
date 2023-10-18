import threading
import numpy as np
import cv2


def calcular_Gx(I, Gx, M, N):
    for i in range(1, M - 2):
        for j in range(1, N - 2):
            value = (I[i + 1, j - 1] + I[i + 1, j] + I[i + 1, j + 1]) - (I[i - 1, j - 1] + I[i - 1, j] + I[i - 1, j + 1])
            Gx[i, j] = np.clip(value, 0, 255)  # Saturação para deixar os valores no intervalo de 0 a 255


def calcular_Gy(I, Gy, M, N):
    for i in range(1, M - 2):
        for j in range(1, N - 2):
            value = (I[i - 1, j + 1] + I[i, j + 1] + I[i + 1, j + 1]) - (I[i - 1, j - 1] + I[i, j - 1] + I[i + 1, j - 1])
            Gy[i, j] = np.clip(value, 0, 255) # Saturação para deixar os valores no intervalo de 0 a 255


def main():
    # Carregar a imagem em nível de cinza
    image = cv2.imread("coins.png", cv2.IMREAD_GRAYSCALE)
    M, N = image.shape

    # Criar arrays de 0 para Gx e Gy 
    Gx = np.zeros((M, N), dtype=np.uint8)
    Gy = np.zeros((M, N), dtype=np.uint8)

    # Criar 2 threads filhas para calcular Gx e Gy
    thread_Gx = threading.Thread(target=calcular_Gx, args=(image, Gx, M, N))
    thread_Gy = threading.Thread(target=calcular_Gy, args=(image, Gy, M, N))

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
    cv2.imwrite("imagem_saida3.png", G)

if __name__ == "__main__":
    main()
    

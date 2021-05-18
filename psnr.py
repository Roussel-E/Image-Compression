from math import log10, sqrt
import cv2
import numpy as np

def PSNR(originale, compressee):
    mse = np.mean((originale - compressee) ** 2)
    if mse == 0 :
        return None
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

def valeur():
     originale = cv2.imread("originale.png")
     compressee = cv2.imread("compressee.png", 1)
     valeur = PSNR(originale, compressee)
     if valeur == None :
         print("Les images sont identiques")
     else :
         print("La valeur de PSNR est {valeur} dB")
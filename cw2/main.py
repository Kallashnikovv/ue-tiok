import cv2

pathColor = "cw2/cat1.jpg"
pathBW = "cw2/cat2.jpg"

# Zad 1
def zad1():
    image = cv2.imread(pathColor)


    if image is None:
        print("Błąd: Nie można wczytać obrazu. Sprawdź ścieżkę.")
    else:
        cv2.imshow('Obraz', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
# Zad 2
def zad2():
    image = cv2.imread(pathColor, cv2.IMREAD_COLOR)

    if image is not None:
        print(f"Liczba kanałów: {image.shape[2]}")
    else:
        print("Błąd: Nie można wczytać obrazu.")
        
# Zad 3
def zad3():
    image = cv2.imread(pathBW, cv2.IMREAD_GRAYSCALE)

    if image is not None:
        print(f"Liczba kanałów: {len(image.shape)}")
    else:
        print("Błąd: Nie można wczytać obrazu.")
        
# Zad 4
def zad4():
    image = cv2.imread(pathBW, cv2.IMREAD_GRAYSCALE)

    newPath = "cw2/newCat.jpg"
    
    if image is not None:
        cv2.imwrite(newPath, image)
        print("Obraz został zapisany.")
    else:
        print("Błąd: Nie można wczytać obrazu.")
        
# Zad 5
def zad5():
    image1 = cv2.imread(pathColor)
    image2 = cv2.imread(pathBW)

    if image1 is not None and image2 is not None:
        cv2.imshow('Obraz 1', image1)
        
        cv2.imshow('Obraz 2', image2)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Błąd: Nie można wczytać jednego z obrazów.")
        
# Zad 6
def zad6():
    image = cv2.imread(pathColor)

    if image is not None:
        cv2.namedWindow('Dostosowane okno', cv2.WINDOW_NORMAL)
        
        cv2.imshow('Dostosowane okno', image)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Błąd: Nie można wczytać obrazu.")
        
def main():
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    #zad5()
    zad6()
    
if __name__ == "__main__":
    main()
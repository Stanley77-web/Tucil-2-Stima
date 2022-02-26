from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits, load_iris, load_wine, load_breast_cancer
from ConvexHull import myConvexHull

if __name__ == "__main__":
    while True:
        print("Pilihan Database : ")
        print("1. Dataset Iris")
        print("2. Dataset Wine")
        print("3. Dataset Breast Cancer")
        print("4. Dataset Digits")
        print("5. Keluar")
        print("===================================")
        # Memilih database yang ingin dibuat convexhullnya
        choices = int(input("Masukan dataset (1/2/3/4) : "))

        if (choices < 1 or choices > 4):
            break

        # Melakukan load database yang dipilih
        match choices:

            case 1:
                print("Pilihan Kolom : ")
                print("1. Sepal-length vs Sepal-width")
                print("2. Petal-length vs Petal-width")
                data = load_iris()
                coulom = int(input("Masukan kolom dataset (1/2) : "))
                if (coulom == 1):
                    n, m = 0, 1
                elif (coulom == 2):
                    n, m = 2,3
                    
            case 2:
                data = load_wine()
                n = int(input("Masukan kolom1 dataset (0-12) : "))
                while True:
                    m = int(input("Masukan kolom2 dataset (0-12) excepet " + str(n) + ") : "))
                    if (n != m):
                        break
                        
            case 3:
                data = load_breast_cancer()
                n, m = 0, 1
                n = int(input("Masukan kolom1 dataset (0-29) : "))
                while True:
                    m = int(input("Masukan kolom2 dataset (0-29) excepet " + str(n) + ") : "))
                    if (n != m):
                        break

            case 4:
                data = load_digits()
                n, m = 9, 10
                n = int(input("Masukan kolom1 dataset (0-64) : "))
                while True:
                    m = int(input("Masukan kolom2 dataset (0-64) excepet " + str(n) + " : "))
                    if (n != m):
                        break

        # Membuat Data Frame
        dataframe = DataFrame(data.data, columns=data.feature_names)
        dataframe['Target'] = DataFrame(data.target)
        dataframe.head()
        
        # Visualisasi convexhull
        plt.figure(figsize = (10, 6))
        colors = ['b','r','g','y','c']
        plt.title(data.feature_names[n] + ' vs ' + data.feature_names[m])
        plt.xlabel(data.feature_names[n])
        plt.ylabel(data.feature_names[m])
        for i in range(len(data.target_names)):
            bucket = dataframe[dataframe['Target'] == i]
            bucket = bucket.iloc[:,[n,m]].values
            hull = myConvexHull(bucket)
            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
            for simplex in hull:
                plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i%5])
        plt.legend()
        plt.show()
        print("===================================")
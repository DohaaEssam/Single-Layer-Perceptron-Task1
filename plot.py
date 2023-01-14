import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#preprocessing of penguins
Penguins  = pd.read_csv("penguins.csv")
#fill-in null values in gender with female
#transform string values of gender into numeric
Penguins["gender"].fillna(value="female", inplace=True)
Penguins["gender"] = Penguins["gender"].replace(['female','male'], [1, 0])
#x = Penguins["gender"]
#Penguins["gender"] = Penguins["gender"].replace(x, 1)
#print(Penguins["gender"])


P_Adelie = Penguins[0:50]
P_Gentoo = Penguins[50:100]
P_Chinstrap = Penguins[100:150]
#x = P_Adelie["species"][1]
#P_Adelie = P_Adelie.replace({'species': x},{'species': "1"})
#print(P_Adelie)

#1 bill_length and bill_depth_mm
plt.scatter(P_Adelie["bill_length_mm"],P_Adelie["bill_depth_mm"],label="adelie")
plt.scatter(P_Gentoo["bill_length_mm"],P_Gentoo["bill_depth_mm"],label="gentoo")
plt.scatter(P_Chinstrap["bill_length_mm"],P_Chinstrap["bill_depth_mm"],label="chinstrap")
plt.title("bill length vs bill depth")
plt.xlabel("bill length")
plt.ylabel("bill depth")
plt.legend()
plt.show()

#2 bill_length and flipper_length
plt.scatter(P_Adelie["bill_length_mm"],P_Adelie["flipper_length_mm"],label="adelie")
plt.scatter(P_Gentoo["bill_length_mm"],P_Gentoo["flipper_length_mm"],label="gentoo")
plt.scatter(P_Chinstrap["bill_length_mm"],P_Chinstrap["flipper_length_mm"],label="chinstrap")
plt.title("bill length vs flipper length")
plt.xlabel("bill length")
plt.ylabel("flipper length")
plt.legend()
plt.show()

#3 bill_length and gender
plt.scatter(P_Adelie["bill_length_mm"],P_Adelie["gender"],label="adelie")
plt.scatter(P_Gentoo["bill_length_mm"],P_Gentoo["gender"],label="gentoo")
plt.scatter(P_Chinstrap["bill_length_mm"],P_Chinstrap["gender"],label="chinstrap")
plt.title("bill length vs gender")
plt.xlabel("bill length")
plt.ylabel("gender")
plt.legend()
plt.show()

#4 bill_length and body_mass_g
plt.scatter(P_Adelie["bill_length_mm"],P_Adelie["body_mass_g"],label="adelie")
plt.scatter(P_Gentoo["bill_length_mm"],P_Gentoo["body_mass_g"],label="gentoo")
plt.scatter(P_Chinstrap["bill_length_mm"],P_Chinstrap["body_mass_g"],label="chinstrap")
plt.title("bill length vs body mass")
plt.xlabel("bill length")
plt.ylabel("body mass")
plt.legend()
plt.show()

#5 bill_depth_mm and flipper_length
plt.scatter(P_Adelie["bill_depth_mm"],P_Adelie["flipper_length_mm"],label="adelie")
plt.scatter(P_Gentoo["bill_depth_mm"],P_Gentoo["flipper_length_mm"],label="gentoo")
plt.scatter(P_Chinstrap["bill_depth_mm"],P_Chinstrap["flipper_length_mm"],label="chinstrap")
plt.title("bill depth vs flipper length")
plt.xlabel("bill depth")
plt.ylabel("flipper length")
plt.legend()
plt.show()

#6 bill_depth_mm and gender
plt.scatter(P_Adelie["bill_depth_mm"],P_Adelie["gender"],label="adelie")
plt.scatter(P_Gentoo["bill_depth_mm"],P_Gentoo["gender"],label="gentoo")
plt.scatter(P_Chinstrap["bill_depth_mm"],P_Chinstrap["gender"],label="chinstrap")
plt.title("bill depth vs gender")
plt.xlabel("bill depth")
plt.ylabel("gender")
plt.legend()
plt.show()

#7 bill_depth_mm and body_mass_g
plt.scatter(P_Adelie["bill_depth_mm"],P_Adelie["body_mass_g"],label="adelie")
plt.scatter(P_Gentoo["bill_depth_mm"],P_Gentoo["body_mass_g"],label="gentoo")
plt.scatter(P_Chinstrap["bill_depth_mm"],P_Chinstrap["body_mass_g"],label="chinstrap")
plt.title("bill depth vs body mass")
plt.xlabel("bill depth")
plt.ylabel("body mass")
plt.legend()
plt.show()

#8 flipper_length and gender
plt.scatter(P_Adelie["flipper_length_mm"],P_Adelie["gender"],label="adelie")
plt.scatter(P_Gentoo["flipper_length_mm"],P_Gentoo["gender"],label="gentoo")
plt.scatter(P_Chinstrap["flipper_length_mm"],P_Chinstrap["gender"],label="chinstrap")
plt.title("flipper length vs gender")
plt.xlabel("flipper length")
plt.ylabel("gender")
plt.legend()
plt.show()

#9 flipper_length and body_mass_g
plt.scatter(P_Adelie["flipper_length_mm"],P_Adelie["body_mass_g"],label="adelie")
plt.scatter(P_Gentoo["flipper_length_mm"],P_Gentoo["body_mass_g"],label="gentoo")
plt.scatter(P_Chinstrap["flipper_length_mm"],P_Chinstrap["body_mass_g"],label="chinstrap")
plt.title("flipper length vs body mass")
plt.xlabel("flipper length")
plt.ylabel("body mass")
plt.legend()
plt.show()

#10 gender and body_mass_g
plt.scatter(P_Adelie["gender"],P_Adelie["body_mass_g"],label="adelie")
plt.scatter(P_Gentoo["gender"],P_Gentoo["body_mass_g"],label="gentoo")
plt.scatter(P_Chinstrap["gender"],P_Chinstrap["body_mass_g"],label="chinstrap")
plt.title("gender vs body mass")
plt.xlabel("gender")
plt.ylabel("body mass")
plt.legend()
plt.show()
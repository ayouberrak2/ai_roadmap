# =====================================================
# tuple est une liste non modifiable apres la creation 
# =====================================================



coordinates = (31.6295, -7.9811)

latitude = coordinates[0]
longitude = coordinates[1]

latitude, longitude = coordinates

print(latitude)
print(longitude)



# coordonnées géographiques ;
# dimensions ;
# configuration fixe ;
# résultat contenant plusieurs valeurs.



database_config = (
    "localhost",
    5432,
    "test",
)

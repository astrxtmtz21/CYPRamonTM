ARSU = 0
ARNO = 0
MERSU = 50000
ARCE = 0
for i in range (1, 13, 1):
    print(f"Mes { i }:")
    RNO = int(input("Promedio de lluvias del mes en la zona norte:"))
    RCE = int(input("Promedio de lluvias en la zona centro:"))
    RSU = int(input("Promedio de lluvias del mes en la zona sur:"))

    ARNO = ARNO + RNO # ARNO += RNO
    ARCE = ARCE + RCE
    ARSU = ARSU + RSU

    if RSU < MERSU:
          MERSU = RSU
          MES = 1
PRORCE = ARCE / 12
print(f"Promedio region centro: { PRORCE }")
print(f"Mes con menor lluvia region sur: { MES }")
print(f"Registro del mes: { MERSU }")

if ARNO > ARCE:
          if ARNO > ARSU:
              print(f"La region con mayor lluvia es la region norte")
          else:
              print(f"La region con mayor lluvia es la sur")
elif ARCE > ARSU:
    print(f"La region con mayor lluvia es la centro")
else:
    print(f"La region con la mayor lluvia es la sur")
        
          

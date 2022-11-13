import matplotlib.pyplot as plt
import math

# STRINGS
string_GGA = "GGA"
string_GLGSV = "GLGSV"
string_GPGSV = "GPGSV"
string_GNGSA = "GNGSA"
filename = "datos_fuera_lab.txt"
#filename = "datos_dentro_lab.txt"

# GGA VARIABLES
lines_gga = []
active_satellites = []
gps_mode = []
heights = 0
geoidal_separations = 0
latitudes = 0
longitudes = 0
hdop_values = 0

# GSV VARIABLES
lines_glgsv = []
lines_gpgsv = []
GP_satellites = []
GL_satellites = []
GP_elevations = []
GL_elevations = []
GP_azimuth = []
GL_azimuth = []
GP_snr = []
GL_snr = []

# GSA VARIABLES
gsa_counter = 0
lines_gsa = []
GSA_satellites_1 = []
GSA_satellites_2 = []
PDOP_1 = []
PDOP_2 = []
HDOP_1 = []
HDOP_2 = []
VDOP_1 = []
VDOP_2 = []

# OPEN DATA FILE
file = open(filename, 'r')
lines = file.readlines()

count = 0
gsa_count = 0
for line in lines:
    count+=1

    # Tramas GGA:
    if string_GGA in line:
        splitted_line = line.split(",")
        lines_gga.append(splitted_line)

        # GPS Quality indicator
        gps_mode.append(int(splitted_line[6]))

        # Number of satellites in use
        value = int(splitted_line[7])
        active_satellites.append(value)

        # Height over sea level
        height = float(splitted_line[9])
        heights += height

        # Geoidal separation
        geoidal_sep_value = float(splitted_line[11])
        geoidal_separations += geoidal_sep_value

        # Latitude
        latitude_value = float(splitted_line[2])
        latitudes += latitude_value
        latitude_pos = splitted_line[3]

        # Longitude
        longitude_value = float(splitted_line[4])
        longitudes += longitude_value
        longitude_pos = splitted_line[5]

        # Dilution of precision
        hdop_value = float(splitted_line[8])
        hdop_values += hdop_value

    # Tramas GLGSV:
    if string_GLGSV in line:
        splitted_line = line.split(",")
        lines_glgsv.append(splitted_line)

        # PRN
        prn = splitted_line[4]
        if prn in GL_satellites or prn == "":
            continue
        GL_satellites.append(prn)

        # Elevation
        elevation = splitted_line[5]
        GL_elevations.append(elevation)

        # Azimuth
        azimuth = splitted_line[6]
        GL_azimuth.append(azimuth)

        # SNR
        snr = splitted_line[7]
        GL_snr.append(snr)

        # Other PRNs:
        try:
            prn = splitted_line[8]
            if prn in GL_satellites or prn == "":
                continue
            elevation = splitted_line[9]
            azimuth = splitted_line[10]
            snr = splitted_line[11]
            GL_satellites.append(prn)
            GL_elevations.append(elevation)
            GL_azimuth.append(azimuth)
            GL_snr.append(snr)
        except Exception:
            pass

        try:
            prn = splitted_line[12]
            if prn in GL_satellites or prn == "":
                continue
            elevation = splitted_line[13]
            azimuth = splitted_line[14]
            snr = splitted_line[15]
            GL_satellites.append(prn)
            GL_elevations.append(elevation)
            GL_azimuth.append(azimuth)
            GL_snr.append(snr)
        except Exception:
            pass

        try:
            prn = splitted_line[16]
            if prn in GL_satellites or prn == "":
                continue
            elevation = splitted_line[17]
            azimuth = splitted_line[18]
            snr = splitted_line[19]
            GL_satellites.append(prn)
            GL_elevations.append(elevation)
            GL_azimuth.append(azimuth)
            GL_snr.append(snr)
        except Exception:
            pass

    # Tramas GPGSV:
    if string_GPGSV in line:
        splitted_line = line.split(",")
        lines_glgsv.append(splitted_line)

        # PRN
        prn = splitted_line[4]
        if prn in GP_satellites:
            continue
        GP_satellites.append(prn)

        # Elevation
        elevation = splitted_line[5]
        GP_elevations.append(elevation)

        # Azimuth
        azimuth = splitted_line[6]
        GP_azimuth.append(azimuth)

        # SNR
        snr = splitted_line[7]
        GP_snr.append(snr)

        # Other PRNs:
        try:
            prn = splitted_line[8]
            if prn in GP_satellites:
                continue
            elevation = splitted_line[9]
            azimuth = splitted_line[10]
            snr = splitted_line[11]
            GP_satellites.append(prn)
            GP_elevations.append(elevation)
            GP_azimuth.append(azimuth)
            GP_snr.append(snr)
        except Exception:
            pass

        try:
            prn = splitted_line[12]
            if prn in GP_satellites:
                continue
            elevation = splitted_line[13]
            azimuth = splitted_line[14]
            snr = splitted_line[15]
            GP_satellites.append(prn)
            GP_elevations.append(elevation)
            GP_azimuth.append(azimuth)
            GP_snr.append(snr)
        except Exception:
            pass

        try:
            prn = splitted_line[16]
            if prn in GP_satellites:
                continue
            elevation = splitted_line[17]
            azimuth = splitted_line[18]
            snr = splitted_line[19]
            GP_satellites.append(prn)
            GP_elevations.append(elevation)
            GP_azimuth.append(azimuth)
            GP_snr.append(snr)
        except Exception:
            pass

    # Tramas GNGSA:
    if string_GNGSA in line:
        gsa_count+=1
        splitted_line = line.split(",")
        lines_gsa.append(splitted_line)

        satellite = splitted_line[3:14]
        pdop = float(splitted_line[15])
        hdop = float(splitted_line[16])
        vdop = splitted_line[17]
        vdop = vdop.split("*")
        vdop = float(vdop[0])
        
        if count % 2 != 0: # impar -> grupo 1
            if satellite not in GSA_satellites_1:
                GSA_satellites_1.append(satellite)
            PDOP_1.append(pdop)
            HDOP_1.append(hdop)
            VDOP_1.append(vdop)

        else: # par -> grupo 2
            if satellite not in GSA_satellites_2:
                GSA_satellites_2.append(satellite)
            PDOP_2.append(pdop)
            HDOP_2.append(hdop)
            VDOP_2.append(vdop)

# Meaned values
final_height = heights / len(lines_gga)
final_height = "{:.2f}".format(final_height)

final_geoidal_separation = geoidal_separations / len(lines_gga)
final_geoidal_separation = "{:.2f}".format(final_geoidal_separation)

final_hdop = hdop_values / len(lines_gga)
final_hdop = "{:.2f}".format(final_hdop)

# Convert NMEA coordinates to decimal coordinates:
nmea_latitude = latitudes / len(lines_gga)
first_latitude_digits = nmea_latitude // 100
last_latitude_digits = nmea_latitude - (first_latitude_digits*100)
decimal_latitude = first_latitude_digits + (last_latitude_digits / 60)

nmea_longitude = longitudes / len(lines_gga)
first_longitude_digits = nmea_longitude // 100
last_longitude_digits = nmea_longitude - (first_longitude_digits*100)
decimal_longitude = first_longitude_digits + (last_longitude_digits / 60)

# Mean DOP magnitudes
final_PDOP_1 = sum(PDOP_1) / len(PDOP_1)
final_PDOP_2 = sum(PDOP_2) / len(PDOP_2)
final_HDOP_1 = sum(HDOP_1) / len(PDOP_1)
final_HDOP_2 = sum(HDOP_2) / len(HDOP_2)
final_VDOP_1 = sum(VDOP_1) / len(VDOP_1)
final_VDOP_2 = sum(VDOP_2) / len(VDOP_2)

# Print computed data
print("\n------------------------------------------------------------------------")
print("-                    DATOS OBTENIDOS DE TRAMAS GGA                     -")
print("------------------------------------------------------------------------")
print("Fichero leído: ", filename)
print("Talkers ID recibidos: GP (GPS), GL (GLONASS), GN (Mixed GPS & GLONASS)")
print("GPS Quality: ", set(gps_mode))
print("Número de satélites en uso: ", set(active_satellites))
print("Altura media sobre el nivel del mar del receptor GPS: ", final_height, "m")
print("Separación geoidal media: ", final_geoidal_separation, "m")
print("Coordenadas medias: ", decimal_latitude, latitude_pos, ", ", decimal_longitude, longitude_pos)
print("HDOP medio: ", final_hdop)




print("\n------------------------------------------------------------------------")
print("-                    DATOS OBTENIDOS DE TRAMAS GSV                     -")
print("------------------------------------------------------------------------")
for index, item in enumerate(GP_satellites):
    snr = GP_snr[index]
    if snr[0] == "*":
        GP_snr[index] = "XX"
    print("Satélite GP: "+item+" | Elevación: "+GP_elevations[index]+" | Azimuth: "+GP_azimuth[index]+" | SNR: "+GP_snr[index][0:2])

print("------------------------------------------------------------------------")

for index, item in enumerate(GL_satellites):
    snr = GL_snr[index]
    if snr[0] == "*":
        GL_snr[index] = "XX"
    print("Satélite GL: "+item+" | Elevación: "+GL_elevations[index]+" | Azimuth: "+GL_azimuth[index]+" | SNR: "+GL_snr[index][0:2])



print("\n------------------------------------------------------------------------")
print("-                    DATOS OBTENIDOS DE TRAMAS GSA                     -")
print("------------------------------------------------------------------------")
print("Grupos de satélites del grupo 1 de tramas GSA: ")
for satellite in GSA_satellites_1:
    print(satellite)

print("\nGrupos de satélites del grupo 2 de tramas GSA: ")
for satellite in GSA_satellites_2:
    print(satellite)
    
print("\nPDOP medio del grupo 1: ", final_PDOP_1)
print("PDOP medio del grupo 2: ", final_PDOP_2)
print("HDOP medio del grupo 1: ", final_HDOP_1)
print("HDOP medio del grupo 2: ", final_HDOP_2)
print("VDOP medio del grupo 1: ", final_VDOP_1)
print("VDOP medio del grupo 2: ", final_VDOP_2)

# Representación polar
GP_azimuts_rad = []
GL_azimuts_rad = []
GP_elevations_rad = []
GL_elevations_rad = []

for angle in GP_azimuth:
    GP_azimuts_rad.append(math.radians(float(angle)))

for angle in GL_azimuth:
    GL_azimuts_rad.append(math.radians(float(angle)))

for angle in GP_elevations:
    GP_elevations_rad.append((float(angle)))

for angle in GL_elevations:
    GL_elevations_rad.append((float(angle)))

fig = plt.figure()
ax = fig.add_subplot(projection="polar")
ax.set_theta_zero_location("N")
ax.set_xticklabels(["Norte", "NO", "Oeste", "SO", "Sur", "SE", "Este", "NE"])
c = ax.scatter(GL_azimuts_rad, GL_elevations_rad, c=GL_azimuts_rad, s=100, cmap="hsv", alpha=1)

for i in range(0, len(GL_azimuts_rad)):
    plt.annotate(GL_satellites[i]+" ["+GL_snr[i][0:2]+"dB]", (GL_azimuts_rad[i], GL_elevations_rad[i]))

plt.show()
plt.title("GPGSV dentro")
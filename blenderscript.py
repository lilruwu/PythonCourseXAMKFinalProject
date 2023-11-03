
with open('M5221.asc', 'r') as file:
    lines = file.readlines()

ncols = int(input("How many columns do you want to read?"))
nrows = int(input("How many rows do you want to read?"))
xllcorner = float(lines[2].split()[1])
yllcorner = float(lines[3].split()[1])
cellsize = float(lines[4].split()[1])
nodata_value = float(lines[5].split()[1])

height_data = []
for line in lines[6:6+nrows]:
    height_data.extend([float(value) for value in line.split()[:ncols]])

print('ncols: ', ncols, 'nrows: ', nrows, 'xllcorner: ', xllcorner, 'yllcorner: ', yllcorner, 'cellsize: ', cellsize, 'nodata_value: ', nodata_value)
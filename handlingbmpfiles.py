# OPEN BINARY FILE USING READ MODE
# START GO THROUGH BINARY FILE HEADER, READ THEM ONE BY ONE AND TRY TO UNDERSTAND

# let us open the binary file in read mode
# 1 nibble is 4 bits
# 1 byte is 8 bits
# 4 bytes is 32 bits
# 32 bits is Integer

# In BMP file, the first 14 bytes are referring to header
# First 2 bytes is for the file signature to tell what is this file

filename = "mypicture.bmp"
outputfilename = "brightmypicture.bmp"

with open(filename, "rb") as handler:
    file_header = handler.read(14)
    # file_header is an array of 14 bytes
    print(file_header, type(file_header)) # give us output in class bytes array
    # we read just 2 bytes we know it is Alphabet BM
    # so we used decode method (convert byte to string)
    file_type = file_header[0:2].decode() #output will be byte array which has b'....'
    print("File_type: ", file_type)
    # we read another 4 bytes which is file size
    # that is going to be an integer so cannot use decode method
    # however int is a class and its has a "class method" from_bytes
    # which means we can call the method using the class
    # using this we can convert byte to integer
    # file_size = file_header[2:6]
    file_size = int.from_bytes(file_header[2:6], 'little')
    print("File size: ", file_size)
    reserved_one = int.from_bytes(file_header[6:8], 'little')
    reserved_two = int.from_bytes(file_header[8:10], 'little')
    offset = int.from_bytes(file_header[10:14], 'little')
    print("Reserved one:", reserved_one)
    print("Reserved two:", reserved_two)
    print("Offset:", offset)

    dip_header = handler.read(40)
    dip_size = int.from_bytes(dip_header[0:4], 'little')
    print("DIP Size:", dip_size)
    width = int.from_bytes(dip_header[4:8], 'little')
    height = int.from_bytes(dip_header[8:12], 'little')
    print("Image Size in pixels:", width, "x", height)
    planes = int.from_bytes(dip_header[12:14], 'little')
    print("Planes:", planes)
    bit_count = int.from_bytes(dip_header[14:16], 'little') #how many bits we have in 1 row of data(pixels)
    print("Bits per pixel:", bit_count) # 1 pixel have 24 bits. # Each pixels have 3 bytes. 3 bytes is RGB colour. How many bytes we can read. Very important!

    # TO FIND HOW MANY BYTES WE NEED TO READ FROM THE FILE, TO READ AN ENTIRE ROW OF PIXELS
    # 819 * (24//3 bits) = 2457 Bytes
    # Each row is suppose to be divisible by 4 (this is called padding)
    # 2457 + 3 = 2460(divisible by 4) #simply add to 3 because 24 bits = 3 bytes
    
    # to find next number which is divisible by 4
    # (x + 3) & ~3
    # Mathematical function
    # Given number is 19 and find the next number which is divisible by 8..... Answer is 24
    # (givenNumber + (divisibleNumber - 1)) & ~(divisibleNumber - 1)
    # 26 & ~7
    # 26    00011010  &
    # ~7    11111000
    #       00011000
    
    row_size = ((width * (bit_count // 3)) + 3) & ~3
    print("Row size (in bytes): ", row_size)

    # READ ACTUAL PIXELS. START FROM OFFSET. BYTES NO 54
    # let us read the actual pixels
    handler.seek(offset) #now we are at the 54th byte
    pixel_data = []
    for index in range(height):
        row = handler.read(row_size)
        pixel_data.append(row)

bytes_per_pixes = bit_count // 8   #Answer 3 bytes
# Let us increase the brightness of the image
for y in range(height):
    # BMP images are read from bottoms to top(upside down)
    row = pixel_data[height - y - 1] # 459th row is the actual 1st row of the image
    new_row = bytearray()
    for x in range(width):
        start_index = x * bytes_per_pixes
        end_index = start_index + bytes_per_pixes
        pixel = row[start_index:end_index]
        if (len(pixel) == 3):
            b, g, r = pixel
            # Increase brightness
            r = min(255, int(r * 2))
            g = min(255, int(g * 2))
            b = min(255, int(b * 2))
            new_row.extend((b,g,r))
    pixel_data[height - y - 1] = new_row

with open(outputfilename, "wb") as handler:
    handler.write(file_header)
    handler.write(dip_header)
    for row in pixel_data:
        handler.write(row.ljust(row_size, b'\x00')) #row now is in string. Convert it to binary and in case if it is not having a correct size then you append it with 00.

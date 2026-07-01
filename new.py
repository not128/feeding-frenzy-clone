# import serial, turtle, time
# ard = serial.Serial('COM4', 115200)
# time.sleep(3)
# ard.write(b"RUN\n")
# turtle.colormode(255)
# t = turtle.Turtle()
# while True:
#     try:
#         line = ard.readline().decode('utf-8').strip()
#         if line:
#             tx, ty, bw = map(int,line.split())
#             bw = 255-bw
#         if bw>255:
#             bw = 255
#         elif bw <0:
#             bw = 0
#         t.color(bw, bw, bw)
#         t.penup()
#         t.goto(tx, ty)
#         t.pendown()
#         t.dot(10)
        
#     except ValueError:
#         pass
#     except serial.serialutil.SerialException:
#         pass
def triangulate_obj(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if line.startswith("f "):
            parts = line.strip().split()[1:]
            # If it's already a triangle, keep it
            if len(parts) == 3:
                new_lines.append(line)
            else:
                # Fan triangulation: split n-gon into triangles
                for i in range(1, len(parts)-1):
                    tri = f"f {parts[0]} {parts[i]} {parts[i+1]}\n"
                    new_lines.append(tri)
        else:
            new_lines.append(line)

    with open(output_file, "w") as f:
        f.writelines(new_lines)

# Usage
triangulate_obj("Untitled.obj", "triangulated.obj")

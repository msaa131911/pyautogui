import mouse as m
def clicked():
    if m.is_pressed(button="left"):
        m.release(button="left")
        return True

while True:
    if clicked()==True:
        print("ok")
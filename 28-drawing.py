for line in range(10):
    row = ""
    for cool in range(10):
        if line % 2 == 0:
         if cool % 2 == 0:
            row += " "
         else:
           row += "*"
        else:
            if cool % 2 == 0:
                row += "*"
            else:
                row += " "
    print(row)
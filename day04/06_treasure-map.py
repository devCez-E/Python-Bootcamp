#https://getemoji.com/

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = int(input("Where do you want to put the treasure? "))
column = int(position / 10)
row = position % 10

map[column - 1][row - 1] = "😈"
print(f"{row1}\n{row2}\n{row3}")
# from pathlib import Path

# path=Path("text-files") / "data1.txt"

# if path.exists():
#     with path.open("r",encoding="utf-8") as f:
#         print(f.read())
# else:
#     print("File not found...")




# from pathlib import Path
# print(Path.cwd())
# print(Path.cwd().parent)
# print(Path.cwd().parent.parent)



# from pathlib import Path
# print(Path.cwd())
# print(Path(__file__))



# from pathlib import Path

# path=Path(r"G:\1_Video_Learning\1_OnlineTraining\63_Python2026\Projects\MyProjects") / "README.md"
# print(path.exists())
# print(path.name)
# print(path.parent)
# print(path.suffix)


from pathlib import Path
path=Path(r"G:\1_Video_Learning\1_OnlineTraining\63_Python2026\Projects\MyProjects\DataStructures")

for item in path.iterdir():
    if item.is_file():
        print(item.name)





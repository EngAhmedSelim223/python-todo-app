filenames = ["1.Doc", "2.Report", "3.Presentation"]
new_list = [f"{x.replace(".", "-")}.txt" for x in filenames]
print(new_list)
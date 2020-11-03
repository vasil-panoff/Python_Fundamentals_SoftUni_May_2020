file_path = input().split("\\")

filename = file_path[-1]
file_name = filename.split('.')
file_name = file_name[0]

extension = filename.split('.')
extension = extension[-1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")

# ALT SOLUTION
# file_path = input().split("\\")[-1]
# file_name = file_path.split(".")[0]
# file_extencion = file_path.split(".")[1]
#
# print(f"File name: {file_name}")
# print(f"File extension: {file_extension}")

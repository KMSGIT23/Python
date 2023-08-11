input_files=["korean_national_anthem_1.txt", "korean_national_anthem_2.txt", "korean_national_anthem_3.txt", "korean_national_anthem_4.txt"]
output_file="output.txt"

paragraphs=[]
for file_path in input_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content=f.read()

        file_name_line=f"{file_path}\n----------------------------\n"
        paragraphs.append(file_name_line + content)

with open(output_file, 'w', encoding='utf-8') as f:
    for paragraph in paragraphs:
        f.write(paragraph + '\n\n')

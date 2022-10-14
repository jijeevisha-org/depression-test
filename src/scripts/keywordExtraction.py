my_file = open("negative-words.txt", "r", encoding="ISO-8859-1")
content = my_file.read()
content_list = content.split("\n")
my_file.close()
print(content_list)

s1 = set(message.split())
s2 = set(content_list)
s3 = s1.intersection(s2)
lst = list(s3)
lst_str = '%20'.join(lst)
print(lst_str)
link = "https://jijeevishaorg.gitlab.io/?q="
link = link+lst_str
print(link)

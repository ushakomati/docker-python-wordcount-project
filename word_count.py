import os
import socket

# Set file paths
data_dir = "/a2"
if_file = os.path.join(data_dir, "IF.txt")
lim_file = os.path.join(data_dir, "Limerick.txt")
output_file = "/a2/result.txt"

# a. List name of all the text files at location: /home/data
file_list = os.listdir(data_dir)

# b. Read the two text files and count total number of words in each text files
def count_words(file_path):
    with open(file_path, "r") as file:
        contents = file.read()
        words = contents.split()
        return len(words)

if_word_count = count_words(if_file)
lim_word_count = count_words(lim_file)

# c. Add all the number of words to find the grand total (total number of words in both files)
total_word_count = if_word_count + lim_word_count

# d. List the top 3 words with maximum number of counts in IF.txt. Include the word counts for the top 3 words.
def top_words(file_path, n):
    with open(file_path, "r") as file:
        contents = file.read()
        words = contents.split()
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        top_n_words = sorted_word_counts[:n]
        return top_n_words

if_top_words = top_words(if_file, 3)

# e. Find the IP address of your machine
ip_address = socket.gethostbyname(socket.gethostname())

# f. Write all the output to a text file at location: /home/output/result.txt (inside your container)
with open(output_file, "w") as file:
    file.write(f"File list: {file_list}\n")
    file.write(f"IF word count: {if_word_count}\n")
    file.write(f"Limerick word count: {lim_word_count}\n")
    file.write(f"Total word count: {total_word_count}\n")
    file.write(f"Top 3 words in IF.txt: {if_top_words}\n")
    file.write(f"IP address: {ip_address}\n")

# g. Upon running your container, it should do all the above stated steps and print the information on console from result.txt file and exit.
with open(output_file, "r") as file:
    contents = file.read()
    print(contents)

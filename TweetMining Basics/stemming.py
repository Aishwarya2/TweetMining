from nltk.stem import RegexpStemmer
st = RegexpStemmer('ing$|s$|e$|able$|ly$', min=4)
file_name = "sriram.yml"
string_to_add = ": [sriram]"
string = "accurating"
with open(file_name, 'r+') as f:
    for line in f:
        print (line)
        st.stem(line)
        f.write(line)
print (st.stem(string))


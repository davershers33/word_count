def readfile(filename):
    with open("./story.txt.docx", "r") as openfile:
        read_file = openfile.read()
        
def countwords():
    text=readfile("./story.txt")
    split_text=text.split()

    count={}
    for i in split_text:
        if i in count:
            count[i]+=1
    else:
        count[i]=1
    return count


print(countwords)
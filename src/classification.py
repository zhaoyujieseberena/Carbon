import json



file = open("./Classification/Target_Problem.md", 'w')
with open('./.github/citation/citation.json', 'r') as f:
        citation = json.load(f)

path = './res/papers.json'
    
with open(path, 'r') as f:
            table = json.load(f)
            
            file.write("### {}\n".format('Review'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :----: | :---------: | :---: |\n")
            for paper in table:
                if "Review" in paper["Target Problem"]:
                    file.write("|{} <br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("\n")
            file.write("### {}\n".format('Optimation'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :------: | :---------: | :---: |\n")
            for paper in table:
                if "Optimation" in paper["Target Problem"]:
                    file.write("|{}<br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("|\n")
            file.write("### {}\n".format('Calculation'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :------: | :---------: | :---: |\n")
            for paper in table:
                if "Calculation" in paper["Target Problem"]:
                    file.write("|{}<br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("|\n")
            file.write("### {}\n".format('Standardization'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :------: | :---------: | :---: |\n")
            for paper in table:
                if "Standardization" in paper["Target Problem"]:
                    file.write("|{} <br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")


file.close()



file = open("./Classification/Computer_system_stack.md", 'w')


with open('./.github/citation/citation.json', 'r') as f:
        citation = json.load(f)

path = './res/papers.json'
    
with open(path, 'r') as f:
            table = json.load(f)
            
            file.write("### {}\n".format('Review'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :----: | :---------: | :---: |\n")
            for paper in table:
                if "Review" in paper["Target Problem"]:
                    file.write("|{} <br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("\n")
            file.write("### {}\n".format('Optimation'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :------: | :---------: | :---: |\n")
            for paper in table:
                if "Optimation" in paper["Target Problem"]:
                    file.write("|{}<br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("|\n")
            file.write("### {}\n".format('Calculation'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :------: | :---------: | :---: |\n")
            for paper in table:
                if "Calculation" in paper["Target Problem"]:
                    file.write("|{}<br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("|\n")
            file.write("### {}\n".format('Standardization'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :------: | :---------: | :---: |\n")
            for paper in table:
                if "Standardization" in paper["Target Problem"]:
                    file.write("|{} <br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")



file.close()



file = open("./Classification/Hardware_system.md", 'w')
with open('./.github/citation/citation.json', 'r') as f:
        citation = json.load(f)

path = './res/papers.json'
    
with open(path, 'r') as f:
            table = json.load(f)
            
            file.write("### {}\n".format('Datacenter'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :----: | :---------: | :---: |\n")
            for paper in table:
                if "Datacenter" in paper["Hardware system"]:
                    file.write("|{} <br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("\n")
            file.write("### {}\n".format('Edge'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :------: | :---------: | :---: |\n")
            for paper in table:
                if "Edge" in paper["Hardware system"]:
                    file.write("|{}<br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("|\n")
            file.write("### {}\n".format('Mobile'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :------: | :---------: | :---: |\n")
            for paper in table:
                if "Mobile" in paper["Hardware system"]:
                    file.write("|{}<br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("|\n")
            file.write("### {}\n".format('TinyML'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :------: | :---------: | :---: |\n")
            for paper in table:
                if "TinyML" in paper["Hardware system"]:
                    file.write("|{} <br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")


file.close()




file = open("./Classification/Included_carbon_life_cycle_stage(s).md", 'w')
with open('./.github/citation/citation.json', 'r') as f:
        citation = json.load(f)

path = './res/papers.json'
    
with open(path, 'r') as f:
            table = json.load(f)
            
            file.write("### {}\n".format('Manufacturing'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :----: | :---------: | :---: |\n")
            for paper in table:
                if "Manufacturing" in paper["Included carbon life cycle stage(s)"]:
                    file.write("|{} <br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("\n")
            file.write("### {}\n".format('Operation'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :------: | :---------: | :---: |\n")
            for paper in table:
                if "Operation" in paper["Included carbon life cycle stage(s)"]:
                    file.write("|{}<br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            

            file.write("\n")
            file.write("### {}\n".format('End-of-life'))
            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :------: | :---------: | :---: |\n")
            for paper in table:
                if "End-of-life" in paper["Included carbon life cycle stage(s)"]:
                    file.write("|{} <br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

file.close()
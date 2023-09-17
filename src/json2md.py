# %%
import json
import os

def load_head(file):
    with open("./res/head.md", 'r') as f:
        for line in f:
            file.write(line)
        file.write("\n")

def load_content(file):
    file.write("## Contents\n")
    file.write("- [Exisiting metrics](##Exisiting metrics)\n")
    file.write("- [Useful Links](##Useful Links)\n")
    file.write("  - [Estimation parameters](###Estimation parameters)\n")
    file.write("  - [Tools](###Tools)\n")
    #file.write("  - [Calculation](###Calculation)\n")
    file.write("- [Papers](##papers)\n")
    file.write("  - [Review](###Review)\n")
    file.write("  - [Optimation](###Optimation)\n")
    file.write("  - [Calculation](###Calculation)\n")
    file.write("  - [Standardization](###Standardization)\n")
    file.write("\n")
'''

    path = 'res/papers.json'
    

    for pf in sorted(os.listdir(path)):
        if not pf.endswith(".json"):
            continue
        with open(os.path.join(path, pf), 'r') as f:
            title = json.load(f)['title']
            file.write("  - [{}](#{})\n".format(title, title.lower().replace(' ', '-')))

    file.write("- [Contribute](#contribute)\n")
'''
def load_lib(file):
    file.write("## Open Source Libraries\n")
    with open("res/library.json", 'r') as f:
        libraries = json.load(f)
    for lib in libraries:
        name = lib['name']
        source = lib['source']
        repo = source.split('github.com/', 1)[1]
        file.write("- [{}]({}) ![GitHub stars](https://img.shields.io/github/stars/{}.svg?logo=github&label=Stars)\n".format(name, source, repo))

def load_paper(file):
    file.write("## Papers\n")

    with open('./.github/citation/citation.json', 'r') as f:
        citation = json.load(f)

    path = './res/papers.json'
    
    with open(path, 'r') as f:
            table = json.load(f)
            
            file.write("| Metric | Target problem | Computer system stack | Hardware system | Carbon life cycle stage(s) | \n")
            file.write("| :---: | :----: | :------: | :------: | :--------: | \n")
            j=0

            for metric in table:
                j+=1
                file.write("|[{}](#paper{})".format(j,j))
                choose(file,metric['Target Problem'])
                file.write("|{}".format(j))
                #choose(file,metric['Computer system stack '])
                choose(file,metric['Hardware system'])
                
                choose(file,metric['Included carbon life cycle stage(s)'])
                file.write("|\n")
            file.write("\n")

            file.write("| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :----: | :---------: | :---: |\n")
            
            j=0
            for paper in table:
                    j+=1
                    file.write("<a name='paper{}'></a>".format(j))
                    file.write("|{} <br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite =1
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("|\n")

        

            '''
                file.write("- [**{}**]".format(paper['venue']))
                file.write(" {}".format(paper['name']))
                file.write(" (*{}*)".format(paper['affiliation']))
                if 'link' in paper:
                    file.write(" [[paper]]({})".format(paper['link']))
                    cite = citation[paper['name']]['citation']
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                if 'source' in paper:
                    source = paper['source']
                    file.write(" [[code]]({})".format(source))
                    repo = source.split('github.com/', 1)[1]
                    if repo.count('/') == 1:
                        file.write("![GitHub stars](https://img.shields.io/github/stars/{}.svg?logo=github&label=Stars)".format(repo))

                file.write("\n")
                '''
def load_legend(file):
    
    with open("./res/legend.md", 'r') as f:
        for line in f:
            file.write(line)
    

def choose(file,string):
    file.write("|")
    if 'Optimation' in string:
        file.write("[![1](images/square1.svg)]()")
    if 'Application' in string:
        file.write("[![1](images/square5.svg)]()")
    if 'Datacenter' in string:
        file.write("[![1](images/square.svg)]()")
    if 'Manufacturing' in string:
        file.write("[![1](images/square6.svg)]()")
    if 'Modeling' in string:
        file.write("[![1](images/star1.svg)]()")
    if 'OS' in string:
        file.write("[![1](images/star5.svg)]()")
    if 'Edge' in string:
        file.write("[![1](images/star.svg)]()")
    if 'Operation' in string:
        file.write("[![1](images/star6.svg)]()")
    if 'Standardization' in string:
        file.write("[![1](images/stop-circle1.svg)]()")
    if 'Microarchitecture' in string:
        file.write("[![1](images/stop-circle5.svg)]()")
    if 'Mobile' in string:
        file.write("[![1](images/stop-circle.svg)]()")
    if 'End-of-life' in string:
        file.write("[![1](images/stop-circle6.svg)]()")
    if 'Review' in string:
        file.write("[![1](images/target1.svg)]()")
    if 'Infrastructure' in string:
        file.write("[![1](images/target5.svg)]()")
    if 'Tiny' in string:
        file.write("[![1](images/target.svg)]()")
    
 

def load_metrics(file):

    file.write("## Metrics\n")

    

    path = './res/metrics.json'
    
    with open(path, 'r') as f:
            table = json.load(f)
            
            
            file.write("| Metric | Computer system stack | Hardware system | Carbon life cycle stage(s) | \n")
            file.write("| :---: | :------: | :------: | :--------: | \n")
            for metric in table:
                file.write("|{}".format(metric['Metric']))
                choose(file,metric['Computer_stack'])
                choose(file,metric['Hardware system'])
                choose(file,metric['Included carbon life cycle stage(s)'])
                file.write("|\n")

            file.write("\n")
            file.write("| Metric | Description | Link |  \n")
            file.write("| :---: | :--------: | :----: | \n")

            for metric in table:
                
                    file.write("|{}|".format(metric['Metric']))
                    file.write("{}|".format(metric['Description']))
                    
                    file.write(" [[Paper]]({})".format(metric['Link']))
                    file.write("|")
                    file.write("\n")
                    
           


    
    


def load_others(file):
    file.write("\n")
    with open("./res/Links.md", 'r') as f:
        for line in f:
            file.write(line)

def load_contribute(file):
    with open("./res/contribute.md", 'r') as f:
        for line in f:
            file.write(line)


file = open("./test.md", 'w')

load_head(file)
load_content(file)
load_legend(file)
load_metrics(file)
#load_lib(file)
load_others(file)
load_paper(file)
load_contribute(file)

file.close()


# %%




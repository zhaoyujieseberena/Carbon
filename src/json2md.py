# %%
import json
import os

def load_head(file):
    with open("./res/head.md", 'r') as f:
        for line in f:
            file.write(line)
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

def load_report(file):
    file.write("## Reports\n")

    path = './res/Report.json'
    
    with open(path, 'r') as f:
            table = json.load(f)
            
            file.write("| Description | Link | Computer system stack | Hardware system | Carbon life cycle stage(s) | \n")
            file.write("| :---: | :----: | :------: | :------: | :--------: | \n")
            j=0

            for metric in table:
                j+=1
                
                file.write("|{}".format(metric['Description']))
                
                file.write(" |[[Link]]({})".format(metric['Link']))
                choose(file,metric['Computer system stack '])
                choose(file,metric['Hardware system'])
                
                choose(file,metric['Included carbon life cycle stage(s)'])
                file.write("|\n")
            file.write("\n")

    

        

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




def load_Link(file):
    file.write("## Links\n")

    path = './res/Link.json'
    
    with open(path, 'r') as f:
            table = json.load(f)
            
            file.write("| ID | Name  | Target problem | Computer system stack | Hardware system | Carbon life cycle stage(s) | \n")
            file.write("| :---: | :---: | :----: | :------: | :------: | :--------: | \n")
            j=0

            for metric in table:
                j+=1
                file.write("|[{}](#Link{})".format(j,j))
                file.write("|{}".format(metric['Name']))
                choose(file,metric['Target Problem'])
                
                choose(file,metric['Computer system stack '])
                choose(file,metric['Hardware system'])
                
                choose(file,metric['Included carbon life cycle stage(s)'])
                file.write("|\n")
            file.write("\n")

            file.write("| ID | Name | Link  | Paperlink | Description | \n")
            file.write("| :-: | :-: | :-: | :----: | :---------: |\n")
            
            j=0
            for paper in table:
                    j+=1
                    file.write("|{}<a name='Link{}'></a>".format(j,j))
                    file.write("|{}".format(metric['Name']))
                    file.write(" |[[Link]]({})".format(paper['Link']))
                   
                    
                    file.write(" |[[paper]]({})".format(paper['Paper Link']))
                    file.write("|{}".format(paper['Description']))
                    file.write("|")
                    file.write("\n")

            file.write("\n")

        

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




def load_paper(file):
    file.write("## Papers\n")

    with open('./.github/citation/citation.json', 'r') as f:
        citation = json.load(f)

    path = './res/papers.json'
    
    with open(path, 'r') as f:
            table = json.load(f)
            
            file.write("| Link | Target problem | Computer system stack | Hardware system | Carbon life cycle stage(s) | \n")
            file.write("| :---: | :----: | :------: | :------: | :--------: | \n")
            j=0

            for metric in table:
                j+=1
                file.write("|[{}](#paper{})".format(j,j))
                choose(file,metric['Target Problem'])
                
                choose(file,metric['Computer system stack '])
                choose(file,metric['Hardware system'])
                
                choose(file,metric['Included carbon life cycle stage(s)'])
                file.write("|\n")
            file.write("\n")

            file.write("| ID | Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :-: | :----: | :---------: | :---: |\n")
            
            j=0
            for paper in table:
                    j+=1
                    file.write("{}<a name='paper{}'></a>".format(j,j))
                    file.write("|{} <br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite = citation[paper['Title']]['citation']
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("\n")

        

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
    if 'Optimization' in string:
        file.write("[![1](image/Optimization.svg) Opt ](Classification/Target_Problem.md#Optimization)")
    if 'Application' in string:
        file.write("[![1](image/App.svg) App ](Classification/Computer_system_stack.md#Application)")
    if 'Datacenter' in string:
        file.write("[![1](image/center.svg) DC ](Classification/Hardware_system.md#Datacenter)")
    if 'Manufacturing' in string:
        file.write("[![1](image/Manufacturing.svg) MF ](Classification/Included_carbon_life_cycle_stage(s).md#Manufacturing)")
    if 'Modeling' in string:
        file.write("[![1](image/Modeling.svg) Modeling ](Classification/Target_Problem.md#Modeling)")
    if 'OS' in string:
        file.write("[![1](image/OS.svg) OS ](Classification/Computer_system_stack.md#OS)")
    if 'Edge' in string:
        file.write("[![1](image/Edge.svg) Edge ](Classification/Hardware_system.md#Edge.md)")
    if 'Operation' in string:
        file.write("[![1](image/Operation.svg) Op ](Classification/Included_carbon_life_cycle_stage(s).md#Operation)")
    if 'Standardization' in string:
        file.write("[![1](image/Stand.svg) Stand. ](Classification/Target_Problem.md#Standardization)")
    if 'Microarchitecture' in string:
        file.write("[![1](image/Micro.svg) Micro. ](Classification/Computer_system_stack.md#Microarchitecture)")
    if 'Mobile' in string:
        file.write("[![1](image/Mobile.svg) Mobile ](Classification/Hardware_system.md#Mobile)")
    if 'End-of-life' in string:
        file.write("[![1](image/End-of-life.svg) E-o-l ](Classification/Included_carbon_life_cycle_stage(s).md#End-of-life)")
    if 'Review' in string:
        file.write("[![1](image/Review.svg) Review ](Classification/Target_Problem.md#Review)")
    if 'Infrastructure' in string:
        file.write("[![1](image/Infrastructure.svg) Infra ](Classification/Computer_system_stack.md#Infrastructure)")
    if 'Tiny' in string:
        file.write("[![1](image/Tiny.svg) Tiny ](Classification/Hardware_system.md#Tiny)")
    if 'Device' in string:
        file.write("[![1](image/Drive.svg) Device&Tech ](Classification/Hardware_system.md#Tiny)")
    if 'Circuit' in string:
        file.write("[![1](image/Circuit.svg) Circuit](Classification/Hardware_system.md#Tiny)")
    
 

def load_metrics(file):

    file.write("## Metrics\n")

    

    path = './res/metrics.json'
    
    with open(path, 'r') as f:
            table = json.load(f)
            
            
            file.write("| Paper| Computer system stack | Hardware system | Carbon life cycle stage(s) | Equation | \n")
            file.write("| :---: | :------: | :------: | :--------: | :------: |\n")
            for metric in table:
                file.write("|{}".format(metric['Metric']))
                choose(file,metric['Computer_stack'])
                choose(file,metric['Hardware system'])
                choose(file,metric['Included carbon life cycle stage(s)'])
                file.write("|{}".format(metric['Equation']))
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
                    
           


    
    



def load_contribute(file):
    with open("./res/contribute.md", 'r') as f:
        for line in f:
            file.write(line)


file = open("./Readme.md", 'w')

load_head(file)

load_legend(file)
load_Link(file)
load_report(file)
load_metrics(file)
#load_lib(file)
load_paper(file)
load_contribute(file)

file.close()


# %%



